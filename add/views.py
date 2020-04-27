from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
def hello(request):
	return render(request, 'main.html', {'name':'Abhilash'})
# Create your views here.
def add(request):
	n1 = int(request.POST['num1'])
	n2 = int(request.POST['num2'])
	op = request.POST['op']
	if op == '+':
		res = n1 + n2
	elif op == '-':
		res = n1 - n2
	elif op == '*':
		res = n1 * n2
	elif op == '/':
		res = n1 / n2

	else:
		return HttpResponse('Wrong operator')
	return render(request, 'result.html', {'result':res})

def back():
	return HttpResponseRedirect('add/')