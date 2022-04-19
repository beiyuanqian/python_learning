*** Keywords ***
loginwebsite
    # 手动访问业务地址——driver.get(url)
    go to  http://localhost/mgr/login/login.html
    # 登录
    input text  id=username  auto
    input text  id=password  sdfsdfsdf
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
    ${course}  get text  css=tbody td:nth-child(2)
    should be true   $course==$expect
deleteAllLesson
    loginwebsite
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