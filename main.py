from pathlib import Path
from rembg import remove
from PIL import Image

print("\nSuppression d'arriere-plan\n")


def controle(output_dir: Path, base_name: str, ext: str) -> Path:
    output_path = output_dir / f"{base_name}{ext}"
    compteur = 1
    while output_path.exists():
        compteur += 1
        output_path = output_dir / f"{base_name}_{compteur}{ext}"
    return output_path

input_path = Path("assets/input/homme_noir.png")
output_dir = Path("assets/output")
output_dir.mkdir(parents=True, exist_ok=True)

base_name = "remove"
ext = ".png"
output_path = controle(output_dir, base_name, ext)

try:
    img = Image.open(input_path)
    remove(img).save(output_path)
    print("Arriere-plan supprimé ! Photo enregistrée sous:", output_path)
except FileNotFoundError:
    print("Erreur : inserer l'image d'operation dans le dossier selectionné")
except Exception as error:
    print("Erreur inattendue:", error)