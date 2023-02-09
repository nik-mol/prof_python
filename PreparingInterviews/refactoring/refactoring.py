import email
import smtplib #импорт модуля smtplib для работы с почтой по протоколу SMTP                    
import imaplib #импортируем модуль imaplib для возможности подключения к почтовому ящику по IMAP
from email.mime.text import MIMEText #импорт атрибута email.mime.text из модуля MIMEText. С его помощью будем задавать формат сообщения
from email.mime.multipart import MIMEMultipart #импорт атрибута email.mime.multipart из модуля MIMEMultipart. Будет использоваться для отправки сообщения в двух форматах (text и html)



GMAIL_IMAP = "imap.gmail.com"


class Email:
  
  def __init__(self, login, password, recipients, header = None):
    self.login = login
    self.password = password  
    self.recipients = recipients    
    self.header = header 

  def send_message(self, subject, message):
    """
    Отправка сообщения
    """  
    msg = MIMEMultipart()  # создание экземпляра объекта сообщения MIMEMultipart
    
    # настройка параметров сообщения
    msg['From'] = self.login
    msg['To'] = ', '.join(self.recipients)
    msg['Subject'] = subject
    
    msg.attach(MIMEText(message))   # добавить в тело (само) сообщения
    
    # создание экземпляра объекта сообщения
    GMAIL_SMTP = "smtp.gmail.com"
    ms = smtplib.SMTP(GMAIL_SMTP, 587)
    
    ms.ehlo() # идентифицируем себя в клиенте smtp gmail
    ms.starttls() # защитить нашу электронную почту с помощью шифрования
    ms.ehlo() # повторно идентифицировать себя как зашифрованное соединение
    
    ms.login(msg['From'], self.password) # Учетные данные для отправки почты
    ms.sendmail(msg['From'], msg['To'], msg.as_string()) # отправить сообщение через сервер.
    
    ms.quit() # выход
    return 'Сообщение успешно отправлено'
    

  def recieve_massage(self): 
    """
    Получение сообщения
    """  
    mail = imaplib.IMAP4_SSL(GMAIL_IMAP) #создаем сессию для подключения к почтовому ящику по IMAP и заносим ее в переменную mail
    mail.login(self.login, self.password) #подключаемся к почтовому ящику по IMAP с использованием учетной записи self.login 
    mail.list() 	#выводим список папок в почтовом ящике 
    mail.select("inbox") #выбираем для работы папку входящие (inbox)
    
    #получаем массив со списком найденных почтовых сообщений
    criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
    result, data = mail.uid('search', None, criterion)

    assert data[0], 'There are no letters with current header'
    
    ids = data[0] #сохраняем в переменную ids строку с номерами писем
    id_list = ids.split() #	получаем массив номеров писем
    latest_email_uid = id_list[-1] #задаем переменную latest_email_id, значением которой будет номер последнего письма
    
    result, data = mail.uid('fetch', latest_email_uid, '(RFC822)') #получаем письмо с идентификатором latest_email_id (последнее письмо)
    raw_email = data[0][1] #в переменную raw_email заносим необработанное письмо
    email_message = email.message_from_string(raw_email)
    
    mail.logout() # выход

    return 'Сообщение получено'
