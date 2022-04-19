# evaluate
*** Test Cases ***
case1
    ${list}  evaluate  [i for i in range(100)]
    ${list}  evaluate  $list[:30]
    ${dict}  evaluate  {"a":"1","b":2}
    ${var1}  evaluate  $dict.update({"a":"world"})
    log to console  ${var1}
    log to console  ${list}
    log to console  ${dict}