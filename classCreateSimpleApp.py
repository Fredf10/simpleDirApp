'''
Created on Oct 5, 2016

@author: fredrik
'''
'''
Created on Oct 3, 2016

@author: fredrik
'''

import numpy as np
import os
from os.path import dirname, join
from bokeh.plotting import Figure
from bokeh.models import ColumnDataSource, Range1d
from bokeh.models.widgets import Select

import h5py


class SetupApp:
    
    def __init__(self):
        
        
        self.lineType = "linear"
        X, Y = self.load_data()
        
        self.source = ColumnDataSource(data=dict(x=X, y=Y))
        # Set up plot_line y = a*x + b
        self.plot_line = Figure(plot_height=300, plot_width=400, title="y = a*x + b",
                            x_axis_label="x", y_axis_label="y",
                            tools="crosshair,pan,reset,resize,save,wheel_zoom",
                            x_range=[0, 1], y_range=[0, 1]
                            )
        
        self.plot_line.line('x', 'y', source=self.source, color='black', line_alpha=0.6, line_width=2)

        localUrl = "simpleDirApp/static/red.png"
         
        self.sourceImg = ColumnDataSource(data=dict(url = [localUrl]))
         
        self.plot_Img = Figure(plot_width=300, plot_height=400)
        self.plot_Img.x_range = Range1d(start=0, end=1)
        self.plot_Img.y_range = Range1d(start=0, end=1)
        self.plot_Img.image_url(url='url', x=0, y=1, h=1, w=1, source=self.sourceImg)
        
        self.lineSelect = Select(title="selcet line", value="linear", options=["linear", "power"])
        self.imageSelect = Select(title="select image", value="red", options=["red", "black"])


        self.Widgetlist = [self.lineSelect, self.imageSelect]
        
    def update_data(self, attrname, old, new):
    
        
        self.lineType = self.lineSelect.value
        self.imageType = self.imageSelect.value
        
        localUrl = "simpleDirApp/static/" + self.imageType + ".png"
        self.sourceImg.data = dict(url=[localUrl])
        self.plot_Img.image_url(url='url', x=0, y=1, h=1, w=1, source=self.sourceImg)
        
        X, Y = self.load_data(relFilePath=True)
        print X[10], Y[10]
        
        self.source.data = dict(x=X, y=Y)
        
    def load_data(self, relFilePath=False):
        file_line = self.lineType + ".txt"
        if relFilePath:
            file_path = join('simpleDirApp', 'data', file_line)
            
        else:
            file_path = join(dirname(__file__), 'data', file_line)
        f1 = open(file_path, 'r')
        X = []
        Y = []
        
        for line in f1:
            x = float(line.split(',')[0])
            y = float(line.split(',')[1])
            X.append(x)
            Y.append(y)
        f1.close()
        
        return X, Y
