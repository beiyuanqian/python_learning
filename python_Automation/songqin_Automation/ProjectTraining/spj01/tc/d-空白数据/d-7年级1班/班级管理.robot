*** Settings ***
Library    pylib.SchoolClassLib


*** Test Cases ***
添加班级2 - tc000002
    ${addret1}=    add school class    1     2班     58
    should be true     $addret1['retcode']==0

#列出班级，检验一下
    ${listret2}=    list school class    1
    ${fc}=   evaluate   $listret2['retlist']
    should be true    {"name":"2班"}

    [Teardown]    delete_school_class   &{addret1}[id]