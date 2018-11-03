from datetime import date
import csv

class bmonth():
	
	def test(self):
		print('we made it')

	def saveVar(self, Smonth, Sday, Syear, Emonth, Eday, Eyear, budget, fullName, entertain, food, rentUtil):
		with open('data.csv', mode='w') as data:
			data_writer= csv.writer(data, delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)			
			csvRow=[Smonth,Sday,Syear,Emonth,Eday,Eyear,budget,fullName,entertain,food,rentUtil]
			data_writer.writerow(csvRow)

	def getDays(self):
		data=[]

		with open("data.csv") as csvfile:
   			reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
			for row in reader:
				data.append(row)

		data2=data[0]

		Smonth=int(data2[0])
		Sday=int(data2[1])
		Syear=int(data2[2])
		Emonth=int(data2[3])
		Eday=int(data2[4])
		Eyear=int(data2[5])
		Budget=data2[6]

		d0=date(Syear,Smonth,Sday)
		d1=date(Eyear,Emonth,Eday)

		delta = d1-d0

		days=delta.days

		return days


	def getBudgetDay(self):
		data=[]

		with open("data.csv") as csvfile:
   			reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
			for row in reader:
				data.append(row)

		data2=data[0]

		Smonth=int(data2[0])
		Sday=int(data2[1])
		Syear=int(data2[2])
		Emonth=int(data2[3])
		Eday=int(data2[4])
		Eyear=int(data2[5])
		budget=data2[6]


		return (float(budget)/self.getDays())


	def getBudgetTotal(self):
		data=[]

		with open("data.csv") as csvfile:
   			reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
			for row in reader:
				data.append(row)

		data2=data[0]

		Smonth=int(data2[0])
		Sday=int(data2[1])
		Syear=int(data2[2])
		Emonth=int(data2[3])
		Eday=int(data2[4])
		Eyear=int(data2[5])
		budget=data2[6]


		return (float(budget))


#####Categories

	def entertainment(self, percent):
		eBudg=self.getBudgetTotal()*percent

		return eBudg


	def food(self, percent):
		fBudg=self.getBudgetTotal()*percent

		return fBudg

	def rentUtil(self, percent):
		rBudg=self.getBudgetTotal()*percent

		return rBudg






