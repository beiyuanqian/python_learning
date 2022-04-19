*** Settings ***
Resource  rflib/rc.robot
*** Test Cases ***
# 方法一：
#添加老师1
#    [Setup]  teachersetup
#    [Teardown]
#
#*** Keywords ***
#teachersetup
#    deleteAllTeacher
#    deleteAllLesson
#    addcourse  初中语文  语文课  2
#    addcourse  初中数学  数学课  1
# 方法二
添加老师1
    [Setup]  run keywords  deleteAllTeacher  AND  deleteAllLesson
    ...  AND  addcourse  初中语文  语文课  2
    ...  AND  addcourse  初中数学  数学课  1
    [Teardown]  run keywords  deleteAllTeacher  AND  deleteAllLesson
    addTeacher  张老师  xiaozhang  语文老师  1  初中语文
    checkTeacher  张老师
