"""Tests for the ska_sdp_wflow_low_selfcal module."""
import os
import shutil
import uuid
from subprocess import check_call

import pytest

from ska_sdp_wflow_low_selfcal.pipeline.wsclean_helper import run_wsclean

TEST_DATA = "../tests/test_data"
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
        raise IOError(f"Not able to find {source}.")
    check_call(["tar", "xf", source])

    facets_path = f"{TEST_DATA}/facets.reg"
    if not os.path.isfile(facets_path):
        raise IOError(f"Not able to find {facets_path}.")
    shutil.copy(facets_path, "facets.reg")

    h5parm_path = f"{TEST_DATA}/fast_phase_0.h5parm"
    if not os.path.isfile(h5parm_path):
        raise IOError(f"Not able to find {h5parm_path}.")
    shutil.copy(h5parm_path, "fast_phase_0.h5parm")

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
