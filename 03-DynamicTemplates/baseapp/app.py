from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    bookmarks = [
        {'id': 1, 'name': 'Job Board', 'addinfo': 'GetCFMLJobs Board Admin', 'link': 'getcfmljobs.com'},
        {'id': 2, 'name': 'Github Dash', 'addinfo': 'My Projects', 'link': 'github.com/Akbarsait'},
        {'id': 3, 'name': 'Vercel Dashboard', 'addinfo': 'Click to Launch', 'link': 'vercel.com'},
        {'id': 4, 'name': 'Manage Applets', 'addinfo': 'One place to Automate', 'link': 'ifttt.com'},
        {'id': 5, 'name': 'Atlassian Jira', 'addinfo': '', 'link': 'mycomp.atlassian.net'}
    ]
    return render_template('home.html', vbookmarks=bookmarks)

@app.route("/about")
def about():
    return render_template("about.html", title='About')

if __name__ == '__main__':
    app.run(debug=True)