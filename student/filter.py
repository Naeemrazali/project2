# ---------------------------------------------------------------------
# Project "Track 3D-Objects Over Time"
# Copyright (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja.
#
# Purpose of this file : Kalman filter class
#
# You should have received a copy of the Udacity license together with this program.
#
# https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013
# ----------------------------------------------------------------------
#

# imports
from math import gamma
import numpy as np

# add project directory to python path to enable relative imports
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import misc.params as params 

class Filter:
    '''Kalman filter class'''
    def __init__(self):
        pass

    def F(self):
        ############
        # TODO Step 1: implement and return system matrix F
        ############
        dt = params.dt

        state_transition_matrix = np.identity(6)
        state_transition_matrix[0,3] = dt
        state_transition_matrix[1,4] = dt
        state_transition_matrix[2,5] = dt

        return state_transition_matrix
        
        ############
        # END student code
        ############ 

    def Q(self):
        ############
        # TODO Step 1: implement and return process noise covariance Q
        ############

        q = params.q
        dt  = params.dt

        covariance_matrix = np.zeros((6,6))
        third_cube = (1/3)*dt**3*q
        half_square = 0.5*dt**2*q
        tq = dt*q

        covariance_matrix[0,0] = third_cube
        covariance_matrix[1,1] = third_cube
        covariance_matrix[2,2] = third_cube
        covariance_matrix[3,3] = tq
        covariance_matrix[4,4] = tq
        covariance_matrix[5,5] = tq
        covariance_matrix[0,3] = half_square
        covariance_matrix[1,4] = half_square
        covariance_matrix[2,5] = half_square

        return covariance_matrix
        
        ############
        # END student code
        ############ 

    def predict(self, track):
        ############
        # TODO Step 1: predict state x and estimation error covariance P to next timestep, save x and P in track
        ############
        F = self.F()

        track.x = F*track.x
        track.P = F*track.P*F.transpose() + self.Q()

        track.set_x(track.x)
        track.set_P(track.P)
        
        ############
        # END student code
        ############ 

    def update(self, track, meas):
        ############
        # TODO Step 1: update state x and covariance P with associated measurement, save x and P in track
        ############
        H = meas.sensor.get_H(track.x)
        S = self.S(track, meas, H)
        K = track.P*H.transpose()*np.linalg.inv(S)
        gamma = self.gamma(track, meas, H) 
        track.x = track.x + K*gamma # state update
        I = np.identity(params.dim_state)
        track.P = (I - K*H) * track.P # covariance update
        
        ############
        # END student code
        ############ 
        track.update_attributes(meas)
    
    def gamma(self, track, meas, H):
        ############
        # TODO Step 1: calculate and return residual gamma
        ############

        return (meas.z - H*track.x) 
        
        ############
        # END student code
        ############ 

    def S(self, track, meas, H):
        ############
        # TODO Step 1: calculate and return covariance of residual S
        ############

        return (H*track.P*H.transpose() + meas.R) 
        
        ############
        # END student code
        ############ 