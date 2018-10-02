import pygal 
import numpy as np

x = np.arange(11)
x = x.astype(float)
y = np.random.randn(11)
chart = pygal.Line()
#(fill=True, zero=1)
chart.force_uri_protocol = 'http'
chart.x_title = '1-100 values'
chart.y_title = 'Random nos.'
chart.title = 'RANDOM VALUES'
chart.x_labels = x
chart.add('Random', y)
chart.render_to_file('Random.svg')
