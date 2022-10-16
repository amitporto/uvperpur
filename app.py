from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

st=''

class inputform(FlaskForm):
      totWt=StringField("Total Weight of samples")
      ns=StringField("Number of samples")
      abs=StringField("Absorbance")
      spa=StringField("Specific absorbance")
      wtTak=StringField("Weight taken")
      dilFac=StringField("Dilution factor")
      ori=StringField("Label claim")
      submit=SubmitField("Submit")


def convert(totWt,ns,abs,spa,wtTak,dilFac,ori):
    av=av=totWt/ns
    amn=(abs*dilFac*av)/(spa*wtTak*100)
    ppur=(amn/ori)*100
    return ppur

@app.route("/", methods=["GET","POST"])

def index():
    input=inputform()
    strn=''
    totWt,ns,abs,spa,wtTak,dilFac,expA='','','','','','',''
    if input.validate_on_submit():
       strn=strn+str(convert(float(request.form["totWt"]),float(request.form["ns"]),float(request.form["abs"]),float(request.form["spa"]),
       float(request.form["wtTak"]),float(request.form["dilFac"]),float(request.form["ori"])))
    return render_template('index.html', template_form=input, template_list=strn)


if __name__=='__main__':
  app.run(debug=True)
