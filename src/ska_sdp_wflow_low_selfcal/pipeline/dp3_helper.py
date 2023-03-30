from subprocess import check_call

common_args = [
            "checkparset=1",
            "msout=test.MS",
            "steps=[averager]",
            "numthreads=1",
            "msout.overwrite=true"
        ]

def run_dp3(msin):
    check_call(
        [
            "/home/csalvoni/scratch/schaap/dp3/build/DP3",
            f"msin={msin}",
        ]
        + common_args
    )
