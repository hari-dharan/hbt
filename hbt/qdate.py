from pandas.tseries.offsets import BMonthEnd
from pandas.tseries.offsets import MonthBegin
import pandas as pd
from collections import OrderedDict

def freq_to_date_type(freq):
    '''
    Translation function for frequency
    D - Weekday to Weekday
    D2 - Daily
    W - EOW to EOW
    M - LDM to LDM
    M2 - EOM to EOM
    Q - EOQ to EOQ
    Y - EOY to EOY
    '''
    pass

def freq_to_lag_type(freq, freq_to_lag=True):
    '''
    Translation function from frequency to the lag type
    Freq types
    D - Weekdays
    D2 - Daily
    W - EOW
    M - LDM
    M2 - EOM
    Q - EOQ
    Y - EOY

    Lag types
    B - Weekdays
    D - Daily
    EOW - EOW
    LDM - LDM
    EOM - EOM
    EOQ - EOQ
    EOY - EOY
    '''
    pass

def date_seq(start="1995-01-01", end=pd.to_datetime("today"), freq="D", interval="N"):
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    assert start < end
    assert start.tz_localize(None) >= pd.to_datetime("1923-01-08")
    assert end.tz_localize(None) <= pd.to_datetime("2079-01-01")
    assert freq in ("D", "W", "M")
    assert freq in ("L", "R", "B")

    date_vec = pd.date_range(start=start, end=end, freq="D")
    if freq == "M":
        date_vec = [pd.to_datetime(i) + BMonthEnd(0) for i in date_vec]
    elif freq == "W":
        date_vec = [pd.to_datetime(i) - pd.to_timedelta((i.weekday()-4)%-7, unit="d") for i in date_vec]
    elif freq == "D":
        date_vec = [pd.to_datetime(i) for i in date_vec if i.weekday() not in (5,6)]
    
    date_vec = [i for i in date_vec if i >= start and i <= end]

    if interval == "L":
        date_vec = [start] + date_vec
    elif interval == "R":
        date_vec = date_vec + [end]
    elif interval == "B":
        date_vec = [start] + date_vec + [end]
    else:
        pass
    
    return list(OrderedDict.fromkeys([pd.to_datetime(i.strftime("%Y-%m-%d")) for i in date_vec]))

def date_lag(dates, lag=0, lag_type="D"):
    '''
    Lag dates by well known frequency
    '''
    pass

def date_minus_wdays(dates, n=1):
    '''
    Minus n weekdays/business days to each of the dates
    '''
    pass

def date_fdm(dates, weekday_flag=True):
    '''
    Get the first day/weekday of the month
    '''
    pass

def date_ldm(dates, lookback=False):
    '''
    Get the last weekday of the month
    '''
    pass

def date_eom(dates):
    '''
    Get the last day of the month
    '''
    pass

def date_ldy(dates, lookback=False):
    '''
    Get the last weekday of the year
    '''
    pass