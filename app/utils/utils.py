from flask import current_app

class Utils():

    @staticmethod
    def get_api_url():
        api_url = current_app.config['API_DATA_CENTER']

        return api_url