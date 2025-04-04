import bpy

class VIDEO_PT_my_panel(bpy.types.Panel):
    bl_label = "Video Editor"
    bl_space_type = 'SEQUENCE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Blender Studio"

    def draw(self, context):
        layout = self.layout
        layout.operator('object.testbutton')
        layout.label(text="Coco jumbo!")
        layout.prop(context.scene, 'my_bool_property')

class TestButtonOperator(bpy.types.Operator):
    bl_idname = "object.testbutton"
    bl_label = "Slice Strip"

    def execute(self, context):
        if context.scene.my_bool_property:
            bpy.ops.sequencer.split(type='SOFT')
        return {"FINISHED"}

classes_list = [
    VIDEO_PT_my_panel,
    TestButtonOperator
]

def register():
    for c in classes_list:
        bpy.utils.register_class(c)

    bpy.types.Scene.my_bool_property = bpy.props.BoolProperty(name="Pozwól ciachać!",
        description="Włącza opcję",
        default=False)

def unregister():
    for c in classes_list:
        bpy.utils.unregister_class(c)
