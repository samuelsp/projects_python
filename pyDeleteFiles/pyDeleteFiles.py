import os
import logging
import tempfile
from send2trash import send2trash
from time import time
from datetime import datetime

start_time = time()
current_date = datetime.now().strftime('%d%m%Y_%H%M%S')
program_name = current_date + '_pyDeleteFiles' 

DTF = tempfile.gettempdir()
DLF = os.path.dirname(os.path.realpath(__file__))
LFN = DLF + '\\' + program_name + '.log' # name of the log file

logging.basicConfig(filename=LFN
                    , level=logging.INFO
                    , format='%(asctime)s - %(levelname)s - %(message)s')

logging.info('Start of program')

files = [f for f in os.listdir(DLF)]
for file in files:
    if file.endswith('.log'):
        try:
            os.unlink(DLF + '\\' + file)
        except Exception as e:
            logging.error(str(e))

files = [f for f in os.listdir(DTF)]
files_deleted = 0
for file in files:    
    try:        
        send2trash(DTF + '\\' + file)   
        files_deleted += 1     
    except Exception as e:
        logging.error(str(e))

           
execution_time = time() - start_time

logging.info(f'Execution time: {execution_time:.2f} seconds.')
logging.info(f'Files deleted: {files_deleted}')
logging.info('End of program')