from flask import Flask, send_file
import os


RUNENVIRONMENT = os.getenv("RUNENVIRONMENT")
WEBSITEURL = os.getenv("WEBSITEURL")

app = Flask(__name__, static_url_path="", static_folder="static", subdomain_matching=True)
secret = os.environ.get("FLASK_SECRET_KEY")
if secret is None:
    raise RuntimeError("FLASK_SECRET_KEY environment variable not set")

app.secret_key = secret.encode()  # convert string → bytes

# Páginas Dedicadas a Documentos
@app.route('/')
def home():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/documents/osantorosario.pdf'
    return send_file(filepath, as_attachment=False)


@app.errorhandler(404)
def page_not_found(e):
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/documents/osantorosario.pdf'
    return send_file(filepath, as_attachment=False)


if __name__ == "__main__":
    if RUNENVIRONMENT == 'DEV':
        print('Run Environment = Development')
    elif RUNENVIRONMENT == 'PROD':
        print('Run Environment = Production')
        app.config['SERVER_NAME'] = WEBSITEURL
    app.run(host='0.0.0.0', port=80)
