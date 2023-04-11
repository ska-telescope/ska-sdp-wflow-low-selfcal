""" This module contains all operations to run in the pipeline """

import logging

from ska_sdp_wflow_low_selfcal.pipeline.support.combine_h5parms import (
    combine_h5parms,
)
from ska_sdp_wflow_low_selfcal.pipeline.support.H5parm_collector import (
    collect_h5parms,
)

MSIN = "/var/scratch/csalvoni/rapthor_working_dir/chiara/midbands.ms"
WORK_DIR = "/var/scratch/csalvoni/rapthor_working_dir/chiara"
START_TIMES = [
    "21Dec2017/07:11:03.906",
    "21Dec2017/07:59:07.909",
    "21Dec2017/08:47:03.901",
    "21Dec2017/09:35:07.905",
    "21Dec2017/10:23:03.897",
    "21Dec2017/11:10:59.889",
    "21Dec2017/11:59:03.893",
    "21Dec2017/12:46:59.885",
    "21Dec2017/13:35:03.889",
    "21Dec2017/14:22:59.881",
]


def calibrate_1(dp3_runner):
    """Define calibrate operation"""
    # ------------------------ Calibrate_1 0:52:21
    logging.info("Start calibrate_1")
    output_solutions_filenames = []
    for i, start_time in enumerate(START_TIMES):
        output_solution_filename = (
            f"{WORK_DIR}/outputs/out_calibration_1_fast_phase_"
            + str(i)
            + ".h5parm"
        )
        dp3_runner.calibrate_scalarphase(
            f"{MSIN}",
            start_time,
            f"{WORK_DIR}/inputs/in_calibration_1.txt",
            False,
            output_solution_filename,
        )
        output_solutions_filenames.append(output_solution_filename)

    # Stitch all solutions together
    collect_h5parms(
        output_solutions_filenames,
        "in_predict_1_field-solutions.h5",
        clobber=True,
    )

    # Missing 2: get outlier_1_predict_skymodel (implement in AST-1236)


def calibrate_2(dp3_runner):
    """Define calibrate operation"""
    # ------------------------ Calibrate_2 1:04:16
    logging.info("Start calibrate_2")
    msin_after_predict = [
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020557063_field",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020559947_field",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020562823_field",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020565707_field",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020568583_field",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020571459_field",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020574343_field",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020577219_field",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020580103_field",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020582979_field",
    ]
    output_solutions_filenames = []
    for i, start_time in enumerate(START_TIMES):
        output_solution_filename = (
            f"{WORK_DIR}/outputs/out_calibration_2_fast_phase_"
            + str(i)
            + ".h5parm",
        )
        dp3_runner.calibrate_scalarphase(
            msin_after_predict[i],
            start_time,
            f"{WORK_DIR}/inputs/in_calibration_2.txt",
            False,
            output_solution_filename,
        )
        output_solutions_filenames.append(output_solution_filename)

    # Stitch all solutions together
    collect_h5parms(
        output_solutions_filenames,
        "in_image_2_field-solutions.h5",
        clobber=True,
    )

    # Missing 2: get outlier_1_predict_skymodel (implement in AST-1236)


def calibrate_3(dp3_runner):
    """Define calibrate operation"""
    # ------------------------ Calibrate_1 0:52:21
    # logging.info("Start calibrate_1")
    # for i, start_time in enumerate(START_TIMES):
    #     dp3_runner.calibrate_scalarphase(
    #         f"{MSIN}",
    #         start_time,
    #         f"{WORK_DIR}/inputs/in_calibration_3.txt",
    #         True,
    #         f"{WORK_DIR}/outputs/out_calibration_3_fast_phase_"
    #         + str(i)
    #         + ".h5parm",
    #     )

    # missing: collect solutions together -> H5parm_collector
    for i, start_time in enumerate(START_TIMES):
        dp3_runner.calibrate_complexgain(
            f"{MSIN}",
            start_time,
            f"{WORK_DIR}/inputs/in_calibration_3.txt",
            f"{WORK_DIR}/inputs/out_calibration_3_fast_phase.h5parm",
            f"{WORK_DIR}/outputs/out_calibration_3_slow_gain_separate_"
            + str(i)
            + ".h5parm",
        )

    # Missing 1: stitch all solutions together
    # Shortcut: get solutions from rapthor output
    # Implement in AST-1236
    # combine combine_h5parms.py -> slow_gains_separate.h5parm

    # Missing 2: get outlier_1_predict_skymodel (implement in AST-1236)


