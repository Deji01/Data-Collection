import requests
from requests_html import HTML
import time

def parse_data(html):
    summary_stats = html.find(".js-post-summary-stats")
    summary_content = html.find(".s-post-summary--content")
    posts_lst = []

    for i in range(len(summary_content)):
        post_dict = {}
        post_dict["votes"] = summary_stats[i].text.split("\n")[0].split("v")[0]
        post_dict["answers"] = summary_stats[i].text.split("\n")[1].split("a")[0]
        post_dict["views"] = summary_stats[i].text.split("\n")[2].split("v")[0]
        posts_dict["question_title"] = summary_content[i].text.split("\n")[0]
        post_dict["question"] = summary_content[i].text.split("\n")[1]
        post_dict["tags"] = summary_content[i].text.split("\n")[2]
        post_dict["user"] = summary_content[i].text.split("\n")[4]
        post_dict["user_reputation"] = summary_content[i].text.split("\n")[5]
        post_dict["time_asked"] = summary_content[i].text.split("\n")[-1]

        posts_lst.append(post_dict)
        
    return posts_lst

def extract_data_from_url(url):
    r = requests.get(url)
    if r.status_code not in range(200,300):
        return []
    html_text = r.text
    html = HTML(html=html_text)
    data = parse_data(html)
    return data

def scrape_tag(tag='python', query_filter='Votes', max_pages=50, pagesize=25):
    base_url = 'https://stackoverflow.com/questions/tagged/'
    data_ = []
    for p in range(max_pages):
        page_num = p + 1
        #     https://stackoverflow.com/questions/tagged/python?tab=votes&page=5&pagesize=15
        url = f'{base_url}{tag}?tab={query_filter}&page={page_num}&pagesize={pagesize}'
        data_ += extract_data_from_url(url)
        time.sleep(1.2)
    return data_