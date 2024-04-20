# Single file QGIS plugin

Code to build a plugin for QGIS in a single file. 

Allows execution via the console (python) or in QGIS.

Base project: [QGIS minimal](https://github.com/wonder-sk/qgis-minimal-plugin/blob/master/README.md)


## Usage (QGIS - Linux)
- Create a new python plugin directory (e.g. `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/minimal`):
  - Copy `__init__.py` and `metadata.txt` to that directory

- Start QGIS and enable the plugin (menu Plugins > Manager and Install Plugins...)

- You should see a "| Go - Plugin |" button in your "Plugins" toolbar.

### Reload the plugin
- Install [Plugin Reloader](https://plugins.qgis.org/plugins/plugin_reloader/) plugin

### Usage (Python)
```
python3 __init__.py
```