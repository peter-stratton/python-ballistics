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
                                               muzzle_velocity_in_fps=1275)
    assert (expect == result)


def test_free_recoil_energy_for_average_length_shotgun_with_two_decimals():
    expect = 30.17
    result = ex.approximate_free_recoil_energy(firearm_code='ALS',
                                               firearm_weight_in_lbs=7.00,
                                               ejecta_weight_in_grains=589.9,
                                               charge_weight_in_grains=33.4,
                                               muzzle_velocity_in_fps=1275,
                                               decimal_places=2)
    assert (expect == result)


def test_free_recoil_energy_for_high_powered_rifle_no_decimals():
    expect = 13
    result = ex.approximate_free_recoil_energy(firearm_code='HPR',
                                               firearm_weight_in_lbs=6,
                                               ejecta_weight_in_grains=170,
                                               charge_weight_in_grains=30,
                                               muzzle_velocity_in_fps=2200)
    assert (expect == result)


def test_free_recoil_energy_for_high_powered_rifle_three_decimals():
    expect = 12.6671
    result = ex.approximate_free_recoil_energy(firearm_code='HPR',
                                               firearm_weight_in_lbs=6.0,
                                               ejecta_weight_in_grains=170.0,
                                               charge_weight_in_grains=30.0,
                                               muzzle_velocity_in_fps=2200,
                                               decimal_places=4)
    assert (expect == result)


def test_free_recoil_energy_one_decimal_matches_chuck_hawks_6mm_rem():
    expect = 10.0
    result = ex.approximate_free_recoil_energy(firearm_code='HPR',
                                               firearm_weight_in_lbs=8,
                                               ejecta_weight_in_grains=100,
                                               charge_weight_in_grains=35.5,
                                               muzzle_velocity_in_fps=3100,
                                               decimal_places=1)
    assert (expect == result)


def test_approximate_recoil_velocity_one_decimal_matches_chuck_haweks_6mm_rem():
    expect = 9.0
    result = ex.approximate_recoil_velocity(firearm_weight_in_lbs=8,
                                            ejecta_weight_in_grains=100,
                                            muzzle_velocity_in_fps=3100,
                                            charge_weight_in_grains=35.5,
                                            firearm_code='HPR',
                                            decimal_places=1)
    assert (expect == result)


def test_free_recoil_energy_no_decimal_matches_chuck_hawks_6mm_rem():
    expect = 10
    result = ex.approximate_free_recoil_energy(firearm_code='HPR',
                                               firearm_weight_in_lbs=8,
                                               ejecta_weight_in_grains=100,
                                               charge_weight_in_grains=35.5,
                                               muzzle_velocity_in_fps=3100)
    assert (expect == result)


def test_approximate_recoil_velocity_no_decimal_matches_chuck_haweks_6mm_rem():
    expect = 9
    result = ex.approximate_recoil_velocity(firearm_weight_in_lbs=8,
                                            ejecta_weight_in_grains=100,
                                            muzzle_velocity_in_fps=3100,
                                            charge_weight_in_grains=35.5,
                                            firearm_code='HPR')
    assert (expect == result)


def test_free_recoil_recoil_energy_one_decimal_matches_chuck_hawks_270_win():
    expect = 17.1
    result = ex.approximate_free_recoil_energy(firearm_code='HPR',
                                               firearm_weight_in_lbs=8,
                                               ejecta_weight_in_grains=140,
                                               charge_weight_in_grains=45,
                                               muzzle_velocity_in_fps=3000,
                                               decimal_places=1)
    assert (expect == result)


def test_approximate_recoil_velocity_one_decimal_matches_chuck_hawks_270_win():
    expect = 11.7
    result = ex.approximate_recoil_velocity(firearm_weight_in_lbs=8,
                                            ejecta_weight_in_grains=140,
                                            muzzle_velocity_in_fps=3000,
                                            charge_weight_in_grains=45,
                                            firearm_code='HPR',
                                            decimal_places=1)
    assert (expect == result)


def test_free_recoil_recoil_energy_no_decimal_matches_chuck_hawks_270_win():
    expect = 17
    result = ex.approximate_free_recoil_energy(firearm_code='HPR',
                                               firearm_weight_in_lbs=8,
                                               ejecta_weight_in_grains=140,
                                               charge_weight_in_grains=45,
                                               muzzle_velocity_in_fps=3000)
    assert (expect == result)


def test_approximate_recoil_velocity_no_decimal_matches_chuck_hawks_270_win():
    expect = 12
    result = ex.approximate_recoil_velocity(firearm_weight_in_lbs=8,
                                            ejecta_weight_in_grains=140,
                                            muzzle_velocity_in_fps=3000,
                                            charge_weight_in_grains=45,
                                            firearm_code='HPR')
    assert (expect == result)


