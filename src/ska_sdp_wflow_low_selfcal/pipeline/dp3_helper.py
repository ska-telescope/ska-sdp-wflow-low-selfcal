from subprocess import check_call

args_calibrate_common= [
        "checkparset=1",
        "msin.datacolumn=DATA",
        "steps=[solve]",
        "solve.type=ddecal",
        "solve.usebeammodel=True",
        "solve.beammode=array_factor",
        "solve.llssolver=qr",
        "solve.maxiter=150",
        "msin=/tmp/0soy7y97/stg5492f725-c9df-403a-b41d-d9430538a2a2/midbands.ms",
        "solve.nchan=10",
        "solve.onebeamperpatch=False",
        "solve.parallelbaselines=False",
        "solve.propagatesolutions=True",
        "solve.smoothnessconstraint=3000000.0",
        "solve.smoothnessrefdistance=0.0",
        "solve.smoothnessreffrequency=143650817.87109375",

        "solve.solveralgorithm=hybrid",
        "solve.solverlbfgs.dof=200.0",
        "solve.solverlbfgs.iter=4",
        "solve.solverlbfgs.minibatches=1",
        "solve.sourcedb=/tmp/0soy7y97/stg44238d01-cf05-4c1b-93e6-a3b5a08bc34c/calibration_skymodel.txt",
        "msin.starttime=21Dec2017/07:11:03.906",
        "solve.stepsize=0.02",
        "solve.tolerance=0.005",
        "solve.uvlambdamin=2000.0"
        "msout=/var/scratch/csalvoni/data/test.MS",  # TODO
        "msout.overwrite=true" # TODO
]
args_calibrate_scalarphase = [
        "solve.mode=scalarphase",
        "solve.h5parm=fast_phase_0.h5parm",
        "solve.llssolver=qr",
        "solve.maxiter=150",
        "solve.solint=1",   
    ]
    
     #   "solve.antennaconstraint=[]" differs when running also complexgain

args_calibrate_complexgain = [
        "solve.mode=complexgain",
        "solve.applycal.steps=[fastphase]",
        "solve.applycal.fastphase.correction=phase000",
        "solve.applycal.parmdb=/tmp/d0ozshit/stgcd773b67-4cfa-455d-9c81-1177ef05b2db/fast_phases.h5parm",
        "solve.h5parm=slow_gain_separate_0.h5parm",
        "msin.nchan=0",
        "solve.solint=75",
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
        "predict.directions=[[Patch_104],[Patch_11],[Patch_114],[Patch_189],[Patch_222],[Patch_73],[Patch_78]]",
        "predict.applycal.parmdb=/tmp/c2zkydk3/stgda8228ac-93c1-4d24-adc5-3966f81b462e/field-solutions.h5",
        "msin=/tmp/c2zkydk3/stgadba1bda-7cda-4ae0-a9e2-81a73319ca3a/midbands.ms",
        "msout=midbands.ms.mjd5020557063.outlier_1_modeldata",
        "predict.onebeamperpatch=False",
        "predict.sourcedb=/tmp/c2zkydk3/stg35291b70-ea23-4633-9ce4-8c8ca7fd130a/outlier_1_predict_skymodel.txt",
        "msin.starttime=21Dec2017/07:11:03.906"
    ]

common_args = [
        "msin.ntimes=75",
        "numthreads=40",
]

def run_dp3(msin, mode):
    if mode == "predict":
        check_call(
            [
                "/home/csalvoni/scratch/schaap/dp3/build/DP3",
                f"msin={msin}",
            ]
            + args_calibrate
            + common_args
        )
    elif mode == "calibrate"
        check_call(
            [
                "/home/csalvoni/scratch/schaap/dp3/build/DP3",
                f"msin={msin}",
            ]
            + args_predict
            + common_args
        )
