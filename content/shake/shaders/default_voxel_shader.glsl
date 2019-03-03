
#ifdef SHAKE_VERTEX_SHADER
//================================================================
// VERTEX

//----------------------------------------------------------------
// IN

// per vertex
layout (location = SHAKE_VERTEX_POS3) in vec3   in_vertex_pos3;
layout (location = SHAKE_VERTEX_NORM) in vec3   in_vertex_norm;

// per instance
layout (location = SHAKE_VOXEL_INDEX) in vec3   in_voxel_index;
layout (location = SHAKE_VOXEL_TEX2)  in vec2   in_voxel_tex2;

//----------------------------------------------------------------
// UNIFORM

uniform mat4 u_model;
uniform mat4 u_view;
uniform mat4 u_projection;

uniform sampler2D u_sampler2;

//----------------------------------------------------------------
// OUT

out vec4  var_vertex_color;

//----------------------------------------------------------------
// FUNCTIONS

//----------------------------------------------------------------
vec3 saturate( vec3 v )
{
	return clamp( v, 0.0, 1.0 );
}

//----------------------------------------------------------------
vec4 Color()
{
    ivec2 texture_size = textureSize( u_sampler2, 0 );
    vec2 tex_coords = vec2( in_voxel_tex2.x + 0.5f, in_voxel_tex2.y + 0.5f ) / texture_size;
    vec4 palette_color = texture( u_sampler2, tex_coords );
    return palette_color;
}

//----------------------------------------------------------------
float AmbientPower()
{
	return 0.3;
}

//----------------------------------------------------------------
float DiffusePower()
{
    vec3 norm = normalize( in_vertex_norm );
    vec3 light_direction = normalize( vec3( 1, -2, 3 ) );
    float diffuse_power = max( dot( norm, light_direction ), 0.0 );
    return diffuse_power;
}

//----------------------------------------------------------------
void main()
{
    vec4 color_4 = Color();
    vec3 color_3 = vec3( color_4 );
    color_3 = saturate( color_3 * AmbientPower() + color_3 * DiffusePower() );
    var_vertex_color = vec4( color_3, color_4.a );

    gl_Position = u_projection * u_view * u_model * vec4( in_vertex_pos3 + in_voxel_index, 1.0f);
}

#endif
#ifdef SHAKE_FRAGMENT_SHADER
//================================================================
// FRAGMENT

in vec4         var_vertex_color;
out vec4        out_fragment_color;

//----------------------------------------------------------------
void main()
{
    out_fragment_color = var_vertex_color;
}

#endif
