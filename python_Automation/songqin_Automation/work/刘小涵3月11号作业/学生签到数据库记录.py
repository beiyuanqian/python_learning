"""
要求大家实现下面的函数。其中参数fileName为数据库记录文件路径， 输出结果是将数据库记录文件中的学生签到信息保存在一个字典对象中，并作为返回值返回。
def putInfoToDict(fileName):
要求返回的字典对象的格式是这样的：key是各个学生的id号， value是该学生的签到信息,其中value，里面保存着该学生所有签到的信息
其中每个签到的信息是字典对象，有两个元素： key是lessonid的记录课程id，key是checkintime的记录签到时间
比如，对于上面的示例中的3条记录，相应的返回结果如下：
{
    131: [{'lessonid': 271, 'checkintime': '2017-03-13 11:50:09'},{'lessonid': 273, 'checkintime': '2017-03-14 10:52:19'},],
    126: [{'lessonid': 271, 'checkintime': '2017-03-13 11:50:19'},],
}
"""
def putInfoToDict(fileName):
    dict={}


    list=[]
    with open(fileName) as fileName:
        info = {}
        lines = fileName.readlines()
        for line in lines:
            # print(line)
            part=line.split("(")[1].split(")")[0].split(",")
            id_students=part[2]
            id_lessons=part[1]
            time=part[0].split("'")[1]
            info['lessonid']=id_lessons
            info['checkintime']=time
            # info={'lessonid':id_lessons,'checktime':time}


            print(info)

            if id_students not in dict:
                dict[id_students] = []
            dict[id_students].append(info)

    return dict

putInfoToDict('File.txt')
