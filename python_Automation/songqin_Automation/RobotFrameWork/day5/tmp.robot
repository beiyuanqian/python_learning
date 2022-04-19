*** Settings ***
Resource  tmp2.robot

*** Test Cases ***
case1
    log to console  ${MgrLoginUrl}
    log to console  ${StudentLoginUrl}
    log to console  ${database}
    log to console  ${user1}
