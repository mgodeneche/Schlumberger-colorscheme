import sublime_plugin
import sublime


def do_disable_highlights(view):
    schlum6 = view.settings().get('schlum6', None)
    if schlum6 is None:
        return
    schlum8 = view.settings().get('schlum8', None)
    if schlum6 is None:
        return
    view.set_syntax_file(pre_schlumberger_syntax)
    view.settings().erase('pre_schlumberger_syntax')
    view.settings().erase('schlumberger_mode')
    file_path = view.file_name()
    #if file_path is not None:
    #    save_rainbow_params(file_path, '', 'disabled')

def do_enable_schlum(view,file_format):
    file_path = view.file_name()
    logging_enabled = get_setting(view, 'enable_debug_logging', False)
    dbg_log(logging_enabled, '=======================================')
    dbg_log(logging_enabled, 'Enabling Schlumberger higlighting for {}: '.format(file_format))
    pre_schlumberger_syntax = view.settings().get('syntax')
    if view.settings().get('pre_schlumberger_syntax', None) is None:
        view.settings().set('pre_schlumberger_syntax', pre_rainbow_syntax)
        view.settings().set('schlumberger_mode', True)

    dbg_log(logging_enabled, 'Saving rainbow params')

def do_set_color_scheme_to_schlumberger8(view):
    view.settings().set("color_scheme", "schlumberger8.sublime-color-scheme")
def do_set_color_scheme_to_schlumberger6(view):
    view.settings().set("color_scheme", "schlumberger6.sublime-color-scheme")


class Schlumberger6Command(sublime_plugin.TextCommand):
    def run(self, edit):
        do_set_color_scheme_to_schlumberger6(self)
        
    def is_enabled(self):
	    return True


class Schlumberger8Command(sublime_plugin.TextCommand):
    def run(self, edit):
        do_set_color_scheme_to_schlumberger8(self)

    def is_enabled(self):
    	return True

class DisableCommand(sublime_plugin.TextCommand):
    def run(self, _edit):
        do_disable_highlights(self.view)