import sublime, sublime_plugin
import os
import functools

class CopyPathCommand(sublime_plugin.WindowCommand):
    def run(self, args):
        print(args)
        branch, leaf = os.path.split(args[0])
        v = self.window.show_input_panel("New Name:", leaf, functools.partial(self.on_done, args[0], branch), None, None)
        name, ext = os.path.splitext(leaf)

        v.sel().clear()
        v.sel().add(sublime.Region(0, len(name)))

    def on_done(self, old, branch, leaf):
        new = os.path.join(branch, leaf)

        try:
            os.rename(old, new)

            v = self.window.find_open_file(old)
            if v:
                v.retarget(new)
        except:
            sublime.status_message("Unable to rename")

    def is_visible(self, args):
        return len(args) == 1