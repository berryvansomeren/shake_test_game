
#ifdef SHAKE_VERTEX_SHADER
//================================================================
// VERTEX

layout (location = SHAKE_VERTEX_POS3) in vec3 in_pos3;

uniform mat4 u_model;
uniform mat4 u_view;
uniform mat4 u_projection;

out vec3 var_tex3;

void main()
{
    var_tex3 = in_pos3;
    mat4 view_without_translation = mat4( mat3 ( u_view ) );
    gl_Position = u_projection * u_model * view_without_translation * vec4( in_pos3, 1.f );
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
    out_fragment_color = vec4( sample_color, 1.0f);
}

#endif
