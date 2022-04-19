*** Settings ***
Library  Collections  # RF操作列表和字典的一个库
*** Test Cases ***
case1
    ${list}  create list  1  2  3
    log to console  ${list}
    append to list  ${list}  a  b  c
    log to console  ${list}
    remove from list  ${list}  0
    log to console  ${list}
    log many  @{list}
    log many  ${list}
