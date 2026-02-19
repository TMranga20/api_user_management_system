import pytest

def pytest_configure(config):
    config._metadata["Project Name"] = "ReqRes API Automation"
    config._metadata["Tester"] = "Mohan"
    config._metadata["Environment"] = "QA"
