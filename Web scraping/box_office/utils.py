import datetime
from webscrape import parse_and_extract

def run(url, start_year=None, years_ago=0):
    if start_year == None:
        now = datetime.datetime.now()
        start_year = now.year
    assert isinstance(start_year, int)
    assert isinstance(years_ago, int)
    assert (len(f'{start_year}')) == 4
    for i in range(0, years_ago+1):
        url_result = f'{url}/{start_year}'
        finished = parse_and_extract(url_result, name=start_year)
        if finished: 
            print(f'Finished {start_year}')
        else:
            print(f'{start_year} not found')
        start_year -= 1