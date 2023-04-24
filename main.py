import sublime_plugin
import sublime


class Schlumberger6Command(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.settings().set("color_scheme", "schlumberger6.sublime-color-scheme")

	def is_enabled(self):
	    return True


class Schlumberger8Command(sublime_plugin.TextCommand):
    def run(self, edit):
         self.view.settings().set("color_scheme", "schlumberger8.sublime-color-scheme")

    def is_enabled(self):
    	return True
