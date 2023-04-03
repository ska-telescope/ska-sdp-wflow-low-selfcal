"""Tests for the ska_sdp_wflow_low_selfcal module."""
import os
import shutil
import uuid
from subprocess import check_call

import pytest

from ska_sdp_wflow_low_selfcal.pipeline.wsclean_helper import run_wsclean

TEST_DATA = "/home/csalvoni/schaap/ska-sdp-wflow-low-selfcal/ska-sdp-wflow-low-selfcal/tests/test_data"
MSIN = "tNDPPP-generic.MS"
CWD = os.getcwd()


@pytest.fixture(autouse=True)
def source_env():
    os.chdir(CWD)
    tmpdir = str(uuid.uuid4())
    os.mkdir(tmpdir)
    os.chdir(tmpdir)
    source = f"{TEST_DATA}/{MSIN}.tgz"
    if not os.path.isfile(source):
        raise IOError(
            f"Not able to find {source} containing the reference solutions."
        )
    check_call(["tar", "xf", source])

    # Tests are executed here
    yield

    # Post-test: clean up
    os.chdir(CWD)
    shutil.rmtree(tmpdir)


def test_wsclean():
    """Test wsclean imaging"""
    run_wsclean(f"{MSIN}")

    # assert that the output fits are created and contains the right fields

    assert True
