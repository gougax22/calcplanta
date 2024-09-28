import matplotlib.pyplot as plt
import numpy as np

class Planta:
    def __init__(self, nome, potencial_agua_solo, potencial_osmotico_raiz, pressao_xilema, altura_arvore):
        self.nome = nome
        self.potencial_agua_solo = potencial_agua_solo  # Em MPa (MegaPascal)
        self.potencial_osmotico_raiz = potencial_osmotico_raiz  # Em MPa
        self.pressao_xilema = pressao_xilema  # Em MPa
        self.altura_arvore = altura_arvore  # Em metros

    def explicacao_fisiologia(self):
        print(f"\nFisiologia do transporte de água em {self.nome}:")
        print("\n1. Osmose e Absorção de Água pelas Raízes:")
        print("   A água é absorvida pelas raízes da planta devido à diferença de potencial hídrico entre o solo e as células das raízes.")
        print("   Esse processo ocorre por osmose, onde a água se move de uma área de maior potencial hídrico (solo) para uma de menor potencial (raiz).")
        
        print("\n2. Pressão Radicular:")
        print("   A pressão radicular ajuda a empurrar a água do solo para o xilema, o tecido responsável pelo transporte de água e nutrientes.")
        print("   Isso cria um fluxo de água que sobe pelas raízes em direção ao caule da planta.")

        print("\n3. Capilaridade e Coesão-Adesão:")
        print("   A água move-se no xilema graças à força da coesão (atração entre moléculas de água) e adesão (atração entre água e as paredes do xilema).")
        print("   Essas forças ajudam a puxar a água para cima, combatendo a gravidade, especialmente em árvores altas.")

        print("\n4. Transpiração nas Folhas:")
        print("   A evaporação da água nas folhas, um processo chamado transpiração, cria uma força de sucção que puxa a água para cima através do xilema.")
        print("   Isso forma um gradiente de pressão que ajuda a puxar a água desde o solo até as copas das árvores mais altas.")
    
    def calcular_fluxo_agua(self):
        # Fórmula simples para calcular o gradiente de potencial hídrico entre o solo e a raiz
        gradiente_potencial = self.potencial_agua_solo - self.potencial_osmotico_raiz
        
        # Simulando a pressão necessária para empurrar a água até o topo
        # Pressão adicional necessária devido à gravidade (0,01 MPa por metro de altura)
        pressao_gravidade = self.altura_arvore * 0.01
        
        # Pressão final no topo da árvore
        pressao_total = self.pressao_xilema - pressao_gravidade
        
        print(f"\nResultados do Balanço Hídrico em {self.nome}:")
        print(f"Potencial hídrico do solo: {self.potencial_agua_solo} MPa")
        print(f"Potencial osmótico da raiz: {self.potencial_osmotico_raiz} MPa")
        print(f"Gradiente de potencial entre solo e raiz: {gradiente_potencial} MPa")
        print(f"Pressão hidrostática no xilema: {self.pressao_xilema} MPa")
        print(f"Altura da árvore: {self.altura_arvore} metros")
        print(f"Pressão devido à gravidade: {pressao_gravidade} MPa")
        print(f"Pressão no topo da árvore: {pressao_total} MPa")
        
        if pressao_total > 0:
            print("\nA planta é capaz de transportar a água até o topo de suas folhas.")
        else:
            print("\nA pressão não é suficiente para transportar a água até o topo da planta.")
        
        # Retornar os valores para plotagem
        return gradiente_potencial, pressao_gravidade, pressao_total

    def plotar_balanco_hidrico(self):
        # Gerar dados
        gradiente_potencial, pressao_gravidade, pressao_total = self.calcular_fluxo_agua()

        # Altura da árvore (de 0 a altura máxima)
        alturas = np.linspace(0, self.altura_arvore, 100)
        
        # Pressão ao longo da altura da árvore
        pressao_xilema = self.pressao_xilema - (alturas * 0.01)  # 0,01 MPa por metro de altura
        
        # Plotar
        plt.figure(figsize=(10, 6))
        
        plt.plot(alturas, pressao_xilema, label='Pressão no Xilema', color='b', linewidth=2)
        
        # Marcar o ponto do solo e do topo da árvore
        plt.scatter(0, self.pressao_xilema, color='g', label='Pressão na raiz')
        plt.scatter(self.altura_arvore, pressao_total, color='r', label='Pressão no topo')
        
        # Personalizações do gráfico
        plt.title(f'Balanço Hídrico e Pressão ao Longo da Altura da {self.nome}')
        plt.xlabel('Altura (metros)')
        plt.ylabel('Pressão (MPa)')
        plt.legend()
        plt.grid(True)
        
        # Mostrar o gráfico
        plt.show()

# Exemplo de uso

# Criar um objeto de uma árvore simulada
arvore = Planta(nome="Carvalho", 
                potencial_agua_solo=-0.3,  # Potencial hídrico do solo (MPa)
                potencial_osmotico_raiz=-0.6,  # Potencial osmótico da raiz (MPa)
                pressao_xilema=0.5,  # Pressão no xilema (MPa)
                altura_arvore=20)  # Altura da árvore (metros)

# Mostrar explicação do transporte de água
arvore.explicacao_fisiologia()

# Plotar o balanço hídrico
arvore.plotar_balanco_hidrico()
