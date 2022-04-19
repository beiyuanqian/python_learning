# For循环，关键字符要大写
*** Test Cases ***
For循环-老语法
    :FOR  ${a}  IN  a  b  c
    log to console  ${a}
    log to console  循环体外面

FOR循环—新语法
#    FOR  ${a}  IN  a  b  c  d
    ${list}  create list  a  b  c  d  e
    FOR  ${a}  IN  @{list}
    log to console  ${a}
    END  # 表示循环结束
    log to console  循环体外面
FOR循环-RANGE
    # FOR IN RANGE 都要注意大写
    FOR  ${a}  IN RANGE  10
    LOG TO CONSOLE  ${a}
    END  # 表示循环结束
    log to console  循环体外面
FOR循环-RANGE-指定区间
    # FOR IN RANGE 都要注意大写
    FOR  ${a}  IN RANGE   5   10
    LOG TO CONSOLE  ${a}
    END  # 表示循环结束
    log to console  循环体外面