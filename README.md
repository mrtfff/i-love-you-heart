# ❤️ I Love You Heart (Terminal Heart Animations)

An interactive, animated terminal art project that renders mathematical heart curves filled with *"I love you"* translated into **80+ languages**, complete with realistic pulse (Lub-Dub) animations, simultaneous typewriter reveals, and customizable multi-line block font names.

![Python](https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

---

## 📸 Overview

This project showcases the evolution of mathematical ASCII rendering in the command line—starting from a raw implicit algebraic surface and evolving into an advanced terminal animation featuring:

- **Mathematical Heart Equation:** Scaled dynamically to account for monospace terminal character aspect ratios (~2.15:1).
- **Smart Text Fitting:** Words are never sliced midway; empty spaces are dynamically balanced and filled with micro-tokens (`♥`, `<3`).
- **Simultaneous Typewriter Reveal:** Characters are revealed concurrently across all lines without jitter or visual distortion (using ghost whitespace padding).
- **Bi-color ASCII Font Engine:** High-definition 3-line block letters rendered in golden ANSI shades embedded directly into a crimson heart.
- **Anatomical Heartbeat (Lub-Dub):** Authentic cardiac cycle simulation with configurable BPM.

---

## 📐 Mathematical Formulation

The heart's contour is rendered using the classic 3D implicit algebraic heart curve projected onto the 2D terminal plane:

$$(x^2 + y^2 - 1)^3 - x^2 \cdot y^3 \le 0$$

To compensate for rectangular monospace character cells, coordinates are adjusted using horizontal step scaling:
$$\Delta x = \frac{\Delta y}{2.15}$$

---

## 📂 Scripts & Progression Roadmap

Each script represents a milestone in the project's development:

| Script | Feature Highlights |
|---|---|
| **`a.py`** | **Basic Mathematical Heart:** Evaluates coordinates on the curve and wraps 10 languages character-by-character. |
| **`b.py`** | **Fixed ASCII Template:** Centered, static heart shape with love messages and heart glyphs. |
| **`c.py`** | **Word-Safe Packing Engine:** Introduces the `satiri_doldur()` algorithm to prevent word breakage across segment boundaries. |
| **`d.py`** | **Global Vocabulary:** Expands the language corpus to over 80+ languages and dialects worldwide. |
| **`e.py`** | **Responsive Scaling:** Adds terminal aspect ratio compensation and customizable height parameters (`YUKSEKLIK`). |
| **`f.py`** | **Curtain / Wipe Animation:** Renders column-by-column across the terminal canvas in ANSI red. |
| **`g.py`** | **Simultaneous Typewriter:** Reveals all words concurrently letter-by-letter with ghost padding to eliminate shape flickering. |
| **`h.py`** | **Random Distribution:** Selects non-repeating words randomly for each line and balances remaining gaps. |
| **`i.py`** | **Cardiac Pulse (Lub-Dub):** Typewriter introduction followed by an authentic two-phase cardiac cycle at 60 BPM across 3 scales. |
| **`j.py`** | **Embedded Name Plate:** Centers a custom 2-line ASCII block font name within the heart's geometric center. |
| **`k.py`** | ⭐ **Flagship Edition:** 3-line high-definition block font name rendered in metallic gold, enclosed within a red typewriter-animated heart. |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or newer.
- A terminal supporting ANSI escape codes and UTF-8 encoding (e.g., Pop!_OS / GNOME Terminal, Alacritty, iTerm2, Windows Terminal).

### Running

To run the **flagship version** (Golden custom name with animated typewriter reveal):
```bash
python3 k.py