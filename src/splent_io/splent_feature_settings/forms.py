from flask_wtf import FlaskForm
from wtforms import SubmitField


class SplentFeatureSettingsForm(FlaskForm):
    submit = SubmitField("Save splent_feature_settings")
