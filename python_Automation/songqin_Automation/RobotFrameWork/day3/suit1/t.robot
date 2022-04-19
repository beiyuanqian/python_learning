*** Test Cases ***
setupANDteardown
    [Setup]  fail
#    [Setup]  log to console  执行用例初始化动作
    # 任何情况下setup和teardown都会执行，即使主体出错，如果setup失败，用例主体不会执行
    [Teardown]  log to console  执行用例清除动作
    log to console  执行用例主体
    should be true  1>2

setupANDteardown1
    [Setup]  log to console  执行用例初始化动作
    log to console  执行用例主体
    should be true  1<2

setupANDteardown2
    [Teardown]  log to console  执行用例清除动作
    log to console  执行用例主体
    should be true  1<2