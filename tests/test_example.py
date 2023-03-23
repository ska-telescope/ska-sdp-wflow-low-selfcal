#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the ska_sdp_wflow_low_selfcal module."""
import pytest

from ska_sdp_wflow_low_selfcal.pipeline import main

def test_example():
    assert main() == "This is a dummy workflow script"

