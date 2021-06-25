from django.db import models

class Youser(models.Model):
	name=models.TextField (default="")
	password=models.TextField (default="")
	repeat=models.TextField (default="")
	age=models.TextField (default="")
	address=models.TextField (default="")
	email=models.TextField (default="")

	def _string_(self):
		return self.name

	class meta:
		db_table="UsersInfo"

class Design(models.Model):
	DYouser=models.ForeignKey (Youser, default=None, on_delete=models.CASCADE)
	TChoices=(
		('Horizontal Window Blinds', 'Horizontal Window Blinds'),
		('Vertical Window Blinds', 'Vertical Window Blinds'),
		)
	OChoices=(
		('Manual', 'Manual'),
		('Automatic', 'Automatic'),
		)
	MChoices=(
		('Plastic', 'Plastic'),
		('Wood', 'Wood'),
		('Fabric', 'Fabric'),
		)
	DChoices=(
		('Trilogy Combi Shades', 'Trilogy Combi Shades'),
		('Natural Color', 'Natural Color'),
		('BlockOut(Monotone)', 'BlockOut(Monotone)'),
		('BlockOut(SeeThruCombi)', 'BlockOut(SeeThruCombi)'),
		)
	Type=models.TextField (default="", null=True, choices=TChoices)
	Operation=models.TextField (default="", null=True, choices=OChoices)
	Materials=models.TextField (default="", null=True, choices=MChoices)
	Design=models.TextField (default="", null=True, choices=DChoices)
	Color=models.TextField (default="")

	class meta:
		db_table="Design"	

class Order(models.Model):
	orderdate=models.DateTimeField(auto_now_add=True, null=True)
	deliverydate=models.DateTimeField(auto_now_add=True, null=True)
	status=models.TextField (default="", null=True)
	class meta:
		db_table="Order"

class Estimate(models.Model):
	EYouser=models.ForeignKey (Youser, default=None, on_delete=models.CASCADE)
	SChoices=(
		('Cm', 'Cm'),
		('Inches', 'Inches'),
		('Foot', 'Foot'),
		('Meter', 'Meter'),
		('Yard', 'Yard'),
		('Millimeter', 'Millimeter'),
		)
	mySelect=models.TextField (default="", null=True, choices=SChoices)
	height=models.IntegerField (default="")
	width=models.IntegerField (default="")
	result1=models.IntegerField (default="")
	result2=models.IntegerField (default="")
	size=models.IntegerField (default="")
	lowestAmount=models.IntegerField (default="")
	highestAmount=models.IntegerField (default="")
	class meta:
		db_table="EstCost"

class Inquiry(models.Model):
	IYouser=models.ForeignKey (Youser, default=None, on_delete=models.CASCADE)
	Message=models.TextField (default="")
	MeetUpDate=models.DateTimeField(auto_now_add=True, null=True)
	Time=models.TextField (default="")
	contnum=models.TextField (default="")
	class meta:
		db_table="UserRequest"

class OrderSlip(models.Model):
	CYouser=models.ForeignKey(Youser, default=None, on_delete=models.CASCADE)
	COrder=models.ForeignKey (Order, default=None, on_delete=models.CASCADE)
	CDesign=models.ForeignKey (Design, default=None, on_delete=models.CASCADE)
	CInquiry=models.ForeignKey (Inquiry, default=None, on_delete=models.CASCADE)
	class meta:
		db_table="Ticket"
# Create your models here.
