"""This module contains commands to use DP3"""
from subprocess import check_call


class Dp3Runner:
    """This class contains commands to use DP3"""

    def __init__(self, dp3_exe):
        self.dp3_exe = dp3_exe

    def predict(  # pylint: disable=R0913
        self,
        msin,
        msout,
        starttime,
        directions,
        input_skymodel,
        solutions_to_apply,
    ):
        """This workflow performs direction-dependent prediction of sector sky
        models and subracts the resulting model data from the input data,
        reweighting if desired. The resulting data are suitable for imaging."""

        check_call(
            [
                self.dp3_exe,
                f"msin={msin}",
                f"msin.starttime={starttime}",
                f"predict.applycal.parmdb={solutions_to_apply}",
                f"predict.directions={directions}",
                f"predict.sourcedb={input_skymodel}",
                f"msout={msout}",
                "msout.overwrite=true",
            ]
            + self.args_predict
            + self.common_args
        )

    def calibrate_scalarphase(  # pylint: disable=R0913
        self,
        msin,
        starttime,
        input_skymodel,
        constraint_antennas,
        output_solutions="fast_phase_0.h5parm",
    ):
        """(1)  a fast phase-only calibration (with
        core stations constrianed to have the same solutions) to correct for
        ionospheric effects, (2) a joint slow amplitude calibration (with all
        stations constrained to have the same solutions) to correct for beam
        errors"""

        antennaconstraint = ["solve.antennaconstraint=[]"]
        if constraint_antennas:
            antennaconstraint = [
                "solve.antennaconstraint=[[CS001HBA0,CS002HBA0,"
                "CS002HBA1,CS004HBA1,RS106HBA,RS208HBA,RS305HBA,RS307HBA]]"
            ]

        check_call(
            [
                self.dp3_exe,
                f"msin.starttime={starttime}",
                f"msin={msin}",
                f"solve.sourcedb={input_skymodel}",
                f"solve.h5parm={output_solutions}",
                "msout= ",
            ]
            + antennaconstraint
            + self.args_calibrate_common
            + self.args_calibrate_scalarphase
            + self.common_args,
        )

    def calibrate_complexgain(  # pylint: disable=R0913
        self,
        msin,
        starttime,
        input_skymodel="calibration_skymodel.txt",
        solutions_to_apply="fast_phases.h5parm",
        output_solutions="slow_gain_separate_0.h5parm",
    ):
        """(3) a further unconstrained slow gain calibration to correct for "
        "station-to-station differences."""

        check_call(
            [
                self.dp3_exe,
                f"msin.starttime={starttime}",
                f"msin={msin}",
                f"solve.applycal.parmdb={solutions_to_apply}",
                f"solve.h5parm={output_solutions}",
                f"solve.sourcedb={input_skymodel}",
                "msout=/var/scratch/csalvoni/data/test.MS",
                "msout.overwrite=true",
            ]
            + self.args_calibrate_common
            + self.args_calibrate_complexgain
            + self.common_args
        )

    def applybeam_shift_average(self, msin, msout, starttime):
        """This step uses DP3 to prepare the input data for imaging. This
        involves averaging, phase shifting, and optionally the application of
        the calibration solutions at the center."""

        check_call(
            [
                self.dp3_exe,
                f"msin.starttime={starttime}",
                f"msin={msin}",
                f"msout={msout}",
                "msin.datacolumn=DATA",
                "msout.overwrite=True",
                "msout.writefullresflag=False",
                "steps=[applybeam,shift,avg]",
                "shift.type=phaseshifter",
                "avg.type=squash",
                "msout.storagemanager=Dysco",
                "applybeam.direction=[258.845708333deg, 57.4111944444deg]",
                "avg.freqstep=1",
                "shift.phasecenter=[258.845708333deg, 57.4111944444deg]",
                "avg.timestep=1",
            ]
            + self.common_args
        )

    args_calibrate_common = [
        "checkparset=1",
        "msin.datacolumn=DATA",
        "steps=[solve]",
        "solve.type=ddecal",
        "solve.usebeammodel=True",
        "solve.beammode=array_factor",
        "solve.llssolver=qr",
        "solve.maxiter=150",
        "solve.nchan=10",
        "solve.onebeamperpatch=False",
        "solve.parallelbaselines=False",
        "solve.propagatesolutions=True",
        "solve.smoothnessconstraint=3000000.0",
        "solve.solveralgorithm=hybrid",
        # "solve.sourcedb=calibration_skymodel.txt",
        # "msin.starttime=21Dec2017/07:11:03.906",
        "solve.stepsize=0.02",
        "solve.tolerance=0.005",
        "solve.uvlambdamin=2000.0",
    ]

    args_calibrate_scalarphase = [
        "solve.mode=scalarphase",
        "solve.llssolver=qr",
        "solve.maxiter=150",
        "solve.solint=1",
        "solve.smoothnessrefdistance=0.0",
        "solve.smoothnessreffrequency=143650817.87109375",
    ]

    args_calibrate_complexgain = [
        "solve.mode=complexgain",
        "solve.applycal.steps=[fastphase]",
        "solve.applycal.fastphase.correction=phase000",
        "msin.nchan=0",
        "solve.solint=75",
        "solve.nchan=10",
        "msin.startchan=0",
    ]

    args_predict = [
        "msin.datacolumn=DATA",
        "msout.overwrite=True",
        "msout.writefullresflag=False",
        "steps=[predict]",
        "predict.type=h5parmpredict",
        "predict.operation=replace",
        "predict.applycal.correction=phase000",
        "predict.applycal.steps=[fastphase]",
        "predict.applycal.fastphase.correction=phase000",
        "predict.usebeammodel=True",
        "predict.beammode=array_factor",
        "msout.storagemanager=Dysco",
        "msout.storagemanager.databitrate=0",
        "predict.onebeamperpatch=False",
        # "predict.sourcedb=outlier_1_predict_skymodel.txt",
        # "msin.starttime=21Dec2017/07:11:03.906",
    ]

    common_args = [
        "msin.ntimes=75",
        "numthreads=40",
    ]
