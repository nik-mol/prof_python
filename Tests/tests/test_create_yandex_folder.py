import pytest
from functions.create_yandex_folder import create_directory



fixture =[
  ('NewFolder', 201)  
]
@pytest.mark.parametrize("name_directory, status_code", fixture) 
def test_create_directory(name_directory, status_code):
    assert create_directory(name_directory) == status_code
  