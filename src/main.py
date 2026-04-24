import flet as ft
from controllers.UserController import AuthController
from controllers.TareaController import TareaController
from view.loginview import LoginView
from view.dashboard import DashboardView

def start(page: ft.Page):

    page.title = "SIGE"
    page.theme_mode = ft.ThemeMode.LIGHT

    auth = AuthController()
    tareas = TareaController()

    def route_change(e):
        page.views.clear()

        try:
            if page.route == "/":
                page.views.append(LoginView(page, auth))

            elif page.route == "/dashboard":
                user = page.session.get("user")

                if not user:
                    page.go("/")
                    return

                page.views.append(DashboardView(page, tareas))

            else:
                page.views.append(
                    ft.View("/", [ft.Text("Página no encontrada")])
                )

            page.update()

        except Exception as ex:
            page.views.clear()
            page.views.append(
                ft.View("/", [ft.Text(f"ERROR: {str(ex)}")])
            )
            page.update()

    def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            page.go(page.views[-1].route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go("/")

ft.app(target=start)