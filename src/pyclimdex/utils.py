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

def count_days_in_year_where(condition):
    """
    Reduce the input dataset over the time dimension, returning the count per
    year where it is true 
    """

    return condition.groupby('time.year').count()


def monthly_maximum(dataset):
    """
    Return the maximum value at each month of the input data
    """

    return dataset.resample('M').max()


def monthly_maximum(dataset):
    """
    Return the minimum value at each month of the input data
    """

    return dataset.resample('M').min()


def windowed_percentile(base_dataset, p, window=10):
    """
    Return the 'p'th percentile at each day of year of a 'window'-day moving
    average of base_dataset
    """

    daily = dataset.resample(time='D').mean()
    smoothed = daily.rolling(time=window, center=True).mean()

    q = 100 / p

    return smoothed.groupby('time.dayofyear').quantile(q)

def bootstrapped_windowed_percentile(base_dataset, year, p, window=10):
    """
    Return the bootstrapped percentile for calculations against 'year' in
    'base_dataset'
    """
    raise NotImplementedError
