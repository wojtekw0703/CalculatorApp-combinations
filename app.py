from flask import Flask
from flask import render_template
from flask import request
from math import factorial

#Declaring the app
app = Flask(__name__)

#Start an app route
@app.route('/')

#Declaring main function
def main():
    return render_template('app.html')

#Form Submission Route
@app.route('/send', methods=['POST'])


def send(sum=sum):
    if request.method == 'POST':
        #Start pulling data from form input
        n = request.form['n']
        k = request.form['k']
        operation = request.form['operation']
        #Calculation
        if operation == 'combinations-with-repetitions':
            try:
                numerator = factorial(int(n) + int(k) - 1)
                denominator = factorial(int(k)) * factorial(int(n) - 1)
                sum = int(numerator) / int(denominator)
                return render_template('app.html', sum=int(sum))
            except:
                return render_template('app.html', sum="An error has been occurred")
        elif operation == 'combinations-without-repetitions':
            try:
                numerator = factorial(int(n))
                denominator = factorial(int(k)) * factorial(int(n) - int(k))
                sum = int(numerator) / int(denominator)
                return render_template('app.html', sum=int(sum))
            except:
                return render_template('app.html', sum="An error has been occurred")
        else:
            return render_template('app.html')




if __name__ == ' __main__':
    app.debug = True
    app.run()
