'''Estás desarrollando un sistema de autenticación para una aplicación web y
deseas implementar un sistema de inicio de sesión que verifique si las
credenciales proporcionadas por el usuario son válidas antes de permitir el
acceso a ciertas funciones. Además, deseas que una vez que el usuario haya
iniciado sesión correctamente, se le proporcione información personal.
Implementa lo siguiente:
1. Un registro de usuarios que contenga información adicional, como el
nombre completo y el correo electrónico.
2. Un decorador llamado verificar_inicio_sesion que acepte el nombre de
usuario y la contraseña como argumentos. Este decorador verificará si las
credenciales proporcionadas son válidas comparándolas con el registro de
usuarios. Si las credenciales son válidas, la función decorada se ejecutará y
se le pasará como argumento la información personal del usuario.
3. Una función llamada informacion_usuario que imprima la información personal
del usuario después de que haya iniciado sesión correctamente.
Implementa este sistema de inicio de sesión utilizando decoradores.'''

usuarios_registrados={
    "usuario1":{"contraseña" : "contraseña123", "nombre" : "David Sanchez", "mail" : "dsg@example.com"},
    "usuario2":{"contraseña" : "contraseña456", "nombre" : "Nuria Tortosa", "mail" : "ntp@example.com"},
    "usuario3":{"contraseña" : "contraseña789", "nombre" : "Israel Gonzalez", "mail" : "igr@example.com"},
}


def verificar_incio_sesion(funcion):
    def wrapper(usuario, contraseña):
        if usuario in usuarios_registrados and usuarios_registrados[usuario]["contraseña"]==contraseña:
            print("Inicio de sesion correcta para el usuario", usuario)
            usuario_info = usuarios_registrados[usuario]
            return (funcion(usuario_info))
        else:
            print("El usuario indicado no tiene las credenciales correctas")
    return wrapper


@verificar_incio_sesion
def informacion_usuario(usuario_info):
    print("Información usuario:")
    print("Nombre completo del usuario: ",usuario_info["nombre"])
    print("Correo electrónico del usuario: ",usuario_info["mail"])

informacion_usuario("usuario1", "contraseña123")
informacion_usuario("usuario3", "contraseña787")