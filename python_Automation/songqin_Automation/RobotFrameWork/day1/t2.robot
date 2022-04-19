# 配置表——大小写敏感
*** Settings ***
# 引入第三方库
Library  SeleniumLibrary
Library  Collections
Library  RequestsLibrary

# 用例表——大小写不敏感
*** Test Cases ***
case1
    [Documentation]  自动化搜搜松勤
    # 打开浏览器
    Open Browser  http://baidu.com  chrome
    set selenium implicit wait  10
    input text  id=kw  松勤\n
    ${res}=    get text  id=1
    should contain  ${res}  松勤网
    close browser
case2
    log to console  用例2
case3
    log to console  用例3

case4
