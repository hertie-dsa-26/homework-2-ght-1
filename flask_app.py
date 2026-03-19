from flask import Flask, render_template, request

from helper import perform_calculation, convert_to_float

from circle import circle_class

app = Flask(__name__)  # create the instance of the flask class


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/calculate', methods=['GET', 'POST'])  # associating the GET and POST method with this route
def calculate():
    if request.method == 'POST':
        # using the request method from flask to request the values that were sent to the server through the POST method
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = str(request.form['operation'])

        try:
            value1 = convert_to_float(value=value1)
            value2 = convert_to_float(value=value2)
        except ValueError:
            return render_template('calculator.html', printed_result="Cannot perform operation with this input")

        try:
            result = perform_calculation(value1=value1, value2=value2, operation=operation)
            return render_template('calculator.html', printed_result=str(result))

        except ZeroDivisionError:
            return render_template('calculator.html', printed_result="You cannot divide by zero")

    return render_template('calculator.html')

@app.route('/circle', methods=['GET', 'POST'])
def circle():
    if request.method == 'POST':

        input = request.form['radius']
        operation = str(request.form['operation'])
        
        try:
            radius = convert_to_float(value = input)
        except ValueError:
            return render_template('circle.html', printed_result="Cannot perform operation with this input.")
        
        if radius <= 0 :
            return render_template('circle.html',
                                   printed_result='Radius must be greater than zero.')
        else:
            final_circle = circle_class(radius)
        
        if operation == 'area':
            result = final_circle.area()
            return render_template('circle.html', printed_result=str(result))
        else:
            result = final_circle.perimeter()
            return render_template('circle.html', printed_result=str(result))
        
    return render_template('circle.html')
        
        