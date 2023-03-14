from flask import render_template, Flask, url_for



menu_dict = [
    {'title':'Главная','link':'index'},
    {'title':'О нас','link':'about'}
]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='HTML', menu=menu_dict)



@app.route('/about')
def about():
    return render_template('index.html', title='About us', menu=menu_dict)












if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)