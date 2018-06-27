from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
import time
import datetime
from gpiozero import DistanceSensor, Button
import os

def doeidoei():
	global player
	if player is not None:
		player.quit()
	os._exit(0)

def shutdown():
	print("Byeeeee! - " + str(datetime.datetime.now()))
	os.system('shutdown -h now')

left_a = Button(14)
left_b = Button(15)
bottom_a = Button(12)
bottom_b = Button(19)
right_a = Button(21)
right_b = Button(26)

#set quit and shutdown features
right_a.hold_time = 5
right_a.when_held = lambda : doeidoei()

right_b.hold_time = 5
right_b.when_held = lambda : shutdown()


def get_ab():
	#get the a or b selection
	a = 0
	b = 0
	was_pressed = False
	start_time = None
	while True:
		if was_pressed:
			if time.time() - start_time > 5:
				print("Results: A - " + str(a) + ", B - " + str(b))
				if a > b:
					return True
				else:
					return False
		if left_a.is_pressed or bottom_a.is_pressed or right_a.is_pressed:
			if not was_pressed:
				was_pressed = True
				start_time = time.time()
			a += 1
			#print("Button A pressed " + str(a) + " time(s)! Timer: " + str(time.time() - start_time))
		elif left_b.is_pressed or bottom_b.is_pressed or right_b.is_pressed:
			if not was_pressed:
				was_pressed = True
				start_time = time.time()
			b += 1
			#print("Button B pressed!" + str(b) + " time(s)! Timer:  " + str(time.time() - start_time))

def wait_for_press():
	#Wait for a button to be pressed
	print("Waiting for press...")
	while True:
		if left_a.is_pressed or bottom_a.is_pressed or right_a.is_pressed or left_b.is_pressed or bottom_b.is_pressed or right_b.is_pressed:
			return True

def wait(secs, use_sensor = False):
	#wait until the video reaches a certain position
	global player
	if use_sensor:
		sensor = DistanceSensor(echo=17, trigger=4)
	while player.position() < secs:
		if use_sensor:
			dist = sensor.distance
			player.set_rate(dist)
			print(dist)
		sleep(1)


print(str(datetime.datetime.now()))

try:
	while True:
		#intro
		print(str(datetime.datetime.now()) + " - Intro")
		player = OMXPlayer(Path("/home/pi/Videos/intro.mp4"), args=['--no-osd','-b'])
		wait(47)
		player.pause()
		wait_for_press()
		player.quit()
		player = None
		
		#question 1
		print(str(datetime.datetime.now()) + " - Tree")
		player = OMXPlayer(Path("/home/pi/Videos/tree.mp4"), args=['--no-osd','-b'])
		wait(8)
		player.pause()
		if get_ab():
			player.set_position(40)
			player.play()
			wait(65, True)
			player.pause()
		else:
			player.set_position(10)
			player.play()
			wait(38, True)
			player.pause()
		wait_for_press()
		player.quit()
		player = None
		
		#question 2
		print(str(datetime.datetime.now()) + " - Gas mask")
		player = OMXPlayer(Path("/home/pi/Videos/gasmask.mp4"), args=['--no-osd','-b'])
		wait(9)
		player.pause()
		if get_ab():
			player.set_position(24)
			player.play()
			wait(98, True)
			player.pause()
		else:
			player.set_position(100)
			player.play()
			wait(105, True)
			player.pause()
		wait_for_press()
		player.quit()
		player = None
		
		#question 3
		print(str(datetime.datetime.now()) + " - Ams")
		player = OMXPlayer(Path("/home/pi/Videos/ams.mp4"), args=['--no-osd','-b'])
		wait(9)
		player.pause()
		if get_ab():
			player.set_position(16)
			player.play()
			wait(42, True)
			player.pause()
		else:
			player.set_position(65)
			player.play()
			wait(95, True)
			player.pause()
		wait_for_press()
		player.quit()
		player = None
		
		#outro
		print(str(datetime.datetime.now()) + " - Outro")
		player = OMXPlayer(Path("/home/pi/Videos/outro.mp4"), args=['--no-osd','-b'])
		wait(45)
		player.pause()
		wait_for_press()
		player.quit()
		player = None
		
		
except KeyboardInterrupt:
	print("\nOk bye! - " + str(datetime.datetime.now()))
	player.quit()

player.quit()
print("Finished at " + str(datetime.datetime.now()))
