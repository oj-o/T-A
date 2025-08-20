import pygame
import moderngl
import struct

# Window dimensions
WIDTH, HEIGHT = 800, 600

def main():
    # Initialize Pygame
    pygame.init()
    # Create a window with OpenGL support
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption("Your Code, Your Canvas")

    # Create a ModernGL context
    ctx = moderngl.create_context()

    # Load shaders
    with open("vertex.glsl", "r") as f:
        vertex_shader = f.read()
    with open("fragment.glsl", "r") as f:
        fragment_shader = f.read()

    # Create the shader program
    prog = ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)

    # Get uniform locations
    u_resolution = prog['u_resolution']
    u_time = prog['u_time']

    # Set the resolution uniform
    u_resolution.value = (WIDTH, HEIGHT)

    # A fullscreen quad
    vertices = struct.pack('8f',
        -1.0, -1.0,
        -1.0,  1.0,
         1.0, -1.0,
         1.0,  1.0,
    )

    # Create vertex buffer and vertex array object
    vbo = ctx.buffer(vertices)
    vao = ctx.vertex_array(prog, [(vbo, '2f', 'in_vert')])

    # Main loop
    running = True
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update time uniform
        time_val = (pygame.time.get_ticks() - start_time) / 1000.0
        u_time.value = time_val

        # Render the scene
        ctx.clear(0.0, 0.0, 0.0)
        vao.render(moderngl.TRIANGLE_STRIP)
        pygame.display.flip()

        # Tick the clock
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
