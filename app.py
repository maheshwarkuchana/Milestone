from flask import Flask, render_template, redirect, url_for, request
from flaskext.mysql import MySQL
import pandas as pd

app = Flask(__name__)

def decode_selected_event(selected_event):
    if selected_event == "1":
        return "Fine Arts Marathon"
    elif selected_event == "2":
        return "online photography contest"
    elif selected_event == "3":
        return "master chef'19"
    elif selected_event == "4":
        return "hackbmu"
    elif selected_event == "5":
        return "sci-ex exhibit"
    elif selected_event == "6":
        return "encrypt"
    elif selected_event == "7":
         return "halls of summer"
    elif selected_event == "8":
         return "inquizitive"
    elif selected_event == "9":
         return "slam poetry"
    elif selected_event == "10":
         return "battle of bands"
    elif selected_event == "11":
         return "beat the street"
    elif selected_event == '12':
         return "rihaai - nukkad"
    elif selected_event == '13':
         return "unplugged"
    elif selected_event == '14':
         return "bailar"
    elif selected_event == '15':
         return "rc nitro"
    elif selected_event == '16':
         return "line follower"
    elif selected_event == '17':
         return "aerial drones"
    elif selected_event == '18':
         return "robo race"
    elif selected_event == '19':    
         return "robo soccer"
    elif selected_event == '20':
         return "robo war"
    elif selected_event == '21':
         return "theatre phantamonica"
    elif selected_event == '22':
         return "war of djs"
    elif selected_event == '23':
         return "spic macay"
    elif selected_event == '24':
         return "fashion crave"
    else:
         return "model united nations"                           

@app.route('/')
def home():
    return render_template('homePage.html')

@app.route('/homePage.html')
def index():
    return render_template('homepPage.html')

@app.route('/events.html')
def courses():
    return render_template('events.html')

@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    
    user_database = pd.read_csv("users.csv", index_col=0)
    if request.method == 'POST':
        name = request.form['username']
        university = request.form['university']
        email = request.form['email']
        selected_event = request.form['selected']
        event = decode_selected_event(selected_event)
        print(name, university, email, event)
        count = user_database['name'].count()
        user_database.loc[count+1] = [name, university,email, event]
        user_database.to_csv("users.csv", header=True)

        return render_template('events.html')

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(host="10.7.6.85", port=5000)
    app.debug = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True

