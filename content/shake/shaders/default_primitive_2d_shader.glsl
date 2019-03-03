
#ifdef SHAKE_VERTEX_SHADER
//================================================================
// VERTEX

layout (location = SHAKE_VERTEX_POS2) in vec2 in_pos2;

uniform mat4 u_model;
uniform mat4 u_projection;

void main()
{
    gl_Position = u_projection * u_model * vec4( in_pos2, 0.f, 1.f );
}

#endif
#ifdef SHAKE_FRAGMENT_SHADER
//================================================================
// FRAGMENT

uniform vec3 u_color;

out vec4 out_fragment_color;

//----------------------------------------------------------------
void main()
{
    out_fragment_color = vec4( u_color, 1.f );
}

#endif
