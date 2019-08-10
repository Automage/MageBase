import os
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request
from flask_mail import Mail, Message
from post import Post
from db_handler import DatabaseHandler

app = Flask(__name__)

# Flask-mail config
# MAIL_USERNAME, MAIL_PASSWORD, MAIL_DEFAULT_SENDER should be set as environ variables
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = 1
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')

mail = Mail(app)

poster = [Post('What the world runs on.',
               'Pranav',
               'Yesterday',
               """
               It's simple. Love. Love is what we run on, all of us.<br/>Whether you know it or not.
               """),
          Post('Dance!',
               'Manasi',
               'Today',
               """
               Follow the rhythm and don't stop. Let the music guide you, sit back and watch your body sway to the vibrations of life.
               """)
          ]


@app.route('/')
def root_reroute():
    return redirect(url_for('home'));


@app.route('/home', methods=['GET', 'POST'])
def home():
    db = DatabaseHandler('guestbook.db')
    # POST: Guestbook form
    if request.method == 'POST':
        timestamp = datetime.now()
        post = Post(request.form['title'].strip(), request.form['author'].strip(), timestamp,
                    request.form['body'].strip())
        db.add_post(post)
        send_email(post)
        return redirect(url_for('home'))

    # GET:
    posts = db.get_posts()
    return render_template('home.html', posts=posts)


def send_email(post):
    # Sender configured in MAIL_DEFAULT_SENDER environ variable
    msg = Message(subject='Guestbook signed!', recipients=['pranav92000@gmail.com'])
    msg.body = f"""The following was posted on MageBase on {post.date}:
    
    Title: {post.title}
    Author: {post.author}
    
    {post.body}
    """
    mail.send(msg)


if __name__ == '__main__':
    app.run(debug=True)
