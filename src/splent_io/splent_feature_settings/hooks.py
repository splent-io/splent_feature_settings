"""
Template hooks for splent_feature_settings.

Register hooks here to inject HTML into the product's layout slots.
Only register layout.scripts if this feature has compiled frontend assets.

Examples:

    from splent_framework.hooks.template_hooks import register_template_hook
    from flask import render_template, url_for

    # Inject a sidebar fragment
    def my_sidebar():
        return render_template("hooks/sidebar_items.html")

    register_template_hook("layout.authenticated_sidebar", my_sidebar)

    # Inject the compiled JS bundle (only if assets/dist/ exists)
    def settings_scripts():
        return (
            '<script src="'
            + url_for("settings.assets", subfolder="dist", filename="splent_feature_settings.bundle.js")
            + '"></script>'
        )

    register_template_hook("layout.scripts", settings_scripts)
"""
