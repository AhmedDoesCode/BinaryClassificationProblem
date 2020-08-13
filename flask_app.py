
from flask import Flask, jsonify, request,render_template, flash
#from flask_restful import Resource, Api
from flask_wtf import FlaskForm
from wtforms import SelectField, FloatField
from wtforms.validators import InputRequired
import predict_app
import json
from time import perf_counter

app = Flask(__name__)
#api = Api(app)
app.config['SECRET_KEY'] = 'secretkey'

class PredictForm(FlaskForm):
    #('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')
    variable1 = SelectField(u'Variable 1', choices=[('a', 'a'), ('b','b')], validators = [InputRequired()])
    variable2 = FloatField('Variable 2', validators = [InputRequired()])
    variable3 = FloatField('Variable 3', validators = [InputRequired()])
    variable4 = SelectField(u'Variable 4', choices=[('u','u'), ('y','y'), ('l','l')], validators = [InputRequired()])
    variable5 = SelectField(u'Variable 5', choices=[('g','g'), ('p','p'), ('gg','gg')], validators = [InputRequired()])
    variable6 = SelectField(u'Variable 6', choices=[('c','c'), ('k','k'), ('ff','ff'), ('i','i'), ('j','j'), ('q','q'), ('W','W'), ('d','d'), ('m','m'), ('cc','cc'), ('aa','aa'),('r','r'), ('x','x'), ('e','e')], validators = [InputRequired()])
    variable7 = SelectField(u'Variable 7', choices=[('v','v'), ('ff','ff'), ('o','o'), ('h','h'), ('j','j'), ('bb','bb') ,('n','n'), ('z','z'), ('dd','dd')])
    variable8 = FloatField('Variable 8', validators = [InputRequired()])
    variable9 = SelectField(u'Variable 9', choices=[('t','t') ,('f','f')], validators = [InputRequired()])
    variable10 = SelectField(u'Variable 10', choices=[('t','t') ,('f','f')], validators = [InputRequired()])
    variable11 = FloatField('Variable 11', validators = [InputRequired()])
    variable12 = SelectField(u'Variable 12', choices=[('t','t') ,('f','f')], validators = [InputRequired()])
    variable13 = SelectField(u'Variable 13', choices=[('g','g'), ('s','s'), ('p','p')], validators = [InputRequired()])
    variable14 = FloatField('Variable 14', validators = [InputRequired()])
    variable15 = FloatField('Variable 15', validators = [InputRequired()])
    variable17 = FloatField('Variable 17', validators = [InputRequired()])
    variable18 = SelectField(u'Variable 18',choices=[('t','t') ,('f','f')], validators = [InputRequired()])
    variable19 = SelectField(u'Variable 19', choices=[('1','1') ,('0','0')], validators = [InputRequired()])


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = PredictForm()
    if form.validate_on_submit():
        variable1 = form.variable1.data
        variable2 = form.variable2.data
        variable3 = form.variable3.data
        variable4 = form.variable4.data
        variable5 = form.variable5.data
        variable6 = form.variable6.data
        variable7 = form.variable7.data
        variable8 = form.variable8.data
        variable9 = form.variable9.data
        variable10 = form.variable10.data
        variable11 = form.variable11.data
        variable12 = form.variable12.data
        variable13 = form.variable13.data
        variable14 = form.variable14.data
        variable15 = form.variable15.data
        variable17 = form.variable17.data
        variable18 = form.variable18.data
        variable19 = form.variable19.data
        output = predict_app.Predict.predict([variable1,variable2, variable3, variable4,variable5, variable6, variable7, variable8, variable9, variable10, variable11, variable12, variable13, variable14, variable15, variable17, variable18, variable19])
        return render_template("form.html", form = form, output = output)

    return render_template("form.html", form = form)


#api.add_resource(Report, '/report/<string:filename>')

if __name__ == '__main__':
    app.run(debug = False, threaded=False)