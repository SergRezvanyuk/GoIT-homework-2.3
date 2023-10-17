import os
import shutil
import threading

def process_folder(folder_path,subpath ):
    for root, dirs, files in os.walk(subpath):
        for file in files:
            file_extension = os.path.splitext(file)[1]
            dest_folder = os.path.join(folder_path, file_extension[1:])
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(os.path.join(root, file), os.path.join(dest_folder, file))

def main():
    folder_path = 'e:\Мотлох' 
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
        thread = threading.Thread(target=process_folder, args=(folder_path, folder_path + '/' + subdir,))
        thread.start()
        threads.append(thread)
    for file in files:
            file_extension = os.path.splitext(file)[1]
            dest_folder = os.path.join(folder_path, file_extension[1:])
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(os.path.join(folder_path, file), os.path.join(dest_folder, file))

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()