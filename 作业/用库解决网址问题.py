from bs4 import BeautifulSoup
import requests
import re
import time
url = 'https://github.com/apache/mynewt-site'
print(url)
# 得到commit大页面url
pro_name = url[26:]
r = requests.get(url).text
soup = BeautifulSoup(r, 'html.parser')
url_head ='https://github.com'
myAttrs = {'class': 'commits'}
class_commits = soup.find_all(name='li', attrs=myAttrs)
class_commits_tag = []
for each in class_commits:
    url_1 = each.find_all('a')
    class_commits_tag.append(url_1[0])
temp = class_commits_tag[0]
commits_url = url_head + temp.get('href')

print(commits_url)


r_1 = requests.get(commits_url).text
soup_1 = BeautifulSoup(r_1, 'html.parser')

myAttrs = {'class': 'message js-navigation-open'}
class_commits_user = soup_1.find_all(name='a', attrs=myAttrs)
# print(class_commits_user)
# print(class_commits_user)
user_commits_urls = []
for each in class_commits_user:
    temp = each.get('href')
    user_commits_urls.append(url_head + temp)

print(user_commits_urls)
print(len(user_commits_urls))
print(time.process_time())
# last_url = []

# length_1 = len(user_commits_urls)
# print(length_1)
# print(user_commits_urls)
# for each in range(0,length_1):
#     temp = user_commits_urls[each]
#     temp_1 = []
#     temp_1.append(temp.get('href'))
#     last_url[each] = url_head + temp_1[0]

# print(last_url)
# print(len(last_url))



# href_ = soup.find_all(href=re.compile(
#     f"\/apache\/{pro_name}\/commits"))
# for each in href_:
#     if str(each.get('href'))[:4] == 'http':
#         # 处理得到commits url
#         temp_url = each.get('href')
#         pro_commits_url.append(temp_url[:-5])

# # 在项目的commits页面寻找内涵的第一页所有commits的url
# url = pro_commits_url[i]
# r = requests.get(url).text
# soup = BeautifulSoup(r, 'html.parser')

# myAttrs = {'class': 'message js-navigation-open'}
# find = soup.find_all(name='a', attrs=myAttrs)
# url_before = 'https://github.com'
# last_url = []
# for each_temp in find:
#     if str(each.get('href'))[:7] == '/apache':
#         # 处理得到commits url
#         temp_url = each_temp.get('href')
#         temp_url = url_before + temp_url
#         last_url.append(temp_url)
