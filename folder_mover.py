# Make a temporary directory to archive.zip in.
# unzip archive.zip in that directory
# tennis_cpp_directory = "/mnt/c/Users/EG/Desktop/2022/june/2nd_week/tennis_cpp"
# for each folder in the directory that the archive created:
  # delete the contents of the associated folder that is in the tennis_cpp_directory.
  # move the contents from the directory of the unzipped archive to the directory with in the tennis_cpp_directory

import shutil
import os
import zipfile

class FolderMover:
    def __init__( self ):
        print( "initializing Folder Mover class..." )

    def execute( self, zip_file ):
        tennis_cpp_directory = "/mnt/c/Users/EG/Desktop/2022/june/2nd_week/tennis_cpp"
        os.mkdir( "temp" )
        shutil.move( zip_file, os.path.join( "temp", zip_file )) # move archive.zip to the temp directory

        with zipfile.ZipFile( "./temp/" + zip_file, 'r') as zip_ref: # unzip archive.zip in that directory
            zip_ref.extractall( "./temp" )

      
        for folder in os.listdir( "./temp" ): # for each folder in the directory that the archive created:
            print ( folder )
           
            if folder.endswith( ".zip" ) or folder == "Morse":  #continue if Morse dir or it is a .zip file
                print( "skipping zip file or Morse directory... " )
                continue

            # delete the contents of the associated folder that is in the tennis_cpp_directory.
            for file in os.listdir( os.path.join( tennis_cpp_directory, folder ) ):
                os.remove( os.path.join( tennis_cpp_directory, folder, file ) )

            # move the contents from the directory of the unzipped archive to the directory with in the tennis_cpp_directory
            for file in os.listdir( os.path.join( "./temp", folder ) ):
                shutil.move( os.path.join( "./temp", folder, file ), os.path.join( tennis_cpp_directory, folder, file ) )
            
        shutil.rmtree( "./temp" ) # delete the temp directory
        