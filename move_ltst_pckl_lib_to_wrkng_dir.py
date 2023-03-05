
# create menu of files to choose from
# wait for user to choose a file
# pull the chosen file from the server, unzip it, and move the files to the working directory

import file_list_module
import file_puller_2  as filePuller
import folder_mover_2 as folderMover

def print_menu(files):
    for i, file in enumerate(files):
        print("{}. {}".format(i + 1, file))

    print("{}. Exit".format(len(files) + 1))

def main():
    chosen_zip_file = ""
    workingPickleballDirectory  = "/mnt/c/Users/EG/Desktop/2022/may/2nd_week/pickle_cpp"
    pickleballLibraryServerPath = "/public_html/scoreprolibraries/chinese_remote_system"             # path to the pickleball libraries on the server
    listGenerator               = file_list_module.PopulateFileList( pickleballLibraryServerPath )
    files                       = listGenerator.execute()
    files.sort()
    while True:
        print_menu(files)
        choice = input("Choose a file: ")
        if choice == str(len(files) + 1):
            break
        try:
            choice = int(choice) - 1
            print(files[choice])
            chosen_zip_file = files[ choice ]
            break
        except ValueError:
            print("Invalid input")

        except IndexError: 
            print("Invalid input")
    
    pickleballFilePuller       = filePuller.PullZipFile(   chosen_zip_file, pickleballLibraryServerPath ) # create a file puller object
    mover                      = folderMover.FolderMover( chosen_zip_file, workingPickleballDirectory  ) # create a folder mover object
    
    pickleballFilePuller.execute()  # pull the chosen file from the server
    mover.execute()                 # move the extracted files to the working directories

if __name__ == '__main__':
    main()
