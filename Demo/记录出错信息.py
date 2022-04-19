# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2021/12/27}

err_path, err_nums, err_count, = [], [], []
with open("D:\PYproject\Demo\\123.txt") as file1, open("D:\PYproject\Demo\\23.txt", "w") as file2:
    for line in file1:
        names = line.split("\\")[-1].replace("\n", "")
        if len(names) > 16:
            err_path.append(names[-16:])
        else:
            err_path.append(names)
    print(err_path)

    for name in err_path:
        if name not in err_count:
            err_count.append(name)
            err_nums.append(name + " " + str(1))
        else:
            for i in range(1, len(err_nums)):
                if name == err_nums[i].split(" ")[0] + " " + err_nums[i].split(" ")[1]:
                    err_nums[i] = name + " " + str(int(err_nums[i].split(" ")[2]) + 1)
                    # print(err_nums[i])
    print(err_nums)
    for name in err_nums[-8:]:
        # print(name)
        file2.write(name + '\n')
