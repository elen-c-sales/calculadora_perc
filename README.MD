# 🧮 Calculadora de Porcentagem com Tkinter

Aplicativo gráfico desenvolvido em Python com foco em operações percentuais mais utilizadas no dia a dia. Inspirado em ferramentas online como a do site 4Devs, esta versão oferece uma interface intuitiva, design limpo e suporte para geração de executável (.exe).

---

## 🚀 Demonstração

![Demonstração animada](docs/demonstracao.gif)

---

## 📌 Funcionalidades

- Quanto é **X% de Y?**
- X é que **porcentagem de Y?**
- **Aumento percentual** de um valor para outro
- **Diminuição percentual** de um valor para outro
- Interface com layout responsivo em duas colunas
- Visual limpo com destaque nos resultados
- Suporte a `.exe` independente para Windows

---

## 🎨 Design

- Fundo: `#f3f3f3`
- Texto de resultado: `#1975c5`
- Componentes estilizados em conformidade com a UI do Windows
- Compatível com alta resolução (DPI aware)

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Tkinter
- `ctypes` para DPI awareness
- PyInstaller (para geração do `.exe` standalone)

---

## 📦 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/calculadora_perc.git
   cd calculadora_perc
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   venv\\Scripts\\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:
   ```bash
   python calculadora_porcentagem.py
   ```

---

## 🧪 Como Gerar um Executável (.exe)

Com o ambiente virtual ativado:

```bash
pyinstaller --noconsole --onefile --icon=icon.ico calculadora_porcentagem.py
```

O executável será gerado na pasta `/dist`.

---

## 📁 Estrutura do Projeto

```
calculadora_perc/
│
├── calculadora_porcentagem.py     # Código principal
├── calculadora_porcentagem.spec   # Arquivo gerado pelo PyInstaller
├── icon.ico                        # Ícone do aplicativo
├── README.md                       # Este arquivo
├── requirements.txt                # Dependências
├── /dist/
│   └── calculadora_porcentagem.exe
├── /docs/
│   ├── demonstracao.gif
│   ├── demonstracao.mp4
│   └── interface.png
└── /venv/                          # Ambiente virtual (opcional, não versionar)
```

---

## 👩‍💻 Desenvolvido por

**Elen C. Sales**  
🔗 [LinkedIn](https://www.linkedin.com/in/elen-c-sales)

---
