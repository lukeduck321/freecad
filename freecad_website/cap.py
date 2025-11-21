import FreeCAD
import Mesh
def cap(var):

    print("test",var)    

    
    doc = FreeCAD.open("cube.FCStd")
    
    # Method 2: Direct property access
    var_set = doc.getObject("VarSet")
    if var_set:
        # List all properties to find the correct one
        print("Properties in VarSet:")
        for prop in var_set.PropertiesList:
            print(f"  - {prop}")
        
        # Try to set the width property directly
        if hasattr(var_set, 'width'):
            var_set.width = float(var)
            doc.recompute()
            print("Width set via direct property access")
        else:
            print("'width' property not found in VarSet")
    
    body = doc.getObject("Body")
    if body:
        Mesh.export([body], "output_model.stl")
        print("STL exported!")
