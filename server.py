from flask import Flask, render_template, session, redirect
app= Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template('index.html', count=session['count'])

@app.route('/destroy_session')
def destroy_session():
    session['count'] = 0
    return redirect('/')

@app.route('/increase_2', methods=['POST'])
def increase_2():
    session['count'] +=1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)