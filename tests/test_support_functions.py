"""Tests for the ska_sdp_wflow_low_selfcal module."""
import os.path

import h5py
import numpy as np
from astropy.coordinates import Angle

from ska_sdp_wflow_low_selfcal.pipeline.support.H5parm_collector import (
    collect_h5parms,
)
from ska_sdp_wflow_low_selfcal.pipeline.support_functions import (
    download_skymodel,
)


def test_download_skymodel():
    """Test the download skymodel given a ra,dec direction"""
    ra = "01h37m41.299"  # pylint: disable=C0103
    dec = "+033d09m35.132"
    if isinstance(ra, str):
        ra = Angle(ra).to("deg").value  # pylint: disable=C0103
    if isinstance(dec, str):
        dec = Angle(dec).to("deg").value

    download_skymodel(ra, dec, "test.skymodel")
    assert os.path.isfile("test.skymodel")


def test_collect_h5():
    """Test the combination of multiple h5 files into one"""
    working_dir = "/var/scratch/csalvoni/rapthor_working_dir/chiara/outputs"

    h5_list = [
        f"{working_dir}/out_calibration_1_fast_phase_0.h5parm",
        f"{working_dir}/out_calibration_1_fast_phase_1.h5parm",
        f"{working_dir}/out_calibration_1_fast_phase_2.h5parm",
        f"{working_dir}/out_calibration_1_fast_phase_3.h5parm",
    ]

    combined_filename = "merged.h5parm"
    collect_h5parms(h5_list, "merged.h5parm", clobber=True)

    combined = h5py.File(combined_filename, "r")
    first = 0
    last = 75

    for single_h5 in h5_list:
        assert np.allclose(
            h5py.File(single_h5, "r")["sol000/phase000/val"][
                first:last, :, :, 0
            ],
            combined["sol000/phase000/val"][first:last, :, :, 0],
        )
        assert np.allclose(
            h5py.File(single_h5, "r")["sol000/phase000/val"][
                first:last, :, :, 1
            ],
            combined["sol000/phase000/val"][first:last, :, :, 2],
        )
        assert np.allclose(
            h5py.File(single_h5, "r")["sol000/phase000/val"][
                first:last, :, :, 2
            ],
            combined["sol000/phase000/val"][first:last, :, :, 1],
        )
        assert np.allclose(
            h5py.File(single_h5, "r")["sol000/phase000/val"][
                first:last, :, :, 3:9
            ],
            combined["sol000/phase000/val"][first:last, :, :, 3:9],
        )
        first = +75
        last = +75
