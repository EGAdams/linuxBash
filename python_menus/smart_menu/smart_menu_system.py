import sys
from MenuManager import MenuManager
from Menu import Menu

if __name__ == "__main__":
    # Default path (used if no arg passed)
    default_config = "/home/adamsl/linuxBash/python_menus/smart_menu/config.json"

    # Get arg1 if provided, else fallback to default
    config_path = sys.argv[1] if len(sys.argv) > 1 else default_config

    menu = Menu()
    menu_manager = MenuManager(menu, config_path)
    menu_manager.load_menus()
    menu.display_and_select(menu_manager)
