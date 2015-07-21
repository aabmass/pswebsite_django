""" Array of all possible menus """
menus = []

########## Module wrapping menus and their creation ##########

##
# @brief A class wrapping the menu objects.
#
# Note: These ARE the menus that go in the nav
class Menu:
    ##
    # @brief Create a new menu object
    #
    # @param name Actual string for the appearing menu
    # @param route_func_name Route to the view for the given menuentry.
    # @param submenus Option arg: array of submenus of this menu
    #
    # @return 
    def __init__(self, name, route_func_name, visible=True, submenus=[]):
        self._name = name
        self._route_func_name = route_func_name
        self._submenus = submenus
        self._visible = visible

    # Properties
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def route_func_name(self):
        return self._route_func_name

    @route_func_name.setter
    def route_func_name(self, route_func_name):
        self._route_func_name = route_func_name

    def visible(self, request):
        return self._visible
    
    @property
    def submenus(self):
        return self._submenus

    @submenus.setter
    def submenus(self, subs):
        self._submenus = subs

    def display_submenus(self):
        """ Boolean of whether or not to render the submenu at all
            Checks that there is at least one visible submenu
        """
        if self._submenus:
            for m in self._submenus:
                if m.visible:
                    return True

        return False

class AuthDependentMenu(Menu):
    def __init__(self, name, route_func_name, visible=True, submenus=[]):
        super().__init__(name, route_func_name, visible, submenus)

    def isAuthenticated(self, request):
        return request.user and \
                request.user.is_authenticated()

class UserMenu(AuthDependentMenu):
    def __init__(self, name, route_func_name, visible=True, submenus=[]):
        self.logoutMenu = Menu("Logout", "pswebsite:logout", False)
        submenus.append(self.logoutMenu)
        super().__init__(name, route_func_name, visible, submenus)

    # Lets override visible() as a pseudo-hook
    def visible(self, request):
        # Change the names if we have auth
        if self.isAuthenticated(request):
            # note, the username will be the email
            # as this is being enforced in the app
            self.name = request.user.username
            self.route_func_name = "pswebsite:user"

            # Turn on the logout submenu
            self.logoutMenu.visible = True
        else:
            self.name = "Login"
            self.route_func_name = "pswebsite:login"

            # Turn off the logout submenu
            self.logoutMenu.visible = False
        return super().visible(request)

class RegisterMenu(AuthDependentMenu):
    def __init__(self, name, route_func_name, visible=True, submenus=[]):
        super().__init__(name, route_func_name, visible, submenus)

    def visible(self, request):
        return not self.isAuthenticated(request)



def createApplicationMenus():
    home = Menu("Home", "pswebsite:index")
    about = Menu("About", "pswebsite:about")

    menus.append(home)
    menus.append(about)

    users = UserMenu("Login", "pswebsite:login")
    menus.append(users)

    register = RegisterMenu("Register", "pswebsite:register")
    menus.append(register)
