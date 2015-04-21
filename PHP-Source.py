import sublime
import sublime_plugin


class MakeSourceCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        fileRegion = sublime.Region(0, self.view.size())

        fileContents = self.view.substr(fileRegion)

        sourceName = self.view.file_name()

        out = ""

        if sourceName == None:  # user hasn't saved the file yet
            return
        elif isPHPFile(sourceName):
            out = sourceName + "s"
        else:
            out = sourceName + ".phps"

        open(out, 'w').write(fileContents)


def isPHPFile(fileName):

    try:
        extensionIndex = fileName.rindex(".php")

        return fileName[:extensionIndex] + ".php" == fileName

    except ValueError:
        return False
