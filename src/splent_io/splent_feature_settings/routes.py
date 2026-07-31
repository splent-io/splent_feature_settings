"""Generic admin panels for feature settings.

Any feature that declares a settings schema (via the framework's
register_settings) gets an admin panel here automatically — one page per
feature — that reads/writes through SettingsService. No per-feature panel code.
"""

from flask import (
    abort,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required

from splent_io.splent_feature_settings import settings_bp
from splent_framework.services.service_locator import service_proxy
from splent_framework.settings.settings_schema import (
    get_config,
    get_schema,
    get_schemas,
    setting_key,
)


def _as_form_value(field: dict, value) -> str:
    """A configured value written the way the form submits it.

    Needed to tell "left alone" from "typed the same thing": app.config
    holds a real bool where the form posts "1" or "0", and an int where the
    form posts a string.
    """
    if field["type"] == "bool":
        return "1" if value in (True, "1", 1, "true", "True") else "0"
    return str(value).strip()


@settings_bp.route("/admin/settings", methods=["GET"])
@login_required
def admin_index():
    return render_template("settings/admin/index.html", schemas=get_schemas())


@settings_bp.route("/admin/settings/<feature>", methods=["GET", "POST"])
@login_required
def admin_feature(feature):
    schema = get_schema(feature)
    if schema is None:
        abort(404)
    if request.method == "POST":
        # The form is filled in with what is in force, which for an untouched
        # field is the value the product set in its environment. Storing that
        # back would freeze it: a later change to the .env would be shadowed
        # by a copy nobody remembers making. So a field submitted unchanged
        # is stored empty, which means "whatever the environment says".
        from splent_framework.settings.settings_schema import env_key

        environment = current_app.config
        values = {}
        for f in schema["fields"]:
            key = setting_key(feature, f["key"])
            if f["type"] == "bool":
                submitted = "1" if f["key"] in request.form else "0"
            else:
                submitted = (request.form.get(f["key"]) or "").strip()

            from_env = environment.get(env_key(feature, f))
            if from_env is not None and submitted == _as_form_value(f, from_env):
                submitted = ""
            values[key] = submitted

        service_proxy("SettingsService").set_many(values)
        flash(f"{schema['title']} settings saved.", "success")
        return redirect(url_for("settings.admin_feature", feature=feature))
    return render_template(
        "settings/admin/feature.html",
        schema=schema,
        cfg=get_config(feature),
        sources=_sources(schema),
    )


def _sources(schema: dict) -> dict:
    """Where each field's current value is coming from.

    A box showing something nobody in this panel typed is a mystery
    otherwise, and the answer is usually the product's own configuration.
    """
    from splent_framework.settings.settings_schema import env_key

    stored = service_proxy("SettingsService").all_dict()
    out = {}
    for f in schema["fields"]:
        if stored.get(setting_key(schema["feature"], f["key"])):
            out[f["key"]] = "panel"
        elif current_app.config.get(env_key(schema["feature"], f)) not in (None, ""):
            out[f["key"]] = "environment"
        else:
            out[f["key"]] = "default"
    return out
