
#ifdef SHAKE_VERTEX_SHADER
//================================================================
// VERTEX

layout (location = SHAKE_VERTEX_POS2) in vec2 in_pos2;
layout (location = SHAKE_VERTEX_TEX2) in vec2 in_tex2;

uniform mat4 u_model;
uniform mat4 u_projection;

out vec2 var_tex2;

void main()
{
    var_tex2 = in_tex2;
    gl_Position = u_projection * u_model * vec4( in_pos2, 0.f, 1.f );
}

#endif
#ifdef SHAKE_FRAGMENT_SHADER
//================================================================
// FRAGMENT

in vec2             var_tex2;
uniform sampler2D   u_sampler2;
uniform vec3        u_color;
out vec4            out_fragment_color;

//----------------------------------------------------------------
void main()
{
    float sample_r = texture( u_sampler2, var_tex2 ).r;
    out_fragment_color = vec4( u_color, sample_r );
}

#endif
