"""
Create a cvs file using a folder of mails
folder
|_a-name
| |_folder_name
| | |_mail
| | |_mail
| |_folder_name
|   |_mail
|   |_mail
|   |_mail
|_...
|
...
"""
import csv


def convert_to_csv(folder_path: str):
    """
    Take a path to a folder, and return an array
    """
    raise NotImplementedError


def write_to_csv(folder_path: str, array):
    """
    Take an array, write a csv to the output path
    """
    raise NotImplementedError


if __name__ == "__main__":
    print("Running as main")
    MAILS_FOLDER_PATH = "../maildir"
    OUTPUT_CSV_PATH = "../mails.csv"
    
    ARRAY = convert_to_csv(MAILS_FOLDER_PATH)
    write_to_csv(OUTPUT_CSV_PATH, ARRAY)

