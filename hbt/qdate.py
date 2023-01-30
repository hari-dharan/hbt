from pandas.tseries.offsets import BMonthEnd
from pandas.tseries.offsets import MonthBegin
import pandas as pd
from collections import OrderedDict

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