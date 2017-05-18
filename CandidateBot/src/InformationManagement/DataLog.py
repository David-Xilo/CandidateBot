# 
# @author David Moura <david.dbmoura at gmail.com>
# 
import csv
from datetime import datetime
import os

    
    
def getReferencesFromLog(path):
    reflst = set()
    with open(path, 'r', newline='') as csvFile:
        reader = csv.reader(csvFile, delimiter=';')
        next(reader)#skips headers
        for row in reader:
            reflst.add(row[0])
    return reflst

# kwargs was maintained for convinience
# the function receives a dictionary as parameter
def writeLogToCSV(kwargs):
    path = kwargs['path']
    method = kwargs['method']
    job = kwargs['jobName']
    ref = kwargs['reference']
    contact = kwargs['contact']
    loc = kwargs['location']
    comp = kwargs['company']
    #desc = kwargs['description']
    #site = kwargs['site']
    tp = kwargs['type']
    date = '{:%d/%m/%Y}'.format(datetime.now())
    time = '{:%H:%M:%S}'.format(datetime.now())
    if not os.path.isfile(path):
        with open(path, 'w', newline='') as csvFile:
            logWriter = csv.writer(csvFile, delimiter=';', quoting=csv.QUOTE_NONE)
            logWriter.writerow(['Reference', 'Job', 'Company', 'Location', 'Type', 'Contact Person',
            'Method Used', 'Date of Submission', 'Time of Submission'])
            csvFile.close()
    with open(path, 'a', newline='') as csvFile:
        logWriter = csv.writer(csvFile, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
        logWriter.writerow([ref, job, comp, loc, tp, contact, method, date, time])
        csvFile.close()
    
#writeLogToCSV(path='newfile.csv', jobName = 'test', reference = '123')