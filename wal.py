# -*- coding: utf-8 -*- 
from flask import Flask, request
from flask import render_template
from wtforms import Form, BooleanField, TextField, TextAreaField, RadioField, validators
from wtforms.validators import Length, NumberRange, DataRequired
from wtforms_html5 import TextField, IntegerField, DateField, EmailField, TelField
import string
import random
import codecs
import os
import glob

def removeoldpdfs():
    files = glob.glob('static/*.pdf')
    for f in files:
        os.remove(f)

def removetexouts(randomstring):
    try:
        os.remove('static/%s.aux' % randomstring)
        os.remove('static/%s.log' % randomstring) 
        os.remove('static/%s.out' % randomstring) 
    except:
        pass

def randomstring():
    char_set = string.ascii_lowercase + string.digits
    return ''.join(random.sample(char_set,25))    

def render_latex(form):
    template = form.template.data + ".tex"
    rendertex = render_template(template, 
                                absname = form.absname.data,
                                absstreet = form.absstreet.data,
                                abslocation = form.abslocation.data,
                                abslocationnum = form.abslocationnum.data,
                                abstelephone = form.abstelephone.data,
                                absemail = form.absemail.data,
                                empname = form.empname.data,
                                empstreet = form.empstreet.data,
                                emplocation = form.emplocation.data,
                                emplocationnum = form.emplocationnum.data,
                                subject = form.subject.data,
                                title = form.title.data,
                                greeting = form.greeting.data, 
                                text = form.text.data,
                                mark = form.mark.data)
    
    return rendertex.replace('[rundauf]', '{').replace('[rundzu]', '}')    
    

class LetterForm(Form):
    absname = TextField(u"Absender Name")
    absstreet = TextField(u"Absender Straße")
    abslocation = TextField(u"Absender Ort")
    abslocationnum = IntegerField(u"Absender PLZ", [validators.Optional()])
    abstelephone = TelField(u"Absender Telefon")
    absemail = EmailField(u"Absender Email")
    
    empname = TextField(u"Empfänger Name")
    empstreet = TextField(u"Empfänger Straße")
    emplocation =TextField(u"Empfänger Ort")
    emplocationnum = IntegerField(u"Absender PLZ", [validators.Optional()])
    
    subject = TextField(u"Betreff")
    title = TextField(u"Anrede")
    greeting = TextField(u"Gruß")
    text = TextAreaField(u'Body')
    template = RadioField(u'Vorlage', choices=[('gbrief', 'G-Brief'), 
                                               ('gbrief2', 'G-Brief2')
                                               ],
                                               default='gbrief')
    mark = BooleanField(label=u'Faltmarken', default=True)

app = Flask(__name__)

@app.route("/")
def index():
    removeoldpdfs()
    return render_template('index.html', form=LetterForm())

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    randomstr = randomstring()
    
    form = LetterForm(request.form)
    
    with codecs.open('/tmp/%s.tex' % randomstr, encoding="utf-8",  mode='w+') as f:
        f.write(render_latex(form))
    
    os.system('pdflatex -no-shell-escape -interaction nonstopmode -output-directory=static  -jobname=%s /tmp/%s.tex' % (randomstr, randomstr)) 
    
    removetexouts(randomstr)

    return render_template('index.html', form=form, pdfname=randomstr, show=True)

if __name__ == "__main__":
    app.run(debug=True)
