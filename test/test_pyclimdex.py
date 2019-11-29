#!/usr/bin/env python
import pytest
import pandas
import xarray


def test_import():
    import pyclimdex

def read_sample_input(path):
    df = pandas.read_csv(path)

    dates = pandas.to_datetime(df['year'], format="%Y")
    dayofyear = pandas.to_timedelta(df['jday'], unit='day')
    dates += dayofyear
    dates = dates.rename('time')

    df = df.set_index(dates)
    s = df[df.columns[2]]

    return s


@pytest.fixture
def indices():
    from pyclimdex import climdex

    tmin = read_sample_input('test/climdex_data/1018935_MIN_TEMP.csv')
    tmax = read_sample_input('test/climdex_data/1018935_MAX_TEMP.csv')
    precip = read_sample_input('test/climdex_data/1018935_ONE_DAY_PRECIPITATION.csv')

    return climdex(tmin=tmin, tmax=tmax, precip=precip)

def test_index(indices):
    i = 'fd'

    expected = pandas.read_csv(f'test/climdex_data/indices/{i}.csv', index_col=0, header=0, names=['year','x']).to_xarray()
    xarray.testing.assert_equal(indices[i], expected.x)
