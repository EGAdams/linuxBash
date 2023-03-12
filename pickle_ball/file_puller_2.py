# module to pull zip file from the jewelry machine
# create the ftp object, get the zip file and close the ftp object
import ftplib
import os
import sys

class PullZipFile:
    def __init__( self,  zipFileArg, libraryPath,):
        self.zipFile     = zipFileArg
        self.libraryPath = libraryPath
        print( "pull object initialized." )
     
    def execute( self ):
        try:
            ftp = ftplib.FTP( 'americansjewelry.com' )  # connect to host, default port
            print( "Connected to americansjewelry.com" )  # connection message from server is printed on stdout (screen)
            try:  # login with username and password - passwd is being sent in clear text
                ftp_user     = os.environ.get( "FTP_USER"     )  # get the login an password from the environment variables
                ftp_password = os.environ.get( "FTP_PASSWORD" )
                # if ftp_user == None or ftp_password == None: # create the .env file if it does not exist
                #     print( "FTP_USER or FTP_PASSWORD environment variables not set. Creating .env file." )
                #     env_file = open( ".env", "w" )
                #     env_file.write( "FTP_USER="     + input( "Enter FTP user name: " ))
                #     env_file.write( "FTP_PASSWORD=" + input( "Enter FTP password:  " ))
                #     env_file.close()
                #     print( "FTP_USER and FTP_PASSWORD environment variables set. Please restart the program." )
                #     sys.exit()
                    
                ftp.login( ftp_user, ftp_password )  
                print( "Logged into americansjewelry.com" )  # connection message from server is printed on stdout (screen)
                try:  
                    ftp.set_pasv( True )  # set passive mode on.  jewelry machine picky about this lately..
                    print( "Set passive mode on" )  # connection message from server is printed on stdout (screen)
                    try:
                        ftp.cwd( self.libraryPath )  # change to directory /public_html/scoreprolibraries/tennis_libraries
                        ftp.retrbinary( 'RETR ' + self.zipFile, open( self.zipFile, 'wb' ).write ) # ftp get zipFile
                    except ftplib.error_perm:  # catch exception if directory does not exist on server
                        print( "Error: " + self.libraryPath + " does not exist on server" )  # connection message from server is printed on stdout (screen)
                except ftplib.error_perm:  # catch exception if directory does not exist on server
                    print( "Error: could not set passive mode on" )  # connection message from server is printed on stdout (screen)
            except ftplib.error_perm:  # catch exception if username or password are incorrect
                print( "Error: could not log in" )  # connection message from server is printed on stdout (screen)
        except ftplib.all_errors as e:  # catch all other exceptions, including socket errors and timeout errors, etc.
            print( "Error connecting to americansjewelry.com" )  # connection message from server is printed on stdout (screen)
            print( e )  # print exception error message
        ftp.quit()  # close ftp connection
        print( "Closed FTP connection" )  # connection message from server is printed on stdout (screen)

