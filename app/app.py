from flask import Flask, render_template
from controllers import c_1

app = Flask(__name__)
app.register_blueprint(c_1.c)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)