import npyscreen

class ParentActionForm(npyscreen.ActionForm):
    def __init__(self, database=None, name=None, parentApp=None, framed=None, help=None, color='FORMDEFAULT', widget_list=None, cycle_widgets=False, *args, **keywords):
        super().__init__(name=name, parentApp=parentApp, framed=framed, help=help, color=color, widget_list=widget_list, cycle_widgets=cycle_widgets, *args, **keywords)

        self.database = database

        