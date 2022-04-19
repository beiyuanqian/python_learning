*** Settings ***
Library    Selenium2Library
Library    Collections
Resource    rflib/rc.robot


*** Test Cases ***

添加课程
    [Setup]  DeleteAllCourse



    addCourse    初中语文    初中语文   2

    ${lessons}=  GetCourseList

    Should Be True   $lessons==[u'初中语文']


    addCourse    初中数学    初中数学   1

    ${lessons}=  GetCourseList

    Should Be True   $lessons==[u'初中数学',u'初中语文']


    [Teardown]     DeleteAllCourse