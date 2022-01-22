class test(Scene):
    def construct(self):
        text = Text("some text.")
        text1 = Text("another text.")
        text2 = Text("its some text.")
        rect = Rectangle()
        circle = Circle()
        text.to_edge(UP)
        text1.move_to(text.get_corner(LEFT+DOWN)-np.array([text1.get_corner(LEFT+UP)]))
        text2.move_to(text1.get_corner(LEFT+DOWN)-np.array([text2.get_corner(LEFT+UP)]))
        rect.next_to(text1,DOWN)
        circle.next_to(rect,RIGHT)
        self.add(text)
        self.play(Transform(text,text1))
        self.play(Transform(text, text2))
        self.play(Transform(text, VGroup(rect,circle)))
        self.wait()
        