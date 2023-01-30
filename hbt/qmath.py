import numpy as np
import pandas as pd
from scipy.stats import norm

def qmath_rescale(x, lb=0.001, ub=0.999):
    '''
    Linearly rescale x to min_x and max_x

    Parameters
    ----------
    x : pandas.Series
        The unscaled series
    lb : float
        The lower bound
    ub : float
        The upper bound
    
    Returns
    -------
    x_s : pandas.Series
        The linearly scaled series
    '''
    assert isinstance(x, pd.Series)
    assert x.dtype == "float"
    assert ub is not None

    if np.nanmin(x) == np.nanmax(x):
        if lb is None:
            x_s = pd.Series(np.repeat(ub, x.size))
        else:
            x_s = pd.Series(np.repeat((lb+ub)/2, x.size))
        
        x_s[np.isnan(x)] = np.nan
        return x_s
    else:
        if lb is None:
            if ub <= 0:
                raise Exception("Unable to evaluate when lb is None and ub <= 0")
            x_s = x*ub/np.nanmax(x)
        else:
            x_s = (ub - lb) * (x - np.nanmin(x)) / (np.nanmax(x) - np.nanmin(x)) + lb
        return x_s

def qmath_rank(x, highlow=1, na_option="bottom"):
    '''
    Rank a series

    Parameters
    ----------
    x : pandas.Series
        The unranked series
    highlow : int
        Method to transform
    na_option : str
        How to rank NaN values:
        - keep: assign NaN rank to NaN values
        - top: assign lowest rank to NaN values
        - bottom: assign highest rank to NaN values
    
    Returns
    -------
    x_r : pandas.Series
        The ranked series
    '''
    assert isinstance(x, pd.Series)
    assert isinstance(na_option, str)
    assert na_option in ("keep", "top", "bottom")

    mod_x = ((1 - highlow) * -x + highlow * x)
    x_r = mod_x.rank(method="average", na_option=na_option)
    x_r[pd.isna(mod_x)] = np.nan
    
    return x_r

def qmath_norm(x, method="invnorm"):
    '''
    Normalize series

    Parameters
    ----------
    x : pandas.Series
        The unnormalized series
    method : str
        Method for transformation. One of invnorm, sum_abs, zscore
    
    Returns
    -------
    x_n : pandas.Series
        The normalized series
    '''
    assert isinstance(x, pd.Series)
    assert isinstance(method, str)
    assert method in ("invnorm", "sum_abs", "zscore")

    if method == "sum_abs":
        x_n = x/np.abs(x).sum()
    elif method == "invnorm":
        x_n = qmath_rescale(qmath_rank(x, highlow=1, na_option="bottom"), lb=0.001, ub=0.999).apply(norm.ppf)
    elif method == "zscore":
        x_n = (x - x[~pd.isna(x)].mean()) / np.std(x[~pd.isna(x)], ddof=1)
    
    return x_n

def qmath_winsorize(x, winsorize_size=2, winsorize_method="sd", trim=False, ends=("H", "T")):
    '''
    x : vector
    winsorize_size : str
        - sd: number of sd
        - median: number of median bands
        - prank: rank percentile of the upperbound, lowerbound is mirrored
        - quantile: quantile of upperbound
        - huber: keep exact bounds
    winsorize_method : str
        - sd: band is sd
        - median: band is median of abs diff between vec and median
        - prank: keep the percentile
        - huber: keep exact bounds
    trim : bool
        whether to fill outliers with NA or replace with boundary value
    ends : can only be within ("H", "T"). H winsorize the head, T winsorize the tail
    '''
    pass

def qmath_ma():
    '''
    Moving Average Smoothing
    '''
    pass

def qmath_ewma(ts, n=0, lambda_=0.94, na_rm=False):
    '''
    Exponentially Weighted Moving Average Smoothing

    Parameters
    ----------
    ts : 

    n : int

    lambda_ : float

    na_rm : boolean
        Flag to remove NA

    Returns
    -------
    ewma :     
    '''
    if na_rm:
        ts = ts.dropna()
    if len(ts) == 0:
        return np.nan
    if n == 0:
        n = len(ts)
    
    w = [lambda_ ** i for i in range(len(ts) - 1, -1, -1)]
    ewma = ts.dot(w) / sum(w)
    return ewma

def qmath_ewsd():
    '''
    Exponential Weighted Standard Deviation
    '''
    pass

def qmath_ewcov():
    '''
    Exponential Weighted Covariance
    '''
    pass

def qmath_holtwinters():
    '''
    Holt Winters Smoothing
    '''
    pass

def qmath_neutralize():
    '''
    Function that takes in dependent and independent variables 
    and returns residuals of linear regression
    '''
    pass

def qmath_pca():
    '''
    Principal Components
    '''
    pass

def qmath_solve_lp():
    '''
    Solve Linear Programming Problem
    '''
    pass

def qmath_solve_qp():
    '''
    Solve Quadratic Programming Problem
    '''
    pass