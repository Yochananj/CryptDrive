import enum

class ViewsAndRoutesList(enum.Enum):
    HOME = "Home"
    SIGN_UP = "Sign Up"
    LOG_IN = "Log In"

    def get_route(self):
        return self.value