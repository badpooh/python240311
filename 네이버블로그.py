# 네이버블로그.py

import requests
from bs4 import BeautifulSoup

def search_naver_blog(search_keyword):
    base_url = "https://search.naver.com/search.naver"
    params = {
        "where": "view",
        "sm": "tab_jum",
        "query": search_keyword
    }
    
    # 네이버 블로그 검색 결과 페이지에 요청을 보냄
    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 블로그 검색 결과의 각 항목을 크롤링하여 출력
    blog_entries = soup.find_all('li', class_='sh_blog_top')
    for entry in blog_entries:
        # 블로그명
        blog_name = entry.find('a', class_='sh_blog_title').text
        
        # 블로그글의 제목
        blog_title = entry.find('a', class_='sh_blog_title')['title']
        
        # 날짜
        blog_date = entry.find('dd', class_='txt_inline').text
        
        # 결과 출력
        print("블로그명:", blog_name)
        print("블로그글 제목:", blog_title)
        print("날짜:", blog_date)
        print()

# 키워드 입력 받기
search_keyword = input("네이버 블로그에서 검색할 키워드를 입력하세요: ")
search_naver_blog(search_keyword)
