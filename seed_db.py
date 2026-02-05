from app import app, db, BlogPost, Video, Project

def add_sample_data():
    with app.app_context():
        db.create_all()
        
        if not Project.query.first():
            project1 = Project(
                title='End-to-End Academic Management System',
                description='A specialized SaaS ecosystem designed to streamline inter-college communication and administrative workflows using React and Node.js.',
                image_url='/static/Project.png',
                github_link=None,
                live_link=None
            )
            db.session.add(project1)
            db.session.commit()
        
        if not BlogPost.query.first():
            blog_post1_image = ('https://lh3.googleusercontent.com/aida-public/AB6AXuCVTQH5z_Mct6Tcjk_oonbtr6GP-M25uwJY5cLxnmzJE31amq3_xviOzpwx_21Gmsr8JdQVsNKWXTYOu2qxYiD31joDdJs7-gOAmlXZVqMOvvsTsBzD8DnzQPhxYrrXcBvEk4FKwYXYF8eICTR-V_65p76BctdHvFeBR0PsoSytiyNpm4H6LNM-5IVV3u-G3-4-2g00ez7hKOQ_3RscKRwD07EBAzxuh7ulQKgxry-B7tEhvoMQ7p_OzxqLQJVg_U1_JHa4vpgL0YJT')
            blog_post1 = BlogPost(title='Rethinking Campus Connectivity: The Birth of Curious Intelligence', content='A detailed look at why I\'m building a specialized SaaS for inter-college communication. This post covers the mission to provide every college with a secure, isolated digital ecosystem for students and faculty.', published_date='January 28, 2026', image_url=blog_post1_image)
            blog_post2_image = ('https://lh3.googleusercontent.com/aida-public/AB6AXuCdIIPHuQ6CQfDxP9cPppBS27Vb7OI_CDAzf9WtADHDf5XaoxYGP2gpFE77ItzLX8FUcb8yNIxS5SgMtW4DMeajfDjJHN92B7PJeoZButi4B1B_ryk7rLtRkxycEPEGe3UlS5XNBPNoH4mpWmySSL6fmk0H3mNcJqEk4NRijEGzc3f1VHkNz6-e-2g00ez7hKOQ_3RscKRwD07EBAzxuh7ulQKgxry-B7tEhvoMQ7p_OzxqLQJVg_U1_JHa4vpgL0YJT')
            blog_post2 = BlogPost(title='Vibe Coding 101: How I\'m Building a SaaS with AI and Intent', content='"Vibe coding" is less about writing line-by-line and more about guiding AI through natural language and clear intent. I share how I use the Gemini CLI to rapidly prototype features and focus on high-level architecture rather than boilerplate code.', published_date='January 25, 2026', image_url=blog_post2_image)
            blog_post3_image = ('https://lh3.googleusercontent.com/aida-public/AB6AXuCVTQH5z_Mct6Tcjk_oonbtr6GP-M25uwJY5cLxnmzJE31amq3_xviOzpwx_21Gmsr8JdQVsNKWXTYOu2qxYiD31joDdJs7-gOAmlXZVqMOvvsTsBzD8DnzQPhxYrrXcBvEk4FKwYXYF8eICTR-V_65p76BctdHvFeBR0PsoSytiyNpm4H6LNM-5IVV3u-G3-4-2g00ez7hKOQ_3RscKRwD07EBAzxuh7ulQKgxry-B7tEhvoMQ7p_OzxqLQJVg_U1_JHa4vpgL0YJT')
            blog_post3 = BlogPost(title='Beyond Copilot: How AI is Raising the Bar for Software Quality', content='AI in 2026 isn\'t just a "helper"—it\'s a second brain that predicts failures, reviews logic gaps, and optimizes code for performance. I discuss how integrating AI-driven testing and refactoring has reduced my rework by 30%.', published_date='January 20, 2026', image_url=blog_post3_image)
            blog_post4_image = ('https://lh3.googleusercontent.com/aida-public/AB6AXuCdIIPHuQ6CQfDxP9cPppBS27Vb7OI_CDAzf9WtADHDf5XaoxYGP2gpFE77ItzLX8FUcb8yNIxS5SgMtW4DMeajfDjJHN92B7PJeoZButi4B1B_ryk7rLtRkxycEPEGe3UlS5XNBPNoH4mpWmySSL6fmk0H3mNcJqEk4NRijEGzc3f1VHkNz6-e-2g00ez7hKOQ_3RscKRwD07EBAzxuh7ulQKgxry-B7tEhvoMQ7p_OzxqLQJVg_U1_JHa4vpgL0YJT')
            blog_post4 = BlogPost(title='From Solo Founder to Team Lead: The Art of Technical Recruitment', content='Finding the right partners for a startup isn\'t about hiring employees; it\'s about finding "believers." I share my strategy for approaching friends and peers to join the Curious Intelligence Platform journey, focusing on shared vision over just technical skills.', published_date='January 15, 2026', image_url=blog_post4_image)
            db.session.add_all([blog_post1, blog_post2, blog_post3, blog_post4])
            db.session.commit()

        if not Video.query.first():
            video1_thumbnail = ('https://lh3.googleusercontent.com/aida-public/AB6AXuAb9tpfLfLGTe6p0tiVeEI4Ypcm-UFGkeZ8Rw79__0ASv-1Vi6qWdZflUDOs6tsS9tWCgH2c73sNcauUqQD_b8T3X5cmWGRofNJvyCCirS3gPWDGRmUwUqYbVZMfMyGBUow_vplJiLLItcbZQsHZaiyQ6hvPsRM-4KcG9Q0ky6AN6tUeOLBt4u__iYMsZuAA5cLN7cvXdtBWfr32taxjLXdIH75wvELzcNMkFpKcTsrFeHinb29NGJ5UF4bQGc89BOAx3xLcoYfCVo3')
            video1 = Video(title='Coding Tutorial: Building a Simple Web App', description='A step-by-step tutorial on building a basic web application using HTML, CSS, and JavaScript.', video_url='#', thumbnail_url=video1_thumbnail)
            video2_thumbnail = ('https://lh3.googleusercontent.com/aida-public/AB6AXuDr03fE1ruAIoZbxn161g3E_ztSeJvyVIeauq2xOf3FIA_Ai04t6HKt50FxtEpQs3M-eQIOWNnvSnTxYAu1rHJFaJdueFElzwOPhrghH9eZM54NjBGhCB3QftqMiJlPOf_b7xdhvWBhNw3k7J-WoiaYkNHRpNPH7RwFGCFFWqXJU-AQhDMkNWb-6WSIfFAENsXTV4asgitEGAOb7mbhBntGG40WZYHV0v05XD6MlzsJAXUiTf9MlVdvzrjq_kc1dHMCHRPBOTFtcxfE')
            video2 = Video(title='Algorithm Explanation: Dijkstra\'s Algorithm', description='A detailed explanation of Dijkstra\'s algorithm for finding the shortest path in a graph.', video_url='#', thumbnail_url=video2_thumbnail)
            db.session.add_all([video1, video2])
            db.session.commit()
        print('Sample data added successfully')

if __name__ == '__main__':
    add_sample_data()
