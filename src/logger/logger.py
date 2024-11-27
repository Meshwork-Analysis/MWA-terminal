from datetime import datetime
import os

def logtrail(log):
    
    if not os.path.isfile(f"/logs/logfile-{datetime.today().strftime('%Y-%m-%d')}"):
        os.system(f'touch logs/logfile-{datetime.today().strftime('%Y-%m-%d')}.logfile')

    with open(f'logs/logfile-{datetime.today().strftime('%Y-%m-%d')}.logfile','a') as file:
        file.write(log+'\n')