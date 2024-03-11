"""
Write a program that logs messages by sending them to an email account. Use SMTP handler.
"""

import logging
import os
from logging import handlers as h
# configure the SMTP Handler with your SMTP server settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'rajakshat7985@gmail.com'
smtp_password = os.environ.get('SMTP')
from_addr = 'rajakshat7985@gmail.com'
to_addr = 'clarkfirth72@gmail.com'
subject = 'Error from application'


smtp_handler = h.SMTPHandler(mailhost=smtp_server,
                             fromaddr=from_addr,
                             toaddrs=to_addr,
                             subject=subject,
                             credentials=(smtp_username, smtp_password))
smtp_handler.secure = ()

smtp_handler.setLevel(logging.ERROR)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
smtp_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(smtp_handler)


logger.error('this is testing message error')
