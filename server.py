from flask import Flask, render_template, request, redirect, session, flash
from validation import formIsValid
app = Flask(__name__)
app.secret_key="secretsrunsdeep"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['post'])
def show_info():

    state = formIsValid(request.form)
    print state
    if (state['isValid']):
        return render_template('/result.html', name = request.form['name'],  dojo = request.form['dojo'], language = request.form['language'], comment = request.form['comment'])
    else:
        for error in state['errors']:
            flash(error)
        return redirect('/')



app.run(debug=True)
