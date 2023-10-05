from flask import*

marketplace = Flask(__name__)
@marketplace.route('/')
def pagina_inicial():
    return  render_template('index.html')

marketplace.run()
