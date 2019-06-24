import sublime, sublime_plugin
import os,shutil
import functools
class CopyfileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if len(self.view.file_name()) > 0:
			file_name = self.view.file_name();
			name, ext = os.path.splitext(file_name)
			copy_file = name+".copy"+ext
			shutil.copy(file_name,copy_file);
			self.view.window().open_file(copy_file, sublime.ENCODED_POSITION);
			branch, leaf = os.path.split(copy_file)
			
			v = self.view.window().show_input_panel("New Name:", leaf, functools.partial(self.on_done, copy_file, branch), None, None)
			name, ext = os.path.splitext(leaf)

			v.sel().clear()
			v.sel().add(sublime.Region(0, len(name)))
		pass
	def on_done(self, old, branch, leaf):
		new = os.path.join(branch, leaf)

		try:
			os.rename(old, new)

			v = self.view.window().find_open_file(old)
			if v:
				v.retarget(new)
		except:
			sublime.status_message("Unable to rename")

	



