import tkinter as tk
import random


ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.geometry("420x480")
ventana.config(bg="#f0f0f0")


piedra_img = tk.PhotoImage(file="piedra.png")
papel_img = tk.PhotoImage(file="papel.png")
tijera_img = tk.PhotoImage(file="tijera.png")


opciones = ["Piedra", "Papel", "Tijera"]


resultado_texto = tk.StringVar()
resultado_texto.set("¡Haz tu elección!")
contador_jugador = 0
contador_pc = 0
contador_empate = 0


label_resultado = tk.Label(ventana, textvariable=resultado_texto, font=("Calibri", 14), bg="#f0f0f0")
label_resultado.pack(pady=15)

marcador = tk.Label(ventana, text=f"Jugador: {contador_jugador}  |  PC: {contador_pc}  |  Empates: {contador_empate}",
                    font=("Calibri", 12), bg="#e0e0e0", width=40)
marcador.pack(pady=10)


def actualizar_marcador():
    marcador.config(text=f"Jugador: {contador_jugador}  |  PC: {contador_pc}  |  Empates: {contador_empate}")


def jugar(eleccion_jugador):
    global contador_jugador, contador_pc, contador_empate

    eleccion_pc = random.choice(opciones)

    if eleccion_jugador == eleccion_pc:
        resultado = "Empate 😐"
        contador_empate += 1
    elif (eleccion_jugador == "Piedra" and eleccion_pc == "Tijera") or \
         (eleccion_jugador == "Papel" and eleccion_pc == "Piedra") or \
         (eleccion_jugador == "Tijera" and eleccion_pc == "Papel"):
        resultado = "¡Ganaste! 😎"
        contador_jugador += 1
    else:
        resultado = "Perdiste 😢"
        contador_pc += 1

    resultado_texto.set(f"Tú: {eleccion_jugador}  |  PC: {eleccion_pc}\n{resultado}")
    actualizar_marcador()


frame_botones = tk.Frame(ventana, bg="#f0f0f0")
frame_botones.pack(pady=25)

btn_piedra = tk.Button(frame_botones, image=piedra_img, command=lambda: jugar("Piedra"))
btn_piedra.grid(row=0, column=0, padx=10)

btn_papel = tk.Button(frame_botones, image=papel_img, command=lambda: jugar("Papel"))
btn_papel.grid(row=0, column=1, padx=10)

btn_tijera = tk.Button(frame_botones, image=tijera_img, command=lambda: jugar("Tijera"))
btn_tijera.grid(row=0, column=2, padx=10)


def reiniciar():
    global contador_jugador, contador_pc, contador_empate
    contador_jugador = contador_pc = contador_empate = 0
    resultado_texto.set("¡Haz tu elección!")
    actualizar_marcador()

btn_reiniciar = tk.Button(ventana, text="🔄 Reiniciar", font=("Calibri", 12), bg="#90caf9", command=reiniciar)
btn_reiniciar.pack(pady=10)


btn_salir = tk.Button(ventana, text="Salir", font=("Calibri", 12), bg="#ef5350", command=ventana.destroy)
btn_salir.pack(pady=10)

ventana.mainloop()
