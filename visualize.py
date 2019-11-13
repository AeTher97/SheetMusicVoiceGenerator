def vizualize(drawContent):
    if len(drawContent) > 0:
        codes = {"c": -2, "d": -1, "e": 0, "f": 1, "g": 2, "a": 3, "h": 4}
        drawable = [0, 2, 4, 6, 8]

        content = []
        contentType = []
        for note in drawContent:
            content.append(note[0])
            contentType.append(note[1])

        drawC = False

        k = 8
        for j in range(11):
            toPrint = ""
            contentNumber = 0

            for i in range(3 * len(content) + 11):
                if i < 10:
                    if j == -1:
                        toPrint = "     "
                    if j == 0:
                        toPrint = "     "
                    if j == 1:
                        toPrint = "  /) "
                    if j == 2:
                        toPrint = "  |/ "
                    if j == 3:
                        toPrint = " /|  "
                    if j == 4:
                        toPrint = "/ |  "
                    if j == 5:
                        toPrint = "|/|\\"
                    if j == 6:
                        toPrint = "|\\| |"
                    if j == 7:
                        toPrint = "\\_|/ "
                    if j == 8:
                        toPrint = "  |  "
                    if j == 9:
                        toPrint = "/ |  "
                    if j == 10:
                        toPrint = "\\/   "
                    if j == 11:
                        toPrint = "     "

                else:
                    draw = False
                    if (i + 1) % 3 != 0:
                        if j in drawable:
                            toPrint += "-"
                        else:
                            toPrint += " "

                    if (i + 1) % 3 == 0:

                        if codes[content[contentNumber]] == k:
                            draw = True
                        else:
                            if j in drawable:
                                toPrint += "-"
                            else:
                                toPrint += " "
                        if contentNumber < len(content) - 1:
                            contentNumber += 1

                    if drawC:
                        toPrint = toPrint[:-1]
                        toPrint += "-"
                        drawC = False

                    if draw:
                        if k == -2:
                            toPrint = toPrint[:-2]
                            toPrint += "-o"
                            drawC = True
                        else:
                            toPrint = toPrint[:-1]
                            toPrint += "-o"


            k -= 1
            print(toPrint)


