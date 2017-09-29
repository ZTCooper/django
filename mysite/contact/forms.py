from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length = 100)
							#设置长度限制，也可用min_length
	email = forms.EmailField(required = False, label = 'Your e-mail address')
							#可选，label自定义字段标签
	message = forms.CharField(widget = forms.Textarea)
							#替换掉默认部件

	def clean_message(self):	#为message字段增加额外校验
		message = self.cleaned_data['message']
		num_words = len(message.split())	#split()分词后取len()
		if num_words < 4:
			raise forms.ValidationError('Not enough words!')
		return message
		#很重要，若无，则返回None，原始数据丢失
