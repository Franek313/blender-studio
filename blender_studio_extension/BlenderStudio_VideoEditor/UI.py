import bpy

class VIDEO_PT_my_panel(bpy.types.Panel):
    bl_label = "Video Editor"
    bl_space_type = 'SEQUENCE_EDITOR'   # albo 'VIEW_3D', jeśli w 3D
    bl_region_type = 'UI'
    bl_category = "Blender Studio"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Hello from the Blender Studio Video Editor!")

def register():
    bpy.utils.register_class(VIDEO_PT_my_panel)

def unregister():
    bpy.utils.unregister_class(VIDEO_PT_my_panel)