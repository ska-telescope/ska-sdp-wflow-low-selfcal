# -*- coding: utf-8 -*-

"""Tests for the single steps."""


from ska_sdp_wflow_low_selfcal.pipeline.dp3_helper import Dp3Runner
from ska_sdp_wflow_low_selfcal.pipeline.operations import (
    calibrate_1,
    calibrate_2,
    calibrate_3,
    image_1,
    predict_1,
)
from ska_sdp_wflow_low_selfcal.pipeline.wsclean_helper import WSCleanRunner

PATH_TO_DP3_EXE = "/home/csalvoni/scratch/schaap/dp3/build/DP3"
PATH_TO_WSCLEAN_EXE = "/home/csalvoni/scratch/schaap/wsclean/build/wsclean"


def test_calibrate_1():
    """Test calibrate_1"""
    dp3_runner = Dp3Runner(PATH_TO_DP3_EXE)
    calibrate_1(dp3_runner)


def test_calibrate_2():
    """Test calibrate_2"""
    dp3_runner = Dp3Runner(PATH_TO_DP3_EXE)
    calibrate_2(dp3_runner)


def test_predict_1():
    """Test predict_1"""
    dp3_runner = Dp3Runner(PATH_TO_DP3_EXE)
    predict_1(dp3_runner)


def test_image_1():
    """Test image_1"""
    dp3_runner = Dp3Runner(PATH_TO_DP3_EXE)
    wsclean_runner = WSCleanRunner(PATH_TO_WSCLEAN_EXE)
    image_1(
        dp3_runner,
        wsclean_runner,
        "tests/test_data/field-solutions_calibration_2.h5",
    )


def test_calibrate_3():
    """Test calibrate_3"""
    dp3_runner = Dp3Runner(PATH_TO_DP3_EXE)
    calibrate_3(
        dp3_runner,
    )
