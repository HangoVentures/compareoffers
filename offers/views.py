from django.shortcuts import get_object_or_404, redirect, render
# from django.template import RequestContext, loader
import datetime

from django.utils import timezone
from .models import Offer
from .forms import Offerform

# Create your views here.
def index(request):
	latest_offers_list = Offer.objects.order_by('annualbase')
	context = {'latest_offers_list': latest_offers_list}
	return render(request, 'offers/templates/index.html', context)

def detail(request, offer_id):
	offer = get_object_or_404(Offer, pk=offer_id)
	return render(request, 'offers/templates/detail.html', {'offer':offer})

def newoffer(request):
	if request.method == "POST":
		form = Offerform(request.POST)
		if form.is_valid():
			# commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
			model_instance = form.save(commit=False)
			model_instance.timestamp = timezone.now()
			model_instance.save()
			return redirect('offers/templates/newoffer.html')
	else:
		form = Offerform()
	return render(request, 'offers/templates/newoffer.html', {'form':form})

def compare(request, offer_id):
	p = get_object_or_404(Offer, pk=offer_id)
	# return render(request, 'offers/templates/detail.html', {'form'}:form}
	# # try:
	# 	Offer.offertype=p.offertype.get(pk=request.POST['offertype'])
	# except(KeyError, offertype.DoesNotExist):
	# 	#redisplay the form
	# 	return render(request, 'offers/templates/details.html', {
	# 		'offertype':p, 'error_message=':"You didn't select a choice.",
	# 	})
	# else:
	# 	Offer.offertype = {{ choice }}