# -*- coding: utf-8 -*-
" This script sefines a SKA LOW self calibration workflow"


# -*- coding: utf-8 -*-
# import logging

# from ska_sdp_wflow_low_selfcal.pipeline.dp3_helper import Dp3Runner
# from ska_sdp_wflow_low_selfcal.pipeline.wsclean_helper import WSCleanRunner

# PATH_TO_DP3_EXE = "/home/csalvoni/scratch/schaap/dp3/build/DP3"
# PATH_TO_WSCLEAN_EXE = "/home/csalvoni/scratch/schaap/wsclean/build/wsclean"


def main():
    """Run pipeline"""
    # logging.basicConfig(level=logging.DEBUG)

    # msin = "/var/scratch/csalvoni/rapthor_work_dir/chiara/midbands.ms"
    # work_dir = "/var/scratch/csalvoni/rapthor_work_dir/chiara"
    # dp3_runner = Dp3Runner(PATH_TO_DP3_EXE)
    # wsclean_runner = WSCleanRunner(PATH_TO_WSCLEAN_EXE)

    # # Expected total runtime 26 hours

    # # Missing 0: Download skymodel and group sources
    # # Shortcut: get solutions from rapthor output
    # # Implement in AST-1236

    # start_times = [
    #     "21Dec2017/07:11:03.906",
    #     "21Dec2017/07:59:07.909",
    #     "21Dec2017/08:47:03.901",
    #     "21Dec2017/09:35:07.905",
    #     "21Dec2017/10:23:03.897",
    #     "21Dec2017/11:10:59.889",
    #     "21Dec2017/11:59:03.893",
    #     "21Dec2017/12:46:59.885",
    #     "21Dec2017/13:35:03.889",
    #     "21Dec2017/14:22:59.881",
    # ]

    # # ------------------------ Calibrate_1 0:52:21
    # logging.info("Start calibrate_1")
    # for i, start_time in enumerate(start_times):
    #     dp3_runner.calibrate_scalarphase(
    #         f"{msin}",
    #         start_time,
    #         f"{work_dir}/inputs/in_calibration_1.txt",
    #         False,
    #         f"{work_dir}/outputs/out_calibration_1_fast_phase_"
    #         + str(i)
    #         + ".h5parm",
    #     )

    # # Missing 1: stitch all solutions together
    # # Shortcut: get solutions from rapthor output
    # # Implement in AST-1236

    # # Missing 2: get outlier_1_predict_skymodel (implement in AST-1236)

    # # ------------------------ Predict_1 0:18:10
    # directions = (
    #     "[[Patch_104],[Patch_11],[Patch_114],[Patch_189],"
    #     "[Patch_222],[Patch_73],[Patch_78]]"
    # )
    # logging.info("Start Predict_1")
    # for i, start_time in enumerate(start_times):
    #     msout = f"midbands.ms.{i}.outlier_1_modeldata"
    #     dp3_runner.predict(
    #         msin,
    #         msout,
    #         start_time,
    #         directions,
    #         f"{work_dir}/inputs/outlier_1_predict_skymodel.txt",
    #         f"{work_dir}/outputs/out_calibration_1_fast_phase_"
    #         f"{work_dir}/inputs/in_predict_1_field-solutions.h5",
    #     )

    # # Missing 3: subtract_sector_models.py * 10 times
    # # IN: outlier_1_modeldata -> OUT: mjd5020559947_field

    # # ------------------------ Image_1 7:06:40
    # logging.info("Start Image_1")

    # msin_after_predict = [
    #     f"{work_dir}/predict_1/midbands.ms.mjd5020557063_field"
    #     f"{work_dir}/predict_1/midbands.ms.mjd5020562823_field"
    #     f"{work_dir}/predict_1/midbands.ms.mjd5020568583_field"
    #     f"{work_dir}/predict_1/midbands.ms.mjd5020574343_field"
    #     f"{work_dir}/predict_1/midbands.ms.mjd5020580103_field"
    #     f"{work_dir}/predict_1/midbands.ms.mjd5020559947_field"
    #     f"{work_dir}/predict_1/midbands.ms.mjd5020565707_field"
    #     f"{work_dir}/predict_1/midbands.ms.mjd5020571459_field"
    #     f"{work_dir}/predict_1/midbands.ms.mjd5020577219_field"
    #     f"{work_dir}/predict_1/midbands.ms.mjd5020582979_field"
    # ]
    # for i, start_time in enumerate(start_times):
    #     msout = f"midbands.ms.{i}.outlier_1_modeldata"
    #     dp3_runner.applybeam_shift_average(
    #         msin_after_predict[i],
    #         f"{msin_after_predict[i]}.sector_1.prep",
    #         start_time,
    #     )

    # # filter_skymodel.py \
    # # In: midbands.ms.mjd5020557063_field.sector_1.prep, etc ???
    # # Out: sector_1_vertices.pkl

    # # Missing blank_image.py
    # # IN: sector_1_vertices.pkl
    # # OUT: sector_1_mask.fits

    # input_imaging = [
    #  f"{work_dir}/predict_1/midbands.ms.mjd5020557063_field.sector_1.prep \
    # {work_dir}/predict_1/midbands.ms.mjd5020559947_field.sector_1.prep \
    # {work_dir}/predict_1/midbands.ms.mjd5020562823_field.sector_1.prep \
    # {work_dir}/predict_1/midbands.ms.mjd5020565707_field.sector_1.prep \
    # {work_dir}/predict_1/midbands.ms.mjd5020568583_field.sector_1.prep \
    # {work_dir}/predict_1/midbands.ms.mjd5020571459_field.sector_1.prep \
    # {work_dir}/predict_1/midbands.ms.mjd5020574343_field.sector_1.prep \
    # {work_dir}/predict_1/midbands.ms.mjd5020577219_field.sector_1.prep \
    # {work_dir}/predict_1/midbands.ms.mjd5020580103_field.sector_1.prep \
    # {work_dir}/predict_1/midbands.ms.mjd5020582979_field.sector_1.prep"
    # ]

    # wsclean_runner.run_wsclean(input_imaging)
    # run_wsclean(msin)

    # # Calibrate_2 1:04:16
    # logging.info("Start Calibrate_2")
    # run_dp3(msin, "calibrate")

    # # Image_2 7:27:09
    # logging.info("Start Image_2")
    # run_wsclean(msin)

    # # Calibrate_3 2:14:40
    # logging.info("Start Calibrate_3")
    # run_dp3(msin, "calibrate")

    # # Predict_3 0:53:04
    # logging.info("Start Predict_3")
    # run_dp3(msin, "predict")

    # # Image_3 5:20:55
    # logging.info("Start Image_3")
    # run_wsclean(msin)


if __name__ == "__main__":
    main()
