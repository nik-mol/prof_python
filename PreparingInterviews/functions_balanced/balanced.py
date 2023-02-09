from functions_balanced.stack import Stack
import re


def balanced(symbol_string):
  # создаем пустой Stack
  s = Stack([])
  
  # поиск нужных символов в строке
  search_symbol = re.findall(r'[^\(\[\{\)\]\}]', symbol_string)
  
  # проверка есть ли список, четное ли кол-во символов, есть ли нужные символы 
  if (not symbol_string) or (len(symbol_string) % 2 != 0) or (search_symbol):
    return False

  # перебираем список
  for symbol in symbol_string:
    # если symbol есть в открывающихся скобках, то добавляем его в конец списка
    if symbol in '([{':
      s.push(symbol)
    # если symbol есть в закрывающихся скобках
    if symbol in ')]}':
      # проверяем если список пустой (не добавили открывающиеся скобки), то False
      if not s.isEmpty():
        return False
      #  удаляем и возвращаем верхние символы (открывающиеся скобки), кладем в переменную top
      top = s.pop()
      # проверяем если выталкиваемый символ не является открывающей фигурной скобкой или не является парой
      # с текущим символом выражения      
      if (top == '(' and symbol != ')') or (top == '{' and symbol != '}') or (top == '[' and symbol != ']'):
        return False        
        
  return not s.isEmpty()
      
  

  
  