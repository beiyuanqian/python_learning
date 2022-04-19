# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2020/7/3}

# 7、浏览器进入网页云音乐  https://music.163.com/
# 在首页的发现音乐菜单，点击进入排行榜>云音乐新歌版
# 查看排名前三的歌曲下的评论，在精彩评论部分找到点赞数量最高的评论，获取评论作者，内容，时间和当前点赞数量

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://y.music.163.com/")

sleep(5)
driver.quit()
