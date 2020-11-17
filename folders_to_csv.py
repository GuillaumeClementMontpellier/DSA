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
from typing import List
import os

SUCCESS = 0

def parse_file(file_path: str) -> List[str]:
    """
    Parse a mail file into a List[str]
    avec envoyeur, destinataire, sujet, Date, folderName 
    """
    raise NotImplementedError


def convert_to_csv(folder_path: str) -> List[List[str]]:
    """
    Take a path to a folder, and return an array
    """
    
    # Check that the folder exists
    if not os.path.isdir(folder_path):
        raise FileNotFoundError("Data folder not found in: " + folder_path)
    
    print(os.listdir(folder_path))
    
    return [["a", "b"], ["az", "az"]]


def write_to_csv(output_path: str, array: List[List[str]]) -> int:
    """
    Take an array, write a csv to the output path
    """
    with open(output_path, mode="w+", newline="") as file:
        result_writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        [result_writer.writerow(row) for row in array]
    
    return SUCCESS


if __name__ == "__main__":
    print("Running as main")
    MAILS_FOLDER_PATH = "maildir"
    OUTPUT_CSV_PATH = "mails.csv"
    ARRAY = convert_to_csv(MAILS_FOLDER_PATH)
    
    if write_to_csv(OUTPUT_CSV_PATH, ARRAY) == SUCCESS:
        print("Write success")
