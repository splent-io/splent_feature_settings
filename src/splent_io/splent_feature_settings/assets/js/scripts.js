// Entry point for splent_feature_settings frontend assets.
// Add your JavaScript here. Webpack compiles this into assets/dist/splent_feature_settings.bundle.js
//
// To load the compiled bundle in the product layout, register it in hooks.py:
//
//   from splent_framework.hooks.template_hooks import register_template_hook
//   from flask import url_for
//
//   def settings_scripts():
//       return '<script src="' + url_for("settings.assets", subfolder="dist", filename="splent_feature_settings.bundle.js") + '"></script>'
//
//   register_template_hook("layout.scripts", settings_scripts)
