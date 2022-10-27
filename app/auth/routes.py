from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/test')
def login_page2():
    return render_template('test.html')