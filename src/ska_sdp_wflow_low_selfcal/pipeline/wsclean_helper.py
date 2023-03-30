from subprocess import check_call


common_args = [
            "-size", "512", "512",
            "-scale", "0.01",
            "-channel-range", "0", "1",
            "-name", "dummy",
        ]

def run_wsclean(msin):
    check_call(
        [
            "/home/csalvoni/scratch/schaap/wsclean/build/wsclean",
        ]
        + common_args
        + [msin]
    )