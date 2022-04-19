*** Settings ***
Library  course_mgr
Library  SeleniumLibrary
*** Test Cases ***
case1
    ${courses}  listCourse
    FOR  ${cour}  IN   @{courses}
    log to console  ${cour}
    END
    should be true   ${courses}==['大学英语1573961896814', '大学英语1573961937773', '高中物理0001', '高中物理00013', '高中物理00015顶顶1111', '高中物理00015顶顶1111sssss', '高中物理00015顶22222', '高中物理00015顶22222wwww', 'A', 'B', '初中化学1573916385932', '初中化学33333332', '初中化学q2323', '初中化学1573916476554', '初中化学1573961141814', '初中化学1573961143877', '初中化学1573961144670', '初中化学1573961145398', '初中化学1573961146140', '初中化学1573961147002']
case2
    open browser  https://www.vmall.com/  chrome
    set selenium implicit wait  10
    ${goods}  get webelements  css=.home-recommend-goods.home-hot-goods.grid-title
    evaluate  [good.text for good in $goods]
    ${res}  log to console  ${goods}

    close browser
