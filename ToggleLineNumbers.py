import sublime_plugin


class ToggleLineNumbersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        on = self.view.settings().get('line_numbers')
        self.view.settings().set('line_numbers', not on)
