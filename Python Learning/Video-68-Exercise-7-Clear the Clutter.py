
import os
import glob

def rename_files_with_format(folder_path, file_format):
    search_pattern = os.path.join(folder_path, f'*.{file_format}')
    files = glob.glob(search_pattern)

    for index, file_path in enumerate(files, start=1):
        new_file_name = f"{index}.{file_format}"
        new_file_path = os.path.join(folder_path, new_file_name)
        os.rename(file_path, new_file_path)

folder = 'C:\\Users\\saswa\\Desktop\\python exercise 7'
format_to_check = input("Enter the file format (e.g., 'png', 'txt'): ")  # Example: 'txt', 'jpg', 'pdf', etc.

rename_files_with_format(folder, format_to_check)

print(f"Renamed {format_to_check} files in the folder.")


or

import os

files = os.listdir("clutteredFolder")
i = 1
for file in files:
  if file.endswith(".png"):
    print(file)
    os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}.png")
    i = i + 1

# info

# what is os.rename?
# ChatGPT said:
# ChatGPT
# os.rename is a function in Python's os module that is used to rename a file or directory. This function can be used to move a file or directory within the same filesystem by renaming it, or simply to give it a new name.
#
# Syntax
# python
# Copy code
# os.rename(src, dst)
# Parameters
# src: The source file or directory you want to rename.
# dst: The new name for the file or directory, or the destination path to move the file or directory to.
# Example
# python
# Copy code
# import os
#
# # Rename a file
# os.rename('old_filename.txt', 'new_filename.txt')
#
# # Move and rename a file
# os.rename('old_directory/filename.txt', 'new_directory/new_filename.txt')
# Important Notes
# If dst is an existing file or directory, os.rename will overwrite it without warning.
# If the source file or directory does not exist, or if you lack the necessary permissions, an OSError will be raised.
# On some platforms (e.g., Windows), os.rename cannot be used to move a file across different filesystems. For such cases, you can use shutil.move.
# Usage Scenarios
# Renaming Files: Changing the name of a file in the same directory.
# Moving Files: Moving a file from one directory to another, possibly changing its name at the same time.
# Renaming Directories: Changing the name of a directory.





