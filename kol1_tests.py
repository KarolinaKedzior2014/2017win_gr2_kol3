import unittest
from kol1 import Vehicle
from kol1 import Simulation
import math

class MyTest(unittest.TestCase):

	def setUp(self):
		self.test_vehicle_instance = Vehicle("Plane", 90)
		self.test_simulation_instance = Simulation(self.test_vehicle_instance, 0.4, 1,0.5)

	def test_init(self):
		self.assertEqual(self.test_vehicle_instance.type_of_vehicle, "Plane" )
		self.assertEqual(self.test_simulation_instance.vehicle, self.test_vehicle_instance )

	def test_get_current_angle(self):
		self.assertEqual(self.test_vehicle_instance.get_current_angle() , 90 )

	def test_change_time_step(self):
		self.test_simulation_instance.change_time_step(5)
		self.assertEqual(self.test_simulation_instance.time_step , 5 )

