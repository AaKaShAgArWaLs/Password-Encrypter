import numpy as np

def reshape_list(s, m):
    rows_m, cols_m = len(m), len(m[0])
    total_elements = rows_m * cols_m

    if len(s) < total_elements:
        # Add zeros to the end of the list
        s += [0] * (total_elements - len(s))
    elif len(s) > total_elements:
        raise ValueError("The total number of elements in s should be less than or equal to the total elements in m.")

    reshaped_s = np.array(s).reshape((rows_m, cols_m)).tolist()
    
    return reshaped_s


