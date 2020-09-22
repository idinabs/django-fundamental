from django.shortcuts import render

def index(request):
	context = {
		'judul':'SatuKode',
		'kontributor' : 'fillateo'
	}
	return render(request, 'blog/index.html', context)

def news(request):
	context = {
		'judul':'SatuKode',
		'kontributor':'hidden'

	}
	return render(request, 'blog/index.html', context)

def cerita(request):
	context = {
		'judul':'SatuKode',
		'kontributor':'petot	'

	}
	return render(request, 'blog/index.html', context)