from pylib.SchoolClassLib import  SchoolClassLib

sc = SchoolClassLib()

class C000082a():
    def  steps(self):

        print('''\n\n***** step 1 ****  列出班级，保存列表\n''')

        listRet1 = sc.list_school_class(1)


        print('''\n\n***** step 2 ****  添加 7年级2班 \n''')
        addRet = sc.add_school_class(1, '2班', 60)
        if addRet['retcode'] != 0:
            raise Exception('返回值非0')



        print('''\n\n***** step 3 ****  列出班级，检验一下\n''')

        listRet2 = sc.list_school_class(1)
        sc.classlist_should_contain(listRet2['retlist'],
                                    '2班',
                                    '七年级',
                                    addRet['invitecode'],
                                    60,
                                    0,
                                    addRet['id'])


        print('''\n\n***** step 4 ****  删除 7年级2班\n''')
        ret = sc.delete_school_class(addRet['id'])
        if ret['retcode'] != 0:
            raise Exception('删除失败')



        print('''\n\n***** step 5 ****  列出班级，检验一下\n''')

        listRet3 = sc.list_school_class(1)
        if listRet1 != listRet3:
            raise Exception('删除结果不正确')