#!/usr/bin/env python2

###Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
#With every simulation step the orentation should be corrected, applied and printed out.
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#If you have spare time you can implement: Command Line Interface, generators, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Good Luck

import numpy as np
import time as t

#MateuszDev


class Vehicle:
    def __init__(self, name):
        self.type_of_vehicle = name
        self.angle = 0


    def correct_angle(self, correction):
        self.angle += correction

    def get_current_angle(self):
        return self.angle

    def get_vehicle_name(self):
        return self.type_of_vehicle


class Simulation:
    def __init__(self, vehicle, mean, standard_deviation, time_step = 0.5):
        self.vehicle = vehicle
        self.standard_deviation = standard_deviation
        self.mean = mean
        self.time_step = time_step

    def start_simulation(self):
        print "To stop simulation press: Crtl + C"
        try:
            while (True):
                print "Current angle ", self.vehicle.get_current_angle()
                self.vehicle.angle += self.get_random_tilt()
                t.sleep(self.time_step)
                print "turbulation: " , self.vehicle.angle, "..."
                self.vehicle.correct_angle(-self.vehicle.angle + np.random.choice([1,-1])*np.random.uniform(0.5))

        except KeyboardInterrupt:
            print "The simulation has ended"
            self.repeat_simulation_process()

    def change_simulation_parameters(self):
        self.mean = float(raw_input("Set new mean: "))
        self.standard_deviation = float(raw_input("Set new standard deviation: "))

    def change_time_step(self, new_time_step):
        self.time_step = new_time_step

    def get_random_tilt(self):
        return np.random.normal(self.mean, self.standard_deviation)

    def repeat_simulation_process(self):
        answer = raw_input("Do you want start next simulation with other parameters? (Yes/No\n")
        if answer == "Yes":
            self.change_simulation_parameters()
            time_step = float(raw_input("New time_step: "))
            self.change_time_step(time_step)
            self.start_simulation()

if __name__ == "__main__":
    plane = Vehicle("Plane")
    event_one = Simulation(plane, 0, 2)
    event_one.start_simulation()

