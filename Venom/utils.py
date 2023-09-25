import sys
import logging
import importlib
from telethon import events
from pathlib import Path
import inspect
import re

def load_plugins(plugin_name):
    path = Path(f"Venom/plugins/{plugin_name}.py")
    name = "Venom.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["Venom.plugins." + plugin_name] = load
    print("🔥 Imported Successfully ⚡ " + plugin_name)
