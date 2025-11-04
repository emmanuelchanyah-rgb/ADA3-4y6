import tkinter as tk
from tkinter import messagebox, simpledialog
from collections import deque

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


class ArbolBusqueda:
    def __init__(self):
        self.raiz = None

    def esVacio(self):
        return self.raiz is None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar(nodo.izq, valor)
        elif valor > nodo.valor:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar(nodo.der, valor)

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscar(nodo.izq, valor)
        else:
            return self._buscar(nodo.der, valor)

    def _minimo(self, nodo):
        while nodo.izq:
            nodo = nodo.izq
        return nodo

    def _maximo(self, nodo):
        while nodo.der:
            nodo = nodo.der
        return nodo

    def eliminar_predecesor(self, valor):
        self.raiz = self._eliminar_predecesor(self.raiz, valor)

    def _eliminar_predecesor(self, nodo, valor):
        if nodo is None:
            return None
        if valor < nodo.valor:
            nodo.izq = self._eliminar_predecesor(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._eliminar_predecesor(nodo.der, valor)
        else:
            if nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            predecesor = self._maximo(nodo.izq)
            nodo.valor = predecesor.valor
            nodo.izq = self._eliminar_predecesor(nodo.izq, predecesor.valor)
        return nodo

    def eliminar_sucesor(self, valor):
        self.raiz = self._eliminar_sucesor(self.raiz, valor)

    def _eliminar_sucesor(self, nodo, valor):
        if nodo is None:
            return None
        if valor < nodo.valor:
            nodo.izq = self._eliminar_sucesor(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._eliminar_sucesor(nodo.der, valor)
        else:
            if nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            sucesor = self._minimo(nodo.der)
            nodo.valor = sucesor.valor
            nodo.der = self._eliminar_sucesor(nodo.der, sucesor.valor)
        return nodo

    def recorrer_niveles(self):
        if self.raiz is None:
            return []
        cola = deque([self.raiz])
        resultado = []
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.valor)
            if nodo.izq:
                cola.append(nodo.izq)
            if nodo.der:
                cola.append(nodo.der)
        return resultado

    def preOrden(self, nodo, recorrido):
        if nodo:
            recorrido.append(nodo.valor)
            self.preOrden(nodo.izq, recorrido)
            self.preOrden(nodo.der, recorrido)

    def inOrden(self, nodo, recorrido):
        if nodo:
            self.inOrden(nodo.izq, recorrido)
            recorrido.append(nodo.valor)
            self.inOrden(nodo.der, recorrido)

    def postOrden(self, nodo, recorrido):
        if nodo:
            self.postOrden(nodo.izq, recorrido)
            self.postOrden(nodo.der, recorrido)
            recorrido.append(nodo.valor)

    def altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self.altura(nodo.izq), self.altura(nodo.der))

    def contar_hojas(self, nodo):
        if nodo is None:
            return 0
        if nodo.izq is None and nodo.der is None:
            return 1
        return self.contar_hojas(nodo.izq) + self.contar_hojas(nodo.der)

    def contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.contar_nodos(nodo.izq) + self.contar_nodos(nodo.der)

    def es_completo(self):
        if self.raiz is None:
            return True
        cola = deque([self.raiz])
        vacio = False
        while cola:
            nodo = cola.popleft()
            if nodo:
                if vacio:
                    return False
                cola.append(nodo.izq)
                cola.append(nodo.der)
            else:
                vacio = True
        return True

    def es_lleno(self, nodo):
        if nodo is None:
            return True
        if nodo.izq is None and nodo.der is None:
            return True
        if nodo.izq and nodo.der:
            return self.es_lleno(nodo.izq) and self.es_lleno(nodo.der)
        return False

    def eliminar_arbol(self):
        self.raiz = None


