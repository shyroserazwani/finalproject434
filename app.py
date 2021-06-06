from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from twitter import fetch_twitter
from google_nlp import nlp_analysis
from wordcloud_generator import generate_wordcloud
from google.oauth2 import service_account
import google.auth
import pandas as pd

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Shyrose', password='jiggymerapiggy'))
users.append(User(id=2, username='Becca', password='secret'))
users.append(User(id=3, username='Carlos', password='somethingsimple'))


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
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('profile.html')

@app.route('/')
def home():
    if not 'user' in session:
        return redirect(url_for('login'))
    else:
        return render_template('profile.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    g.user = None
    # flash('Successfully logged out.')
    return redirect(url_for('home'))






@app.route('/chik')
def chik():
    twitter_result=fetch_twitter("amc","2021-6-1",200)
    credentials, your_project_id = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
    nlp_result=nlp_analysis(credentials=credentials, project='shyrose125-finalproject434',paragraph_text=twitter_result)
    #nlp_result_df=pd.DataFrame({"Name":nlp_result['entity_name'],"Salience":nlp_result['entity_salience']})
    wordcloud_figure=generate_wordcloud(nlp_result)
      
    #return render_template('home.html',nlp_result=nlp_result)
    return nlp_result

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8080, debug=False)
 

