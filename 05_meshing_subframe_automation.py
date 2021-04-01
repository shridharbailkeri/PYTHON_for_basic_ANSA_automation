# PYTHON script
import os
import ansa
from ansa import *
deck = constants.NASTRAN

def main():
	face_list=base.CollectEntities(deck, None, 'FACE',False, True)
	print(face_list)
	print(len(face_list))
	base.IsolateRadius(2000)
	mesh.CreateMapMesh()
	print(base.CurrentMenu())
	base.SetCurrentMenu("MESH")
	print(mesh.UnmeshedMacros())
	mesh.CreateSpotMesh()
	base.All()
	mesh.CreateSpotMesh()
	base.All()
	print(mesh.AutoPaste(visible = True, project_on_geometry=True, project_2nd_order_nodes=False, move_to="geometry pos",   distance=0.1))
	status = mesh.ReadMeshParams("F:/ansa/hm_frame/params.ansa_mpar")
	mesh.Reconstruct()
	# ansa.base.GetEntity(deck, type, element_id, location)  Named Arguments
	# set = (base.GetEntity(constants.ABAQUS, "SET", 1),)
	# pshell = base.GetEntity(ansa.constants.NASTRAN, "PSHELL", 1)
	# Entity._id: Returns ANSA entity id
	# Entity._name: Returns ANSA entity name
	# Entity._comment: Returns ANSA entity comment
	# Entity._idDefunct(): Returns true if referenced ANSA entity has been destroyed
	# Entity._ansaType(deck): Returns ansa type of entity in specified deck
	# Entity._cardFields(deck): Returns list with active card fields
	
	
   
	

if __name__ == '__main__':
	main()
