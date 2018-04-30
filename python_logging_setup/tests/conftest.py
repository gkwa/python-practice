import pytest
import logging
import sys
import os.path

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '..', 'src')
    ))
import util


@pytest.fixture()
def setup_logging():
    util.setup_logging(
        default_path=os.path.join(
            os.path.dirname(__file__), '..', 'logging.json')
    )

    logging.info("ok")

    yield

    logging.error("uh oh")
