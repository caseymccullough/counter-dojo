from flask import Flask, render_template, redirect, session
from flask.globals import request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def default():
   if "count" not in session:
      session['count'] = 0
   else:
      session['count'] += 1
   return render_template('index.html')

@app.route('/two')
def two_points():
   if "count" not in session:
      session['count'] = 0
   else:
      session['count'] += 2
      print("UP BY TWO!!")
   return render_template('index.html')

@app.route('/increment')
def increment ():
   print("post info: ")
   print(request.form)
   return redirect('/')

@app.route('/reset')
def reset():
   print ('starting new session')
   session.clear() #clears all keys
   return redirect('/')

if __name__ == "__main__":
   app.run(debug=True)

