import bpy
import string

def getData(dataAsString):
    
    dataAsString =  ''.join(filter(lambda x: x.isalpha()==0, dataAsString))
    
    return dataAsString.split()

def mapKeyframes(data, object):
    print("animating object "+object.name)
    bpy.context.scene.objects.active = object
    
    for i in range(int(len(data)/4)) :
        frame = int(data[i*4])
        xPos = float(data[(i*4)+1])*scaleFactor+offsetX
        yPos = float(data[(i*4)+2])*-scaleFactor+offsetY
        zPos = float(data[(i*4)+3])*scaleFactor+offsetZ
        bpy.ops.anim.change_frame(frame=frame)
        object.location = (xPos, zPos, yPos)
        bpy.ops.anim.keyframe_insert()

scn = bpy.context.scene
context = bpy.context

#Custom Vars
scaleFactor = 0.001;
offsetX = -10;
offsetY = 1;
offsetZ = 0;

#bpy.ops.object.select_camera()
#cam = context.active_object 
#if cam==None:
    #print("No camera found. Creating a new one.")
#else:
#    print("Found existing camera. Overwriting it.")
    

#poi = bpy.ops.objects["AE_POI"]

#if poi==None:
#    print("No POI found. Creating a new one.")

#else:
#    print("Found existing POI. Overwriting it.")

input  = "Transform    Point of Interest    Frame    X pixels    Y pixels    Z pixels        1    2167.28    400.192    -8381.23        56    6234.96    518.058    -6601.34        106    5558.56    511.258    -6856.46        163    4547.61    602.465    -7024.43        220    5341.9    300.484    -3254.33        250    5434.92    290.204    -2664.68        317    3005.53    -571.183    -4129.96        379    309.207    -3.29347    3135.84        466    761.148    539.724    -223.635    Transform    Position    Frame    X pixels    Y pixels    Z pixels        1    833.771    288.114    -8965.58        56    4805.26    469.979    -7185.78        106    4329.05    463.18    -7640.81        163    4091.01    686.418    -8173.64        220    5156.67    320.954    -4428.41        250    5092.99    327.991    -4832.03        317    3439.14    -881.777    -5773.89        379    798.72    58.1206    791.163        466    729.148    475.724    -2794.3"

poiIndex = input.find("Point of Interest")
locIndex = input.find("Position")
oriIndex = input.find("Orientation")

poiData = input[poiIndex:locIndex]
locData = input[locIndex:oriIndex]
oriData = input[oriIndex:]


poiData = getData(poiData)
print(poiData)

locData = getData(locData)
print(locData)



bpy.ops.object.camera_add()
cam = context.active_object
cam.name = "AE_CAM"
bpy.ops.anim.keying_set_active_set(type="Location")
mapKeyframes(locData, cam)

bpy.ops.object.add()
poi = bpy.context.active_object
poi.name = "AE_POI"
mapKeyframes(poiData, poi)

bpy.data.objects["AE_CAM"].select = True;
bpy.data.objects["AE_POI"].select = True;
bpy.ops.object.track_set(type="TRACKTO")
        
scn.frame_start = int(poiData[0])
scn.frame_end = int(poiData[len(poiData)-4])
    


