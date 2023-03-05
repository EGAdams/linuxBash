# module to pull zip file from the jewelry machine
# create the ftp object
# get the zip file
# close the ftp object
import ftplib
import os

class PullZipFile:
    def __init__( self,  zipFileArg, libraryPath,):
        self.zipFile     = zipFileArg
        self.libraryPath = libraryPath
        print( "pull object initialized." )
     
    def execute( self ):
        try:
            ftp = ftplib.FTP('americansjewelry.com')  # connect to host, default port
            print( "Connected to americansjewelry.com" )  # connection message from server is printed on stdout (screen)
            try:  # login with username and password - passwd is being sent in clear text
                ftp.login('tinman72', 'sep02@Th')  
                print( "Logged into americansjewelry.com" )  # connection message from server is printed on stdout (screen)
                try:  
                    ftp.set_pasv( True )  # set passive mode on
                    print( "Set passive mode on" )  # connection message from server is printed on stdout (screen)
                    try:  # change to directory /public_html/scoreprolibraries/tennis_libraries
                        ftp.cwd( self.libraryPath )
                        # ftp get zipFile
                        ftp.retrbinary( 'RETR ' + self.zipFile, open( self.zipFile, 'wb' ).write )
                        
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

