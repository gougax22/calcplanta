import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

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
        st.pyplot(plt)

# Interface web com Streamlit
st.title("Simulação de Balanço Hídrico da Planta")

nome = st.text_input("Nome da Planta:")
potencial_agua_solo = st.number_input("Potencial Hídrico do Solo (MPa):", value=0.0)
potencial_osmotico_raiz = st.number_input("Potencial Osmótico da Raiz (MPa):", value=0.0)
pressao_xilema = st.number_input("Pressão no Xilema (MPa):", value=0.0)
altura_arvore = st.number_input("Altura da Árvore (metros):", value=0.0)  # Fechado o parêntese corretamente aqui

if st.button("Mostrar Balanço Hídrico"):
    if nome and potencial_agua_solo and potencial_osmotico_raiz and pressao_xilema and altura_arvore:
        planta = Planta(nome, potencial_agua_solo, potencial_osmotico_raiz, pressao_xilema, altura_arvore)
        planta.plotar_balanco_hidrico()
    else:
        st.error("Por favor, insira todos os valores corretamente.")
