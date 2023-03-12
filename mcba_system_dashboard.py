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
    print( "      "                                            )
    print( "      Welcome to the main MCBA System Dashboard"                    )
    print( "      "                                            )
    print( "      ///////////////////////////////////////////" )
    print( "\n")
    print("     1. clean all tables.  keep admin\n\n")
    print("     2. clean all tables.  keep users, conversations, and admin\n\n")
    print("     3. show all tables\n\n")
    print("     4. open car wash page and click on phone icon\n\n")
    print("     5. Script 5\n\n")
    print("     6. Exit\n\n")

    choice = input("    Please select an option: \n\n    >")
    print( "                                                 " )

    if choice == "1":
        print("clearing all table data.  keeping admin info... " )
        # cd to the directory where the script is located
        #os.chdir( "/home/adamsl/zero_w_projects/temp/rpi-rgb-led-matrix" )
        # open vscode in the directory
        os.system( "./clean_all_but_admin.sh" )
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

    elif choice == "next":
        print("You have chosen script next")
        # open a child process to execute script 3
        os.system("python script3.py")
        main()

    elif choice == "4":
        print("Goodbye!")

    else:  # if the user enters anything other than 1, 2, 3 or 4 then the program will exit with an error message.

        print("Invalid input, please try again.")

    return 0


main()
