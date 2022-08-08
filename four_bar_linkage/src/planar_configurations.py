from src.planar_animation import PlanarAnimation

#------ animation functions

def staggeredCrankAnim(radius_input, radius_output, conrod, x_output, y_output, ang_offset):
	fcrank = lambda x: x + ang_offset
	output = PlanarAnimation(radius_input, radius_output, conrod, 0, x_output, y_output, fcrank)
	return output.animate()

def duelCrankAnim(radius_input, radius_output, conrod, x_input, x_output, y_output):
	fcrank = lambda x: -x
	x_input += radius_input
	output = PlanarAnimation(radius_input, radius_output, conrod, x_input, x_output, y_output, fcrank, flip_input=True)
	return output.animate()
	
def insideOutCrankAnim(radius_input, radius_output, conrod, x_output, y_output):
	x_output += radius_output
	output = PlanarAnimation(radius_input, radius_output, conrod, 0, -x_output, y_output)
	return output.animate()	
