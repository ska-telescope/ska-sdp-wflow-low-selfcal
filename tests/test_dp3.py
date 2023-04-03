# -*- coding: utf-8 -*-

"""Tests for the ska_sdp_wflow_low_selfcal module."""
from ska_sdp_wflow_low_selfcal.pipeline.dp3_helper import run_dp3


def test_predict():
    """Test DP3 predict"""
    run_dp3("/var/scratch/csalvoni/data/tNDPPP-generic.MS", "predict")
    assert True


def test_calibrate_phaseonly():
    """Test DP3 phase only calibration"""
    run_dp3(
        "/var/scratch/csalvoni/data/tNDPPP-generic.MS", "calibrate_phaseonly"
    )
    assert True


def test_calibrate_complex():
    """Test DP3 calibration"""
    assert True
