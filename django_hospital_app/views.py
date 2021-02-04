from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import appointments
from .forms import Appoform

def hello(request):
	 data=appointments.objects.all()
	 ad = {
	"appo": data
}
	 return render(request, 'appointments.html',ad)
def createappo(request):
	form = Appoform()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = Appoform(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")

	context = {'form':form}
	return render(request, 'createappo.html', context)

def updateappo(request, pk):

	appo = appointments.objects.get(id=pk)
	form = Appoform(instance=appo)

	if request.method == 'POST':
		form = Appoform(request.POST, instance=appo)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")

	context = {'form':form}
	return render(request, 'createappo.html', context)

def deleteappo(request, pk):
	appo = appointments.objects.get(id=pk)
	if request.method =="POST":
		appo.delete()
		return HttpResponseRedirect("/")

	return render(request, "delete.html")

# Create your views here.
