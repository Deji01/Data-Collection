import datetime
import os
from utils import run

url = 'https://www.boxofficemojo.com/year/world'

if __name__ == '__main__':
    run(url, years_ago=5)