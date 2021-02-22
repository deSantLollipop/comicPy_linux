"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
######################
import urllib.request, json 

beg = 'https://xkcd.com/'
end = '/info.0.json'
images = []

with open('nr.txt') as f:
    numbs = f.read().splitlines()

for num in numbs:
    URL = beg + num + end
    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())
        images.append(data['img'])

###########################

from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)
# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def home():
    return render_template('index.html', images=images)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)




