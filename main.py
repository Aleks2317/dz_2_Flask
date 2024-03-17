from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)
app.secret_key = 'bf191431d1674c63ca34d0ebfa45a7a4551bd5ad7f224dbf14d910bf4c631ed9'


@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('answer_user'))
    return redirect(url_for('answer_user'))


@app.route('/answer_user/', methods=['GET', 'POST'])
def answer_user():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        name = request.form.get('name') or 'Anonymous'
        context = {
            'title': 'HI_USER!',
            'name': name,
        }
        return render_template('hi_user.html', **context)
    return render_template('answer_user.html', **({'title': 'answer_user'}))


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
