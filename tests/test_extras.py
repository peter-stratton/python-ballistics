# -*- coding: utf-8 -*-
""" ballistics.extras module tests """
import pytest

import ballistics.extras as ex


def test_propellant_gas_velocity_constants_for_rifle():
    assert 1.75 == ex.PROPELLANT_GAS_VELOCITY_CONSTANTS['HighPoweredRifle']


def test_propellant_gas_velocity_constants_for_average_length_shotgun():
    assert 1.50 == ex.PROPELLANT_GAS_VELOCITY_CONSTANTS['AverageLengthShotgun']


def test_propellant_gas_velocity_constants_for_long_barrel_shotgun():
    assert 1.25 == ex.PROPELLANT_GAS_VELOCITY_CONSTANTS['LongBarrelShotgun']


def test_propellant_gas_velocity_constants_for_pistol_and_revolover():
    assert 1.50 == ex.PROPELLANT_GAS_VELOCITY_CONSTANTS['PistolAndRevolver']


def test_propellant_gas_velocity_upper_case_arg():
    assert 1.75 == ex.propellant_gas_velocity_multiplier('HPR')


def test_propellant_gas_velocity_lower_case_arg():
    assert 1.50 == ex.propellant_gas_velocity_multiplier('als')


def test_propellant_gas_velocity_multiplier_raises_key_error():
    with pytest.raises(KeyError):
        ex.propellant_gas_velocity_multiplier('xxx')


def test_propellant_gas_velocity_multiplier_requires_firearm_code():
    with pytest.raises(TypeError):
        ex.propellant_gas_velocity_multiplier()
