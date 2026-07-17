from ui.components.banner import show_banner
from ui.components.divider import draw_divider
from ui.components.footer import show_footer
from ui.components.loading import show_loading

def show_startup():
    show_banner()

    draw_divider()

    show_loading()

    show_footer()


# also have this one, as i continue to work i beileve i will figure out which one i want to use 

from  banner import show_banner
from theme_dividers import draw_divider
from theme_loading import show_loading
from theme_footer import show_footer


def show_startup():

    show_banner()

    draw_divider()

    show_loading()

    draw_divider()

    show_footer()
