from functions_balanced.balanced import balanced 
import pytest
  
from refactoring.refactoring import Email


if __name__ == '__main__':
      
    symbol_str = input('Введите список фигурных скобок:')  

    if balanced(symbol_str):
      print('Сбалансировано')
    else:
      print('Несбалансировано')
  
    pytest.main()    

    send_email = Email(login = 'login@gmail.com',
                  password = 'qwerty',                 
                  recipients = ['vasya@email.com', 'petya@email.com'],                  
                  header = None)   

    send_email.send_message('First_Vessage', 'Text_Message')

  
    recieve_email = Email(login = 'login@gmail.com',
                  password = 'qwerty',                 
                  recipients = ['vasya@email.com', 'petya@email.com'],                  
                  header = None)   

    recieve_email.recieve_massage()




  
  
 



































