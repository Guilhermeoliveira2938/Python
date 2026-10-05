# 📱 Gerador de QR Code

Gera um QR Code (arquivo `.png`) a partir de um link. Tem duas versões:

| Arquivo | Versão |
|---|---|
| `app.py` | Janela com interface gráfica (Tkinter): digite o link, o nome do arquivo e escolha a pasta |
| `qr.py` | Terminal: pergunta o link e o nome do arquivo em um loop (digite `sair` para encerrar) |

Se o link não começar com `http`, o programa adiciona `https://` sozinho.

## ▶️ Como usar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Rode a versão que preferir:
   ```bash
   python app.py   # interface gráfica
   python qr.py    # terminal
   ```

> O Tkinter já vem com o Python. No Linux pode ser preciso instalar o pacote `python3-tk`.

## 🧰 Tecnologias

- Python 3
- [qrcode](https://pypi.org/project/qrcode/) e [Pillow](https://pypi.org/project/pillow/)
- Tkinter
