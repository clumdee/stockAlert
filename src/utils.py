import yfinance as yf


def get_stock_info(ticker="^IXIC", info="rsi"):
    """
    Return latest date and requested information of a target ticker.

    Parameters
    ----------
    ticker:
        Ticker to retrieve data from Yahoo Finance
    info:
        Information of the stock to return
        Only "price" and "rsi" are available

    Returns
    -------
    (dt, info):
        Tuple of latest date and requested info
    """

    # init object
    stck = yf.Ticker(ticker)

    # get historical close price
    s = stck.history(period="120d", interval="1d")["Close"]

    dt = s.index[-1].strftime("%Y-%m-%d")
    price = f"{s.iloc[-1]:.2f}"
    rsi = get_rsi(s, window=14)

    return (dt, price) if info == "price" else (dt, rsi)


def get_rsi(s, window=14):
    """
    Calculate RSI.

    Parameters
    ----------
    s:
        Pandas Series
    window:
        Calculation window

    Returns
    -------
    rsi:
        Latest RSI
    """

    # calculate change, gain, loss
    c = s - s.shift(1)
    g = c.clip(lower=0)
    l = c.clip(upper=0).abs()

    # smoothen gain and loss
    g_smma = g.ewm(
        alpha=1.0 / window, min_periods=0, adjust=True, ignore_na=False
    ).mean()
    l_smma = l.ewm(
        alpha=1.0 / window, min_periods=0, adjust=True, ignore_na=False
    ).mean()

    # calculate RSI
    rs = g_smma / l_smma
    rsi = 100 - 100 / (1 + rs)
    rsi = f"{rsi.iloc[-1]:.2f}"

    return rsi
