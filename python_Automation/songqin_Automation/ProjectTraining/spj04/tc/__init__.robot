*** Settings ***
Library    pylib.SchoolClassLib
Library    pylib.TeacherLib
Suite Setup     Run Keywords   delete all teachers   AND
                ...  delete all school classes
