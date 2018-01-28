# -*- coding: utf-8 -*-

"""
Script to drive a donkey car using a webserver hosted on the vehicle.

"""
import donkeycar as dk 

V = dk.vehicle.Vehicle()

cam = dk.parts.PiCamera()
V.add(cam, outputs=['cam/image_array'], threaded=True)

ctr = dk.parts.LocalWebController()
V.add(ctr, 
      inputs=['cam/image_array'],
      outputs=['user/angle', 'user/throttle', 'user/mode'],
      threaded=True)


steering_controller = dk.parts.PCA9685(1)
steering = dk.parts.PWMSteering(controller=steering_controller,
                                left_pulse=460, right_pulse=260)

throttle_controller = dk.parts.PCA9685(0)
throttle = dk.parts.PWMThrottle(controller=throttle_controller,
                                max_pulse=500, zero_pulse=370, min_pulse=220)

V.add(steering, inputs=['user/angle'])
V.add(throttle, inputs=['user/throttle'])

odometer = dk.parts.RotaryEncoder(m_per_tick=0.0329, pin=23)
V.add(odometer, outputs=['odometer/meters', 'odometer/meters_per_second'], threaded=True)

#add tub to save data
path='~/mydonkey/sessions/odometer_with_dist'
inputs=['user/angle', 'user/throttle', 'cam/image_array', 
        'odometer/meters', 'odometer/meters_per_second']
types=['float', 'float', 'image_array', 'float', 'float']
tub=dk.parts.TubWriter(path, inputs=inputs, types=types)
V.add(tub, inputs=inputs)

#run the vehicle for 20 seconds
V.start(rate_hz=10, max_loop_count=1000)

#you can now go to localhost:8887 to move a square around the image
