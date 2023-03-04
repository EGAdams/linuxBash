
# create menu of files to choose from
# wait for user to choose a file
# pull the chosen file from the server


import tennis_list_module
import file_puller
import folder_mover

def print_menu(files):
    for i, file in enumerate(files):
        print("{}. {}".format(i + 1, file))

    print("{}. Exit".format(len(files) + 1))


def main():
    chosen_zip_file = ""
    listGenerator = tennis_list_module.TennisList()
    files = listGenerator.populate_list()
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

    filePuller = file_puller.PullZipFile() # create a file puller object
    filePuller.execute( chosen_zip_file )  # pull the chosen file from the server
    mover = folder_mover.FolderMover()     # create a folder mover object
    mover.execute( chosen_zip_file )       # move the extracted files to the tennis_cpp directories

if __name__ == '__main__':
    main()
