import os
import mysql.connector
import hashlib
from Departamento import Departamento
from Empleado import Empleado
from Proyecto import Proyecto
from ProyectoEmpleado import ProyectoEmpleado
from RegistroTiempo import RegistroTiempo
from TipoEmpleado import TipoEmpleado

# Configuración de la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '',
    'database': 'gestion_empleados'
}

class Usuario:
    def __init__(self, db_config):
        """Inicializa la conexión a la base de datos."""
        self.db_config = db_config
        self.conexion = mysql.connector.connect(**self.db_config)
        self.cursor = self.conexion.cursor()

    def registrar_usuario(self, username, password, rol_id):
        """Registra un nuevo usuario en la base de datos."""
        id_empleado = self._obtener_id_empleado()  # Obtiene el ID de empleado
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        try:
            sql = "INSERT INTO usuarios (username, password_hash, rol_id, id_empleado) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(sql, (username, hashed_password, rol_id, id_empleado))
            self.conexion.commit()
            print("✅ Usuario registrado exitosamente.")
            return True
        except mysql.connector.Error as e:
            self._manejar_error_registro(e)
            return False

    def _obtener_id_empleado(self):
        """Solicita al usuario que ingrese un ID de empleado hasta que sea válido."""
        while True:
            id_empleado = input("Ingrese el ID del empleado: ")
            if id_empleado.strip():  # Verifica que no esté vacío
                # Verificar si el id_empleado existe en la tabla empleado
                sql = "SELECT COUNT(*) FROM empleado WHERE id_empleado = %s"
                self.cursor.execute(sql, (id_empleado,))
                if self.cursor.fetchone()[0] > 0:
                    return id_empleado
                else:
                    print("❌ El ID de empleado no existe. Inténtelo de nuevo.")
            else:
                print("❌ El ID de empleado no puede estar vacío. Inténtelo de nuevo.")

    def _manejar_error_registro(self, error):
        """Maneja errores durante el registro de usuarios."""
        if error.errno == 1062:
            print("❌ El usuario ya existe.")
        else:
            print(f"❌ Error al registrar el usuario: {error}")

    def validar_usuario(self, username, password):
        """Valida las credenciales de un usuario."""
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        sql = "SELECT password_hash, rol_id FROM usuarios WHERE username = %s"
        self.cursor.execute(sql, (username,))
        result = self.cursor.fetchone()

        if result:
            if result[0] == hashed_password:
                print("✅ Acceso concedido.")
                return result[1]  # Devuelve el rol_id
            else:
                print("❌ Contraseña incorrecta.")
                return None
        else:
            print("❌ Usuario no encontrado.")
            return None

    def cerrar_conexion(self):
        """Cierra la conexión a la base de datos."""
        self.cursor.close()
        self.conexion.close()