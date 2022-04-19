*** Test Cases ***
# 列表
case1
    # 如何使用变量和定义时候使用的符号没有关系，只和传参的时候有关
    @{list}  create list  1  2  3
#    log many  @{list}  # 以list形式传参，相当于展开列表内的元素，作为多个参数进行传参
    log many  @{list}[0]  # 使用下标取参数或@{list[0]}
#    log many  1   2   3
#    log many  ${list}  # 以普通形式传参，就把变量作为一个整体进行传递
# 字典
case2
    ${dict}  create dictionary   a=1  b=2  c=3
    log to console  ${dict}
    log many  &{dict}  # 传递的字典的键值对
    log to console  ${dict['a']}
    log to console  &{dict}[a]