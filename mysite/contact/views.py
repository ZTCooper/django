from django.core.mail import send_mail 
#此函数有四个必选参数：主题，正文，寄信人和收件人列表
from django.http import HttpResponseRedirect
#将网页重新定向至一个包含成功信息的页面
from django.shortcuts import render_to_response
from contact.forms import ContactForm

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial = {'subject':'I love your site!'}
            #设置初始值
            )    #实例化对象
    return render_to_response('contact_form.html', {'form': form})
    '''
    return render_to_response('contact_form.html',
        {'errors': errors,
        'subject': request.POST.get('subject',''),
        'message': request.POST.get('message',''),
        'email': request.POST.get('email',''),
        #若发生错误将原始填写数据一起返回以便查看
        })
    '''

def thanks(request):
    return render_to_response('contact_thanks.html',{})