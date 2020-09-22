from django.shortcuts import render

def index(request):
	context = {
		'judul' : 'SatuKode',
		'subjudul' : 'Selamat Datang',
		'kontributor' : 'Petot',
		'nav' : [
			['/','Home'],
			['/blog', 'Blog'],
		]


	}
	return render(request, 'index.html', context)