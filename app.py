from flask import Flask
from flask import render_template
from flask import request
from math import factorial
import itertools as it


my_list=[]
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
    if request.method == 'POST' and request.form['action'] == "Calculate":
        try:
            #Start pulling data from form input
            n = request.form['n']
            k = request.form['k']
            operation = request.form['operation']

            if operation == 'combinations-with-repetitions':
                numerator = factorial(int(n) + int(k) - 1)
                denominator = factorial(int(k)) * factorial(int(n) - 1)
                sum = int(numerator) / int(denominator)
                for i in range(1, int(n)+1):
                    my_list.append(i)
                result = set(list(it.combinations(my_list, int(k))))


            elif operation == 'combinations-without-repetitions':
                numerator = factorial(int(n))
                denominator = factorial(int(k)) * factorial(int(n) - int(k))
                sum = int(numerator) / int(denominator)
                for i in range(1, int(n)+1):
                    my_list.append(i)
                result = set(list(it.combinations(my_list, int(k))))

            return render_template('app.html', sum=int(sum), combinations=result)
        except Exception as err:
            return render_template('app.html', sum=err)




if __name__ == ' __main__':
    app.debug = True
    app.run()
