"""Email Notified Magic"""
__version__ = '0.0.2'

from .email_notify_magic import EmailNotifier
from .email_notify_magic import *

def load_ipython_extension(ipython):
    ipython.register_magics(EmailNotifier)
