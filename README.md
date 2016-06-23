# bc-8-IssueTracker
Issue Tracker

Issue Tracker is a web application written in Python using Flask for the Andela Kenya Class VI Bootcamp project. The application is a simple way to keep track of issues raised by people within an organization.

Main Features

The application is able to:

Allow users to register and login
Allow users to raise an issue, specifying the issue subject, description, priority (low, medium, or high), and the department that is to handle the issue
Allow users to view, edit, and delete their issues
Allow admin users to view all issues
Allow admin users to comment on issues
Allow admin users to assign issues to another user for resolution
Allow admin users to mark issues as resolved (closed) or in-progress
Using Issue Tracker

You may view a live demonstration of Issue Tracker on Heroku. To use the app, you will have to register a new user account and login with the specified details. You may also login to the administrator account using the following credentials:

Email: admin@it.com Password: cat2016

Installation

You may also install the app on your local machine.

Prerequisites You should have a working installation of Python 2.7 as well as pip. It is recommended that you use a virtual environment for this project.

To install the app:

Clone this repository git clone https://github.com/mbithe/bc-6-my-issue-tracker

Install requirements pip install -r requirements.txt

Run the server python manage.py runserver

Workflow

Non-administrative Users

Non-administrative users must register and login to use the application. Once logged in, they can raise an issue. They can view, edit, and delete their issues. The dashboard shows a summary of the status of their issues, whether they are pending(open), in-progress or resolved(closed).

Administrative Users

Administrative users can view all issues raised by all users. They can mark issues as resolved or assign issues to users. Assignment of issues automatically marks them as in-progress. Admin users can also comment on issues.

Admin users can also add departments, which are the departments to which issues are assigned (such as Operations, Training, and Human Resources). They can also specify department heads for each department. Admin users can view, edit, and delete departments.

Icebox Features

The following are features that I did not implement in the application:

Notifications: users notified whenever their issue is commented on, marked as resolved, or marked as in-progress
Email confirmation as part of the registration process
User profiles: capabality for users to add or edit their password, email address, profile picture, and biography
You can view a complete list of completed and icebox features on the Trello board for this application.
