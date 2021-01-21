
from __future__ import print_function


import time
import numpy as np
import traceback

import robobo
import cv2
import sys
import signal
import prey
from states import Agent
from actions import*
from q_learning import *
def terminate_program(signal_number, frame):
        print("Ctrl-C received, terminating program")
        rob.stop_world()
        sys.exit(1)

def simulation(rob):
    ## Initialize agent
    rob.set_phone_tilt(np.pi/7, 100)
    agent = Agent(rob=rob)
    ql = QLearning()
    ## Train agent with specified parameters and save the controller
    # agent.train(filename = 'controller.npy', n_episodes = 39, max_steps = 60, shuffle=False)
    ## Load controller and run
    run(agent = agent,q= ql,n_episodes = 40, max_steps = 50,max_food = 7, filename = 'food_1.npy')

    rob.stop_world()


def main():
    signal.signal(signal.SIGINT, terminate_program)

    # rob = robobo.HardwareRobobo(camera=True).connect(address="192.168.1.7")
    global rob
    rob = robobo.SimulationRobobo().connect(address='127.0.0.1', port=19997)
    
    try:
        simulation(rob)
    except Exception as e:
        cv2.imshow('img',rob.get_image_front())
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(e)
        traceback.print_exc()
        rob.pause_simulation()

    

<<<<<<< HEAD
    # Following code moves the robot

   
    # print("robobo is at {}".format(rob.position()))
    # # rob.sleep(1)

    # # # Following code moves the phone stand
    # # rob.set_phone_pan(343, 100)
    # # rob.set_phone_tilt(109, 100)
    # # time.sleep(1)
    # # rob.set_phone_pan(11, 100)
    # # rob.set_phone_tilt(26, 100)

    # # Following code makes the robot talk and be emotional
    # # rob.set_emotion('happy')
    # # rob.talk('Hi, my name is Robobo')
    # # rob.sleep(1)
    # # rob.set_emotion('sad')

    # # Following code gets an image from the camera
    # # image = rob.get_image_front()
    # # cv2.imwrite("test_pictures.png",image)

    # # time.sleep(0.1)

    # # IR reading
    # for i in range(2):
    #     print(rob.read_irs())
    #     # print("ROB Irs: {}".format(np.log(np.array(rob.read_irs()))/10))
    #     time.sleep(0.1)

    # # pause the simulation and read the collected food
    # # rob.pause_simulation()
    
    # # Stopping the simualtion resets the environment
    # rob.stop_world()
=======
    # # Following code moves the robot
    # for i in range(10):
    #         print("robobo is at {}".format(rob.position()))
    #         rob.move(5, 5, 2000)
   
    # print("robobo is at {}".format(rob.position()))
    # rob.sleep(1)

    # # Following code moves the phone stand
    # rob.set_phone_pan(343, 100)
    # rob.set_phone_tilt(109, 100)
    # time.sleep(1)
    # rob.set_phone_pan(11, 100)
    # rob.set_phone_tilt(26, 100)

    # # Following code makes the robot talk and be emotional
    # rob.set_emotion('happy')
    # rob.talk('Hi, my name is Robobo')
    # rob.sleep(1)
    # rob.set_emotion('sad')

    # # Following code gets an image from the camera
    # image = rob.get_image_front()
    # cv2.imwrite("test_pictures.png",image)

    # time.sleep(0.1)

    # # IR reading
    # for i in range(1000000):
    #     print("ROB Irs: {}".format(np.log(np.array(rob.read_irs()))/10))
    #     time.sleep(0.1)

    # # pause the simulation and read the collected food
    # rob.pause_simulation()
    
    # # Stopping the simualtion resets the environment


"""
Here I added my code, as i said in the chat. It is a bit sketchy but moving up and moving down based on a goal works. Only turning 180 still doens't work quite well.
"""
    def action(direction):
        if direction == "forward":
            return rob.move(20, 20, 1000)
        elif direction == "backward":
            return rob.move(-20, -20, 1000)
        elif direction == "right":
            return rob.move(20, -20, 1000)
        elif direction == "left":
            return rob.move(-20, 20, 1000)

    def pos_change(oldPos, newPos):
        deltaX = round(oldPos[0] - newPos[0], 3)
        deltaY = round(oldPos[1] - newPos[1], 3)
        return (deltaX, deltaY)

    def movingDirection(movingDir):
        x = movingDir[0]
        y = movingDir[1]
        if x < 0 and y == 0:
            return "a"
        elif x > 0 and y == 0:
            return "b"
        elif x == 0 and y < 0:
            return "c"
        elif x == 0 and y > 0:
            return "d"

    def changeDirection(degrees):
        if degrees == 0:
            action("forward")
        elif degrees == 90:
            action("right")
            action("right")
            action("forward")
        elif degrees == -90:
            action("left")
            action("left")
            action("forward")
        elif degrees == 180:
            action("left")
            action("left")
            action("forward")

    def goal(goal, direction):
        if goal == direction:
            changeDirection(0)
        elif goal == "a" and direction == "b":
            changeDirection(180)
        elif goal == "a" and direction == "c":
            changeDirection(90)
        elif goal == "a" and direction == "d":
            changeDirection(-90)
        elif goal == "b" and direction == "a":
            changeDirection(180)
        elif goal == "b" and direction == "c":
            changeDirection(90)
        elif goal == "b" and direction == "d":
            changeDirection(-90)
        elif goal == "c" and direction == "a":
            changeDirection(90)
        elif goal == "c" and direction == "b":
            changeDirection(-90)
        elif goal == "c" and direction == "d":
            changeDirection(180)
        elif goal == "d" and direction == "a":
            changeDirection(-90)
        elif goal == "d" and direction == "b":
            changeDirection(90)
        elif goal == "d" and direction == "c":
            changeDirection(180)

    for i in range(20):
        print("robobo is at {}".format(rob.position()))
        oldPos = rob.position()
        action("forward")
        newPos = rob.position()
        rob.sleep(0.01)
        posChange = pos_change(oldPos, newPos)
        goal("d", movingDirection(posChange))





    rob.stop_world()
>>>>>>> 44b12bec2fef43e6a11f0ad81fd670e73e5029a6


if __name__ == "__main__":
    main()
