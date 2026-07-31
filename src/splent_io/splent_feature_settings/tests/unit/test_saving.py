"""What the panel stores when somebody presses Save.

The form arrives filled in with what is in force, which for a field nobody
has touched is the value the product set in its environment. Storing that
back would freeze it: a later change to the .env would be shadowed forever
by a copy nobody remembers making, and the file would stop being the truth
about a setting it appears to state.

So a field submitted unchanged is stored empty, which the resolver reads as
"whatever the environment says".
"""

from splent_io.splent_feature_settings.routes import _as_form_value


class TestTellingLeftAloneFromTypedTheSame:
    def test_a_bool_from_the_environment_is_compared_as_the_form_sends_it(self):
        """config.py has already turned the variable into a Python bool by
        the time this runs, while the form posts "1" and "0"."""
        field = {"key": "nav", "type": "bool"}

        assert _as_form_value(field, True) == "1"
        assert _as_form_value(field, False) == "0"

    def test_a_bool_still_written_as_a_word_is_understood(self):
        """A product may set SEARCH_NAV=true and a feature may pass it
        through without casting."""
        field = {"key": "nav", "type": "bool"}

        assert _as_form_value(field, "true") == "1"
        assert _as_form_value(field, "0") == "0"

    def test_an_int_is_compared_as_text(self):
        field = {"key": "limit", "type": "int"}

        assert _as_form_value(field, 20) == "20"

    def test_text_is_stripped_the_way_the_form_strips_it(self):
        """Otherwise a trailing space in the .env would read as an edit."""
        field = {"key": "placeholder", "type": "text"}

        assert _as_form_value(field, "  Buscar aquí ") == "Buscar aquí"
