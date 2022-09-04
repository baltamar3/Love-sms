import os

from chalice import Chalice, Rate
from chalicelib.sns import send_sms
from chalicelib.utils import get_random_compliment

app = Chalice(app_name="love-sms")
