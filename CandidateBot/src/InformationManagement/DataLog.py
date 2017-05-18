# 
# @author David Moura <david.dbmoura at gmail.com>
# 
import csv
from datetime import datetime
from pathlib import Path

    
def writeLogToCSV(**kwargs):
    path = 'C:/Users/David/Desktop/RandomPessoal/Pessoal/PW/CandidateLog.csv'
    job = kwargs['jobName']
    ref = kwargs['reference']
    contact = kwargs['contact']
    loc = kwargs['location']
    comp = kwargs['company']
    desc = kwargs['description']
    site = kwargs['site']
    tp = kwargs['type']
    date = '{:%d/%m/%Y}'.format(datetime.now())
    time = '{:%H:%M:%S}'.format(datetime.now())
    if !Path(path).exists():
        with open(path, 'w', newline='') as csvFile:
            logWriter = csv.writer(csvFile, delimiter=';', quoting=csv.QUOTE_NONE)
            logWriter.writerow(['Reference', 'Site', 'Job', 'Company', 'Location', 'Type', 'Contact Person',
            'Description', 'Date of Submission', 'Time of Submission'])
            csvFile.close()
    with open(path, 'a', newline='') as csvFile:
        logWriter = csv.writer(csvFile, delimiter=';', quoting=csv.QUOTE_NONE)
        logWriter.writerow([ref, site, job, comp, loc, tp, contact, desc, date, time])
        csvFile.close()
    
#writeLogToCSV(path='newfile.csv', jobName = 'test', reference = '123')