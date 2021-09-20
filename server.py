from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key="@@lockdown"

@app.route('/')
def login():
    return render_template('dojoSurvey.html')

@app.route('/info', methods=["POST"])
def complete():
    session['name'] = request.form['name']
    session['Language'] = request.form['Language']
    session['location'] = request.form['location']
    session['comments'] = request.form['comments']
    print(request.form)
    return redirect('/result')


@app.route('/result')
def display():
    return render_template('result.html')
if __name__=='__main__':
    app.run(debug=True)