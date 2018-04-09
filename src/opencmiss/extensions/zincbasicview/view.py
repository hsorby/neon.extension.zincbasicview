
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QToolButton, QSpacerItem, QSizePolicy

from opencmiss.neon.extensions.zinc_views import ZincView
from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget


class ZincBasicView(ZincView):

    def __init__(self, context, parent=None):
        super(ZincBasicView, self).__init__(parent)
        self._context = context
        self._context.getMaterialmodule().defineStandardMaterials()
        self._context.getGlyphmodule().defineStandardGlyphs()

        self._sceneviewer_widget = SceneviewerWidget()
        self._sceneviewer_widget.setContext(context)

        view_all_button = QToolButton()
        view_all_button.clicked.connect(self._view_all_triggered)

        spacer = QSpacerItem(40, 5, QSizePolicy.Expanding, QSizePolicy.Minimum)

        tool_button_layout = QHBoxLayout()
        tool_button_layout.setContentsMargins(5, 5, 5, 0)
        tool_button_layout.addWidget(view_all_button)
        tool_button_layout.addSpacerItem(spacer)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addLayout(tool_button_layout)
        main_layout.addWidget(self._sceneviewer_widget)
        self.setLayout(main_layout)

    def _view_all_triggered(self):
        self._sceneviewer_widget.viewAll()
