import logging
from tqdm import tqdm
import time

def decor_logging_parametres(path):
    def decor_logger(old_function):    
        def wrapper(*args, **kwargs):        
          logging.basicConfig(filename=path,                                                                      
                              filemode='a',
                              level=logging.DEBUG,                            
                              format= '%(message)s  -->  TimeCallFunction: %(asctime)s')   #параметры логирования        
          logger = logging.getLogger()   
    
          logging.getLogger('urllib3').setLevel('CRITICAL') #
    
          # for key in logging.Logger.manager.loggerDict: #все используемые логеры
          #   print(key)
    
          result = old_function(*args, **kwargs) 
          
          for i in tqdm(range(len(result))): #индикатор выполнения    
            time.sleep(1)        
            logger.debug(f"NameFunction: {old_function.__name__} --> FuncfArguments: {args} and {kwargs}") #вызов логирования     
          return result        
        return wrapper
    return decor_logger