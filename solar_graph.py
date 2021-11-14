# coding: utf-8
# license: GPLv3

import numpy as np
import matplotlib.pyplot as plt


def vt_graph(data):
    """"
    """
    plt.xlabel('t')
    plt.ylabel('v')
    plt.plot(data[0], data[1])
    plt.show()

def rt_graph(data):
    """"
    """
    plt.xlabel('t')
    plt.ylabel('r')
    plt.plot(data[0], data[2])
    plt.show()

def vr_graph(data):
    """"
    """
    plt.xlabel('r')
    plt.ylabel('v')
    plt.plot(data[2], data[1])
    plt.show()