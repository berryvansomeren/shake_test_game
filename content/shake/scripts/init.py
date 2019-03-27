
from pyshake import core, ecs, hid, graphics


#----------------------------------------------------------------
def update_polygonmode() -> None:

    # Press L to switch polygonmode
    polygonmode = graphics.PolygonMode.Fill
    if ( hid.Keyboard.is_down( hid.Keyboard.Key.L ) ):
        polygonmode = graphics.PolygonMode.Line
    graphics.set_current_polygon_mode( polygonmode )


#----------------------------------------------------------------
# Called when the game is initialized
def init() -> None:

    #test.test( "LOL" );

    # create the world
    global world
    world = ecs.World( "Python World" )
    world.add_system__render_system( ecs.RenderSystem() )
    world.add_python_system( TestSystem() )

    # create the scene entity
    entity = world.create_entity()

    # add the render component
    render_pack = graphics.make_render_pack_3d__voxel_grid( "voxel_models/default_voxel_model.vox" )
    render_component = ecs.RenderComponent3D( render_pack )
    world.add_component_to_entity__render_component_3d( entity, render_component )

    # add the transform component
    transform = core.Transform3D()
    transform_component = ecs.TransformComponent3D( transform )
    world.add_component_to_entity__transform_component_3d( entity, transform_component )


    # create a skybox entity
    skybox_entity = world.create_entity();

    skybox_render_pack = graphics.make_render_pack_3d__voxel_grid( "voxel_models/default_voxel_model.vox" )


#----------------------------------------------------------------
# Called at every game update
def update( dt: float ) -> None:

    #graphics.clear( [ graphics.FrameBufferBitFlag.Color, graphics.FrameBufferBitFlag.Depth ] )
    update_polygonmode()

    global world
    world.update_systems( dt )


#----------------------------------------------------------------
# Called when the game is terminated
def terminate() -> None:

    core.log( "Terminated." )
    pass


#----------------------------------------------------------------
def run() -> None:

    init()
    while( True ):
        update( 0.16 )
    terminate()


#----------------------------------------------------------------
run()
