# comicPy_linux
only executable files


nr.txt - plik z numerami indeksów komiksów które chciałbym zobaczyć na swojej stronie "index.html"; numery można dodawać i usuwać odpowiednio.

app.py - plik główny odpowiedzialny za pobieranie indeksów z pliku "nr.txt"; łączeniem i pobieraniem odpowiednich linków z https://xkcd.com/; dodawanie "images" - listy pobranych linków, jako argumentu w funkcji render_template() - aby miec do niej dostęp z pliku index.html, dla kolejnych operacji; odpalenie lokalnego hosta i strony "index.html", która jest domyślnie strona domowa. Na stronie znajdują się zdjęcia, które można zobaczyć w całości po odpowiednim kliknięciu przycisków pod zdjeciami - kliknicie przenosi bezpośrednio do oryginalnych linków każdego z obrazków.

base.html - bazowy html plik, szablon strony internetowej.

index.html - rozszerza plik "base.html", i jest go następcą. wtyczka z pythona: w pętli dodaje kolejne elementy html klasy "card" do strony z odpowiednimi linkami na zdjęcia.





################ Instrukcja dla linuksa ##################

Pliki "index.html" i "base.html" koniecznie musza znajdować sie pod katalogiem "templates".

Sprawdzilem na Ubuntu, też dziala : 

najperw musi byc zainstalowany python3;

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
