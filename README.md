<!-- Aviern CG field guide v001 (2026-10-26), aviern.com. -->
# Film-quality product CG with AI agents

A field guide for making film-quality CG of a physical product with AI coding agents (Claude Code, Codex, or similar), a 3D
renderer and rented or local GPUs. It is written to be handed to an agent as-is: the agent checks your setup, asks one round of
questions, maps each step onto your tools, and scaffolds the project. It stops before any spending, upload of product data or
outside contact until you approve that action.

The process and its figures come from a real production: 16 photoreal and stylised 4K shots for a launch video, made in October
2026 with Claude Code, Codex, Blender and cloud GPUs.

## Quick start

1. Copy `docs/CG_FIELD_GUIDE.md` into your project folder at the same path (or start from a clone of this repository).
2. Start Claude Code, Codex or another coding agent with shell access in that folder.
3. Send it this:

```text
Read docs/CG_FIELD_GUIDE.md in full, then follow its section A ("For AI agents") for my company. Check what you can on this
machine first, ask me the intake questions in one round, then propose an adaptation plan. Do not create any paid resource, buy
anything, upload our product data anywhere or contact anyone until I approve that specific action.
```

## What is here

| Path | What it is |
|---|---|
| `docs/CG_FIELD_GUIDE.md` | The guide: agent instructions, the 13-stage pipeline, render and colour settings, agent roles, failure modes with guards, measured run times and costs, and paste-ready templates. |
| `scripts/render_shot.py` | Renders a frame range of a Blender scene to half-float EXR, exits non-zero on failure, writes a success marker (guide 4.7). |
| `scripts/finish_look.py` | Applies the project look once to EXR frames, producing 16-bit PNG for encoding; supports alpha and a choice of display (guide 4.9). |

Both scripts, and the ffmpeg encode commands in section 4.9 of the guide, were tested on Blender 5.2.3 and ffmpeg 9.0. Prices,
quotas and model names in the guide are as of October 2026.

---

*Aviern field guide · aviern.com*
