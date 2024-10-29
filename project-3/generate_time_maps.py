import subprocess
import time
import os

# covert_file:
# Convert filename and URI pairs to dictionary 
# key = filename
# value = uri
def convert_file(path):
    uri_dict = {}
    file = path

    with open(file, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        l = line.split(',')
        temp = l[0]
        hash_name = temp[:31]
        uri_dict[hash_name] = l[1]
    
    return uri_dict

# get_maps:
# For each value contained in dictionary...
#   Create memgator command containing current uri
#   Pass memgator command to subprocess
#       # If subprocess returns 1, then error occurred. Check stderr on subprocess for details 
#   Write output to JSON file for parsing   
#   Pause for 20 seconds
#   Continue
def get_maps(uri_dict):
    output_dir = './time-maps'
    for key, value in uri_dict.items():
        file_name = key + ".json"
        output_filepath = os.path.join(output_dir, file_name)
        uri = value.strip()
        memgator_command = [
            'memgator',
            '-c',
            '"ODU CS432/532 cskee004@odu.edu"',
            '-a',
            './resources/updated_archives.json',
            '-F',
            '2',
            '-f',
            'JSON',
            uri
        ]
        print(memgator_command[9])
        with open(output_filepath, 'w') as output_file:
            subprocess.run(memgator_command, stdout=output_file)
        time.sleep(20)
        


#test_dict = {}
#test_dict['78c426e850ad376854627ac9ef77f068'] = ['https://finance.yahoo.com/']

path = './resources/key-uri.txt'
processed_dict = convert_file(path)
get_maps(processed_dict)







