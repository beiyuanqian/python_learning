# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/3/11}

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = "http://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code: ", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories: ", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

# # 处理结果
# print(response_dict.keys())

# # 研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\nKeys: ", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# # 概述最受欢迎的仓库
# print("\nSelected information about first repository: ")
# for repo_dict in repo_dicts:
#     print("\nName: ", repo_dict['name'])
#     print("Owner: ", repo_dict['owner']['login'])
#     print("Stars: ", repo_dict["stargazers_count"])
#     print("Repository: ", repo_dict['html_url'])
#     print("Created: ", repo_dict["created_at"])
#     print("Updated: ", repo_dict['updated_at'])
#     print("Description: ", repo_dict['description'])

# Github上受欢迎程度最高的Python项目
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)
# 可视化
my_style = LS("#333366", base_style=LCS)

# 改进pygal图表
my_config = pygal.Config()
# 让标签绕x轴旋转45°
my_config.x_label_rotation = 45
# 隐藏图例
my_config.show_legend = False
# 设置图表标题字体大小
my_config.title_font_size = 24
# 设置副标签字体大小
my_config.label_font_size = 14
# 设置主标签字体大小
my_config.major_label_font_size = 18
# 将较长的项目名缩短为15个字符
my_config.truncate_label = 15
# 隐藏图表中的水平线
my_config.show_y_guides = False
# 设置自定义宽度，
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-Starred Python Projects on Github"
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file("python_repos.svg")
