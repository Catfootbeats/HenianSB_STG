import os.path as _path
import toml as _toml
import sys as _sys

if getattr(_sys, 'frozen', False) and hasattr(_sys, '_MEIPASS'):
    __is_pyinstaller__ = True
    __pyproject__ = _toml.load(_path.abspath(_path.join(_path.dirname(__file__), "../_pkg/pyproject.toml")))
else:
    __is_pyinstaller__ = False
    __pyproject__ = _toml.load(_path.abspath(_path.join(_path.dirname(__file__), "../../pyproject.toml")))

__resource_path__ = _path.abspath(_path.join(_path.dirname(__file__), "../resources/"))
__version__ = __pyproject__["project"]["version"]
