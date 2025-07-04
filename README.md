# Mr. Curious's Portfolio

A modern, responsive personal portfolio website built with Flask and Tailwind CSS. This project showcases skills, projects, blog posts, and provides comprehensive information about Mr. Curious, a final year Computer Science Engineering student.

## ✨ Features

### 🏠 **Home Page**
- Hero section with professional introduction
- Comprehensive About Me section
- Interactive skills showcase with tabbed categories:
  - Programming Languages (Python, Java, C++, JavaScript)
  - Frameworks (React, Angular, Express.js, Tailwind CSS)
  - Databases (PostgreSQL, MongoDB, MySQL)
  - AI Tools (ChatGPT, Gemini CLI, GitHub Copilot)
  - Development Tools (VS Code, Git)
  - Cloud Platforms
- Featured projects section

### 📊 **Skills Page**
Detailed breakdown of technical competencies organized by categories

### 💼 **Projects Page**
Showcase of academic and personal projects with:
- Project descriptions
- Technology stacks
- GitHub links
- Live demo links
- Project images

### 📝 **Blog Page**
Content hub featuring:
- Technical blog posts
- Tutorial videos
- Educational content

### 📞 **Contact Page**
Professional contact information and social media links

### 🎨 **Design Features**
- Fully responsive design
- Dark/Light mode support
- Modern UI with Tailwind CSS
- Interactive components
- Optimized performance

## 🛠 Technologies Used

### Backend
- **Flask** - Python web framework
- **Flask-SQLAlchemy** - Database ORM
- **SQLite** - Database for development

### Frontend
- **HTML5** - Semantic markup
- **Tailwind CSS v4.1.11** - Utility-first CSS framework
- **JavaScript** - Interactive functionality
- **PostCSS** - CSS processing
- **Autoprefixer** - CSS vendor prefixing

### Development Tools
- **npm** - Package management
- **PostCSS CLI** - CSS build process
- **Git** - Version control

### Database Models
- **Project** - Portfolio project information
- **BlogPost** - Blog content management
- **Video** - YouTube video integration

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Node.js and npm
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/CLI_Portfolio.git
   cd CLI_Portfolio
   ```

2. **Set up Python environment:**
   ```bash
   # Create virtual environment
   python3 -m venv venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   .\venv\Scripts\activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```

4. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

5. **Build CSS (optional):**
   ```bash
   npm run build:css
   ```

6. **Run the application:**
   ```bash
   python app.py
   ```

7. **Access the application:**
   Open your browser and navigate to `http://localhost:5000`

## 📁 Project Structure

```
CLI_Portfolio/
├── app.py                 # Main Flask application
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── skill.html        # Skills page
│   ├── project.html      # Projects page
│   ├── blog.html         # Blog page
│   └── contact.html      # Contact page
├── static/               # Static assets
│   └── css/
│       ├── input.css     # Tailwind input file
│       └── output.css    # Compiled CSS
├── package.json          # Node.js dependencies
├── tailwind.config.js    # Tailwind configuration
├── postcss.config.js     # PostCSS configuration
└── README.md            # Project documentation
```

## 🔧 Development

### Database Setup
The application automatically creates the SQLite database and populates it with sample data on first run.

### CSS Development
To rebuild CSS after making changes:
```bash
npm run build:css
```

### Adding New Content
- **Projects**: Add new entries to the Project model in `app.py`
- **Blog Posts**: Add new entries to the BlogPost model
- **Videos**: Add new entries to the Video model

## 🌟 Key Features Breakdown

### Skills Showcase
- **Languages**: Python, Java, C++, JavaScript
- **Frameworks**: React, Angular, Express.js, Tailwind CSS
- **Databases**: PostgreSQL, MongoDB, MySQL
- **AI Tools**: ChatGPT, Gemini CLI, GitHub Copilot
- **Tools**: VS Code, Git
- **Cloud**: Various cloud platforms

### Responsive Design
- Mobile-first approach
- Tablet and desktop optimized
- Cross-browser compatibility
- Accessibility features

## 📱 Usage

1. **Navigation**: Use the header navigation to explore different sections
2. **Skills Tab**: Click on skill categories to view different technology stacks
3. **Projects**: Browse through featured projects with detailed information
4. **Blog**: Read technical articles and watch educational videos
5. **Contact**: Get in touch through provided contact information

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Steps to contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 About the Developer

Mr. Curious is a passionate final year Computer Science Engineering student with expertise in:
- Full-stack web development
- Modern JavaScript frameworks
- Python backend development
- Database design and management
- AI tool integration
- Cloud technologies

## 📞 Contact

Feel free to reach out for collaborations, questions, or just to connect!

---

⭐ **Star this repository if you found it helpful!**
