from typing import TypeVar, Callable, Literal
from abc import ABC, abstractmethod
import pandas as pd
import random
import sys
import os

# Custom types
T = TypeVar("T")
FileMode = Literal["r", "w"]

class Conversion:
    def to(self, prompt: str, err_msg: str, cast_type: Callable[[str], T] = int, exit_on_fail: bool = False, additional_checks: Callable[[T], bool] = lambda x: True) -> T:
        try:
            casted_type = cast_type(input(prompt))
            if not additional_checks(casted_type): 
                raise ValueError(err_msg)
            return casted_type
        except ValueError:
            print(err_msg)
            if exit_on_fail:
                sys.exit(1)
            else:
                return self.to(prompt, err_msg, cast_type, exit_on_fail, additional_checks)

    def to_int(self, prompt: str, err_msg: str, exit_on_fail: bool = False, additional_checks: Callable[[int], bool] = lambda x: True) -> int:
        return self.to(prompt, err_msg, int, exit_on_fail, additional_checks)

    def to_str(self, prompt: str, err_msg: str, exit_on_fail: bool = False, additional_checks: Callable[[str], bool] = lambda x: True) -> str:
        return self.to(prompt, err_msg, str, exit_on_fail, additional_checks)

class LogAnalyser:
    def __init__(self) -> None:
        self.data: list[dict[str, int]] = []
        self.conversion = Conversion()
        self.dataframe = pd.DataFrame()

    def get_filename(self, prompt: str) -> str:
        return self.conversion.to_str(prompt, "Invalid file path. Please enter a valid file path.", additional_checks=lambda x: x.endswith(".txt"))

    def get_save_dir(self, folder_name: str) -> str:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(script_dir, folder_name)

    def load(self, folder_name: str, filename: str) -> pd.DataFrame:
        save_dir = self.get_save_dir(folder_name)
        file_path = os.path.join(save_dir, filename)

        try:
            with open(file_path, "r") as file:
                content = file.read()
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found in '{folder_name}' folder")
            return pd.DataFrame()
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            return pd.DataFrame()
        
        self.player_names = []
        self.data = []
        
        lines = content.split('\n')
        for line in lines:
            if line.startswith("Round") and ":" in line:
                try:
                    _round_part, rolls_part = line.strip().split(":", 1)
                    rolls_dict = {}
                    for part in rolls_part.split(","):
                        part = part.strip()
                        if " rolled " in part:
                            name, _, roll = part.partition(" rolled ")
                            rolls_dict[name] = int(roll)
                            if name not in self.player_names:
                                self.player_names.append(name)
                    self.data.append(rolls_dict)
                except ValueError:
                    continue
        
        if self.data:
            self.dataframe = pd.DataFrame(self.data, columns=self.player_names)
            self.dataframe.index += 1
            self.dataframe.index.name = "Round"
            return self.dataframe
        else:
            return pd.DataFrame()

    def save(self, prompt: str, folder_name: str, content: str, mode: FileMode = "w", log_success: bool = True) -> str:
        save_dir = self.get_save_dir(folder_name)
        os.makedirs(save_dir, exist_ok=True)

        filename = self.get_filename(prompt)
        file_path = os.path.join(save_dir, filename)
        
        with open(file_path, mode) as file:
            file.write(content)

        if log_success:
            print(f"Results saved to {file_path}")

        return filename

class Dice:
    def __init__(self, sides: int) -> None:
        self.sides = sides

    def roll(self) -> int:
        return random.randint(1, self.sides)

class Person(ABC):
    def __init__(self, name: str, address: str, email: str, phone_number: str, country: str) -> None:
        self.phone_number = phone_number
        self.address = address
        self.country = country
        self.email = email
        self.name = name
    
    @abstractmethod
    def get_details(self) -> str:
        pass

class Player(Person):
    def __init__(self, name: str, address: str, email: str, phone_number: str, country: str) -> None:
        super().__init__(name, address, email, phone_number, country)
        self.rolls: list[int] = []
        self.wins = 0

    def get_details(self) -> str:
        return f"Name: {self.name}\n* Address: {self.address}\n* E-mail: {self.email}\n* Phone: {self.phone_number}\n* Country: {self.country}\n* Wins: {self.wins}\n"

