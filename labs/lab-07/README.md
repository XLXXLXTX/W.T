## How to run? 
Run ``create-env.sh`` to set up the python enviroment and install the dependecies for the project.

```
./create-env.sh
```

First run ``createtables.py`` to create the SQLite database and populate it with the data.

```
python3 createtables.py
```

Then, run ``flaskapp.py`` to deploy the Flask app and their routes.   `
```
python3 flaskapp.py
```

## How to use:
- Visit localhost:5000/ to see a Hello world
- Visit localhost:5000/users to see a list of users from the database
- Visit localhost:5000/user/profile/{id} to see the profile of a specific user with **``id = {id}``**