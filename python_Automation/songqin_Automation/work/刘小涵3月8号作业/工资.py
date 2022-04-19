file1='file1.txt'
file2='file2.txt'
with open(file1) as file1,open(file2,'w') as file2:
    lines=file1.readlines()
    for line in lines:
        name=line.split(";")[0].split(':')[1].strip()
        salary=int(line.split(";")[1].split(':')[1].strip())
        tax=int(salary*0.1)
        income=int(salary*0.9)
        outputstr='name:{:8};   salary:{:8};   tax:{:8};   income:{:8}'.format(name,salary,tax,income)
        print(outputstr)
        file2.write(outputstr + '\n')