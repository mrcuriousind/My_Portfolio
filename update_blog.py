from app import app, db, BlogPost

with app.app_context():
    # Delete all existing blog posts
    BlogPost.query.delete()
    
    # Add new blog posts
    blog_post1 = BlogPost(
        title='Rethinking Campus Connectivity: The Birth of Curious Intelligence',
        content='A detailed look at why I\'m building a specialized SaaS for inter-college communication. This post covers the mission to provide every college with a secure, isolated digital ecosystem for students and faculty.',
        published_date='January 28, 2026',
        image_url='/static/Campus.jpeg'
    )
    blog_post2 = BlogPost(
        title='Vibe Coding 101: How I\'m Building a SaaS with AI and Intent',
        content='Vibe coding is less about writing line-by-line and more about guiding AI through natural language and clear intent. I share how I use the Gemini CLI to rapidly prototype features and focus on high-level architecture rather than boilerplate code.',
        published_date='January 25, 2026',
        image_url='/static/vibe.png'
    )
    blog_post3 = BlogPost(
        title='Beyond Copilot: How AI is Raising the Bar for Software Quality',
        content='AI in 2026 is not just a helper—it is a second brain that predicts failures, reviews logic gaps, and optimizes code for performance. I discuss how integrating AI-driven testing and refactoring has reduced my rework by 30%.',
        published_date='January 20, 2026',
        image_url='/static/Copilot.png'
    )
    blog_post4 = BlogPost(
        title='From Solo Developer to Leading a Collective: Building a Team of Believer',
        content='Building a mission-driven project isn\'t about hiring employees; it\'s about finding a collective of believers. We share our strategies for identifying high-agency partners who care about the vision as much as the code.',
        published_date='January 15, 2026',
        image_url='/static/teamleader.png'
    )
    
    db.session.add_all([blog_post1, blog_post2, blog_post3, blog_post4])
    db.session.commit()
    print('Blog posts updated successfully')
