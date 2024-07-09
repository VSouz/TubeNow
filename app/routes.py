from app import app
from flask import render_template, request, send_file
from app import baixar

@app.route('/')
@app.route('/index')

def index():
    return render_template('home.html')

@app.route('/mp3')

def mp3():
    return render_template('mp3.html')

@app.route('/home')

def home():
    return render_template('home.html')

@app.route('/autenticarmp3', methods = ['GET'])

def autenticarmp3():
    link = request.args.get('link')

    if link:
        info = baixar.details(link)

        return render_template('autenticarmp3.html', info=info )
    else:
        return render_template('mp3.html')

@app.route('/autenticarmp4', methods = ['GET','POST'])

def autenticarmp4():
    link = request.args.get('link')

    if link:
        info = baixar.details(link)

        return render_template('autenticarmp4.html', info=info )
    else:
        return render_template('home.html')


@app.route('/baixarVideoBest', methods=['POST'])

def baixarVideoBest():
    link = request.form.get('video1080')
    baixado = baixar.baixarVideoBest(link)
    return send_file(baixado, as_attachment=True)


@app.route('/baixarVideo', methods=['POST'])

def baixarVideo():
    link = request.form.get('video360')
    baixado = baixar.baixarAudio50(link)
    return send_file(baixado, as_attachment=True)

@app.route('/baixaraudio50', methods=['POST'])
def baixaraudio50():
    link = request.form.get('audio50')
    baixado = baixar.baixarAudio50(link)
    return send_file(baixado, as_attachment=True)

@app.route('/baixaraudio70', methods=['POST'])
def baixaraudio70():
    link = request.form.get('audio70')
    baixado = baixar.baixarAudio70(link)
    return send_file(baixado, as_attachment=True)

@app.route('/baixaraudio128', methods=['POST'])
def baixaraudio128():
    link = request.form.get('audio128')
    baixado = baixar.baixarAudio128(link)
    return send_file(baixado, as_attachment=True)

@app.route('/baixaraudio160', methods=['POST'])
def baixaraudio160():
    link = request.form.get('audio160')
    baixado = baixar.baixarAudio160(link)
    return send_file(baixado, as_attachment=True)