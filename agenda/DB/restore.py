#!/usr/bin/python
###########################################################
#
# This python script is used for mysql database backup
# using mysqldump utility.
#
# Written by : Rahul Kumar
# Website: http://tecadmin.net
# Created date: Dec 03, 2013
# Last modified: Dec 03, 2013
# Tested with : Python 2.6.6
# Script Revision: 1.1
#
##########################################################

# Import required python libraries
import os
import time
import datetime
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# MySQL database details to which backup to be done. Make sure below user having enough privileges to take databases backup. 
# To take multiple databases backup, create any file like /backup/dbnames.txt and put databses names one on each line and assignd to DB_NAME variable.

DB_HOST = 'localhost'
DB_USER = 'postgres'
DB_USER_PASSWORD = '000000'
DB_NAME = 'agenda'
BACKUP_PATH = '/backup/dbbackup/'
FILE_BK = BASE_DIR + '/agenda.sql'
# Getting current datetime to create seprate backup folder like "12012013-071334".
DATETIME = time.strftime('%m%d%Y-%H%M%S')

TODAYBACKUPPATH = BASE_DIR


# Checking if backup folder already exists or not. If not exists will create it.
print ("creating backup folder")
if not os.path.exists(TODAYBACKUPPATH):
    os.makedirs(TODAYBACKUPPATH)

# Code for checking if you want to take single database backup or assinged multiple backups in DB_NAME.
print ("checking for databases names file.")
if os.path.exists(FILE_BK):
    multi = 1
    print ("El fichero existe "+FILE_BK)
else:
    print ("El fichero no existe "+FILE_BK)
    multi = 0

# Starting actual database backup process.
if multi:
   
     db = DB_NAME
     password = '000000'
     filename = TODAYBACKUPPATH + "/" + db + ".sql"
     
     command = 'export PGPASSWORD=%s\ncat %s | psql %s -U %s -h %s' % (DB_USER_PASSWORD, FILE_BK, DB_NAME , DB_USER,DB_HOST)
     print(command)
     os.system(command)
     print ("Restore DB script completed")