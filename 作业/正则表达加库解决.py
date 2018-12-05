from bs4 import BeautifulSoup
import requests
import re
import time
url = 'https://github.com/apache/mynewt-site'
# 得到commit大页面
pro_name = url[26:]
# print(f"firt print {pro_name}")
r = requests.get(url).text
soup = BeautifulSoup(r, 'html.parser')
# 获取该网页中href符合指定指定正则表达式的内容
pro_commits_url = []
href_ = soup.find_all(href=re.compile(
    f"\/apache\/{pro_name}\/commits"))
for each in href_:
    if str(each.get('href'))[:4] == 'http':
        # 处理得到commits url
        temp_url = each.get('href')
        pro_commits_url.append(temp_url[:-5])
print(pro_commits_url)
# 在项目的commits页面寻找内涵的第一页所有commits的url
url = pro_commits_url[0]
r = requests.get(url).text
soup = BeautifulSoup(r, 'html.parser')

myAttrs = {'class': 'message js-navigation-open'}
find = soup.find_all(name='a', attrs=myAttrs)
url_before = 'https://github.com'
commits_user_url = []
for each_temp in find:
    if str(each.get('href'))[:7] == '/apache':
        # 处理得到commits url
        temp_url = each_temp.get('href')
        temp_url = url_before + temp_url
        commits_user_url.append(temp_url)
print(commits_user_url)
print(len(commits_user_url))
print(time.process_time())
