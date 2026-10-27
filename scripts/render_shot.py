# render_shot.py: render frames <first>..<last> of the open scene at its saved final settings, as half-float ZIP EXR, to
# <out_dir>/<SHOT>_####.exr (SHOT = the .blend name). Exits non-zero on any error or missing frame; writes
# RENDER_OK_<first>_<last>.txt (renderer version and build) on success, for the next pipeline step to gate on.
# Usage: blender -b <SHOT>.blend --python-exit-code 1 --python render_shot.py -- <first> <last> <out_dir>
import bpy, os, sys
first, last, out_dir = sys.argv[sys.argv.index("--") + 1:][:3]
first, last = int(first), int(last)
shot = os.path.splitext(os.path.basename(bpy.data.filepath))[0]
os.makedirs(out_dir, exist_ok=True)
scn = bpy.context.scene
scn.frame_start, scn.frame_end = first, last
st = scn.render.image_settings
st.file_format, st.color_depth, st.exr_codec, st.color_mode = "OPEN_EXR", "16", "ZIP", "RGBA"
scn.render.filepath = os.path.join(out_dir, shot + "_####")
scn.render.use_file_extension = True
scn.render.use_overwrite = True
bpy.ops.render.render(animation=True)
missing = [f for f in range(first, last + 1) if not os.path.isfile(os.path.join(out_dir, f"{shot}_{f:04d}.exr"))]
if missing:
    raise RuntimeError(f"RENDER_FAILED {shot}: missing frames {missing}")
with open(os.path.join(out_dir, f"RENDER_OK_{first:04d}_{last:04d}.txt"), "w") as fh:
    fh.write(f"{shot} {first}-{last} blender {bpy.app.version_string} build {bpy.app.build_hash.decode()}\n")
print("RENDER_OK", shot, first, last)
