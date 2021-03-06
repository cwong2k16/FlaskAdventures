from flask import render_template, flash, redirect, url_for, request, make_response
from app import app
from app.forms import SubmissionForm
from app.models import Post


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SubmissionForm()
    if request.method=='POST':
        selectedValue = request.form.get('operator')
        new_num1 = request.form['number']
        new_num2 = request.form['number2']
        if form.validate()== False:
            return redirect(url_for('result', selectedValue="error"))
        else:
            response = make_response(redirect(url_for('result', selectedValue=selectedValue)))
            response.set_cookie('num1', new_num1)
            response.set_cookie('num2', new_num2)
            return response

    elif request.method=='GET':
        return render_template('index.html', title='Home', form=form)
    
@app.route('/result/<selectedValue>')
def result(selectedValue):
    if selectedValue == "error":
        return render_template('error.html', title='Result', result="You have an error with your input!")
    num1=float(request.cookies.get('num1'))
    num2=float(request.cookies.get('num2'))

    if selectedValue == 'subtract':
        result=num1-num2
    elif selectedValue == 'multiply':
        result=num1*num2
    elif selectedValue == 'add':
        result=num1+num2
    else:
        result=num1/num2
    
    if((str(result))[-2:] == '.0'):
        result = str(result)
        result=result[:-2]

    return render_template('success.html', title='Result', result=result)

@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server(error):
    return render_template('500.html'), 500
