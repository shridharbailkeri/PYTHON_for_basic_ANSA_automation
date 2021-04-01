# PYTHON script
import os
import ansa
from ansa import * 

deck = constants.NASTRAN

prop_1 = base.GetEntity(deck, "PSHELL", 542931,)  # 542931 is pid
print(prop_1)
print(type(prop_1)) # its an entity
print(prop_1._id)
print(prop_1._name) 
print(prop_1._comment)

