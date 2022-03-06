import datetime
import os
import pandas as pd
import requests
from requests_html import HTML

cwd = os.getcwd()
BASE_DIR  = os.path.dirname(cwd)

name = f'{datetime.datetime.now().year}'
table_class = '.imdb-scroll-table'
file_dir = 'data'

def url_to_txt(url, filename=None, save=False):
    response = requests.get(url)
    if response.status_code == 200:
        html_text = response.text
        if save:
            with open(filename, 'w') as f:
                f.write(html_text)
        return html_text
    return None

def parse_and_extract(url, name):
    html_text = url_to_txt(url)
    if html_text == None:
        return False
    html_result = HTML(html=html_text)
    
    table_result = html_result.find(table_class)
    table_data = []
    table_data_list = []
    header_names = []
    if len(table_result) == 0:
        return False
    parsed_table = table_result[0]
    rows = parsed_table.find('tr')
    header_row = rows[0]
    header_cols = header_row.find('th')
    header_names = [x.text for x in header_cols]
    for row in rows[1:]:
        cols = row.find('td')
        row_dict_data = {}
        for i, col in enumerate(cols):
            header_name = header_names[i]
            row_dict_data[header_name] = col.text
        table_data_list.append(row_dict_data)
    df = pd.DataFrame(table_data_list)
    path = os.path.join(BASE_DIR, file_dir)
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join(file_dir, f'{name}.csv')
    df.to_csv(filepath, index=False)
    return True