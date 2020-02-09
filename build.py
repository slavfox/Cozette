from pathlib import Path
from cozette_builder.imagegen import save_sample, save_charlist, read_sample
from cozette_builder.ttfbuilder import TTFBuilder

REPO_ROOT = Path(__file__).resolve().parent
bdfpath = REPO_ROOT / "Cozette8" / "Cozette-10.bdf"

def save_images():

    save_charlist(bdfpath, REPO_ROOT / "img" / "characters.png")

    save_sample(
        "Clozette",
        read_sample(REPO_ROOT / "img" / "sample.txt"),
        REPO_ROOT / "img" / "sample.png",
    )


if __name__ == "__main__":
    # save_images()
    TTFBuilder.from_bdf_path(bdfpath).build("cloze.ttf")

