"""Tests for the ska_sdp_wflow_low_selfcal module."""
from ska_sdp_wflow_low_selfcal.pipeline.wsclean_helper import run_wsclean

MSIN = "tNDPPP-generic.MS"


def test_wsclean(create_environment):  # pylint: disable=W0613
    """Test wsclean imaging"""
    run_wsclean(f"{MSIN}")

    # assert that the output fits are created and contains the right fields

    assert True
