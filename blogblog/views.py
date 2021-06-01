from django.shortcuts import redirect,render
from blogblog.models import Item, Youser
	
def tweet(request):
	return render (request, 'tweet.html')
	
def ViewList(request, youId):
	yId = Youser.objects.get(id=youId)
	return render (request, 'tweet2.html', {'yId':yId, 'Feeling': 'Feeling', 'Codename': 'Codename','Description': 'Description'})
	
def NewList(request):
	newYou=Youser.objects.create()
	Item.objects.create(youId=newYou, text=request.POST['Content'], feelId=request.POST['Feeling'], codeId=request.POST['Codename'], descId=request.POST['Description'])
	return redirect(f'/blogblog/{newYou.id}/')
	
def AddList(request, youId):
	yId= Youser.objects.get(id=youId)
	Item.objects.create(youId=yId, text=request.POST['Content'], feelId=request.POST['Feeling'], codeId=request.POST['Codename'], descId=request.POST['Description'])
	return redirect(f'/blogblog/{yId.id}/')
	
