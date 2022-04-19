*** Settings ***
Library    pylib.SchoolClassLib


*** Test Cases ***
添加班级1 - tc000001
    ${addret1}=    add school class    1     1班     60
    should be true     $addret1['retcode']==0

#列出班级，检验一下
    ${listret2}=    list school class    1
    ${fc}=   evaluate   $listret2['retlist'][0]
    should be true    $fc['id']==$addret1['id']
    should be true    $fc['invitecode']==$addret1['invitecode']

    [Teardown]    delete_school_class   &{addret1}[id]