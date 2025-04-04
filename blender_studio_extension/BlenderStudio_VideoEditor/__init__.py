bl_info = {
    "name": "BlenderStudio_VideoEditor",
    "blender": (4, 40, 0),
    "category": "Object",
}

from . import UI

def register():
    UI.register()
    print("Hello World, I'm Video Editor!")

def unregister():
    UI.unregister()
    print("Goodbye World! I'm Video Editor")