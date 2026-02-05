import os
import shutil

# Ask user to enter folder path
folder_path = input("Enter the folder's path: ")

# Check if the folder path is correct
if not os.path.exists(folder_path):
    print("Folder not found! Please check the path.")
    exit()

# Check if it's a folder
if not os.path.isdir(folder_path):
    print("That's not a folder!")
    exit()

# Returns a list of names in a directory
files = os.listdir(folder_path)

# Group Files by Type
file_groups = {}  # empty dictionary

for file in files:
    # Exclude your own script from being organized
    if file == "file_organizer.py":
        continue  

    #Build path from current directory
    file_path = os.path.join(folder_path, file)
    
    # Check if it's a file
    if os.path.isfile(file_path):
        #Get the extension by separating the file from extension
        extension = os.path.splitext(file)[-1]
        
        # If key doesn't exist, add new content to dictionary
        if extension not in file_groups:
            file_groups[extension] = [file]
        # If key exist, add values to the list inside the dictionary
        else:
            file_groups[extension].append(file)

# Show preview
print("\nPreview of changes:")

for extension, file_list in file_groups.items():
    folder_name = extension[1:] + "_files"
    print(f"\n{folder_name}/ ({len(file_list)} files)")
    for file in file_list:
        print(f"  - {file}")

# Ask for confirmation
response = input("\nProceed with organizing? (y/n): ")

if response == "y":
    print("\nOrganizing files...")

    for extension, file_list in file_groups.items():
        # Build path from current directory
        folder_name = os.path.join(folder_path, extension[1:] + "_files")

        # Create a folder for this extension (handle if it exists)
        os.makedirs(folder_name, exist_ok=True)

        #Move each file to the folder based on extension
        for file in file_list:
            source = os.path.join(folder_path, file)
            shutil.move(source, folder_name)

        print(f"{folder_name} : {len(file_list)} files")

    print("\nFiles organized successfully!")

else:
    print("\nOrganization cancelled!")



