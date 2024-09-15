from django.shortcuts import render

def index(reguest):
	return render(reguest,'index.html')
	
def about(request):
	return render(request,'about.html')
	
def contact(request):
	return render(request,'contact.html')

def analyze(request):
	djtext = request.GET.get('text','default')
	removepunc = request.GET.get('removepunc','off')
	uppercase = request.GET.get('uppercase','off')
	newlineremover = request.GET.get('newlineremover','off')
	ex = request.GET.get('ex','off')
	
	punc='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
	
	if removepunc=='on':
		w=""
		for char in djtext:
			if char not in punc:
				w=w+char
		djtext=w
		
	if uppercase=='on' :
		w=""
		for char in djtext:
			w=w+char.upper()
		djtext=w

	if newlineremover=='on':
		w=""
		for char in djtext:
			if char !="\n" and char !='\r':
				w=w+char
		djtext=w
		
	if ex=='on':
		w=djtext.replace("  ","")
					
	djtext=w
	if removepunc !='on' and uppercase !='on' and newlineremover != 'on' and ex !='on':
		return render(request,'index.html')
	
	else:
		return render(request,'analyzed.html',{'after':djtext})
		
		
		
	