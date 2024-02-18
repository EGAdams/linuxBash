# Create a menu in python that with be able to execute 3 other scripts also written in python.
# The menu should be able to exit the program.
# The menu should be able to go back to the main menu from the other scripts.
# The menu should be able to execute the other scripts more than once.
import os

SHELL_SCRIPTS_DIR = "/home/adamsl/linuxBash/menu_shell_scripts"

def main():
    print( "                                                 " )
    print( "                                                 " )
    print( "                                                 " )
    print( "      ///////////////////////////////////////////" )
    print( "      The adb dashboard"                    )
    print( "      ///////////////////////////////////////////" )
    print( "\n")
    print("     1. show device ip address" )
    print("     2. switch to tcpip mode")
    print("     3. show all tables")
    print("     m. delete all messages.") 
    print("     c. delete all conversations.") 
    print("     j. clear monitored objects table.") 
    print("     4. open car wash page and click on phone icon")
    print("     5. open log viewer")
    print("     h. show mycustom table" )
    print("     t. delete all messages with est in them") 
    print("     keys. show gcm_keys table" )
    print("     g. delete all guests.  keep admin") 
    print("     6. Exit \n" )

    choice = input("    Please select an option: >>----> ") 
    print( "                                     " )

    if choice == "1":
        print( "show device ip address" )
        # cd to the directory where the script is located
        #os.chdir( "/home/adamsl/zero_w_projects/temp/rpi-rgb-led-matrix" )
        # open vscode in the directory
        # run a command in the windows OS
        # open a cmd prompt to send a command to windows

        
        os.system ( "adb shell ip route" )
        input("press enter to continue...")
        main()

    
        
    elif choice == "2":
        print( "switching to tcpip mode... " )
        # open a child process to execute script 3
        os.system( "adb tcpip 5555 " )
        # os.system( "python3 ./linuxBash/python_menus/show_table_clean.py" )
        main()

    elif choice == "4":
        print( "opening car wash page and clicking on phone icon... " )
        # change to directory: ~/ai_generated_projects/car_wash_test
        os.chdir( "/home/adamsl/ai_generated_projects/car_wash_test" )
        
        # execute python3 open_fcw_page.py 
        os.system( "python3 open_fcw_page.py " )
        print( "changing back to main directory... " )
        # sleep to display message
        #os.system( "sleep 2" )
        os.chdir( "/home/adamsl/linuxBash" )

        main()

    elif choice == "5":
        print("opening log viewer... " )
        # open a child process to execute script
        os.chdir( "/home/adamsl/the-factory" )
        os.system( "npm run start" )
        main()
    
    elif choice == "h":
        print( "showing mycustom table... " )
        os.system( "./show_mycustom_tables.sh " )
        main()
        
    elif choice == "6":
        print("Goodbye!")
        # exit the program
        exit()
    
    elif choice == "t":
        print ( "deleting test messages..." )
        os.system( "./delete_test_messages.sh" )
        main()
    
    elif choice == "keys":
        print ( "show gcm_keys table..." )
        os.system( "./show_gcm_keys.sh" )
        main()
    
    elif choice == "g":
        print("deleting all guests... " )
        # cd to the directory where the script is located
        #os.chdir( "/home/adamsl/zero_w_projects/temp/rpi-rgb-led-matrix" )
        # open vscode in the directory
        os.system( "./delete_guests.sh" )
        main()
    
    elif choice == "m":
        print("deleting all messages... " )
        # cd to the directory where the script is located
        #os.chdir( "/home/adamsl/zero_w_projects/temp/rpi-rgb-led-matrix" )
        # open vscode in the directory
        os.system( SHELL_SCRIPTS_DIR + "/delete_all_messages.sh" )
        main()
    
    elif choice == "c":
        print("deleting all conversations... " )
        # cd to the directory where the script is located
        #os.chdir( "/home/adamsl/zero_w_projects/temp/rpi-rgb-led-matrix" )
        # open vscode in the directory
        os.system( SHELL_SCRIPTS_DIR + "/delete_all_conversations.sh" )
        main()
    
    elif choice == "j":
        print("cleaning the monitored objects from the jewelry machine... " )
        # cd to the directory where the script is located
        #os.chdir( "/home/adamsl/zero_w_projects/temp/rpi-rgb-led-matrix" )
        # open vscode in the directory
        os.system( SHELL_SCRIPTS_DIR + "/delete_monitors.sh" )
        main()

    else:  # if the user enters anything other than 1, 2, 3 or 4 then the program will exit with an error message.

        print("Invalid input, please try again.")

    return 0


main()
