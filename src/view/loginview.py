import flet as ft

def LoginView(page, auth_controller):

    page.bgcolor = "#f8bbd0"  
    correo = ft.TextField(
        label="Correo electrónico",
        width=300,
        border_radius=10
    )

    contraseña = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=300,
        border_radius=10
    )

    mensaje = ft.Text(color="red")

    def login(e):
        user = auth_controller.model.validar_login(correo.value, contraseña.value)

        if user:
            page.session.set("user", user)
            page.go("/dashboard")
        else:
            mensaje.value = "Correo o contraseña incorrectos"
            page.update()

    return ft.View(
        route="/",
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(ft.icons.AUTO_AWESOME, size=60, color="pink"),
                        ft.Text("Bienvenido", size=28, weight="bold", color="pink"),
                        correo,
                        contraseña,
                        ft.ElevatedButton(
                            "Iniciar sesión",
                            width=200,
                            bgcolor="pink",
                            color="white",
                            on_click=login
                        ),
                        mensaje
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=15
                ),
                alignment=ft.alignment.center,
                expand=True
            )
        ]
    )