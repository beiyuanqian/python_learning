*** Settings ***
Library  SeleniumLibrary
*** Test Cases ***
case1
    # scalar
    ${var1}  set variable  {"a":1}
    ${var2}  set variable  hello
    ${var3}  set variable  [1,2,3]
    ${num}  convert to integer  2020

#    log to console  ${var1}  # 会输出到控制台
#    log  ${var1}  # 不会输出到控制台，输出到日志
#    sleep  5  # 默认时间是秒，可以设置其他时间单位1d,2h,3m,4s,5ms
    # should contain  ${var}  hello
    # should be equal  ${2020}  ${num}
    # should be true  10<9
#    should be true  2020==${num}
#    should be true  {"a":1}==${var1}
#    should be true  'hello'=='${var2}'  # 或$var
#    should be true  [1,2,3]==${var3}  # 列表或字典比较时，不能缺少{}
    should be true  'hello'.startswith('he')

