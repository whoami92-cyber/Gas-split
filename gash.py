from flask import Flask, request, render_template

app=Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def caculator():
    f=None
    if request.method=='POST':
        b= float (request.form['travel'].replace(',', '.'))
        c=float (request.form['cars'].replace(',', '.'))
        e=float (request.form['gasprice'].replace(',', '.'))
        g=float (request.form['p'].replace(',', '.'))
        a=(b/100)*c
        d=a*e
        f=d/g
        f= round(f, 2)
    return render_template('index.html', total=f)
@app.route('/robots.txt')
def robots():
    return "User-agent: *\n Allow: /", 200, {'Content-Type: text/plain'}
if __name__=='__main__':
    app.run(debug=True)


