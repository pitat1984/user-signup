from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

def valid_input(text_input):
    
    if len(text_input) < 3 or len(text_input) > 20:
        return False
    elif " " in text_input:
        return False
    else:
        return True

def valid_userpass(text_input):

    if (not text_input) or (valid_input(text_input) == False):
        return False
    else:
        return True

def valid_email(text_input):
    at_count = 0
    dot_count = 0
    for char in text_input:
        if char is "@":
            at_count = at_count + 1
        if char is ".":
            dot_count = dot_count + 1

    if text_input is "":
        return True    
    elif (at_count == 1) and (dot_count == 1) and (valid_input(text_input) == True):
        return True
    else:
        return False    
    
def passwords_match(input_one, input_two):

    if (not input_two) or (input_one != input_two):
        return False
    else:
        return True




@app.route("/signup", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify-password']
    email = request.form['email']

    if valid_userpass(username) == False:
        username_error = "That's not a valid username"
    else:
        username_error = ""

    if valid_userpass(password) == False:
        password_error = "That's not a valid password"
    else:
        password_error = ""

    if passwords_match(password,verify_password) == False:
        match_error = "Passwords don't match"
    else:
        match_error = ""

    if valid_email(email) == False:
        email_error = "That's not a valid email"
    else:
        email_error = ""

    if (valid_userpass(username) == False) or (valid_userpass(password) == False) or (passwords_match(password,verify_password) == False) or (valid_email(email) == False):  
        return render_template('Index.html', username = username, email=email, username_error=username_error, password_error=password_error, match_error=match_error, email_error=email_error)
    
    return render_template('welcome.html', username=username)

@app.route("/")
def index():
    
    encoded_error = request.args.get("error")
    return render_template('index.html', error = encoded_error and cgi.escape(encoded_error, quote=True))

app.run()