from flask import Flask, request, render_template

app=Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def caculator():
    f=None
    if request.method=='POST':
        b= float (request.form['travel'])
        c=float (request.form['cars'])
        e=float (request.form['gasprice'])
        g=float (request.form['p'])
        a=(b/100)*c
        d=a*e
        f=d/g
        f= round(f, 2)
    return render_template('index.html', total=f)
@app.route('/robots.txt')
def robots():
    return "user-agent: *\n Allow:/", 200, {'Content-Type: text/plain'}
    if __name__=='__main__':
        app.run(debug=True)


