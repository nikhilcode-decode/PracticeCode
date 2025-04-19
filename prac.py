# from flask import Flask, jsonify, request
# from celery import Celery
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# app = Flask(__name__)
# app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
# app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
# celery.conf.update(app.config)

# Base = declarative_base()

# # Define the User model
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)

# # Create the database engine and session
# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
# Session = sessionmaker(bind=engine)

# # Celery task to fetch users from the database
# @celery.task
# def fetch_users():
#     session = Session()
#     users = session.query(User).all()
#     session.close()
#     return [{'id': user.id, 'name': user.name} for user in users]

# # Endpoint to get all users
# @app.route('/users', methods=['GET'])
# def get_users():
#     # Call the Celery task to fetch users asynchronously
#     task = fetch_users.delay()
#     # Return a task ID to track the progress
#     return jsonify({"task_id": task.id}), 202

# # Endpoint to retrieve the result of the task
# @app.route('/users/<task_id>', methods=['GET'])
# def get_users_task_result(task_id):
#     task = fetch_users.AsyncResult(task_id)
#     if task.state == 'SUCCESS':
#         return jsonify(task.result)
#     else:
#         return jsonify({"message": "Task is still processing"}), 202

# if __name__ == '__main__':
#     # Create the database tables if they don't exist
#     Base.metadata.create_all(engine)
#     app.run(debug=True)


#     from celery import Celery

# app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# @app.task
# def send_email(user_id):
#     # Logic to send email
#     return f"Email sent to user {user_id}!"

# @app.task
# def generate_report(user_id):
#     # Logic to generate report
#     return f"Report generated for user {user_id}!"

# @app.task
# def update_profile(user_id):
#     # Logic to update user profile
#     return f"Profile updated for user {user_id}!"

# # Example function to run multiple tasks
# def handle_user_actions(user_id):
#     results = []
#     results.append(send_email.delay(user_id))
#     results.append(generate_report.delay(user_id))
#     results.append(update_profile.delay(user_id))
#     return results

# from asyncio.log import logger
# class CountRequestsMiddleware:

#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.count_requests = 0
#         self.count_exceptions = 0

#     def __call__(self, request, *args, **kwargs):
#         self.count_requests += 1
#         logger.info(f"Handled {self.count_requests} requests so far")
#         return self.get_response(request)

#     def process_exception(self, request, exception):
#         self.count_exceptions += 1
#         logger.error(f"Encountered {self.count_exceptions} exceptions so far")



