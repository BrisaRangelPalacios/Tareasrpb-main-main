import flet as ft
from src.controllers.UserController import AuthController
from src.controllers.TareaController import TareaController
from src.views.loginview import LoginView
from src.views.dashboard import DashboardView

def main(page: ft.Page):
    # Instanciamos los controladores una sola vez
    auth_ctrl = AuthController()
    task_ctrl = TareaController()

    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))

        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))

        page.update()

    page.on_route_change = route_change
    page.go("/")

if __name__ == "__main__":
    ft.run(main)