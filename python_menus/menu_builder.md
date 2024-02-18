# Your role
- Expert Python Developer
- World-class Object-Oriented Programmer
- Seasoned user of The Gang of Four Design Patterns

# Your task
- Break up the following code into classes and methods. You can use any design pattern you see fit.
- During your refactoring process, make at least one object that reads a configuration file and runs the appropriate commands.
  - an example:
  - ``` 1.) Execute the Python run.py script.
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
import os
import dotenv
import pexpect

def main():
    os.system( "clear" )
    print( "                                                 " )
    # print the current path
    print( "      current path: " + os.getcwd() )
    print( "                                                 " )
    print( "                                                 " )
    print( "      ///////////////////////////////////////////" )
    print( "      "                                            )
    print( "      Welcome to the main menu"                    )
    print( "      "                                            )
    print( "      ///////////////////////////////////////////" )
    print( "\n")
    print("     l. open linux bash workspace in vscode\n")
  
    print( "     m. mcba menu\n" )        
    
    print( "     a. airport project\n" )     
    
    print( "     t. the matrix\n" )
    
    print( "     k. ai research\n" )  # dont forget about the tree-sitter implementation code base
    
    print("     x. Exit\n")
    choice = input("\n    Please select an option: \n    > ")
    print( "                                                 " )

    if choice == "m":
        print("making mode 1 score tests... " )
        # open a child process to execute script
        os.chdir( "/home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/Mode1Score/" )
        os.system( "make" )
        main()
        
    elif choice == "1":
        # clear the linux terminal screen
        os.system( "clear" )
        print( "\n\n\n\n\n\n\n\n\n\n      ///////////////////////////////////////////" )
        print( "      "                                            )
        print( "      Welcome to the main menu"                    )
        print( "      "                                            )
        print( "      ///////////////////////////////////////////" )
        print( "1.")

    elif choice == "2":
        print( "running mode 1 score tests..." )
        os.chdir( "/home/adamsl/linuxBash/SMOL_AI/tennis_unit_tests/Mode1Score/" )
        os.system("./run_tests" )
        input( "Press Enter to continue..." )
        main()
        
    elif choice == "3":
        print( "pushing git... " )
        git_token = os.getenv("GIT_TOKEN", "") # get git token from .env file
        print ( "git token: " + git_token )
        try:  # open a child process to execute script 3
            print ( "starting git push..." ) # Start the git push process
            child = pexpect.spawn('git push')
            child.expect('Username for .*:') # Wait for the username prompt and send the username
            child.sendline( "egadams" )
            child.expect('Password for .*:') # Wait for the password prompt and send the password
            git_token = os.getenv("GIT_TOKEN", "") # API Keys
            print ( git_token )
            child.sendline( git_token )
            child.expect(pexpect.EOF) # Wait for the process to complete
            print(child.before.decode('utf-8'))
            
        except pexpect.ExceptionPexpect as e:
            print("Encountered an error:", e)
        main()

    elif choice == "45":
        print( "pushing git... " )
        os.chdir( "/home/adamsl/ai_generated_projects/car_wash_test" )
        os.system( "python3 open_fcw_page.py " )
        print( "changing back to main directory... " )
        os.chdir( "/home/adamsl/linuxBash" )

        main()

    elif choice == "4":
        print( "opening mcba menu... " )
        os.system( "clear" ) # clear terminal screen
        os.system( "python3 /home/adamsl/linuxBash/python_menus/mcba_system_dashboard.py " )
        main()
    
    elif choice == "5":
        print("opening tree-sitter implementation... " )
        os.chdir( "/home/adamsl/openai-search-codebase-and-chat-about-it" )
        os.system( "code ." )
        main()

    elif choice == "6":
        print("opening linux bash repository in vscode... " )
        os.chdir( "/home/adamsl/linuxBash" )
        os.system( "code ." )
        main()
    
    elif choice == "7":
        print("opening current tennis matrix repository in vscode... " )
        os.chdir( "/home/adamsl/rpi-rgb-led-matrix" )
        os.system( "code ." )
        main()
    
    elif choice == "8":
        print("openning current test fixture workspace( SMOL_AI ) in vscode... " )
        os.chdir( "/home/adamsl/linuxBash/SMOL_AI" )
        os.system( "code ." )
        main()
    
    elif choice == "9":
        print("opening test fixture for tennis matrix repository in vscode... " )
        os.system( "code  /home/adamsl/linuxBash/project-management/next_steps.md" )
        main()
    
    elif choice == "air":
        print("opening acceleration doc... " )
        os.system( "code  /home/adamsl/linuxBash/acceleration_documentation.md" )
        main()
    
    elif choice == "s":
        print("opening main swift startup in folder chrome-meta-gpt using vscode... " )
        os.system( "code  /home/adamsl/linuxBash/chrome-meta-gpt/swift_startup.py" )
        main()

    elif choice == "o":
        print("opening python menu directory in vscode... " )
        os.system( "code  /home/adamsl/linuxBash/python_menus/" )
        main()
    
    elif choice == "h":
        print( "showing mycusom table... " )
        os.system( "./show_mycustom_tables.sh " )
        main()
        
    elif choice == "x":
        print("Goodbye!")
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
        os.system( "./delete_guests.sh" )
        main()
    
    elif choice == "m":
        print("deleting all messages... " )
        os.system( "./delete_all_messages.sh" )
        main()
    
    elif choice == "c":
        print("deleting all conversations... " )
        os.system( "./delete_all_conversations.sh" )
        main()
    
    elif choice == "j":
        print("cleaning the monitored objects from the jewelry machine... " )
        os.system( "./delete_monitors.sh" )
        main()

    else:  # if the user enters anything other than 1, 2, 3 or 4 then the program will exit with an error message.

        print("Invalid input, please try again.")

    return 0

main()
```