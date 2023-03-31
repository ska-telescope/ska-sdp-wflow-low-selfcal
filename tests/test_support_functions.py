
"""Tests for the ska_sdp_wflow_low_selfcal module."""
import pytest
import os.path
from ska_sdp_wflow_low_selfcal.pipeline.support_functions import download_skymodel
from astropy.coordinates import Angle


def test_download_skymodel():

    # Download skymodel and group sources
    ra = "01h37m41.299"
    dec = "+033d09m35.132"
    if type(ra) is str:
        ra = Angle(ra).to('deg').value
    if type(dec) is str:
        dec = Angle(dec).to('deg').value

    download_skymodel(ra, dec, "test.skymodel")
    assert(os.path.isfile("test.skymodel"))


