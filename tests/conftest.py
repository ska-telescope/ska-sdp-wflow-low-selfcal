""" In this module all the fixture to run the python tests are defined """
import os
import shutil
from subprocess import check_call

import pytest

TEST_DATA = "/home/csalvoni/schaap/ska-sdp-wflow-low-selfcal-branch/\
ska-sdp-wflow-low-selfcal/tests/test_data"

CWD = os.getcwd()


@pytest.fixture(autouse=False, name="create_environment")
def source_env(tmp_path, run_dp3=True, run_wsclean=True):
    """Define a temporary folder to run the test. The folder is deleted
    once the test has been run"""
    os.chdir(tmp_path)

    ms_name = "tNDPPP-generic.MS"
    source = f"{TEST_DATA}/{ms_name}.tgz"
    if not os.path.isfile(source):
        raise IOError(f"Not able to find {source}.")
    check_call(["tar", "xf", source])
    # untar_ms(f"{tcf.RESOURCEDIR}/{MSIN}.tgz")
    check_call(["tar", "xf", source])

    if run_dp3:
        copy_data_dp3()
    if run_wsclean:
        copy_data_wsclean()
    # Tests are executed here
    yield

    # Post-test: clean up
    os.chdir(CWD)


@pytest.fixture(autouse=False, name="create_environment_support_functions")
def source_env_support_functions(tmp_path):
    """Define a temporary folder to run the test. The folder is deleted
    once the test has been run"""
    os.chdir(tmp_path)

    copy_data_support_functions()
    # Tests are executed here
    yield

    # Post-test: clean up
    os.chdir(CWD)


def copy_data_support_functions():
    """Copy data needed for tests into temporary folder"""
    files_to_copy = [
        "facets.reg",
        "fast_phase_0.h5parm",
        "grouped.skymodel",
        "sector_1_vertices.pkl",
        "sector_1-sources-pb.txt",
    ]
    for filename in files_to_copy:
        file_path = f"{TEST_DATA}/{filename}"
        if not os.path.isfile(file_path):
            raise IOError(f"Not able to find {file_path}.")
        shutil.copy(file_path, filename)


def copy_data_dp3():
    """Copy data needed for DP3 tests into temporary folder"""
    skymodel_path = f"{TEST_DATA}/grouped.skymodel"
    if not os.path.isfile(skymodel_path):
        raise IOError(f"Not able to find {skymodel_path}.")
    shutil.copy(skymodel_path, "grouped.skymodel")


def copy_data_wsclean():
    """Copy data needed for WSClean tests into temporary folder"""
    facets_path = f"{TEST_DATA}/facets.reg"
    if not os.path.isfile(facets_path):
        raise IOError(f"Not able to find {facets_path}.")
    shutil.copy(facets_path, "facets.reg")

    h5parm_path = f"{TEST_DATA}/fast_phase_0.h5parm"
    if not os.path.isfile(h5parm_path):
        raise IOError(f"Not able to find {h5parm_path}.")
    shutil.copy(h5parm_path, "fast_phase_0.h5parm")
