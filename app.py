from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone, timedelta
import time
from flask_wtf.csrf import CSRFProtect
import json
import os
import re
import urllib.request
import urllib.error

# Indian Standard Time (IST) timezone
IST = timezone(timedelta(hours=5, minutes=30))

def get_ist_time():
    """Get current time in IST"""
    return datetime.now(IST)

def fetch_github_profile(username):
    if not username:
        return None
    url = f"https://api.github.com/users/{username}"
    try:
        request_obj = urllib.request.Request(
            url,
            headers={"User-Agent": "portfolio-app"}
        )
        with urllib.request.urlopen(request_obj, timeout=5) as response:
            data = json.load(response)
        return {
            "username": data.get("login") or username,
            "name": data.get("name") or username,
            "avatar_url": data.get("avatar_url"),
            "html_url": data.get("html_url"),
            "public_repos": data.get("public_repos"),
            "followers": data.get("followers"),
            "following": data.get("following"),
        }
    except (urllib.error.URLError, urllib.error.HTTPError, ValueError):
        return None

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
secret_key = os.environ.get('SECRET_KEY')
if not secret_key:
    if os.environ.get('FLASK_ENV') == 'production':
        raise RuntimeError('SECRET_KEY environment variable is required in production')
    secret_key = 'dev-only-change-me'
app.config['SECRET_KEY'] = secret_key
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_SECURE'] = os.environ.get('SESSION_COOKIE_SECURE', '0') == '1'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 60 * 60 * 24 * 30
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
    created_at = db.Column(db.DateTime, nullable=False, default=get_ist_time)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=get_ist_time)
    is_read = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<ContactMessage from {self.name}>'

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=True)
    message = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=5)
    created_at = db.Column(db.DateTime, nullable=False, default=get_ist_time)
    is_approved = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Feedback from {self.name}>'

@app.route('/')
def home():
    projects = Project.query.all()
    blog_posts = BlogPost.query.order_by(BlogPost.id.desc()).limit(2).all()
    return render_template('index.html', projects=projects, blog_posts=blog_posts)



@app.route('/projects')
def projects():
    projects = Project.query.all()
    return render_template('project.html', projects=projects)

@app.route('/blog')
def blog():
    blog_posts = BlogPost.query.all()
    videos = Video.query.all()
    github_username = os.getenv('GITHUB_USERNAME', 'mrcuriousind')
    github_profile = fetch_github_profile(github_username)
    linkedin_url = os.getenv('LINKEDIN_URL', 'https://www.linkedin.com/in/mrcuriousind')
    linkedin_label = os.getenv('LINKEDIN_LABEL', 'mrcuriousind')
    linkedin_connections = os.getenv('LINKEDIN_CONNECTIONS', '820')
    return render_template(
        'blog.html',
        blog_posts=blog_posts,
        videos=videos,
        github_profile=github_profile,
        github_username=github_username,
        linkedin_url=linkedin_url,
        linkedin_label=linkedin_label,
        linkedin_connections=linkedin_connections,
    )

@app.route('/connect')
def connect():
    # Get last 2 approved feedbacks
    feedbacks = Feedback.query.filter_by(is_approved=True).order_by(Feedback.created_at.desc()).limit(2).all()
    return render_template('connect.html', feedbacks=feedbacks)

@app.route('/fun')
def fun():
    return render_template('fun.html')

