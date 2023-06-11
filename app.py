# from flask import Flask, request, url_for, redirect, render_template, session
# import pickle
# import numpy as np

# app = Flask(__name__)
# # you can set any secret key but remember it should be secret
# app.secret_key = 'ItShouldBeAnythingButSecret'

# # step – 3 (creating a dictionary to store information about users)
# user = {"username": "abcd", "password": "kri"}
# #model = pickle.load(open('model.pkl', 'rb'))


# @app.route('/dashboard')
# def dashboard():
#     if('user' in session and session['user'] == user['username']):
#         return render_template("homepage.html")
#     return '<h1>You are not logged in.</h1>'  # if the user is not in the session


# # @app.route('/login', methods=['POST', 'GET'])
# # def login():
# #     print("djrqwtff", request, request.method, request.form[0])
# #     if(request.method == 'GET'):
# #         print("trying herw", request.form)
# #         username = request.form.get('username')
# #         password = request.form.get('password')
# #         print(username, password)
# #         if username == user['username'] and password == user['password']:

# #             session['user'] = username
# #             print("yesss")
# #             return redirect('/dashboard')

# #         else:
# #             return render_template("login.html")
# #     return render_template("login.html")

# @app.route('/login', methods = ['POST', 'GET'])
# def login():
#     if(request.method == 'POST'):
#         username = request.form.get('username')
#         password = request.form.get('password')
#         if username == user['username'] and password == user['password']:

#             session['user'] = username
#             return redirect('/dashboard')

#         return "<h1>Wrong username or password</h1>"    #if the username or password does not matches

#     return render_template("login.html")
# @app.route('/logout')
# def logout():
#     # session.pop('user') help to remove the session from the browser
#     session.pop('user')
#     return redirect('/login')
# # @app.route('/predict',methods=['POST','GET'])
# # def predict():
# #     int_features=[int(x) for x in request.form.values()]
# #     final=[np.array(int_features)]
# #     print(int_features)
# #     print(final)
# #     prediction=model.predict_proba(final)
# #     output='{0:.{1}f}'.format(prediction[0][1], 2)

# #     if output>str(0.5):
# #         return render_template('forest_fire.html',pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output),bhai="kuch karna hain iska ab?")
# #     else:
# #         return render_template('forest_fire.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output),bhai="Your Forest is Safe for now")


# if __name__ == '__main__':
#     app.run(debug=True)
from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'


users = []
users.append(User(id=1, username='Krithikha', password='u19cs076'))
users.append(User(id=2, username='Mahitha', password='u19cs066'))
users.append(User(id=3, username='Sankirtana', password='u19cs068'))
users.append(User(id=4, username='Nandhini', password='u19cs078'))


app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'


@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))
        error = "invalid password"
        return redirect(url_for('login'))

    return render_template('login.html', error=error)


@app.route('/profile')
def profile():
    # if not g.user:
    #    return redirect(url_for('login'))
    return render_template('homepage.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
#     session.pop('user')
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
