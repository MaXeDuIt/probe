from exif import Image
import os
import shutil

# from exif import Image
#
# with open("D:/photo/1.jpg", "rb") as palm_1_file:
#     palm_1_image = Image(palm_1_file)
#
# with open("D:/photo/2.jpg", "rb") as palm_2_file:
#     palm_2_image = Image(palm_2_file)
#
# images = [palm_1_image, palm_2_image]
#
# for index, image in enumerate(images):
#     year = image.datetime_original[0:4]
#     month = image.datetime_original[5:7]
#     day = image.datetime_original[8:10]
#     print(year, month, day)

class Arrange:


    def __init__(self, file_name):
        self.file_name = file_name


    def organize(self):
        for dirpath, dirnames, filenames in os.walk(self.file_name):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                with open(full_file_path, "rb") as palm_file:
                    palm_image = Image(palm_file)
                year = palm_image.datetime_original[0:4]
                month = palm_image.datetime_original[5:7]
                day = palm_image.datetime_original[8:10]
                self.creation_dir(folder=year, subfolder=month, ssfolder=day)
                folder_for_copying = f"D:\photo\\{year}\\{month}\\{day}"
                self.copying(source=full_file_path, destination=folder_for_copying)

    def creation_dir(self, folder, subfolder, ssfolder):
            os.makedirs(f"D:\photo\\{folder}\\{subfolder}\\{ssfolder}", exist_ok=True)

    def copying(self, source, destination):
            shutil.copy2(source, destination)

icons = Arrange('D:\photo')
icons.organize()
