### Accounts

- [Forms](/accounts/tests_forms.py)
    - Login Form tested for:
        - valid when completed correctly
        - invalid with missing input
    - Registration Form tested for:
        - valid when completed correctly and user is created
        - invalid when email is not unique and correct error message
        - invalid with missing input and correct error message
        - invalid when passwords do not match and correct error message

- [Models](/accounts/tests_models.py) 
    - Profile tested for:
        - when a User is created a profile is also created for the user
        - values can be assigned to the profile and saved

- [Views](/accounts/tests_views.py)
    - Register page tested for:
        - URL works and status is 200
        - correct template is used
    - Login page tested for:
        - URL works and status is 200
        - correct template is used
    - Profile page tested for:
        - URL works and status is 200 when user is logged in
        - redirected to login page is user is not logged in
        - correct template is used
    - Edit Profile page tested for:
        - URL works and status is 200 when user is logged in
        - redirected to login page is user is not logged in
        - correct template is used

### Blog

- [Models](/blog/test_models.py)
    - Blog tested for:
        - date created by default
        - data inputed is saved correctly
        - when saved a topic with same data is created for the forum

- [Views](/blog/test_views.py)
    - Blog page tested for:
        - URL works and status is 200
        - correct template is used

### Donations

- [Models](/donations/tests_models.py)
    - Donation tested for:
        - date created by default
        - data inputed is saved correctly

- [Views](/donations/tests_views.py)
    - Donation page tested for:
        - URL works and status is 200
        - correct template is used
    - Donate page tested for:
        - URL works and status is 200 when user is logged in
        - redirected to login page is user is not logged in
        - correct template is used

### Forum

- [Forms](/forum/tests_forms.py)
    - Topic Form tested for:
        - valid when completed correctly
    - Post Form tested for:
        - valid when completed correctly

- [Models](/forum/tests_models.py)
    - Category tested for:
        - date created by default
        - posts set to 0 by default
        - data inputed is saved correctly
    - Topic tested for:
        - date created by default
        - posts set to 0 by default
        - locked set to false by default
        - data inputed is saved correctly
    - Post tested for:
        - date created by default
        - upvotes set to 0 by default
        - data inputed is saved correctly

- [Views](/forum/tests_views.py)
    - Forum Home page tested for:
        - URL works and status is 200
        - correct template is used
    - Forum Category page tested for:
        - URL works and status is 200
        - correct template is used
    - Forum Topic page tested for:
        - URL works and status is 200
        - correct template is used
    - Create Topic page tested for:
        - URL works and status is 200 when user is logged in
        - redirected to login page is user is not logged in
        - correct template is used
    - Edit Topic page tested for:
        - URL works and status is 200
        - correct template is used
    - Create Post page tested for:
        - URL works and status is 200 when user is logged in
        - redirected to login page is user is not logged in
        - correct template is used
    - Edit Post page tested for:
        - URL works and status is 200
        - correct template is used
    - Upvote Post tested for:
        - URL works and redirects back to Topic page
        

### Ticket

- [Forms](/tickets/tests_forms.py)
    - Ticket Form tested for:
        - valid when completed correctly
        - invalid with missing input and correct error message

- [Models](/tickets/tests_models.py)
    - Ticket tested for:
        - date created by default
        - upvotes set to 0 by default
        - data inputed is saved correctly
        - when saved a topic with same data is created for the forum

- [Views](/tickets/tests_views.py)
    - Ticket page tested for:
        - URL works and status is 200
        - correct template is used
    - Edit Ticket page tested for:
        - URL works and status is 200
        - correct template is used
    - Upvote Ticket tested for:
        - URL works and redirects back to Ticket page