# http://www.shooterscalculator.com/
def test_approximate_recoil_impulse_generic_two_decimals_01():
    expect = 2.33  # lbs sec
    result = ex.approximate_recoil_impulse(ejecta_weight_in_grains=100,
                                           muzzle_velocity_in_fps=3000,
                                           charge_weight_in_grains=45,
                                           decimal_places=2)
    assert (expect == result)


def test_approximate_recoil_impulse_generic_no_decimals_01():
    expect = 2  # lbs sec
    result = ex.approximate_recoil_impulse(ejecta_weight_in_grains=100,
                                           muzzle_velocity_in_fps=3000,
                                           charge_weight_in_grains=45)
    assert (expect == result)


def test_approximate_recoil_with_firearm_code_two_decimals_01():
    expect = 2.38  # lbs sec
    result = ex.approximate_recoil_impulse(ejecta_weight_in_grains=100,
                                           muzzle_velocity_in_fps=3000,
                                           charge_weight_in_grains=45,
                                           firearm_code='HPR',
                                           decimal_places=2)
    assert (expect == result)


# http://www.shooterscalculator.com/
def test_approximate_recoil_impulse_generic_two_decimals_02():
    expect = 3.66  # lbs sec
    result = ex.approximate_recoil_impulse(ejecta_weight_in_grains=200,
                                           muzzle_velocity_in_fps=3000,
                                           charge_weight_in_grains=45,
                                           decimal_places=2)
    assert (expect == result)


def test_approximate_recoil_impulse_generic_no_decimals_02():
    expect = 4  # lbs sec
    result = ex.approximate_recoil_impulse(ejecta_weight_in_grains=200,
                                           muzzle_velocity_in_fps=3000,
                                           charge_weight_in_grains=45)
    assert (expect == result)


def test_approximate_recoil_impulse_with_firearm_code_two_decimals_02():
    expect = 3.71  # lbs sec
    result = ex.approximate_recoil_impulse(ejecta_weight_in_grains=200,
                                           muzzle_velocity_in_fps=3000,
                                           charge_weight_in_grains=45,
                                           firearm_code='HPR',
                                           decimal_places=2)
    assert (expect == result)


# http://www.shooterscalculator.com/
def test_approximate_recoil_impulse_generic_03():
    expect = 2.18  # lbs sec
    result = ex.approximate_recoil_impulse(ejecta_weight_in_grains=150,
                                           muzzle_velocity_in_fps=2100,
                                           charge_weight_in_grains=35,
                                           decimal_places=2)
    assert (expect == result)


def test_approximate_recoil_impulse_with_firearm_code_03():
    expect = 1.97  # lbs sec
    result = ex.approximate_recoil_impulse(ejecta_weight_in_grains=150,
                                           muzzle_velocity_in_fps=2100,
                                           charge_weight_in_grains=35,
                                           firearm_code='HPR',
                                           decimal_places=2)
    assert (expect == result)


# http://www.shooterscalculator.com/
def test_free_recoil_energy_no_firearm_code_01():
    expect = 12.69
    result = ex.approximate_free_recoil_energy(firearm_weight_in_lbs=6,
                                               ejecta_weight_in_grains=150,
                                               charge_weight_in_grains=35,
                                               muzzle_velocity_in_fps=2100,
                                               decimal_places=2)
    assert (expect == result)


# http://www.shooterscalculator.com/
def test_free_recoil_energy_no_firearm_code_02():
    expect = 16.49
    result = ex.approximate_free_recoil_energy(firearm_weight_in_lbs=8,
                                               ejecta_weight_in_grains=140,
                                               muzzle_velocity_in_fps=3000,
                                               charge_weight_in_grains=45,
                                               decimal_places=2)
    assert (expect == result)


# http://www.shooterscalculator.com/
def test_approx_recoil_velocity_no_firearm_code_01():
    expect = 11.67
    result = ex.approximate_recoil_velocity(firearm_weight_in_lbs=6,
                                            ejecta_weight_in_grains=150,
                                            muzzle_velocity_in_fps=2100,
                                            charge_weight_in_grains=35,
                                            decimal_places=2)
    assert (expect == result)


# http://www.shooterscalculator.com/
def test_approx_recoil_velocity_no_firearm_code_02():
    expect = 11.52
    result = ex.approximate_recoil_velocity(firearm_weight_in_lbs=8,
                                            ejecta_weight_in_grains=140,
                                            muzzle_velocity_in_fps=3000,
                                            charge_weight_in_grains=45,
                                            decimal_places=2)
    assert (expect == result)
