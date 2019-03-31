
#ifdef SHAKE_VERTEX_SHADER
//================================================================
// VERTEX

layout (location = SHAKE_VERTEX_POS3) in vec3 in_pos3;

uniform mat4 u_SHAKE_VIEW;
uniform mat4 u_SHAKE_PROJECTION;

out vec3 var_tex3;

void main()
{
	// The OpenGL cubemap orientation is defined using a Z-up coordinate system.
	// When inside the cube, it seems as if the handed-ness of the system is flipped, 
	// and thus front, and back are swapped. 
	// In addition, since textures are then seen from inside the cube instead of from outside, 
	// the x coordinate needs to be flipped. 
	// However, Shake uses a Z-up coordinate system,
	// and thus we also need a rotation around the X-axis. 
	// All transformations for interpreting the cubemap correctly, 
	// and then transforming it to our own system, combined, 
	// result in simply swapping the y and z coordinates.

	var_tex3 = in_pos3.xzy;

	vec4 position = u_SHAKE_PROJECTION * mat4( mat3( u_SHAKE_VIEW ) ) * vec4( in_pos3, 1.f );
    gl_Position = position;
}

#endif
#ifdef SHAKE_FRAGMENT_SHADER
//================================================================
// FRAGMENT

in vec3 var_tex3;

uniform samplerCube u_sampler_cube;

out vec4 out_fragment_color;

//----------------------------------------------------------------
void main()
{
    vec3 sample_color = vec3( texture( u_sampler_cube, var_tex3 ) );
    out_fragment_color = vec4( sample_color, 1.0f );
}

#endif
