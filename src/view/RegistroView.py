import flet as ft
from datetime import datetime

def RegistroView(page: ft.Page, auth_controller):

    def ver_contra(e):
        contra.password = not contra.password
        contra.update()

    # 🔹 CAMPOS
    nombre = ft.TextField(label="Nombre", icon=ft.Icons.BADGE)
    apellido = ft.TextField(label="Apellido", icon=ft.Icons.BADGE)
    telefono = ft.TextField(label="Teléfono", icon=ft.Icons.CALL)
    correo = ft.TextField(label="Correo", icon=ft.Icons.EMAIL)
    contra = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=False,
        icon=ft.Icons.LOCK,
        suffix=ft.IconButton(
            icon=ft.Icons.VISIBILITY,
            on_click=ver_contra
        )
    )

    mensaje = ft.Text(color="red")

  
    def registra(e):
        
        if not all([nombre.value, apellido.value, telefono.value, correo.value, contra.value]):
            mensaje.value = "Completa todos los campos"
            page.update()
            return

        fecha = datetime.now().strftime("%Y-%m-%d")

        user, msg = auth_controller.registrar_Usuario(
            nombre.value,
            apellido.value,
            correo.value,
            contra.value,
            telefono.value,
            fecha
        )

        if user:
         
            page.user_data = user

            page.snack_bar = ft.SnackBar(ft.Text("Usuario registrado correctamente"))
            page.snack_bar.open = True

            page.go("/dashboard")  
        else:
            mensaje.value = msg

        page.update()

   
    registrar_btn = ft.ElevatedButton(
        "Registrarse",
        bgcolor="blue",
        color="white",
        on_click=registra
    )

    def regresar(e):
        page.go("/")

    volver_btn = ft.TextButton("¿Ya tienes cuenta? Inicia sesión", on_click=regresar)

    # 🔹 VISTA
    return ft.View(
        route="/registro",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("Registro"),
            bgcolor=ft.Colors.BLUE_GREY_900,
            color="white"
        ),
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(ft.Icons.ACCOUNT_BOX, size=60, color=ft.Colors.BLUE),
                        ft.Text("Crear cuenta", size=28, weight="bold"),

                        ft.Row([nombre, apellido], alignment=ft.MainAxisAlignment.CENTER),
                        telefono,
                        correo,
                        contra,

                        registrar_btn,
                        volver_btn,
                        mensaje
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=15
                ),
                width=350
            )
        ]
    )