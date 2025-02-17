from flask import Flask, send_file
import os


RUNENVIRONMENT = os.getenv("RUNENVIRONMENT")
WEBSITEURL = os.getenv("WEBSITEURL")

app = Flask(__name__, static_url_path="", static_folder="static", subdomain_matching=True)
app.secret_key = b'048j79hdfosdFGh90h7es9f8jsdoFDG3F148d0nsdf8zt853fhxec'


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
