from flask import Flask, render_template, request, redirect, url_for  # type: ignore

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check credentials (this is a simplified example)
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            # Redirect to main interface page upon successful login
            return redirect(url_for('main_interface'))
    # Render login page template if no valid credentials provided
    return render_template('main.html')

@app.route('/main')
def main_interface():
    # Render main interface page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
