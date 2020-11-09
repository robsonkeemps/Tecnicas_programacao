from flask import Flask, render_template, request, redirect, url_for, jsonify
import core
import validacao
import json

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/getData', methods=['GET','POST'])
def getData():
    if request.method == "POST":
        pergunta = request.form.get("pergunta")
        return json.dumps(validacao.similar(pergunta), ensure_ascii=False)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=8080, debug=True)