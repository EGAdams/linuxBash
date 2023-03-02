#!/bin/bash

while true; do
    echo "Please select an option:"
    echo "  1. Open tennis cpp and view."
    echo "  2. Compile tennis project and open view." 
    echo "  3. Open vite-vue-electron project containing the latest command objects." 
    echo "  4. Quit"

    read -p "Enter your selection [1-4] " selection

    case $selection in
        1) echo "Openning tennis_cpp vscode project and view... " 
            cd /mnt/c/Users/EG/Desktop/2022/june/2nd_week/tennis_cpp
            powershell.exe code .
            cd /mnt/c/Users/EG/Desktop/2022/april/5th_week/electron-quick-start
            powershell.exe code .
            sleep 1;
        ;;
        
        2) echo "Compiling tennis cpp... " 
            echo "cd /mnt/c/Users/EG/Desktop/2022/june/2nd_week/tennis_cpp/... "
            cd /mnt/c/Users/EG/Desktop/2022/june/2nd_week/tennis_cpp/
            echo "running compile.bat... "
            powershell.exe ./compile.bat
            echo "changing directory to electron-quick-start... "
            sleep 1;
            cd /mnt/c/Users/EG/Desktop/2022/april/5th_week/electron-quick-start
            echo "firing up the tennis view... "
            powershell.exe "npm run start"
        ;;
        3) 
            echo "going to .../vite-vue-electron directory where all of the latest commands are... "
            sleep 1; 
            cd /mnt/c/Users/EG/Desktop/2022/july/1st_week/vite-vue-electron
            echo "opening vscode... "
            powershell.exe code .
        ;;

        4) echo "You chose to quit" 
            exit 0 
        ;;
        
        *) echo "Invalid selection" ;;
    esac
done
