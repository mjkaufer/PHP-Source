import sublime
import sublime_plugin


class MakeSourceCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        fileRegion = sublime.Region(0, self.view.size())

        fileContents = self.view.substr(fileRegion)

        sourceName = self.view.file_name()

        outName = ""

        if sourceName == None:  # user hasn't saved the file yet
            return
        elif sourceName.endswith(".php"):
            outName = sourceName + "s"
        else:
            outName = sourceName + ".phps"

        with open(outName, 'w') as outFile:
            outFile.write(fileContents)