<!-- Aviern CG field guide v001 (2026-10-26), aviern.com. -->
<p align="center">
  <a href="https://aviern.com"><img src="assets/brand/banner.jpg" alt="Aviern CG Field Guide: film-quality product CG with AI agents" width="100%"></a>
</p>

<p align="center">
  <img alt="Tested on Blender 5.2.3" src="https://img.shields.io/badge/tested-Blender%205.2.3-73baf2?style=flat-square&labelColor=17232e">
  <img alt="Tested on ffmpeg 9.0" src="https://img.shields.io/badge/tested-ffmpeg%209.0-73baf2?style=flat-square&labelColor=17232e">
  <img alt="Agents: Claude Code and Codex" src="https://img.shields.io/badge/agents-Claude%20Code%20%C2%B7%20Codex-73baf2?style=flat-square&labelColor=17232e">
  <img alt="Output: 4K, ProRes 4444, EXR" src="https://img.shields.io/badge/output-4K%20%C2%B7%20ProRes%204444%20%C2%B7%20EXR-73baf2?style=flat-square&labelColor=17232e">
</p>

A field guide for making film-quality CG of a physical product with AI coding agents (Claude Code, Codex, or similar), a 3D
renderer and rented or local GPUs. It is written to be handed to an agent as-is: the agent checks your setup, asks one round of
questions, maps each step onto your tools, and scaffolds the project. It stops before any spending, upload of product data or
outside contact until you approve that action.

The process and its figures come from a real production: 16 photoreal and stylised 4K shots of Aviern's unmanned cargo aircraft
for a launch video, made in October 2026 with Claude Code, Codex, Blender and cloud GPUs.

## Rendered with this process

Final frames from that production: 3840x2160 at 24 fps, rendered in Blender Cycles on cloud GPUs and finished with the scripts in
this repository. No frame was retouched.

<table>
  <tr>
    <td width="50%"><img src="assets/renders/ground_takeoff.jpg" alt="The aircraft climbing away from a dry-grass airfield with its landing gear retracting"><br><b>Takeoff, gear retracting.</b> A fully 3D airfield joined to a 360° photo panorama.</td>
    <td width="50%"><img src="assets/renders/ground_landing.jpg" alt="The aircraft rolling out on the runway into a low sun"><br><b>Landing rollout into a low sun.</b> Photoscanned plants, scanned asphalt.</td>
  </tr>
  <tr>
    <td><img src="assets/renders/inflight_sunset_orbit.jpg" alt="The aircraft in flight over canyon country at sunset"><br><b>Sunset orbit.</b> Lit by an HDRI shot from a drone at altitude, with a sun fitted to the plate.</td>
    <td><img src="assets/renders/inflight_canyon_joinup.jpg" alt="The aircraft seen from above over a river bend in a canyon"><br><b>Join-up over a canyon river.</b> A full 3D world built from 1 m lidar and aerial photos.</td>
  </tr>
  <tr>
    <td><img src="assets/renders/inflight_autumn_chase.jpg" alt="The aircraft seen from above over an autumn forest"><br><b>Chase over an autumn forest.</b> Drone HDRI; propellers with a short-exposure camera look.</td>
    <td><img src="assets/renders/inflight_bank_away.jpg" alt="The aircraft banking away over canyon cliffs"><br><b>Bank-away exit.</b> The continuation of the sunset orbit.</td>
  </tr>
  <tr>
    <td><img src="assets/renders/cutaway_nose.jpg" alt="Studio cutaway of the aircraft nose showing cargo inside"><br><b>Progressive nose cutaway.</b> A per-pixel cut in every material; cargo vanishes whole as the slice passes.</td>
    <td><img src="assets/renders/cutaway_roof.jpg" alt="Studio cutaway of the aircraft roof from above showing parcels in the hold"><br><b>Roof cutaway.</b> Studio void with six softboxes; also delivered with alpha.</td>
  </tr>
  <tr>
    <td><img src="assets/renders/ground_robot_loading.jpg" alt="An industrial robot arm loading parcels into the aircraft at a loading dock"><br><b>Robot-arm loading.</b> Per-frame clearance and motion gates before every render.</td>
    <td><img src="assets/renders/ground_holdshort.jpg" alt="The aircraft turning onto the runway, seen from a low camera on the centreline"><br><b>Turning onto the runway.</b> Camera 1.3 m above the centreline; panorama turned so the runway points down a valley.</td>
  </tr>
  <tr>
    <td><img src="assets/renders/ground_parked_orbit.jpg" alt="The aircraft parked on the runway with propellers turning"><br><b>Parked orbit.</b> Propellers turning, exterior lights flashing.</td>
    <td><img src="assets/renders/ground_overhead.jpg" alt="The aircraft on final approach, about to pass over the camera"><br><b>Final approach overhead.</b> The shot ends on open sky.</td>
  </tr>
</table>

Measured at 4K on an RTX PRO 6000: in-flight shots 3-6 s per frame, studio cutaways 8-13 s, airfield shots 33-71 s, robot-arm
loading 95-112 s. Section 8 of the guide has the full table and what the project cost.

### One orbit, three looks

<table>
  <tr>
    <td width="33%"><img src="assets/renders/look_wireframe.jpg" alt="The aircraft as a white wireframe on black"><br><b>Wireframe</b></td>
    <td width="33%"><img src="assets/renders/look_clay.jpg" alt="The aircraft as a grey clay render on black"><br><b>Clay</b></td>
    <td width="33%"><img src="assets/renders/look_photoreal.jpg" alt="The aircraft photoreal over canyon country"><br><b>Photoreal</b></td>
  </tr>
</table>

The same orbit move delivered in three looks. Motion was agreed once in a wireframe previs before any final rendering (guide
section 4.3). The photoreal panel is a raw scene-linear EXR frame finished with `scripts/finish_look.py` from this repository; it
matches the same frame of the delivered review copy at 40.7 dB PSNR.

## By the numbers

| | Reference production |
|---|---|
| Shots | 16 (19 masters, three with alpha) |
| Final 4K frames | 4,071 |
| Wall clock | 46.7 hours from project setup to checksum-verified delivery |
| Compute | about $2,200-2,330 (GCP Spot and RunPod GPUs) |
| Independent AI reviews | 101 (Claude and Codex) |
| Human 3D artists | 0 |

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
| `assets/` | The images on this page. |

Both scripts, and the ffmpeg encode commands in section 4.9 of the guide, were tested on Blender 5.2.3 and ffmpeg 9.0. Prices,
quotas and model names in the guide are as of October 2026.

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
