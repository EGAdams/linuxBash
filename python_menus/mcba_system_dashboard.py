# Create a menu in python that with be able to execute 3 other scripts also written in python.
# The menu should be able to exit the program.
# The menu should be able to go back to the main menu from the other scripts.
# The menu should be able to execute the other scripts more than once.
import os

def main():
    print( "                                                 " )
    print( "                                                 " )
    print( "                                                 " )
    print( "      ///////////////////////////////////////////" )
    print( "      Welcome to the main MCBA System Dashboard"                    )
    print( "      ///////////////////////////////////////////" )
    print( "\n")
    print("     1. clean all tables.  keep admin")
    print("     2. clean all tables.  keep users, conversations, and admin")
    print("     3. show all tables")
    print("     4. open car wash page and click on phone icon")
    print("     5. open log viewer")
    print("     h. show mycustom table" )
    print("     t. delete all messages with est in them") 
    print("     keys. show gcm_keys table" )
    print("     g. delete all guests.  keep admin") 
    print("     m. delete all messages.") 
    print("     j. clear monitored objects table.") 
    print("     c. delete all conversations.") 
    print("     6. Exit")

    choice = input("    Please select an option: notbash$")
    print( "                                     " )

    if choice == "1":
        print("clearing all table data.  keeping admin info... " )
        # cd to the directory where the script is located
        #os.chdir( "/home/adamsl/zero_w_projects/temp/rpi-rgb-led-matrix" )
        # open vscode in the directory
        os.system( "./delete_all_but_admin.sh" )
        main()

    elif choice == "2":
        print( "clearing all table data.  keeping user, conversation and admin info... " )
        # open a child process to execute script 2
        os.system(" ./delete_all_but_users_conversations_admin.sh " )
        main()
        
    elif choice == "3":
        print( "showing all tables... " )
        # open a child process to execute script 3
        os.system( "./show_all_tables.sh " )
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
        print("openining log viewer... " )
        # open a child process to execute script
        os.chdir( "/home/adamsl/the-factory" )
        os.system( "npm run start" )
        main()
    
    elif choice == "h":
        print( "showing mycusom table... " )
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
        os.system( "./delete_all_messages.sh" )
        main()
    
    elif choice == "c":
        print("deleting all conversations... " )
        # cd to the directory where the script is located
        #os.chdir( "/home/adamsl/zero_w_projects/temp/rpi-rgb-led-matrix" )
        # open vscode in the directory
        os.system( "./delete_all_conversations.sh" )
        main()
    
    elif choice == "j":
        print("cleaning the monitored objects from the jewelry machine... " )
        # cd to the directory where the script is located
        #os.chdir( "/home/adamsl/zero_w_projects/temp/rpi-rgb-led-matrix" )
        # open vscode in the directory
        os.system( "./delete_monitors.sh" )
        main()

    else:  # if the user enters anything other than 1, 2, 3 or 4 then the program will exit with an error message.

        print("Invalid input, please try again.")

    return 0


main()