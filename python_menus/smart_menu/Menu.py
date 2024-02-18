# import MenuItem
from MenuItem import MenuItem

class Menu:
    def __init__(self, title):
        self.title = title
        self.items = []  # List to hold menu items

    def add_item(self, item):
        """Adds a new MenuItem to the menu."""
        if isinstance(item, MenuItem):
            self.items.append(item)
        else:
            raise TypeError("item must be an instance of MenuItem")

    def display(self):
        """Displays the menu items and prompts for user selection."""
        print(f"\n{self.title}\n" + "-" * len(self.title))
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item.title}")

        # Adding extra menu options as per requirements
        print(f"{len(self.items) + 1}. Exit this menu")
        print(f"{len(self.items) + 2}. Add a menu item")

        # Placeholder for user input handling and executing the selected menu item.
        # This will involve interaction with MenuManager and CommandExecutor.
        choice = input("Please select an option: ")
        print(f"You have selected: {choice}")
    
    def to_dict(self):
        """Serializes the menu item to a dictionary."""
        return {
            "title": self.title,
            "action": self.action,
            "workingDirectory": self.working_directory,
            "openInSubprocess": self.open_in_subprocess,
            "useExpectLibrary": self.use_expect_library
        }
