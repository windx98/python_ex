from selenium import webdriver
import time
message_dic = {
    "kigmtv04783@chacuo.net": "xyj@1007",
    "1253101930@qq.com": "xyj@1007",
    "2480095417@qq.com": "xyj@1007",
    "imysqt90165@chacuo.net": "xyj@1007",
    "2036137286@qq.com": "xyj@1007",
    "jviksa47192@chacuo.net": "ssssssss",
    "qirymh71549@027168.com": "xyj@1007"
}

for name, password in message_dic.items():
    count = 0
    login_url = 'https://www.520ssr.me/auth/login'

    drive = webdriver.Chrome()
    drive.get(login_url)
    username_input = drive.find_element_by_name("Email")
    password_input = drive.find_element_by_name("Password")

    username_input.send_keys(name)
    password_input.send_keys(password)
    drive.find_element_by_id("login").click()
    time.sleep(2)
    _url = 'https://www.520ssr.me/user'
    drive.get(_url)
    drive.find_element_by_id("checkin").click()
    drive.close()
    count += 1
    if count == len(message_dic):
        print("game_over")
        break
