from flask import redirect, render_template, Flask, request, url_for



menu_dict = [
    {'title':'Главная','link':'index'},
    {'title':'О нас','link':'about'},
    {'title':'Форма','link':'form'},
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



@app.route('/menu')
def menu():
    return render_template('menu.html')



@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        name=request.form['name']
        message = request.form['message']
        return redirect (url_for('feedback', code=307, name=name, message=message))
    
    return render_template('form.html', title='Обратная связь', menu=menu_dict)


@app.route('/feedback', methods=['GET','POST'])
def feedback():
    if request.method == 'POST':
        name=request.form['name']
        message = request.form['message']        
    else:
        name = request.args.get('name')
        message = request.args.get('message')
    
    return render_template('abracadabra.html', name=name, text=message, menu=menu_dict, title='Ответ от формы')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)