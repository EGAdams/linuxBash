# 
# prompt created on March 4, 2022
# using code-davinci-002
#
# class to populate the file list from the ftp server
# ftp to remote site name is americansjewelry.com
# use passive mode for ftp.
# the directory to list is  libraryDirectory
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

class PopulateFileList:

    def __init__( self, directoryArg ):
        print( "\ninitializing file list class...\n" )
        self.fileDirectory = directoryArg
        self.fileList = [] # initialize private array        
    
    def execute( self ):
        now = datetime.now()
        now_string = now.strftime( "%Y-%m-%d %H:%M" )
        print( "Starting FTP process at " + now_string + "\n" )
        log_file_name = "ftp_logs/ftp_log" + now_string + ".txt"
        # open log file name if it exists.  If not create it
        log_file = None
        if os.path.exists( log_file_name ):
            log_file = open(log_file_name, 'a')
        else:
            # get the current working directory
            cwd = os.getcwd()
            print ( cwd )
            # change to the ftp_logs directory
            os.chdir( "./pickle_ball/" )
            log_file = open(log_file_name, 'w')
    
        log_file.write( "Starting FTP process at " + now_string + "\n" )
        log_file.close()

        try:
            ftp = ftplib.FTP('americansjewelry.com')  # connect to host, default port
            print( "\nConnected to americansjewelry.com" )  # connection message from server is printed on stdout (screen)

            try:  # login with username and password - passwd is being sent in clear text, sendcmd() sends command and returns response string (not printed on screen)   
                ftp_user = os.environ.get( "FTP_USER" )  # get the login an password from the environment variables
                ftp_password = os.environ.get( "FTP_PASSWORD" )

                # create the .env file if it does not exist
                if ftp_user == None or ftp_password == None:
                    print( "FTP_USER or FTP_PASSWORD environment variables not set. Creating .env file." )
                    env_file = open( ".env", "w" )
                    env_file.write( "FTP_USER="     + input( "Enter FTP user name: " ))
                    env_file.write( "FTP_PASSWORD=" + input( "Enter FTP password:  " ))
                    env_file.close()
                    print( "FTP_USER and FTP_PASSWORD environment variables set. Please restart the program." )
                    #sys.exit()

                ftp.login( ftp_user, ftp_password )  # login as user anonymous, passwd anonymous@ (usually email address is used as password) - passwd is being sent in clear text!
                print( "\nLogged into americansjewelry.com" )  # connection message from server is printed on stdout (screen)

                try:  # set binary mode for transferring image files - use ASCII for text files! - setpassive() sets passive mode on or off (default off), returns nothing - passive mode is used when client behind firewall/NAT router needs to initiate data transfer with server outside firewall/NAT router! - active mode is used when client outside firewall/NAT router needs to initiate data transfer with server behind firewall/NAT router! - active mode requires that client be able to accept incoming connections from server! - passive mode requires that client be able to initiate outgoing connections with server! - active vs passive modes are not related to FTP commands PORT vs PASV! PORT command tells server which port number it should connect back to for data transfer while PASV command tells client which port number it should connect back to for data transfer! In both cases, client is initiating connection!
                    ftp.set_pasv(True)  # set passive mode on
                    print( "\nSet passive mode on" )  # connection message from server is printed on stdout (screen)

                    try:  # change to libraryDirectory - cwd() changes working directory, returns nothing - if directory doesn't exist, raise error_perm exception!
                        ftp.cwd( self.fileDirectory )
                        print( "\nChanged to " + self.fileDirectory )  # connection message from server is printed on stdout (screen)

                        try:  # get list of files in current directory
                            filelist = ftp.nlst()
                            print( "\nGot file list\n" )  # connection message from server is printed on stdout (screen)
                            for file in filelist:
                                if file.endswith( ".zip" ):
                                    self.fileList.append( file )
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
        
        log_file = open(log_file_name, 'a')
        log_file.write( "Ending FTP process at " + now_string + "\n" )
        log_file.close()
        print( "Ending FTP process at " + now_string + "\n" )

        return self.fileList