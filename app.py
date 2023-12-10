from flask import Flask, render_template, redirect, url_for
import models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
models.init_db(app)

@app.route('/')
def index():
    from models import Comments
    comments = Comments.query.all()
    return render_template('index.html', comments=comments)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/comments/add/')
def add_comment():
    return render_template('add_comment.html')

@app.route("/submit_comment/", methods=["POST"])
def submit_comment():
    from models import Comments
    from flask import request
    print(request.form)
    author = request.form["author"]
    comment = request.form["comment"]
    comment = Comments(author=author, comment=comment)
    models.db.session.add(comment)
    models.db.session.commit()
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()


