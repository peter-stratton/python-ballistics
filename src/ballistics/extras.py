# -*- coding: utf-8 -*-
"""ballistics.extras

This module contains functions that are related to, but not part of the core ballistics calculations contained
in the `internal`, `transitional`, `external`, or `terminal` modules.
"""

# CONSTANTS
PROPELLANT_GAS_VELOCITY_CONSTANTS = {
    'HighPoweredRifle': 1.75,
    'AverageLengthShotgun': 1.50,
    'LongBarrelShotgun': 1.25,
    'PistolAndRevolver': 1.50
}


def propellant_gas_velocity_multiplier(firearm_code):
    """Provides the Propellant Gas Velocity multiplier for a given firearm_code

    Parameters
    ----------
    firearm_code : {'HPR', 'ALS', 'LBS', 'PAR'}
        HPR = HighPoweredRifle
        ALS = AverageLengthShotgun
        LBS = LongBarrelShotgun
        PAR = PistolAndRevolver

    Returns
    -------
    float
        Propellant Gas Velocity multiplier for a given firearm type

    Notes
    -----
    Refer to http://www.saami.org/PubResources/GunRecoilFormulae.pdf

    The PROPELLANT_GAS_VELOCITY_CONSTANTS were sourced from the SAAMI GunRecoilFormulae document and were originally
    derived from "extensive experiments by the British, published in "British Text Book of Small Arms" published in 1929
    and confirmed by later work in [the United States]".
    """
    pgvcs = {
        'HPR': PROPELLANT_GAS_VELOCITY_CONSTANTS['HighPoweredRifle'],
        'ALS': PROPELLANT_GAS_VELOCITY_CONSTANTS['AverageLengthShotgun'],
        'LBS': PROPELLANT_GAS_VELOCITY_CONSTANTS['LongBarrelShotgun'],
        'PAR': PROPELLANT_GAS_VELOCITY_CONSTANTS['PistolAndRevolver']
    }
    return pgvcs[firearm_code.upper()]
