"""VSCode Debugger Magic"""
__version__ = '1.2.0'

from .email_notify_magic import EmailNotifier

def load_ipython_extension(ipython):
    ipython.register_magics(EmailNotifier)