@app.route('/submit-connect', methods=['POST'])
def submit_connect():
    try:
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()
        
        # Validate required fields
        if not all([name, email, subject, message]):
            return jsonify({'success': False, 'message': 'All fields are required'})
        
        # Validate email format
        email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        if not re.match(email_regex, email):
            return jsonify({'success': False, 'message': 'Invalid email address'})

        # Validate lengths
        if len(name) > 100:
            return jsonify({'success': False, 'message': 'Name is too long'})
        if len(email) > 120:
            return jsonify({'success': False, 'message': 'Email is too long'})
        if len(subject) > 200:
            return jsonify({'success': False, 'message': 'Subject is too long'})
        if len(message) > 2000:
            return jsonify({'success': False, 'message': 'Message is too long'})
        
        # Create new contact message
        new_message = ContactMessage(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        db.session.add(new_message)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Thank you for your message! I will get back to you soon.'})
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': 'An error occurred. Please try again later.'})

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    try:
        name = request.form.get('name', '').strip()
        role = request.form.get('role', '').strip()
        company = request.form.get('company', '').strip()
        message = request.form.get('message', '').strip()
        rating = request.form.get('rating', 5)
        
        # Validate required fields
        if not all([name, role, message]):
            return jsonify({'success': False, 'message': 'Name, role, and message are required'})
        
        # Validate rating
        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                rating = 5
        except:
            rating = 5

        # Validate lengths
        if len(name) > 100:
            return jsonify({'success': False, 'message': 'Name is too long'})
        if len(role) > 100:
            return jsonify({'success': False, 'message': 'Role is too long'})
        if len(company) > 100:
            return jsonify({'success': False, 'message': 'Company is too long'})
        if len(message) > 2000:
            return jsonify({'success': False, 'message': 'Message is too long'})
        
        # Create new feedback
        new_feedback = Feedback(
            name=name,
            role=role,
            company=company,
            message=message,
            rating=rating
        )
        
        db.session.add(new_feedback)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Thank you for your feedback! It will be reviewed and published soon.'})
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': 'An error occurred. Please try again later.'})

@app.route('/animations-demo')
def animations_demo():
    return render_template('animations_demo.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return redirect(url_for('home'))
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')
    confirm_password = request.form.get('confirm_password', '')

    if not email or not password:
        return jsonify({'success': False, 'message': 'Email and password are required'})

    email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    if not re.match(email_regex, email):
        return jsonify({'success': False, 'message': 'Invalid email address'})

    if len(password) < 8:
        return jsonify({'success': False, 'message': 'Password must be at least 8 characters'})
    if not re.search(r'[A-Z]', password):
        return jsonify({'success': False, 'message': 'Password must include an uppercase letter'})
    if not re.search(r'[a-z]', password):
        return jsonify({'success': False, 'message': 'Password must include a lowercase letter'})
    if not re.search(r'[0-9]', password):
        return jsonify({'success': False, 'message': 'Password must include a number'})
    if confirm_password and password != confirm_password:
        return jsonify({'success': False, 'message': 'Passwords do not match'})
    
    # Check if email already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'success': False, 'message': 'Email already registered'})
    
    # Generate username from email (part before @)
    username_base = email.split('@')[0]
    # Remove special characters and make it lowercase
    username_base = re.sub(r'[^a-zA-Z0-9]', '', username_base).lower()
    
    # Check if username exists, if so add numbers
    username = username_base
    counter = 1
    while User.query.filter_by(username=username).first():
        username = f"{username_base}{counter}"
        counter += 1
    
    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'success': True, 'username': username})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return redirect(url_for('home'))
    username_or_email = request.form.get('username', '').strip()
    password = request.form.get('password', '')
    if not username_or_email or not password:
        return jsonify({'success': False, 'message': 'Username/email and password are required'})
    
    # Try to find user by username or email (username is case-insensitive)
    user = None
    if username_or_email:
        user = User.query.filter(
            (User.username == username_or_email.lower()) | (User.email == username_or_email)
        ).first()
    
    if user and user.check_password(password):
        if not user.is_active:
            return jsonify({'success': False, 'message': 'Account is deactivated'})
        session['user_id'] = user.id
        session['user_initial'] = user.username[0].upper()
        session['is_admin'] = user.is_admin
        return jsonify({'success': True})
    return jsonify({'success': False, 'message': 'Invalid username/email or password'})

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
        # Check if username is being changed
        new_username = request.form.get('username', '').strip().lower()
        if new_username and new_username != user.username:
            # Check if new username is already taken
            existing_user = User.query.filter_by(username=new_username).first()
            if existing_user:
                flash('Username already taken. Please choose another one.')
                return render_template('edit_profile.html', user=user)
            user.username = new_username
        
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

@app.route('/check-username', methods=['POST'])
def check_username():
    username = request.form.get('username', '').strip().lower()
    user_id = session.get('user_id')
    
    if not username:
        return jsonify({'available': False, 'message': 'Username cannot be empty'})
    
    # Check if username contains only valid characters
    if not re.match(r'^[a-z0-9_]+$', username):
        return jsonify({'available': False, 'message': 'Username can only contain lowercase letters, numbers, and underscores'})
    
    # Check if username is too short
    if len(username) < 3:
        return jsonify({'available': False, 'message': 'Username must be at least 3 characters'})
    
    # Check if username already exists
    existing_user = User.query.filter_by(username=username).first()
    
    # If user is editing their own profile, allow their current username
    if existing_user:
        if user_id and existing_user.id == user_id:
            return jsonify({'available': True, 'message': 'This is your current username'})
        return jsonify({'available': False, 'message': 'Username already taken'})
    
    return jsonify({'available': True, 'message': 'Username is available'})

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_initial', None)
    session.pop('is_admin', None)
    flash('You have been logged out successfully')
    return redirect(url_for('home'))

