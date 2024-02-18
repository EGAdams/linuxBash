from MenuManager import MenuManager
# from Menu import Menu
from DialogMenu import DialogMenu
if __name__ == "__main__":
    config_path = "/home/adamsl/linuxBash/python_menus/smart_menu/config.json"

    menu = DialogMenu()
    menu_manager = MenuManager(menu, config_path )
    menu_manager.load_menus()
    menu.display_and_select(menu_manager)