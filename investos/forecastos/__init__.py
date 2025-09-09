import os

from investos.forecastos.exposure import *
from investos.forecastos.feature import *
from investos.forecastos.forecast import *
from investos.forecastos.global_utils import *
from investos.forecastos.provider import *

api_key = os.environ.get("FORECASTOS_API_KEY", "")
api_key_team = os.environ.get("FORECASTOS_API_KEY_TEAM", "")
api_endpoint = "https://app.forecastos.com/api/v1"
