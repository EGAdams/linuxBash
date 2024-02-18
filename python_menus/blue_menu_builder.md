# Your role
- Expert Python Developer
- World-class Object-Oriented Programmer
- Seasoned user of The Gang of Four Design Patterns

# Your task
- Break up the following code into classes and methods. You can use any design pattern you see fit.
- During your refactoring process, make at least one object that reads a configuration file and runs the appropriate commands to build the menus.
- There should always be to extra menu items in every menu or submenu, "Exit this menu", and "Add a menu item".
- The "Add menu item" will start the process of collecting information about the new menu item like:
```example_questions
- what is the full path to the directory that you want to run the script in?
- what is the name of the executable script that will be executed when choosing this menu item?
- do you want a prefix like "open notepad" or do you just want the next consecutive number like if there are 2 menu items ( 1. and 2. ) the next one will be "3.".
- should we open in a separate window, or just use this one?
- should the window that you are executing the script from close after a selected script is executed?

other questions that you think that we should ask to add informationi about the menu item...
``` 

## An example pseudo config file ( translate to valid JSON for me please ):
```
    1.) Execute the Python run.py script.
    - Action - run.py
    - Change to Working Directory - /home/adamsl
    - Open Subprocess - false
    - Use the Expect library - false
    ...

    2.) Open the AI Research Menu
    - Action - ai_menu.py
    - Change to Working Directory - /home/adamsl
    - Open Subprocess - true
    - Use the Expect Library - false
    ...

    n. ) ...
```
    
# Source Code to Refactor
```python
#!/bin/bash

# while-menu-dialog: a menu driven system information program

DIALOG_CANCEL=1
DIALOG_ESC=255
HEIGHT=0
WIDTH=0
NUMBER_OF_OPTIONS=9
CURRENT_WORKSPACE='/mnt/c/Users/EG/march/fresh_electron'
LATEST_SOURCE='/mnt/c/Users/EG/electron-vue-example'

display_result() {
  dialog --title "$1" \
    --no-collapse \
    --msgbox "$result" 0 0
}

echo "entering while loop... "
echo;

while true; do
  exec 3>&1
  echo "decalring selection... "
  selection=$(dialog \
    --backtitle "Main Directory Menu" \
    --title "Menu" \
    --clear \
    --cancel-label "Exit" \
    --menu "Please select:" $HEIGHT $WIDTH $NUMBER_OF_OPTIONS \
    "0" "exit this menu" \
    "p" "open pickleball dashboard" \
    "1" "Clean all but users" \
    "f" "open flash menu ( includes matrix project with fonts )" \
    "2" "Edit this menu" \
    "j" "vscode projects" \
    "k" "MCBA System Dashboard" \
    "a" "clean all but admin"\
    "c" "clean keep users and conversations"\
    "m" "start monitor"\
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
      cd /mnt/c/Users/EG/Desktop/2022/july/1st_week/vite-vue-electron/src/typescript_source/concrete/commands/delete_html_logs/
      ./clean_but_keep_users.sh
      #display_result "clean all but users"
      cd -
      ;;
    f )
      cd /home/adamsl/linuxBash
      ./flash_menu.sh
      break
      ;;
    2 )
      cd /home/adamsl/linuxBash
      code .
      cd -
      ;;
    j )
      cd /home/adamsl/linuxBash
      ./vscode_projects.sh
      ;;
    k )
      cd /home/adamsl/linuxBash
      python3 mcba_system_dashboard.py
      break
      ;;
    a )
      cd /home/adamsl/linuxBash
      ./clean_all_but_admin.sh
      ;;
    c )
      cd /home/adamsl/linuxBash
      ./clean_keep_users_conversatons.sh
    ;;

    p )
      cd /home/adamsl/linuxBash/pickle_ball
      python3 pickleball_dashboard.py
      break
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
  esac
  echo "done with case selection."
done
```


# Here is the vanilla g4 answer
https://chat.openai.com/share/daa918d7-135c-468a-b86f-6c8791346268


# Professional coder answer
https://chat.openai.com/share/7ed5b449-cb78-428b-97ce-6ae11cd1a164

anyways im using the one from the professional coder anyway, it is slightly better.


