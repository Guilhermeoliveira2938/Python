# 🗂️ Organizador de Arquivos

Script que arruma uma pasta: pega cada arquivo e move para uma subpasta de acordo com a extensão.

| Extensão | Subpasta |
|---|---|
| `.pdf` | PDFs |
| `.jpg`, `.png` | Imagens |
| `.mp4` | Videos |
| `.mp3` | Audios |
| `.xlsx` | Planilhas |
| qualquer outra | Outros |

Arquivos ocultos (que começam com `.`) e pastas são ignorados. As subpastas são criadas automaticamente.

## ▶️ Como usar

```bash
python organizador.py
```

Por padrão ele organiza a pasta `teste`, dentro da sua pasta de usuário (`~/teste`). Para organizar outra pasta, troque esta linha no começo do arquivo:

```python
pasta = Path.home() / "teste"
```

> ⚠️ O script **move** os arquivos de verdade. Teste primeiro em uma pasta com cópias.

## 🧰 Tecnologias

- Python 3 (somente biblioteca padrão: `pathlib` e `shutil`)
