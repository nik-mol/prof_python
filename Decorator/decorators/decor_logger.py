from tqdm import tqdm
import time
from datetime import datetime

def decor_logger_parametres(path):
    def decor_logger(old_function):    
        def wrapper(*args, **kwargs):   
                        
          result = old_function(*args, **kwargs) 
          
          for i in tqdm(range(len(result))): #индикатор выполнения    
            time.sleep(1) 
            with open (path, 'a') as f:
              f.write(f"NameFunction: {old_function.__name__} --> TimeCallFunction: {datetime.now().strftime('%d-%m-%Y %S:%M:%H')} --> FuncfArguments: {args} and {kwargs}  \n")     
                 
          return result        
        return wrapper
    return decor_logger