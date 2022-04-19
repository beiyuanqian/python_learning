*** Settings ***
Library  SeleniumLibrary
Resource  course.robot  # 导入资源文件
Suite Setup  setupwebtest
Suite Teardown  teardownwebtest
*** Test Cases ***
添加课程
    [Setup]  deleteAllLesson
    [Teardown]  deleteAllLesson
    loginwebsite
    # 创建课程
    addCourse  robot  RF框架  1
    # 检查添加的课程
    checkCourse  robot


添加课程2
    [Setup]  deleteAllLesson
    [Teardown]  deleteAllLesson
    loginwebsite
    # 创建课程
    addCourse  selenium  webUI测试  2
    # 检查添加的课程
    checkCourse  selenium
