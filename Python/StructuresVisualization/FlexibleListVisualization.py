import tkinter as tk
import random

class ListaVisual:
    def __init__(self, root, tamanho):
        self.root = root
        self.root.title("Visualização da Lista")
        self.tamanho = tamanho
        self.elementos = []
        self.rectangles = []
        self.text_ids = []

        # Configurando a visualização
        self.canvas = tk.Canvas(root, width=200, height=150)
        self.canvas.pack(pady=20)

        # Posições dos retângulos da lista
        self.posicoes = [(i * 40 + 10, 10, i * 40 + 40, 40) for i in range(tamanho)]
        self.criar_visualizacao()

        self.passos = 0
        self.numeros = [random.randint(1, 100) for _ in range(10)]
        self.executar_passos()

    def criar_visualizacao(self):
        self.canvas.delete("all")
        self.rectangles = []
        self.text_ids = []
        for i in range(self.tamanho):
            x0, y0, x1, y1 = self.posicoes[i]
            rect = self.canvas.create_rectangle(x0, y0, x1, y1, fill='white')
            self.rectangles.append(rect)
            text_id = self.canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text='', font=("Arial", 12))
            self.text_ids.append(text_id)

    def atualizar_visualizacao(self):
        for i in range(self.tamanho):
            if i < len(self.elementos):
                self.canvas.itemconfig(self.rectangles[i], fill='green')
                self.canvas.itemconfig(self.text_ids[i], text=str(self.elementos[i]))
            else:
                self.canvas.itemconfig(self.rectangles[i], fill='white')
                self.canvas.itemconfig(self.text_ids[i], text='')

    def inserir(self, valor):
        if len(self.elementos) < self.tamanho:
            self.elementos.append(valor)
            self.atualizar_visualizacao()

    def remover(self):
        if self.elementos:
            self.elementos.pop(0)  # Remove sempre o primeiro da lista, como uma fila
            self.atualizar_visualizacao()

    def inserir_com_pausa(self, i, fim):
        if i < fim:
            self.inserir(self.numeros[i])
            self.root.after(500, self.inserir_com_pausa, i + 1, fim)  # Pausa de 300 ms entre as inserções

    def executar_passos(self):
        if self.passos == 0:
            # Inserir até completar
            for i in range(self.tamanho):
                self.inserir(self.numeros[i])
        elif self.passos == 1:
            # Remover 2 elementos
            for i in range(2):
                self.remover()
        elif self.passos == 2:
            # Inserir 1 elemento
            self.inserir(self.numeros[5])
        elif self.passos == 3:
            # Remover 1 elemento
            self.remover()
        elif self.passos == 4:
            # Remover 1 elemento
            self.remover()
        elif self.passos == 5:
            # Inserir até completar (com pausa)
            self.inserir_com_pausa(6, 8)

        # Avançar para o próximo passo
        self.passos += 1
        if self.passos <= 5:
            self.root.after(1000, self.executar_passos)

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaVisual(root, 5)
    root.mainloop()
