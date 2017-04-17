import sublime_plugin

class MinimapHider(sublime_plugin.EventListener):

    def on_modified(self, view):
        count = view.rowcol(view.size())[0] + 1
        view.window().set_minimap_visible(count > 100)

    on_activated = on_modified
