# PYTHON script
import os
import ansa
from ansa import base
from ansa import constants

def main():
	types = ("CQUAD4",)
	results = base.PickEntities(0, types)
	new_part = base.NewPart("New_part")
	base.SetEntityPart(results, new_part)


if __name__ == '__main__':
	main()
