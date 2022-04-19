#*** Variables ***
#${MgrLoginUrl}  http://localhost/mgr/login/login.html
#${StudentLoginUrl}  http://localhost/student/login/login.html
#@{database}  127.0.0.1  3306
#&{user1}  name=auto  pw=sdfsdfsdf
*** Settings ***
Variables  cfg.py
*** Test Cases ***
case1
    log to console  ${MgrLoginUrl}
    log to console  ${StudentLoginUrl}
    log to console  ${database}
    log to console  ${user1}

