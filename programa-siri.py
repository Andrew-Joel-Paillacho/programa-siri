 
 
import webbrowser

print("Bienvenido, Byron")
dia = input("Ingrese un día de la semana: ")

match dia:
    case "lunes":
        print("Hoy debes, hacer ejercicios")
    case "martes":
        print("Hoy debes, hacer las compras")
    case "miércoles":
        print("Hoy debes, ver películas")
        print("¿Deseas que te recomiende un canal?")
        tipoWeb=input("Dime si o no: ")
        if tipoWeb == "si":
            webbrowser.open_new_tab("https://www.disneyplus.com/")
    case "jueves":
        print("Hoy debes, hacer deberes")
    case "viernes":
        print("Hoy debes, jugar fútbol")
    case _:
        print("No existe actividad para ess día")
