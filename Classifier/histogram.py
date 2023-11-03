import numpy as np
import random

def generate_x_bins(min, max, bins):
  return np.linspace(min,max,num=bins+1)

def generate_y_bins(min, max, bins):
  return np.logspace(min, max, num = bins, base = 10, endpoint = False)

def generate_2d_histogram(x_values,y_values,x_bins=None,y_bins=None, x_min = None, x_max = None, num_bins_x = None, y_min = None, y_max = None, num_bins_y = None):
  if x_bins is None:
    x_bins = generate_x_bins(x_min, x_max, num_bins_x)
  if y_bins is None:
    y_bins = generate_y_bins(y_min, y_max, num_bins_y)
  histogram, _, _ = np.histogram2d(x_values,y_values,bins = [x_bins, y_bins])
  histogram /= np.sum(histogram)
  histogram = histogram.T
  return histogram