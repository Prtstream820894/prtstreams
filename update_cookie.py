import requests
import re

source_url = "https://zioplus.saqlainhaider8198.workers.dev/skstar.m3u"
my_file = "prr.m3u"

def get_new_cookie():
    # Source se data fetch karna
    response = requests.get(source_url)
    # Cookie extract karne ka logic
    match = re.search(r'Cookie":"(.*?)"', response.text)
    return match.group(1) if match else None

def update_my_file(new_cookie):
    with open(my_file, 'r', encoding='utf-8') as f:
        content = f.read()
    # Purani cookie ko nayi cookie se badalna (Baki sab same rahega)
    updated_content = re.sub(r'Cookie":"(.*?)"', f'Cookie":"{new_cookie}"', content)
    with open(my_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)

new_c = get_new_cookie()
if new_c:
    update_my_file(new_c)
  
