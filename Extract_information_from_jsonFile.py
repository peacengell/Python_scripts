# Reading all files found in dir.
# Read a json files.
# Format the output nicely.


import os
import json

def Get_running_dir():

    path = os.getcwd()
    
    files = [f for f in os.listdir(path) if f.endswith('.log')]      
    
    for file in files:
       
        with open(file, 'r') as f:
            
            for line in f :
                data = line
                data_json = json.loads(data)
                date_post = json.loads(data)
                msg = json.loads(data_json['message'])
                date = date_post['datetime']
                
                # Formating the output.
                print("-" * 75)
                print(msg['gender'] ,msg['first_name'], msg['last_name'])
                print("Email :", msg['email'])
                print("Subject :", msg['subject'])
                print("Sub_Subject :", msg['sub_subject'])
                print("Question :", msg['question'])
                print("Store :", msg['store'])
                print("Date :", date['date'][:11])
                print("-" * 75)
 
    
Get_running_dir()
