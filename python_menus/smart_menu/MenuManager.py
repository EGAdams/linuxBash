from ConfigReader import ConfigReader
from Menu import Menu
from MenuItem import MenuItem
from CommandExecutor import CommandExecutor
import json
import shutil
import os

class MenuManager:
    def __init__(self, menu, config_path):
        self.menu = menu
        self.config_path = config_path

    def load_menus(self):
        """Loads the menu items from the configuration file."""
        config_data = ConfigReader.read_config(self.config_path)
        for item_config in config_data:
            menu_item = MenuItem(
                title=item_config['title'],
                action=item_config['action'],
                working_directory=item_config.get('workingDirectory', ''),
                open_in_subprocess=item_config.get('openInSubprocess', False),
                use_expect_library=item_config.get('useExpectLibrary', False)
            )
            self.menu.add_item(menu_item)

    def display_menu(self):
        """Displays the menu and handles user input."""
        while True:
            # self.menu.display_and_select()
            choice = input("Please select an option: ")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(self.menu.items):
                    self.menu.items[choice - 1].execute()
                elif choice == len(self.menu.items) + 1:
                    break  # Exit the menu
                elif choice == len(self.menu.items) + 2:
                    self.add_menu_item()
            else:
                print("Invalid selection. Please try again.")

    def add_menu_item(self):
        """Collects information from the user to add a new menu item."""
        print("Adding a new menu item...")
        title = input("Enter the title for the new menu item: ")
        action = input("Enter the command to execute: ")
        working_directory = input("Enter the full path to the directory: ")
        open_in_subprocess_str = input("Should this command open in a separate window (yes/no)? ")
        use_expect_library_str = input("Should use the Expect library (yes/no)? ")

        open_in_subprocess = open_in_subprocess_str.lower() == 'yes'
        use_expect_library = use_expect_library_str.lower() == 'yes'

        new_menu_item = MenuItem(title, action, working_directory, open_in_subprocess, use_expect_library)
        self.menu.add_item(new_menu_item)
        print("New menu item added successfully.")
        self.save_menus_to_config()

    def save_menus_to_config(self):
        """Serializes and saves the menu structure to the configuration file."""
        config_data = [item.to_dict() for item in self.menu.items]
        with open(self.config_path, 'w') as config_file:
            json.dump(config_data, config_file, indent=4)
        print("Menu configuration saved.")

    def save_to_config(self):
        """Saves the current menu configuration to a file."""
        with open(self.config_path, 'w') as config_file:
            json.dump(self.menu.to_dict_list(), config_file, indent=4)
        print("Menu configuration saved.")
        
    # def add_new_item(self):
    #     # Existing code to add a new item
    #     self.menu.add_item(new_item)
    #     print("New menu item added successfully.")
    #     # Save the updated menu configuration
    #     self.save_to_config()

def main():
    menu = Menu()
    menu_manager = MenuManager(menu, "path_to_config.json")
    menu_manager.load_menus()
    menu.display_and_select(menu_manager)

if __name__ == "__main__":
    main()
