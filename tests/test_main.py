import runpy
import sys


def test_main_runs_as_script(monkeypatch):
    """
    Ensure the module runs correctly when executed as __main__
    and cover the __main__ guard branch.
    Suppresses the runpy import warning by removing the module first.
    """

    # Patch setup_logging to avoid side effects
    monkeypatch.setattr("python_project_blueprint_example.main.setup_logging", lambda *args, **kwargs: None)

    # Remove the already imported module to avoid warnings
    sys.modules.pop("python_project_blueprint_example.main", None)

    # Execute as if run via `python -m python_project_blueprint_example.main`
    runpy.run_module("python_project_blueprint_example.main", run_name="__main__")
