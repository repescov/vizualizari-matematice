from manim import *

# Configurare pentru format VERTICAL 4K (9:16)
config.pixel_height = 3840
config.pixel_width = 2160
config.frame_height = 16.0
config.frame_width = 9.0

class AdunareFractii(Scene):
    def construct(self):
        # Culori de bază
        C_BLUE = BLUE
        C_ORANGE = ORANGE
        C_RESULT = GREEN
        s_size = 3.2
        
        # Liste de nuanțe pentru efectul mozaic
        blue_shades = [BLUE_E, BLUE_D, BLUE_C, BLUE_B, BLUE_A]
        orange_shades = [ORANGE, "#E88E32", "#F39C12", "#D35400", "#E67E22"]

        # --- INTRO ---
        intro_text = Text("Cum adunăm fracțiile?", font_size=50, color=BLUE).to_edge(UP, buff=1)
        self.play(Write(intro_text))
        self.wait(4)
        self.play(FadeOut(intro_text))
        self.wait(1)

        # --- SCENA 1: 1/5 + 3/5 (ACELAȘI NUMITOR) ---
        title1 = Text("1) Același numitor", font_size=45).to_edge(UP, buff=1.2)
        eq1 = MathTex(r"\frac{1}{5} + \frac{3}{5} = ?", font_size=90).next_to(title1, DOWN, buff=0.2)
        self.play(Write(title1))
        self.wait(1)
        self.play(Write(eq1))
        self.wait(2)

        sq1a = Rectangle(height=s_size, width=s_size, stroke_width=4).shift(UP * 2 + LEFT * 2)
        sq1b = Rectangle(height=s_size, width=s_size, stroke_width=4).shift(UP * 2 + RIGHT * 2)
        sq1_res = Rectangle(height=s_size, width=s_size, stroke_width=4).shift(DOWN * 3 + LEFT * 1.5)

        def get_5_cols(rect):
            return VGroup(*[
                Line(rect.get_top() + LEFT * (s_size/2 - i * s_size/5), rect.get_bottom() + LEFT * (s_size/2 - i * s_size/5))
                for i in range(1, 5)
            ]).set_stroke(width=3)

        v1a, v1b, v1_res = get_5_cols(sq1a), get_5_cols(sq1b), get_5_cols(sq1_res)

        pieces1a = VGroup(*[
            Rectangle(height=s_size, width=s_size/5, fill_color=blue_shades[0], fill_opacity=0.8, stroke_width=1)
            .move_to(sq1a.get_center()).align_to(sq1a, LEFT)
        ])
        pieces1b = VGroup(*[
            Rectangle(height=s_size, width=s_size/5, fill_color=orange_shades[i], fill_opacity=0.8, stroke_width=1)
            .move_to(sq1b.get_center()).align_to(sq1b, LEFT).shift(RIGHT * i * s_size/5)
            for i in range(3)
        ])

        self.play(Create(sq1a))
        self.play(Create(v1a))
        self.play(FadeIn(pieces1a))
        self.wait(1)
        
        self.play(Create(sq1b), Create(v1b))
        self.play(FadeIn(pieces1b))
        self.wait(1)

        # Tranzitie curată Cazul 1
        all_pieces1 = VGroup(*pieces1a, *pieces1b)
        self.play(FadeOut(sq1a, sq1b, v1a, v1b))
        self.play(Create(sq1_res), Create(v1_res))
        targets1 = [sq1_res.get_left() + RIGHT * (s_size/10 + i * s_size/5) for i in range(4)]
        self.play(AnimationGroup(*[all_pieces1[i].animate.move_to(targets1[i]) for i in range(4)], lag_ratio=0.3), run_time=2.5)
        self.wait(1)
        res1_label = MathTex(r"= \frac{4}{5}", font_size=110, color=C_RESULT).next_to(sq1_res, RIGHT, buff=0.5)
        self.play(Write(res1_label))
        self.wait(3)
        self.play(FadeOut(sq1_res, v1_res, pieces1a, pieces1b, res1_label, title1, eq1))
        self.wait(1)

        # --- SCENA 2: 1/2 + 1/4 (NUMITOR MULTIPLU) ---
        title2 = Text("2) Numitori înrudiți", font_size=45).to_edge(UP, buff=1.2)
        eq2 = MathTex(r"{{ \frac{1}{2} }}", r" + ", r"\frac{1}{4}", font_size=90).next_to(title2, DOWN, buff=0.2)
        self.play(Write(title2))
        self.wait(0.5)
        self.play(Write(eq2))
        self.wait(2)

        # Explicație adițională
        expl2 = Text("Numitori diferiți, dar unul este\n multiplul celuilalt", font_size=35, color=GRAY).to_edge(DOWN, buff=1.5)
        self.play(FadeIn(expl2))
        self.wait(1)

        sq2a = Rectangle(height=s_size, width=s_size, stroke_width=4).shift(UP * 2 + LEFT * 2)
        sq2b = Rectangle(height=s_size, width=s_size, stroke_width=4).shift(UP * 2 + RIGHT * 2)
        sq2_res = Rectangle(height=s_size, width=s_size, stroke_width=4).shift(DOWN * 3 + LEFT * 1.5)

        v2a = Line(sq2a.get_top(), sq2a.get_bottom(), stroke_width=4)
        v2b = VGroup(*[Line(sq2b.get_top() + LEFT*(s_size/2 - i*s_size/4), sq2b.get_bottom() + LEFT*(s_size/2 - i*s_size/4)) for i in range(1,4)]).set_stroke(width=3)
        
        f2a = Rectangle(height=s_size, width=s_size/2, fill_color=C_BLUE, fill_opacity=0.7, stroke_width=0).move_to(sq2a.get_center()).align_to(sq2a, LEFT)
        f2b = Rectangle(height=s_size, width=s_size/4, fill_color=orange_shades[0], fill_opacity=0.8, stroke_width=1).move_to(sq2b.get_center()).align_to(sq2b, LEFT)

        self.play(Create(sq2a), Create(sq2b), Create(v2a), Create(v2b))
        self.play(FadeIn(f2a), FadeIn(f2b))
        self.wait(1)

        eq2_step1 = MathTex(r"{{ \frac{1 \cdot 2}{2 \cdot 2} }}", r" + ", r"\frac{1}{4}", font_size=90).move_to(eq2)
        eq2_step1[0].set_color(C_BLUE)
        v2a_extra = VGroup(Line(sq2a.get_top() + LEFT * s_size/4, sq2a.get_bottom() + LEFT * s_size/4), Line(sq2a.get_top() + RIGHT * s_size/4, sq2a.get_bottom() + RIGHT * s_size/4)).set_stroke(width=3)
        
        f2a_split = VGroup(*[
            Rectangle(height=s_size, width=s_size/4, fill_color=blue_shades[i], fill_opacity=0.8, stroke_width=1)
            .move_to(sq2a.get_center()).align_to(sq2a, LEFT).shift(RIGHT * i * s_size/4)
            for i in range(2)
        ])
        
        self.play(Transform(eq2[0], eq2_step1[0]), Create(v2a_extra), ReplacementTransform(f2a, f2a_split), run_time=1.5)
        self.wait(0.5)
        eq2_step2 = MathTex(r"{{ \frac{2}{4} }}", r" + ", r"\frac{1}{4}", font_size=90).move_to(eq2)
        eq2_step2[0].set_color(C_BLUE)
        self.play(Transform(eq2[0], eq2_step2[0]))
        self.wait(1)

        # Tranzitie curată Cazul 2
        all_pieces2 = VGroup(*f2a_split, f2b)
        v2_res = VGroup(*[Line(sq2_res.get_top() + LEFT*(s_size/2 - i*s_size/4), sq2_res.get_bottom() + LEFT*(s_size/2 - i*s_size/4)) for i in range(1,4)]).set_stroke(width=3)
        self.play(FadeOut(sq2a, sq2b, v2a, v2b, v2a_extra, expl2))
        self.play(Create(sq2_res), Create(v2_res))
        targets2 = [sq2_res.get_left() + RIGHT * (s_size/8 + i * s_size/4) for i in range(3)]
        self.play(AnimationGroup(*[all_pieces2[i].animate.move_to(targets2[i]) for i in range(3)], lag_ratio=0.4), run_time=2)
        
        res2_label = MathTex(r"= \frac{3}{4}", font_size=110, color=C_RESULT).next_to(sq2_res, RIGHT, buff=0.5)
        self.play(Write(res2_label))
        self.wait(2)
        self.play(FadeOut(sq2_res, v2_res, f2a_split, f2b, res2_label, title2, eq2))

        # --- SCENA 3: 1/2 + 2/5 (METODA UNIVERSALĂ) ---
        title3 = Text("3) Metoda universală", font_size=45).to_edge(UP, buff=1.2)
        eq3 = MathTex(r"{{ \frac{1}{2} }}", r" + ", r"{{ \frac{2}{5} }}", font_size=90).next_to(title3, DOWN, buff=0.2)
        self.play(Write(eq3))
        self.wait(1)
        self.play(Write(title3))
        self.wait(2)

        sq3a = Rectangle(height=s_size, width=s_size, stroke_width=4).shift(UP * 2 + LEFT * 2)
        sq3b = Rectangle(height=s_size, width=s_size, stroke_width=4).shift(UP * 2 + RIGHT * 2)
        v3a = Line(sq3a.get_top(), sq3a.get_bottom(), stroke_width=3)
        h3b = VGroup(*[Line(sq3b.get_left() + UP*(s_size/2 - i*s_size/5), sq3b.get_right() + UP*(s_size/2 - i*s_size/5)) for i in range(1,5)]).set_stroke(width=3)
        f3a = Rectangle(height=s_size, width=s_size/2, fill_color=C_BLUE, fill_opacity=0.7, stroke_width=0).move_to(sq3a.get_center()).align_to(sq3a, LEFT)
        f3b = Rectangle(height=2*s_size/5, width=s_size, fill_color=C_ORANGE, fill_opacity=0.7, stroke_width=0).move_to(sq3b.get_center()).align_to(sq3b, DOWN)

        self.play(Create(sq3a), Create(sq3b), Create(v3a), Create(h3b))
        self.play(FadeIn(f3a), FadeIn(f3b))
        self.wait(1)

        eq3_step1 = MathTex(r"{{ \frac{1 \cdot 5}{2 \cdot 5} }}", r" + ", r"{{ \frac{2 \cdot 2}{5 \cdot 2} }}", font_size=90).move_to(eq3)
        eq3_step1[0].set_color(C_BLUE)
        eq3_step1[2].set_color(C_ORANGE)
        h3a_extra = h3b.copy().move_to(sq3a.get_center())
        v3b_extra = v3a.copy().move_to(sq3b.get_center())
        
        p3a_split = VGroup(*[Rectangle(height=s_size/5, width=s_size/2, fill_color=blue_shades[i%5], fill_opacity=0.8, stroke_width=1).move_to(sq3a.get_top() + LEFT*(s_size/4) + DOWN*(s_size/10 + i*s_size/5)) for i in range(5)])
        p3b_split = VGroup(*[Rectangle(height=s_size/5, width=s_size/2, fill_color=orange_shades[i%5], fill_opacity=0.8, stroke_width=1).move_to(sq3b.get_bottom() + LEFT*(s_size/4 - (i//2)*s_size/2) + UP*(s_size/10 + (i%2)*s_size/5)) for i in range(4)])

        self.play(Transform(eq3[0], eq3_step1[0]), Create(h3a_extra), ReplacementTransform(f3a, p3a_split), run_time=1.5)
        self.wait(0.3)
        self.play(Transform(eq3[2], eq3_step1[2]), Create(v3b_extra), ReplacementTransform(f3b, p3b_split), run_time=1.5)
        self.wait(0.5)
        eq3_step2 = MathTex(r"{{ \frac{5}{10} }}", r" + ", r"{{ \frac{4}{10} }}", font_size=90).move_to(eq3)
        eq3_step2[0].set_color(C_BLUE)
        eq3_step2[2].set_color(C_ORANGE)
        self.play(Transform(eq3[0], eq3_step2[0]), Transform(eq3[2], eq3_step2[2]))
        self.wait(1.5)

        sq3_res = Rectangle(height=s_size, width=s_size, stroke_width=4).shift(DOWN * 3 + LEFT * 1.5)
        v3_res, h3_res = v3a.copy().move_to(sq3_res.get_center()), h3b.copy().move_to(sq3_res.get_center())
        targets3 = [sq3_res.get_top() + LEFT*(s_size/4) + DOWN*(s_size/10 + i*s_size/5) for i in range(5)] + [sq3_res.get_top() + RIGHT*(s_size/4) + DOWN*(s_size/10 + i*s_size/5) for i in range(4)]
        all_pieces3 = VGroup(*p3a_split, *p3b_split)
        self.play(FadeOut(sq3a, sq3b, v3a, h3b, h3a_extra, v3b_extra))
        self.play(Create(sq3_res), Create(v3_res), Create(h3_res))
        self.play(AnimationGroup(*[all_pieces3[i].animate.move_to(targets3[i]) for i in range(9)], lag_ratio=0.2), run_time=2.5)
        res3_label = MathTex(r"= \frac{9}{10}", font_size=110, color=C_RESULT).next_to(sq3_res, RIGHT, buff=0.5)
        self.play(Write(res3_label))
        self.wait(2)
        self.play(FadeOut(sq3_res, v3_res, h3_res, all_pieces3, res3_label, title3, eq3))

        # --- SCENA 4: 1/4 + 1/6 (CMMMC) ---
        title4 = Text("4) Numitorul comun\n      (CMMMC)", font_size=45).to_edge(UP, buff=1.2)
        eq4 = MathTex(r"{{ \frac{1}{4} }}", r" + ", r"{{ \frac{1}{6} }}", font_size=90).next_to(title4, DOWN, buff=0.2)
        lcm_hint = MathTex(r"CMMMC(4, 6) = 12", font_size=40, color=BLUE_B).next_to(eq4, DOWN, buff=0.5)
        
        self.play(Write(title4), Write(eq4))
        self.wait(2)  # Timp pentru explicația vocală despre CMMMC
        self.play(FadeIn(lcm_hint, shift=UP))
        self.wait(1)

        sq4a = Rectangle(height=s_size, width=s_size, stroke_width=4).shift(UP * 0.5 + LEFT * 2)
        sq4b = Rectangle(height=s_size, width=s_size, stroke_width=4).shift(UP * 0.5 + RIGHT * 2)
        v4a = VGroup(*[Line(sq4a.get_top() + LEFT*(s_size/2 - i*s_size/4), sq4a.get_bottom() + LEFT*(s_size/2 - i*s_size/4)) for i in range(1, 4)]).set_stroke(width=3)
        v4b = VGroup(*[Line(sq4b.get_top() + LEFT*(s_size/2 - i*s_size/6), sq4b.get_bottom() + LEFT*(s_size/2 - i*s_size/6)) for i in range(1, 6)]).set_stroke(width=3)
        f4a = Rectangle(height=s_size, width=s_size/4, fill_color=C_BLUE, fill_opacity=0.7, stroke_width=0).move_to(sq4a.get_center()).align_to(sq4a, LEFT)
        f4b = Rectangle(height=s_size, width=s_size/6, fill_color=C_ORANGE, fill_opacity=0.7, stroke_width=0).move_to(sq4b.get_center()).align_to(sq4b, LEFT)
        self.play(Create(sq4a), Create(sq4b), Create(v4a), Create(v4b))
        self.play(FadeIn(f4a), FadeIn(f4b))
        self.wait(1)

        eq4_step1 = MathTex(r"{{ \frac{1 \cdot 3}{4 \cdot 3} }}", r" + ", r"{{ \frac{1 \cdot 2}{6 \cdot 2} }}", font_size=90).move_to(eq4)
        eq4_step1[0].set_color(C_BLUE)
        eq4_step1[2].set_color(C_ORANGE)
        v4a_12 = VGroup(*[Line(sq4a.get_top() + LEFT*(s_size/2 - i*s_size/12), sq4a.get_bottom() + LEFT*(s_size/2 - i*s_size/12)) for i in range(1, 12)]).set_stroke(width=2, opacity=0.6)
        v4b_12 = VGroup(*[Line(sq4b.get_top() + LEFT*(s_size/2 - i*s_size/12), sq4b.get_bottom() + LEFT*(s_size/2 - i*s_size/12)) for i in range(1, 12)]).set_stroke(width=2, opacity=0.6)
        
        p4a_split = VGroup(*[Rectangle(height=s_size, width=s_size/12, fill_color=blue_shades[i % 5], fill_opacity=0.8, stroke_width=1).move_to(sq4a.get_left() + RIGHT*(s_size/24 + i*s_size/12)) for i in range(3)])
        p4b_split = VGroup(*[Rectangle(height=s_size, width=s_size/12, fill_color=orange_shades[i % 5], fill_opacity=0.8, stroke_width=1).move_to(sq4b.get_left() + RIGHT*(s_size/24 + i*s_size/12)) for i in range(2)])

        self.play(Transform(eq4[0], eq4_step1[0]), ReplacementTransform(v4a, v4a_12), ReplacementTransform(f4a, p4a_split), run_time=1.5)
        self.wait(0.3)
        self.play(Transform(eq4[2], eq4_step1[2]), ReplacementTransform(v4b, v4b_12), ReplacementTransform(f4b, p4b_split), run_time=1.5)
        self.wait(0.5)
        eq4_step2 = MathTex(r"{{ \frac{3}{12} }}", r" + ", r"{{ \frac{2}{12} }}", font_size=90).move_to(eq4)
        eq4_step2[0].set_color(C_BLUE)
        eq4_step2[2].set_color(C_ORANGE)
        self.play(Transform(eq4[0], eq4_step2[0]), Transform(eq4[2], eq4_step2[2]))
        self.wait(1.5)

        sq4_res = Rectangle(height=s_size, width=s_size, stroke_width=4).shift(DOWN * 3.5 + LEFT * 1.5)
        v4_res = v4a_12.copy().move_to(sq4_res.get_center())
        targets4 = [sq4_res.get_left() + RIGHT * (s_size/24 + i * s_size/12) for i in range(5)]
        all_pieces4 = VGroup(*p4a_split, *p4b_split)
        self.play(FadeOut(sq4a, sq4b, v4a_12, v4b_12, lcm_hint))
        self.play(Create(sq4_res), Create(v4_res))
        self.play(AnimationGroup(*[all_pieces4[i].animate.move_to(targets4[i]) for i in range(5)], lag_ratio=0.2), run_time=3)
        res4_label = MathTex(r"= \frac{5}{12}", font_size=110, color=C_RESULT).next_to(sq4_res, RIGHT, buff=0.5)
        self.play(Write(res4_label))
        self.wait(2)
        self.play(FadeOut(sq4_res, v4_res, all_pieces4, res4_label, title4, eq4))
        
        final_text = Text("Matematica\n  e simplă!", font_size=90, color=BLUE).move_to(UP * 2)
        sub_text = Text("Follow pentru perspective noi", font_size=35, color=GRAY).next_to(final_text, DOWN, buff=1)
        self.play(Write(final_text), FadeIn(sub_text, shift=UP))
        self.wait(2)