@app.context_processor
def inject_user():
    user_id = session.get('user_id')
    unread_messages_count = 0
    if user_id:
        user = User.query.get(user_id)
        if user and user.is_admin:
            unread_messages_count = ContactMessage.query.filter_by(is_read=False).count()
        return dict(current_user=user, unread_messages_count=unread_messages_count)
    return dict(current_user=None, unread_messages_count=0)

@app.context_processor
def inject_static_version():
    def static_version(rel_path):
        try:
            abs_path = os.path.join(app.static_folder, rel_path)
            return int(os.path.getmtime(abs_path))
        except OSError:
            return int(time.time())
    return dict(static_version=static_version)

@app.after_request
def add_security_headers(response):
    response.headers.setdefault('X-Frame-Options', 'DENY')
    response.headers.setdefault('X-Content-Type-Options', 'nosniff')
    response.headers.setdefault('Referrer-Policy', 'strict-origin-when-cross-origin')
    response.headers.setdefault('Permissions-Policy', 'camera=(), microphone=(), geolocation=()')
    return response

@app.template_filter('ist_datetime')
def ist_datetime_filter(dt):
    """Convert datetime to IST and format it"""
    if dt is None:
        return ''
    # If datetime is naive (no timezone), assume it's already IST
    if dt.tzinfo is None:
        return dt.strftime('%b %d, %Y %I:%M %p IST')
    # If datetime has timezone, convert to IST
    ist_dt = dt.astimezone(IST)
    return ist_dt.strftime('%b %d, %Y %I:%M %p IST')



# Admin Panel Routes
@app.route('/admin')
def admin_dashboard():
    user_id = session.get('user_id')
    if not user_id:
        flash('Please login to access admin panel')
        return redirect(url_for('home'))
    
    user = User.query.get(user_id)
    if not user or not user.is_admin:
        flash('Access denied. Admin privileges required.')
        return redirect(url_for('home'))
    
    # Get statistics
    total_users = User.query.count()
    total_projects = Project.query.count()
    total_posts = BlogPost.query.count()
    total_videos = Video.query.count()
    total_messages = ContactMessage.query.count()
    unread_messages = ContactMessage.query.filter_by(is_read=False).count()
    total_feedback = Feedback.query.count()
    pending_feedback = Feedback.query.filter_by(is_approved=False).count()
    
    # Get recent users
    recent_users = User.query.order_by(User.created_at.desc()).limit(5).all()
    
    return render_template('admin/dashboard.html', 
                         user=user,
                         total_users=total_users,
                         total_projects=total_projects,
                         total_posts=total_posts,
                         total_videos=total_videos,
                         total_messages=total_messages,
                         unread_messages=unread_messages,
                         total_feedback=total_feedback,
                         pending_feedback=pending_feedback,
                         recent_users=recent_users)

@app.route('/admin/users')
def admin_users():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('home'))
    
    user = User.query.get(user_id)
    if not user or not user.is_admin:
        return redirect(url_for('home'))
    
    users = User.query.order_by(User.created_at.desc()).all()
    return render_template('admin/users.html', user=user, users=users)

@app.route('/admin/messages')
def admin_messages():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('home'))
    
    user = User.query.get(user_id)
    if not user or not user.is_admin:
        return redirect(url_for('home'))
    
    messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()
    unread_count = ContactMessage.query.filter_by(is_read=False).count()
    return render_template('admin/messages.html', user=user, messages=messages, unread_count=unread_count)

@app.route('/admin/feedback')
def admin_feedback():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('home'))
    
    user = User.query.get(user_id)
    if not user or not user.is_admin:
        return redirect(url_for('home'))
    
    feedbacks = Feedback.query.order_by(Feedback.created_at.desc()).all()
    pending_count = Feedback.query.filter_by(is_approved=False).count()
    return render_template('admin/feedback.html', user=user, feedbacks=feedbacks, pending_count=pending_count)

