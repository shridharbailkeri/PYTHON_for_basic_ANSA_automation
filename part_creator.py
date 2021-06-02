# PYTHON script
import os
import ansa
from ansa import *
deck = constants.NASTRAN

def main():
	l = ['rail1', 'rail2', 'lh_frame_1', 'lh_frame_2', 'square_plate', 'c_frame',  'rh_frame_1',  'rh_frame_2']
	for i, j in enumerate(l):
		part = base.NewPart(j)
		
		
	


if __name__ == '__main__':
	main()
