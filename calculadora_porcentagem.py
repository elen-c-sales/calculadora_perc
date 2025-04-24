import tkinter as tk

class CalculadoraPorcentagem:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Porcentagem")
        self.root.geometry("960x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#f3f3f3')

        self.criar_interface()

    def criar_interface(self):
        titulo = tk.Label(self.root, text="Calculadora de Porcentagem", font=("Segoe UI", 24, "bold"), bg='#f3f3f3')
        titulo.pack(pady=20)

        container = tk.Frame(self.root, bg='#f3f3f3')
        container.pack(fill='both', expand=True, padx=20)

        coluna_esquerda = tk.Frame(container, bg='#f3f3f3')
        coluna_direita = tk.Frame(container, bg='#f3f3f3')

        coluna_esquerda.pack(side='left', fill='both', expand=True, padx=10)
        coluna_direita.pack(side='right', fill='both', expand=True, padx=10)

        self.criar_secao("Quanto é X% de Y?", self.calcular_percentual_de_valor, ["X (%)", "Y (valor)"], coluna_esquerda)
        self.criar_secao("X é que porcentagem de Y?", self.calcular_percentagem_relativa, ["X (valor)", "Y (valor base)"], coluna_direita)
        self.criar_secao("Aumento percentual de X para Y", self.calcular_aumento_percentual, ["De X", "Para Y"], coluna_esquerda)
        self.criar_secao("Diminuição percentual de X para Y", self.calcular_reducao_percentual, ["De X", "Para Y"], coluna_direita)

    def criar_secao(self, titulo, funcao, campos, parent):
        frame = tk.Frame(parent, bg='#f3f3f3', highlightbackground="#ccc", highlightthickness=1)
        frame.pack(fill='x', pady=10)

        tk.Label(frame, text=titulo, font=("Segoe UI", 14, "bold"), bg='#f3f3f3').pack(anchor='w', pady=(5, 0))

        entradas = []
        for campo in campos:
            container = tk.Frame(frame, bg='#f3f3f3')
            container.pack(fill='x', pady=5)
            tk.Label(container, text=campo, font=("Segoe UI", 11), bg='#f3f3f3').pack(side='left')
            entrada = tk.Entry(container, font=("Segoe UI", 12), width=20, justify='right')
            entrada.pack(side='right')
            entradas.append(entrada)

        resultado_var = tk.StringVar()
        resultado_label = tk.Label(frame, textvariable=resultado_var, font=("Segoe UI", 12), bg='#f3f3f3', fg='#1975c5')
        resultado_label.pack(pady=5)

        def ao_calcular():
            try:
                valores = [float(e.get().replace(',', '.')) for e in entradas]
                resultado = funcao(*valores)
                resultado_var.set(f"Resultado: {resultado:.2f}")
            except:
                resultado_var.set("Erro: verifique os valores.")

        tk.Button(frame, text="Calcular", command=ao_calcular, font=("Segoe UI", 10), bg='#fcfcfc', relief='flat', activebackground='#f6f6f6').pack(pady=5)

    # Funções de cálculo
    def calcular_percentual_de_valor(self, percentual, valor):
        return (percentual / 100) * valor

    def calcular_percentagem_relativa(self, valor1, valor2):
        return (valor1 / valor2) * 100

    def calcular_aumento_percentual(self, valor_inicial, valor_final):
        return ((valor_final - valor_inicial) / valor_inicial) * 100

    def calcular_reducao_percentual(self, valor_inicial, valor_final):
        return ((valor_inicial - valor_final) / valor_inicial) * 100

if __name__ == "__main__":
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    root = tk.Tk()
    app = CalculadoraPorcentagem(root)
    root.mainloop()
