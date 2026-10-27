# finish_look.py: scene-linear EXR frames -> display-referred 16-bit PNG with the project look, applied exactly as Blender's
# "Save as Render" does. Worker k of n takes every n-th frame; run n workers in parallel. Add --alpha to keep the alpha channel.
# Exits non-zero on any error; writes LOOK_OK_<k>_of_<n>.txt with its frame count, for the next step to gate on.
# Display device: env FINISH_DISPLAY, default "sRGB" (web and consumer screens); "Rec.1886" for a Rec.709 master graded on a
# BT.1886 reference monitor. Set the view and look below to the project look.
# Usage: blender -b --factory-startup --python-exit-code 1 --python finish_look.py -- <exr_dir> <png_dir> <k> <n> [--alpha]
import bpy, sys, os, glob
args = sys.argv[sys.argv.index("--") + 1:]
src, dst, k, n = args[:4]
k, n = int(k), int(n)
os.makedirs(dst, exist_ok=True)
scn = bpy.context.scene
scn.display_settings.display_device = os.environ.get("FINISH_DISPLAY", "sRGB")
vs = scn.view_settings
vs.view_transform, vs.look, vs.exposure, vs.gamma = "AgX", "AgX - Medium High Contrast", 0.0, 1.0   # your project look here
vs.use_curve_mapping = False
st = scn.render.image_settings
st.file_format, st.color_depth, st.compression = "PNG", "16", 15
st.color_mode = "RGBA" if "--alpha" in args else "RGB"
files = sorted(glob.glob(os.path.join(src, "*.exr")))
if not files:
    raise RuntimeError(f"LOOK_FAILED: no EXR frames in {src}")
done = 0
for i, p in enumerate(files):
    if i % n != k:
        continue
    img = bpy.data.images.load(p)
    img.save_render(os.path.join(dst, os.path.basename(p)[:-4] + ".png"), scene=scn)
    bpy.data.images.remove(img)
    done += 1
with open(os.path.join(dst, f"LOOK_OK_{k}_of_{n}.txt"), "w") as fh:
    fh.write(f"{done}\n")
print("LOOK_OK", k, n, done)
