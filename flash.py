# Create a menu in python that with be able to execute 3 other scripts also written in python.
# The menu should be able to exit the program.
# The menu should be able to go back to the main menu from the other scripts.
# The menu should be able to execute the other scripts more than once.
import os

def main():
    print( "Welcome to the main menu" )
    print( "1. test mode 1 score object" )
    print( "2. test mode 1 functions objects " )
    print( "3. test tie break" )
    print( "4. run all tests" )
    print( "x. Exit" )

    choice = input( "Please enter your choice: " )

    if choice == "1":
        print( "openning the latest matrix project... " )
        # cd to the directory where the script is located
        #os.chdir( "/home/adamsl/zero_w_projects/temp/rpi-rgb-led-matrix" )
        # open vscode in the directory
        os.system( "python3 the_matrix_project.py " )
        main()
    elif choice == "2":
        print( "You have chosen tennis C++ unit testing menu" )
        # open a child process to execute tennis C++ unit testing menu
        os.system( "python3 tennis_unit_tests.py" )
        main()
    elif choice == "3":
        print( "You have chosen script 3" )
        # open a child process to execute script 3
        os.system( "python script3.py" )
        main()

    elif choice == "x":
        print( "Goodbye!  exiting..." )
        # exit system
        exit( 0 )

    else:  # if the user enters anything other than 1, 2, 3 or 4 then the program will exit with an error message.

        print( "Invalid input, please try again." )

    return 0


main()
