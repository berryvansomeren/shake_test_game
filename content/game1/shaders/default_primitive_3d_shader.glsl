#ifdef SHAKE_VERTEX_SHADER
//================================================================
// VERTEX

layout (location = SHAKE_VERTEX_POS3) in vec3 in_pos3;

uniform mat4 u_SHAKE_MODEL;
uniform mat4 u_SHAKE_VIEW;
uniform mat4 u_SHAKE_PROJECTION;

void main()
{
    gl_Position = u_SHAKE_PROJECTION * u_SHAKE_VIEW * u_SHAKE_MODEL * vec4( in_pos3, 1.f );
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
