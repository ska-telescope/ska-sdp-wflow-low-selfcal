#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the ska_sdp_wflow_low_selfcal module."""
from ska_sdp_wflow_low_selfcal.pipeline.main import run_pipeline


def test_example():
    "Dummy test"
    assert run_pipeline() == "This is a dummy workflow script"
