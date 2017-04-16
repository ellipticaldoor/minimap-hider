import sublime_plugin
import sublime

class MinimapHider(sublime_plugin.ViewEventListener):

    def on_modified(self):
        region = sublime.Region(0, self.view.size())
        count = self.view.rowcol(self.view.size())[0] + 1
        self.view.window().set_minimap_visible(count > 100)

    on_new = on_activated = on_clone = on_modified
