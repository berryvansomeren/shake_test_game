import sys
sys.path.append( "C:/Users/Berry/Documents/shake_build/" )
import pyshake
from test_system import TestSystem
import time

from sea_grid import SeaGrid

#----------------------------------------------------------------
def handle_camera_controls( camera, dt ):

    translation_velocity = dt * 0.01
    if pyshake.hid.Keyboard.is_down( pyshake.hid.Keyboard.Key.W ):
        camera.get_transform().translate( pyshake.core.Vec3( 0, 0, -translation_velocity ) )

    if pyshake.hid.Keyboard.is_down( pyshake.hid.Keyboard.Key.S ):
        camera.get_transform().translate( pyshake.core.Vec3( 0, 0, translation_velocity ) )

    if pyshake.hid.Keyboard.is_down( pyshake.hid.Keyboard.Key.A ):
        camera.get_transform().translate( pyshake.core.Vec3( -translation_velocity, 0, 0 ) )

    if pyshake.hid.Keyboard.is_down( pyshake.hid.Keyboard.Key.D ):
        camera.get_transform().translate( pyshake.core.Vec3( translation_velocity, 0, 0 ) )

    if pyshake.hid.Keyboard.is_down( pyshake.hid.Keyboard.Key.E ):
        camera.get_transform().translate( pyshake.core.Vec3( 0, translation_velocity, 0 ) )

    if pyshake.hid.Keyboard.is_down( pyshake.hid.Keyboard.Key.Q ):
        camera.get_transform().translate( pyshake.core.Vec3( 0, -translation_velocity, 0 ) )
        
    """
    rotation_velocity = 0.01 * dt
    if pyshake.hid.Mouse.is_down( pyshake.hid.Mouse.Key.Left ):
        # to prevent introducing rotation by pitching and yawing, you do yaw relative to world
        camera.get_transform().yaw_world       ( -mouse.get_diff_x() * rotation_velocity );
        camera.get_transform().pitch_relative  ( -mouse.get_diff_y() * rotation_velocity );
    """ 

#----------------------------------------------------------------
def main():

    application = pyshake.Application( 2560, 1440, "Shake Engine" )
    content_manager = application.content_manager();

    # create a scene
    world = pyshake.ecs.World( "Python World" )
    world.add_system__RenderSystem( pyshake.ecs.RenderSystem() )
    #world.add_python_system( TestSystem() )

    # create the scene entity
    entity = world.create_entity()

    # add the render component
    voxel_geometry_path = pyshake.content.Path( "voxel_models/procedure/nature.vox" )
    voxel_geometry = content_manager.get_or_load__VoxelGrid( voxel_geometry_path )
    voxel_material_path = pyshake.content.Path( "materials/default_voxel_material.json" )
    voxel_material = content_manager.get_or_load__Material( voxel_material_path )
    voxel_render_pack = pyshake.graphics.RenderPack3D( voxel_geometry, voxel_material )
    render_component = pyshake.ecs.RenderComponent3D( voxel_render_pack )
    world.add_component_to_entity__RenderComponent3D( entity, render_component )

    transform_component = pyshake.ecs.TransformComponent3D( pyshake.core.Transform3D() )
    world.add_component_to_entity__TransformComponent3D( entity, transform_component )

    font_path = pyshake.content.Path( "fonts/open_sans/open_sans.json" )
    font = content_manager.get_or_load__Font( font_path )

    # The scene needs a camera to render to
    camera = pyshake.graphics.Camera( 2560, 1440 )
    pyshake.graphics.set_current_camera( camera )

    # create the sea grid
    sea_grid = SeaGrid( 0, 50, 0, 50, 100, 100 )
    sea_material_path = pyshake.content.Path( "materials/sea_material.json" )
    sea_material = content_manager.get_or_load__Material( sea_material_path )
    sea_render_pack = pyshake.graphics.RenderPack3D( sea_grid.mesh, sea_material )
    sea_render_component = pyshake.ecs.RenderComponent3D( sea_render_pack )
    world.add_component_to_entity__RenderComponent3D( entity, render_component )


    total_time = 0
        
    while True:
        
        ## update engine systems and get time delta
        application.update()
        dt = application.get_current_frame_time()
        fps = application.get_current_fps()

        total_time = total_time + dt
        sea_grid.update_mesh( total_time )
        sea_mesh = sea_grid.mesh

        handle_camera_controls( camera, dt )
       

        # Press L to switch polygonmode
        polygonmode = pyshake.graphics.PolygonMode.Fill
        if ( pyshake.hid.Keyboard.is_down( pyshake.hid.Keyboard.Key.L ) ):
            polygonmode = pyshake.graphics.PolygonMode.Line
        pyshake.graphics.set_current_polygon_mode( polygonmode )
        
        # Clear color and depth buffers
        pyshake.graphics.clear( [ 
            pyshake.graphics.FramebufferBitFlag.Color,
            pyshake.graphics.FramebufferBitFlag.Depth
        ] )
        
        # update all systems
        world.update_systems( dt )
        
        pyshake.graphics.draw_text( "CamPos: {}".format( camera.get_transform() ), pyshake.core.Vec2( 20, 100 ), font )

        pyshake.graphics.draw_text( "FPS: {}".format( fps ), pyshake.core.Vec2( 20, 20 ), font )

        # The render system will automatically be updated here, 
        # it will scan all entities in it,
        # and if they have the required components to consider them "drawable"
        # i.e. a rendercomponent and a transform
        # it will automatically draw them

        # The python-based TestSystem is also managed by C++,
        # and is thus also automatically updated here. 
        # You can check the log/console to see the result. 

        # replace the buffers on the screen
        application.window().swap_buffers()

#----------------------------------------------------------------
if __name__ == "__main__":
    main()