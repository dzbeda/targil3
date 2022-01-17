import logging
import os
import zipfile
import time

                                                    ## Functions ##

def create_file(full_file_name):
    open(full_file_name,'w+')
    #time.sleep(20)  #Using sleep will give you the option to delete the file manually in order to check the if statment in case the file was not created
    if os.path.exists(full_file_name) == True:
        print(full_file_name+"File exists")
        logging.info("Created filename: " + filename + file_extension + " under " + file_path)
    else:
        print("Failed to create file  - exiting")
        logging.error("Could not create filename: " + filename + file_extension + " under " + file_path + " exiting")
        exit()

def create_zip(zip_file_name,full_file_name):
    handle = zipfile.ZipFile(zip_file_name,"w")
    handle.write(full_file_name,compress_type= zipfile.ZIP_DEFLATED)
    handle.close()
    #time.sleep(20)  #Using sleep will give you the option to delete the file manually in order to check the if statment in case the file was not created
    if os.path.exists(zip_file_name) == True:
        print(zip_file_name+"ZIP File exists")
        logging.info("Created filename: " + zip_file_name + " under " + zip_file_path)
    else:
        print("Failed to create file  - exiting")
        logging.error("Could not create filename: " + zip_file_name + " under " + zip_file_path + " exiting")
        exit()

                                             ####  variables   #####
## Log file parameters ##
logFile = '/data/dudu-private/assignments/targil3/files/output.log'
logging.basicConfig(filename=logFile,filemode='a',format='%(asctime)s - %(levelname)s - %(message)s' , level=logging.INFO)


## Program variables ##
files = {'a','b','c','d'}
file_extension= '.txt'
file_path='/data/dudu-private/assignments/targil3/files/'  #define the path were txt files will be created
zip_file_path= '/data/dudu-private/assignments/targil3/'   #define the path were zip files will be created
version=os.getenv('VERSION')


                                                        ## Start program ##
if os.getenv('VERSION') is not None:
    print(version)
    version = os.getenv('VERSION')
    logging.info("Running version is: " + version)
else:
    print("env VERSION is not defined - exiting")
    logging.error("env VERSION is not defined - exiting")
    exit()

for filename in files:
    full_file_name = file_path+filename+file_extension
    create_file(full_file_name)
    zip_file_name = zip_file_path+filename+"_"+version+".zip"
    create_zip(zip_file_name,full_file_name)

