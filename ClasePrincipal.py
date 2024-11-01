import os
import mysql.connector
from Departamento import Departamento
from Empleado import Empleado
import informe
from Proyecto import Proyecto
from ProyectoEmpleado import ProyectoEmpleado
from RegistroTiempo import RegistroTiempo
from TipoEmpleado import TipoEmpleado
from prettytable import PrettyTable
import pandas as pd
import xlsxwriter


def mostrar_menu():
    """Muestra el menú principal de opciones."""
    print("=== Menú Principal ===")
    print("1) Agregar")
    print("2) Buscar")
    print("3) Editar")
    print("4) Eliminar")
    print("5) Registrar tiempo")
    print("6) Informe")
    print("7) Salir")
    print("=======================")


def mostrar_sub_menu_agregar():
    """Muestra el submenú para agregar nuevos registros."""
    print("=== Submenú de Agregar ===")
    print("1) Agregar departamento")
    print("2) Agregar Tipo de empleado")
    print("3) Agregar empleado")
    print("4) Agregar Proyecto")
    print("5) Asignar trabajador a proyecto")
    print("===========================")


def buscar_datos_de():
    """Muestra las opciones de búsqueda disponibles."""
    print("=== Submenú de Búsqueda ===")
    print("1) Buscar departamento")
    print("2) Buscar empleado")
    print("3) Buscar Proyecto")
    print("============================")


def mostrar_sub_menu_editar():
    """Muestra las opciones para editar registros existentes."""
    print("=== Submenú de Edición ===")
    print("1) Editar departamento")
    print("2) Editar empleado")
    print("3) Editar Proyecto")
    print("4) Reasignar departamento")
    print("5) Reasignar proyecto")
    print("===========================")


def mostrar_sub_menu_eliminar():
    """Muestra las opciones para eliminar registros."""
    print("=== Submenú de Eliminación ===")
    print("1) Eliminar departamento")
    print("2) Eliminar empleado")
    print("3) Eliminar Proyecto")
    print("===============================")


def mostrar_sub_menu_informe():
    """Muestra las opciones para informes."""
    print("=== Submenú de Informes ===")
    print("1) Departamentos y sus trabajadores")
    print("2) Empleados de la empresa")
    print("3) Proyectos y sus trabajadores")
    print("4) Registro de tiempos de cada empleado")
    print("===============================")


# Crear directorio para almacenamiento si no existe
CARPETA = "sistema/"


def crear_directorio():
    """Crea un directorio para almacenamiento si no existe."""
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)


def obtener_input_usuario(mensaje):
    """Obtiene y valida la entrada del usuario."""
    try:
        return int(input(mensaje))
    except ValueError:
        print("❌ Por favor, ingrese un número válido.")
        return None


def manejar_opcion_agregar(opcion):
    """Maneja la opción de agregar registros."""
    if opcion == 1:
        Departamento.obtener_info_departamento()
    elif opcion == 2:
        TipoEmpleado.obtener_info_tipo_empleado()
    elif opcion == 3:
        Empleado.obtener_info_empleado()
    elif opcion == 4:
        Proyecto.obtener_info_proyecto()
    elif opcion == 5:
        Proyecto.mostrar_proyectos()
        Empleado.mostrar_empleados()
        ProyectoEmpleado.asignar_Proyecto_A_Empleado()
    else:
        print("❌ Opción no válida.")


def manejar_opcion_buscar(opcion):
    """Maneja la opción de búsqueda."""
    if opcion == 1:
        id_a_buscar = input("Ingrese el ID del departamento a buscar: ")
        Departamento.buscar_departamento(id_a_buscar)
    elif opcion == 2:
        id_a_buscar = input("Ingrese el ID del empleado a buscar: ")
        Empleado.buscar_empleado(id_a_buscar)
    elif opcion == 3:
        id_a_buscar = input("Ingrese el ID del proyecto a buscar: ")
        Proyecto.buscar_proyecto(id_a_buscar)
    else:
        print("❌ Opción no válida.")


