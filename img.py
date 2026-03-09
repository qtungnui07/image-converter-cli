import os
import sys
from PIL import Image
from pillow_heif import register_heif_opener
from tqdm import tqdm

register_heif_opener()

def main():
    target_ext = sys.argv[1].lower() if len(sys.argv) > 1 else "jpg"
    if target_ext.startswith("."):
        target_ext = target_ext[1:]

    folder = os.getcwd()
    valid_extensions = (".heic", ".png", ".jpg", ".jpeg", ".webp", ".bmp")

    files = [f for f in os.listdir(folder) 
             if f.lower().endswith(valid_extensions) and not f.lower().endswith(f".{target_ext}")]

    if not files:
        print("not found")
        return

    print(f"converting {len(files)} to {target_ext}...")

    for f in tqdm(files, desc="processing"):
        in_path = os.path.join(folder, f)
        base_name = os.path.splitext(f)[0]
        out_path = os.path.join(folder, f"{base_name}.{target_ext}")

        try:
            with Image.open(in_path) as img:
                rgb_img = img.convert("RGB")
                save_format = "JPEG" if target_ext == "jpg" else target_ext.upper()
                rgb_img.save(out_path, save_format, quality=95)
        except Exception as e:
            print(f"eror {f}: {e}")

    print(f"\ndone, saved {folder}")

if __name__ == "__main__":
    main()