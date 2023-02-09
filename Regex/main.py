import csv
import re


def get_list_from_csv(file_name: str) -> list:
    '''
    Gets contact list from csv file
    '''
    with open(file_name, encoding='utf8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        return contacts_list
      

def trans_matrix(matrix: list) -> list:
  '''
    Transposes matrix, rows turn into columns and vise versa    
  '''
  trans_matrix = [[matrix[row][column] for row in range(len(matrix))] for column in range(len(matrix[0]))] 
  return trans_matrix
  

def standardization_phone(phone_list: list) -> None:
  '''
  Standardizes phone numbers to pattern '+7(999)999-99-99 доб.9999'
  '''
  for i, phone in enumerate(phone_list):
    search_pattern = r'(\+7|8)?\s?\(?(\d{3})\)?[-|\s]?(\d{3})[-|\s]?(\d{2})[-|\s]?(\d{2})[\s,]?\(?(доб\.)?\.?\s?(\d{4})?\)?'
    replace_phone = r'+7(\2)\3-\4-\5 \6\7'
    new_phone = re.sub(search_pattern, replace_phone, phone)
    phone_list[i] = new_phone  

def split_lastname(lastname_list: list) -> list:
    '''
    Splits lastname string (if firstname and/or surname (patronym) is indicated in the same string as lastname)
    and moves firstname and/or surname (patronym) to corresponding strings 
    '''
    for i, lastname in enumerate(lastname_list[0]):
        pattern = r'[а-яёА-ЯЁ]+'  # or pattern = r'\w+'
        search_lastname = re.findall(pattern, lastname)
        if len(search_lastname) == 2:
            lastname_list[0][i] = search_lastname[0]
            lastname_list[1][i] = search_lastname[1]
        elif len(search_lastname) == 3:
            lastname_list[0][i] = search_lastname[0]
            lastname_list[1][i] = search_lastname[1]
            lastname_list[2][i] = search_lastname[2]
        else:
            pass

def split_firstname(firstname_list: list) -> list:
    '''
    Splits firstname string (if surname (patronym) is indicated in the same string as firstname)
    and moves surname (patronym) to corresponding string
    '''
    for i, firstname in enumerate(firstname_list[0]):
        pattern = r'[а-яёА-ЯЁ]+'  # or pattern = r'\w+'
        search_lastname = re.findall(pattern, firstname)
        if len(firstname) == 2:
            firstname_list[0][i] = firstname[0]
            firstname_list[1][i] = firstname[1]
        else:
            pass  

def join_doubled_contacts(contact_list: list) -> list:
    '''
    Finds doubled persons in contact list and joins information from several lines into one
    '''
    final_list = []
    contact_list.sort()
    final_list.append(contact_list[0])
    for person in contact_list:
        if person[0] == final_list[-1][0] and person[1] == final_list[-1][1]:
            for i, parameter in enumerate(final_list[-1]):
                if not parameter:
                    final_list[-1][i] = person[i]
        else:
            final_list.append(person)
    return final_list

def save_list_to_csv(file_name: str, contact_list: list) -> None:
    '''
    Saves contact list to csv file    
    '''
    with open(file_name, "w", newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contact_list)


if __name__ == '__main__':
    contact_list = get_list_from_csv("phonebook_raw.csv")
    transposed_list = trans_matrix(contact_list)    
    standardization_phone(transposed_list[5])
    split_lastname(transposed_list)
    split_firstname(transposed_list)
    return_contact_list = trans_matrix(transposed_list)
    ordered_contact_list = join_doubled_contacts(return_contact_list)
    save_list_to_csv("phonebook.csv", ordered_contact_list)