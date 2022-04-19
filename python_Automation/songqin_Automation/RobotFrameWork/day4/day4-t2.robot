*** Settings ***
Resource  rclib.robot  # 导入资源文件
*** Test Cases ***
case1
    [Template]   datadriven
    # 不写关键字，写关键字的参数
    20200521
    20200522

*** Keywords ***
datadriven
    [Arguments]   ${data}
    ${res}  checklog3  ${data}
    log to console  ${res}