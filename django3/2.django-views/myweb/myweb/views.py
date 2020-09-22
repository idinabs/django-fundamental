# meresponse file views

from django.http import HttpResponse

def index(request):
	return HttpResponse("SatuKode")