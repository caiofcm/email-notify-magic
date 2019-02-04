"""Email Notified Magic"""
__version__ = '0.0.1'

from .email_notify_magic import EmailNotifier

def load_ipython_extension(ipython):
    ipython.register_magics(EmailNotifier)
