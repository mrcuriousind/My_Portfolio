from app import app, db, Project

with app.app_context():
    # Update the existing project
    project = Project.query.filter_by(title='End-to-End Academic Management System').first()
    if project:
        project.image_url = '/static/Project.png'
        db.session.commit()
        print('Project updated successfully')
    else:
        print('Project not found')
