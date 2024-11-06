import zipfile
import os
import shutil
from dotenv import load_dotenv

load_dotenv()

def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    zip_filename = os.path.join(script_dir, os.path.basename(folder) + '.zip')
    
    with zipfile.ZipFile(zip_filename, 'a') as backupZip:
        existing_files = set(backupZip.namelist())
        for foldername, subfolders, filenames in os.walk(folder):
            for filename in filenames:
                newBase = os.path.basename(folder) + '_'
                if filename.startswith(newBase) and filename.endswith('.zip'):
                    continue
                file_path = os.path.join(foldername, filename)
                arcname = os.path.relpath(file_path, folder)
                if arcname not in existing_files:
                    backupZip.write(file_path, arcname)
    
    print(f'Backup saved to {zip_filename}')
    
def copyFiles(origin, destination):
    origin = os.path.abspath(origin)
    destination = os.path.abspath(destination)

    if not os.path.exists(origin):
        os.makedirs(origin)
    
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    try:
        for item in os.listdir(origin):
            s = os.path.join(origin, item)
            d = os.path.join(destination, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
        return True
    except Exception as e:
        print(f'An error occurred: {e}')
        return False

if __name__ == '__main__':
    target = os.getenv('TARGET')
    backup = os.getenv('BACKUP')
    
    if target and backup:
        if copyFiles(target, backup):
            backupToZip(backup)
            print('Done.')
    else:
        print('Environment variables TARGET and BACKUP must be set.')