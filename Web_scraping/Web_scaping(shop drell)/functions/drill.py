import re
from tqdm import tqdm
from functions.soup import create_soup


def get_drill(URL):
    """Get catalog drill
  """
    # вызов функции создания 'супа'
    soup = create_soup(URL)

    drill_list = soup.find(class_='catalog-item-table-view')
    drill_card = drill_list.find_all(class_='catalog-item-card')

    print()
    print(f'Количество дрелей: {len(drill_card)} шт.')
    print('*' * 30)

    catalog_drill = ''
    for drill in drill_card:
        # наименование дрели
        drill_title = drill.find('img').attrs['title']
        # URL дрели
        drill_href = drill.find('a').attrs['href']
        url_main_page = URL.replace(
            '/catalog/elektroinstrument/akkumulyatornye_dreli_shurupovyerty/',
            '')
        drill_url = url_main_page + drill_href
        # количество вналичии
        drill_quantity = drill.find('input', class_='quantity').attrs['value']
        # стоимость дрели
        get_drill_price = drill.find(class_='item-price').text
        # фильтр (отделение цены от текста)
        drill_price_list = re.findall(r'\d+\s\d+', get_drill_price)
        # проверка на наличие товара
        if int(drill_quantity) >= 1:
            # запись даннных в файл
            with open('drill.txt', 'a') as file:
                drill = ''
                for drill_price in drill_price_list:
                    # логирование
                    for i in tqdm(range(len(drill_price_list))):
                        drill += f'  Наименование: {drill_title} -> Цена: {drill_price} руб. -> Ссылка: {drill_url} ;\n\n'
                file.write(drill)

        for drill_price in drill_price_list:
            # вывод каталога аккумкляторных дрелей
            catalog_drill += f'  Наименование: {drill_title} -> Цена: {drill_price} руб. -> Ссылка: {drill_url} ;\n\n'
    return catalog_drill