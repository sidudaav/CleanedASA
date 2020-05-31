# Name: RandomSim.py
# This program simulates 1 million MSE values for a theoretically random keyword

import numpy as np
import pandas as pd


def mse(in_list1, in_list2):
    val = 0
    for i in range(0, len(in_list1)):
        val = val + (in_list1[i] - in_list2[i]) ** 2;
    val = val / 50
    return val

def average(lst):
    return sum(lst) / len(lst)


def main():
    mse_holder = []
    count = 0

    for i in range(0, 1000000):
        vec1 = np.random.permutation(50)
        vec2 = np.random.permutation(50)
        val = mse(vec1, vec2)
        mse_holder.append(val)

        if val < 200:
            count = count + 1

    df = pd.DataFrame({
        "MSE": mse_holder
    })

    df.to_csv("ValRange")


main()





