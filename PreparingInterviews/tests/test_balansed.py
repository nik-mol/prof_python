import pytest
from functions_balanced.balanced import balanced

fixture = [
  ('(((([{}]))))',True),
  ('{{[()]}}', True),
  ('[([])((([[[]]])))]{()}', True)
]
@pytest.mark.parametrize("symbol_string, result", fixture)
def test_balanced_true(symbol_string, result):
  assert balanced(symbol_string) == result

fixture = [
  ('{{[(])]}}', False),
  ('[[{())}]', False),
  ('{([55])}', False)
]
@pytest.mark.parametrize("symbol_string, result", fixture)
def test_baslansed_false(symbol_string, result):
  assert balanced(symbol_string) == result