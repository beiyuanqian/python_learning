from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.views.decorators.csrf import csrf_exempt
from sgin.models import Event, Guest, GuestEvent


# Create your views here.
# 发布会视图
def events(request):
    # # 初试页面查看
    # return HttpResponse('测试开发课程发布会')

    # # 尝试返回拼接字符串
    # event_list = ['测开课程发布会', '自动化发布会', '性能发布会', '安全发布会', '全栈发布会', 'ISTQB', 'TM项目管理', 'PMP考证']
    # return HttpResponse(' | '.join(event_list))

    # # 内容套在<li>中
    # event_list = ['测开课程发布会', '自动化发布会', '性能发布会', '安全发布会', '全栈发布会', 'ISTQB', 'TM项目管理', 'PMP考证']
    # content = '<ol>'
    # for event in event_list:
    #     content += f'<li>{event}</li>'
    # content += '</ol>'
    # return HttpResponse(content)

    # # 尝试使用html文件访问,此处可不添加sgin文件夹，event.html直接放在templates中，并直接引用event.html
    # return render(request, 'sgin/event.html')

    # # 引用变量返回页面内容
    # event_list = ['测开课程发布会', '自动化发布会', '性能发布会', '安全发布会', '全栈发布会', 'ISTQB', 'TM项目管理', 'PMP考证']
    # return render(request, 'sgin/event1.html', {'event_list': event_list})

    # # 使用标签渲染页面,使用for循环遍历参数
    # event_list = ['测开课程发布会', '自动化发布会', '性能发布会', '安全发布会', '全栈发布会', 'ISTQB', 'TM项目管理', 'PMP考证']
    # return render(request, 'sgin/event2.html', {'event_list': event_list})

    # # 使用模板美化页面，只考虑当前页
    # event_list = ['测开课程发布会', '自动化发布会', '性能发布会', '安全发布会', '全栈发布会', 'ISTQB', 'TM项目管理', 'PMP考证']
    # return render(request, 'sgin/base1.html', {'event_list': event_list})

    # 使用模板美化页面，考虑多个页面样式相同
    # event_list = ['测开课程发布会', '自动化发布会', '性能发布会', '安全发布会', '全栈发布会', 'ISTQB', 'TM项目管理', 'PMP考证']
    # return render(request, 'sgin/events.html', {'event_list': event_list})

    # 使用真实数据从数据库进行查询所有发布会信息
    event_list = Event.objects.all()
    return render(request, 'sgin/events.html', {'event_list': event_list})


# # 返回发布会详情
# def event_detail(request):
#     return render(request, 'sgin/event_detail.html')
# 返回指定id的发布会详情
def event_detail(request, event_id):
    # 根据event_id查询对应的发布会数据
    event = Event.objects.get(pk=event_id)  # pk 主键，默认为id
    return render(request, 'sgin/event_detail.html', {'event': event})


# 嘉宾列表视图
def guests(request):
    # 查询所有嘉宾
    guest_list = Guest.objects.all()
    return render(request, 'sgin/guests.html', {'guest_list': guest_list})


# 嘉宾详情页
def guest_detail(request, guest_id):
    # 根据 id 查找嘉宾信息
    guest = Guest.objects.get(id=guest_id)
    return render(request, 'sgin/guest_detail.html', {'guest': guest})


