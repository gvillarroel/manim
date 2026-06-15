"""Manim primitives for the temporary AI concept spike system."""

from __future__ import annotations

import textwrap

from manim import (
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    Arrow,
    Circle,
    Dot,
    Line,
    RoundedRectangle,
    Square,
    Text,
    VGroup,
)

from components.styles.ai_concept_theme import (
    BACKGROUND,
    FONT,
    LINE,
    MUTED,
    PANEL,
    SOFT_BLUE,
    TEXT,
)


def wrap_words(copy: str, max_chars: int) -> str:
    """Wrap plain English copy into short lines for Manim Text."""
    if not copy:
        return ""
    return "\n".join(textwrap.wrap(copy, width=max_chars, break_long_words=False))


def fitted_text(
    copy: str,
    *,
    font_size: int = 24,
    color: str = TEXT,
    max_width: float = 4.0,
    max_lines: int = 3,
    line_chars: int = 28,
    line_spacing: float = 0.84,
) -> Text:
    wrapped = wrap_words(copy, line_chars)
    lines = wrapped.splitlines()
    if len(lines) > max_lines:
        kept = lines[:max_lines]
        kept[-1] = kept[-1].rstrip(".") + "..."
        wrapped = "\n".join(kept)

    size = font_size
    mob = Text(wrapped, font=FONT, font_size=size, color=color, line_spacing=line_spacing)
    while mob.width > max_width and size > 14:
        size -= 1
        mob = Text(wrapped, font=FONT, font_size=size, color=color, line_spacing=line_spacing)
    return mob


def pill(label: str, color: str, *, font_size: int = 20, min_width: float = 1.0) -> VGroup:
    text = fitted_text(label, font_size=font_size, color=color, max_width=2.2, max_lines=1, line_chars=16)
    box = RoundedRectangle(
        width=max(min_width, text.width + 0.45),
        height=0.44,
        corner_radius=0.16,
        stroke_color=color,
        stroke_width=1.6,
        fill_color=BACKGROUND,
        fill_opacity=1.0,
    )
    text.move_to(box)
    return VGroup(box, text)


def panel_frame(width: float, height: float, color: str = LINE, fill: str = PANEL) -> RoundedRectangle:
    return RoundedRectangle(
        width=width,
        height=height,
        corner_radius=0.12,
        stroke_color=color,
        stroke_width=1.6,
        fill_color=fill,
        fill_opacity=1.0,
    )


def concept_card(
    title: str,
    body: str,
    color: str,
    *,
    width: float = 3.0,
    height: float = 1.18,
    title_size: int = 18,
    body_size: int = 20,
    body_max_lines: int = 2,
) -> VGroup:
    frame = panel_frame(width, height, color=color, fill=BACKGROUND)
    title_mob = fitted_text(title.upper(), font_size=title_size, color=color, max_width=width - 0.35, max_lines=1)
    body_mob = fitted_text(
        body,
        font_size=body_size,
        color=TEXT,
        max_width=width - 0.42,
        max_lines=body_max_lines,
        line_chars=24,
        line_spacing=0.9,
    )
    content = VGroup(title_mob, body_mob).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
    content.move_to(frame.get_center())
    return VGroup(frame, content)


def numbered_stack(items: list[str], color: str, *, width: float = 5.45) -> VGroup:
    rows = VGroup()
    for index, item in enumerate(items, start=1):
        marker = Circle(radius=0.16, stroke_color=color, stroke_width=1.8, fill_color=BACKGROUND, fill_opacity=1.0)
        number = Text(str(index), font=FONT, font_size=15, color=color).move_to(marker)
        label = fitted_text(item, font_size=21, color=TEXT, max_width=width - 0.65, max_lines=2, line_chars=34)
        row = VGroup(VGroup(marker, number), label).arrange(RIGHT, buff=0.18, aligned_edge=UP)
        rows.add(row)
    rows.arrange(DOWN, buff=0.18, aligned_edge=LEFT)
    return rows


def flow_nodes(items: list[str], color: str, *, width: float = 5.45) -> VGroup:
    nodes = VGroup()
    arrows = VGroup()
    node_width = min(1.55, (width - max(0, len(items) - 1) * 0.42) / max(1, len(items)))
    for item in items:
        label = fitted_text(item, font_size=18, color=TEXT, max_width=node_width - 0.16, max_lines=2, line_chars=13)
        box = RoundedRectangle(
            width=node_width,
            height=0.88,
            corner_radius=0.10,
            stroke_color=color,
            stroke_width=1.7,
            fill_color=SOFT_BLUE,
            fill_opacity=0.75,
        )
        label.move_to(box)
        nodes.add(VGroup(box, label))
    nodes.arrange(RIGHT, buff=0.42)
    for left, right in zip(nodes[:-1], nodes[1:]):
        arrows.add(Arrow(left.get_right(), right.get_left(), buff=0.08, color=color, stroke_width=2.4, max_tip_length_to_length_ratio=0.18))
    return VGroup(nodes, arrows)


def comparison_pair(left_title: str, left_body: str, right_title: str, right_body: str, color: str) -> VGroup:
    left = concept_card(left_title, left_body, color, width=2.55, height=1.55, body_size=18)
    right = concept_card(right_title, right_body, color, width=2.55, height=1.55, body_size=18)
    divider = Line(UP * 0.9, DOWN * 0.9, color=LINE, stroke_width=1.5)
    return VGroup(left, divider, right).arrange(RIGHT, buff=0.28)


def meter_stack(labels: list[str], color: str, *, width: float = 5.4) -> VGroup:
    bars = VGroup()
    for index, label in enumerate(labels):
        amount = 0.35 + 0.16 * (index % 4)
        base = RoundedRectangle(width=width, height=0.34, corner_radius=0.12, stroke_color=LINE, stroke_width=1.0, fill_color=BACKGROUND, fill_opacity=1)
        fill = RoundedRectangle(width=width * amount, height=0.34, corner_radius=0.12, stroke_color=color, stroke_width=0, fill_color=color, fill_opacity=0.18)
        fill.align_to(base, LEFT)
        text = fitted_text(label, font_size=18, color=TEXT, max_width=width - 0.25, max_lines=1, line_chars=32).move_to(base)
        bars.add(VGroup(base, fill, text))
    bars.arrange(DOWN, buff=0.16)
    return bars


def chip_grid(labels: list[str], color: str, *, columns: int = 3) -> VGroup:
    chips = VGroup(*[pill(label, color, font_size=18, min_width=1.25) for label in labels])
    chips.arrange_in_grid(rows=None, cols=columns, buff=(0.18, 0.18))
    return chips


def mini_matrix(color: str) -> VGroup:
    squares = VGroup()
    for row in range(4):
        for col in range(5):
            square = Square(side_length=0.27, stroke_color=color, stroke_width=1.0, fill_color=color, fill_opacity=0.12 + 0.04 * ((row + col) % 3))
            squares.add(square)
    squares.arrange_in_grid(rows=4, cols=5, buff=0.06)
    return squares


def progress_dots(active: int, total: int, color: str) -> VGroup:
    dots = VGroup()
    for index in range(total):
        fill = color if index == active else LINE
        dots.add(Dot(radius=0.045, color=fill))
    dots.arrange(RIGHT, buff=0.10)
    return dots


def caption_label(copy: str, color: str = MUTED, *, width: float = 5.4) -> Text:
    return fitted_text(copy, font_size=20, color=color, max_width=width, max_lines=2, line_chars=42)
