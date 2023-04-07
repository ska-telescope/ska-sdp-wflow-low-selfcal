# -*- coding: utf-8 -*-
" This script sefines a SKA LOW self calibration workflow"


from ska_sdp_wflow_low_selfcal.pipeline.dp3_helper import Dp3Runner
from ska_sdp_wflow_low_selfcal.pipeline.operations import (
    calibrate_1,
    calibrate_2,
    calibrate_3,
    image_1,
    image_3,
    predict_1,
    predict_3,
)
from ska_sdp_wflow_low_selfcal.pipeline.wsclean_helper import WSCleanRunner

PATH_TO_DP3_EXE = "/home/csalvoni/scratch/schaap/dp3/build/DP3"
PATH_TO_WSCLEAN_EXE = "/home/csalvoni/scratch/schaap/wsclean/build/wsclean"

WORK_DIR = "/var/scratch/csalvoni/rapthor_working_dir/chiara"


def main():
    """Run pipeline"""
    dp3_runner = Dp3Runner(PATH_TO_DP3_EXE)
    wsclean_runner = WSCleanRunner(PATH_TO_WSCLEAN_EXE)

    # Calibrate_1 0:52:21
    calibrate_1(dp3_runner)
    # Predict_1 0:18:10
    predict_1(dp3_runner)
    # Image_1 7:06:40

    image_1(
        dp3_runner,
        wsclean_runner,
        f"{WORK_DIR}/inputs/field-solutions_calibration_1.h5",
    )

    # Missing: how to get the skymodel for calibration_2

    # Calibrate_2 1:04:16
    calibrate_2(dp3_runner)
    # Image_2 7:27:09
    image_1(
        dp3_runner,
        wsclean_runner,
        f"{WORK_DIR}/inputs/field-solutions_calibration_2.h5",
    )

    # Calibrate_3 2:14:40
    calibrate_3(dp3_runner)
    # Predict_3 0:53:04
    predict_3(dp3_runner)
    # Image_3 5:20:55
    image_3(
        dp3_runner,
        wsclean_runner,
        f"{WORK_DIR}/inputs/field-solutions_calibration_3.h5",
    )


if __name__ == "__main__":
    main()
