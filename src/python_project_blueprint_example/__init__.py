from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("python_project_blueprint_example")
except PackageNotFoundError:
    __version__ = "unknown"
