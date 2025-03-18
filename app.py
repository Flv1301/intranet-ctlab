from flask import Flask, render_template

app = Flask(__name__, static_url_path='/intranet/static')

@app.route('/intranet')
def index():
    return render_template('index.html')

@app.route('/intranet/sobreolaboratorio')
def sobreolaboratorio():
    return render_template('sobreolaboratorio.html')

@app.route('/intranet/legislacao')
def legislacao():
    return render_template('legislacao.html')

@app.route('/intranet/documentos')
def documentos():
    return render_template('documentos.html')

@app.route('/intranet/acordos')
def acordos():
    return render_template('acordos.html')

@app.route('/intranet/leis')
def leis():
    return render_template('leis.html')

@app.route('/intranet/atos')
def atos():
    return render_template('atos.html')

@app.route('/intranet/simba')
def simba():
    return render_template('simba.html')

@app.route('/intranet/simba/legislacao')
def simba_legislacao():
    return render_template('simba_legislacao.html')

@app.route('/intranet/simba/manuais')
def simba_manuais():
    return render_template('simba_manuais.html')

@app.route('/intranet/rif')
def rif():
    return render_template('rif.html')

@app.route('/intranet/rif/legislacao')
def rif_legislacao():
    return render_template('rif_legislacao.html')

@app.route('/intranet/rif/manuais')
def rif_manuais():
    return render_template('rif_manuais.html')

@app.route('/intranet/manuais')
def manuais():
    return render_template('manuais.html')

@app.route('/intranet/apoio')
def apoio():
    return render_template('apoio.html')

@app.route('/intranet/linksuteis')
def linksuteis():
    return render_template('linksuteis.html')

@app.route('/intranet/restrito')
def restrito():
    return render_template('restrito.html')

@app.route('/intranet/fontes')
def fontes():
    return render_template('fontes.html')

@app.route('/intranet/contatos')
def contatos():
    return render_template('contatos.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
