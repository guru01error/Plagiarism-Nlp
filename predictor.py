from flask import Flask , render_template,request
from train import plagarism_check
app  = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    plagarism = None
    matches = []
    if requfrom flask import Flask, render_template, request
from train import plagarism_check

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    plag_score = None
    matches = []

    if request.method == "POST":
        # Safe input extraction with fallback
        text1 = request.form.get('text1', '').strip()
        text2 = request.form.get('text2', '').strip()

        # Input validation check
        if text1 and text2:
            raw_score, matches = plagarism_check(text1, text2)
            
            # Formats score to 2 decimal places (e.g., 46.51)
            plag_score = round(float(raw_score), 2)
        else:
            # Empty input handling
            plag_score = 0.0
            matches = []

    return render_template(
        "index.html",
        plagarism=plag_score,
        matches=matches
    )

if __name__ == "__main__":
    app.run(debug=True)est.method=="POST":
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