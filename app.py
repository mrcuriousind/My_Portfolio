from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'
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

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    published_date = db.Column(db.String(20), nullable=False)
    image_url = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<BlogPost {self.title}>'

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    video_url = db.Column(db.String(200), nullable=False)
    thumbnail_url = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Video {self.title}>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    avatar_url = db.Column(db.String(200), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    website = db.Column(db.String(200), nullable=True)
    github_username = db.Column(db.String(100), nullable=True)
    linkedin_username = db.Column(db.String(100), nullable=True)
    twitter_username = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/')
def home():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

@app.route('/skills')
def skills():
    return render_template('skill.html')

@app.route('/projects')
def projects():
    projects = Project.query.all()
    return render_template('project.html', projects=projects)

@app.route('/blog')
def blog():
    blog_posts = BlogPost.query.all()
    videos = Video.query.all()
    return render_template('blog.html', blog_posts=blog_posts, videos=videos)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return redirect(url_for('home'))
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'success': False, 'message': 'Username already exists'})
    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'success': True})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return redirect(url_for('home'))
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        return jsonify({'success': True})
    return jsonify({'success': False, 'message': 'Invalid username or password'})

@app.route('/profile')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('home'))
    user = User.query.get(user_id)
    return render_template('profile.html', user=user)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('home'))
    user = User.query.get(user_id)
    
    if request.method == 'POST':
        user.first_name = request.form.get('first_name', '')
        user.last_name = request.form.get('last_name', '')
        user.bio = request.form.get('bio', '')
        user.location = request.form.get('location', '')
        user.website = request.form.get('website', '')
        user.github_username = request.form.get('github_username', '')
        user.linkedin_username = request.form.get('linkedin_username', '')
        user.twitter_username = request.form.get('twitter_username', '')
        
        db.session.commit()
        flash('Profile updated successfully')
        return redirect(url_for('profile'))
    
    return render_template('edit_profile.html', user=user)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out')
    return redirect(url_for('home'))

@app.context_processor
def inject_user():
    user_id = session.get('user_id')
    if user_id:
        return dict(current_user=User.query.get(user_id))
    return dict(current_user=None)

def add_sample_data():
    with app.app_context():
        db.create_all()
        if not BlogPost.query.first():
            blog_post1_image = ('https://lh3.googleusercontent.com/aida-public/AB6AXuCVTQH5z_Mct6Tcjk_oonbtr6GP-M25uwJY5cLxnmzJE31amq3_xviOzpwx_21Gmsr8JdQVsNKWXTYOu2qxYiD31joDdJs7-gOAmlXZVqMOvvsTsBzD8DnzQPhxYrrXcBvEk4FKwYXYF8eICTR-V_65p76BctdHvFeBR0PsoSytiyNpm4H6LNM-5IVV3u-G3-4-2g00ez7hKOQ_3RscKRwD07EBAzxuh7ulQKgxry-B7tEhvoMQ7p_OzxqLQJVg_U1_JHa4vpgL0YJT')
            blog_post1 = BlogPost(title='Understanding Data Structures', content='A comprehensive guide to data structures, covering arrays, linked lists, trees, and graphs.', published_date='June 19, 2025', image_url=blog_post1_image)
            blog_post2_image = ('https://lh3.googleusercontent.com/aida-public/AB6AXuCdIIPHuQ6CQfDxP9cPppBS27Vb7OI_CDAzf9WtADHDf5XaoxYGP2gpFE77ItzLX8FUcb8yNIxS5SgMtW4DMeajfDjJHN92B7PJeoZButi4B1B_ryk7rLtRkxycEPEGe3UlS5XNBPNoH4mpWmySSL6fmk0H3mNcJqEk4NRijEGzc3f1VHkNz6-e-2g00ez7hKOQ_3RscKRwD07EBAzxuh7ulQKgxry-B7tEhvoMQ7p_OzxqLQJVg_U1_JHa4vpgL0YJT')
            blog_post2 = BlogPost(title='Introduction to Machine Learning', content='An introductory overview of machine learning concepts, including supervised and unsupervised learning.', published_date='May 25, 2025', image_url=blog_post2_image)
            db.session.add_all([blog_post1, blog_post2])
            db.session.commit()

        if not Video.query.first():
            video1_thumbnail = ('https://lh3.googleusercontent.com/aida-public/AB6AXuAb9tpfLfLGTe6p0tiVeEI4Ypcm-UFGkeZ8Rw79__0ASv-1Vi6qWdZflUDOs6tsS9tWCgH2c73sNcauUqQD_b8T3X5cmWGRofNJvyCCirS3gPWDGRmUwUqYbVZMfMyGBUow_vplJiLLItcbZQsHZaiyQ6hvPsRM-4KcG9Q0ky6AN6tUeOLBt4u__iYMsZuAA5cLN7cvXdtBWfr32taxjLXdIH75wvELzcNMkFpKcTsrFeHinb29NGJ5UF4bQGc89BOAx3xLcoYfCVo3')
            video1 = Video(title='Coding Tutorial: Building a Simple Web App', description='A step-by-step tutorial on building a basic web application using HTML, CSS, and JavaScript.', video_url='#', thumbnail_url=video1_thumbnail)
            video2_thumbnail = ('https://lh3.googleusercontent.com/aida-public/AB6AXuDr03fE1ruAIoZbxn161g3E_ztSeJvyVIeauq2xOf3FIA_Ai04t6HKt50FxtEpQs3M-eQIOWNnvSnTxYAu1rHJFaJdueFElzwOPhrghH9eZM54NjBGhCB3QftqMiJlPOf_b7xdhvWBhNw3k7J-WoiaYkNHRpNPH7RwFGCFFWqXJU-AQhDMkNWb-6WSIfFAENsXTV4asgitEGAOb7mbhBntGG40WZYHV0v05XD6MlzsJAXUiTf9MlVdvzrjq_kc1dHMCHRPBOTFtcxfE')
            video2 = Video(title='Algorithm Explanation: Dijkstra\'s Algorithm', description='A detailed explanation of Dijkstra\'s algorithm for finding the shortest path in a graph.', video_url='#', thumbnail_url=video2_thumbnail)
            db.session.add_all([video1, video2])
            db.session.commit()

@app.before_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    add_sample_data()
    app.run(debug=True, port=5001)
