"""Tests for the ska_sdp_wflow_low_selfcal module."""
import shutil

import pytest

from ska_sdp_wflow_low_selfcal.pipeline.wsclean_helper import WSCleanRunner

MSIN = "tNDPPP-generic.MS"
PATH_TO_WSCLEAN_EXE = "/home/csalvoni/scratch/schaap/wsclean/build/wsclean"


@pytest.fixture(autouse=True)
def is_wsclean_installed():
    """Check if WSClean is installed, and skip test if not"""
    if shutil.which(PATH_TO_WSCLEAN_EXE) is None:
        pytest.skip("Skipping test as WSClean is not installed")


def test_wsclean(create_environment):  # pylint: disable=W0613
    """Test wsclean imaging"""
    wsclean_runner = WSCleanRunner(PATH_TO_WSCLEAN_EXE)
    wsclean_runner.run_wsclean(f"{MSIN}", "facets.reg", "solutions.h5parm")

    # assert that the output fits are created and contains the right fields

    assert True
