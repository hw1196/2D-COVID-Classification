# Histograms
## generate_x_bins


Generates an array of bin edges for the x-axis for a 2d histogram

### Parameters

- `min` (float): The minimum value for a bin edge.
- `max` (float): The maximum value for a bin edge. 
- `bins` (int): The number of bins to generate.

### Returns

- `x_bins` (array): An array of bin edges for the x-axis. The bin edges are in linear scale. 
## generate_y_bins


Generates an array of bin edges for the y-axis for a 2d histogram. 

### Parameters

- `min` (float): The minimum value for the y-axis in logarithmic space.
- `max` (float): The maximum value for the y-axis in logarithmic space.
- `bins` (int): The number of bins to generate.

### Returns

- `y_bins` (array): An array of bin edges for the y-axis on a logarithmic scale.

## generate_2d_histogram

Generates a 2D histogram based on an array of x-values, an array of y-values, and the x and y bin edges. 

### Parameters

- `x_values` (array-like): All the x-coordinates of the data points. 
- `y_values` (array-like): All the y-coordinates of the data points corresponding to the values of x in `x-values.`
- `x_bins` (array-like, optional): The bin edges for the x-axis. If not provided, they will be generated with the minimum bin edge, the maximum bin edge, and the number of bins. 
- `y_bins` (array-like, optional): The bin edges for the x-axis. If not provided, they will be generated with the minimum bin edge, the maximum bin edge, and the number of bins. 
- `x_min` (float, optional): The minimum value for the x-axis. 
- `x_max` (float, optional): The maximum value for the x-axis. 
- `num_bins_x` (int, optional): The number of bins to use for the x-axis bins.
- `y_min` (float, optional): The minimum value for the y-axis. 
- `y_max` (float, optional): The maximum value for the y-axis. 
- `num_bins_y` (int, optional): The number of bins to use for the y-axis. 

### Returns

- `histogram` (2D array): The 2D histogram distribution of the data points. The values are normalized to sum to 1.

