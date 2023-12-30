#!/bin/bash

# while-menu-dialog: a menu driven system information program

DIALOG_CANCEL=1
DIALOG_ESC=255
HEIGHT=0
WIDTH=0
NUMBER_OF_OPTIONS=8
CURRENT_WORKSPACE='/mnt/c/Users/EG/march/fresh_electron'
LATEST_SOURCE='/mnt/c/Users/EG/electron-vue-example'

display_result() {
  dialog --title "$1" \
    --no-collapse \
    --msgbox "$result" 0 0
}

while true; do
  exec 3>&1
  selection=$(dialog \
    --backtitle "System Information" \
    --title "VS Code Project Menu" \
    --clear \
    --cancel-label "Exit" \
    --menu "Please select:" $HEIGHT $WIDTH $NUMBER_OF_OPTIONS \
    "0" "exit this menu" \
    "1" "vite-vue-electron" \
    "2" "Edit this menu" \
    "f" "open wsl factory" \
    "w" "open project wordpress" \
    "m" "the matrix project" \
    "6" "open app test" \
    "7" "copy workspace to fresh electron" \
    "a" "open app test" \
    2>&1 1>&3)
  exit_status=$?
  exec 3>&-
  case $exit_status in
    $DIALOG_CANCEL)
      clear
      echo "Program terminated."
      exit
      ;;
    $DIALOG_ESC)
      clear
      echo "Program aborted." >&2
      exit 1
      ;;
  esac
  case $selection in
    0 )
      clear
      break
      ;;
    1 )
      cd /mnt/c/Users/EG/Desktop/2022/july/1st_week/vite-vue-electron
      code .
      cd -
      ;;
    2 )
      cd /home/adamsl/linuxBash
      code .
      cd -
      ;;
    f )
      cd /home/adamsl/the-factory
      code .
      ;;
    w )
      cd /mnt/c/xampp-joomla/htdocs/wordpress/
      code .
      cd -
      ;;
    m )
      cd /home/adamsl/zero_w_projects/temp/rpi-rgb-led-matrix/
      code .
      cd -
      ;;
    6 )
      cd /mnt/c/Users/EG/electron-vue-example
      powershell.exe startElectron.bat
    ;;  
    7 )
      clear
      cp -fp $LATEST_SOURCE/src/components/* $CURRENT_WORKSPACE/src/components/
      cp -rfp $LATEST_SOURCE/src/typescript_source $CURRENT_WORKSPACE/src/
      cp -rfp $LATEST_SOURCE/src/views $CURRENT_WORKSPACE/src/
      cp -fp $LATEST_SOURCE/src/router/*.ts $CURRENT_WORKSPACE/src/router/
      cd $CURRENT_WORKSPACE
      echo "yarn add electron-ssh2"
      echo "npm install --save-dev @types/jquery"
      echo "yarn add @types/jquery"
      echo "yarn add jquery mysql --ignore-engines"

      echo "npm install --save-dev @types/mysql"
      echo "yarn add @types/mysql"
      echo "yarn add mysql --ignore-engines"
      echo "npm install --save-dev @types/socket.io-client"
      echo "yarn add @types/socket.io-client"
      echo "yarn add electron-ssh2"
      echo "npm install --save-dev dns"
      echo "yarn add dns --ignore-engines"
      echo "npm install --save-dev cpu-features"
      echo "npm install node-loader --save-dev"
      echo "npm install https://github.com/mscdex/cpu-features.git"
      echo "npm install https://github.com/mscdex/ssh2.git"
      echo "npm install -g npm-install-peers"
      echo "yarn add -D native-ext-loader --ignore-engines"

      echo "npm install --save-dev node-loader@latest"
      echo "npm install"
      echo "yarn add node-loader@latest --ignore-engines"
      echo "yarn add cpu-features --ignore-engines"
      echo "yarn add vue@next"
      echo "yarn add vue@next --ignore-engine"
      echo "yarn add @vue/compiler-sfc -D"
      echo "RUN THE INSTALLS IN WINDOWS ENV!"
      break
    ;; 

    a )
      cd /mnt/c/Users/EG/appium_example
      code .
      ;; 
  esac
done
