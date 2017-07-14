#!/usr/bin python

# This script will read the TEMP directory found 
# in [ C:\Users\toto\Documents\Temp ] 
# an will clear every files that is more that 5 days old

# Fist steps Read the Directory and make a list of files found.

import os
from datetime import datetime, timedelta
"""all module needed has been imported"""

def find_all_files_dir_and_subdir(directory):
    
    files_found = []
    
    for root, dirs, files in os.walk(directory):

        for file in files:
            files_found.append(os.path.join(root, file))

    return files_found


def Get_list_from_temp_dir(files_found, days_ago):
   
    ''' This functions Get_list_from_temp_dir checks if files are older than 15 days '''
    ''' Do not take into considerations of path and file name start/contains with Python, python, PYTHON and Taches in the list'''
    
    days_ago = 15
    fithteen_days_ago = datetime.now() - timedelta(days=days_ago)

    for file in files_found:
        if "Python" not in file and "Port" not in file and "Taches" not in file:
            if os.path.islink(file) :
                pass
            else:
                
                 filetime = datetime.fromtimestamp(os.path.getctime(file))

            if filetime < fithteen_days_ago:
                """ Uncoment the line below will print only the files that's are older than days specified""" 
    
                #print("files will be Deleted ", file)
                
                """ Uncoment the line below will remove the files older than days specified""" 
                
                #os.remove(file)

    else:
        print("No file older than 15 Day's Found")
        


if __name__ == '__main__':
    
    from sys import argv    
    all = argv[1:]

    directory, days_ago = all
    if directory == "" and days_ago == " ":
        """This will print how to use this scipt. """
        print("example : python clean.py /tmp  15")
        print("Enter directory eg: /tmp" + " Enter days_ago eg: 10")
    
    else:

        # directory = input("Enter Directory to Scan : ")
        # days_ago = int(input("Enter older days: "))
        Get_list_from_temp_dir(find_all_files_dir_and_subdir(directory), days_ago)
