"""settings injects a single "Settings" entry into the admin sidebar, which
lists every feature that declared a settings schema (via register_settings).
"""

from flask import request, url_for

from splent_framework.hooks.template_hooks import register_template_hook


def settings_admin_link():
    active = (
        "active"
        if request.endpoint and request.endpoint.startswith("settings.admin")
        else ""
    )
    return (
        f'<li class="sidebar-item {active}">'
        f'<a class="sidebar-link" href="{url_for("settings.admin_index")}">'
        '<i class="align-middle" data-feather="settings"></i> '
        '<span class="align-middle">Settings</span>'
        "</a>"
        "</li>"
    )


register_template_hook("layout.authenticated_sidebar", settings_admin_link)
