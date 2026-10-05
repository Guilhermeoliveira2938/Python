from pathlib import Path
import shutil

pasta = Path.home() / "teste"

tabela = {
    ".pdf": "PDFs",
    ".jpg": "Imagens",
    ".png": "Imagens",
    ".mp4": "Videos",
    ".mp3": "Audios",
    ".xlsx": "Planilhas",
}

for item in list(pasta.iterdir()):
    if not item.is_file() or item.name.startswith("."):
        continue

    extensao =  item.suffix.lower()
    nome_pasta = tabela.get(extensao, "Outros")

    destino = pasta / nome_pasta
    destino.mkdir(exist_ok=True)
    shutil.move(item, destino)
    print(f"{item.name} -> {nome_pasta}")
