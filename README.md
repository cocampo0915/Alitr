# ALITR

ALITR is a full-stack web application built with Python-based Django framework that helps users track job applications. The app implements Django's built-in authentication and implements authorization by restricting access to the Create, Read, Update and Delete resources.


## Getting Started

[Click here](https://alitr.herokuapp.com/) to see the app on Heroku!

## Technologies Used
- HTML5
- CSS3
- JavaScript
- Python
- Django
- PostgreSQL
- AWS S3

-----

## App Screenshots and WireFrames

Home Page

![screenshot](/main_app/static/images/alitrhomepage.png)

Login and Sign up Page

![screenshot](/main_app/static/images/alitrfinalsignup.png)

After user is logged in, the 'Add job application' Page

![screenshot](/main_app/static/images/alitraddjob.png)

After a job application is added, it is categorized under 'New Jobs', 'In Progress', or 'Outcome'. User can update the status of the job application. 

![screenshot](/main_app/static/images/alitralljobs.png)


Users can edit, or delete the job application as well as the status and date. 

![screenshot](/main_app/static/images/alitrjobdetails.png)

Users can view their profile page

![screenshot](/main_app/static/images/alitauserprofile.PNG)

Users can update their profile page to add a photo, or add/change information

![screenshot](/main_app/static/images/alitruserprofileupdate.PNG)

Users can add a Professional skill, which will be displayed on their profile page. 

![screenshot](/main_app/static/images/alitraddskill.png)

Users can edit or delete the Professional skill.

![screenshot](/main_app/static/images/alitrskilldetail.png)



-----



## ERD
![screenshot](/main_app/static/images/alitrerds.png)


An important part of our planning process was to determine the data needs of our application.

The main data entity of this web application is the "Job_application" model.
Secondary is the "User" model, which has a One-to-Many relationship with "Job_application".
The third "Status" model, which "Job_application" has a One-to-Many relationship.
The "User" model was also extended with a "Profile" model, which it has a One-to-One relationship with. A separate "Photo" model was also made to handle uploading of profile pictures, and has a One-to-Many relationship with "Profile".
"Skill" is the last model, which has a One-to-Many relationship with "User", and is displayed as part of the user profile.



## Pitch Deck

Click [here](https://docs.google.com/presentation/d/19crljcsBgCRyAg5mleOzzwwlLGEVdwZPkZUDIxCQs_4/edit?usp=sharing) to see our pitch deck

-----
## Trello Board

Click [here](https://trello.com/b/VTVjj9L5/project-4) to see our Trello Board

-----
## Future Enhancements
- Responsive design for mobile/tablet
- User being able to upload attachments to a job application, such as PDFs (resumes, cover letters, etc)
- Adding a "Company" model linked to the job applications, where users can add information and notes about companies they apply to, and can view applications by Company, should a user submit more than one application to the same company
- A default status ("Applied") is created and linked to a job application when a new job application is created -- currently, the user must manually add statuses after the creation of a job app.

## Challenges
- Extending Django's User model to add fields for users to sign up or sign in using email.