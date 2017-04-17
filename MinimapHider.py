import sublime_plugin

class MinimapHider(sublime_plugin.ViewEventListener):

	def on_modified(self):
		count = self.view.rowcol(self.view.size())[0] + 1
		self.view.window().set_minimap_visible(count > 100)

	on_activated = on_modified
