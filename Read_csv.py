# This is the final script.

# Importing csv modules.
import csv
import os
import sys

class OpenFile:

    def readfile(self, filename):
        self.filename = filename
        
    def search_by_env(self, patern, OpenFile):
        self.patern = patern
        
        with open(filename, 'r', newline='') as f:
            reader = csv.DictReader(f)
            print(str(patern))
            for row in reader:
                if patern in row['Environment']:
                    print(row['Application Name'])



read = OpenFile()

dn = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dn,"List_of_Migrated_Server.csv")

print(read.search_by_env(filename, "UAT"))


#Application_Name
#Environment
#server_hostname
#Overall_ORT_Status
#Migration_Date
#Migration_Approach
#Source_server_hostname
#source_server_role
#Source_server_OS_version
#server_OS_version
#server_Front_IP_address
#server_Admin_Address
