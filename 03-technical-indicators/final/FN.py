import numpy as np
from typing import Dict

# Set NumPy print options to suppress scientific notation for small numbers
np.set_printoptions(suppress=True)


def GetData(id: str) -> np.ndarray:
    """
    Fetches stock data for a given id over May to July 2021.
    Processes data to include day, open, high, low, close, and volume.

    Parameters:
    - id (str): Stock id.

    Returns:
    - np.ndarray: Processed data array.
    """

    o5data = open('./data/STOCK_DAY_' + id + '_202105.csv').readlines()
    o5data_1 = o5data[2:-5]  # Remove the header and footer
    p5data = [line.strip('\n').lstrip('"').rstrip('",') for line in o5data_1]
    p5data_1 = [line.split('","') for line in p5data]
    s5data = np.asarray(p5data_1)
    o6data = open('./data/STOCK_DAY_' + id + '_202106.csv').readlines()
    o6data_1 = o6data[2:-5]  # Remove the header and footer
    p6data = [line.strip('\n').lstrip('"').rstrip('",') for line in o6data_1]
    p6data_1 = [line.split('","') for line in p6data]
    s6data = np.asarray(p6data_1)
    o7data = open('./data/STOCK_DAY_' + id + '_202107.csv').readlines()
    o7data_1 = o7data[2:-5]  # Remove the header and footer
    p7data = [line.strip('\n').lstrip('"').rstrip('",') for line in o7data_1]
    p7data_1 = [line.split('","') for line in p7data]
    s7data = np.asarray(p7data_1)

    mdataset = np.vstack((s5data, s6data, s7data))

    # Original data contains commas for thousands, which need to be removed for string conversion to numbers
    # Remove commas from the opening price
    op_1 = np.delete(mdataset, [0, 1, 2, 4, 5, 6, 7, 8], 1)
    op_2 = [",".join(i) for i in op_1.astype(str)]
    op_3 = [w.replace(",", "") for w in op_2]
    op_4 = np.asarray(op_3).reshape(-1, 1)

    # Remove commas from the highest price
    hp_1 = np.delete(mdataset, [0, 1, 2, 3, 5, 6, 7, 8], 1)
    hp_2 = [",".join(i) for i in hp_1.astype(str)]
    hp_3 = [w.replace(",", "") for w in hp_2]
    hp_4 = np.asarray(hp_3).reshape(-1, 1)

    # Remove commas from the lowest price
    lp_1 = np.delete(mdataset, [0, 1, 2, 3, 4, 6, 7, 8], 1)
    lp_2 = [",".join(i) for i in lp_1.astype(str)]
    lp_3 = [w.replace(",", "") for w in lp_2]
    lp_4 = np.asarray(lp_3).reshape(-1, 1)

    # Remove commas from the closing price
    cp_1 = np.delete(mdataset, [0, 1, 2, 3, 4, 5, 7, 8], 1)
    cp_2 = [",".join(i) for i in cp_1.astype(str)]
    cp_3 = [w.replace(",", "") for w in cp_2]
    cp_4 = np.asarray(cp_3).reshape(-1, 1)

    # Remove commas from the volume
    volume_1 = np.delete(mdataset, [0, 1, 2, 3, 4, 5, 6, 7], 1)
    volume_2 = [",".join(i) for i in volume_1.astype(str)]
    volume_3 = [w.replace(",", "") for w in volume_2]
    volume_4 = np.asarray(volume_3).reshape(-1, 1)  # 成交量

    # Generate time
    day = np.arange(1,65).reshape(-1, 1) # 5、6、7月共有64個交易日

    # Combine
    mdataset_1 = np.hstack((day, op_4, hp_4, lp_4, cp_4, volume_4)) # 交易日、ohlc、成交量
    mdataset_2 = np.float_(mdataset_1)  # 轉為浮點數

    return mdataset_2


def GetTaKbar(id: str) -> Dict[str, np.ndarray]:
    """
    Prepares stock data for technical analysis with TA-Lib.
    Transforms data into a dictionary format suitable for TA-Lib indicators.

    Parameters:
    - id (str): Stock ID.

    Returns:
    - Dict[str, np.ndarray]: Data dictionary for open, high, low, close, and volume.
    """

    Kbar = GetData(id)
    TaKbar = {}
    TaKbar['time'] = np.array([ l[0] for l in Kbar])
    TaKbar['open'] = np.array([ l[1] for l in Kbar])
    TaKbar['high'] = np.array([ l[2] for l in Kbar])
    TaKbar['low'] = np.array([ l[3] for l in Kbar])
    TaKbar['close'] = np.array([ l[4] for l in Kbar])
    TaKbar['volume'] = np.array([ l[5] for l in Kbar])

    return TaKbar
