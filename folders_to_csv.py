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


def parse_file(file_path: str, folder_name: str) -> List[List[str] ]:
    """
    Parse a mail file into a List[str]
    avec envoyeur, destinataire, sujet, Date, folderName, metadata, content
    """
    # print(file_path)
    with open(file_path, mode="r", newline="") as file:
        sender = 0
        recipients = []
        
        for line in file:
            data = line.split(":")
            if (data[0] == "From" and sender == 0):
                sender = data[1].strip()
            elif (data[0] == "To" and recipients == []):
                recipients += list(map(str.strip, data[1].split(",")))
               
        return map(lambda a: [sender, a] ,recipients)


def convert_to_csv(folder_path: str, writer) -> List[List[str]]:
    """
    Take a path to a folder or file, and return an array
    If folder, call itself on every child and concatenate the arrays
    If file, call and return [parse_file]
    """
    base_path = folder_path
    def convert_to_csv_rec(folder_path: str, caller_folder: str, writer)-> List[List[str]]:
        if caller_folder == base_path:
            print(folder_path)
        if os.path.isdir(folder_path):
            for folder in os.listdir(folder_path):
                convert_to_csv_rec(os.path.join(folder_path, folder), folder_path, writer)
        elif os.path.isfile(folder_path):
            for row in parse_file(folder_path, caller_folder):
                writer.writerow(row)
        else:
            raise FileNotFoundError("Data folder not found in: " + folder_path)
    writer.writerow(["sender", "recipient"])
    convert_to_csv_rec(folder_path, "base", writer)


if __name__ == "__main__":
    print("Running as main")
    MAILS_FOLDER_PATH = "maildir"
    # MAILS_FOLDER_PATH = os.path.join(MAILS_FOLDER_PATH, "allen-p")
    OUTPUT_CSV_PATH = "mails.csv"
    with open(OUTPUT_CSV_PATH, mode="w+", newline="") as FILE:
        CSV_WRITER = csv.writer(FILE, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        convert_to_csv(MAILS_FOLDER_PATH, CSV_WRITER)
    print("Write success")
