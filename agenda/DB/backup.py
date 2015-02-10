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
def hacerBackUp():
    # Import required python libraries
    import os
    import time
    import datetime
    from AP_Agenda.settings import BASE_DIR, DB_HOST, DB_USER, DB_USER_PASSWORD, DB_NAME
    #BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # MySQL database details to which backup to be done. Make sure below user having enough privileges to take databases backup. 
    # To take multiple databases backup, create any file like /backup/dbnames.txt and put databses names one on each line and assignd to DB_NAME variable.

    #DB_HOST = 'ec2-54-83-205-46.compute-1.amazonaws.com'
    #DB_USER = 'rmwbyxiytiwdzq'
    #DB_USER_PASSWORD = 'RMxz34GI7yhQV0Cxs_ayf3dMD9'
    #DB_NAME = 'd5snf1vtia97an'
    
    #DB_HOST = 'localhost'
    #DB_USER = 'postgres'
    #DB_USER_PASSWORD = '000000'
    #DB_NAME = 'agenda'
    
    
    BACKUP_PATH = '/agenda/DB/backup/'
    # Getting current datetime to create seprate backup folder like "12012013-071334".
    DATETIME = time.strftime('%m%d%Y-%H%M%S')
    
    TODAYBACKUPPATH = BASE_DIR + BACKUP_PATH + DATETIME
    FILENAME = TODAYBACKUPPATH + "/" + DB_NAME + ".sql"
    
    
    # Checking if backup folder already exists or not. If not exists will create it.
    
    if not os.path.exists(TODAYBACKUPPATH):
        os.umask(0)
        os.makedirs(TODAYBACKUPPATH)
        print ("creating backup folder"+TODAYBACKUPPATH)
    
    # Code for checking if you want to take single database backup or assinged multiple backups in DB_NAME.
    if os.path.exists(FILENAME):
        file1 = open(FILENAME)
        multi = 1
    else:
        multi = 0
    
    # Starting actual database backup process.
    if multi:
        os.remove(FILENAME) 
        command = 'export PGPASSWORD=%s\npg_dump %s -U %s --file="%s" -h localhost' % (DB_USER_PASSWORD, DB_NAME, DB_USER, FILENAME)
        os.system(command)
    else:
         command = 'export PGPASSWORD=%s\npg_dump %s -U %s --file="%s" -h localhost' % (DB_USER_PASSWORD, DB_NAME, DB_USER, FILENAME)
         os.system(command)
         print("comando" + command)
    print ("Backup script completed")
    #print ("Your backups has been created in '" + TODAYBACKUPPATH + "' directory")