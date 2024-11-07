import os
import shutil

# .exe , .msi, .gif, .png .jpg, jpeg, .csv, .pdf , .pdf , .xls , .xlsx , .ppt , .pptx

from_dir = "/Users/megan/Downloads"
to_dir = "/Users/megan/Downloads"

list_of_files = os.listdir(from_dir)
#print(lists_of_files)

# Move All Image files from Downloads Folder to Another Folder
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:

        path1 = from_dir + '/' + file_name                      #Example path1 : Downloads/Image
        path2 = to_dir + '/' + "Image_Files"                    #Example path2 : D:/MY Files/Image
        path3 = to_dir + '/' + "Image_Files" + '/' + file_name #Example path3 : D:/My Files/Image

        if os.path.exists(path2):
            print("Moving " + file_name + ".....")

            #Move from path1 ---> path3
            shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)