# 处理签到逻辑
# @csrf_exempt  # 加上可以取消csrf防护，也可以在表单内部加上{% csrf_token %}
def do_sgin(request, event_id):
    # # 请求是通过POST方法传递过来的,尝试先拿到手机号
    # if request.method == 'POST':
    #     phone = request.POST['phone']
    #     return HttpResponse(f'拿到手机号：{phone}')
    #     # 判断手机号是否正确，根据手机号能否搜索到嘉宾判断

    # # 请求是通过POST方法传递过来的,判断手机号是否正确
    # if request.method == 'POST':
    #     phone = request.POST['phone']
    #
    #     # 判断手机号是否正确，根据手机号能否搜索到嘉宾判断
    #     res = Guest.objects.filter(phone=phone)
    #     if not res:
    #         # return HttpResponse('手机号错误')
    #         return render(request, 'sgin/event_detail.html',
    #                       {'event': Event.objects.get(id=event_id), 'error': '手机号错误'})
    #
    #     # 是否属于当前发布会的嘉宾  嘉宾关联的发布会id是否和当前发布会ID一致
    #     guest = res[0]
    #     if guest.event.id != event_id:
    #         return HttpResponse('非当前发布会嘉宾')
    #     #     return render(request, 'sgin/event_detail.html', {'event': guest.event, 'error': '非当前发布会嘉宾'})
    #
    #     # 是否已经签到
    #     if guest.is_sgin:
    #         return HttpResponse('已签到，不要重复签到')
    #
    #     # 正式签到
    #     guest.is_sgin = True
    #     guest.save()  # 保存更新
    #     return HttpResponse(f'拿到手机号：{phone}，签到成功')

    # 请求是通过POST方法传递过来的,判断手机号是否正确,，如果正确，返回签到成功页
    if request.method == 'POST':
        phone = request.POST['phone']

        # 判断手机号是否正确，根据手机号能否搜索到嘉宾判断
        res = Guest.objects.filter(phone=phone)
        if not res:
            # return HttpResponse('手机号错误')
            return render(request, 'sgin/event_detail.html',
                          {'event': Event.objects.get(id=event_id), 'error': '手机号错误'})

        # # 当关联的发布会是单选时
        # # 是否属于当前发布会的嘉宾
        # guest = res[0]
        # if guest.event.id != event_id:
        #     # return HttpResponse('非当前发布会嘉宾')
        #     return render(request, 'sgin/event_detail.html', {'event': guest.event, 'error': '非当前发布会嘉宾'})

        # # 是否已经签到
        # if guest.is_sgin:
        #     # return HttpResponse('已签到，不要重复签到')
        #     return render(request, 'sgin/event_detail.html', {'event': guest.event, 'error': '已签到，不要重复签到'})

        # # 正式签到
        # guest.is_sgin = True
        # guest.save()  # 保存更新
        # # return redirect(request, 'sgin/sgin_success.html', {'phone': phone})
        # # 使页面重定向至签到成功页
        # return redirect(f'/sgin/sgin_success/{phone}')

        # 当关联的发布会是多选时
        # 嘉宾关联的发布会id是否和当前发布会ID一致
        guest = res[0]
        event_ids = [event.id for event in guest.events.all()]
        if event_id not in event_ids:
            # return HttpResponse('非当前发布会嘉宾')
            return render(request, 'sgin/event_detail.html', {'event': guest.events, 'error': '非当前发布会嘉宾'})

        # 获取关联关系
        relation = GuestEvent.objects.get(guest_id=guest.id, event_id=event_id)
        # 是否已经签到
        if relation.is_sgin:  # 通过关联关系查看是否签到
            return render(request, 'sgin/event_detail.html', {'event': event_id, 'error': '已签到，不要重复签到'})

        # 正式签到
        relation.is_sgin = True
        relation.save()  # 保存更新
        return redirect(f'/sgin/sgin_success/{phone}')


# 签到成功页
def sgin_success(request, phone):
    return render(request, 'sgin/sgin_success.html', {'phone': phone})


# 新增发布会页面
def add_event_page(request):
    event_list = Event.objects.all()
    return render(request, 'sgin/event_add.html', {'event_list': event_list})


# 新增发布会视图
def add_event(request):
    if request.method == 'POST':
        in_params = request.POST.get  # 返回字典
        # 发布会名称
        name = in_params('name')
        # 地址
        address = in_params('address')
        # 人数
        limits = in_params('limits')

        # 创建发布会
        try:
            Event.objects.create(name=name, address=address, limits=limits)
        except Exception as e:
            # repr(e) 精简错误信息
            return render(request, 'sgin/event_add.html', {'error': repr(e)})

        # 保存成功 跳转到嘉宾列表页面
        return redirect('/sgin/events/')


# 新增嘉宾表单页面
def add_guest_page(request):
    event_list = Event.objects.all()
    return render(request, 'sgin/guest_add.html', {'event_list': event_list})


# 新增嘉宾视图
def add_guest(request):
    if request.method == 'POST':
        in_params = request.POST  # 返回字典
        # 姓名
        name = in_params['name']
        # 手机号
        phone = in_params['phone']
        # 邮箱
        email = in_params['email']

        # # 关联发布会--只可以传一个id时
        # event_id = in_params['event_id']
        # # 创建嘉宾
        # try:
        #     Guest.objects.create(name=name, phone=phone, email=email, event_id=event_id)
        # except Exception as e:
        #     # repr(e) 精简错误信息
        #     return render(request, 'sgin/guest_add.html', {'error': repr(e)})
        #
        # # 保存成功 跳转到嘉宾列表页面
        # return redirect('/sgin/guests/')

        # 关联发布会--可以传多个发布会ID
        # event_ids = in_params.['event_ids'] # 只会取到列表最后一个值
        event_ids = in_params.getlist('event_ids')  # 获取id的列表

        # 创建嘉宾
        try:
            with transaction.atomic():  # 数据库事务，失败时回滚
                # 此时嘉宾和发布会是多对多关系，不用外键进行关联
                guest = Guest.objects.create(name=name, phone=phone, email=email)  # 先创建嘉宾数据
                # 根据ID获取发布会信息
                event_list = [Event.objects.get(pk=event_id) for event_id in event_ids]
                # 嘉宾关联多个发布会
                # guest.events.add(*event_list)
                for event in event_list:
                    GuestEvent.objects.create(guest=guest, event=event)
        except Exception as e:
            # repr(e) 精简错误信息
            return render(request, 'sgin/guest_add.html', {'error': repr(e)})

        # 保存成功 跳转到嘉宾列表页面
        return redirect('/sgin/guests/')
