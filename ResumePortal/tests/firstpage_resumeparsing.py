import json
import csv
import pytest
import re

#converting Json file to lists
def json_to_list():
    with open('C:\\Users\\prade\\PycharmProjects\\ResumePortal\\tests\\Datafile.json') as json_file:
        data = json.load(json_file)
        test_data = []
        keylist = ['Filename', 'Expected_result']
        for row in data:
            row2 = []
            for key in keylist:
                row2.append(row[key])
            test_data.append(row2)
    print (test_data)
    return test_data


#checking docx funtionality
def check_file_is_docx(Filename):
    if Filename.lower().endswith('.docx'):
        return True
    else:
        return False