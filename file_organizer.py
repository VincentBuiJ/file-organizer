#Separate Files from Folders
import os

#Returns a list of names in a directory
files = os.listdir()

#loop through each file to check if its a file
for file in files:
    if file == "file_organizer.py":
        continue  # skip this file
    
    #get full path of the selected folder
    file_path = os.path.join("../python_projects", file)
    if os.path.isfile(file_path):
        #Extract File Extensions
        extension = os.path.splitext(file)[-1]
        print(f"File: {file}, Extension: {extension}")

#Group Files by Type
file_groups = {}  # empty dictionary
for file in files:
    #Exclude your own script from being organized
    if file == "file_organizer.py":
        continue  

    #Combine the folder path with the filename
    file_path = os.path.join("../python_projects", file)
    if os.path.isfile(file_path):
        #Get the extension by separating the file from extension
        extension = os.path.splitext(file)[-1]
        if extension not in file_groups:
            file_groups[extension] = [file]
        else:
            file_groups[extension].append(file)

#Create Folders and Move Files
import shutil

# After you've built your file_groups dictionary:
for extension, file_list in file_groups.items():
    # Create a folder for this extension (handle if it exists)
    folder_name = extension[1:] + "_files"
    os.makedirs(folder_name, exist_ok=True)
    # Move file to the folder
    for file in file_list:
        shutil.move(file, folder_name)

print("✅ Files organized successfully!")









