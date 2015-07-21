from pswebsite import environment
from pswebsite.menus import menus as all_menus

def proj_vars(request):
    """ Adds the proj_vars dictionary to the context if enabled
        This dictionary contains project name, global menus, etc..
    """
    return {'proj_vars': environment.proj_vars}

def menus(request):
    """ This adds the menus to the context as a dictionary
        mapping 'menu' to an array of menus to be displayed.

        This allows the menu logic to be processed outside of
        the templates
    """
    dict_to_add = {'menus': []}
    for m in all_menus:
        if m.visible(request):
            dict_to_add['menus'].append(m)

    return dict_to_add
