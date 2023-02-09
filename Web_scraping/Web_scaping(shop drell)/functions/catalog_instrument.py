from functions.soup import create_soup


def get_catalog_instrument(URL):
    """Get catalog instrument
  """

    # вызов функции создания 'супа'
    soup = create_soup(URL)

    catalog_list = soup.find(class_='catalog-section-childs')
    instrument_list = catalog_list.find_all(class_='catalog-section-child')

    print(f'Количество категорий: {len(instrument_list)} шт.')
    print('*' * 30)

    instrument_catalog = ''
    for instrument in instrument_list:
        instrumen_title = instrument.find('a').attrs['title']
        instrumen_href = instrument.find('a').attrs['href']
        instrumen_url = URL + instrumen_href
        # вывод каталога оборудования электроинструмент
        instrument_catalog += f'{instrumen_title} --> {instrumen_url} ;\n'
    return instrument_catalog