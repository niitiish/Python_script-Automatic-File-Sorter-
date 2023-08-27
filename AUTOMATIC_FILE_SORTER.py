#!/usr/bin/env python
# coding: utf-8

# In[29]:


import os, shutil

path = r'path_directory'  -> Specfies path of the directory for the code 
os.listdir(path)  --> make list of directories for the path 
os.path.exists(path) --> Check if the path exists or not 
os.makedirs(path) --> create path 
shutil.move(from_path , to_path)In the code, we'll use OS library to check directory, create list of directories and create folders required for moving the files.
SHUTIL is used  for moving the files from the original directory to the one formed by OS libraryWe'll get list of files from the directory and we'll use split function to get the extension of the files which will be used for getting the required folders for movement. We can also make dictionary for the file_name and file_type so that the specified files will be moved to the values of that particular key. We'll loop over and create the folder if it doesn't exists and with the help of SHUTIl we'll move over the files 

# In[30]:


path = r'C:/Users/nitis/Downloads/'


# In[31]:


# This code will create folders and checks for existing folders (if any)

files = os.listdir(path)
files_dict = dict()
for file in files :
    file_plus_extension = file.split('.')
    extension = file_plus_extension[len(file_plus_extension)-1]
    files_dict[file] = extension
for extension in files_dict.values():
    if os.path.exists(path + extension) == True :
        pass 
    else :
        os.makedirs(path + extension)
        


# In[32]:


# This code will move the files to specific folders 

for file,extension in files_dict.items() :
    shutil.move( path + file , path + extension +'/'+ file )


# In[ ]:


import os, shutil

# Define the path of the directory that contains the files to be moved
path = r'[PATH_OF_FOLDER]'

# Use the os.listdir method to get a list of all files in the specified directory
files = os.listdir(path)

# Create an empty dictionary to store each file and its extension
files_dict = dict()

# Loop through all files in the directory and store their extensions in the files_dict dictionary
for file in files :
    # Split the file name and extension by using the '.' separator and store it as a list
    file_plus_extension = file.split('.')
    # Get the last element of the list, which is the file extension
    extension = file_plus_extension[len(file_plus_extension)-1]
    # Add the file and its extension to the files_dict dictionary
    files_dict[file] = extension

# Loop through all values in the files_dict dictionary (i.e., all file extensions)
for extension in files_dict.values():
    # Check if a directory with the same name as the extension already exists in the specified path
    if os.path.exists(path + extension) == True :
        # If the directory already exists, do nothing and move on to the next iteration of the loop
        pass 
    else :
        # If the directory does not exist, create a new directory with the extension name in the specified path
        os.makedirs(path + extension)

# Loop through all items (i.e., file names and their extensions) in the files_dict dictionary
for file,extension in files_dict.items() :
    # Use the shutil.move method to move each file to a new directory with the same name as its extension
    shutil.move( path + file , path + extension +'/'+ file )

