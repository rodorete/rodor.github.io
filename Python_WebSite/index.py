from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
        return render_template('home.html')
        
@app.route('/Imagenes')
def Imagenes():
    return render_template('Imagenes.html')

if __name__ == '__main__':
    app.run (debug=True)  