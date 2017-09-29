# -*- coding: utf-8 -*-

#from django.template.loader import get_template
#from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def hello(request):     # request 必须为第一个参数
    return HttpResponse(u'你好, world')     # 返回实例化


def current_datetime(request):
    
    now = datetime.datetime.now()
    
    #t = get_template('current_datetime.html')
    #html = t.render(({'current_date': now}))    #传入参数必须为dict，t.render(Context('':now)报错)
    
    return render_to_response('current_datetime.html', {'current_date':now})
                                #返回HttpResponse对象
                                #第一个参数必须为模板名称，第二个参数为Context dict，若无则使用空dict
                                # locals() 可传入当前所有局部变量
                                #代码可进一步修改，replace('current_date', 'now'), replace(locals(), dict)

def hours_ahead(request, offset):   #多了一个参数offset表示时间差
    try:                            
        offset = int(offset)
    except ValueError:
        raise Http404()             #捕获异常，raise一个404Error
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    #assert False
    #html = '<html><body>In %s hour(s), it will be %s.</body></html>' % (offset,dt)
    return render_to_response('hours_ahead.html', {'hour_offset':offset, 'next_time':dt})

def display_meta(request):
    values = request.META.items()
    #html = []
    return render_to_response('display_meta.html', {'values':values})
    #    html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    #return HttpResponse('<table>%s</table>' % '\n'.join(html))