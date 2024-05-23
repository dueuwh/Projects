import numpy as np
import typing as t

def taylor_diff(input_list: t.Union[list, np.ndarray], order: int)-> list:
    if order > len(input_list):
        raise ValueError(f"order is larger than the length of input: order:{order}, len(input):{len(input_list)}")

