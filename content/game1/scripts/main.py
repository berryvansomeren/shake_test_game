import sys
sys.path.append( "C:/Users/Berry/Documents/development/shake3/build/" )
import pyshake

from pyshake.core import Vec3
from pyshake.hid import Keyboard


class Game:
    #----------------------------------------------------------------
    def __init__( self ):
        self.width = 2560
        self.height = 1440
        self.application = pyshake.Application( 
            lambda      : self.init(),
            lambda dt   : self.update( dt ),
            lambda      : self.draw(),
            lambda      : self.destroy(),
            self.width, 
            self.height,
            "GLSL SDF Ray Marching" 
        )

    #----------------------------------------------------------------
    def run( self ) -> None:
        self.application.run()

    #----------------------------------------------------------------
    def init( self ) -> None:
        # content_manager = self.application.get_content_manager()
        # content_manager.host_content_directory( "" )
        # main_shader = content_manager.get_or_load__program( "shaders/default_primitive_2d_shader.glsl" )
        # main_material = make_material( main_shader )
        # main_geometry = make_rectangle_2D( self.width, self.height )
        # self.render_pack = pyshake.graphics.RenderPack2D( main_geometry, main_material )
        # self.camera_transform = pyshake.Transform3D()
        pass

    #----------------------------------------------------------------
    def update( self, dt : float ) -> None:
        # v = dt * 0.001
        # translations = [
        #     ( Keyboard.Key.W, Vec3(  0,  0, -v ) ),
        #     ( Keyboard.Key.S, Vec3(  0,  0,  v ) ),
        #     ( Keyboard.Key.A, Vec3( -v,  0,  0 ) ),
        #     ( Keyboard.Key.D, Vec3(  v,  0,  0 ) ),
        #     ( Keyboard.Key.E, Vec3(  0,  v,  0 ) ),
        #     ( Keyboard.Key.Q, Vec3(  0, -v,  0 ) ),
        # ]
        #
        # for key, translation_vector in translations:
        #      if Keyboard.is_down( key ):
        #          self.camera_transform.translate( translation_vector )
        pass

    #----------------------------------------------------------------
    def draw( self ) -> None:
        # self.render_pack.material.set_uniform( "camera_transform", self.camera_transform )
        # pyshake.graphics.draw( self.render_pack, pyshake.Transform2D() )
        pass

    #----------------------------------------------------------------
    def destroy( self ) -> None:
        pass


#----------------------------------------------------------------
if __name__ == "__main__":
    game = Game()
    game.run()