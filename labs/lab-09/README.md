> This lab is an extension of [Lab 07](labs/lab-07) work.


## How to run? 
Run ``create-env.sh`` to set up the python enviroment and install the dependecies for the project.

```
./create-env.sh
```

First run ``create_db.py`` to create the SQLite database (users and posts tables) and populate it with the data.

```
python3 create_db.py
```

Then, run ``flaskapp.py`` to deploy the Flask app and their routes.   `
```
python3 flaskapp.py
```

## How to use:
- Visit [localhost:5000/](localhost:5000/) to see a Hello world
- Visit [localhost:5000/users](localhost:5000/users) to see a list of users from the database
- Visit [localhost:5000/user/profile/{id}](localhost:5000/user/profile/{id}) to see the profile of a specific user with **``id = {id}``**
- Visit [localhost:5000/posts](localhost:5000/posts) to see a list of posts from the database
- Visit [localhost:5000/post/{id}](localhost:5000/post/{id}) to see a specific post with **``id = {id}``** 