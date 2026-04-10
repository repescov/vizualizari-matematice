from manim import *

# Configurare pentru format VERTICAL 4K (9:16)
config.pixel_height = 3840
config.pixel_width = 2160
config.frame_height = 16.0
config.frame_width = 9.0

class SquareEnding5(Scene):
    def construct(self):
        # Culori
        C_MAIN = WHITE
        C_DIGIT1 = TEAL
        C_DIGIT2 = YELLOW
        C_RESULT = GREEN

        # --- CONFIGURARE TIMPI ---
        t_intro = 0.6  # durata pentru fiecare element din intro

        # --- SCENA 1: INTRODUCEREA ---
        # 35^2 = ?
        num_3 = MathTex("3", font_size=170, color=C_DIGIT1)
        num_5 = MathTex("5", font_size=170, color=C_DIGIT2)
        power_2 = MathTex("^2", font_size=120)
        equals_q = MathTex("=", font_size=170)
        question_m = MathTex("?", font_size=200)
        
        # Aranjăm elementele
        num_5.next_to(num_3, RIGHT, buff=0.1)
        power_2.next_to(num_5, UR, buff=0.1).shift(UP * 0.2)
        equals_q.next_to(num_5, RIGHT, buff=0.8)
        question_m.next_to(equals_q, RIGHT, buff=0.6)
        
        # Grupăm doar pentru poziționarea pe ecran
        intro_group = VGroup(num_3, num_5, power_2, equals_q, question_m).move_to(UP * 4.5 + LEFT * 1.5)
        
        # Animație secvențială
        self.play(Write(num_3), run_time=t_intro)
        self.wait(0.25)
        self.play(Write(num_5), run_time=t_intro)
        self.wait(0.25)
        self.play(Write(power_2), run_time=t_intro)
        self.wait(0.5)
        self.play(Write(equals_q), run_time=t_intro)
        self.wait(0.5)
        self.play(Write(question_m), run_time=t_intro)

        self.play(Indicate(question_m))
        self.wait(2)

        # Pregătim base_group pentru restul animației (consistență cu codul vechi)
        base_group = VGroup(num_3, num_5)

        # --- SCENA 2: TRUCUL - PRIMA CIFRĂ ---
        # Luăm 3, înmulțim cu 4
        # self.play(FadeOut(equals_q)) # Îl păstrăm pentru final
        
        copy_3 = num_3.copy()
        self.play(copy_3.animate.move_to(LEFT * 3.2 + UP * 0.5).set_font_size(160))
        
        times_sign = MathTex(r"\times", font_size=120).next_to(copy_3, RIGHT, buff=0.5)
        next_num = MathTex("4", font_size=160, color=TEAL).next_to(times_sign, RIGHT, buff=0.5)
        
        self.play(Write(times_sign))
        
        # Săgeată sau indicație că 4 este "3+1"
        plus_one_text = Text("(următorul)", font_size=50, color=TEAL).next_to(next_num, UP, buff=0.3)
        self.play(FadeIn(plus_one_text, shift=DOWN))
        self.wait(1)
        
        self.play(TransformFromCopy(copy_3, next_num))

        equals_12 = MathTex("= 12", font_size=160, color=C_DIGIT1).next_to(next_num, RIGHT, buff=0.5)
        self.play(Write(equals_12))
        self.wait(1)

        # --- SCENA 3: TRUCUL - A DOUA CIFRĂ ---
        # Luăm 5, ridicăm la pătrat
        copy_5 = num_5.copy()
        self.play(copy_5.animate.move_to(LEFT * 2.1 + DOWN * 3).set_font_size(160))
        
        power_2_copy = MathTex("^2", font_size=100).next_to(copy_5, UR, buff=0.1)
        self.play(TransformFromCopy(power_2, power_2_copy))
        
        equals_25 = MathTex("= 25", font_size=160, color=C_DIGIT2).next_to(copy_5, RIGHT, buff=0.8)
        self.play(Write(equals_25))
        self.wait(1)

        # --- SCENA 4: REZULTATUL FINAL ---
        self.play(
            FadeOut(plus_one_text), FadeOut(times_sign), FadeOut(copy_3), 
            FadeOut(next_num), FadeOut(copy_5), FadeOut(power_2_copy)          
        )
        
        # Extragem doar cifrele
        val_12 = equals_12[0][1:]
        val_25 = equals_25[0][1:]

        # Poziția finală a rezultatului relativ la equals_q existent
        # Folosim un buff minim pentru a lipi cifrele: 1225
        final_result_pos = VGroup(
            MathTex("12", font_size=200), 
            MathTex("25", font_size=200)
        ).arrange(RIGHT, buff=0.05).next_to(equals_q, RIGHT, buff=0.5)

        self.play(
            val_12.animate.move_to(final_result_pos[0]).set_font_size(220),
            val_25.animate.move_to(final_result_pos[1]).set_font_size(220),
            FadeOut(equals_12[0][0]), # Ștergem "=" din "= 12"
            FadeOut(equals_25[0][0]), # Ștergem "=" din "= 25"
            FadeOut(question_m),      # Îl scoatem din scenă
            run_time=2
        )
        self.remove(question_m) # Ne asigurăm că nu mai există în grup/scenă
        
        final_result_group = VGroup(val_12, val_25)
        self.play(Indicate(final_result_group, scale_factor=1.1))
        self.wait(3)

     # --- SCENA 5: OUTRO ---
        # Fădem elementele individuale rămase pentru a fi siguri
        self.play(FadeOut(base_group), FadeOut(power_2), FadeOut(equals_q), FadeOut(val_12), FadeOut(val_25))
        
        final_text = Text("Matematica\ne simplă!", font_size=90, color=BLUE).move_to(UP * 2)
        sub_text = Text("Follow pentru trucuri", font_size=50, color=GRAY).next_to(final_text, DOWN, buff=1)
        
        self.play(Write(final_text))
        self.play(FadeIn(sub_text, shift=UP))
        self.wait(1)
