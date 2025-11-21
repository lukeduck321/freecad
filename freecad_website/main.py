import os
import FreeCAD
import Mesh

def main():
    width_value = os.getenv('WIDTH_VALUE', '42')  # Default to 42 if not set
    
    print(f"Setting width to: {width_value}")
    
    doc = FreeCAD.open("cube.FCStd")
    var_set = doc.getObject("VarSet")
    
    if var_set and hasattr(var_set, 'width'):
        var_set.width = float(width_value)
        doc.recompute()
        print(f"Width set to {width_value}")
    
    body = doc.getObject("Body")
    if body:
        Mesh.export([body], "output_model.stl")
        print("STL exported!")

main()
