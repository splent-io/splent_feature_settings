from splent_io.splent_feature_settings.models import Setting
from splent_io.splent_feature_settings.repositories import SettingsRepository
from splent_framework.db import db
from splent_framework.services.BaseService import BaseService


class SettingsService(BaseService):
    """Runtime key/value settings, editable from the admin (WP-options style)."""

    def __init__(self):
        super().__init__(SettingsRepository())

    def get(self, key, default=None):
        s = Setting.query.filter_by(key=key).first()
        if s is None or s.value in (None, ""):
            return default
        return s.value

    def set(self, key, value):
        s = Setting.query.filter_by(key=key).first()
        if s is None:
            s = Setting(key=key, value=value or "")
            db.session.add(s)
        else:
            s.value = value or ""
        db.session.commit()
        return s

    def set_many(self, mapping):
        for key, value in mapping.items():
            s = Setting.query.filter_by(key=key).first()
            if s is None:
                db.session.add(Setting(key=key, value=value or ""))
            else:
                s.value = value or ""
        db.session.commit()

    def all_dict(self):
        return {s.key: s.value for s in Setting.query.all()}
