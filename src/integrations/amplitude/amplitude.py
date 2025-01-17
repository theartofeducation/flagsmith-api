import urllib.parse

import requests

from integrations.common.wrapper import AbstractBaseIdentityIntegrationWrapper
import logging
from util.util import postpone

logger = logging.getLogger(__name__)

AMPLITUDE_API_URL = "https://api.amplitude.com"


class AmplitudeWrapper(AbstractBaseIdentityIntegrationWrapper):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.url = f"{AMPLITUDE_API_URL}/identify?api_key={self.api_key}"

    def _identify_user(self, user_data: dict) -> None:
        self.url = self.url + "&" + urllib.parse.urlencode(user_data)

        response = requests.post(self.url)
        logger.debug(
            "Sent event to Amplitude. Response code was: %s" % response.status_code
        )

    def generate_user_data(self, user_id, feature_states):
        return {
            "identification": {
                "user_id": user_id,
                "user_properties": {
                    feature_state.feature.name: feature_state.get_feature_state_value()
                    if feature_state.get_feature_state_value() is not None
                    else "None"
                    for feature_state in feature_states
                },
            }
        }
