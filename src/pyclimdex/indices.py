#!/usr/bin/env python
# Copyright 2019 ARC Centre of Excellence for Climate Extremes
# author: Scott Wales <scott.wales@unimelb.edu.au>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pandas
import xarray
from .utils import *


def _normalize_input(data):
    if data is None:
        return data

    if isinstance(data, xarray.DataArray):
        return data

    if isinstance(data, pandas.Series):
        da = data.to_xarray()
        return da

    if isinstance(data, pandas.DataFrame):
        raise TypeError(f"Please provide a pandas.Series or xarray.DataArray instead of {type(data)}")

    raise NotImplementedError


def climdex(tmin=None, tmax=None, tmean=None, precip=None):
    """
    Calculate all climdex indices
    """

    tmin = _normalize_input(tmin)
    tmax = _normalize_input(tmax)
    tmean = _normalize_input(tmean)
    precip = _normalize_input(precip)

    # Derive tmean if not given
    if tmean is None and (tmin is not None and tmax is not None):
        tmean = (tmin + tmax) / 2.0

    ds = xarray.merge([
        tmin_indices(tmin),])

    return ds

    
def tmin_indices(tmin):
    """
    Calculate all indices based on tmin
    """

    ds = xarray.Dataset({
        'fd': fd(tmin),
        })

    return ds


def fd(tmin):
    """
    Annual number of frost days
    """

    return count_days_in_year_where(tmin < 0)
