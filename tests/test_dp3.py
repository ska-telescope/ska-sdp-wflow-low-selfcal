# -*- coding: utf-8 -*-

"""Tests for the ska_sdp_wflow_low_selfcal module."""
from ska_sdp_wflow_low_selfcal.pipeline.dp3_helper import run_dp3
import os
import shutil
import uuid
from subprocess import check_call

import pytest

#TEST_DATA = "tests/test_data/"


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
    
    skymodel_path = f"{TEST_DATA}/grouped.skymodel"
    if not os.path.isfile(skymodel_path):
        raise IOError(
            f"Not able to find {skymodel_path} containing the reference solutions."
        )
    shutil.copy(skymodel_path, "grouped.skymodel")

    # Tests are executed here
    yield

    # Post-test: clean up
    os.chdir(CWD)
    #shutil.rmtree(tmpdir)

def test_pipeline_phaseonly():
    """Test DP3 phase only calibration"""
    run_dp3(f"{MSIN}", "calibrate_phaseonly")

    # assert that the h5parm is created and contains the right fields

    run_dp3(f"{MSIN}", "predict")

    assert True


def test_pipeline_complex():
    """Test DP3 calibration"""

    run_dp3(f"{MSIN}", "calibrate_scalarphase")
    run_dp3(f"{MSIN}", "calibrate_complexgain")

    # assert that the h5parm is created and contains the right fields

    run_dp3(f"{MSIN}", "predict")

    assert True
