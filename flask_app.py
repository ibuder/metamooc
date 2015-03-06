from flask import Flask, request, render_template
app = Flask('metamooc')

import wtforms.form
import wtforms.validators as validators
import wtforms.fields

class RecommendWeightForm(wtforms.form.Form):
    difficulty = wtforms.fields.DecimalField(u'Difficulty weight', [validators.required()])


@app.route("/", methods=['GET', 'POST'])
def recommend():
    form = RecommendWeightForm(request.form)
    if request.method == 'POST' and form.validate():
        return('Success!')
    return render_template('weight_form.html', form=form)

def hello():
    return "Hello MOOC World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
