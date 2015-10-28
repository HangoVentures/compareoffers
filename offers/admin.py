from django.contrib import admin
from .models import Offer, Other, Vest
# Register your models here.

class ChoiceInline1(admin.TabularInline):
	model = Other
	extra = 1

class ChoiceInline2(admin.TabularInline):
	model = Vest
	extra = 1

class OfferAdmin(admin.ModelAdmin):
	fieldsets = [
		('Offer Info', 			
		{'fields': ['offertype', 'companyname', 'locationzip','positionname','startdate']}),
		('Compensation Info',	
		{'fields': ['annualbase', 'annualbonus', 'signingbonus','stockbonus']}),
	]
	inlines = [ChoiceInline1, ChoiceInline2]

	list_display = ['offertype', 'annualbase', 'companyname']
	list_filter = ['annualbase']
	search_fields = ['companyname']

admin.site.register(Offer, OfferAdmin)