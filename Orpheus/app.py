from flask import Flask, render_template
import os
  
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/spotify')
def spotify():
    print("Spotify script called")
    # song="pretty when you cry"
    # name="lana del rey"
    # cmd =  f'python orpheus.py "{song}" "{name}"'
    # os.system(cmd)
    return ("nothing")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