def predict_1(dp3_runner):
    """Define predict operation"""
    # ------------------------ Predict_1 0:18:10
    directions = (
        "[[Patch_104],[Patch_11],[Patch_114],[Patch_189],"
        "[Patch_222],[Patch_73],[Patch_78]]"
    )
    logging.info("Start Predict_1")
    for i, start_time in enumerate(START_TIMES):
        msout = f"midbands.ms.{i}.outlier_1_modeldata"
        dp3_runner.predict(
            MSIN,
            msout,
            start_time,
            directions,
            f"{WORK_DIR}/inputs/outlier_1_predict_skymodel.txt",
            "in_predict_1_field-solutions.h5",
        )

    # Missing 3: subtract_sector_models.py * 10 times
    # IN: outlier_1_modeldata -> OUT: mjd5020559947_field


def predict_3(dp3_runner):
    """Define predict operation"""

    directions_1 = "[[Patch_1022],[Patch_1042],[Patch_1075],[Patch_136],\
    [Patch_151],[Patch_152],[Patch_231],[Patch_235],[Patch_313],[Patch_34],\
    [Patch_341]]"
    logging.info("Start Predict_1")
    for i, start_time in enumerate(START_TIMES):
        msout = f"midbands.ms.{i}.outlier_1_modeldata"
        dp3_runner.predict(
            MSIN,
            msout,
            start_time,
            directions_1,
            f"{WORK_DIR}/inputs/bright_source_2_predict_skymodel.txt",
            f"{WORK_DIR}/outputs/out_calibration_2_fast_phase_"
            f"{WORK_DIR}/inputs/in_predict_3_field-solutions.h5",
        )

    directions_2 = "[[Patch_341],[Patch_375],[Patch_423],[Patch_456],\
    [Patch_47],[Patch_479],[Patch_51],[Patch_809],[Patch_865],[Patch_900]]"
    logging.info("Start Predict_1")
    for i, start_time in enumerate(START_TIMES):
        msout = f"midbands.ms.{i}.outlier_1_modeldata"
        dp3_runner.predict(
            MSIN,
            msout,
            start_time,
            directions_2,
            f"{WORK_DIR}/inputs/bright_source_2_predict_skymodel.txt",
            f"{WORK_DIR}/outputs/out_calibration_2_fast_phase_"
            f"{WORK_DIR}/inputs/in_predict_3_field-solutions.h5",
        )
    # Missing 3: subtract_sector_models.py * 10 times
    # IN: outlier_1_modeldata -> OUT: mjd5020559947_field


def image_1(dp3_runner, wsclean_runner, solutions_to_apply, facets_file):
    """Define imaging operation"""
    # ------------------------ Image_1 7:06:40
    logging.info("Start Image_1")

    msin_after_predict = [
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020557063_field",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020559947_field",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020562823_field",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020565707_field",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020568583_field",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020571459_field",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020574343_field",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020577219_field",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020580103_field",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020582979_field",
    ]
    for i, start_time in enumerate(START_TIMES):
        dp3_runner.applybeam_shift_average(
            msin_after_predict[i],
            f"{msin_after_predict[i]}.sector_1.prep",
            start_time,
        )

    # filter_skymodel.py \
    # In: midbands.ms.mjd5020557063_field.sector_1.prep, etc ???
    # Out: sector_1_vertices.pkl

    # Missing blank_image.py
    # IN: sector_1_vertices.pkl
    # OUT: sector_1_mask.fits

    input_imaging = [
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020557063_field.sector_1.prep",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020559947_field.sector_1.prep",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020562823_field.sector_1.prep",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020565707_field.sector_1.prep",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020568583_field.sector_1.prep",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020571459_field.sector_1.prep",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020574343_field.sector_1.prep",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020577219_field.sector_1.prep",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020580103_field.sector_1.prep",
        f"{WORK_DIR}/predict_1/midbands.ms.mjd5020582979_field.sector_1.prep",
    ]

    wsclean_runner.run_wsclean(input_imaging, facets_file, solutions_to_apply)


def image_3(dp3_runner, wsclean_runner, solutions_to_apply):
    """Define imaging operation"""

    # do nothing
