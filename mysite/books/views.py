from django.http import HttpResponse
from django.shortcuts import render_to_response
from books.models import Book

# Create your views here.
def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	errors = []
	if 'q' in request.GET: #and request.GET['q']:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters.')
		else:
			books = Book.objects.filter(title__icontains=q)	#icontains是查询关键字
			return render_to_response('search_results.html',
				{'books':books, 'query':q})
		#message = 'You searched for: %r' % request.GET['q']
	return render_to_response('search_form.html', {'errors':errors})
	#return HttpResponse('Please submit a search term.')
	#message = 'You submitted an empty form.'
	#return HttpResponse(massage)



