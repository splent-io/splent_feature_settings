"""
Functional tests for splent_feature_settings.

Functional tests use Flask's test client to exercise full HTTP
request/response cycles (GET, POST, redirects, rendered HTML).

The scaffolded version of this file probed "/settings", which this
feature has never served: settings are edited from the back-office. The
routes asserted here are the ones the contract actually declares.
"""


def test_settings_screen_is_registered(test_client):
    """Anonymous callers are sent to login rather than getting a 404."""
    response = test_client.get("/admin/settings")
    assert response.status_code in (200, 302)


def test_per_feature_settings_screen_is_registered(test_client):
    response = test_client.get("/admin/settings/theme")
    assert response.status_code in (200, 302)
