# Mr. Curious's Portfolio

This is a personal portfolio website for Mr. Curious, built with Flask and styled using Tailwind CSS. It showcases projects, skills, blog posts, and provides contact information.

## Features

*   **Home Page:** Introduction, About Me, Skills (interactive tabs), Projects, Blog, and Contact sections.
*   **Skills Page:** Detailed breakdown of programming languages, frameworks, databases, and tools.
*   **Projects Page:** A collection of academic and personal projects.
*   **Blog Page:** Blog posts and YouTube videos.
*   **Contact Page:** A contact form and recent social posts/feedback.
*   **Responsive Design:** Built with Tailwind CSS for a modern and responsive user interface.

## Technologies Used

*   **Backend:** Flask (Python)
*   **Database:** SQLite (managed by Flask-SQLAlchemy)
*   **Frontend:** HTML, CSS (Tailwind CSS via CDN), JavaScript
*   **Package Manager:** npm

## Setup and Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd CLI_Portfolio
    ```

2.  **Create a Python virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```

4.  **Install Python dependencies:**
    ```bash
    pip install Flask Flask-SQLAlchemy
    ```

5.  **Run the Flask application:**
    ```bash
    python3 app.py
    ```
    The application will typically run on `http://127.0.0.1:5001/` (or `http://localhost:5001/`).

## Usage

Navigate through the different sections using the header navigation links: Home, Skills, Projects, Blog, and Contact.

On the Home page, click on the skill categories (Languages, Frameworks, Databases, Tools, AI Tools) to view different sets of skills.

## Contributing

If you'd like to contribute, please fork the repository and create a pull request.
