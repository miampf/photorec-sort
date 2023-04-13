#!/usr/bin/python3

import os
import sys

# print_green prints in green.
def print_green(text: str) -> None:
    print(f"\033[32m{text}\033[0m")

# PhotoRecSorter is responsible for looping through the folders
# and sorting everything.
class PhotoRecSorter:
    photorec_folder = "."
    output_folder = "."
    range_increment = 0
    
    def __init__(self, photorec_folder: str, output_folder: str, range_increment: int) -> None:
        self.photorec_folder = photorec_folder
        self.output_folder = output_folder
        self.range_increment = range_increment

    # sort_folder will recursively sort a folder and return the number of files moved.  
    def sort_folder(self) -> int:
        files_count = 0

        for root, _, files in os.walk(self.photorec_folder):
            dir_files_count = len(files)
            file_counter = 1 

            for name in files:
                percentage_done = int((file_counter/dir_files_count)*100)
                file_path = os.path.join(root, name)
                print_green(f"{file_path}")
                print(f"\t[{'#' * percentage_done + ' ' * (100-percentage_done)}]")
                
                self.__move_file(file_path)

                file_counter += 1
                files_count += 1

        return files_count

    def __move_file(self, file_path: str) -> None:
        file_size = os.path.getsize(file_path)

        # convert the file size to GiB
        file_size = file_size/pow(pow(2, 10), 3)
        
        # get the size range in which the file belongs
        low_range = 0
        high_range = 0
        i = 0
        while True:
            if self.range_increment*i >= file_size:
                low_range = (i-1)*self.range_increment if i > 0 else 0
                high_range = i*self.range_increment
                break
            i += 1
        size_sorted_folder = f"{low_range}_{high_range}"

        # get the file extension
        file_extension = os.path.splitext(file_path)[1].removeprefix(".")
        file_name = os.path.basename(file_path)

        new_dirs = os.path.join(self.output_folder, file_extension, size_sorted_folder)
        new_path = os.path.join(new_dirs, file_name)

        try:
            os.makedirs(new_dirs)
        except FileExistsError:
            pass
        os.rename(file_path, new_path)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Error: Didn't specify enough arguments.")
        print("Usage:\npython photorec-sort.py <SIZE_INCREASE> <PHOTOREC_FOLDER> <OUTPUT_FOLDER>")
        sys.exit(1)

    SIZE_INCREASE = int(sys.argv[1])
    PHOTOREC_FOLDER = sys.argv[2]
    OUTPUT_FOLDER = sys.argv[3]

    sorter = PhotoRecSorter(PHOTOREC_FOLDER, OUTPUT_FOLDER, SIZE_INCREASE)
    sorter.sort_folder()
