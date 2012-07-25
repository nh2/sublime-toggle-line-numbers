Toggle Line Numbers
===================

Allows you to turn line numbers in the current buffer on/off.

DEPRECATED - READ THIS FIRST
----------------------------

This plugin has become redundant. You can get the same functionality by this simple `toggle_setting` keybinding:

```
  {"keys": ["ctrl+k", "ctrl+n"], "command": "toggle_setting", "args": {"setting": "line_numbers"} }
```

See http://www.sublimetext.com/docs/2/settings.html for documentation.

Below are the original README contents:

Setup
-----

Add this to your keybindings:

```
  { "keys": ["ctrl+k", "ctrl+n"], "command": "toggle_line_numbers" }
```

Now you can toggle line numbers with *Ctrl-K-N*.
