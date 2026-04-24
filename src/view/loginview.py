import flet as ft

def LoginView(page, auth_controller):

    correo = ft.TextField(label="Correo", width=300)
    contraseña = ft.TextField(label="Contraseña", password=True, width=300)
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
                        ft.Text("SIGE - Login", size=30, weight="bold"),
                        correo,
                        contraseña,
                        ft.ElevatedButton("Iniciar sesión", on_click=login),
                        mensaje
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                alignment=ft.alignment.center,
                expand=True
            )
        ]
    )