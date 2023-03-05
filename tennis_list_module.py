# 
# prompt created on March 4, 2022
# using code-davinci-002
#
# class to populate the tennis library list from the ftp server
# ftp to remote site name is americansjewelry.com
# use passive mode for ftp.
# the username is tinman72
# the password is sep02@Th
# the directory to list is  /public_html/scoreprolibraries/tennis_libraries
# list only the .zip files
# put the list of files in a menu.
# wait for a user to choose one of the files from the menu
# return the name of the file chosen by the user

import ftplib
import os
import sys
import time
from datetime import datetime
from datetime import timedelta

class TennisList:

    def __init__( self ):
        print( "\ninitializing Tennis list class...\n" )

        #initialize private array
        self.__tennis_library_list = []         
    
    def populate_list( self ):

        # get the current date and time
        now = datetime.now()

        # get the current date and time in a string format
        now_string = now.strftime( "%Y-%m-%d %H:%M" )

        print( "Starting FTP process at " + now_string + "\n" )

        # create a file name for the log file using the current date and time in the string format above
        log_file_name = "ftp_logs/ftp_log" + now_string + ".txt"

        # open a log file to write to using the file name created above
        log_file = open(log_file_name, 'w')

        # write to the log file that we are starting this process at this time and date
        log_file.write( "Starting FTP process at " + now_string + "\n" )

        # close the log file so we can reopen it later in append mode if needed
        log_file.close()

        try:
            ftp = ftplib.FTP('americansjewelry.com')  # connect to host, default port

            print( "\nConnected to americansjewelry.com" )  # connection message from server is printed on stdout (screen)

            try:  # login with username and password - passwd is being sent in clear text, sendcmd() sends command and returns response string (not printed on screen)
                ftp.login('tinman72', 'sep02@Th')  # login as user anonymous, passwd anonymous@ (usually email address is used as password) - passwd is being sent in clear text!

                print( "\nLogged into americansjewelry.com" )  # connection message from server is printed on stdout (screen)

                try:  # set binary mode for transferring image files - use ASCII for text files! - setpassive() sets passive mode on or off (default off), returns nothing - passive mode is used when client behind firewall/NAT router needs to initiate data transfer with server outside firewall/NAT router! - active mode is used when client outside firewall/NAT router needs to initiate data transfer with server behind firewall/NAT router! - active mode requires that client be able to accept incoming connections from server! - passive mode requires that client be able to initiate outgoing connections with server! - active vs passive modes are not related to FTP commands PORT vs PASV! PORT command tells server which port number it should connect back to for data transfer while PASV command tells client which port number it should connect back to for data transfer! In both cases, client is initiating connection!
                    ftp.set_pasv(True)  # set passive mode on

                    print( "\nSet passive mode on" )  # connection message from server is printed on stdout (screen)

                    try:  # change to directory /public_html/scoreprolibraries/tennis_libraries - cwd() changes working directory, returns nothing - if directory doesn't exist, raise error_perm exception!
                        ftp.cwd('/public_html/scoreprolibraries/tennis_libraries')

                        print( "\nChanged to /public_html/scoreprolibraries/tennis_libraries" )  # connection message from server is printed on stdout (screen)

                        try:  # get list of files in current directory
                            # dir() prints list of files in current directory to stdout (screen), returns nothing 
                            # nlst() returns list of files in current directory as a list of strings, 
                            # raise error_perm exception if no files found!
                            filelist = ftp.nlst()

                            print( "\nGot file list\n" )  # connection message from server is printed on stdout (screen)

                            # loop through the list of files and populate the tennis library list
                            for file in filelist:
                                # check to see if the file is a zip file
                                if file.endswith( ".zip" ):
                                    #add the file to the tennis library list
                                    self.__tennis_library_list.append( file )

                        except ftplib.error_perm as resp:
                            if str( resp ) == "550 No files found":
                                print( "No files in this directory" )

                            else:
                                raise

                    except ftplib.error_perm as resp:
                        if str( resp ).startswith('550'):
                            print( "Error changing directories." )

                        else:
                            raise resp

                except ftplib.error_perm as resp:
                    if str( resp ).startswith('530'):
                        print( "Login failed." )

            finally:
                ftp.quit()
            
        except ftplib.all_errors as e:
            print( "FTP error:", e)
        
        # open the log file in append mode
        log_file = open(log_file_name, 'a')

        # write to the log file that we are ending this process at this time and date
        log_file.write( "Ending FTP process at " + now_string + "\n" )

        # close the log file
        log_file.close()

        print( "Ending FTP process at " + now_string + "\n" )

        return self.__tennis_library_list