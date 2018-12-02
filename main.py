# [START gae_python37_app]

from logzero import logger
import uuid
import json


if __name__ == '__main__':
    user_id = uuid.uuid4()
    logger.info('consumer data from Report Users, promotion available, now send function to notificated USER {}'.format(user_id))