class Game:
    def __init__(self) -> None:
        self.default_int_prompt_err_msg: str = "Invalid input. Please enter a valid number."
        self.default_str_prompt_err_msg: str = "Invalid input. Please enter a valid input."
        self.results_folder_name: str = "results"
        self.log_analyser = LogAnalyser()
        self.players: list[Player] = []
        self.conversion = Conversion()
        self.game_over: bool = False
        self.round = 0

    def set_game_over(self, game_over: bool) -> None:
        self.game_over = game_over

    def get_dice(self) -> None:
        dice_sides = self.conversion.to_int("Enter the number of sides of the dice: ", self.default_int_prompt_err_msg)
        self.dice = Dice(dice_sides)

    def get_score_to_win(self) -> None:
        self.score_to_win = self.conversion.to_int("Enter the score to win: ", self.default_int_prompt_err_msg)

    def get_players(self) -> list[Player]:
        num_players: int = self.conversion.to_int("Enter the number of players: ", self.default_int_prompt_err_msg)
        
        for i in range(num_players):
            name = self.conversion.to_str(f"Enter the name of player {i+1}: ", self.default_str_prompt_err_msg)
            address = self.conversion.to_str(f"Enter the address of player {i+1}: ", self.default_str_prompt_err_msg)
            email = self.conversion.to_str(f"Enter the email of player {i+1}: ", self.default_str_prompt_err_msg)
            phone_number = self.conversion.to_str(f"Enter the phone number of player {i+1}: ", self.default_str_prompt_err_msg)
            country = self.conversion.to_str(f"Enter the country of player {i+1}: ", self.default_str_prompt_err_msg)
            player = Player(name, address, email, phone_number, country)
            self.players.append(player)

        return self.players

    def should_play_again(self) -> bool:
        should_play_again = self.conversion.to_str("Do you want to play again? (y/n): ", self.default_str_prompt_err_msg)
        return should_play_again.lower().startswith("y")

    def get_players_details(self) -> str:
        players_details: str = "Player Information:\n"
        for each_player in self.players:
            players_details += each_player.get_details() + "\n"
        return players_details

    def get_game_rounds(self) -> str:
        game_rounds: str = "Game rounds:\n"

        for r in range(self.round + 1):
            rolls_str = ""
            for i, each_player in enumerate(self.players):
                rolls_str += f"{each_player.name} rolled {each_player.rolls[r]}"
                if i < len(self.players) - 1:
                    rolls_str += ", "
            game_rounds += f"Round {r+1}: {rolls_str}\n"

        return game_rounds

    def get_results(self) -> str:
        results: str = self.get_players_details()
        results += f"\n{self.get_game_rounds()}"
        return results

    def play(self) -> None:
        while True:
            print(f"Round {self.round+1}:")
            current_rolls: list[int] = []
            
            for each_player in self.players:
                roll = self.dice.roll()
                each_player.rolls.append(roll)
                current_rolls.append(roll)
                print(f"Player {each_player.name} rolled: {roll}")
            
            max_roll = max(current_rolls)
            winners: list[str] = []
            
            # Check for winners of this round
            for each_player in self.players:
                if(each_player.rolls[-1] == max_roll):
                    each_player.wins += 1
                    winners.append(each_player.name)
            
            # Print winners and handle multiple winners of round
            if len(winners) == 1:
                print(f"Winner of this round is: {winners[0]}")
            else:
                print(f"Winners of this round are: {' and '.join(winners)}")
            print("Current scores:", {player.name: player.wins for player in self.players})
            
            for each_player in self.players:
                if(each_player.wins >= self.score_to_win):
                    print(f"\n {each_player.name} is the newest Battle of Dices Champion!")
                    self.set_game_over(True)
                    break
            
            if self.game_over or not self.should_play_again():
                print("Game over!")
                break
            
            self.round += 1
            self.set_game_over(False)

        filename = self.log_analyser.save("Enter the file path to save the results (file must be a .txt file): ", self.results_folder_name, self.get_results(), mode="w", log_success=True)

        should_show_history = self.conversion.to_str("Do you want to show the game history? (y/n): ", self.default_str_prompt_err_msg, additional_checks=lambda x: x.lower().startswith("y"))
        if should_show_history:
            self.log_analyser.load(self.results_folder_name, filename)
            print(self.log_analyser.dataframe)

    def start(self) -> None:
        self.get_dice()
        self.get_score_to_win()
        self.get_players()
        self.play()

if __name__ == "__main__":
    game = Game()
    game.start()