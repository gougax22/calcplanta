import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox

class Planta:
    def __init__(self, nome, potencial_agua_solo, potencial_osmotico_raiz, pressao_xilema, altura_arvore):
        self.nome = nome
        self.potencial_agua_solo = potencial_agua_solo  # Em MPa
        self.potencial_osmotico_raiz = potencial_osmotico_raiz  # Em MPa
        self.pressao_xilema = pressao_xilema  # Em MPa
        self.altura_arvore = altura_arvore  # Em metros

    def calcular_fluxo_agua(self):
        # Calcular gradiente e pressões
        gradiente_potencial = self.potencial_agua_solo - self.potencial_osmotico_raiz
        pressao_gravidade = self.altura_arvore * 0.01
        pressao_total = self.pressao_xilema - pressao_gravidade
        
        return gradiente_potencial, pressao_gravidade, pressao_total

    def plotar_balanco_hidrico(self):
        # Gerar dados para o gráfico
        gradiente_potencial, pressao_gravidade, pressao_total = self.calcular_fluxo_agua()
        alturas = np.linspace(0, self.altura_arvore, 100)
        pressao_xilema = self.pressao_xilema - (alturas * 0.01)

        # Plotar gráfico
        plt.figure(figsize=(10, 6))
        plt.plot(alturas, pressao_xilema, label='Pressão no Xilema', color='b', linewidth=2)
        plt.scatter(0, self.pressao_xilema, color='g', label='Pressão na raiz')
        plt.scatter(self.altura_arvore, pressao_total, color='r', label='Pressão no topo')
        plt.title(f'Balanço Hídrico e Pressão ao Longo da Altura da {self.nome}')
        plt.xlabel('Altura (metros)')
        plt.ylabel('Pressão (MPa)')
        plt.legend()
        plt.grid(True)
        plt.show()

def criar_planta_e_mostrar():
    try:
        # Pegando valores do formulário
        nome = entrada_nome.get()
        potencial_agua_solo = float(entrada_solo.get())
        potencial_osmotico_raiz = float(entrada_raiz.get())
        pressao_xilema = float(entrada_xilema.get())
        altura_arvore = float(entrada_altura.get())

        # Criar objeto da planta
        planta = Planta(nome, potencial_agua_solo, potencial_osmotico_raiz, pressao_xilema, altura_arvore)
        planta.plotar_balanco_hidrico()

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criando a janela principal
janela = tk.Tk()
janela.title("Simulação de Balanço Hídrico da Planta")

# Interface do usuário
tk.Label(janela, text="Nome da Planta:").grid(row=0)
tk.Label(janela, text="Potencial Hídrico do Solo (MPa):").grid(row=1)
tk.Label(janela, text="Potencial Osmótico da Raiz (MPa):").grid(row=2)
tk.Label(janela, text="Pressão no Xilema (MPa):").grid(row=3)
tk.Label(janela, text="Altura da Árvore (metros):").grid(row=4)

# Campos de entrada
entrada_nome = tk.Entry(janela)
entrada_solo = tk.Entry(janela)
entrada_raiz = tk.Entry(janela)
entrada_xilema = tk.Entry(janela)
entrada_altura = tk.Entry(janela)

# Posicionamento dos campos de entrada
entrada_nome.grid(row=0, column=1)
entrada_solo.grid(row=1, column=1)
entrada_raiz.grid(row=2, column=1)
entrada_xilema.grid(row=3, column=1)
entrada_altura.grid(row=4, column=1)

# Botão para gerar gráfico
tk.Button(janela, text='Mostrar Balanço Hídrico', command=criar_planta_e_mostrar).grid(row=5, column=1)

# Iniciar a interface gráfica
janela.mainloop()
