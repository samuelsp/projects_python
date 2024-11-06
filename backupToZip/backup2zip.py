import zipfile, os
from dotenv import load_dotenv

load_dotenv('.env', override=True)
path = os.getenv('PATH')

def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder) # make sure folder is absolute
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number += 1
        
    # Create the ZIP file.
    print(f'Creating {zipFileName}...')
    backupZip = zipfile.ZipFile(zipFileName, 'w')
    
    for folderName, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {folderName}...')
        # Add the current folder to the ZIP file.     
        backupZip.write(folderName)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folderName) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(folderName, filename))
    
    backupZip.close()     
    
    
if __name__ == '__main__':
    backupToZip(path)
    print('Done.')
                    
        
        