## NO CONTENTS WERE ADDED TO THE CREATED FILES. USE OF GLOBAL VARIABLES IN FUNCTIONS
## SCORE = 26 MARKS OUT OF 30
## TOTAL SCORE = 91 MARKS OUT OF 100
import os, os.path, shutil
import zipfile

def Folder_Creation(User_Folder):
    if os.path.exists(New_Folder):
        shutil.rmtree(New_Folder)
        os.makedirs(New_Folder)
    else:
        os.makedirs(New_Folder)

    for val in ['backup', 'working']:
        os.makedirs(os.path.join(New_Folder, val))

    for val in ['pics', 'docs', 'movie']:
        os.makedirs(os.path.join(Working_Path, val))

    for val in ['SCREENTIME.txt', 'DANGEROUS.txt', 'KEEPSAFE.txt', 'CONCENTRATE.txt', 'SUCCEED.txt']:
        file_creator = open(os.path.join(Document_Path, val), 'w')
        file_creator.close()

    for val in ['school', 'party']:
        os.makedirs(os.path.join(Document_Path, val))

#def Folder_Renamer():
#    Contents = os.listdir(Document_Path)
#    Files = []
#    for val in Contents:
#        if val is os.path.isfile:
#            Files.append(val)
#    print(Files)

def Folder_Zipper(Document_Path, Backup_Path):
    for i in range(1, 6):
        zipf = zipfile.ZipFile(os.path.join(Backup_Path, f'Docs_Backup{i}.zip'), 'w', zipfile.ZIP_DEFLATED)
        for file in os.listdir(Document_Path):
            zipf.write(os.path.join(Document_Path, file))
        zipf.close()
    for Backups in os.listdir(Backup_Path):
        print(Backups)
    with zipfile.ZipFile(os.path.join(Backup_Path, 'Docs_Backup1.zip'), 'r') as zip_ref:
        for Stuff in zip_ref.namelist():
            print(Stuff)

User_Folder = input(str("What folder name would you like to create? -> "))
Working_Directory = os.getcwd()
New_Folder = os.path.join(Working_Directory, f"{User_Folder}")
Working_Path = os.path.join(New_Folder, 'working')
Document_Path = os.path.join(Working_Path, 'docs')
Backup_Path = os.path.join(New_Folder, 'backup')

Folder_Creation(User_Folder)
Folder_Zipper(Document_Path, Backup_Path)


