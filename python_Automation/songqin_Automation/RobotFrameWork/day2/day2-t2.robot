# 引入自定义都得库文件
*** Settings ***
Library  testlib
# 导入自动义库，执行的时候需要指定pythonpath，robot --pythonpath . t2.robot或robot -P . t2.robot
*** Test Cases ***
case1
    ${var}   gettime1
    log to console  ${var}
case2
    ${var}   webapi  http://www.baidu.com
    log to console  ${var}

