# 🎨 Mr. Curious's Portfolio

A stunning, modern personal portfolio website with advanced animations, user authentication, and admin panel. Built with Flask, Tailwind CSS, and featuring a complete user management system.

![Portfolio](https://img.shields.io/badge/Status-Live-success)
![Flask](https://img.shields.io/badge/Flask-3.0.0-blue)
![Tailwind](https://img.shields.io/badge/Tailwind-4.1.11-38bdf8)
![Python](https://img.shields.io/badge/Python-3.7+-3776ab)

---

## ✨ Features

### 🎯 **Core Pages**

#### 🏠 Home Page
- Stunning hero section with gradient text animations
- Interactive skills showcase with 6 categories (Languages, Frameworks, Databases, AI Tools, Tools, Cloud)
- Featured projects with 3D card effects
- Blog preview section
- Contact form with validation
- Smooth scroll animations

#### 💼 Projects Page
- Portfolio project showcase
- Hover effects and animations
- Project details and links

#### 📝 Blog Page
- Technical articles
- Video content integration
- Clean, readable layout

#### 📞 Contact Page
- Professional contact form with validation
- Quick stats (Projects, Clients, Coffee, Response Time)
- Client testimonials
- Contact information cards (Email, Location, Availability)

---

### 🔐 **Authentication System**

#### User Registration
- ✅ Email-based signup
- ✅ Auto-generated usernames from email
- ✅ Strong password validation (8+ chars, uppercase, lowercase, number)
- ✅ Real-time password strength indicator
- ✅ Password confirmation with matching validation
- ✅ Email format validation with visual feedback

#### User Login
- ✅ Login with username OR email
- ✅ Password visibility toggle
- ✅ "Forgot Password?" functionality (UI ready)
- ✅ Session-based authentication
- ✅ Beautiful modal design with animations

#### User Profile
- ✅ View profile information
- ✅ Edit profile (username, name, bio, location, website)
- ✅ Social media links (GitHub, LinkedIn, Twitter)
- ✅ Avatar with user initials
- ✅ Logout functionality

---

### 🛡️ **Admin Panel**

#### Dashboard
- 📊 Statistics overview (Users, Projects, Posts, Videos)
- 🎯 Quick action menu
- 👥 Recent users list
- 🎨 Beautiful gradient design

#### User Management
- 👥 View all registered users
- 🛡️ Promote users to admin
- 🚫 Activate/Deactivate user accounts
- 🗑️ Delete users
- 📊 User status and role badges
- 🔒 Self-protection (can't delete/deactivate yourself)

---

### 🎨 **Design Features**

#### Visual Effects
- ✨ Smooth scroll reveal animations
- 🎭 3D card hover effects
- 🌊 Gradient text animations
- 💫 Button glow effects
- 🎪 Magnetic button interactions
- 🔄 Page transition animations
- 📊 Counter animations

#### Theme System
- 🌓 Dark/Light mode toggle
- 🎚️ Modern iOS-style toggle switch
- 💾 Theme preference saved in localStorage
- 🎨 Consistent color scheme throughout
- 🌈 Gradient accents (Cyan #9de1f5 → Green #33c46b)

#### Responsive Design
- 📱 Mobile-first approach
- 💻 Tablet and desktop optimized
- 🖥️ Container queries for adaptive layouts
- 🎯 Touch-friendly interactions

---

## 🛠 Technologies Used

### Backend
- **Flask 3.0.0** - Python web framework
- **Flask-SQLAlchemy 3.1.1** - Database ORM
- **Werkzeug 3.0.1** - Password hashing and security
- **SQLite** - Database

### Frontend
- **HTML5** - Semantic markup
- **Tailwind CSS v4.1.11** - Utility-first CSS framework
- **JavaScript (ES6+)** - Interactive functionality
- **Font Awesome 6.4.0** - Icon library
- **Google Fonts** - Space Grotesk, Noto Sans

### Build Tools
- **PostCSS** - CSS processing
- **Autoprefixer** - CSS vendor prefixing
- **npm** - Package management

### Database Models
- **User** - Authentication and profiles
- **Project** - Portfolio projects
- **BlogPost** - Blog content
- **Video** - Video content

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- Node.js 14+ and npm
- Git

### Step-by-Step Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/mrcuriousind/CLI_Portfolio.git
cd CLI_Portfolio
```

#### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install Flask Flask-SQLAlchemy Werkzeug
```

#### 3. Install Node.js Dependencies
```bash
npm install
```

#### 4. Build CSS
```bash
npm run build:css
```

#### 5. Initialize Database
```bash
python init_db.py
```

#### 6. Run the Application
```bash
python app.py
```

#### 7. Access the Website
Open your browser and go to: **http://127.0.0.1:5000**

---

## 👤 User System Setup

### Create Your Account
1. Click **"Login"** in the header
2. Click **"Create Account"**
3. Enter your email
4. Create a strong password
5. Confirm password
6. Your username will be auto-generated!

### Make Yourself Admin
```bash
python make_admin.py <your_username>
```

Example:
```bash
python make_admin.py mrcuriousind
```

### Access Admin Panel
After making yourself admin:
1. Logout and login again
2. Click **"Admin"** in the header
3. Access dashboard at: http://127.0.0.1:5000/admin

---

## 📁 Project Structure

```
CLI_Portfolio/
├── app.py                      # Main Flask application
├── init_db.py                  # Database initialization script
├── make_admin.py               # Admin user creation script
├── migrate_db.py               # Database migration script
├── requirements.txt            # Python dependencies
├── package.json                # Node.js dependencies
├── tailwind.config.js          # Tailwind configuration
├── postcss.config.js           # PostCSS configuration
│
├── templates/                  # HTML templates
│   ├── base.html              # Base template with header/footer
│   ├── index.html             # Home page
│   ├── contact.html           # Contact page
│   ├── profile.html           # User profile page
│   ├── edit_profile.html      # Edit profile page
│   ├── animations_demo.html   # Animation showcase
│   └── admin/                 # Admin panel templates
│       ├── dashboard.html     # Admin dashboard
│       └── users.html         # User management
│
├── static/                     # Static assets
│   ├── css/
│   │   ├── input.css          # Tailwind source file
│   │   └── output.css         # Compiled CSS
│   ├── js/
│   │   └── animations.js      # Animation controller
│   └── Curious_Logo.png       # Logo image
│
└── instance/                   # Instance folder
    └── portfolio.db           # SQLite database
```

---

## 🎯 Key Features Explained

### 🎨 Animation System
- **Scroll Reveal**: Elements fade in as you scroll
- **Hover Effects**: 3D transforms and shadows
- **Counter Animations**: Numbers count up on view
- **Magnetic Buttons**: Buttons follow cursor
- **Ripple Effects**: Click feedback animations
- **Page Transitions**: Smooth page changes

### 🔐 Security Features
- Password hashing with Werkzeug
- Session-based authentication
- Protected admin routes
- CSRF protection ready
- SQL injection prevention (SQLAlchemy ORM)
- XSS protection

### 📧 Form Validation
- Real-time email validation
- Password strength checking
- Password match verification
- Visual feedback (icons, colors, messages)
- HTML5 validation patterns

---

## 🎮 Available Commands

### Development
```bash
# Run the Flask app
python app.py

# Build CSS
npm run build:css

# Initialize database
python init_db.py

# Make user admin
python make_admin.py <username>

# Migrate database (add new columns)
python migrate_db.py
```

### Database Management
```bash
# Create all tables
python init_db.py

# Add admin privileges
python make_admin.py mrcuriousind

# Check database
sqlite3 instance/portfolio.db ".tables"
```

---

## 🎨 Color Scheme

### Primary Colors
- **Cyan**: `#9de1f5` - Light accent
- **Green**: `#33c46b` - Primary action color
- **Dark Blue**: `#101923` - Dark mode background
- **Medium Blue**: `#182534` - Dark mode cards
- **Border Blue**: `#314b68` - Dark mode borders
- **Text Blue**: `#90abcb` - Dark mode secondary text

### Gradients
- **Primary Gradient**: `from-[#9de1f5] to-[#33c46b]`
- **Background Gradient**: Used for banners and highlights

---

## 📊 Database Schema

### User Model
```python
- id (Primary Key)
- username (Unique, Auto-generated)
- email (Unique, Required)
- password_hash (Encrypted)
- first_name, last_name
- bio (Text)
- location, website
- github_username, linkedin_username, twitter_username
- created_at (DateTime)
- is_active (Boolean)
- is_admin (Boolean)
```

### Project Model
```python
- id, title, description
- image_url, github_link, live_link
```

### BlogPost Model
```python
- id, title, content
- published_date, image_url
```

### Video Model
```python
- id, title, description
- video_url, thumbnail_url
```

---

## 🔗 Routes

### Public Routes
- `/` - Home page
- `/skills` - Skills page
- `/projects` - Projects page
- `/blog` - Blog page
- `/contact` - Contact page

### Authentication Routes
- `/signup` (POST) - User registration
- `/login` (POST) - User login
- `/logout` - User logout

### User Routes (Protected)
- `/profile` - View profile
- `/edit_profile` - Edit profile

### Admin Routes (Admin Only)
- `/admin` - Admin dashboard
- `/admin/users` - User management
- `/admin/make-admin/<id>` - Promote to admin
- `/admin/delete-user/<id>` - Delete user
- `/admin/toggle-status/<id>` - Activate/Deactivate user

---

## 🎯 Usage Guide

### For Regular Users
1. **Browse** the portfolio without login
2. **Create account** to access profile features
3. **Login** with username or email
4. **Edit profile** to customize your information
5. **Add social links** (GitHub, LinkedIn, Twitter)

### For Admins
1. **Make yourself admin**: `python make_admin.py <username>`
2. **Access admin panel**: Click "Admin" in header
3. **View statistics**: See user and content counts
4. **Manage users**: Promote, deactivate, or delete users
5. **Monitor activity**: View recent registrations

---

## 🐛 Troubleshooting

### Database Issues
```bash
# Recreate database
rm instance/portfolio.db
python init_db.py
```

### CSS Not Updating
```bash
# Rebuild CSS
npm run build:css

# Hard refresh browser
# Mac: Cmd + Shift + R
# Windows: Ctrl + Shift + F5
```

### Can't Access Admin Panel
```bash
# Make yourself admin
python make_admin.py <your_username>

# Logout and login again to refresh session
```

### Module Not Found Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt
npm install
```

---

## 🚀 Deployment

### Production Checklist
- [ ] Change `SECRET_KEY` in app.py
- [ ] Use production WSGI server (Gunicorn, uWSGI)
- [ ] Set up PostgreSQL/MySQL for production
- [ ] Configure environment variables
- [ ] Enable HTTPS
- [ ] Set up email service for password reset
- [ ] Configure backup system
- [ ] Set up monitoring and logging

### Recommended Hosting
- **Heroku** - Easy deployment
- **DigitalOcean** - VPS hosting
- **AWS** - Scalable cloud hosting
- **Vercel/Netlify** - For static frontend

---

## 📚 Documentation

Additional documentation files:
- `LOGIN_SYSTEM_GUIDE.md` - Complete authentication guide
- `ADMIN_PANEL_GUIDE.md` - Admin panel documentation

---

## 🎉 Features Highlights

✅ **Beautiful UI** - Modern, clean design with smooth animations
✅ **Dark Mode** - Full dark mode support with theme toggle
✅ **Responsive** - Works perfectly on all devices
✅ **User System** - Complete authentication and profiles
✅ **Admin Panel** - Powerful content and user management
✅ **Form Validation** - Real-time validation with visual feedback
✅ **Security** - Password hashing, session management
✅ **Performance** - Optimized CSS, lazy loading
✅ **Accessibility** - Semantic HTML, ARIA labels
✅ **SEO Ready** - Proper meta tags and structure

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 About

**Mr. Curious** - Final Year Computer Science Engineering Student

Passionate about creating efficient and scalable applications using modern technologies. Specializing in full-stack web development, AI integration, and cloud technologies.

### Skills
- **Languages**: Python, Java, C++, JavaScript
- **Frameworks**: React, Angular, Express.js, Tailwind CSS
- **Databases**: PostgreSQL, MongoDB, MySQL
- **AI Tools**: ChatGPT, Gemini CLI, GitHub Copilot
- **Cloud**: AWS, Azure, Google Cloud

---

## 📞 Contact

- **Email**: mrcuriousindia@gmail.com
- **Location**: Bangalore, India
- **GitHub**: [@mrcuriousind](https://github.com/mrcuriousind)
- **LinkedIn**: [mrcuriousind](https://www.linkedin.com/in/mrcuriousind)
- **YouTube**: [@brocheloraspirants](https://www.youtube.com/@brocheloraspirants)

---

## 🙏 Acknowledgments

- Font Awesome for icons
- Google Fonts for typography
- Tailwind CSS for styling framework
- Flask community for excellent documentation

---

## 📈 Version History

- **v2.0** - Added authentication system and admin panel
- **v1.5** - Implemented advanced animations
- **v1.0** - Initial portfolio release

---

⭐ **If you found this project helpful, please give it a star!**

Made with ❤️ by Mr. Curious
