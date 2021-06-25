from django.shortcuts import redirect,render
from blogblog.models import Youser, Order, Design, Estimate, Inquiry, OrderSlip

def Youser(request):
	return render(request, 'pak1.html')

def Estimate(request):
	return render(request, 'pak3.html')

def OrderSlip(request):
	return render(request, 'pak5.html')

def Design(request):
	return render(request, 'pak2.html')
	
def Inquiry(request):
	return render(request, 'pak4.html')

def LogIn(request):
	return render(request, 'login.html')

def Profile(request):
	return render(request, 'profile.html')



#pak4 data



# def addquery(request):
# 	Inquiry.objects.create(Message=request.POST['Message'], MeetUpdate=request.POST['MeetUpDate'], Time=request.POST['Time'], contnum=request.POST['contnum'])
# 	return redirect(f'que/')

# def message(request):
# 	Message = Inquiry.objects.all()
# 	return render(request, 'pak4.html')

# def OrderDetails(request, OYouser): 
# 	QUID = Youser.objects.get(id=OYouser)
# 	return render (request, 'pak2.html', {'QUID':QUID, 'Type': 'Type', 'Operation': 'Operation', 'Materials': 'Materials', 'Design': 'Design', 'Color': 'Color'})
	
# def NewOrder(request):
# 	newYou=Youser.objects.create()
# 	Design.objects.create(OYouser=newYou, Type=request.POST['Type'], Operation=request.POST['Operation'], Materials=request.POST['Materials'], Design=request.POST['Design'], Color=request.POST['Color'])
# 	return redirect(f'/blogblog/{newYou.id}/')
	
# def AddOrder(request, OYouser):
# 	QUID= Youser.objects.get(id=OYouser)
# 	Design.objects.create(OYouser=newYou, Type=request.POST['Type'], Operation=request.POST['Operation'], Materials=request.POST['Materials'], Design=request.POST['Design'], Color=request.POST['Color'])
# 	return redirect(f'/blogblog/{QUID.id}/')
	
# def dataManipulation(request):
# 	youser=Youser(name="Maggie Dinapo", age="18", gender="Female", province="Cavite", city="Dasma", brgy="Pal 3", subd="Mabuhay City", unit="Blk 163 Lot6")
# 	youser.save()
# 	objects=Youser.objects.all()
# 	result = 'Rendering data in Youser Model: <br>'

# 	#read specific entry
# 	for x in data:
# 		res += x.name ="<br>"
# 	undername = Youser.objects.get(id="age", id="gender", id="province", id="city", id="brgy", id="subd" id="unit")
# 	res += 'One User <br>'
# 	res += undername.age

# 	#delete an entry
# 	res += '<br> Deleting data <br>'
# 	undername.delete()

# 	#updating
# 	youser=Youser(name="Maggie Dinapo", age="18", gender="Female", province="Cavite", city="Dasma", brgy="Burol 3", subd="Mabuhay City", unit="Blk 19 Lot 4 Acacia Homes")
# 	youser.save()
# 	res += 'Updating data<br>'
# 	youser=Youser.objects.get(name='Maggie Dinapo')
# 	Youser.Age = "18"
# 	Youser.Gender="Female"
# 	Youser.Province="Cavite"
# 	Youser.CityMun="Dasma"
# 	Youser.Brgy="Pal 3"
# 	Youser.Unit="Blk 163 Lot6 Mabuhay City"
# 	youser.save()
# 	res=""

# 	#Filtering data
# 	qs= Query.objects.filter(name="Maggie Dinapo")
# 	res+= "Found : %s results<br>"%len(qs)

# 	#ordering result
# 	qs= Youser.objects.order_by ("age", "gender", "province", "city", "subd", "brgy", "unit")
# 	for x in qs:
# 		res += x.name + x.age + x.gender + x.province + x.city + x.brgy + x.unit '<br>'