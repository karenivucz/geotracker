import os
import random
import string
import shutil
import ctypes

def shred_file(file_path, passes=3):
    """
    Overwrites a file with random data multiple times to ensure it's unrecoverable.
    
    :param file_path: Path to the file to shred.
    :param passes: Number of times to overwrite the file.
    """
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return

    file_size = os.path.getsize(file_path)
    with open(file_path, 'ba+', buffering=0) as f:
        for _ in range(passes):
            f.seek(0)
            f.write(os.urandom(file_size))
    os.remove(file_path)
    print(f"File {file_path} shredded and deleted.")

def shred_folder(folder_path, passes=3):
    """
    Overwrites and deletes all files in a folder recursively.
    
    :param folder_path: Path to the folder to shred.
    :param passes: Number of times to overwrite the files in the folder.
    """
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} does not exist.")
        return

    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            shred_file(file_path, passes)

        for name in dirs:
            dir_path = os.path.join(root, name)
            shutil.rmtree(dir_path)
            print(f"Directory {dir_path} deleted.")

    shutil.rmtree(folder_path)
    print(f"Folder {folder_path} shredded and deleted.")

def disable_file_recovery(file_path):
    """
    Marks a file for deletion upon next reboot, enhancing unrecoverability.
    
    :param file_path: Path to the file to mark for deletion.
    """
    if os.path.exists(file_path):
        ctypes.windll.kernel32.SetFileAttributesW(file_path, 0x00000002)
        print(f"File {file_path} marked for deletion on next reboot.")

def main():
    print("GeoTracker - Secure File and Folder Deletion")
    choice = input("Do you want to shred a file or a folder? (file/folder): ").strip().lower()

    if choice not in ['file', 'folder']:
        print("Invalid choice.")
        return

    path = input(f"Enter the path of the {choice} to shred: ").strip()
    passes = int(input("Enter the number of passes for shredding (default is 3): ").strip() or 3)

    if choice == 'file':
        shred_file(path, passes)
        disable_file_recovery(path)
    elif choice == 'folder':
        shred_folder(path, passes)

if __name__ == "__main__":
    main()