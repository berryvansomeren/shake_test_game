import sys
sys.path.append( "C:/Users/Berry/Documents/shake_build/" )
import pyshake
from test_system import TestSystem

#----------------------------------------------------------------
def main():
    application = pyshake.Application( 2560, 1440, "Shake Engine" )
    
    # create a scene
    world = pyshake.ecs.World( "Python World" )
    world.add_system__render_system( pyshake.ecs.RenderSystem() )
    #world.add_python_system( TestSystem() )

    # create the scene entity
    entity = world.create_entity()

    # add the render component
    render_pack = pyshake.graphics.make_render_pack_3d__voxel_grid( "voxel_models/default_voxel_model.vox" )
    render_component = pyshake.ecs.RenderComponent3D( render_pack )
    world.add_component_to_entity__render_component_3d( entity, render_component )

    transform_component = pyshake.ecs.TransformComponent3D( pyshake.core.Transform3D() )
    world.add_component_to_entity__transform_component_3d( entity, transform_component )

    # The scene needs a camera to render to
    camera = pyshake.graphics.Camera( 2560, 1440 )
    pyshake.graphics.set_current_camera( camera )
    
    while True:
        
        # update engine systems and get time delta
        application.update()
        dt = application.get_current_frame_time()

        # the camera controls are still implemented in c++ for now
        camera.update( dt )

        # Press L to switch polygonmode
        polygonmode = pyshake.graphics.PolygonMode.Fill
        if ( pyshake.hid.Keyboard.is_down( pyshake.hid.Keyboard.Key.L ) ):
            polygonmode = pyshake.graphics.PolygonMode.Line
        pyshake.graphics.set_current_polygon_mode( polygonmode )
        
        # Clear color and depth buffers
        pyshake.graphics.clear( [ 
            pyshake.graphics.FrameBufferBitFlag.Color,
            pyshake.graphics.FrameBufferBitFlag.Depth
        ] )
        
        # update all systems
        world.update_systems( dt )

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
main();