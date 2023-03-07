# Create a menu in python that with be able to execute 3 other scripts also written in python.
# The menu should be able to exit the program.
# The menu should be able to go back to the main menu from the other scripts.
# The menu should be able to execute the other scripts more than once.
import os

def main():
    print("\n\n\n//////////////////////////////////" )
    print( "Welcome to the Matrix Project Menu" )
    print("//////////////////////////////////\n" )
    print("1. Fony.exe")
    print("2. Open the code repository")
    print("3. Script 3")
    print("4. Exit")

    choice = input("Please enter your choice: ")

    if choice == "1":
        print("openning Fony... ")
        # cd to the directory where the script is located
        # open vscode in the directory
        os.system("Fony.exe")
        main()
    elif choice == "2":
        print("openning the code repository... ")
        os.chdir( "/home/adamsl/zero_w_projects/temp/rpi-rgb-led-matrix" )
        # open a child process to execute script 2
        os.system("code .")
        main()
    elif choice == "3":
        print("You have chosen script 3")
        # open a child process to execute script 3
        #os.system("python script3.py")
        main()

    elif choice == "4":
        print("Goodbye!")

    else:  # if the user enters anything other than 1, 2, 3 or 4 then the program will exit with an error message.

        print("Invalid input, please try again.")

    return 0


main()
