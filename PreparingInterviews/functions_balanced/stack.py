class Stack:
  
  def __init__(self, stack: list):
    self.stack = stack

  def isEmpty(self) -> bool:
    '''
    Проверка стека на пустоту. Метод возвращает True или False.
    '''
    if len(self.stack) > 0:
      return True
    else:
      return False

  def push(self, new_element: all) -> None:
    '''
    Добавляет новый элемент на вершину стека. 
    Метод ничего не возвращает
    '''
    self.stack.append(new_element) 

  def pop(self) -> str:
    '''
    Удаляет верхний элемент стека. Стек изменяется. 
    Метод возвращает верхний элемент стека.
    '''
    result = self.stack.pop() 
    return result

  def peek(self) ->str:
    '''
    Возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    '''
    result = self.stack[-1]
    return result 

  def size(self) -> int:
    '''
    Возвращает количество элементов в стеке.
    '''
    return len(self.stack)

  def __str__(self) -> str:
    '''
    Возвращает весь стек.
    '''
    return f'Текущий Stack: {self.stack}'    
  
