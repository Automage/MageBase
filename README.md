# MageBase
www.mage-base.com

Testing the waters of the Flask microframework, using Gunicorn as the application server.

Current features:
- Redirection
- Serving static files

## Deployment

Create a virtualenv and install the requirements from requirements.txt.

```
pip install -r requirements.txt
```

## Execution
Start local server with 4 workers:
```
gunicorn -w 4 app:app
```

Start public server with 4 workers:
```
gunicorn -b <public_ip>:<internal_port> -w 4 app:app
```

See for setup help:
https://www.reddit.com/r/flask/comments/b2qhfp/making_gunicorn_flask_app_public_without_nginx/eivlzua?utm_source=share&utm_medium=web2x
