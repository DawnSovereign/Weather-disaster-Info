from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/tornado')
def tornado():
    return render_template("tornado.html")

@app.route('/handle_selection', methods=['POST'])
def handle_selection():
    selected_option = request.form.get('selected_option')

    if selected_option == 'tornado':
        return redirect(url_for('tornado'))

    return redirect(url_for('home'))  # Home page is redirected if no option is selected 

if __name__ == '__main__':
    app.run(debug=True)
