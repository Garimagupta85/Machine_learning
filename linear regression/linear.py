
from numpy import *


def compute_error(b, m, points):
	totalerror = 0
	for i in range(0, len(points)):
		x = points[i ,0]
		y = points[i, 1]
		totalerror +=(y -(m*x+b)) ** 2
	return totalerror / float(len(points))

def step_gradient(b_current, m_current, points, learningrate):
	b_updated = 0
	m_updated = 0
	N = float(len(points))
	for i in range(0, len(points)):
		x = points[i ,0]
		y = points[i, 1]
		b_updated += -(2/N) * (y- ((m_current * x) + b_current))
		m_updated += -(2/N) * x * (y - ((m_current * x) + b_current))
	new_b = b_current - (learningrate * b_updated)
	new_m = m_current - (learningrate * m_updated)
	return [new_b, new_m]

def gradient_decent(points, starting_b, starting_m, learningrate, number_itera):
    b = starting_b
    m = starting_m
    for i in range(number_itera):
    	b, m = step_gradient(b, m, array(points), learningrate)
    return [b, m]

def run():
	points = genfromtxt("data.csv" , delimiter=",")
	learningrate = 0.0001
	initial_b = 0
	initial_m = 0
	number_itera = 1000
	print "Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error(initial_b, initial_m, points))"
	print "RUNNING"
	[b, m] = gradient_decent(points, initial_b, initial_m, learningrate, number_itera)
	print "after {0} iterations b = {1}, m = {2}, error = {3}".format(number_itera, b, m, compute_error(b, m, points))

if __name__ == '__main__' :
	run()
