#!/bin/bash

# make sure to have installed virtualenv in python
#   $ pip install virtualenv

# after that select a python version for virtualenv
# and use this comand: 
#   $ virtualenv -p PythonX.X <venv-name>
if [ ! -d "lab-4-flask" ]; then
    virtualenv -p python3.10 lab-4-flask
fi

# activate the virtual env with this command:
#   $ source <venv-name>/bin/activate
source lab-4-flask/bin/activate

# or deactivate it with this command:
#   $ deactivate 