def manejar_opcion_editar(opcion):
    """Maneja la opción de editar registros."""
    if opcion == 1:
        Departamento.mostrar_departamentos()
        Departamento.editar_departamento(input("Ingrese el ID del departamento a editar: ")) 
    elif opcion == 2:
        Empleado.mostrar_empleados()
        Empleado.editar_empleado(input("Ingrese el ID del empleado a editar: "))         
    elif opcion == 3:
        Proyecto.mostrar_proyectos()
        Proyecto.editar_proyecto(input("Ingrese el ID del proyecto a editar: "))
    elif opcion == 4:
        Empleado.mostrar_resumen_empleados()
        print("Departamentos:")
        Departamento.mostrar_departamentos()
        id_empleado = input("Ingrese el ID del empleado que desea reasignar: ")
        nuevo_id_departamento = input("Ingrese el nuevo ID del departamento: ")
        Empleado.reasignar_departamento(id_empleado, nuevo_id_departamento)
    else:
        print("❌ Opción no válida.")


def manejar_opcion_eliminar(opcion):
    """Maneja la opción de eliminar registros."""
    if opcion == 1:
        Departamento.mostrar_departamentos()
        id_departamento_a_eliminar = input("Ingrese el ID del departamento a eliminar: ")
        Departamento.eliminar_departamento(id_departamento_a_eliminar)
    elif opcion == 2:
        Empleado.mostrar_empleados()
        id_empleado_a_eliminar = input("Ingrese el ID del empleado a eliminar: ")
        Empleado.eliminar_empleado(id_empleado_a_eliminar)
    elif opcion == 3:
        Proyecto.mostrar_proyectos()
        id_proyecto_a_eliminar = input("Ingrese el ID del proyecto a eliminar: ")
        Proyecto.eliminar_proyecto(id_proyecto_a_eliminar)
    else:
        print("❌ Opción no válida.")


def manejar_opcion_informe(opcion):
    """Maneja la opción de informes."""
    if opcion == 1:
        Departamento.informe_departamentos_y_trabajadores()
    elif opcion == 2:
        Empleado.mostrar_empleados()
        Empleado.informe_empleados()
    elif opcion == 3:
        Proyecto.informe_proyectos_y_empleados()
    elif opcion == 4:
        RegistroTiempo.informe_registro_tiempos()
    else:
        print("❌ Opción no válida.")


def app():
    """Función principal de la aplicación."""
    crear_directorio()
    mostrar_menu()

    while True:
        eleccion = obtener_input_usuario("Seleccione una opción: ")
        if eleccion is None:
            continue

        if eleccion == 1:
            mostrar_sub_menu_agregar()
            opcion = obtener_input_usuario("Seleccione una opción: ")
            if opcion is not None:
                manejar_opcion_agregar(opcion)

        elif eleccion == 2:
            buscar_datos_de()
            opcion = obtener_input_usuario("Ingrese una opción: ")
            if opcion is not None:
                manejar_opcion_buscar(opcion)

        elif eleccion == 3:
            mostrar_sub_menu_editar()
            opcion = obtener_input_usuario("Ingrese una opción: ")
            if opcion is not None:
                manejar_opcion_editar(opcion)

        elif eleccion == 4:
            mostrar_sub_menu_eliminar()
            opcion = obtener_input_usuario("Ingrese una opción: ")
            if opcion is not None:
                manejar_opcion_eliminar(opcion)

        elif eleccion == 5:
            RegistroTiempo.obtener_info_registro_tiempo()

        elif eleccion == 6:
            mostrar_sub_menu_informe()
            opcion = obtener_input_usuario("Seleccione una opción: ")
            if opcion is not None:
                manejar_opcion_informe(opcion)

        elif eleccion == 7:
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción no válida.")
        mostrar_menu()


# Ejecuta la aplicación si es el módulo principal
if __name__ == "__main__":
    app()