#!/usr/bin/env python
# coding: utf-8

# In[29]:


import os, shutil

''' path = r'path_directory'  -> Specfies path of the directory for the code 
os.listdir(path)  --> make list of directories for the path 
os.path.exists(path) --> Check if the path exists or not 
os.makedirs(path) --> create path 
shutil.move(from_path , to_path)In the code, we'll use OS library to check directory, create list of directories and create folders required for moving the files.
SHUTIL is used  for moving the files from the original directory to the one formed by OS libraryWe'll get list of files from the directory and we'll use split function to get the extension of the files which will be used for getting the required folders for movement. We can also make dictionary for the file_name and file_type so that the specified files will be moved to the values of that particular key. We'll loop over and create the folder if it doesn't exists and with the help of SHUTIl we'll move over the files '''

# In[30]:


path = r'[ENTER_PATH]'


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


