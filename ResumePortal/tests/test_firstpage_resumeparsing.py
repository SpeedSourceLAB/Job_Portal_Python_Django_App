import pytest
import sys,os,json
from tests import firstpage_resumeparsing as fp
mypath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, mypath + '/../')


@pytest.mark.parametrize("Filename, Expected_result",fp.json_to_list())
def test_json_to_list(Filename,Expected_result):
    assert str(fp.check_file_is_docx(Filename)) == Expected_result

