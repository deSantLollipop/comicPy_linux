# comicPy_linux
Python script for simple image scraping.

only executable files
nr.txt - This file contains the comic index numbers that I would like to display on my "index.html" webpage. These numbers can be added or removed as needed.

app.py - This is the main file responsible for fetching the comic indexes from the "nr.txt" file, connecting to and retrieving the appropriate links from https://xkcd.com/, and populating the "images" list with these links. This list is passed as an argument in the render_template() function so that it can be accessed from the "index.html" file for further operations. It also runs a local host and displays the "index.html" page, which serves as the default homepage. The page contains images that can be viewed in their entirety by clicking the buttons below each image; clicking these buttons directly links to the original images.

base.html - This is the base HTML file, serving as a website template.

index.html - An extension of the "base.html" file, it succeeds it. It's a Python plugin that, in a loop, adds additional HTML elements with the "card" class to the page, along with the corresponding image links.

################ Linux Instructions ##################

The "index.html" and "base.html" files must be located within the "templates" directory.

I've tested it on Ubuntu, and it works there as well:

First, you need to have Python3 installed.

$ sudo apt install python3.8

$ sudo apt install python-pip

$ chmod a+x app.py

$ chmod a+x templates/index.html

$ chmod a+x templates/base.html

$ python3 -V
  outupt powinien byc :
  Python 3.8.5

$ sudo apt install python3-venv

w dyrektorii z naszymi plikami :

$ python3 -m venv venv

$ source venv/bin/activate

$ pip install Flask

$ python -m flask --version
  output powinien byc :
  Python 3.8.5
  Flask 1.1.2
  Werkzeug 1.0.1

$ export FLASK_APP=app.py

$ flask run
  output : 
  * Serving Flask app "hello.py"
  * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
  * Debug mode: off
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Odpalic strone http://127.0.0.1:5000/ w przegladarce.
