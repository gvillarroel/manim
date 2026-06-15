"""Animated visual scene system for the AI concept spike series."""

from __future__ import annotations

import math

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    TAU,
    UP,
    ArcBetweenPoints,
    Arrow,
    Circle,
    Create,
    CurvedArrow,
    Dot,
    FadeIn,
    FadeOut,
    GrowArrow,
    Indicate,
    LaggedStart,
    Line,
    MoveAlongPath,
    ReplacementTransform,
    Scene,
    Square,
    Text,
    Transform,
    VGroup,
)

from components.mobjects.ai_concept_primitives import (
    caption_label,
    fitted_text,
    flow_nodes,
    meter_stack,
    mini_matrix,
    panel_frame,
    pill,
)
from components.styles.ai_concept_theme import (
    ACCENT_SEQUENCE,
    BACKGROUND,
    FONT,
    LINE,
    MUTED,
    PANEL,
    TEXT,
)


class AIConceptScene(Scene):
    """Base class for 39-second white-background visual explainers.

    The structure deliberately avoids slide-card replacement. Each beat keeps a
    single evolving diagram on screen and explains the idea through motion:
    misconception -> equation -> mechanism -> consequence -> recap map.
    """

    concept: dict = {}

    def construct(self):
        self.camera.background_color = BACKGROUND
        data = self.concept
        accent = data.get("accent", ACCENT_SEQUENCE[0])

        header = self._header(data, accent)
        self.play(FadeIn(header, shift=DOWN * 0.08), run_time=0.8)

        hook = self._hook_beat(data, accent)
        self.wait(1.7)

        equation = self._equation_beat(data, accent, hook)
        self.wait(3.0)

        mechanism = self._mechanism_beat(data, accent, equation)
        self.wait(2.0)

        consequence = self._consequence_beat(data, accent, mechanism)
        self.wait(2.0)

        recap = self._recap_beat(data, accent, consequence)
        self.wait(5.0)
        self.play(FadeOut(VGroup(header, recap), shift=UP * 0.08), run_time=0.9)

    def _header(self, data: dict, accent: str) -> VGroup:
        series = Text("AI CONCEPTS", font=FONT, font_size=17, color=accent)
        title = fitted_text(data["title"], font_size=36, color=TEXT, max_width=8.5, max_lines=1, line_chars=42)
        subtitle = fitted_text(data["subtitle"], font_size=18, color=MUTED, max_width=8.5, max_lines=1, line_chars=60)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.07)
        title_group.move_to(UP * 3.35)
        series.next_to(title_group, LEFT, buff=0.75)
        underline = Line(LEFT * 6.25, RIGHT * 6.25, color=accent, stroke_width=3).next_to(title_group, DOWN, buff=0.25)
        return VGroup(series, title_group, underline)

    def _hook_beat(self, data: dict, accent: str) -> VGroup:
        misconception = fitted_text(data["hook"], font_size=29, color=TEXT, max_width=8.4, max_lines=2, line_chars=58)
        misconception.move_to(UP * 0.92)
        slash = Line(misconception.get_left() + LEFT * 0.2, misconception.get_right() + RIGHT * 0.2, color=accent, stroke_width=6)
        keyword_cloud = self._keyword_cloud(data["keywords"], accent).move_to(DOWN * 1.05)

        self.play(FadeIn(misconception, shift=UP * 0.12), run_time=0.8)
        self.play(Create(slash), run_time=0.45)
        self.play(
            misconception.animate.set_opacity(0.34),
            FadeIn(keyword_cloud, shift=UP * 0.18),
            run_time=0.9,
        )
        self.play(
            LaggedStart(*[Indicate(mob, color=accent, scale_factor=1.06) for mob in keyword_cloud], lag_ratio=0.08),
            run_time=1.3,
        )
        return VGroup(misconception, slash, keyword_cloud)

    def _equation_beat(self, data: dict, accent: str, previous: VGroup) -> VGroup:
        definition = fitted_text(data["definition"], font_size=26, color=TEXT, max_width=9.2, max_lines=2, line_chars=68)
        definition.move_to(UP * 1.35)
        parts = data["recap"][:5] if len(data["recap"]) >= 5 else data["mechanism"][:5]
        equation = self._equation_strip(parts, accent).move_to(DOWN * 0.2)
        lenses = self._lens_annotations(data["lenses"], accent).next_to(equation, DOWN, buff=0.45)

        self.play(ReplacementTransform(previous, VGroup(definition, equation)), run_time=1.1)
        self.play(LaggedStart(*[FadeIn(label, shift=UP * 0.08) for label in lenses], lag_ratio=0.18), run_time=1.4)
        self.play(self._pulse_equation(equation, accent), run_time=2.4)
        return VGroup(definition, equation, lenses)

    def _mechanism_beat(self, data: dict, accent: str, previous: VGroup) -> VGroup:
        flow = self._mechanism_flow(data["mechanism"], accent).move_to(UP * 0.45)
        note = caption_label(data["mechanism_note"], width=9.5).next_to(flow, DOWN, buff=0.48)
        particle_group = self._particles_for_flow(flow, accent)

        self.play(ReplacementTransform(previous, VGroup(flow, note)), run_time=1.0)
        self.play(*particle_group["create"], run_time=0.6)
        for dot, path in particle_group["paths"]:
            self.play(MoveAlongPath(dot, path), run_time=0.62)
        self.play(
            LaggedStart(*[Indicate(node, color=accent, scale_factor=1.08) for node in flow[0]], lag_ratio=0.07),
            run_time=1.1,
        )
        side_notes = self._mechanism_side_notes(data, accent)
        self.play(FadeIn(side_notes, shift=LEFT * 0.1), run_time=1.0)
        return VGroup(flow, note, particle_group["dots"], side_notes)

    def _consequence_beat(self, data: dict, accent: str, previous: VGroup) -> VGroup:
        contrast = self._animated_contrast(data, accent).move_to(LEFT * 3.1 + UP * 0.35)
        meters = meter_stack(data["practical"], accent, width=5.4).move_to(RIGHT * 3.05 + UP * 0.25)
        footer = self._short_takeaway(data, accent).move_to(DOWN * 2.55)
        curve = self._rising_curve(accent).next_to(meters, DOWN, buff=0.38)

        self.play(ReplacementTransform(previous, VGroup(contrast, meters, footer, curve)), run_time=1.0)
        self.play(self._animate_meter_fill(meters), Create(curve), run_time=1.7)
        self.play(Indicate(contrast[-1], color=accent, scale_factor=1.08), run_time=0.9)
        self.wait(0.5)
        return VGroup(contrast, meters, footer, curve)

    def _recap_beat(self, data: dict, accent: str, previous: VGroup) -> VGroup:
        map_group = self._orbit_map(data, accent)
        caution = self._small_callout("Caution", data["caution"], accent).move_to(RIGHT * 3.4 + DOWN * 1.8)
        handoff = self._small_callout("Next", data["handoff"], accent).move_to(LEFT * 3.4 + DOWN * 1.8)
        self.play(ReplacementTransform(previous, map_group), run_time=1.0)
        self.play(
            LaggedStart(*[GrowArrow(edge) for edge in map_group[1]], lag_ratio=0.06),
            run_time=1.0,
        )
        self.play(FadeIn(caution, shift=UP * 0.08), FadeIn(handoff, shift=UP * 0.08), run_time=1.0)
        self.play(
            LaggedStart(*[Indicate(node, color=accent, scale_factor=1.05) for node in map_group[2]], lag_ratio=0.08),
            run_time=1.2,
        )
        return VGroup(map_group, caution, handoff)

    def _keyword_cloud(self, keywords: list[str], accent: str) -> VGroup:
        chips = VGroup(*[pill(word, accent, font_size=18, min_width=1.0) for word in keywords[:6]])
        chips.arrange_in_grid(rows=2, cols=3, buff=(0.22, 0.24))
        for index, chip in enumerate(chips):
            chip.shift((0.08 * ((index % 3) - 1)) * UP)
        return chips

    def _equation_strip(self, parts: list[str], accent: str) -> VGroup:
        items = VGroup()
        for index, part in enumerate(parts):
            token = pill(part, accent, font_size=19, min_width=1.25)
            items.add(token)
            if index < len(parts) - 1:
                plus = Text("+", font=FONT, font_size=26, color=accent)
                items.add(plus)
        items.arrange(RIGHT, buff=0.18)
        brace = Line(items.get_left(), items.get_right(), color=accent, stroke_width=2).next_to(items, DOWN, buff=0.18)
        result = fitted_text("one working mental model", font_size=19, color=MUTED, max_width=4.0, max_lines=1)
        result.next_to(brace, DOWN, buff=0.18)
        return VGroup(items, brace, result)

    def _lens_annotations(self, lenses: list[tuple[str, str]], accent: str) -> VGroup:
        labels = VGroup()
        positions = [LEFT * 3.8, ORIGIN, RIGHT * 3.8]
        for position, (title, body) in zip(positions, lenses):
            label = VGroup(
                fitted_text(title, font_size=17, color=accent, max_width=2.7, max_lines=1),
                fitted_text(body, font_size=16, color=MUTED, max_width=3.0, max_lines=2, line_chars=34),
            ).arrange(DOWN, buff=0.08)
            label.move_to(position)
            labels.add(label)
        return labels

    def _pulse_equation(self, equation: VGroup, accent: str):
        return LaggedStart(*[Indicate(item, color=accent, scale_factor=1.05) for item in equation[0][::2]], lag_ratio=0.08)

    def _mechanism_flow(self, steps: list[str], accent: str) -> VGroup:
        nodes = VGroup()
        arrows = VGroup()
        node_width = min(1.45, 9.4 / max(1, len(steps)))
        for index, step in enumerate(steps):
            shape = Circle(radius=0.44, stroke_color=accent, stroke_width=2.4, fill_color=PANEL, fill_opacity=1.0)
            label = fitted_text(step, font_size=17, color=TEXT, max_width=node_width, max_lines=2, line_chars=12)
            node = VGroup(shape, label.move_to(shape))
            nodes.add(node)
        nodes.arrange(RIGHT, buff=0.78)
        for left, right in zip(nodes[:-1], nodes[1:]):
            arrows.add(Arrow(left.get_right(), right.get_left(), buff=0.14, color=accent, stroke_width=3))
        return VGroup(nodes, arrows)

    def _particles_for_flow(self, flow: VGroup, accent: str) -> dict:
        nodes = flow[0]
        dots = VGroup()
        creates = []
        paths = []
        for index, (left, right) in enumerate(zip(nodes[:-1], nodes[1:])):
            dot = Dot(left.get_right(), radius=0.065, color=accent)
            path = Line(left.get_right(), right.get_left())
            dots.add(dot)
            creates.append(FadeIn(dot, scale=0.5))
            paths.append((dot, path))
        return {"dots": dots, "create": creates, "paths": paths}

    def _mechanism_side_notes(self, data: dict, accent: str) -> VGroup:
        notes = VGroup()
        x_positions = [-4.4, 0, 4.4]
        for x, (title, body) in zip(x_positions, [("Input", data["mechanism_cards"][0]), ("Rule", data["mechanism_cards"][1]), ("Result", data["mechanism_cards"][2])]):
            note = self._small_callout(title, body, accent).scale(0.82)
            note.move_to((x, -1.85, 0))
            notes.add(note)
        return notes

    def _animated_contrast(self, data: dict, accent: str) -> VGroup:
        left_title, left_body, right_title, right_body = data["contrast"]
        left = self._diagrammed_box(left_title, left_body, LINE)
        right = self._diagrammed_box(right_title, right_body, accent)
        left.move_to(LEFT * 1.75)
        right.move_to(RIGHT * 1.75)
        arrow = CurvedArrow(left.get_right() + RIGHT * 0.08, right.get_left() + LEFT * 0.08, angle=-TAU / 6, color=accent, stroke_width=3)
        label = fitted_text("replace the weak frame", font_size=17, color=MUTED, max_width=3.0, max_lines=1).next_to(arrow, DOWN, buff=0.08)
        return VGroup(left, arrow, right, label)

    def _diagrammed_box(self, title: str, body: str, color: str) -> VGroup:
        frame = panel_frame(2.3, 1.25, color=color, fill=BACKGROUND)
        title_mob = fitted_text(title, font_size=17, color=color, max_width=1.95, max_lines=1)
        body_mob = fitted_text(body, font_size=17, color=TEXT, max_width=2.0, max_lines=2, line_chars=18)
        graph = mini_matrix(color).scale(0.32).next_to(body_mob, DOWN, buff=0.09)
        contents = VGroup(title_mob, body_mob, graph).arrange(DOWN, buff=0.08)
        contents.move_to(frame)
        return VGroup(frame, contents)

    def _animate_meter_fill(self, meters: VGroup):
        return LaggedStart(*[Indicate(row, scale_factor=1.02) for row in meters], lag_ratio=0.12)

    def _rising_curve(self, accent: str) -> VGroup:
        axes = VGroup(
            Line(LEFT * 2.3, RIGHT * 2.3, color=LINE, stroke_width=1.5),
            Line(LEFT * 2.3, LEFT * 2.3 + UP * 0.95, color=LINE, stroke_width=1.5),
        )
        curve = ArcBetweenPoints(LEFT * 2.0 + DOWN * 0.25, RIGHT * 2.0 + UP * 0.45, angle=-TAU / 5, color=accent, stroke_width=4)
        label = fitted_text("pressure rises with wasted steps", font_size=16, color=MUTED, max_width=4.4, max_lines=1).next_to(axes, DOWN, buff=0.08)
        return VGroup(axes, curve, label).scale(0.78)

    def _short_takeaway(self, data: dict, accent: str) -> VGroup:
        line = panel_frame(9.3, 0.64, color=accent, fill=BACKGROUND)
        text = fitted_text(data.get("footer", data["takeaway"]), font_size=22, color=TEXT, max_width=8.65, max_lines=1, line_chars=58)
        text.move_to(line)
        return VGroup(line, text)

    def _orbit_map(self, data: dict, accent: str) -> VGroup:
        center = panel_frame(2.45, 1.12, color=accent, fill=PANEL)
        title_copy = (
            data["title"]
            .replace("What is an ", "")
            .replace("What is a ", "")
            .replace("?", "")
        )
        if title_copy == data["title"].replace("?", "") and len(title_copy) > 18:
            title_copy = title_copy.replace(" and ", "\n")
        title = fitted_text(title_copy, font_size=22, color=TEXT, max_width=2.05, max_lines=2, line_chars=18)
        center_group = VGroup(center, title.move_to(center))
        nodes = VGroup()
        edges = VGroup()
        labels = data["recap"][:5]
        radius = 2.55
        for index, label in enumerate(labels):
            angle = TAU * index / len(labels) + TAU / 10
            pos = radius * (RIGHT * math.cos(angle) + UP * math.sin(angle))
            node = VGroup(
                Circle(radius=0.43, stroke_color=accent, stroke_width=2, fill_color=BACKGROUND, fill_opacity=1),
                fitted_text(label, font_size=16, color=TEXT, max_width=0.95, max_lines=2, line_chars=10),
            )
            node[1].move_to(node[0])
            node.move_to(pos)
            nodes.add(node)
            edges.add(Arrow(center_group.get_center(), node.get_center(), buff=0.88, color=accent, stroke_width=2.2, max_tip_length_to_length_ratio=0.12))
        return VGroup(center_group, edges, nodes)

    def _small_callout(self, title: str, body: str, accent: str) -> VGroup:
        frame = panel_frame(3.0, 0.95, color=accent, fill=BACKGROUND)
        title_mob = fitted_text(title.upper(), font_size=14, color=accent, max_width=2.6, max_lines=1)
        body_mob = fitted_text(body, font_size=15, color=TEXT, max_width=2.65, max_lines=2, line_chars=32)
        content = VGroup(title_mob, body_mob).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
        content.move_to(frame)
        return VGroup(frame, content)
