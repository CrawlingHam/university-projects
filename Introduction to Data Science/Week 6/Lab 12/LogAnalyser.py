import pandas as pd

class LogAnalyser:
    def __init__(self):
        self.data = []
        self.player_names = []
        self.df = pd.DataFrame()

    def load_file(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
        for line in lines:
            # Example line: "Round 1: a rolled 1, b rolled 2, c rolled 3"
            try:
                _round_part, rolls_part = line.strip().split(":", 1)
            except ValueError:
                continue # skip malformed lines
            rolls_dict = {}
            for part in rolls_part.split(","):
                part = part.strip() # remove spaces
                if " rolled " in part:
                    name, _, roll = part.partition(" rolled ")
                    rolls_dict[name] = int(roll)
                    if name not in self.player_names:
                        self.player_names.append(name)
            self.data.append(rolls_dict)
        # Convert list of dicts to DataFrame
        self.df = pd.DataFrame(self.data, columns=self.player_names)
        self.df.index += 1 # rounds starting from 1
        self.df.index.name = "Round"


log_analyser = LogAnalyser()
filename = "Week 6/Lab 12/results.txt" # results.txt file is in Week 6/Lab 12 folder (same as LogAnalyser.py)
log_analyser.load_file(filename)

# print(f"Data frame \n{log_analyser.df}\n")
# print(f"Data frame head \n{log_analyser.df.head(2)}\n")
# print(f"Data frame info \n{log_analyser.df.info()}\n")
# print(f"Data frame description \n{log_analyser.df.describe()}\n")
print(f"Data frame shape \n{log_analyser.df.shape}\n")