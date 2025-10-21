from src.model.main import Model
from src.menu.main import Menu

def main():
    model = Model()

    menu = Menu(load_file=lambda file_name: model.loading_data(file_name))
    menu.start()

if __name__ == "__main__":
    main()