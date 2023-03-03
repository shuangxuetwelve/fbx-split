import bpy

bpy.ops.import_scene.fbx(filepath='1.fbx')

# 删除Blender默认插入的Cube。
cube = bpy.data.objects['Cube']
bpy.data.objects.remove(cube)

# 记录下所有type为MESH的object。
meshes = []
for obj in bpy.data.objects:
    print(f'{obj.name}: {obj.type}')
    if obj.type == 'MESH':
        meshes.append(obj)

bpy.ops.object.select_all(action='DESELECT')
count = 0
for mesh in meshes:
    count += 1

    mesh.select_set(True)
    bpy.ops.export_scene.fbx(filepath=f'component-{count}.fbx', use_selection=True)
