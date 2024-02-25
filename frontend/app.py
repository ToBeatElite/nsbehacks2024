from flask import Flask, render_template
import json, requests

app = Flask(__name__)             

@app.route('/')
def home():
    posts = json.loads(requests.get('http://django-app:8000/posts/').text)
    cleaned_data = [{key: value for key, value in item.items() if key != 'id'} for item in posts]
    return render_template('index.html', data=cleaned_data)

@app.route('/events')
def events():
    events_api = requests.get('http://django-app:8000/events/').text
    jobs_api = requests.get('http://django-app:8000/jobs/').text
    events = json.loads(events_api)
    jobs = json.loads(jobs_api)
    return render_template('events.html', data=events, other_data=jobs)

@app.route('/create_post')
def create_post():
    return render_template('create_post.html')

if __name__ == "__main__":        
    app.run(host="0.0.0.0", port=5000, debug=True) # SECURITY WARNING   
