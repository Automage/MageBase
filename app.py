from flask import Flask, render_template, redirect, url_for, request
from post import Post

app = Flask(__name__)

posts = [Post('What the world runs on.',
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
              """),
         Post('Blowin\' in the wind',
              'Bob Dylan',
              'Today',
              """
              Lorem ipsum dolor sit amet, est ex laudem similique interpretaris, aeque albucius euripidis has ad, 
              id lorem accusamus reformidans ius. Mundi alienum conceptam te nam, quodsi invidunt per ex. At est debet 
              qualisque mnesarchum, mei ne harum sententiae. Est discere sententiae inciderint no, sea ne saepe perpetua, 
              illum elitr usu ne. Viris oblique consulatu est te, ei mei modo dissentiunt efficiantur. Vero illud 
              adipiscing vel te, putant invidunt mea ne.
              """),
         Post('Blowin\' in the wind',
              'Bob Dylan',
              'Today',
              """
              Lorem ipsum dolor sit amet, est ex laudem similique interpretaris, aeque albucius euripidis has ad, 
              id lorem accusamus reformidans ius. Mundi alienum conceptam te nam, quodsi invidunt per ex. At est debet 
              qualisque mnesarchum, mei ne harum sententiae. Est discere sententiae inciderint no, sea ne saepe perpetua, 
              illum elitr usu ne. Viris oblique consulatu est te, ei mei modo dissentiunt efficiantur. Vero illud 
              adipiscing vel te, putant invidunt mea ne.
              """),
         Post('Blowin\' in the wind',
              'Bob Dylan',
              'Today',
              """
              Lorem ipsum dolor sit amet, est ex laudem similique interpretaris, aeque albucius euripidis has ad, 
              id lorem accusamus reformidans ius. Mundi alienum conceptam te nam, quodsi invidunt per ex. At est debet 
              qualisque mnesarchum, mei ne harum sententiae. Est discere sententiae inciderint no, sea ne saepe perpetua, 
              illum elitr usu ne. Viris oblique consulatu est te, ei mei modo dissentiunt efficiantur. Vero illud 
              adipiscing vel te, putant invidunt mea ne.
              """)
         ]


@app.route('/')
def root_reroute():
    return redirect(url_for('home'));


@app.route('/home', methods=['GET', 'POST'])
def home():
    print(request)
    if request.method == 'POST':
        return "Title: " + request.form['title'] + "\nAuthor: " + request.form['author'] + "\nBody:\n" + request.form[
            'body']
    return render_template('home.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
