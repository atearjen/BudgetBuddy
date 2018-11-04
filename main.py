from bmonth import bmonth
from bmonth import *
from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

test= bmonth()


@app.route('/save', methods=['POST'])
def formData():
    data= request.form
    fullname=data['fullname']
    budget=data['amount-budget']
    sDate=data['date']
    eDate=data['duration']

    sDate=sDate.split('-')
    eDate=eDate.split('-')

    test.saveVar(int(sDate[1]),int(sDate[2]),int(sDate[0]),int(eDate[1]),int(eDate[2]),int(eDate[0]),int(budget),fullname)

    return '',200

#leftover total
@app.route('/total', methods=['GET'])
def leftTot():
	return test.getBudgetTotal()-test.totalSpent(),200

#leftover food
@app.route('/food', methods=['GET'])
def leftFood():
	spentFood=test.subMoney()

	return (((0.3)*test.getBudgetTotal())-spentFood[1]),200


#leftover rnt
@app.route('/rent', methods=['GET'])
def leftRent():
	spentRent=test.subMoney()

	return (((0.4)*test.getBudgetTotal())-spentRent[2]),200

#leftover entertainment
@app.route('/entertainment', methods=['GET'])
def leftEnter():
	spentEnter=test.subMoney()

	return (((0.3)*test.getBudgetTotal())-spentEnter[0]),200


#from bmonth import bmonth


#test = bmonth()

#numDays=test.init(1,1,2018,2,1,2018,1500)
#budgPerDay=test.getBudget(1500,numDays)

#print(numDays)
#print(budgPerDay)

#test.saveVar(1,1,2018,2,1,2018,1500)
#print(test.getDays())
#print(test.getBudget())

#print test.entertainment(.15)

#####################################################################################
