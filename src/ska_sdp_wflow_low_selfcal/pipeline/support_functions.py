"""
Module that holds miscellaneous functions and classes
"""
# pylint: skip-file
import logging
import os
import subprocess
import time

import lsmtool


def download_skymodel(
    ra,
    dec,
    skymodel_path,
    radius=5.0,
    overwrite=False,
    source="TGSS",
    targetname="Patch",
):
    """
    Download the skymodel for the target field

    Parameters
    ----------
    ra : float
        Right ascension of the skymodel centre.
    dec : float
        Declination of the skymodel centre.
    skymodel_path : str
        Full name (with path) to the skymodel.
    radius : float
        Radius for the TGSS/GSM cone search in degrees.
    source : str
        Source where to obtain a skymodel from. Can be TGSS or GSM. Default is
        TGSS.
    overwrite : bool
        Overwrite the existing skymodel pointed to by skymodel_path.
    target_name : str
        Give the patch a certain name. Default is "Patch".
    """
    SKY_SERVERS = {
        "TGSS": "http://tgssadr.strw.leidenuniv.nl/cgi-bin/gsmv4.cgi?coord=\
        {ra:f},{dec:f}&radius={radius:f}&unit=deg&deconv=y",
        "GSM": "https://lcs165.lofar.eu/cgi-bin/gsmv1.cgi?coord={ra:f},{dec:f}\
        &radius={radius:f}&unit=deg&deconv=y",
    }
    if source.upper() not in SKY_SERVERS.keys():
        raise ValueError(
            "Unsupported skymodel source specified! Please use TGSS or GSM."
        )

    logger = logging.getLogger("rapthor:skymodel")

    file_exists = os.path.isfile(skymodel_path)
    if file_exists and not overwrite:
        logger.warning(
            'Skymodel "%s" exists and overwrite is set to False! Not \
            downloading skymodel. If this is a restart this may be \
            intentional.'
            % skymodel_path
        )
        return

    if (not file_exists) and os.path.exists(skymodel_path):
        logger.error('Path "%s" exists but is not a file!' % skymodel_path)
        raise ValueError('Path "%s" exists but is not a file!' % skymodel_path)

    # Empty strings are False. Only attempt directory creation if there is a
    # directory path involved.
    if (
        (not file_exists)
        and os.path.dirname(skymodel_path)
        and (not os.path.exists(os.path.dirname(skymodel_path)))
    ):
        os.makedirs(os.path.dirname(skymodel_path))

    if file_exists and overwrite:
        logger.warning(
            'Found existing skymodel "%s" and overwrite is True. Deleting \
            existing skymodel!'
            % skymodel_path
        )
        os.remove(skymodel_path)

    logger.info("Downloading skymodel for the target into " + skymodel_path)

    tries = 0
    while tries < 5:
        result = subprocess.run(
            [
                "wget",
                "-O",
                skymodel_path,
                SKY_SERVERS[source].format(ra=ra, dec=dec, radius=radius),
            ]
        )
        if result.returncode != 0:
            logger.error(
                "Attempt {t:d} download of skymodel failed. Attempting {t:d} \
                more times.".format(
                    t=5 - tries
                )
            )
        else:
            break
        time.sleep(5)
        tries += 1
        if tries == 5:
            logger.critical("Download of skymodel failed after 5 attempts.")

    if not os.path.isfile(skymodel_path):
        logger.critical(
            'Skymodel "%s" does not exist after trying to download the \
            skymodel.'
            % skymodel_path
        )
        raise IOError(
            'Skymodel "%s" does not exist after trying to download the \
            skymodel.'
            % skymodel_path
        )

    # Treat all sources as one group (direction)
    skymodel = lsmtool.load(skymodel_path)
    skymodel.group("single", root=targetname)
    skymodel.write(clobber=True)


# def group_sources():
