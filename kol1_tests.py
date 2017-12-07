import unittest
from kol1 import Vehicle
from kol1 import Simulation
import math
from contextlib import contextmanager
import __builtin__

@contextmanager
def mockRawInput(mock_value):
	original_raw_input = __builtin__.raw_input
	__builtin__.raw_input = lambda prompt='': mock_value.next()
	yield 
	__builtin__.raw_input = original_raw_input

def my_generator(li):
	for i in li:
		yield i
class MyTest(unittest.TestCase):

	def setUp(self):
		self.test_vehicle_instance = Vehicle("Plane")
		self.test_simulation_instance = Simulation(self.test_vehicle_instance, 0.4, 1,0.5)

	def test_init(self):
		self.assertEqual(self.test_vehicle_instance.type_of_vehicle, "Plane" )
		self.assertEqual(self.test_simulation_instance.vehicle, self.test_vehicle_instance )

	def test_get_current_angle(self):
		self.assertEqual(self.test_vehicle_instance.get_current_angle() , 0 )
		self.assertNotEqual(self.test_vehicle_instance.get_current_angle() , "d" )
		
	def test_get_vehicle_name(self):
		self.assertEqual(self.test_vehicle_instance.get_vehicle_name() , "Plane" )
		self.assertNotEqual(self.test_vehicle_instance.get_vehicle_name() , "NotPlane" )
		
	def test_correct_angle(self):
		current_angle = self.test_vehicle_instance.get_current_angle()
		test_value = 10
		self.assertEqual(self.test_vehicle_instance.correct_angle(test_value) , current_angle+test_value )

	def test_change_simulation_parameters_valid(self):
		generator = my_generator([55,30 ])
		with mockRawInput(generator):
			self.test_simulation_instance.change_simulation_parameters()
			self.assertEqual(self.test_simulation_instance.mean , 55 )
			self.assertEqual(self.test_simulation_instance.standard_deviation , 30 )
		
	def test_change_time_step(self):
		self.test_simulation_instance.change_time_step(5)
		self.assertEqual(self.test_simulation_instance.time_step , 5 )
		self.assertNotEqual(self.test_simulation_instance.time_step , 1 )
		
	def test_repeat_simulation_process_NO(self):
		generator = my_generator(["No" ])
		with mockRawInput(generator):
			current_time_step = self.test_simulation_instance.time_step
			self.test_simulation_instance.repeat_simulation_process()
			self.assertEqual(self.test_simulation_instance.time_step , current_time_step )
	def test_repeat_simulation_process_YES(self):
		generator = my_generator(["Yes" , 20, 30,100 ])
		with mockRawInput(generator ) :
			self.test_simulation_instance.repeat_simulation_process()
			self.assertEqual(self.test_simulation_instance.mean , 20 )
			self.assertEqual(self.test_simulation_instance.standard_deviation , 30 )
			self.assertEqual(self.test_simulation_instance.time_step , 100 )

if __name__ == '__main__':
    unittest.main()