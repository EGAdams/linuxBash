# module to pull zip file from the jewelry machine
# create the ftp object
# get the zip file
# close the ftp object
import ftplib
import os

class PullZipFile:
    def __init__( self ):
        print( "pull object initialized." )
     
    def execute( self, zipFile ):
        try:
            ftp = ftplib.FTP('americansjewelry.com')  # connect to host, default port
            print( "Connected to americansjewelry.com" )  # connection message from server is printed on stdout (screen)
            try:  # login with username and password - passwd is being sent in clear text
                ftp_user     = os.environ.get( "FTP_USER"     )  # get the login an password from the environment variables
                ftp_password = os.environ.get( "FTP_PASSWORD" )
                if ftp_user == None or ftp_password == None: # create the .env file if it does not exist
                    print( "FTP_USER or FTP_PASSWORD environment variables not set. Creating .env file." )
                    env_file = open( ".env", "w" )
                    env_file.write( "FTP_USER="     + input( "Enter FTP user name: " ))
                    env_file.write( "FTP_PASSWORD=" + input( "Enter FTP password:  " ))
                    env_file.close()
                    print( "FTP_USER and FTP_PASSWORD environment variables set. Please restart the program." )
                    sys.exit()
                    
                ftp.login( ftp_user, ftp_password )   
                print( "Logged into americansjewelry.com" )  # connection message from server is printed on stdout (screen)
                try:  
                    ftp.set_pasv( True )  # set passive mode on
                    print( "Set passive mode on" )  # connection message from server is printed on stdout (screen)
                    try:  # change to directory /public_html/scoreprolibraries/tennis_libraries
                        ftp.cwd( '/public_html/scoreprolibraries/tennis_libraries' )
                        # ftp get zipFile
                        ftp.retrbinary( 'RETR ' + zipFile, open( zipFile, 'wb' ).write )
                        
                    except ftplib.error_perm:  # catch exception if directory does not exist on server
                        print( "Error: could not change to /public_html/scoreprolibraries/tennis_libraries" )
                except ftplib.error_perm:  # catch exception if directory does not exist on server
                    print( "Error: could not set passive mode on" )  # connection message from server is printed on stdout (screen)

            except ftplib.error_perm:  # catch exception if username or password are incorrect
                print( "Error: could not log in" )  # connection message from server is printed on stdout (screen)

        except ftplib.all_errors as e:  # catch all other exceptions, including socket errors and timeout errors, etc.
            print( "Error connecting to americansjewelry.com" )  # connection message from server is printed on stdout (screen)
            print( e )  # print exception error message

        ftp.quit()  # close ftp connection
        print( "Closed FTP connection" )  # connection message from server is printed on stdout (screen)

