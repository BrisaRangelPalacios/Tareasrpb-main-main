import flet as ft
from controllers.UserController import AuthController
from controllers.TareaController import TareaController
from view.LoginView import LoginView
from view.dashboardView import DashboardView
from view.RegistroView import RegistroView
from view.UserView import UserView, ModificarView

def start(page: ft.Page):
    page.title = "Sistema SIGE"

    auth_ctrl = AuthController()
    task_ctrl = TareaController()

    def route_change(e):
        page.views.clear()

        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))

        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))

        page.update()

    page.on_route_change = route_change

    page.go("/")

def main():
    ft.app(target=start)  

if __name__ == "__main__":
    main() 