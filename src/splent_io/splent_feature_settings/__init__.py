from splent_framework.blueprints.base_blueprint import create_blueprint
from splent_framework.services.service_locator import register_service, service_proxy

from splent_io.splent_feature_settings.services import SettingsService

settings_bp = create_blueprint(__name__)


def init_feature(app):
    register_service(app, "SettingsService", SettingsService)


def inject_context_vars(app):
    # {{ setting('key', default) }} — read a runtime, admin-editable setting,
    # falling back to the given default. Safe to call even mid-request.
    def setting(key, default=""):
        try:
            return service_proxy("SettingsService").get(key, default)
        except Exception:
            return default

    return {"setting": setting}
