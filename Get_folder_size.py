# Get folder size 



import os

BYTES_IN_GIGABYTE = 1073741824
GIGABYTE_DISPLAY_LIMIT = 2
ACCESS_ERROR_CODE = 13

def get_folder_size(filepath):
    size = os.path.getsize(filepath)
    try:
        for item in os.listdir(filepath):
            item_path = os.path.join(filepath, item)
            try:
                if os.path.isfile(item_path):
                    size += os.path.getsize(item_path)
                elif os.path.isdir(item_path):
                    size += get_folder_size(item_path)
            except OSError as err:
                if err.errno == ACCESS_ERROR_CODE:
                    print('Unable to access ' + item_path)
                    continue
                else:
                    raise
    except OSError as err:
        if err.errno != ACCESS_ERROR_CODE:
            raise
        else:
            print('Unable to access ' + filepath)
    return size

def get_all_folder_sizes(root_filepath):
    folders = []
    for item in os.walk(root_filepath):
        if os.path.isdir(os.path.join(root_filepath, item[0])):
            folders.append([item[0], get_folder_size(item[0])])
    return folders

def convert_bytes_to_gigabytes(bytes):
    return bytes / BYTES_IN_GIGABYTE

def main():
    folder_sizes = get_all_folder_sizes('C:\\')
    folder_sizes.sort()
    for folder in folder_sizes:
        gigabytes = convert_bytes_to_gigabytes(folder[1])
        if gigabytes > GIGABYTE_DISPLAY_LIMIT:
            print(folder[0] + ' = ' + format(gigabytes, '.2f') + ' GB')

if __name__ == '__main__':
    main()
