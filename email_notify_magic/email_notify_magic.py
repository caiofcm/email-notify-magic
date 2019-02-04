from IPython.core.getipython import get_ipython
from IPython.core import magic_arguments
from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic, line_cell_magic)
import smtplib, ssl
import getpass


@magics_class
class EmailNotifier(Magics):

    session_password = ''


    @magic_arguments.magic_arguments()
    @magic_arguments.argument('fromemail', help='From email')
    @magic_arguments.argument('--to', '-t', help='To email - If not provied sender email is used.')
    @magic_arguments.argument('--subject', '-s', help='Email Subject',
        default='Jupyter Cell Completed'
    )
    @magic_arguments.argument('--body', '-b', help='Email Body message',
        default='The jupyter cell execution is completed.'
    )
    @magic_arguments.argument('--keep-password', '-k', help='Save password in the current jupyter session for latter usage', action='store_true')
    @line_cell_magic
    def email(self, line, cell=None):
        args = magic_arguments.parse_argstring(self.email, line)
        # fromemail = None
        # if args.fromemail:
        fromemail = args.fromemail
        toemail = fromemail
        if args.to:
            toemail = args.to
        subject = args.subject
        text_body = args.body

        if self.session_password == '':
            password = getpass.getpass("Type your password and press enter: ")
        else:
            password = self.session_password
        if args.keep_password:
            self.session_password = password
            # password = self.

        if cell is not None:
            output = get_ipython().run_cell(cell)
            # print(output.result)
            try: #Ref: https://github.com/ShopRunner/jupyter-notify/blob/master/jupyternotify/jupyternotify.py
                output_as_str = str(output.result)
            except ValueError:
                output_as_str = None # can't convert to string. Use default message
            if output_as_str is not None and output_as_str != 'None':
                text_body = 'Cell output: \n' + output_as_str
            send_email_gmail(fromemail, toemail, text_body, subject, password)

        return

def send_email_gmail(e_from, e_to, message_text = None, subject = None, password = None):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = e_from
    receiver_email = e_to
    if password is None:
        password = getpass.getpass("Type your password and press enter: ")
    if subject is None:
        subject = 'email from python script'
    if message_text is None:
        message_text = 'Email sent from python'
    msg = 'Subject: {}\n\n{}'.format(subject, message_text)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)
