# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based smart menu system that allows users to create and manage interactive command-line menus with configurable menu items. Menu items can execute shell commands, change working directories, and support both regular execution and subprocess execution.

## Running the Application

**Main entry point:**
```bash
python3 smart_menu_system.py [config_path]
```

If no config path is provided, it defaults to the local `config.json` file.

## Architecture

The system follows object-oriented design patterns with clear separation of concerns:

### Core Classes

- **Menu**: Manages collections of menu items and handles the display/selection loop
- **MenuItem**: Base class representing executable menu items with command, working directory, and subprocess options
- **SmartMenuItem**: Extends MenuItem to support nested submenus
- **MenuManager**: Coordinates menu loading from config files and handles menu item creation
- **ConfigReader**: Handles JSON configuration file parsing with error handling
- **CommandExecutor**: Alternative execution strategy for menu items (currently unused in favor of MenuItem.execute())

### Key Files

- `smart_menu_system.py`: Main application entry point
- `MenuItem.py:22`: Core execution logic - the "Shabaaam!" line that executes commands
- `MenuManager.py:21-30`: Configuration loading and MenuItem instantiation
- `Menu.py:11-28`: Main menu display and user interaction loop

## Configuration System

Menu items are configured via JSON files in the `configurations/` directory:
- `config.json`: Default configuration
- `configurations/`: Location-specific configurations (home, largo, spring_hill, voice)

Each menu item supports:
- `title`: Display name
- `action`: Shell command to execute (null for submenus)
- `working_directory`: Directory to execute command in
- `open_in_subprocess`: Whether to run in separate process
- `use_expect_library`: For interactive command handling

## Menu Item Execution Flow

1. User selects menu item from numbered list
2. `Menu.display_and_select()` calls `MenuItem.execute()`
3. `MenuItem.execute()` changes working directory if specified
4. Command executed via subprocess or direct shell execution
5. Working directory restored to original location

## Development Notes

- The codebase includes both `MenuItem` and `SmartMenuItem` classes, with `SmartMenuItem` extending functionality for nested menus
- There's an alternative `CommandExecutor` class that duplicates some functionality from `MenuItem.execute()`
- Configuration files may contain sensitive information (API keys visible in current config.json)
- The system supports dynamic menu item addition during runtime with automatic config persistence