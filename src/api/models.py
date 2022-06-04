from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(255), nullable = False)
    last_name = db.Column(db.String(255), nullable = False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    def __repr__(self):
        return f'<User{self.id} {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name":self.last_name,
        }

class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    link_type = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255), nullable = True)
    user = db.relationship("User")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "link_type":self.link_type,
            "link":self.link
        }

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    job_title = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    req_id = db.Column(db.String(255), nullable=False)
    description =  db.Column(db.Text, nullable=False)
    status = db.Column(db.String(255), nullable=False)
    experience = db.Column(db.String(255), nullable=False)
    job_type  = db.Column(db.String(255), nullable=False)
    user = db.relationship("User")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "job_title": self.job_title,
            "company": self.company,
            "date_created": self.date_created,
            "location": self.location,
            "req_id": self.req_id,
            "description": self.description,
            "status": self.status,
            "experience": self.experience,
            "job_type":self.job_type
        }

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer, db.ForeignKey('application.id'))
    note = db.Column(db.Text, nullable=False)
    application = db.relationship("Application")

    def serialize(self):
        return {
            "id": self.id,
            "application_id": self.application_id,
            "note": self.note
        }

class Interaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer, db.ForeignKey('application.id'))
    interaction_type = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(255), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    application = db.relationship("Application")

    def serialize(self):
        return {
            "id": self.id,
            "application_id": self.application_id,
            "interaction_type": self.interaction_type,
            "date": self.date,
            "comment": self.comment
        }