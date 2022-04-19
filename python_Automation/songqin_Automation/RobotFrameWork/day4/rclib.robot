# 资源文件——和套件文件形式一致
# 区别是资源文件没有用例表

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
