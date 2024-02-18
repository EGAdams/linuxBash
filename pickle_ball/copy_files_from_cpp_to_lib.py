# for each folder in the source directory, find the folder with the same name in the destination directory
# overwrite the contents of the folder in the destination directory with the content of the folder from the source directory

import os
source_directory      = "/mnt/c/Users/EG/Desktop/2022/may/2nd_week/pickle_cpp"
# destination_directory = "/mnt/c/Users/EG/Desktop/2022/june/3rd_week/pickleball_library"
destination_directory = "/mnt/c/Users/EG/libraries"

for folder in os.listdir(source_directory):
    if os.path.isdir(os.path.join(source_directory, folder)):
        if ".git" in folder or ".vscode" in folder or "node_modules" in folder or "pin_data" in folder \
             or "build" in folder or "TranslateConstant" in folder or "Arduino" in folder or "Morse" in folder:
            continue
        
        # if the folder is not in the destination directory, create it
        if not os.path.isdir(os.path.join(destination_directory, folder)):
            print( "*** new directory found! ***" )
            print("creating the folder " + folder + " in the destination directory")
            os.system("mkdir \"" + destination_directory + "/" + folder + "\"")

        for file in os.listdir( os.path.join( source_directory, folder )):
            # continue if the file contains ".txt" or ".git"
            if ".txt" in file or ".git" in file or ".sln" in file or ".gypi" in file or ".vcxproj" in file \
               or ".js" in file or ".DS_Store" in file:
                continue

            if os.path.isfile(os.path.join(source_directory, folder, file)):
                print("copying " + file + " from " + source_directory + " to "                              + destination_directory + "/" + folder + "\"" )
                os.system("cp \""                  + source_directory + "/" + folder + "/" + file + "\" \"" + destination_directory + "/" + folder + "\"" )
            else:
                print( folder + "/" + file + " is not a file" )
                print( "exiting process..." )
                exit()
