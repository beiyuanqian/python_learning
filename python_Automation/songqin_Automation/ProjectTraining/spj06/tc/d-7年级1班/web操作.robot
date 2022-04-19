*** Settings ***
Library  pylib.WebOpLib
Library  pylib.TeacherLib
Variables  cfg.py

Suite Setup   open browser
Suite Teardown   close browser


*** Test Cases ***
老师登录1 - tc005001

    ${addRet}=  add teacher    tuobahong   拓跋宏
           ...  ${g_subject_math_id}
           ...  ${suite_g7c1_classid}
           ...  13000000001  1301@g.com  320520001

    should be true  $addRet['retcode']==0


    teacher login   tuobahong   888888

    ${teacherinfo}=  get_teacher_homepage_info
    ${eteacherinfo}=  create list  松勤学院0001   拓跋宏
                  ...  初中数学   0   0   0

    should be equal   ${teacherinfo}    ${eteacherinfo}


    ${classstudent}=  get_teacher_class_students_info
    should be true   $classstudent=={'七年级1班':[]}

    [Teardown]  delete teacher   &{addRet}[id]