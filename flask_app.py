from flask import Flask, request, render_template
app = Flask('metamooc')

import wtforms.form
import wtforms.validators as validators
import wtforms.fields
import babel

import features
cf = features.CourseraFeatures()


def map_lang_form(langs):
    """
    Utility to map a list of language codes to (code, human-readable) pairs
    """
    def pair_builder(lang):
        loc = babel.Locale.parse(lang.replace('_', '-'), sep='-')
        return (lang, loc.english_name + ' (' + loc.get_language_name() + ')',)

    return map(pair_builder, langs)


class RecommendWeightForm(wtforms.form.Form):
    average_hours = wtforms.fields.DecimalField(u'Time commitment', [validators.required()])
    targetAudience = wtforms.fields.DecimalField(u'Difficulty', [validators.required()])
    n_rating = wtforms.fields.DecimalField(u'Popularity', [validators.required()])
    subtitle_lang = wtforms.fields.SelectField(u'Subtitle language', 
        [validators.optional()], choices=map_lang_form(cf.subtitle_languages().columns))
    subtitle_weight = wtforms.fields.DecimalField(u'Subtitle importance',
        [validators.optional()], default=0.0)

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
