# [START gae_python37_app]

from logzero import logger
import uuid
import json
import requests


def send_notification_from_function():
    try:
        request_call_function = requests.post("https://us-central1-pocprojetcintegratorfinal.cloudfunctions.net/notification").json()
        logger.info("calling from function notification")
        data_function = {
            "status_code": request_call_function.status_code,
            "data": json.loads(request_call_function.text)
        }
        return json.dumps(data_function)
    except Exception as ex:
        logger.warning(str(ex))
        return


if __name__ == '__main__':
    call = uuid.uuid4()
    logger.info('consumer data from Report Users, promotion available, now send function to notificated USER {}'.format(call))
    send_notification_from_function()


