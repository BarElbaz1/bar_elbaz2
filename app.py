from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/home')
@app.route('/home_page')
@app.route('/')
def hello_func():
    return render_template('index.html', name='Bar', secondName='Elbaz')

@app.route('/ABOUT') #this is another page
def about_func():
    # TODO
    # do something with db
    print('Hi you')
    return render_template('ABOUT.html',
                           uni='BGU',
                           profile={'name': 'Bae',
                                    'lastName': 'Elbaz'},
                           degrees=['BSc', 'MSc'],
                           hobbies=('dancing', 'art', 'reading'))

@app.route('/base')
def base_func():
    return render_template('base.html')




@app.route('/menu')
def menu_func():
    return render_template('/')

@app.route('/catalog')
def catalog_func():
    return render_template('catalog.html', name='Bar', secondName='Elbaz')


@app.route('/home')
def ex7_func():
    return redirect('/')

def hello_world():
    return 'hello ex7'

@app.route('/base')
def hello():
    return redirect(url_for('hello_world'))


if __name__ == '__main__' :
    app.run(debug=True)

