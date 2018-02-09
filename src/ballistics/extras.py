# -*- coding: utf-8 -*-
"""
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


# HELPER FUNCTIONS
def propellant_gas_velocity_multiplier(firearm_code):
    """Provides the Propellant Gas Velocity multiplier for a given firearm_code

    Parameters
    ----------
    firearm_code : {'HPR', 'ALS', 'LBS', 'PAR'}
        * HPR = High Powered Rifle
        * ALS = Average Length Shotgun
        * LBS = Long Barrel Shotgun
        * PAR = Pistol And Revolver

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


# Primary Functions
def approximate_free_recoil_energy(firearm_code, firearm_weight_in_lbs, ejecta_weight_in_grains,
                                   charge_weight_in_grains, average_load_velocity_in_fps, decimal_places=0):
    """Provides the approximate free recoil energy for a given load firearm type combination

    Parameters
    ----------
    firearm_code : str
        Argument to use for the :func:`~ballistics.extras.propellant_gas_velocity_multiplier` function.
    firearm_weight_in_lbs : float
        Weight in lbs of the firearm plus any accessories.
    ejecta_weight_in_grains : float
        Weight in grains of the projectile plus wad (if fired from a shotgun).
    charge_weight_in_grains : float
        Weight in grains of the powder charge.
    average_load_velocity_in_fps : int
        Average velocity for this load (field measurement or from loading manual reference table).
    decimal_places : int, optional
        How many decimal places to return, (default value is 0 which returns the floor of the result).

    Returns
    -------
    int or float
        By default ``decimal_places`` is 0 which will return the floor integer value.  If a value greater than 0 is
        passed in, the function will return a float value rounded to ``decimal_places``.

    Notes
    -----
    Refer to http://www.saami.org/PubResources/GunRecoilFormulae.pdf

    The accuracy of the value returned from this function is directly related to the accuracy of the charge
    weight and projectile velocity.

    """
    mass = firearm_weight_in_lbs / 64.34
    firearm_weight_in_grains = firearm_weight_in_lbs * 7000.0
    ejecta_energy = float(ejecta_weight_in_grains) * average_load_velocity_in_fps
    propellant_gas_energy = charge_weight_in_grains * propellant_gas_velocity_multiplier(
        firearm_code) * average_load_velocity_in_fps
    velocity = pow((ejecta_energy + propellant_gas_energy) / firearm_weight_in_grains, 2)
    if decimal_places:
        return round(mass * velocity, decimal_places)
    return int(mass * velocity)
