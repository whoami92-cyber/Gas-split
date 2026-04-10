from flask import Flask, render_template
import os
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/robots.txt')
def robots():
    return "User-agent: *\nAllow: /", 200, {'Content-Type: text/plain'}
if __name__=='__main__':
    port=int(os.onviron.get("PORT", 1000))
    app.run(host='0.0.0.0', port=port)


