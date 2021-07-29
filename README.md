# ALITR

ALITR is a full-stack web application built with Python-based Django framework that helps users track job applications. The app implements Django's built-in authentication and implements authorization by restricting access to the Create, Read, Update and Delete resources.


## Getting Started

[Click here](https://alitr.herokuapp.com/) to see the app on Heroku!

## App Screenshots and WireFrames

Home Page

![screenshot](/alitr/main_app/static/images/alitrhomepage.png)

Login and Sign up Page

![screenshot](/alitr/main_app/static/images/alitrloginandsignup.png)

After user is logged in, the 'Add job application' Page

![screenshot](/alitr/main_app/static/images/alitraddjob.png)

After a job application is added, it is categorized under 'New Jobs', 'In Progress', or 'Outcome'. User can update the status of the job application. 

![screenshot](/alitr/main_app/static/images/alitralljobs.png)

Users can edit, or delete the job application as well as the status and date. 

![screenshot](/alitr/main_app/static/images/alitrjobdetails.png)

Users can add a Professional skill. 

![screenshot](/alitr/main_app/static/images/alitraddskill.png)

Users can edit or delete the Professional skill.

![screenshot](/alitr/main_app/static/images/alitrskilldetail.png)







## ERD
![screenshot](/alitr/main_app/static/images/alitrerds.png)


An important part of our planning process was to determine the data needs of our application.

The main data entity of this web application is the "Job_application" model.
Secondary is the "User" model, which has a One-to-Many relationship with "Job_application".
The third "Status" model, which "Job_application" has a One-to-Many relationship with as well as the "Attachment" model. 


## Technologies Used
- HTML5
- CSS3
- JavaScript
- Python
- Django
- PostgreSQL
-----
## Pitch Deck

Click [here]() to see our pitch deck

-----
## Trello Board

Click [here]() to see our Trello Board

-----
## Future Enhancements
- Responsive design

## Challenges
- Extending Django's User model to add fields for users to sign up or sign in using email.