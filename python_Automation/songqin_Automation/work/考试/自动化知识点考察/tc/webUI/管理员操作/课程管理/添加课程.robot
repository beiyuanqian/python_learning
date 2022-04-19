*** Settings ***
Resource  rflib/rc.robot
*** Test Cases ***
添加课程
    [Setup]  deleteAllLesson
    [Teardown]  deleteAllLesson
    # 创建课程
    addCourse  robot  RF框架  1
    # 检查添加的课程
    checkCourse  robot


添加课程2
    [Setup]  deleteAllLesson
    [Teardown]  deleteAllLesson
    # 创建课程
    addCourse  selenium  webUI测试  2
    # 检查添加的课程
    checkCourse  selenium
