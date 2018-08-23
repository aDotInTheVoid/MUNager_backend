# MUNager_backend
The backend to MUNager.

Exposes a graphql API for the frontend to conect to.

The frontend is being developed but the source isn't availible at this time due to legal reasons.

# Dependencys
- python3.7
- postgresql (yes postgres, anythin else wount work)

# Install
```
virtualenv -p python3.7 .venv
source .venv/bin/activate
pip install -r requirements.txt
```
configure your postgresql and then setup local_setings.py to conect to the DB

