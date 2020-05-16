#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.dates as mdates
import matplotlib as mpl

title_font = {'fontweight':'bold', 'fontsize':22}
label_font = {'weight':'bold', 'fontsize': 15}

class Graph:
    plt.style.use('ggplot')
    
    def __init__(self, chart_name, ylabel, xlabel):
        self.chart_name = chart_name
        self.ylabel = ylabel
        self.xlabel = xlabel
        self.fig, self.ax = plt.subplots(num='COVID-19', figsize=(15,7))

    def set_info(self):
        self.ax.set_title(self.chart_name, fontdict=title_font)
        self.ax.set_xlabel(self.xlabel.title(), fontdict=label_font)
        self.ax.set_ylabel(self.ylabel.title(), fontdict=label_font)

    def ajust_graph(self):
        plt.xticks(fontsize=10, rotation=50, ha="right")
        plt.yticks(fontsize=10)
        self.ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
        self.ax.xaxis.set_major_locator(mdates.WeekdayLocator())
        plt.legend(loc=2)
        plt.tight_layout()
        plt.margins(x=0)