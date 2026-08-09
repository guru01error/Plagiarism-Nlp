from flask import Flask , render_template,request
from train import plagarism_check
app  = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    plagarism = None
    matches = []
    if request.method=="POST":
        text1= request.form['text1']
        text2 = request.form['text2']
        plagarism, matches = plagarism_check(text1,text2)
    return render_template(
        "index.html",
        plagarism=plagarism,
        matches=matches
    )
if __name__ == "__main__":
    app.run(debug=True)