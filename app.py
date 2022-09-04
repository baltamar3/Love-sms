import os

from chalice import Chalice, Rate
from chalicelib.sns import send_sms
from chalicelib.utils import get_random_compliment

app = Chalice(app_name="love-sms")


# Automatically runs every day
@app.schedule(Rate(1, unit=Rate.DAYS))
def send_sms_periodic_task(event):
    telephone = os.environ.get("RECEIVER_PHONE")
    msg = get_random_compliment()
    resp = send_sms(telephone, msg)
    return {"send_sms": resp}
