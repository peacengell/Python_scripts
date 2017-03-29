# Linux Hardening script
# Still in progress .... 

# Working on this slowly slowly


import os


CONFIG_DIR = "/etc"
GET_DIR = os.getcwd()

list_dir = os.listdir(os.getcwd())


def check_ect_folder():
    
    if "etc" in list_dir:
        print("The etc dir exist, hence moving into the etc directory")
        os.chdir(GET_DIR + "/" + CONFIG_DIR)
        print(os.getcwd())
        print(os.listdir("."))
        

    else:
        os.mkdir("etc")


def check_ect_folder_writable():

    etc_writable = os.access(GET_DIR + "/" + CONFIG_DIR, os.W_OK) 
    if etc_writable == True:
        print("Directory is writable")

def read_etc_hosts_file():
    
    if os.path.isfile(GET_DIR + "/" + CONFIG_DIR+"/hosts"):

        with open(GET_DIR + "/" + CONFIG_DIR+"/hosts") as host_file:
            host_readline = host_file.read()
          

def write_into_etc_host_file():
    
    ''' write_into_etc_host_file if ip not found '''

    ip_address = input("Please enter ns1 or n2 Ip address: ")
   
    if os.path.isfile(GET_DIR + "/" + CONFIG_DIR+"/hosts"):
    
        with open(GET_DIR + "/" + CONFIG_DIR+"/hosts") as host_file:
            host_readline = host_file.read().splitlines()

            Address = []
            for line in host_readline:
                Ip_add = line.split(' ')
                Address.append(Ip_add[0])

            if  ip_address in Address:

                print("Exit nothing to do")

            else:
                print("writing " + ip_address + " into the hostfile")
                with open(GET_DIR + "/" + CONFIG_DIR+"/hosts", 'a') as host_file:
                    host_file.write('\n'+ip_address)

check_ect_folder()
check_ect_folder_writable()
read_etc_hosts_file()
write_into_etc_host_file()
