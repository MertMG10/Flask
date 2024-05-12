from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/Mert")
def gerçek():
    x= ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
    "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir."]
    return f"<h2>{random.choice(x)}<h2>"

@app.route("/Sayfa2")
def yt(Sayfa2):
    y=["Yazı","Tura"]
    a=random.choice(y)
    if a == Sayfa2:
        return "<p>Bildiniz Tebrikler </p>"
    else:
        return f"<p>Bilemediniz Cevap {a} </p>"






@app.route("/<x>/<y>")
def toplama(x,y):
    toplam= int(x)+ int (y)
    return f"<p>{toplam}</p>"





app.run(debug=True)



