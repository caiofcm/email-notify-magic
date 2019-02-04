# Vscode-Debugger-Magic

Attach a debugging session of visual studio code to the jupyter notebook

## Install

```
pip install vscode-debugger-magic
```

## Usage

- Load the magic extension:

```
%load_ext vscode_debugger_magic
```

- Run the magic in jupyter notebook

```
%vscodedebugger
```

- Activate the debugging session in Visual studio code in the Python attached mode:

```json
{
    "name": "Python: Attach",
    "type": "python",
    "request": "attach",
    "port": 5678,
    "host": "localhost"
},
```

- Set breakpoints in vscode
- Invoke functions to be debugged

## Option:

- `--timeout`or `-t` seconds: timeout to attach debugger

```
%vscodedebugger -t 10
```
