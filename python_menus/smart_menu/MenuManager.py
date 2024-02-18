from ConfigReader import ConfigReader
from Menu import Menu
from MenuItem import MenuItem
from CommandExecutor import CommandExecutor
import json
import shutil
import os

class MenuManager:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.menus = {}  # Key: menu title, Value: Menu object

    def load_menus(self):
        """Loads menus and menu items from the configuration file."""
        config = ConfigReader.read_config(self.config_file_path)
        # if the config length is zero, exit
        # if config is empty, exit
        if ( len( config ) == 0 ):
            print( "*** ERROR: there is no configriation information, exiting ***" )
            exit()
        for menu_config in config:
            menu_title = menu_config.get("title", "Main Menu")
            if menu_title not in self.menus:
                self.menus[menu_title] = Menu(menu_title)

            menu_item = MenuItem(
                title=menu_config.get("title"),
                action=menu_config.get("action"),
                working_directory=menu_config.get("workingDirectory", ""),
                open_in_subprocess=menu_config.get("openSubprocess", False),
                use_expect_library=menu_config.get("useExpectLibrary", False)
            )
            self.menus[menu_title].add_item(menu_item)

    def display_menu(self, menu_id):
        """Displays the specified menu and handles user input, including adding new menu items."""
        menu = self.menus[menu_id]  # Assuming menus are stored in a dictionary
        while True:
            menu.display()
            choice = input("Select an option: ")

            if choice.isdigit() and int(choice) <= len(menu.items):
                # Handle menu item selection
                selected_item = menu.items[int(choice) - 1]
                selected_item.execute()
            elif choice == str(len(menu.items) + 1):
                break  # Exit the menu
            elif choice == str(len(menu.items) + 2):
                menu.add_new_item_interactively()  # Add a new menu item
            else:
                print("Invalid selection. Please try again.")

    def add_menu_item(self, menu_id):
        """Collects information from the user to add a new menu item to the specified menu."""
        print("Adding a new menu item...")

        title = input("Enter the title for the new menu item: ")
        action = input("Enter the command to execute: ")
        working_directory = input("Enter the full path to the directory: ")
        open_in_subprocess_input = input("Should this command open in a separate window (yes/no)? ")
        use_expect_library_input = input("Should use the Expect library (yes/no)? ")

        open_in_subprocess = open_in_subprocess_input.strip().lower() == 'yes'
        use_expect_library = use_expect_library_input.strip().lower() == 'yes'

        # Create the new MenuItem
        new_item = MenuItem(title, action, working_directory, open_in_subprocess, use_expect_library)

        # Adding the new item to the specified menu
        if menu_id in self.menus:
            self.menus[menu_id].add_item(new_item)
            print("New menu item added successfully.")
            
            # Save changes to configuration file
            self.save_menus_to_config()
        else:
            print(f"Menu with ID {menu_id} not found.")
        
    def save_menus_to_config(self):
        """Serializes and saves the menu structure to the configuration file with a backup."""
        # Create a backup of the current configuration file
        backup_path = f"{self.config_path}.bak"
        try:
            # Only create a backup if the configuration file already exists
            if os.path.exists(self.config_path):
                shutil.copyfile(self.config_path, backup_path)
                print("Backup of the configuration file created.")
                
            # Serialize the menu structure
            config_data = [menu.to_dict() for menu in self.menus.values()]  # Assuming Menu has a to_dict method

            # Save the updated configuration
            with open(self.config_path, 'w') as config_file:
                json.dump(config_data, config_file, indent=4)
                
            print("Menu configuration saved successfully.")
        except Exception as e:
            # In case of an error, restore from the backup
            if os.path.exists(backup_path):
                shutil.copyfile(backup_path, self.config_path)
                print("An error occurred. Configuration restored from backup.")
            else:
                print("An error occurred, but no backup was available.")
            print(f"Error details: {e}")
