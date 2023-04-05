""" In this module all the fixture to run the python tests are defined """
import os
import shutil
import uuid
from subprocess import check_call

import pytest

TEST_DATA = "../tests/test_data"


@pytest.fixture(scope="session", autouse=False, name="create_environment")
def source_env(run_dp3=True, run_wsclean=True):
    """Define a temporary folder to run the test. The folder is deleted
    once the test has been run"""

    ms_name = "tNDPPP-generic.MS"
    current_directory = os.getcwd()

    os.chdir(current_directory)
    tmpdir = str(uuid.uuid4())
    os.mkdir(tmpdir)
    os.chdir(tmpdir)
    source = f"{TEST_DATA}/{ms_name}.tgz"
    if not os.path.isfile(source):
        raise IOError(f"Not able to find {source}.")
    check_call(["tar", "xf", source])

    if run_dp3:
        copy_data_dp3()
    if run_wsclean:
        copy_data_wsclean()
    # Tests are executed here
    yield

    # Post-test: clean up
    os.chdir(current_directory)
    shutil.rmtree(tmpdir)


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
