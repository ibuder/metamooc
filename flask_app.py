from flask import Flask, request, render_template
app = Flask('metamooc')

import wtforms.form
import wtforms.validators as validators
import wtforms.fields
import babel
import numpy as np

import features
cf = features.CourseraFeatures()  # Global db cache


def map_lang_form(langs):
    """
    Utility to map a list of language codes to (code, human-readable) pairs
    """
    def pair_builder(lang):
        loc = babel.Locale.parse(lang.replace('_', '-'), sep='-')
        return (lang, loc.english_name + ' (' + loc.get_language_name() + ')',)

    return map(pair_builder, langs)


class RecommendWeightForm(wtforms.form.Form):
    average_hours = wtforms.fields.FloatField(u'Workload', [validators.InputRequired()])
    targetAudience = wtforms.fields.FloatField(u'Difficulty', [validators.InputRequired()])
    n_rating = wtforms.fields.FloatField(u'Popularity', [validators.required()])
    subtitle_lang = wtforms.fields.SelectField(u'Subtitle language', 
        [validators.optional()], choices=map_lang_form(cf.subtitle_languages().columns))
    subtitle_weight = wtforms.fields.FloatField(u'Subtitle importance',
        [validators.optional()], default=0.0)

@app.route("/", methods=['GET', 'POST'])
def recommend():
    form = RecommendWeightForm(request.form)
    if request.method == 'POST' and form.validate():
        theta = {}  # User preferences
        theta[form.subtitle_lang.data] = form.subtitle_weight.data
        theta[u'average_hours'] = form.average_hours.data
        theta[u'targetAudience'] = form.targetAudience.data
        theta[u'n_rating'] = form.n_rating.data
        print theta
        r = cf.recommend_content_based(theta, n_courses=10)
        # Jinja has trouble with DataFrame, so get the values we want to display
        recommendations = [ (r.loc[i, 'name'].decode('utf-8'), r.loc[i, 'score'],) for i in r.index]
        return render_template('weight_form.html', form=form, recommendations=recommendations)
    return render_template('weight_form.html', form=form)

def hello():
    return "Hello MOOC World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
