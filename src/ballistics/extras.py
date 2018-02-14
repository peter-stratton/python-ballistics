# -*- coding: utf-8 -*-
"""
This module contains useful or interesting functions that are related to ballistics but don't fit well anywhere else.
"""

# CONSTANTS
PROPELLANT_GAS_VELOCITY_CONSTANTS = {
    'HighPoweredRifle': 1.75,
    'AverageLengthShotgun': 1.50,
    'LongBarrelShotgun': 1.25,
    'PistolAndRevolver': 1.50
}

GENERIC_PROPELLANT_GAS_VELOCITY = 5000.0


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


def propellant_gas_energy(charge_weight_in_grains, firearm_code, muzzle_velocity_in_fps):
    """Calculates the propellant gas energy for a given load and firearm type

    Parameters
    ----------
    charge_weight_in_grains : float
        Weight in grains of the powder charge.
    firearm_code : str
        Argument to use for the :func:`~ballistics.extras.propellant_gas_velocity_multiplier` function.
    muzzle_velocity_in_fps : int
        Muzzle velocity for this load (field measurement or from loading manual reference table).

    Returns
    -------
    float
        Propellant gas energy generated for a given load/firearm combination
    """
    return charge_weight_in_grains * propellant_gas_velocity_multiplier(firearm_code) * muzzle_velocity_in_fps


# Primary Functions
def approximate_free_recoil_energy(firearm_code, firearm_weight_in_lbs, ejecta_weight_in_grains,
                                   charge_weight_in_grains, muzzle_velocity_in_fps, decimal_places=0):
    """Provides the approximate free recoil energy for a given load and firearm type combination

    Parameters
    ----------
    firearm_code : str
        Argument to use for the :func:`~ballistics.extras.propellant_gas_velocity_multiplier` function.
    firearm_weight_in_lbs : float
        Weight in lbs of the firearm plus any accessories.
    ejecta_weight_in_grains : float
        Weight in grains of the projectile plus wad (if fired from a shotgun).
    muzzle_velocity_in_fps : int
        Muzzle velocity for this load (field measurement or from loading manual reference table).
    charge_weight_in_grains : float
        Weight in grains of the powder charge.
    decimal_places : int, optional
        How many decimal places to return, (default value is 0 which returns the floor of the result).

    Returns
    -------
    int or float
        By default ``decimal_places`` is 0 which will return the nearest integer value.  If a value greater than 0 is
        passed in, the function will return a float value rounded to ``decimal_places``.

    Notes
    -----
    Refer to http://www.saami.org/PubResources/GunRecoilFormulae.pdf

    The accuracy of the value returned from this function is directly related to the accuracy of the charge
    weight and projectile velocity.
    """
    mass = firearm_weight_in_lbs / 64.34
    firearm_weight_in_grains = firearm_weight_in_lbs * 7000.0
    ejecta_energy = float(ejecta_weight_in_grains) * muzzle_velocity_in_fps
    propellant_energy = propellant_gas_energy(charge_weight_in_grains, firearm_code, muzzle_velocity_in_fps)
    velocity = pow((ejecta_energy + propellant_energy) / firearm_weight_in_grains, 2)
    if decimal_places:
        return round(mass * velocity, decimal_places)
    return int(round(mass * velocity))


def approximate_recoil_velocity(firearm_code, firearm_weight_in_lbs, ejecta_weight_in_grains, muzzle_velocity_in_fps,
                                charge_weight_in_grains, decimal_places=0):
    """Provides the approximate recoil velocity for a given load and firearm type combination

    Parameters
    ----------
    firearm_code : str
        Argument to use for the :func:`~ballistics.extras.propellant_gas_velocity_multiplier` function.
    firearm_weight_in_lbs : float
        Weight in lbs of the firearm plus any accessories.
    ejecta_weight_in_grains : float
        Weight in grains of the projectile plus wad (if fired from a shotgun).
    muzzle_velocity_in_fps : int
        Muzzle velocity for this load (field measurement or from loading manual reference table).
    charge_weight_in_grains : float
        Weight in grains of the powder charge.
    decimal_places : int, optional
        How many decimal places to return, (default value is 0 which returns the floor of the result).

    Returns
    -------
    int or float
        By default ``decimal_places`` is 0 which will return the nearest integer value.  If a value greater than 0 is
        passed in, the function will return a float value rounded to ``decimal_places``.

    Notes
    -----
    The accuracy of the value returned from this function is directly related to the accuracy of the charge
    weight and projectile velocity.
    """
    ejecta_energy = float(ejecta_weight_in_grains) * muzzle_velocity_in_fps
    firearm_weight_in_grains = firearm_weight_in_lbs * 7000.0
    propellant_energy = propellant_gas_energy(charge_weight_in_grains, firearm_code, muzzle_velocity_in_fps)
    velocity = (ejecta_energy + propellant_energy) / firearm_weight_in_grains
    if decimal_places:
        return round(velocity, decimal_places)
    return int(round(velocity))


def approximate_recoil_impulse(ejecta_weight_in_grains, muzzle_velocity_in_fps, charge_weight_in_grains, firearm_code=None):
    """Provides the approximate recoil impulse for a give

    Args:
        ejecta_weight_in_grains:
        muzzle_velocity_in_fps:
        charge_weight_in_grains:

    Returns:

    """
    ejecta_weight_in_kgs = ejecta_weight_in_grains * 0.0000648  # 1gr == 0.0000648kg
    charge_weight_in_kgs = charge_weight_in_grains * 0.0000648  # 1gr == 0.0000648kg
    muzzle_velocity_in_meters_per_second = muzzle_velocity_in_fps * 0.3048037 # 1ft == 0.30480370641307 meter
    ejecta_energy = ejecta_weight_in_kgs * muzzle_velocity_in_meters_per_second
    charge_energy = charge_weight_in_kgs * (GENERIC_PROPELLANT_GAS_VELOCITY * 0.3048037)  # propellant gas energy OR 5000 constant
    return round((ejecta_energy + charge_energy) * 0.224809, 2)  # 1 newton == 0.224809 pound force
