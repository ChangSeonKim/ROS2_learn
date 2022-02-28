#!/usr/bin/env python

# Copyright (c) 2011, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Willow Garage, Inc. nor the names of its
#      contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from flask import Flask, request
# from flask_restful import Resource, Api
# from sqlalchemy import create_engine
from json import dumps
# from flask.ext.jsonpify import jsonify
from flask_jsonpify import jsonify


import rospy

from geometry_msgs.msg import Twist

from std_msgs.msg import String


import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

def vels(target_linear_vel, target_angular_vel):
    return "currently:\tlinear vel %s\t angular vel %s " % (target_linear_vel,target_angular_vel)

def checkLinear(target_linear_vel, control_linear_vel):
    if target_linear_vel > control_linear_vel:
        # control_linear_vel = min( target_linear_vel, control_linear_vel + (0.01/4.0) )
        control_linear_vel = ( target_linear_vel + control_linear_vel + (0.01/4.0) ) /2
    else:
        control_linear_vel = target_linear_vel

    return target_linear_vel,  control_linear_vel

def checkAngular(target_angular_vel, control_angular_vel):
    if target_angular_vel > control_angular_vel:
        control_angular_vel = min( target_angular_vel, control_angular_vel + (0.1/4.0) )
    else:
        control_angular_vel = target_angular_vel

    return target_angular_vel, control_angular_vel

def publishAction(control_linear_vel, control_angular_vel, pub):
    twist = Twist()
    twist.linear.x = control_linear_vel; twist.linear.y = 0; twist.linear.z = 0
    twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = control_angular_vel
    app.logger.info(twist) 
    rospy.loginfo("%s", str(twist))
    pub.publish(twist)
    return twist 

def move(action, speed, pub):
    global status
    global target_linear_vel
    global target_angular_vel
    global control_linear_vel
    global control_angular_vel

    # print(action)
    # print(speed)
    times = 1
    # print(speed == None)
    # print(speed != None)

    if speed != None:
        if type(int(speed)) is int:
            times = int(speed)
            target_linear_vel   = 0
            # control_linear_vel  = 0
            target_angular_vel  = 0
            # control_angular_vel = 0

    if action == "front":
        target_linear_vel = target_linear_vel + 0.01 * times
        status = status + 1
    elif action == "back" :
        target_linear_vel = target_linear_vel - 0.01 * times
        status = status + 1
    elif action == "left" :
        # if target_angular_vel < 0:
        #     target_angular_vel = 0
        target_angular_vel = target_angular_vel + 0.1 * times
        status = status + 1
    elif action == "right":
        # if target_angular_vel > 0:
        #     target_angular_vel = 0
        target_angular_vel = target_angular_vel - 0.1 * times
        status = status + 1
    else :
        target_linear_vel   = 0
        control_linear_vel  = 0
        target_angular_vel  = 0
        control_angular_vel = 0

    #print vels(target_linear_vel,target_angular_vel)

    target_linear_vel, control_linear_vel = checkLinear(target_linear_vel, control_linear_vel)
    target_angular_vel, control_angular_vel = checkLinear(target_angular_vel, control_angular_vel)

    return publishAction(control_linear_vel, control_angular_vel, pub)


@app.route('/')
def hello_world():
    return jsonify({'status': 'working node'})

@app.route('/turtlebot3/msg')
def msg():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    data = request.args.get('data')
    pub.publish(data) 
    return jsonify({'status': '200'}) 

@app.route('/turtlebot3/all/<action>')
def allAction(action):
    
    speed = request.args.get('speed')
    topics = (rospy.get_published_topics())
    return jsonify({'action': topics})


@app.route('/turtlebot3/move/<action>')
def action(action):
    speed = request.args.get('speed')
    
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)
    move(action, speed, pub)
    
    return jsonify({'action': action})


if __name__ == '__main__':
    
    rospy.init_node('turtlebot3_flask')
    rospy.loginfo("test")
    rospy.loginfo(rospy.get_published_topics())
    
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)

    status = 0
    target_linear_vel = 0
    target_angular_vel = 0
    control_linear_vel = 0
    control_angular_vel = 0

    while not rospy.is_shutdown():

        try :
             app.run(host='0.0.0.0',port='5002', debug="on")

        except OSError as e:
             rospy.loginfo(e)
             print(e)