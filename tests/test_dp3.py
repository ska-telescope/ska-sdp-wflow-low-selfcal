# -*- coding: utf-8 -*-

"""Tests for the ska_sdp_wflow_low_selfcal module."""


from ska_sdp_wflow_low_selfcal.pipeline.dp3_helper import (
    calibrate_complexgain,
    calibrate_scalarphase,
    predict,
)

MSIN = "tNDPPP-generic.MS"


def test_pipeline_phaseonly():
    """Test DP3 phase only calibration"""

    # Optional: read directions from skymodel
    directions = (
        "[[Patch_0],[Patch_1],[Patch_10],[Patch_11],[Patch_12],"
        "[Patch_13],[Patch_14],[Patch_15],[Patch_16],[Patch_17],[Patch_18],"
        "[Patch_19],[Patch_2],[Patch_20],[Patch_21],[Patch_22],[Patch_23],"
        "[Patch_24],[Patch_25],[Patch_26],[Patch_27],[Patch_3],[Patch_4],"
        "[Patch_5],[Patch_6],[Patch_7],[Patch_8],[Patch_9]]"
    )

    calibrate_scalarphase(
        f"{MSIN}",
        "29-Mar-2013/13:59:53.007",
        "grouped.skymodel",
        False,
        "fast_phase_0.h5parm",
    )

    # assert that the h5parm is created and contains the right fields
    assert True

    predict(
        f"{MSIN}",
        "29-Mar-2013/13:59:53.007",
        directions,
        "grouped.skymodel",
        "fast_phase_0.h5parm",
    )
    assert True


def test_pipeline_complex():
    """Test DP3 calibration"""
    # Optional: read directions from skymodel
    calibrate_scalarphase(
        f"{MSIN}",
        "29-Mar-2013/13:59:53.007",
        "grouped.skymodel",
        True,
        "fast_phase_0.h5parm",
    )

    # assert that the h5parm is created and contains the right fields
    assert True

    calibrate_complexgain(
        f"{MSIN}",
        "29-Mar-2013/13:59:53.007",
        "grouped.skymodel",
        "fast_phase_0.h5parm",
        "slow_gain_separate_0.h5parm",
    )

    # assert that the h5parm is created and contains the right fields
    assert True
