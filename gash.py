from flask import Flask, request, render_template

app=Flask(__name__)
@app.route('/')
    return render_template('index.html')
@app.route('/robots.txt')
def robots():
    return "User-agent: *\n Allow: /", 200, {'Content-Type: text/plain'}
if __name__=='__main__':
    app.run()


