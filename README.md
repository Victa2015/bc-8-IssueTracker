# bc-8-IssueTracker
Issue Tracker

Issue Tracker is a python web application that keeps track of issues.
Main Features

Features:

Allow users to register and login
Allow users to raise an issue, specifying the issue subject, description, priority (low, medium, or high), and the department that is to handle the issue
Allow users to keep track of their issues
Allow admin users to view all issues
Allow admin users to resolve the issues
Allow admin users to assign issues to another user for resolution
Allow admin users to mark issues as resolved (closed) or in-progress

Using Issue Tracker

You may view a live demonstration of Issue Tracker on Heroku. (https://issuetrackery.herokuapp.com) To use the app, you will have to register a new user account and login with the specified details. You may also login to the administrator account using the following credentials:

Email: victor@gmail.com Password: v

Installation

You may also install the app on your local machine.

Prerequisites You should have a working installation of Python 2.7 as well as pip. It is recommended that you use a virtual environment for this project.

To install the app:

Clone this repository git clone https://github.com/Victa2015/bc-8-IssueTracker

Install requirements pip install -r requirements.txt

Run the server python run.py runserver


Non-administrative users must register and login to use the application. Once logged in, they can raise and keep track of their issues.

Administrative Users

Administrative users can view all issues raised by all users. They can mark issues as resolved or assign issues to users. Assignment of issues automatically marks them as in-progress. Admin users can also comment on issues.

Admin users can also add departments, which are the departments to which issues are assigned (such as Operations, Training, and Human Resources). They can also specify department heads for each department. Admin users can view, edit, and delete departments.

Icebox Features

The following are features that I did not implement in the application:

Notifications: users notified whenever their issue is commented on, marked as resolved, or marked as in-progress
Email confirmation as part of the registration process
User profiles: capabality for users to add or edit their password, email address, profile picture, and biography
You can view a complete list of completed and icebox features on the Trello board for this application.
