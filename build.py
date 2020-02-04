from pathlib import Path
from cozette_builder.imagegen import save_sample, save_charlist, Sample

SAMPLE_TEXT = """
$BLUE$┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ $MAGENTA$♡$NC$        $FG$Cozette$NC$        $MAGENTA$♡$BLUE$ ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ $WHITE$A B C D E F G H I J K L M $BLUE$│
│ $WHITE$N O P Q R S T U V W X Y Z $BLUE$│
╞═══════════════════════════╡
│    1 2 3 4 5 6 7 8 9 0    │
╞═══════════════════════════╡
│ $WHITE$a b c d e f g h i j k l m $BLUE$│
│ $WHITE$n o p q r s t u v w x y z $BLUE$│
├┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┤
│ $RED$() [] {} <> ? / \ : " ' ;$BLUE$ │
│ $RED$! @ # $ % ^ & * _ = + - |$BLUE$ │
│          , . ` ~$BLUE$          │
╰───────────────────────────╯
 $YELLOW$  
  
   $BLUE$│  $FG$╔═══════════════╗
   $BLUE$└──$FG$║ $GREEN$✓ ✔ $YELLOW$✕ ✖ $MAGENTA$✗ ✘ $FG$ ║$BLUE$▒
      $FG$║ $BLUE$       $FG$║$BLUE$▒
      $FG$╚═══════════════╝$BLUE$▒
       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒


  $GREEN$Pchnąć w tę łódź jeża lub
      ósm skrzyń fig.

     Eĥoŝanĝo ĉiuĵaŭde.

    Příliš žluťoučký kůň
     úpěl ďábelské ódy.

          $FG$♠ ♣ $MAGENTA$♥ ♦
"""
REPO_ROOT = Path(__file__).resolve().parent


def save_images():
    bdfpath = REPO_ROOT / "Cozette8" / "Cozette-10.bdf"

    save_charlist(bdfpath, REPO_ROOT / "img" / "characters.png")

    save_sample(
        "Clozette",
        Sample(SAMPLE_TEXT, 30, 32),
        REPO_ROOT / "img" / "sample.png",
    )


if __name__ == "__main__":
    save_images()
