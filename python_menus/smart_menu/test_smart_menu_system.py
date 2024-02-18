from MenuManager import MenuManager
# Initialization code - This is a simplification
if __name__ == "__main__":
    config_path = "/home/adamsl/linuxBash/python_menus/smart_menu/config.json"  # Path to your sample config file
    menu_manager = MenuManager(config_path)
    menu_manager.load_menus()  # Assuming this method parses config.json and initializes menus
    menu_manager.display_menu("main")  # Display the main menu, handle user input