@app.route('/admin/feedback/<int:feedback_id>/approve', methods=['POST'])
def approve_feedback(feedback_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('home'))
    
    user = User.query.get(user_id)
    if not user or not user.is_admin:
        return redirect(url_for('home'))
    
    feedback = Feedback.query.get(feedback_id)
    if feedback:
        feedback.is_approved = True
        db.session.commit()
        flash('Feedback approved')
    
    return redirect(url_for('admin_feedback'))

@app.route('/admin/feedback/<int:feedback_id>/hide', methods=['POST'])
def hide_feedback(feedback_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('home'))
    
    user = User.query.get(user_id)
    if not user or not user.is_admin:
        return redirect(url_for('home'))
    
    feedback = Feedback.query.get(feedback_id)
    if feedback:
        feedback.is_approved = False
        db.session.commit()
        flash('Feedback hidden')
    
    return redirect(url_for('admin_feedback'))

@app.route('/admin/feedback/<int:feedback_id>/delete', methods=['POST'])
def delete_feedback(feedback_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('home'))
    
    user = User.query.get(user_id)
    if not user or not user.is_admin:
        return redirect(url_for('home'))
    
    feedback = Feedback.query.get(feedback_id)
    if feedback:
        db.session.delete(feedback)
        db.session.commit()
        flash('Feedback deleted')
    
    return redirect(url_for('admin_feedback'))

@app.route('/admin/message/<int:message_id>/mark-read', methods=['POST'])
def mark_message_read(message_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('home'))
    
    user = User.query.get(user_id)
    if not user or not user.is_admin:
        return redirect(url_for('home'))
    
    message = ContactMessage.query.get(message_id)
    if message:
        message.is_read = True
        db.session.commit()
        flash('Message marked as read')
    
    return redirect(url_for('admin_messages'))

@app.route('/admin/message/<int:message_id>/delete', methods=['POST'])
def delete_message(message_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('home'))
    
    user = User.query.get(user_id)
    if not user or not user.is_admin:
        return redirect(url_for('home'))
    
    message = ContactMessage.query.get(message_id)
    if message:
        db.session.delete(message)
        db.session.commit()
        flash('Message deleted successfully')
    
    return redirect(url_for('admin_messages'))

@app.route('/admin/make-admin/<int:user_id>', methods=['POST'])
def make_admin(user_id):
    admin_id = session.get('user_id')
    if not admin_id:
        return redirect(url_for('home'))
    
    admin = User.query.get(admin_id)
    if not admin or not admin.is_admin:
        return redirect(url_for('home'))
    
    target_user = User.query.get(user_id)
    if target_user:
        target_user.is_admin = True
        db.session.commit()
        flash(f'{target_user.username} is now an admin')
    
    return redirect(url_for('admin_users'))

@app.route('/admin/delete-user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    admin_id = session.get('user_id')
    if not admin_id:
        return redirect(url_for('home'))
    
    admin = User.query.get(admin_id)
    if not admin or not admin.is_admin:
        return redirect(url_for('home'))
    
    target_user = User.query.get(user_id)
    if target_user:
        # Prevent admin from deleting themselves
        if target_user.id == admin.id:
            flash('You cannot delete your own account')
            return redirect(url_for('admin_users'))
        
        username = target_user.username
        db.session.delete(target_user)
        db.session.commit()
        flash(f'User {username} has been deleted')
    
    return redirect(url_for('admin_users'))

@app.route('/admin/toggle-status/<int:user_id>', methods=['POST'])
def toggle_user_status(user_id):
    admin_id = session.get('user_id')
    if not admin_id:
        return redirect(url_for('home'))
    
    admin = User.query.get(admin_id)
    if not admin or not admin.is_admin:
        return redirect(url_for('home'))
    
    target_user = User.query.get(user_id)
    if target_user:
        # Prevent admin from deactivating themselves
        if target_user.id == admin.id:
            flash('You cannot deactivate your own account')
            return redirect(url_for('admin_users'))
        
        target_user.is_active = not target_user.is_active
        status = 'activated' if target_user.is_active else 'deactivated'
        db.session.commit()
        flash(f'{target_user.username} has been {status}')
    
    return redirect(url_for('admin_users'))

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG') == '1'
    port = int(os.environ.get('PORT', '5000'))
    app.run(debug=debug_mode, port=port)
