from manim import *


class AnimateSVGLogo(Scene):

    def construct(self):
        self.camera.background_color = WHITE
        svgLogo = SVGMobject(file_name = "svg-images/BonkedBrain.svg").scale(2)
        
        
        text = Title("Artificial Stupidity", GrowFromCenter = True, stroke_width=1.2, color = BLUE, size = 6, height= 1, width= 2, font = 'Computer Modern').scale(1.5)
        text.move_to(DOWN*2)
        self.play(Write(text),Write(svgLogo), run_time = 6)
        
        self.wait()
