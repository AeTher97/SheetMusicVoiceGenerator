from subprocess import *
import os

def generate(titleData,composer,tagline,notes):

    staffAdded = " "

    for i in notes:
        staffAdded += i
        staffAdded += " "

    staff = "\\score {"
    staff += "\\new Staff << \n"
    staff += "\\new Voice \\relative c' {"
    staff += "\\set midiInstrument = #\"flute\""
    staff += "\\key g \\major"
    staff += "\\time 3/4"
    staff += staffAdded
    staff += "}"
    staff += ">>"

    # title = "\\header {"
    # title += "title = \"" + titleData + "\""
    # title += "composer = \"" + composer + "\""
    # title += "tagline = \"Copyright:\"" + tagline + "\""
    # title += "}"
    #
    # title = """\header {
    #   title = "title"
    #   composer = "composer"
    #   tagline = "Copyright: tagline"
    # }"""

    title = "\\header {"
    title += "title = \"" + titleData + "\""
    title += "composer = \"" + composer + "\""
    title += "tagline = \"Copyright: " + tagline +"\""
    title += "}"


    layout = """ \\layout { }
    \\midi {
      \\context {
        \\Staff
        \\remove "Staff_performer"
      }
      \\context {
        \\Voice
        \\consists "Staff_performer"
      }
      \\tempo 2 = 100
     }
    }"""

    fileName = "file.ly"
    file = open(fileName, "w")

    file.write(title + staff + layout)

    lilypond_popenargs = ["lilypond", fileName]
    Popen(lilypond_popenargs)

    os.system("clear")




