import datetime

from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.

# offer classes
class Offer(models.Model):
	CURRENTJOB = 'CJ'
	NEWJOB = 'NJ'

	OFFER_CHOICES = (
		(CURRENTJOB, 'Current Job'),
		(NEWJOB, 'New Job'),
	)

	offertype = models.CharField(max_length=2, choices=OFFER_CHOICES, default=NEWJOB)
	companyname = models.CharField('company name', null=True, blank=True, max_length=100)
	positionname = models.CharField('position name', null=True, blank=True, max_length=100)
	locationzip = models.IntegerField(default=0,null=True, blank=True)
	startdate = models.DateField('start date')
	annualbase = models.IntegerField()
	salarygrowth = models.FloatField(default=.15)
	annualbonus = models.FloatField(default=.10)
	signingbonus = models.IntegerField(default=0,null=True, blank=True)
	tuitionbonus = models.IntegerField(default=0, null=True, blank=True)
	stockbonus = models.IntegerField(default=0, null=True, blank=True)
	stockgrowth = models.FloatField(default=.10, null=True, blank=True)
	discountrate = models.FloatField(default=.08)
class Other(models.Model):
	offer = models.ForeignKey(Offer)
	otherbonus = models.IntegerField(default=0, null=True, blank=True)
	bonusdate = models.DateField('other bonus date', null=True, blank=True)

class Vest(models.Model):
	offer = models.ForeignKey(Offer)
	vestingamount = models.IntegerField(default=0, null=True, blank=True)
	vestingdate = models.DateField('vest date', null=True, blank=True)

class OfferForm(ModelForm):
	class Meta:
		model = Offer
		fields = ['offertype', 'companyname', 'positionname']
		


# person classes
# class Visitor(models.Model):
# 	age = models.IntegerField(default=0,null=True, blank=True)
# 	sex = models.IntegerField(default=0,null=True, blank=True)

# class Student(Visitor):
# 	UNDERGRAD = 'UG'
# 	GRADUATE = 'GR'
# 	PHD = 'PD'
# 	EDUCATION_LEVEL = (
# 		(UNDERGRAD, 'Undergraduate Degree'),
# 		(GRADUATE, 'Masters Degree'),
# 		(PHD, 'Doctors Degree'),
# 	)
# 	edlevel = models.CharField(max_length=2, choices=EDUCATION_LEVEL, default=GRADUATE)