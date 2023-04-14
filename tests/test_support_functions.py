"""Tests for the ska_sdp_wflow_low_selfcal module."""
import os.path

import h5py
import numpy as np
from astropy.coordinates import Angle

from ska_sdp_wflow_low_selfcal.pipeline.support.blank_image import blank_image
from ska_sdp_wflow_low_selfcal.pipeline.support.combine_h5parms import (
    combine_h5parms,
)
from ska_sdp_wflow_low_selfcal.pipeline.support.filter_skymodel import (
    filter_skymodel,
)
from ska_sdp_wflow_low_selfcal.pipeline.support.H5parm_collector import (
    collect_h5parms,
)
from ska_sdp_wflow_low_selfcal.pipeline.support_functions import (
    download_skymodel,
)


def test_download_skymodel(
    create_environment_support_functions,
):  # pylint: disable=W0613
    """Test the download skymodel given a ra,dec direction"""
    ra = "01h37m41.299"  # pylint: disable=C0103
    dec = "+033d09m35.132"
    if isinstance(ra, str):
        ra = Angle(ra).to("deg").value  # pylint: disable=C0103
    if isinstance(dec, str):
        dec = Angle(dec).to("deg").value

    download_skymodel(ra, dec, "test.skymodel")
    assert os.path.isfile("test.skymodel")


def test_collect_h5(
    create_environment_support_functions,
):  # pylint: disable=W0613
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


def test_combine_h5(
    create_environment_support_functions,
):  # pylint: disable=W0613
    """Check that two H5 files are correclty combined"""
    working_dir = "/var/scratch/csalvoni/rapthor_working_dir/chiara/outputs"
    combine_h5parms(
        f"{working_dir}/out_calibration_3_fast_phase_0.h5parm",
        f"{working_dir}/out_calibration_3_slow_gain_separate_0.h5parm",
        "combined.h5parm",
        "p1p2a2_scalar",
        solset1="sol000",
        solset2="sol000",
        reweight=False,
        cal_names="Patch_1022,Patch_1042,Patch_1075,Patch_136,Patch_151,\
        Patch_152,Patch_231,Patch_235,Patch_313,Patch_34,Patch_341,Patch_375,\
        Patch_423,Patch_456,Patch_47,Patch_479,Patch_51,Patch_809,Patch_865,\
        Patch_900",
        cal_fluxes="1.1334742100000001,1.70710925,3.2476566,5.00693068,\
        1.122316848,3.2364227,0.656659973,4.06428878,1.96108164,1.32103399,\
        1.5094014900000001,0.9435658,0.88880649,0.812606685,\
        6.2081472699999996,1.89063376,1.1275013843000001,13.01872833,\
        3.0365853,1.9651040569999998",
    )


def test_blank_image(
    create_environment_support_functions,
):  # pylint: disable=W0613
    """Test generation of mask"""
    blank_image(
        "sector_1_mask.fits",
        input_image=None,
        vertices_file="sector_1_vertices.pkl",
        reference_ra_deg="258.845708333",
        reference_dec_deg="57.4111944444",
        cellsize_deg="0.00034722222222222224",
        imsize="24394,24394",
    )


def test_filter_skymodel(
    create_environment_support_functions,
):  # pylint: disable=W0613
    """Test skymodel filtering"""
    working_dir = "/var/scratch/csalvoni/rapthor_working_dir/chiara"

    beam_ms = f"{working_dir}/midbands.ms.mjd5020557063_field.sector_1.prep,\
    {working_dir}/predict_1/midbands.ms.mjd5020559947_field.sector_1.prep,\
    {working_dir}/predict_1/midbands.ms.mjd5020562823_field.sector_1.prep,\
    {working_dir}/predict_1/midbands.ms.mjd5020565707_field.sector_1.prep,\
    {working_dir}/predict_1/midbands.ms.mjd5020568583_field.sector_1.prep,\
    {working_dir}/predict_1/midbands.ms.mjd5020571459_field.sector_1.prep,\
    {working_dir}/predict_1/midbands.ms.mjd5020574343_field.sector_1.prep,\
    {working_dir}/predict_1/midbands.ms.mjd5020577219_field.sector_1.prep,\
    {working_dir}/predict_1/midbands.ms.mjd5020580103_field.sector_1.prep,\
    {working_dir}/predict_1/midbands.ms.mjd5020582979_field.sector_1.prep"

    filter_skymodel(
        f"{working_dir}/inputs/sector_1-MFS-image.fits",
        "sector_1-sources-pb.txt",
        "sector_1",
        "sector_1_vertices.pkl",
        beamMS=beam_ms,
        threshisl=4.0,
        threshpix=5.0,
    )
