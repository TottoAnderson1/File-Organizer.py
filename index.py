import os #this module provides a way of using operating system-indepentent fuctionality like reading or writing to the file system.
import shutil  # this module helps perfoming in high-level operation on folder and collection of files.

#define the main functions

def organize_directory(directory): # Define a dictionary to map file extensions to folder names 
    file_types = { 'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'], 'documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'], 'audio': ['.mp3', '.wav', '.aac'], 'video': ['.mp4', '.mkv', '.flv', '.avi'], 'archives': ['.zip', '.rar', '.tar', '.gz'] } # Create folders for each file type 
    for folder in file_types.keys(): 
        folder_path = os.path.join(directory, folder) 
        if not os.path.exists(folder_path): 
            os.makedirs(folder_path) 

# Iterate over files in the specified directory 
    
    for filename in os.listdir(directory): 
        file_path = os.path.join(directory, filename) 
        if os.path.isfile(file_path): 
            # Ignore directories 
            move_file_to_folder(file_path, file_types, directory)

#Define the function to move files

def move_file_to_folder(file_path, file_types, directory): 
    # Get the file extension _, 
    file_extension = os.path.splitext(file_path) 
    # Move the file to the appropriate folder 
    for folder, extensions in file_types.items(): 
        if file_extension in extensions: 
            destination_folder = os.path.join(directory, folder) 
            shutil.move(file_path, destination_folder) 
            break

if __name__ == "__main__": 
    # Specify the directory to be organized 
    directory_to_organize = "C:\Users\User\OneDrive\Documents\FX NEW\FXTDR" 
    # Call the main function to organize the directory 
    organize_directory(directory_to_organize)

#Running the Script

#Replace "path_to_your_directory" with the actual path of the directory you want to organize.

#Explanation of the Script

#Import Modules: The script begins by importing the os and shutil modules to interact with the file system and move files.
#Main Function: The organize_directory function is responsible for organizing files. It creates folders for different file types and then moves each file into the appropriate folder.
#Move Files Function: The move_file_to_folder function handles the logic for moving files based on their extensions.
#Script Entry Point: The if __name__ == "__main__": block ensures that the script runs when executed directly.