from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/greeet', methods=['POST'])
def greet():
    name = request.form.get('name')
    return render_template('greeat.html',name = name)
if __name__ == '__main__':
   app.run(debug=True)


