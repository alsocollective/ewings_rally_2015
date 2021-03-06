from django.shortcuts import render, render_to_response, get_object_or_404
from easy_thumbnails.files import get_thumbnailer
from django.http import HttpResponse
from manager.models import *
from django.template import RequestContext

def home(request):

	query = Content.objects.all()
	content = query[0]
	slides = query[0].slides.all().order_by('order')
	map_locations = query[0].map_locations.all().order_by('order')
	sponsors = query[0].sponsors.all()

	return render_to_response('index.html',{"data":content,"slides":slides,"map_locations":map_locations,"sponsors":sponsors,"desktop":not request.is_mobile},context_instance = RequestContext(request))

