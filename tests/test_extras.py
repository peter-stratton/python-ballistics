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


def test_free_recoil_energy_for_average_length_shotgun_no_decimals():
    expect = 30
    result = ex.approximate_free_recoil_energy(firearm_code='ALS',
                                               firearm_weight_in_lbs=7.00,
                                               ejecta_weight_in_grains=589.9,
                                               charge_weight_in_grains=33.4,
                                               average_load_velocity_in_fps=1275)
    assert (expect == result)


def test_free_recoil_energy_for_average_length_shotgun_with_two_decimals():
    expect = 30.17
    result = ex.approximate_free_recoil_energy(firearm_code='ALS',
                                               firearm_weight_in_lbs=7.00,
                                               ejecta_weight_in_grains=589.9,
                                               charge_weight_in_grains=33.4,
                                               average_load_velocity_in_fps=1275,
                                               decimal_places=2)
    assert (expect == result)


def test_free_recoil_energy_for_high_powered_rifle_no_decimals():
    expect = 12
    result = ex.approximate_free_recoil_energy(firearm_code='HPR',
                                               firearm_weight_in_lbs=6,
                                               ejecta_weight_in_grains=170,
                                               charge_weight_in_grains=30,
                                               average_load_velocity_in_fps=2200)
    assert (expect == result)


def test_free_recoil_energy_for_high_powered_rifle_three_decimals():
    expect = 12.6671
    result = ex.approximate_free_recoil_energy(firearm_code='HPR',
                                               firearm_weight_in_lbs=6.0,
                                               ejecta_weight_in_grains=170.0,
                                               charge_weight_in_grains=30.0,
                                               average_load_velocity_in_fps=2200,
                                               decimal_places=4)
    assert (expect == result)
