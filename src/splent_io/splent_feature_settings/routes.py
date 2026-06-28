"""Generic admin panels for feature settings.

Any feature that declares a settings schema (via the framework's
register_settings) gets an admin panel here automatically — one page per
feature — that reads/writes through SettingsService. No per-feature panel code.
"""

from flask import abort, flash, redirect, render_template, request, url_for
from flask_login import login_required

from splent_io.splent_feature_settings import settings_bp
from splent_framework.services.service_locator import service_proxy
from splent_framework.settings.settings_schema import (
    get_config,
    get_schema,
    get_schemas,
    setting_key,
)


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
        values = {}
        for f in schema["fields"]:
            key = setting_key(feature, f["key"])
            if f["type"] == "bool":
                values[key] = "1" if f["key"] in request.form else "0"
            else:
                values[key] = (request.form.get(f["key"]) or "").strip()
        service_proxy("SettingsService").set_many(values)
        flash(f"{schema['title']} settings saved.", "success")
        return redirect(url_for("settings.admin_feature", feature=feature))
    return render_template(
        "settings/admin/feature.html", schema=schema, cfg=get_config(feature)
    )
