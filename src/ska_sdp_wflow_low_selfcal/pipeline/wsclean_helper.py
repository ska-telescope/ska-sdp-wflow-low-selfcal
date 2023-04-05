""" This module contains commands to use WSClean """
from subprocess import check_call


class WSCleanRunner:
    """This class contains commands to use WSClean"""

    def __init__(self, wsclean_exe):
        self.wsclean_exe = wsclean_exe

    common_args = [
        "-no-update-model-required",
        "-save-source-list",
        "-local-rms",
        "-join-channels",
        "-apply-facet-beam",
        "-log-time",
        "-gridder",
        "wgridder",
        "-temp-dir",
        "/tmp/64ltgyh9",
        "-parallel-deconvolution",
        "2048",
        "-pol",
        "I",
        "-mgain",
        "0.85",
        "-multiscale-scale-bias",
        "0.8",
        "-fit-spectral-pol",
        "3",
        "-auto-threshold",
        "1.0",
        "-local-rms-window",
        "50",
        "-local-rms-method",
        "rms-with-min",
        "-facet-beam-update",
        "120",
        "-auto-mask",
        "5.0",
        "-scale",
        "0.00034722222222222224",
        "-channels-out",
        "4",
        "-deconvolution-channels",
        "4",
        "-idg-mode",
        "cpu",
        "-fits-mask",
        "sector_1_mask.fits",
        "-maxuv-l",
        "1000000.0",
        "-minuv-l",
        "0.0",
        "-multiscale",
        "-name",
        "sector_1",
        "-deconvolution-threads",
        "16",
        "-parallel-gridding",
        "16",
        "-j",
        "40",
        "-facet-regions",
        "facets.reg",
        "-taper-gaussian",
        "0.0",
        "-size",
        "24394",
        "24394",
        "-mem",
        "90.0",
        "-niter",
        "6666666",
        "-nmiter",
        "6",
        "-weight",
        "briggs",
        "-0.5",
        "-apply-facet-solutions",
        "fast_phase_0.h5parm",
        "phase000",
    ]

    restore_args = [
        "-j",
        "-40",
        "-restore-list",
    ]

    def run_wsclean(self, msin):
        """Run WSClean"""
        check_call(
            [
                self.wsclean_exe,
            ]
            + self.common_args
            + [msin]
        )

    def restore(
        self, image_name, bright_source_skymodel="bright_source_skymodel.txt"
    ):
        """Run WSClean restore operation"""
        check_call(
            [
                self.wsclean_exe,
            ]
            + self.restore_args
            + [
                f"{image_name}.fits",
                f"{bright_source_skymodel}",
                f"{image_name}.fits",
            ]
        )

        check_call(
            [
                self.wsclean_exe,
            ]
            + self.restore_args
            + [
                f"{image_name}-pb.fits",
                f"{bright_source_skymodel}",
                f"{image_name}-pb.fits",
            ]
        )
