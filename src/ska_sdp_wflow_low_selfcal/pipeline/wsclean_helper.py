""" This module contains commands to use WSClean """
from subprocess import check_call

common_args = [
    "-size",
    "512",
    "512",
    "-scale",
    "0.01",
    "-channel-range",
    "0",
    "1",
    "-name",
    "/var/scratch/csalvoni/data/dummy",
]


def run_wsclean(msin):
    """Run WSClean"""
    check_call(
        [
            "/home/csalvoni/scratch/schaap/wsclean/build/wsclean",
        ]
        + common_args
        + [msin]
    )
