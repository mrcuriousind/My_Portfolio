from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)
    github_link = db.Column(db.String(200), nullable=True)
    live_link = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Project {self.title}>'

@app.route('/')
def home():
    projects = Project.query.all()
    return render_template('Home.html', projects=projects)

@app.route('/skills')
def skills():
    return render_template('Skill.html')

@app.route('/projects')
def projects():
    projects = Project.query.all()
    return render_template('Project.html', projects=projects)

@app.route('/blog')
def blog():
    return render_template('Blog.html')

@app.route('/contact')
def contact():
    return render_template('Contact.html')

@app.before_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Create tables before running the app
    app.run(debug=True)