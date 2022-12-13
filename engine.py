from flask import Flask, flash, redirect, render_template, request, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/about/')
def about():
    return render_template('about.html')
    
@app.route('/accomodation/')
def accomodation():
    return render_template('accomodation.html')
    
@app.route('/gallery/')
def gallery():
    return render_template('gallery.html')
    

if __name__ == '__main__':
    app.run(debug=True)
  