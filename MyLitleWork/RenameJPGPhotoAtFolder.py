# Rename file at folder, but only in format 'year-index.jpg'
# Created for formating file name at folder with many photos
import os
from datetime import datetime


def rename_files(path):
    for root, dirs, files in os.walk(path):
        counting = {}
        for file in files:
            try:
                print(f'Start work with {file}')
                year = str(datetime.fromtimestamp(os.path.getmtime(os.path.join(root, file)))).split('-')[0]
                print(f'Finde year of creation: {year}')
                if year not in counting:
                    counting[year] = 0
                new_name = f'{year}-{counting[year]}.jpg'
                os.rename(os.path.join(root, file), os.path.join(root, new_name))
                counting[year] += 1
                print(f"Success! New name are {new_name}")
            except Exception as e:
                print(f"Error processing file {file}: {e}")

rename_files(r"C:\Users\darkd\Documents\MotherBirthday")
