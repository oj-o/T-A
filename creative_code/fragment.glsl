#version 330 core

out vec4 f_color;

uniform vec2 u_resolution;
uniform float u_time;

void main() {
    vec2 uv = gl_FragCoord.xy / u_resolution.xy;
    float color = 0.0;

    // A mix of sine and cosine functions for a wavy, psychedelic look
    color += sin(uv.x * cos(u_time / 3.0) * 8.0 + u_time) + cos(uv.y * sin(u_time / 2.5) * 6.0 + u_time);
    color += sin(uv.y * sin(u_time / 1.5) * 4.0 + u_time) + cos(uv.x * cos(u_time / 3.5) * 12.0 + u_time);

    // A slow sine wave to modulate the overall brightness
    color *= sin(u_time / 10.0) * 0.5;

    // Output the final color, mapping the calculated value to RGB
    f_color = vec4(vec3(cos(color * 2.5), sin(color * 3.0), sin(color * 1.5)) * 0.5 + 0.5, 1.0);
}
