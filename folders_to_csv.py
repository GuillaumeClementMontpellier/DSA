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
from typing import List, Optional
import os

# EMAIL_SUFFIX =  "enron.com"

def stringToName(input_string: str) -> str:
    
    # print("emailToName")
    # print(email)
    
    if (not input_string):
        # print("Not input string : " + input_string)
        return ""
    
    data = input_string.split("<")
    
    if (len(data) >= 2):
        data = data[1]
        # print(data)
    else :
        data = data[0]
        
    data = data.split("@")
    
    # print(data)
    
    if (len(data) < 2):
        # print("Not valid mail : " + input_string)
        return ""
    
    # suffix = data[1]
    
    # if(suffix != EMAIL_SUFFIX):
    #     return ""       
    
    prefix = data[0]
    
    # print(prefix)
    
    return prefix.strip().replace("\"", "")
    
    

def parse_file(file_path: str, folder_name: str) -> List[List[str] ]:
    """
    Parse a mail file into a List[str]
    avec envoyeur, destinataire, sujet, Date, folderName, metadata, content
    """
    # print(file_path)
    
    with open(file_path, mode="r", newline="") as file:
        sender = 0
        recipients = []
        ccs = []
        
        inTo = False
        inCC = False
        
        try :
            for line in file:
                data = line.split(":")
                
                if(len(data) >= 2):
                    inTo = False
                    inCC = False
                
                if (data[0] == "From" and sender == 0):
                    sender = stringToName(data[1].strip())             
                elif (inTo or data[0] == "To" and recipients == []):
                    inTo = True
                    if(len(data) < 2):
                        data = ["", data[0]]
                    # print(data)
                    recipients.append(stringToName(data[1]))
                elif (inCC or data[0] == "CC" and ccs == []):
                    inCC = True
                    if(len(data) < 2):
                        data = ["", data[0]]
                    # print(data)
                    ccs.append(stringToName(data[1]))
                    
        except UnicodeDecodeError:
            return [["", ""]]
        
        # print(recipients + ccs)
                          
        return filter(lambda a: a[0] != "" and a[1] != "", map(lambda a: [sender, a] , recipients + ccs))


def convert_to_csv(folder_path: str, writer) -> List[List[str]]:
    """
    Take a path to a folder or file, and return an array
    If folder, call itself on every child and concatenate the arrays
    If file, call and return [parse_file]
    """
    # base_path = folder_path
    def convert_to_csv_rec(folder_path: str, caller_folder: str, writer)-> List[List[str]]:
        if os.path.isdir(folder_path):
            print(folder_path)
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
    MAILS_FOLDER_PATH = "mails_perso"
    # MAILS_FOLDER_PATH = os.path.join(MAILS_FOLDER_PATH, "allen-p")
    OUTPUT_CSV_PATH = "mails_perso.csv"
    with open(OUTPUT_CSV_PATH, mode="w+", newline="") as FILE:
        CSV_WRITER = csv.writer(FILE, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        convert_to_csv(MAILS_FOLDER_PATH, CSV_WRITER)
    print("Write success")
