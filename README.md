# Email-Notify-Magic

Send an email after cell execution complete.

Obs: Currently only used with gmail.

## Install

```
pip install email-notify-magic
```

## Usage

- Load the magic extension:

```
%load_ext email_notify_magic
```

- Run the cell magic in jupyter notebook (see options bellow):

```
%%email email@gmail.com
```

- Insert password in the prompt and **done**

- Make sure your email account is enable for such usage (see [link](https://realpython.com/python-send-email/) and [less-secure-apps](https://myaccount.google.com/lesssecureapps)). It is recommend not to use personal accounts.

## Option:

- Sender and receiver same email address if `--to` is not supplied.

```
%%email email@gmail.com
```

- Set receiver with `--to` [`-t`]:

```
%%email email@gmail.com --to receiver@gmail.com
```

- Set e-mail subject `--subject` [`-s`]:

```
%%email email@gmail.com --s 'My subject'
```

- Set e-mail body `--body` [`-b`]:

```
%%email email@gmail.com --body 'From cell x'
```

Notice that the cell output is used if `--body` is not provided.

- Save password in jupyter session for latter usage `--keep-password` [`-k`]:

```
%%email email@gmail.com --body 'From cell x' -k
```

The next cell evoked with `%%email` will not require the password.


## Others

- Notification after cell execution inspired by [jupyter-notify](https://github.com/ShopRunner/jupyter-notify)
