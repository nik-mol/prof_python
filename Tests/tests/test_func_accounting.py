import pytest
from functions.func_accounting import *


# ------------get_owner_name------------------------
fixture =[
  ('11-2', "Геннадий Покемонов"),
  ('10006', "Аристарх Павлов")
]
@pytest.mark.parametrize("number_document, owner_name", fixture) 
def test_get_doc_owner_name(number_document, owner_name):
    assert get_doc_owner_name(number_document) == owner_name


# ------------get_doc_shelf------------------------
fixture =[
  ('11-2', '1'),
  ('10006', '2')
]
@pytest.mark.parametrize("number_document, number_shelf", fixture)
def test_get_doc_shelf(number_document, number_shelf):
    assert get_doc_shelf(number_document) == number_shelf
    
# ------------move_doc_to_shelf------------------------
fixture =[
  ('11-2','2', '11-2', '2'),
  ('10006','3', '10006', '3')
]
@pytest.mark.parametrize("number_document, number_shelf, move_document, move_shelf", fixture)
def test_move_doc_to_shelf(number_document, number_shelf, move_document, move_shelf):  
    assert move_doc_to_shelf(number_document, number_shelf) == (move_document, move_shelf)
  
# ------------delete_document------------------------
fixture = [
  ('11-2','11-2'),
  ('10006','10006')
]
@pytest.mark.parametrize("number_document, del_document", fixture)
def test_delete_document(number_document, del_document):  
    assert delete_document(number_document) == (del_document)
  
# ------------add_new_doc------------------------
fixture = [
  ('15','passport','Nikolay', '2', '15', '2'),
  ('20','passport','Olesya','3', '20', '3')
]
@pytest.mark.parametrize("number_document, type, name, shelf, new_document, number_shelf", fixture)
def test_add_new_doc(number_document, type, name, shelf, new_document, number_shelf):  
    assert add_new_doc(number_document, type, name, shelf) == (new_document, number_shelf)

# ------------add_shelf------------------------
fixture = [
  ('5', '5'),
  ('6', '6')
]
@pytest.mark.parametrize("number_shelf, added_shelf", fixture)
def test_add_shelf(number_shelf, added_shelf): 
    result = add_shelf(number_shelf)
    assert  result == (added_shelf)