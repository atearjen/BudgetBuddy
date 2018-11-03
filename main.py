from bmonth import bmonth
from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

test= bmonth()
@app.route('/save', methods=['POST'])
def formData():
    test.test()
    data= request.form
    print(data['fullname'])

    return '',200


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
