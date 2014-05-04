#!/usr/bin/env python

# a simple code to backup critical directories on your machine to a
# separate local disk mounted on that machine.  Several copies are
# kept and an e-mail is sent at the completion.
#
# M. Zingale (v. 1.0: 2013-02-14)
#
# version 1.1 (2014-01-22)
#
# (use at your own risk...)

import sys
import os
import datetime
import shutil
import smtplib
from email.mime.text import MIMEText


#----------------------------------------------------------------------------
# USER EDITS -- edit the following to customize your backup

# list of directories to backup -- add any directory names here, in
# quotes, relative to your home directory
dirs = ['bin',
        'papers',
        'software']

# home directory -- this is where the dirs live.  Change this to your
# home directory.  Avoid using the '~' -- write out the whole
# directory
backup_home = '/home/username'

# root directory to place the backup -- this should be on a separate
# disk mounted on the local machine.  Make sure this directory exists
backup_root = '/raid/backup/auto/'


# backup prefix name -- this will be prepended to the date for each
# backup stored
backup_prefix = "my-backup-"


# number of old backups to store
NSTORE = 3

# info for e-mailing results -- edit these to have your e-mail
# address.  Note: you must make sure your local machine is capable of
# sending mail.
sender = "your e-mail address here"
receiver = "your e-mail address here"

subjectPass = "Output from backup-machine.py"
subjectFail = "ERROR from backup-machine.py"

outMsg = \
"""
Output from backup-machine.py

"""

# END OF USER EDITS
#-----------------------------------------------------------------------------


# a simple logging facility
class log:
    def __init__(self, str=""):
        self.str = str

    def log(self, str):
        print str,
        sys.stdout.flush()
        self.str += str


# send an e-mail with the results
def report(myStr, subject):
    msg = MIMEText(myStr)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receiver, msg.as_string())
    except SMTPException:
        sys.exit("ERROR sending mail")




# log the output
backupLog = log(outMsg)


# make sure that the output directory exists and if so, get all the
# subdirectories in it
try: oldDirs = os.listdir(backup_root)
except:
    backupLog.log("destination directory is not readable/doesn't exist\n")
    report(backupLog.str,subjectFail)
    sys.exit("directory not readable")


# how many existing backups are in that directory?
backupDirs = []
for dir in oldDirs:
    if (dir.startswith(backup_prefix) and 
        os.path.isdir(backup_root + '/' + dir)):
        backupDirs.append(dir)

backupDirs.sort()
backupDirs.reverse()


# backupDirs now contains a list of all the currently stored backups.
# The most recent backups are at the start of the list.
print "currently stored backups: "
n = 0
while (n < len(backupDirs)):
    print backupDirs[n]
    n += 1


# get ready for the new backups
dt = datetime.datetime.now()
backup_date = str(dt.replace(second=0, microsecond=0)).replace(" ", "_")

backup_dest = os.path.normpath(backup_root) + '/' + backup_prefix + backup_date

try: os.mkdir(backup_dest)
except: 
    backupLog.log("error making directory\n")
    report(backupLog.str,subjectFail)
    sys.exit("Error making dir")


backupLog.log("writing to: %s\n\n" % (backup_dest) )

failure = 0

for d in dirs:

    backupLog.log("copying %s ..." % (d) )

    try: shutil.copytree(os.path.normpath(backup_home) + '/' + d, 
                         os.path.normpath(backup_dest) + '/' + d, 
                         symlinks=True)
    except:
        backupLog.log("ERROR copying\n")
        backupLog.log("aborting\n")
        failure = 1
        break
    
    else:
        backupLog.log(" done\n")


backupLog.log("done!\n")


# if we were successful, then remove any old backups, as necessary
if (not failure):

    # keep in mind that we just stored another backup
    if (len(backupDirs) > NSTORE-1):
        n = NSTORE-1

        while (n < len(backupDirs)):
            rmDir = backup_root + '/' + backupDirs[n]

            backupLog.log("removing old backup: %s\n" % (rmDir) )

            try: shutil.rmtree(rmDir)
            except:
                backupLog.log("ERROR removing %s\n" % (rmDir) )
            
            n += 1


if not failure:
    report(backupLog.str,subjectPass)
else:
    report(backupLog.str,subjectFail)
