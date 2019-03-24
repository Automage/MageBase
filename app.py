from flask import Flask, render_template, redirect, url_for
from user import User

app = Flask(__name__)

users = [User('Pranav'), User('Man')]

users[0].addPost('What the world runs on.',
                 """
                 It's simple. Love. Love is what we run on, all of us.<br/>Whether you know it or not.
                 """)

users[0].addPost('Dance!',
                 """
                 Follow the rhythm and don't stop. Let the music guide you, sit back and watch your body sway
                 to the vibrations of life.
                 """)

users[1].addPost('How to live?',
                 """
                 Love <strong>everyone</strong> around you. Be yourself, and never let anyone tell you otherwise.   
                 """)


@app.route('/')
def root_reroute():
    return redirect(url_for('home'));


@app.route('/home')
def home():
    return render_template('home.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
