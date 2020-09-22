from django.shortcuts import render

def index(request):
	context = {
		'judul' : 'SatuKode',
	}
	return render(request, 'index.html', context)