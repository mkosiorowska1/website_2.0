from flask import Flask, render_template, request, flash
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
app = Flask(__name__)

app.secret_key="a"

def wykres():
    img = io.BytesIO()
    l1 = request.form['a_input'] #dane z ramek do wprowadzania liczb
    l2 = request.form['b_input']

    a = float(l1)
    b = float(l2)
    p1 = str(l2+"x") #na potrzebę legendy (żeby podniosło dwie zmienne do potęgi)
    p2 = str(l1+"x")
    plt.style.use('seaborn-darkgrid')
    if a > 0: #jeśli a większe od 0, to:
        fig, ax = plt.subplots()
        x = np.linspace(0.001, 5, 100)
        y1 = a*np.exp(b*x) #funkcja wykładnicza
        y2 = b*np.log(a*x) #funkcja logarytmiczna
        ax.plot(x, y1)
        ax.plot(x, y2)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend((l1+f"$e^{{{p1}}}$", l2+f"$log_e{{{p2}}}$")) #sformatowana legenda
        idx = np.argwhere(np.diff(np.sign(y1 - y2))).flatten() #wyznaczenie punktów przecięcia
        ax.plot(x[idx], y1[idx], 'ro')
        plt.savefig(img, format='png')
        try: #jeśli punkty przecięcia istnieją, to pod wykresem pojawi się informacja z punktem, w którym się przecinają 
            point = "(" + str(round(x[idx][0], 3))+","+str(round(y1[idx][0], 3)) + ")"
            kom = "Funkcje przecinają się w punkcie " + point
        except: #jeśli punkty się nie przecinają, to pojawi się informacja, że się nie przecinają
            kom = "Funkcje nie przecinają się."
    elif a < 0: #jeśli a mniejsze od 0, to:
        fig, ax = plt.subplots()
        x = np.linspace(-5, -0.001, 100)
        y1 = a*np.exp(b*x)
        y2 = b*np.log(a*x)
        ax.plot(x, y1)
        ax.plot(x, y2)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend((l1+f"$e^{{{p1}}}$", l2+f"$log_e{{{p2}}}$"))
        idx = np.argwhere(np.diff(np.sign(y1 - y2))).flatten()
        ax.plot(x[idx], y1[idx], 'ro')
        plt.savefig(img, format='png')
        try:
            point = "(" + str(round(x[idx][0], 3))+","+str(round(y1[idx][0], 3)) + ")"
            kom = "Funkcje przecinają się w punkcie " + point
        except:
            kom = "Funkcje nie przecinają się."
    else:       #jeśli a równa 0, to:
        x1 = np.linspace(-2, 2, 100)
        y1 = a*np.exp(b*x1)
        plt.plot(x1,y1, color = "orange")
        plt.xlabel("x")
        plt.ylabel("0e")
        plt.savefig(img, format='png')
        kom = "Tutaj mamy tylko jeden wykres, więc z czym ma się przeciąć? ;)"
    img.seek(0)
    url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return ('data:image/png;base64,{}'.format(url), kom)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/glowna")
def glowna():
  
    return render_template("index.html")



@app.route("/autorzy")
def autorzy():

    return render_template("autorzy.html")   




