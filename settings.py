# -*- coding: utf-8 -*-

import json

class SettingsException(Exception):
    pass

class Settings():
    '''Stores the crawlers general configs'''

    def __init__(self):
        self.__facebook_token = None

    @property
    def facebook_access_token(self):
        with open('settings.json','r') as settings_file:
            settings_json = json.load(settings_file)
            self.__facebook_token = settings_json['facebook_access_token']
            settings_file.close()

        if not self.__facebook_token:
            raise SettingsException('The facebook access token sould not be None.')

        return self.__facebook_token