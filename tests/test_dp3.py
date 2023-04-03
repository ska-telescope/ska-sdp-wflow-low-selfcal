# -*- coding: utf-8 -*-

"""Tests for the ska_sdp_wflow_low_selfcal module."""
from ska_sdp_wflow_low_selfcal.pipeline.dp3_helper import run_dp3

TEST_DATA="tests/test_data/"

def test_pipeline_phaseonly():
    """Test DP3 phase only calibration"""
    run_dp3(f"{TEST_DATA}/tNDPPP-generic.MS", "calibrate_phaseonly")

    # assert that the h5parm is created and contains the right fields

    run_dp3(f"{TEST_DATA}/tNDPPP-generic.MS", "predict")

    assert True


def test_pipeline_complex():
    """Test DP3 calibration"""

    run_dp3(f"{TEST_DATA}/tNDPPP-generic.MS", "calibrate_scalarphase")
    run_dp3(f"{TEST_DATA}/tNDPPP-generic.MS", "calibrate_complexgain")

    # assert that the h5parm is created and contains the right fields


    run_dp3(f"{TEST_DATA}/tNDPPP-generic.MS", "predict")

    assert True
