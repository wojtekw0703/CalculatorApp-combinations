from flask import Flask
from flask import render_template
from flask import request

#Declaring the app
app = Flask(__name__)

#Start an app route
@app.route('/')

#Declaring main function
def main():
    return render_template('app.html')

#Form Submission Route
@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        #Start pulling data from form input
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']
        #Calculation
        if operation == 'combinations-with-repetitions':
            sum = 0
            return render_template('app.html', sum=sum)
        elif operation == 'combinations-with-repetitions':
            sum = 0
            return render_template('app.html', sum=sum)

