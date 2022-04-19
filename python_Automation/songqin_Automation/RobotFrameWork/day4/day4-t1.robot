# 如何定义用户关键字
*** Test Cases ***
case1
#    checklog
#    checklog2  20200524
    ${res}  checklog3  20200524
    log to console  ${res}

# 定义用户关键字
*** Keywords ***
checklog
    ${var}  set variable  hello
    log to console  ${var}
    should be true  $var=='hello'

checklog2
    [Arguments]  ${expect}
    ${var}  set variable  ${expect}
    log to console  ${var}
    should be true  $var==$expect

checklog3
    [Arguments]  ${expect}
    ${var}  set variable  ${expect}
    log to console  ${var}
    should be true  $var==$expect
    [Return]    Sucess

