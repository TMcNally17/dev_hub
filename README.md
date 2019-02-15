# Full Stack Django Project - Developer Hub

[![Build Status](https://travis-ci.org/TMcNally17/dev_hub.svg?branch=master)](https://travis-ci.org/TMcNally17/dev_hub)

Developer Hub is a site where you can get all the support for a project a 
developer needs. Developer Hub can be tailored to a project to provide feedback 
from users by using Bug Tickets to track issues experienced by users, a Forum for
users to discuss different topics and Donations from backers of your project.

Developer Hub can be maintained by an admin to check on the Bug Tickets and updated
their status, the Forum can be moderated and topics can be lock or deleted if not
appropriate and also provide feedback to users with a Blog which can be created 
on the site. 

## UX

Developer Hub is designed for 3 user types which are:

- User A, Admin, the user who's project the site has been tailored for.
- User B, Member, the users who have registered an account.
- User C, Non-Member, the users who haven't registered an account.

These user types will have different needs to each other and I have used these
user stories to help guide the UX process:

- As User A I want to:
    - Do Admin Tasks, to keep the site running effectively
    - Update Content, to keep the site relevant
    - Be a Forum Moderator, to make sure its safe for everyone
    - Update Bug Statuses, to show User B progress
    - Update Developer Blog, to keep User B and C updated as to the project

- As User B I want to:
    - Login, to be able to interact with tickets, post in forums and make donations
    - Have a Profile, to personalize my experience 
    - Have access to a Forum, to be able to discuss topics with other User B
    - Create a Bug Ticket, to inform User A of an issue
    - Discuss Existing Tickets, to inform other User B of opinions and similar issues via the Forum
    - View the status of Bug Tickets, to see when the Bug will be fixed
    - Be able to Upvote Bug Tickets, to inform User A of how many User B have had the same issue
    - Make Donations, to help User A develop the project for rewards later
    - View a Developer Blog, to find out what User A has to say
    - Have access to a Contact Form, to be able to contact User A
    
- As User C I want to:
    - Be able to Register, to be a member and access more of the site
    - View a Developer Blog, to find out what User A has to say
    - View a Forum, to see what discussions are going on
    - View Bug Tickets, to see how many issues are fixed
    - Have access to a Contact Form, to be able to contact User A

Mock ups can be viewed for each page below:
- [Index](/mock_ups/Index.jpg)
- [Tickets](/mock_ups/Tickets.jpg)
- [Forum](/mock_ups/Forum.jpg)
- [Blog](/mock_ups/Blog.jpg)
- [Donations](/mock_ups/Donations.jpg)
- [Graphs](/mock_ups/Graphs.jpg)
- [Profile](/mock_ups/Profile.jpg)
- [Register](/mock_ups/Register.jpg)
- [Contact](/mock_ups/Contact.jpg)

## Features

### Existing Features

Currently these are the features that are implemented and how each feature 
provides UX:

- Bug Tickets - allows User B to inform User A of an issue, tickets can be moderated by User A 
    - Create - allows User B to create a ticket, by completing the ticket form
    - Edit - allows User B to edit a ticket by the user who created it, by completing the ticket form
    - Comment - allows User B to discuss tickets via the forum topic which is created when the ticket is created
    - Status - allows User A to inform User B of current status of tickets
    - Upvote - allows User B to inform User A which tickets most users are encountering, by using the upvote button 

- Donations - allows User B to be a backer for the project for rewards from User A
    - Donation Buttons - allows User B to select an amount which suits them, by selecting one of the donation buttons
    - Donation Slider - allows User A to inform User B and C of the current development target and total donations

- Accounts - allows Users to create and update an account
    - Login - allows User B to login to access site
    - Register - allows User C to register an account, by completing registration form
    - Profile - User account details and profile
    - Edit Profile - allows User to personalize profile, by filling profile form.

- Graphs - allows User A to show Users B and C a summary of tickets and donations
    - Most Upvoted Ticket - shows the top 5 most upvoted tickets 
    - Ticket Status - shows how many of each status there are for all tickets 
    - Donations - shows how much in donations have been recieved per day where a donation has been made
    
- Blog - allows User A to update User B and C of news via blog posts

- Forum - allows User B to discuss topics, by posting using the post form
    - Categories - these are created by User A
        - Accounts
        - Tickets - a topic is created when a ticket is created so that ticket can be discussed
        - Blog - a topic is created when a blog post is created so that blog post can be discussed
        - Donations
    - Topics - topics and posts can be moderated by User A 
        - Create - User B can create their own topics, by completing topic form 
        - Edit Topic - User B can edit topics by the user who created it, by completing edit topic form 

### Planned Features
 
- Contact Form
    - to users to contact the site


## Technology Used

- [Python](https://www.python.org)
    - **Python** is used to create the backend using Django.
- [Django](https://www.djangoproject.com)
    - **Django** is a high-level python web framework.
- [Gunicorn](https://gunicorn.org/)
    - **Gunicorn** is a Python WSGI HTTP Server used to run the server.
- [PostgreSQL](https://www.postgresql.org)
    - **PostgreSQL** is a powerful, open source object-relational database system.
- [Bootstrap](http://getbootstrap.com)
    - **Bootstrap** is used to give a responsive layout.
- [JQuery](https://jquery.com)
    - **JQuery** is used to give better UX.
- [AWS](https://aws.amazon.com/)
    - **AWS** is used for cloud based S3 bucket to serve static files. 
- [Stripe](https://stripe.com/gb)
    - **Stripe** is a ecommerce platform which is used for donations on my project

## Testing

The project is built using Django which has built in test framework. For each
section of the project there are test files for models, forms and views if 
applicable. I wrote the test this way so that each file tests a different 
aspect of each section making it easier to follow and track errors. 

A summary of the tests can be found in [test summary](/test_summary.md)

These are automated tests which can be run by using the following command:

    python3 manage.py test

Testing can be run for each section individually by adding the section name to 
the end of the command.

I have also tested my project for responsiveness and on different browsers which 
is detailed in [Browser Tests](/browser_tests.pdf)

## Deployment

### Heroku

My project is deployed on [Heroku](https://www.heroku.com/) hosting platform and
can be viewed at [Dev Hub](https://dev-hub-project.herokuapp.com/)

When deploying the project I needed to:

- Include a Procfile which tells Heroku what type of app it is and what to run
- Include a requirements.txt to tell Heroku what dependencies need installing
- Install gunicorn to run the server
- Install a Postgres Database on Heroku as the Production Database
- Set up Travis CI to ensure build is working before deployment
- Set up AWS S3 Bucket to host the static files
- Set up Heroku Config Vars for AWS, Database URL, Secret Key, Stripe Keys and Disable Collectstatic as served from AWS 

### Local

To run locally you need to clone the repository:

    - git clone https://github.com/TMcNally17/dev_hub.git

You need to install the dependencies in requirements.txt:

    - pip install -r requirements.txt
    
You need to set environ variables: 

    - DEVELOPMENT=1
    - SECRET_KEY=[Insert a secret key]
    
You also need to include Stripe Keys

    - STRIPE_PUBLISHABLE=[Insert a stripe key]
    - STRIPE_SECRET=[Insert a stripe secret key]
    
Run the project by:

    - Adding your domain host name to ALLOWED_HOSTS in /devhub/settings.py 
    - Run the command "python3 manage.py runserver IP:PORT" with your local IP and PORT  

## Credits


### Media

The images in the project are from [Pexels](https://www.pexels.com/)

- [Blog Image](https://www.pexels.com/photo/alphabet-arts-and-crafts-blog-conceptual-459688/)
- [Light Bulb Image](https://www.pexels.com/photo/bright-clear-close-up-dark-401107/)