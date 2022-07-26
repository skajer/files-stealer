
#TODO 1. Check size of folder/folders that script copies,  2. Add timer to the end of copying,  3. Work on if statements, 4. Add progress bar or smth, 5. sending email ~ hour
#* 1 - 
#* 2 - 
#* 3 ✓
#* 4 - 

#! USE THIS SCRIPT FOR YOUR OWN RISK 

#? THIS SCRIPT IS MONITORING THAT IF NEW DEVICES (PENDRIVES) ARE  

import os
from socket import herror 
import time 
import shutil
import subprocess
import smtplib
from string import digits
from datetime import datetime, timedelta
from distutils.dir_util import copy_tree
#import pseduo_progress_bar


if os.name != "nt":
    exit()

def script():
    print('')

if __name__ == '__main':
    script()

def diff(list1, list2):
    list_difference = [item for item in list1 if item not in list2]
    return list_difference

def choice():

    print("Choice 1 to send emails: ")
    user_choice = int(input())

    if user_choice == 1:
       # mails():
        pass


def main():

    save_path = "C:/save_files" ### whatever path you want 

    dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]

    print(drives)
    pass

    uncheckeddrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]

    x = diff(uncheckeddrives, drives)

    while True:

        if x:
            print("New drives:     " + str(x))
            print("New dive introduced")
            print("...")

            pc_name = os.environ['COMPUTERNAME']
            
            out = subprocess.check_output('wmic logicaldisk get  DriveType, caption', shell=True)

            while True: 

                for drive in str(out).strip().split('\\r\\r\\n'):
                        
                    if '2' in drive:                
                        drive_litter = drive.replace(' ', '').translate({ord(k): None for k in digits}) + '/'

                        print(drive_litter)
                        print("\n")

                        datetime_help = datetime.now().strftime("%Y%m%d_%H%M%S")

                        if os.path.exists(drive_litter):
                            print("copying...   ")              #prograss bar here

                            #progras_bar_here() >>>> 

                            path_check_size = save_path + pc_name + datetime_help

                            try:
                                shutil.copytree(drive_litter, os.path.join(save_path, pc_name, datetime_help)) 
                            except:
                                Exception, FileNotFoundError

                                print("Drive disconnected, removing target folder...  ")

                                datetime_help = str()

                                print(f"Removing {datetime_help} in {save_path}... % ")
                                try:
                                    s = os.rmdir(save_path + "/" + pc_name + "/" + datetime_help) 
                                    p = (save_path + "/" + pc_name + "/" + datetime_help) 
                                    lk = "Copied succesfully!" + '\n'
                                    print(lk)
                                   
                                except:
                                    #progress_bar here
                                    print("Didn't find the folder")
                                    Exception, FileNotFoundError, IOError

                            # checking folder size

                            lk = "Copied succesfully!" + '\n'
                            print(lk)

                            #size = os.path.getsize(path_check_size)
                            #print(f"Folder weights {size} ...")
                            #time.sleep(0.5)
                            #size_in_MB = size * 1000000
                          #  #print(f"Folder weights {size_in_MB} ...")
                            #time.sleep(0.5)
                            

                            f = open(p)
                            f.seek(0, os.SEEK_END)
                            print('Size of folder is', f.tell(), 'bytes')
                break
                

        x = diff(drives, uncheckeddrives)

        if x:
            print("Removed drives: " + str(x))
            print("Drive disconnected")
        drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]

while True:

    main()
