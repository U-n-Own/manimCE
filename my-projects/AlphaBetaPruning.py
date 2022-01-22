from manim import *
import networkx as nx


class Introduction(Scene):
    def construct(self):


        #Title
        text_intro = Title('This is an animation for better understanding' r''' $\alpha-\beta$  ''' '   Pruning', include_underline = True, scale_factor=0.8, tex_environment = "center")
        
        self.play(Write(text_intro), run_time = 3)

        self.wait()

        self.remove(FadeOutAndShift(text_intro))

        #Pause

        text_explaining_minmax = Tex('Let\'s recap how does work the algorithm MiniMax.', tex_environment = "flushleft").scale(0.6)
        text_here_pseudo = Tex('Here is the pseudocode:', tex_environment = "flushleft").scale(0.5)
        text_explaining_minmax.to_edge().move_to(2.7*LEFT+2*UP)
        text_here_pseudo.to_edge().move_to(4*LEFT+UP)
        self.play(Write(text_explaining_minmax), run_time = 2)
        self.play(Write(text_here_pseudo), run_time = 1)

        self.wait(1)

        #Pseudocode           
        text_pseudocode = MathTex(r''' 
MINIMAX(s) =  
\begin{cases}
    \text{UTILITY(s,MAX),} & \quad\text{if IS-TERMINAL(s)}\\
    \text{$max_a$} \in \text{ Actions(s) MINIMAX(RESULT(s, a)),} &  \quad\text{if TO-MOVE(s) = MAX}\\
    \text{$min_a$} \in \text{ Actions(s) MINIMAX(RESULT(s, a)),} & \quad\text{if TO-MOVE(s) = MIN}
\end{cases}''', tex_environment = 'displaymath').scale(0.4)
        self.play(Write(text_pseudocode))
        self.wait(2)


class Pseudocode(Scene):
       def construct(self):
#Pseudocode           
        text_pseudocode = MathTex(r''' 
MINIMAX(s) =  
\begin{cases}
    \text{UTILITY(s,MAX),} & \quad\text{if IS-TERMINAL(s)}\\
    \text{$max_a$} \in \text{ Actions(s) MINIMAX(RESULT(s, a)),} &  \quad\text{if TO-MOVE(s) = MAX}\\
    \text{$min_a$} \in \text{ Actions(s) MINIMAX(RESULT(s, a)),} & \quad\text{if TO-MOVE(s) = MIN}
\end{cases}''', tex_environment = 'displaymath').scale(0.4)
        self.play(Write(text_pseudocode))
        self.wait(2)





class BinaryCompleteTree(Scene):
    def construct(self):
        
        nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12, 13, 14]
        edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (3, 8), (4, 9), (4, 10), (5, 11), (5, 12), (6, 13), (6, 14)]
        
        root = nodes[0]

        g = Graph(nodes, edges, layout = "tree", layout_scale = 7, root_vertex = root, labels = True, label_fill_color = DARK_BLUE, vertex_config = )
        #self.play(ShowCreation(g))
        
        #This replace the labels with the filling color
        #g.set_color_by_gradient(RED, BLUE)

        self.play(ShowCreation(g))


        self.wait()
        # self.play(g[1].animate.move_to([1, 1, 0]),
        #           g[2].animate.move_to([-1, 1, 0]),
        #           g[3].animate.move_to([1, -1, 0]),
        #           g[4].animate.move_to([-1, -1, 0]))
        # self.wait()


