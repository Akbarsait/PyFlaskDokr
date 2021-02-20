from flask import Flask, render_template, url_for, redirect, flash
from baseapp.forms import BookmarkForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '9791628bb0b19ce0c676dfde280ba243'

@app.route("/")
@app.route("/home")
def home():
    bookmarks = [
        {'id': 1, 'name': 'Job Board', 'addinfo': 'GetCFMLJobs Board Admin', 'link': 'getcfmljobs.com'},
        {'id': 2, 'name': 'Github Dash', 'addinfo': 'My Projects', 'link': 'github.com/Akbarsait'},
        {'id': 3, 'name': 'Vercel Dashboard', 'addinfo': 'Click to Launch', 'link': 'vercel.com'},
        {'id': 4, 'name': 'Manage Applets', 'addinfo': 'One place to Automate', 'link': 'ifttt.com'},
        {'id': 5, 'name': 'Atlassian Jira', 'addinfo': '', 'link': 'mycomp.atlassian.net'},
        {'id': 6, 'name': 'Amazon AWS', 'addinfo': 'One place to Automate', 'link': 'aws.amazon.com'},
        {'id': 7, 'name': 'Digi Ocean', 'addinfo': '', 'link': 'digitalocean.com'}
    ]
    return render_template('home.html', vbookmarks=bookmarks)

@app.route("/about")
def about():
    return render_template("about.html", title='About')

@app.route("/addbookmark", methods=['GET' , 'POST'])
def addbookmark():
    form = BookmarkForm()
    if form.validate_on_submit():
        flash(f'Bookmark added for {form.title.data} - {form.description.data}')
        return redirect(url_for('home'))
    return render_template("addbookmark.html", title='Add Bookmark', form=form)

if __name__ == '__main__':
    app.run(debug=True)