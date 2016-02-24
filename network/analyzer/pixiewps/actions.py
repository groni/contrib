#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
WorkDir="pixiewps-"+ get.srcVERSION() +"/src/"

def build():
    autotools.make()

def install():
    pisitools.dosbin("pixiewps", "usr/bin")
    pisitools.dodoc("../LICENSE.md", "../README.md")
