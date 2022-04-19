*** Settings ***
Library  SeleniumLibrary
Variables  cfg/cfg.py
*** Keywords ***

${data}    set Variable    { "version": "1.0"}
${uri} set variable    /xxxx/xxxx/query
${dict}    create Dictionary   Host=http://localhost/mgr/login/login.html   Content-Type=application/x-www-form-urlencoded
create session  query   http://api.xxxx.com ${dict}
${response}	post request	query	${uri}  ${data}	headers=${dict}
${res}	To Json	${response.content}
log ${res["result_msg"]}
步骤讲解：
请求数据设置成变量${data}
${uri} 参数设置
构造请求头字典${dict}
创建一个query session
${response} 接收请求变量
${response.content} 转成json 对象
打印请求结果中的内容

loginwebsite
    # 手动访问业务地址——driver.get(url)
    go to  http://localhost/mgr/login/login.html
    # 登录
    input text  id=username  ${user1}[name]
    input text  id=password  ${user1}[pw]
    click element  css=.btn-success
addCourse
    [Arguments]  ${name}  ${desc}  ${idx}=1
    click element  css=[ng-click="showAddOne=true"]
    input text  css=[ng-model="addData.name"]  ${name}
    input text  css=[ng-model="addData.desc"]  ${desc}
    input text  css=[ng-model="addData.display_idx"]  ${idx}
    click element  css=[ng-click="addOne()"]
checkCourse
    [Arguments]  ${expect}
     # 确保在课程界面
    click element  css=[ui-sref="course"]
    ${course}  get text  css=tbody td:nth-child(2)
    should be true   $course==$expect
deleteAllLesson
    # 确保在课程界面
    click element  css=[ui-sref="course"]
    # 删除课程
    set selenium implicit wait  1
    FOR  ${i}  IN RANGE  9999
        ${del_btns}  get webElements  css=[ng-click="delOne(one)"]
        # 判断当删除按钮没有时，退出删除课程操作
        run keyword if  $del_btns == []  exit for loop
        click element  ${del_btns[0]}  # 点击删除按钮
        #  点击确定框
        click element  css=.btn-primary
        # 等待弹出框消失
        sleep  1
    END
    set selenium implicit wait  10

setupwebtest
    open browser  http://localhost  chrome
    set selenium implicit wait  10
    log to console  打开浏览器
teardownwebtest
    close browser
    log to console  关闭浏览器

deleteAllTeacher
    # 确保在老师界面
    click element  css=[href="#/teacher"]
    # 开始删除老师
    set selenium implicit wait  2
    FOR  ${i}  IN RANGE  9999
        ${del_btns}  get webElements  css=[ng-click="delOne(one)"]
        # 判断当删除按钮没有时，退出删除老师操作
        run keyword if  $del_btns == []  exit for loop
        # 点击删除按钮
        # click element  ${del_btns[0]}
        evaluate  $del_btns[0].click()
        # 点击确定框
        click element  css=.btn-primary
        # 等待弹出框消失
        sleep  2
    END
    set selenium implicit wait  10

addTeacher
    [Arguments]  ${realname}  ${username}  ${desc}  ${idx}  ${course}
    # 确保在老师界面
    click element  css=[href="#/teacher"]
    click element  css=[ng-click="showAddOne=true"]
    input text  css=[ng-model="addEditData.realname"]  ${realname}
    input text  css=[ng-model="addEditData.username"]  ${username}
    input text  css=[ng-model="addEditData.desc"]  ${desc}
    input text  css=[ng-model="addEditData.display_idx"]  ${idx}
    # 关联授课信息
    select from list by label  css=[ng-model="$parent.courseSelected"]  ${course}
    click element  css=[ng-click="addEditData.addTeachCourse()"]
    click element  css=[ng-click="addOne()"]
checkTeacher
    [Arguments]  ${expect}
    # 确保在老师界面
    click element  css=[href="#/teacher"]
    ${realname}  get text  css=tbody td:nth-child(2)
    should be true   $realname==$expect