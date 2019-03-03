import pyshake

#----------------------------------------------------------------
# You can implement custom systems in Python
# They will still be invoked from C++
class TestSystem( pyshake.ecs.PythonSystem ):

    #----------------------------------------------------------------
    # Make sure the base class is initialized
    # required to do proper cloning
    def __init__( self ):
        pyshake.ecs.PythonSystem.__init__( self )

    #----------------------------------------------------------------
    # This function is required by the system manager,
    # in order to clone c++ object with a python implementation
    # without losing the reference to the python object
    def clone( self ):

        pyshake.core.log( "Cloning a TestSystem" )

        # create a mew pbject without initializing it
        cloned = TestSystem.__new__( TestSystem )
        # clone the c++ state
        pyshake.ecs.PythonSystem.__init__( cloned, self )
        # clone the Python state
        cloned.__dict__.update( self.__dict__ )
        return cloned

    #----------------------------------------------------------------
    # This will be called by the system manager at every game update
    def update( self, dt: float, world: pyshake.ecs.World, entity_id_set: pyshake.ecs.EntityIdVec ) -> None:

        pyshake.core.log( "Hello World, from TestSystem in Python!" )

