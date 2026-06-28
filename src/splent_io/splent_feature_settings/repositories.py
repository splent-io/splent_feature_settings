from splent_io.splent_feature_settings.models import Setting
from splent_framework.repositories.BaseRepository import BaseRepository


class SettingsRepository(BaseRepository):
    def __init__(self):
        super().__init__(Setting)
