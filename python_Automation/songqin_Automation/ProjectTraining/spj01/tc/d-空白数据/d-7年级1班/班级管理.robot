*** Settings ***
Library    pylib.SchoolClassLib


*** Test Cases ***
��Ӱ༶2 - tc000002
    ${addret1}=    add school class    1     2��     58
    should be true     $addret1['retcode']==0

#�г��༶������һ��
    ${listret2}=    list school class    1
    ${fc}=   evaluate   $listret2['retlist']
    should be true    {"name":"2��"}

    [Teardown]    delete_school_class   &{addret1}[id]