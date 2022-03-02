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
    --title "Menu" \
    --clear \
    --cancel-label "Exit" \
    --menu "Please select:" $HEIGHT $WIDTH $NUMBER_OF_OPTIONS \
    "0" "exit this menu" \
    "1" "Display System Information" \
    "2" "Display Disk Space" \
    "3" "Display Home Space Utilization" \
    "4" "start vscode in vue 3 component directory" \
    "5" "change to vue 3 component directory"\
    "6" "run electron vue dashboard"\
    "7" "copy workspace to fresh electron"\
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
      result=$(echo "Hostname: $HOSTNAME"; uptime)
      display_result "System Information"
      ;;
    2 )
      result=$(df -h)
      display_result "Disk Space"
      ;;
    3 )
      if [[ $(id -u) -eq 0 ]]; then
        result=$(du -sh /home/* 2> /dev/null)
        display_result "Home Space Utilization (All Users)"
      else
        result=$(du -sh $HOME 2> /dev/null)
        display_result "Home Space Utilization ($USER)"
      fi
      ;;
    4 )
      cd /home/adamsl/vue3_components/vue_typescript_components
      code .
      clear
      break
      ;;
    5 )
      cd /home/adamsl/vue3_components/vue_typescript_components
      clear
      break
      ;;
    6 )
      cd /mnt/c/Users/EG/electron-vue-example
      powershell.exe startElectron.bat
    ;;  
    7 )
      clear
      echo "cp -fp $LATEST_SOURCE/src/components/* $CURRENT_WORKSPACE/src/components/"
      echo "cp -rfp $LATEST_SOURCE/src/typescript_source $CURRENT_WORKSPACE/src/"
      echo "cp -rfp $LATEST_SOURCE/src/views $CURRENT_WORKSPACE/src/"
      echo "cp -fp $LATEST_SOURCE/src/router/*.ts $CURRENT_WORKSPACE/src/router/"
      cd $CURRENT_WORKSPACE
      echo "npm install --save-dev @types/jquery"
      echo "npm install --save-dev @types/mysql"
      echo "npm install --save-dev @types/socket.io-client"
      echo "npm install --save-dev @types/ssh2"
      echo "npm install --save-dev dns"
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
      break
    ;;  
  esac
done
