# settings has no routes of its own: it is the key/value store. Other features
# (theme's Appearance editor, the captcha panels, …) provide their own admin
# panels and read/write via SettingsService and the {{ setting() }} helper.
from splent_io.splent_feature_settings import settings_bp  # noqa: F401
