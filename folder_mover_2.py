# Make a temporary directory to archive.zip in and unzip archive.zip in that directory
# for each folder in the directory that the archive created:
  # delete the contents of the associated folder that is in the self.workingDirectory.
  # move the contents from the directory of the unzipped archive to the directory with in the self.workingDirectory
import shutil
import os
import zipfile
class FolderMover:
    def __init__( self, zipFileArg, workingDirectoryArg ):
        self.zippedFile       = zipFileArg
        self.workingDirectory = workingDirectoryArg
        print( "Folder Mover class initialized." )

    def execute( self ):
        os.mkdir( "temp" )
        shutil.move( self.zippedFile, os.path.join( "temp", self.zippedFile )) # move archive.zip to the temp directory

        with zipfile.ZipFile( "./temp/" + self.zippedFile, 'r') as zip_ref: # unzip archive.zip in that directory
            zip_ref.extractall( "./temp" )

        for folder in os.listdir( "./temp" ): # for each folder in the directory that the archive created:
            print ( folder )
            if folder.endswith( ".zip" ) or folder == "Morse": #continue if it is a .zip file or the folder is named "Morse"
                print( "skipping this data... \n" )
                continue

            # delete the contents of the associated folder that is in the self.workingDirectory.
            for file in os.listdir( os.path.join( self.workingDirectory, folder )):
                os.remove( os.path.join( self.workingDirectory, folder, file ))

            # move the contents from the directory of the unzipped archive to the directory with in the self.workingDirectory
            for file in os.listdir( os.path.join( "./temp", folder )):
                shutil.move( os.path.join( "./temp", folder, file ), os.path.join( self.workingDirectory, folder, file ))
            
        shutil.rmtree( "./temp" ) # delete the temp directory


            

