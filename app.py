from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex']

    # Perform regex matching
    matches = re.findall(regex_pattern, test_string)
    
    return render_template('index.html', test_string=test_string, regex=regex_pattern, matches=matches)
@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    is_valid = re.match(email_pattern, email) is not None
    
    return render_template('index.html', email=email, is_valid=is_valid)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

