import requests
from bs4 import BeautifulSoup

url = "https://media.naver.com/press/055/ranking"

response = requests.get(url)
response.raise_for_status() 

soup = BeautifulSoup(response.content, 'lxml')

title = soup.select_one('h2.media_end_head_headline')  
if title:
    title_text = title.text.strip()
else:
    title_text = "제목을 찾을 수 없습니다."

main = soup.select_one('div#dic_area')  
if main:
    main_text = main.text.strip()
else:
    main_text = "본문을 찾을 수 없습니다."

print("제목:", title_text)
print("본문:", main_text)
