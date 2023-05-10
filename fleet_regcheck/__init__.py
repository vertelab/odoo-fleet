from . import models
from . import controllers


def set_default_values():
    config = models.MyModuleSettings.create({})
    config.execute()

def post_init_hook(cr, registry):
    set_default_values()
