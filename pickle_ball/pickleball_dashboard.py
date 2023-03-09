# Create a menu in python that with be able to execute 3 other scripts also written in python.
# The menu should be able to exit the program.
# The menu should be able to go back to the main menu from the other scripts.
# The menu should be able to execute the other scripts more than once.
import os
from threading import Thread

def main():
    print( "                                                 " )
    print( "                                                 " )
    print( "                                                 " )
    print( "      ///////////////////////////////////////////" )
    print( "      "                                            )
    print( "      Welcome to the main Pickleball Dashboard"    )
    print( "      "                                            )
    print( "      ///////////////////////////////////////////" )
    print( "\n")
    print("     1. open pickeball view project\n\n")
    print("     2. open pickleball cpp\n\n")
    print("     3. open the chinese remote system project\n\n")
    print("     4. run the remote electron from package.json\n\n")
    print("     5. open the electron pickle ball view from package.json\n\n")
    print("     6. compile pickle cpp\n\n")
    print("     7. pull a library file from the jewelry machine and move it to pickle cpp\n\n")
    print("     8. Exit\n\n")

    choice = input("    Please select an option: \n\n    >")
    print( "                                                 " )

    if choice == "1":
        print( "openning pickleball view... " )
        os.system( "sleep 1" )
        os.system( "powershell.exe code c:/Users/EG/Desktop/2022/may/2nd_week/pickleball_view" )
        main()

    elif choice == "2":
        print( "openning pickleball remote project... " )
        os.system( "sleep 1" )
        os.system( "powershell.exe code c:/Users/EG/Desktop/2022/may/2nd_week/pickle_cpp" )
        main()
        
    elif choice == "3":
        print( "openning the chinese remote system project... " )
        os.system( "sleep 1" )
        os.system( "powershell.exe code c:/Users/EG/Desktop/2022/august/5th_week/chinese_remote_system" )
        main()

    elif choice == "4":
        print( "changing directory to chinese remote system project... " )
        os.chdir( "/mnt/c/Users/EG/Desktop/2022/august/5th_week/chinese_remote_system/" )
        os.system( "sleep 1" )
        # print the current directory
        print( "print changed directory to " )
        os.system( "pwd" )
        os.system( "sleep 1" )
        print( "running remote electron from project... " )
        os.system( "npm run start" )
        main()

    elif choice == "5":
        print( "openning the pickleball view ... " )
        os.chdir( "/mnt/c/Users/EG/Desktop/2022/may/2nd_week/pickleball_view/" )
        os.system( "sleep 1" )
        # print the current directory
        print( "print changed directory to " )
        os.system( "pwd" )
        os.system( "sleep 1" )
        print( "running picklball view electron from project... " )
        os.system( "npm run start" )
        main()

    elif choice == "6":
        print( "compiling pickle cpp... " )
        os.chdir( "/mnt/c/Users/EG/Desktop/2022/may/2nd_week/pickle_cpp/" )
        os.system( "sleep 1" )
        # print the current directory
        print( "print changed directory to " )
        os.system( "pwd" )
        os.system( "sleep 1" )
        os.system( "powershell.exe ./compile.bat" )

        print( "openning the pickleball view ... " )
        os.chdir( "/mnt/c/Users/EG/Desktop/2022/may/2nd_week/pickleball_view/" )
        os.system( "sleep 1" )
        # print the current directory
        print( "print changed directory to " )
        os.system( "pwd" )
        os.system( "sleep 1" )
        print( "running picklball view electron from project... " )
        # make an os system call to open the pickleball view in a separate thread
        thread = Thread( target=start_npm )
        thread.start()
        #os.system( "npm run start" )

        print( "changing directory to chinese remote system project... " )
        os.chdir( "/mnt/c/Users/EG/Desktop/2022/august/5th_week/chinese_remote_system/" )
        os.system( "sleep 1" )
        # print the current directory
        print( "print changed directory to " )
        os.system( "pwd" )
        os.system( "sleep 1" )
        print( "running remote electron from project... " )
        thread = Thread( target=start_npm )
        thread.start()
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

def start_npm():
    os.system( "npm run start" )


main()
