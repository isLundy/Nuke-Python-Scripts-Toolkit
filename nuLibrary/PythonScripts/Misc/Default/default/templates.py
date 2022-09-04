"""This module contains template xml values."""


# Import built-in modules
import os

# Root directory of this tool
TOOLS_ROOT = os.path.dirname(os.path.dirname(__file__))

# Settings xml template
SETTINGS = """<?xml version='1.0' encoding='utf-8'?>
<defaultSettings>
  <set name="cur_preset">custom.xml</set>
  <set name="presets_path">{}/presets</set>
</defaultSettings>
""".format(TOOLS_ROOT)

# Knob defualts xml template
KNOB_DEFAULTS = """<?xml version='1.0' encoding='utf-8'?>
<defaults>
</defaults>"""
