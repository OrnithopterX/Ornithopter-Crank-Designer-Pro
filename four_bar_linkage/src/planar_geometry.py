import numpy as np
from matplotlib import pyplot as plt
from math import pi as PI

class PlanarGeometry:
	def __init__(self, radius_input, radius_output, conrod, origin_input, origin_output):
		# convert
		origin_input = np.array(origin_input)
		origin_output = np.array(origin_output)
		# geometry
		self._RADIUS_INPUT  = radius_input
		self._RADIUS_OUTPUT = radius_output
		self._CONROD        = conrod
		# origin coordinates
		self._ORIGIN_INPUT  = origin_input
		self._ORIGIN_OUTPUT = origin_output
        # squared lengths
		self._CONROD_SQ        = conrod**2
		self._RADIUS_INPUT_SQ  = radius_input**2
		self._RADIUS_OUTPUT_SQ = radius_output**2
        # origin distance
		self._ANG    = self._vectorAngle( origin_input, origin_output )		
		self._LEN    = np.linalg.norm(origin_output - origin_input)
		self._LEN_SQ = np.square(self._LEN)
		
		# define patches
			# bars
		vinput, voutput, vconrod = self._vectors(0)
		self._bar_input  = plt.Polygon( vinput,  closed = None, fill = None, ec = 'blue', lw = 3 )
		self._bar_output = plt.Polygon( voutput, closed = None, fill = None, ec = 'red', lw = 3 )
		self._bar_conrod = plt.Polygon( vconrod, closed = None, fill = None, ec = 'gray' , lw = 3 )
			# pins
		pin_size = np.sqrt( sum( np.square( [radius_input, radius_output, conrod] ) ) ) * 1.5e-2
				# static
		self._pin_input_origin  = plt.Circle( origin_input , pin_size, fc = 'yellow', ec='black' )
		self._pin_output_origin = plt.Circle( origin_output, pin_size, fc = 'yellow', ec='black' )
				# dynamic
		self._pin_input  = plt.Circle( self._posInput(0) , pin_size, fc = 'yellow', ec='black' )
		self._pin_output = plt.Circle( self._posOutput(0), pin_size, fc = 'yellow', ec='black' )

	#---- private
			
	def _posCircle(self, angle, radius):
		return np.array( [np.cos(angle), np.sin(angle)] )*radius
	
	def _posInput(self, angle):
		return self._posCircle(angle, self._RADIUS_INPUT) + self._ORIGIN_INPUT
		
	def _posOutput(self, angle):
		angle_out = self._outputAngle(angle)
		return self._posCircle(angle_out, self._RADIUS_OUTPUT) + self._ORIGIN_OUTPUT
	
	def _vectors(self, angle):
		p1 = self._posInput(angle)
		p2 = self._posOutput(angle)
		vinput  = [self._ORIGIN_INPUT , p1]
		voutput = [self._ORIGIN_OUTPUT, p2]
		vconrod = [p1, p2]
		return vinput, voutput, vconrod

	def _vectorAngle(self, p1, p2):
		dp = p2 - p1
		return np.arctan2( dp[1], dp[0] )
	
	def _outputAngle(self, angle):
		# crank-to-output length
		ang1   = self._ANG - angle
		len_sq = self._RADIUS_INPUT_SQ + self._LEN_SQ - 2*(self._RADIUS_INPUT)*(self._LEN)*np.cos(ang1)
		len    = np.sqrt(len_sq)
		# output angles
		ang2 = self._vectorAngle( self._posInput(angle), self._ORIGIN_OUTPUT )
		ang3 = np.arccos( (self._RADIUS_OUTPUT_SQ + len_sq - self._CONROD_SQ)/( 2*len*(self._RADIUS_OUTPUT) ) )
		return ang3 + ang2 - PI

	def _drawFrame(self, axis):
		x1 = self._ORIGIN_INPUT[0]
		x2 = self._ORIGIN_OUTPUT[0]
		y2 = self._ORIGIN_OUTPUT[1]
		axis.plot( [0, 0] , [0, y2] , lw=2, color='black', alpha=0.5)
		axis.plot( [0, x1], [0, 0]  , lw=2, color='black', alpha=0.5)
		axis.plot( [0, x2], [y2, y2], lw=2, color='black', alpha=0.5)

	#---- Public
	
	def add_patches(self, axis):
		# frame
		self._drawFrame(axis)
		# bars
		axis.add_patch( self._bar_input )
		axis.add_patch( self._bar_output )
		axis.add_patch( self._bar_conrod )
		# pins
		axis.add_patch( self._pin_input )
		axis.add_patch( self._pin_output )
		axis.add_patch( self._pin_input_origin )
		axis.add_patch( self._pin_output_origin )
		# output
		return self._bar_input, self._bar_output, self._bar_conrod \
		      ,self._pin_input, self._pin_output 

	def update_position(self, angle):
		# bars
		vinput, voutput, vconrod = self._vectors(angle)
		self._bar_input.set_xy( vinput )
		self._bar_output.set_xy( voutput )
		self._bar_conrod.set_xy( vconrod )
		# pins
		self._pin_input.center  = self._posInput(angle)
		self._pin_output.center = self._posOutput(angle)
		# output
		return self._bar_input, self._bar_output, self._bar_conrod \
		      ,self._pin_input, self._pin_output               
