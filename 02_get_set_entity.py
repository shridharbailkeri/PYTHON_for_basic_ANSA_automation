# PYTHON script
import os
import ansa
from ansa import *

def main():
	pid_list = base.CollectEntities(0, None, "PSHELL", )
	print(pid_list)
	
	prop_1 = base.GetEntity(0, "PSHELL", 542923,)
	print(prop_1)
	elms_2 = base.CollectEntities(0, prop_1, "SHELL", True )
	print(elms_2)
	elm_3 = base.GetEntity(0, "SHELL", 7931,)
	print(elm_3)
	grids_of_element = base.CollectEntities(0 ,elm_3, "GRID",  )
	print(grids_of_element)
	single_grid =  base.GetEntity(0, "GRID", 10153,)
	print(single_grid)
	grid_info = base.GetEntityCardValues(0, single_grid,  ("X1",))
	print(grid_info)
	grid_info = base.GetEntityCardValues(0, single_grid,  ("NID", "X1", "X2", "X3",))
	print(grid_info)
	vals = {'T':5.2, 'Name':"PSHELL property"}
	base.SetEntityCardValues(0, prop_1, vals)
	
	


if __name__ == '__main__':
	main()
