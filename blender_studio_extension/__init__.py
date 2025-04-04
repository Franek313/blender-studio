# blender_studio_extension/__init__.py

from . import BlenderStudio_VideoEditor

modules = [BlenderStudio_VideoEditor]

def register():
    for mod in modules:
        if hasattr(mod, "register"):
            mod.register()

def unregister():
    for mod in reversed(modules):
        if hasattr(mod, "unregister"):
            mod.unregister()