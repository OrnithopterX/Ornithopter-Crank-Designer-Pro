import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from math import pi as PI

from src.planar_geometry import PlanarGeometry

class PlanarAnimation:
	def __init__(self, radius_input, radius_output, conrod \
	                 , x_input, x_output, y_output         \
	                 , fcrank = lambda x: x                \
	                 , flip_input = False                  ):
		# coordinates
		origin_input_L  = [-x_input, 0]
		origin_input_R  = [x_input , 0]
		origin_output_L = [-x_output, y_output]
		origin_output_R = [x_output , y_output]
		
		# patches
		radius_input_L = -radius_input if flip_input == True else radius_input
		self._geom_R = PlanarGeometry(radius_input, radius_output, conrod, origin_input_R, origin_output_R )
		self._geom_L = PlanarGeometry(radius_input_L,-radius_output, conrod, origin_input_L, origin_output_L )
				
	    # plot
		self._figure = plt.figure()  
		self._axis   = plt.axes()
			# axis limits
		xlim   = radius_output*1.1 + abs(x_output - x_input)
		ylim_p = radius_output*1.1 + y_output 
		ylim_n = -radius_input*1.1
		self._axis.set_xlim(-xlim , xlim)
		self._axis.set_ylim(ylim_n, ylim_p)
		self._axis.set_aspect('equal')
			# format axes
		self._axis.set_xlabel("x-axis")
		self._axis.set_ylabel("y-axis")
		self._axis.spines['top'].set_visible(False)
		self._axis.spines['right'].set_visible(False)	
		self._axis.ticklabel_format(useMathText=True, scilimits=(-2,2))
		# store crank function
		self._fcrank = fcrank
	
	#---- private
		
	def _finit(self):
		dataR = self._geom_R.add_patches(self._axis)
		dataL = self._geom_L.add_patches(self._axis)
		return tuple(dataR) + tuple(dataL)

	def _fanim(self, i):        
		angle_R = np.radians(i)
		angle_L = self._fcrank(angle_R)
		dataR = self._geom_R.update_position(angle_R)
		dataL = self._geom_L.update_position(angle_L)
		return tuple(dataR) + tuple(dataL)
	
	#---- public
	
	def animate(self):
		return animation.FuncAnimation( self._figure, self._fanim, init_func = self._finit,
                                		frames = 800, interval = 5, blit = True )
