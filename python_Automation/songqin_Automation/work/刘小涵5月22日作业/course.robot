*** Settings ***
Library  SeleniumLibrary
Library  courselib
*** Test Cases ***
添加课程
    [Setup]  deleteAllLesson
    [Teardown]  deleteAllLesson
    open browser  http://localhost/mgr/login/login.html  chrome
    set selenium implicit wait  10
    # 登录
    input text  id=username  auto
    input text  id=password  sdfsdfsdf
    click element  css=.btn-success
    # 创建课程
    click element  css=[ng-click="showAddOne=true"]
    input text  css=[ng-model="addData.name"]  robot
    input text  css=[ng-model="addData.desc"]  RF框架
    input text  css=[ng-model="addData.display_idx"]  1
    click element  css=[ng-click="addOne()"]
    # 检查添加的课程
    ${course}  get text  css=tbody td:nth-child(2)
    should be true   $course=='robot'
    close browser