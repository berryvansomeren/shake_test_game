import math

import pyshake

#----------------------------------------------------------------
def _lerp( v0: float, v1: float, t: float ):
    return ( 1 - t ) * v0 + t * v1

#----------------------------------------------------------------
class SeaGrid:

    #----------------------------------------------------------------
    def __init__( 
        self,
        min_x:          float, 
        max_x:          float,
        min_y:          float, 
        max_y:          float,
        n_vertices_x:   int,
        n_vertices_y:   int
    ):
        self.vertices       = [ ]
        self.n_vertices_x   = n_vertices_x
        self.n_vertices_y   = n_vertices_y

        for vertex_index_y in range( self.n_vertices_y - 1 ):
            for vertex_index_x in range( self.n_vertices_x - 1 ):
                
                # define the corner points of the quad
                quad_min_x = _lerp( min_x, max_x, ( ( vertex_index_x     ) / n_vertices_x ) )
                quad_max_x = _lerp( min_x, max_x, ( ( vertex_index_x + 1 ) / n_vertices_x ) )
                quad_min_y = _lerp( min_y, max_y, ( ( vertex_index_y     ) / n_vertices_y ) )
                quad_max_y = _lerp( min_y, max_y, ( ( vertex_index_y + 1 ) / n_vertices_y ) )

                # define the vertices that make up the two triangles of the quad

                # first triangle:
                #   0
                #  /|
                # 0-0
                self.vertices.extend( [ quad_min_x, quad_min_y, 0 ] ) # bottom left
                self.vertices.extend( [ quad_max_x, quad_min_y, 0 ] ) # bottom right
                self.vertices.extend( [ quad_max_x, quad_max_y, 0 ] ) # top right

                # second triangle:
                # 0-0
                # |/
                # 0
                self.vertices.extend( [ quad_max_x, quad_max_y, 0 ] ) # top right
                self.vertices.extend( [ quad_min_x, quad_max_y, 0 ] ) # top left
                self.vertices.extend( [ quad_min_x, quad_min_y, 0 ] ) # bottom left

        self.update_mesh( 0 )

    #----------------------------------------------------------------
    def update_mesh( self, time: int ) -> None:

        for vertex_index_y in range( self.n_vertices_y - 1 ):
            for vertex_index_x in range( self.n_vertices_x - 1 ):
                z_component_index = vertex_index_y * self.n_vertices_x + self.n_vertices_x
                self.vertices[ z_component_index ] = math.sin( time )

        self.mesh = pyshake.graphics.Triangles3D( self.vertices )

