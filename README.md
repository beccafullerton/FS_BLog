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
+ The ability to view posts filtered by author
+ Responsive design using Bootstrap

## Notes

This site can also be viewed at [rebeccakempe.com](rebeccakempe.com)*

This does technically use ajax to add new posts to the front page, but it does so in an incredibly hacky way. After about a 15 minute conversation with a programmer I work with, I was able to do a much better job - which can be viewed [here](https://github.com/beccafullerton/FS_BLOG2). I also realized that my use of buil-in views was impeding my ability to manipulate some of the info in the way I wanted, so I've changed some of that as well.


