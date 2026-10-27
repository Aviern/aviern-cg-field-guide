<!-- Aviern CG field guide v001 (2026-10-26), aviern.com. -->
<p align="center">
  <a href="https://aviern.com"><img src="assets/brand/banner.jpg" alt="Aviern CG Field Guide" width="100%"></a>
</p>

A guide for making film-quality CG of your product with AI coding agents (Claude Code, Codex or similar), Blender and local or
cloud GPUs. Hand it to an agent: it checks your setup, asks you one round of questions, maps the process onto your tools and sets
up the project, and asks before spending money or sending your files anywhere.

<p align="center">
  <img src="assets/renders/ground_takeoff.jpg" width="32%" alt="Aircraft taking off from an airfield">
  <img src="assets/renders/inflight_sunset_orbit.jpg" width="32%" alt="Aircraft in flight at sunset">
  <img src="assets/renders/cutaway_nose.jpg" width="32%" alt="Studio cutaway of the aircraft with cargo">
</p>

## Quick start

1. Copy `docs/CG_FIELD_GUIDE.md` into your project at the same path.
2. Open Claude Code or Codex in that folder.
3. Send:

```text
Read docs/CG_FIELD_GUIDE.md in full, then follow its section A ("For AI agents") for my company. Check what you can on this
machine first, ask me the intake questions in one round, then propose an adaptation plan. Do not create any paid resource, buy
anything, upload our product data anywhere or contact anyone until I approve that specific action.
```

## Contents

- `docs/CG_FIELD_GUIDE.md`: the guide.
- `scripts/render_shot.py`: renders a frame range of a Blender scene to EXR.
- `scripts/finish_look.py`: applies the colour look once and writes 16-bit PNGs for encoding.

The scripts are tested on Blender 5.2.3 and ffmpeg 9.0.

---

<p align="center">
  <a href="https://aviern.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/brand/aviern-mark-white.png">
      <img src="assets/brand/aviern-mark-ink.png" alt="Aviern" width="110">
    </picture>
  </a>
  <br>
  <b>Aviern</b> · Nobody on board. · <a href="https://aviern.com">aviern.com</a>
</p>
