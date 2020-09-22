from django.shortcuts import render

def index(request):
	context = {
		'judul' : 'SatuKode',
		'subjudul' : 'Selamat Datang',
		'kontributor' : 'hidden',
		'nav' : [
			['/','Home'],
			['/blog', 'Blog'],
		]


	}
	return render(request, 'blog/index.html',context)