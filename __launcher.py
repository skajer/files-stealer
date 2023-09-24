import os
import shutil
import subprocess
import time
from string import digits
from datetime import datetime
import sys
import smtplib
import ssl


def emails(email, port):
    
    port = 465 
    email = "email@gmail.com"
    context = ""

    with smtplib.SMTP_SSL(email,port,context=context) as server:
        server.login(email, password="")
        server.send_message()
        #....
        #....


def diff(list1, list2):
    list_difference = [item for item in list1 if item not in list2]
    return list_difference

def copy_with_progress(src, dst):
    total_size = sum(os.path.getsize(os.path.join(root, file)) for root, _, files in os.walk(src) for file in files)
    bytes_copied = 0

    for root, dirs, files in os.walk(src):
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(dst, os.path.relpath(src_file, src))

            if not os.path.exists(os.path.dirname(dst_file)):
                os.makedirs(os.path.dirname(dst_file))

            shutil.copy2(src_file, dst_file)
            bytes_copied += os.path.getsize(src_file)

            
            progress = min(100, int(bytes_copied / total_size * 100))
    print(f"\rCopying... [{('#' * (progress // 5)).ljust(20)}] {progress}% complete", end="")
    sys.stdout.flush()

if __name__ == '__main__':
    save_path = "C:/save_files"
    dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    uncheckeddrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    x = diff(uncheckeddrives, drives)

    while True:
        if x:
            print("New drives:     " + str(x))
            print("New drive introduced")
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
                            print("Copying...")

                            path_check_size = save_path + pc_name + datetime_help

                            try:
                                copy_with_progress(drive_litter, os.path.join(save_path, pc_name, datetime_help))
                            except Exception as e:
                                print("Error while copying:", e)

                            print("\nCopied successfully!")
                        
                break

        x = diff(drives, uncheckeddrives)

        if x:
            print("Removed drives: " + str(x))
            print("Drive disconnected")

        drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
        time.sleep(1)