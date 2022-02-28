from manim import *
class Anagram(Scene):
    def construct(self):
        src = Text("Astrazeneca")
        tar = Text("Catanzarese")
        self.play(Write(src))
        self.wait(0.5)
        self.play(TransformMatchingShapes(src, tar, path_arc=PI/3*PI))
        self.wait(0.5)
        

        