*** Settings ***
Library    Selenium2Library
Library    Collections
Resource    rflib/rc.robot


*** Test Cases ***

添加老师1
    [Setup]   Run Keywords   DeleteAllCourse
    ...  AND  DeleteAllTeacher
    ...  AND  AddCourse   初中语文    初中语文描述    1
    ...  AND  AddCourse   初中数学    初中数学    2




    Click Element   css=ul.nav a[href*=teacher]
    Sleep  1  # wait for teacher info displayed

    AddTeacher        庄子    zhuangzi    庄子老师   1   初中语文

    ${teachers}=       GetTeacherList
    Should Be True    $teachers==[u'庄子']


    AddTeacher        孔子    kongzi    孔子老师   2     初中数学

    ${teachers}=       GetTeacherList
    Should Be True    $teachers==[u'庄子',u'孔子']



    [Teardown]    Run Keywords   DeleteAllCourse   AND  DeleteAllTeacher