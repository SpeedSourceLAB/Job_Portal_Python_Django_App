import pytest
import glob
import os
from resumeapp import views
import pathlib

@pytest.fixture()
def get_file():
    list_of_files = glob.glob('C:\\Users\\prade\\PycharmProjects\\ResumePortal\\media\\*')
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file

def test_file_size(get_file):
    print(get_file)
    expected_result = os.path.getsize(get_file)
    print(expected_result)
    actual_result = views.latest_file()

    assert actual_result == expected_result

def test_file_type(get_file):
    actual_result = pathlib.Path(get_file).suffix
    print("======",actual_result)
    assert actual_result == ".doc" or actual_result == ".docx"