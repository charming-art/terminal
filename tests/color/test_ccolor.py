# preview: https://raw.githubusercontent.com/charming-art/public-files/master/test_ccolor.png

import charming as cm

cm.full_screen()
cm.no_cursor()

c0 = cm.CColor()
c1 = cm.CColor('@')
c2 = cm.CColor('@', cm.RED)
c3 = cm.CColor('@', cm.RED, cm.YELLOW)

cm.stroke(c0)
cm.point(0, 0)  # nothing

cm.stroke(c1)
cm.point(1, 1)  # ('@', cm.WHITE, cm.BLACK)

cm.stroke(c2)
cm.point(2, 2)  # ('@', cm.RED, cm.BLACK)

cm.stroke(c3)
cm.point(3, 3)  # ('@', cm.RED, cm.YELLOW)

cm.run()
