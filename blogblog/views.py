from django.shortcuts import redirect,render
from django.http import HttpResponse
from blogblog.models import Item

#def tweet(request):
#	if request.method =='POST':
#		newItem = request.POST['Content']
#		Item.objects.create(text=request.POST['Content'])
#		return redirect('/')
#	else:
#		newItem=''
#	return render (request, 'tweet.html')
	
def tweet(request):
	if request.method =='POST':
		Item.objects.create(text=request.POST['Content'])
		return redirect('/blogblog/viewlist_url')
	items = Item.objects.all()
	return render (request, 'tweet.html', {'Content':items})
	
def ViewList(request):
	items = Item.objects.all()
	return render (request, 'tweet.html', {'Content':items})
