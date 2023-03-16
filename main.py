from flask import render_template, Flask, url_for



menu_dict = [
    {'title':'Главная','link':'index'},
    {'title':'О нас','link':'about'},
    {'title':'frame','link':'frame'}
]

app = Flask(__name__)


@app.template_filter('static_url')
def static_url_filter(file):
    return url_for('static', filename=file)



@app.route('/')
def index():
    return render_template('index.html', title='HTML', menu=menu_dict)



@app.route('/about')
def about():
    return render_template('about.html', title='About us', menu=menu_dict)


@app.route('/frame')
def frame():
    return render_template('frame.html', title='Frame', menu=menu_dict)









if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)