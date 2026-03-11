
from qgis.PyQt.QtCore import QT_VERSION_STR
from qgis.PyQt.QtCore import Qt

QT_MAJOR = int(QT_VERSION_STR.split(".", 1)[0])

if QT_MAJOR >= 6:
    SCROLLBAR_AS_NEEDED = Qt.ScrollBarPolicy.ScrollBarAsNeeded
    SCROLLBAR_ALWAYS_OFF = Qt.ScrollBarPolicy.ScrollBarAlwaysOff
    SCROLLBAR_ALWAYS_ON = Qt.ScrollBarPolicy.ScrollBarAlwaysOn
    CHECKED = Qt.CheckState.Checked
    UNCHECKED = Qt.CheckState.Unchecked
    PARTIALLY_CHECKED = Qt.CheckState.PartiallyChecked
else:
    SCROLLBAR_AS_NEEDED = Qt.ScrollBarAsNeeded
    SCROLLBAR_ALWAYS_OFF = Qt.ScrollBarAlwaysOff
    SCROLLBAR_ALWAYS_ON = Qt.ScrollBarAlwaysOn
    CHECKED = Qt.Checked
    UNCHECKED = Qt.Unchecked
    PARTIALLY_CHECKED = Qt.PartiallyChecked