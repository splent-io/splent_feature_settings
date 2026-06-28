from splent_framework.db import db


class Setting(db.Model):
    """A single runtime, admin-editable key/value setting (the WP-options
    analogue). Features read these via SettingsService / the {{ setting() }}
    template helper, falling back to product config and defaults."""

    __tablename__ = "setting"

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(191), nullable=False, unique=True, index=True)
    value = db.Column(db.Text, default="")

    def __repr__(self):
        return f"Setting<{self.key}>"