class InterfazArbol:
    def __init__(self, master):
        self.master = master
        self.master.title("Árbol Binario de Búsqueda - Tkinter")
        self.master.geometry("950x600")

        self.arbol = ArbolBusqueda()

        # Frame de botones
        frame_botones = tk.Frame(master)
        frame_botones.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        botones = [
            ("Insertar", self.insertar),
            ("Buscar", self.buscar),
            ("Eliminar Predecesor", self.eliminar_predecesor),
            ("Eliminar Sucesor", self.eliminar_sucesor),
            ("PreOrden", self.mostrar_preorden),
            ("InOrden", self.mostrar_inorden),
            ("PostOrden", self.mostrar_postorden),
            ("Por Niveles", self.mostrar_niveles),
            ("Altura", self.mostrar_altura),
            ("Contar Hojas", self.mostrar_hojas),
            ("Contar Nodos", self.mostrar_nodos),
            ("¿Completo?", self.verificar_completo),
            ("¿Lleno?", self.verificar_lleno),
            ("Eliminar Árbol", self.eliminar_arbol),
        ]

        for texto, comando in botones:
            tk.Button(frame_botones, text=texto, width=20, command=comando).pack(pady=3)

        # Canvas de dibujo
        self.canvas = tk.Canvas(master, bg="white", width=700, height=600)
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def insertar(self):
        try:
            valor = int(simpledialog.askstring("Insertar", "Ingrese valor:"))
            self.arbol.insertar(valor)
            self.dibujar_arbol()
        except:
            messagebox.showerror("Error", "Valor inválido")

    def buscar(self):
        valor = simpledialog.askinteger("Buscar", "Valor a buscar:")
        if self.arbol.buscar(valor):
            messagebox.showinfo("Resultado", f"El valor {valor} SÍ está en el árbol.")
        else:
            messagebox.showwarning("Resultado", f"El valor {valor} NO se encuentra.")

    def eliminar_predecesor(self):
        valor = simpledialog.askinteger("Eliminar (Predecesor)", "Valor a eliminar:")
        self.arbol.eliminar_predecesor(valor)
        self.dibujar_arbol()

    def eliminar_sucesor(self):
        valor = simpledialog.askinteger("Eliminar (Sucesor)", "Valor a eliminar:")
        self.arbol.eliminar_sucesor(valor)
        self.dibujar_arbol()

    def mostrar_preorden(self):
        recorrido = []
        self.arbol.preOrden(self.arbol.raiz, recorrido)
        messagebox.showinfo("PreOrden", " → ".join(map(str, recorrido)))

    def mostrar_inorden(self):
        recorrido = []
        self.arbol.inOrden(self.arbol.raiz, recorrido)
        messagebox.showinfo("InOrden", " → ".join(map(str, recorrido)))

    def mostrar_postorden(self):
        recorrido = []
        self.arbol.postOrden(self.arbol.raiz, recorrido)
        messagebox.showinfo("PostOrden", " → ".join(map(str, recorrido)))

    def mostrar_niveles(self):
        recorrido = self.arbol.recorrer_niveles()
        messagebox.showinfo("Por niveles", " → ".join(map(str, recorrido)))

    def mostrar_altura(self):
        h = self.arbol.altura(self.arbol.raiz)
        messagebox.showinfo("Altura", f"Altura del árbol: {h}")

    def mostrar_hojas(self):
        hojas = self.arbol.contar_hojas(self.arbol.raiz)
        messagebox.showinfo("Hojas", f"Cantidad de hojas: {hojas}")

    def mostrar_nodos(self):
        nodos = self.arbol.contar_nodos(self.arbol.raiz)
        messagebox.showinfo("Nodos", f"Cantidad de nodos: {nodos}")

    def verificar_completo(self):
        completo = self.arbol.es_completo()
        messagebox.showinfo("Completo", "Sí" if completo else "No")

    def verificar_lleno(self):
        lleno = self.arbol.es_lleno(self.arbol.raiz)
        messagebox.showinfo("Lleno", "Sí" if lleno else "No")

    def eliminar_arbol(self):
        self.arbol.eliminar_arbol()
        self.canvas.delete("all")
        messagebox.showinfo("Eliminar", "Árbol eliminado correctamente")

    def dibujar_arbol(self):
        self.canvas.delete("all")

        def dibujar_nodo(nodo, x, y, dx):
            if nodo:
                self.canvas.create_oval(x-15, y-15, x+15, y+15, fill="#A7C7E7")
                self.canvas.create_text(x, y, text=str(nodo.valor))
                if nodo.izq:
                    self.canvas.create_line(x, y+15, x-dx, y+60-15)
                    dibujar_nodo(nodo.izq, x-dx, y+60, dx/2)
                if nodo.der:
                    self.canvas.create_line(x, y+15, x+dx, y+60-15)
                    dibujar_nodo(nodo.der, x+dx, y+60, dx/2)

        dibujar_nodo(self.arbol.raiz, 350, 40, 150)

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazArbol(root)
    root.mainloop()
