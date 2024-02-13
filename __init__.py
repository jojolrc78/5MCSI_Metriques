from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
import requests
                                                                                                                                       
app = Flask(__name__) 

# Route pour extraire les minutes d'une date
@app.route('/extract-minutes/<date_string>')
def extract_minutes(date_string):
    date_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
    minutes = date_object.minute
    return jsonify({'minutes': minutes})

# Route pour extraire et afficher les commits par minute
@app.route('/commits/')
def commits():
    url = 'https://api.github.com/repos/OpenRSI/5MCSI_Metriques/commits'
    response = requests.get(url)
    commits_data = response.json()
    
    # Initialisation du dictionnaire pour stocker le nombre de commits par minute
    commits_per_minute = {}
    
    # Parcourir les commits et compter le nombre de commits par minute
    for commit in commits_data:
        date_string = commit['commit']['author']['date']
        minutes = extract_minutes(date_string).json['minutes']
        if minutes in commits_per_minute:
            commits_per_minute[minutes] += 1
        else:
            commits_per_minute[minutes] = 1
    
    # Préparer les données pour le graphique
    minutes = list(commits_per_minute.keys())
    commit_counts = list(commits_per_minute.values())
    
    return jsonify({'minutes': minutes, 'commit_counts': commit_counts})

# Route pour extraire les minutes d'une date
@app.route('/extract-minutes/<date_string>')
def extract_minutes(date_string):
    date_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
    minutes = date_object.minute
    return jsonify({'minutes': minutes})

# Route pour extraire et afficher les commits par minute
@app.route('/commits/')
def commits():
    url = 'https://api.github.com/repos/OpenRSI/5MCSI_Metriques/commits'
    response = requests.get(url)
    commits_data = response.json()
    
    # Initialisation du dictionnaire pour stocker le nombre de commits par minute
    commits_per_minute = {}
    
    # Parcourir les commits et compter le nombre de commits par minute
    for commit in commits_data:
        date_string = commit['commit']['author']['date']
        minutes = extract_minutes(date_string).json['minutes']
        if minutes in commits_per_minute:
            commits_per_minute[minutes] += 1
        else:
            commits_per_minute[minutes] = 1
    
    # Préparer les données pour le graphique
    minutes = list(commits_per_minute.keys())
    commit_counts = list(commits_per_minute.values())
    
    return jsonify({'minutes': minutes, 'commit_counts': commit_counts})
  
@app.route("/contact/")
def Utilisateur():
    return render_template("contact.html")
  
@app.route("/histogramme/")
def monhistogramme():
    return render_template("histogramme.html")
  
@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")
  
@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)
  
#@app.route("/contact/")
#def MaPremiereAPI():
    #return "<h2>Ma page de contact</h2>"

@app.route('/')
def hello_world():
    return render_template('hello.html') #Comm2
  
if __name__ == "__main__":
  app.run(debug=True)
