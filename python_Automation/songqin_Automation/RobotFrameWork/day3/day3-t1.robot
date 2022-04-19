*** Test Cases ***
条件判断
    run keyword if  10>9  log to console  测试通过
    ${year}   set variable  {"a":1}  # 传入的是字符串
    run keyword if  ${year}=='2020'  log to console  测试通过
    should be true  $year=='{"a":1}'  # 只有当关键字的参数是python表达式的时候，可以采用$year格式
    log to console  ${year}
条件判断2
    ${date}  get time
    run keyword if  '2020' in $date and '08' in $date
    ...  log to console  pass  # 换行方法
    log to console  ${date}
条件判断3-条件成立只能执行一个关键字
    ${date}  get time
    run keyword if  '2020' in $date and '08' in $date
    ...  log to console  pass
    ...  log to console  ${date}  # 结果不会打印


条件判断-分支
    ${date}  get time
    run keyword if  '2021' in $date  log to cosnole  今年是2021年
    ...  ELSE  log to cosnole 今年不是2021年
条件判断-多分支
    ${date}  get time
    run keyword if  '2021' in $date  log to cosnole  今年是2021年
    ...  ELSE IF  '05' in $date  log to console  现在是5月份
    ...  ELSE  log to console  现在天气很热
