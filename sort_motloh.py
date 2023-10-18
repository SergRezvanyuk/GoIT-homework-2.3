import os
import shutil
import threading
from pathlib import Path
import sys



def process_folder(folder_path,subpath, type_file,type_name ):
    for root, dirs, files in os.walk(subpath):
        for file in files:
            file_extension = os.path.splitext(file)[1]
            # dest_folder = os.path.join(folder_path, file_extension[1:])
            # os.makedirs(dest_folder, exist_ok=True)
            if file_extension[1:] in type_file:
                dest_folder = type_name[type_file[file_extension[1:]]]
            else:
                dest_folder = 'unfamiliar'
            if os.path.exists(os.path.join(folder_path + '/' + dest_folder, file)):
                os.remove(os.path.join(folder_path + '/' + dest_folder, file))
            shutil.move(os.path.join(root + '/', file), os.path.join(folder_path + '/' + dest_folder, file))


def main():
    if len(sys.argv) != 2:
        print("Введіть 2 параметра: назву скрипта і папку, яку потрібно розібрати")
        quit()
    folder_path = Path(sys.argv[1])
    # folder_path = Path('e:/ttt')
    print(repr(folder_path))


    if not folder_path.exists():
        print('Папку', folder_path, 'не знайдено')
        sys.exit()

    folder_path = str(folder_path)
    Path.mkdir(Path(folder_path+'/images'), exist_ok=True)
    Path.mkdir(Path(folder_path+'/video'), exist_ok=True)
    Path.mkdir(Path(folder_path+'/documents'), exist_ok=True)
    Path.mkdir(Path(folder_path+'/audio'), exist_ok=True)
    Path.mkdir(Path(folder_path+'/archives'), exist_ok=True)
    Path.mkdir(Path(folder_path+'/unfamiliar'), exist_ok=True)
    Path.mkdir(Path(folder_path+'/python'), exist_ok=True)

    type_name = {1:'images', 2:'video', 3:'documents', 4:'audio',5:'archives',
                 6:'python', 7:'unfamiliar'}

    type_file = {'jpeg':1, 'jpg':1, 'png':1, 'svg':1,
                'avi':2, 'mp4':2, 'mov':2, 'mkv':2,
                'doc':3, 'docx':3, 'txt':3, 'pdf':3, 'xlsx':3, 'pptx':3,
                'mp3':4, 'ogg':4, 'wav':4, 'arm':4,
                'zip':5, 'gz':5, 'tar':5,
                'py':6}
    threads = []
    files = []
    directories = []
    for entry in os.listdir(folder_path):
        full_path = os.path.join(folder_path, entry)
        # Перевіряємо, чи є це файл чи каталог
        if os.path.isfile(full_path):
            files.append(entry)
        elif os.path.isdir(full_path):
            directories.append(entry)
    
    for subdir in directories:
        sdir =  True

        for dir in type_name.values():
            if subdir == dir:
                sdir = False
        
        if sdir:
            thread = threading.Thread(target=process_folder, args=(folder_path, folder_path + '/' + subdir,type_file,type_name))
            thread.start()
            threads.append(thread)
    for file in files:
            file_extension = os.path.splitext(file)[1]
            
            # dest_folder = os.path.join(folder_path, file_extension[1:])
            # os.makedirs(dest_folder, exist_ok=True)
            if file_extension[1:] in type_file:
                dest_folder = type_name[type_file[file_extension[1:]]]
            else:
                dest_folder = 'unfamiliar'
            try:
                shutil.move(os.path.join(folder_path, file), os.path.join(folder_path + '/' + dest_folder, file))
            except Exception:
                pass
    for thread in threads:
        thread.join()
    for entry in os.listdir(folder_path):
        full_path = os.path.join(folder_path, entry)
        if os.path.isdir(full_path):
            t = True
            for dir in type_name.values():
                if dir == entry[-len(dir):]:
                    t = False
            if t:
                try:
                    shutil.rmtree(full_path)
                except Exception:
                    pass

if __name__ == '__main__':
    main()