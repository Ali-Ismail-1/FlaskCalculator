from operator import truediv
from xml.dom import ValidationErr
from flask import Flask
from flask import render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    try:        
        return render_template('index.html')
    except Exception as e:
        print(e)        
        return render_template('error.html')    


@app.route('/calculator')
def calculator():
    try:
        return render_template('calculator.html')
    except Exception as e:
        print(e)
        return render_template('error.html')

@app.route('/solve', methods = ['GET'])
def solve():
    print("Begin Solving")
    
    try:

        # 1. Get Payload
        equationArray = request.args.getlist('equationArray[]')
        print(equationArray)

        # 2. Validate
        if (not help_validate(equationArray)):
            raise ValidationErr

        # 3. Get Answer
        answer = help_evaluate(equationArray)
        return jsonify({'Status': True, 'Answer' : answer})
        
    except ValidationErr:
        print('Validation Error')
        return jsonify({'Status': False, 'Answer' : '', 'Message' : 'Validation Error' })        
    except Exception as e:
        print('Other Error')
        return jsonify({'Status': False, 'Answer': '', 'Message': e })


def help_isfloatable(n):
    try:
        float(n)        
    except ValueError:
        return False
    return True

def help_validate(equationArray):

    # Cannot Calculate 
    if (len(equationArray) == 0):
        print('Error: Array Length Too Short')
        return False

    # If only one, Must be a number
    if (len(equationArray) == 1 and not help_isfloatable(equationArray[0])):
        return False

    # First and Last in array must be numeric
    if (len(equationArray) > 1 and (help_isfloatable(equationArray[0]) == False or help_isfloatable(equationArray[len(equationArray) - 1]) == False)):
        print('Error: Must Start and End Numeric')
        return False

    # Must be alternating operators and numbers
    prevNumeric = False
    for x in equationArray:
        if (help_isfloatable(x) == prevNumeric):
            return False
        prevNumeric = not prevNumeric

    return True

def help_evaluate(equationArray):

    equationString = ''
    for x in equationArray:
        equationString += x + ' '

    try:
        answer = eval(equationString)
        return answer
    except:
        raise ValueError("Unable to Evaluate Expression")


if __name__ == '__main__':
    app.run(debug=True)