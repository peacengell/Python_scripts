# This script will read the TEMP directory found
# in the argument supply and date. 
# an will clear every files that is more that 5 days old

# Fist steps Read the Directory and make a list of files found.

import os
from sys import argv
from datetime import datetime, timedelta
"""all module needed has been imported"""

all = argv[1:]

directory, days = all


def find_all_files_dir_and_subdir(directory):
    
    files_found = []
    
    for root, dirs, files in os.walk(directory):

        for file in files:
            files_found.append(os.path.join(root, file))

    #return files_found
    print(files_found)
    
    
find_all_files_dir_and_subdir(directory)


