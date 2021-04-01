# PYTHON script
import os
import ansa
from ansa import base
from ansa import constants
def main():
	ents = ("FACE","SOLID")
	results = base.PickNodes(constants.NASTRAN, ents)
	vals = {'Name':'constraints_barrier'}
	set = base.CreateEntity(constants.NASTRAN, "SET", vals)
	base.AddToSet(set, list(results))

	
if __name__ == '__main__':
	main()
