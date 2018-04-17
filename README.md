# FS_Blog

This is a basic blog site created using the Django (2.0) framework with a PostgreSQL database.

## Getting Started

Assuming that you have Django installed and have followed [the instructions](https://docs.djangoproject.com/en/2.0/topics/install/#database-installation) to set up your database:

+ open the settings.py file in mysite/mysite/ and edit the NAME, USER, PASSWORD, and HOST keys in the DATABASES item 
+ run the command: `$ python manage.py migrate` to create any necessary database tables
+ run the command: `$ python manage.py runserver` to view the site in a development environment

## Includes

+ Register & Login
+ Create, Read, Update and Delete a new blog post (title, body)
+ Viewing posts on a front page
+ Responsive design using Bootstrap

## Notes

This site can also be viewed at [rebeccakempe.com](rebeccakempe.com)*

The AJAX used does technically add new posts to the front page, but it does so in an admittedly hacky way. I plan to keep working on it, but this is the best I could figure out this weekend.




* probably by the time you're reading this, that will be true. It's up, but I'm trying to troubleshoot an intermittent nginx-related gateway issue. I don't have a lot of experience with server configuration, and I didn't want to violate the rules by asking for help. That said, now that this is submitted, I'm going to see if someone at work can help me figure that out.
