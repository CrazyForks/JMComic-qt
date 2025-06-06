# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

from component.widget.animation_stack_widget import AnimationStackWidget
from component.widget.navigation_widget import NavigationWidget
from view.category.category_view import CategoryView
from view.comment.all_comment_view import AllCommentView
from view.comment.comment_view import CommentView
from view.comment.my_comment_view import MyCommentView
from view.comment.sub_comment_view import SubCommentView
from view.download.download_all_view import DownloadAllView
from view.download.download_some_view import DownloadSomeView
from view.download.download_view import DownloadView
from view.help.help_view import HelpView
from view.history.history_view import HistoryView
from view.history.remote_history_view import RemoteHistoryView
from view.index.index_view import IndexView
from view.index.week_view import WeekView
from view.info.book_eps_view import BookEpsView
from view.info.book_info_view import BookInfoView
from view.nas.nas_view import NasView
from view.read.read_view import ReadView
from view.search.search_view import SearchView
from view.setting.setting_view import SettingView
from view.tool.local_read_all_view import LocalReadAllView
from view.tool.local_read_eps_view import LocalReadEpsView
from view.tool.local_read_view import LocalReadView
from view.tool.waifu2x_tool_view import Waifu2xToolView
from view.user.favorite_view import FavoriteView
from view.user.local_favorite_view import LocalFavoriteView

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(800, 600)
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.totalStackWidget = QStackedWidget(self.centralwidget)
        self.totalStackWidget.setObjectName(u"totalStackWidget")
        self.subMainWindow = QWidget()
        self.subMainWindow.setObjectName(u"subMainWindow")
        self.horizontalLayout_2 = QHBoxLayout(self.subMainWindow)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.navigationWidget = NavigationWidget(self.subMainWindow)
        self.navigationWidget.setObjectName(u"navigationWidget")
        self.navigationWidget.setMinimumSize(QSize(240, 0))
        self.navigationWidget.setMaximumSize(QSize(280, 16777215))

        self.horizontalLayout_2.addWidget(self.navigationWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menuLayout = QHBoxLayout()
        self.menuLayout.setObjectName(u"menuLayout")
        self.menuButton = QPushButton(self.subMainWindow)
        self.menuButton.setObjectName(u"menuButton")

        self.menuLayout.addWidget(self.menuButton)

        self.label = QLabel(self.subMainWindow)
        self.label.setObjectName(u"label")

        self.menuLayout.addWidget(self.label)


        self.horizontalLayout_3.addLayout(self.menuLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.subStackWidget = AnimationStackWidget(self.subMainWindow)
        self.subStackWidget.setObjectName(u"subStackWidget")
        self.indexView = IndexView()
        self.indexView.setObjectName(u"indexView")
        self.subStackWidget.addWidget(self.indexView)
        self.downloadSomeView = DownloadSomeView()
        self.downloadSomeView.setObjectName(u"downloadSomeView")
        self.subStackWidget.addWidget(self.downloadSomeView)
        self.nasView = NasView()
        self.nasView.setObjectName(u"nasView")
        self.subStackWidget.addWidget(self.nasView)
        self.weekView = WeekView()
        self.weekView.setObjectName(u"weekView")
        self.subStackWidget.addWidget(self.weekView)
        self.localReadAllView = LocalReadAllView()
        self.localReadAllView.setObjectName(u"localReadAllView")
        self.subStackWidget.addWidget(self.localReadAllView)
        self.localReadEpsView = LocalReadEpsView()
        self.localReadEpsView.setObjectName(u"localReadEpsView")
        self.subStackWidget.addWidget(self.localReadEpsView)
        self.localReadView = LocalReadView()
        self.localReadView.setObjectName(u"localReadView")
        self.subStackWidget.addWidget(self.localReadView)
        self.downloadAllView = DownloadAllView()
        self.downloadAllView.setObjectName(u"downloadAllView")
        self.subStackWidget.addWidget(self.downloadAllView)
        self.helpView = HelpView()
        self.helpView.setObjectName(u"helpView")
        self.subStackWidget.addWidget(self.helpView)
        self.settingView = SettingView()
        self.settingView.setObjectName(u"settingView")
        self.subStackWidget.addWidget(self.settingView)
        self.searchView = SearchView()
        self.searchView.setObjectName(u"searchView")
        self.subStackWidget.addWidget(self.searchView)
        self.searchView2 = SearchView()
        self.searchView2.setObjectName(u"searchView2")
        self.subStackWidget.addWidget(self.searchView2)
        self.favoriteView = FavoriteView()
        self.favoriteView.setObjectName(u"favoriteView")
        self.subStackWidget.addWidget(self.favoriteView)
        self.bookInfoView = BookInfoView()
        self.bookInfoView.setObjectName(u"bookInfoView")
        self.subStackWidget.addWidget(self.bookInfoView)
        self.waifu2xToolView = Waifu2xToolView()
        self.waifu2xToolView.setObjectName(u"waifu2xToolView")
        self.subStackWidget.addWidget(self.waifu2xToolView)
        self.bookEpsView = BookEpsView()
        self.bookEpsView.setObjectName(u"bookEpsView")
        self.subStackWidget.addWidget(self.bookEpsView)
        self.commentView = CommentView()
        self.commentView.setObjectName(u"commentView")
        self.subStackWidget.addWidget(self.commentView)
        self.subCommentView = SubCommentView()
        self.subCommentView.setObjectName(u"subCommentView")
        self.subStackWidget.addWidget(self.subCommentView)
        self.downloadView = DownloadView()
        self.downloadView.setObjectName(u"downloadView")
        self.subStackWidget.addWidget(self.downloadView)
        self.allCommentView = AllCommentView()
        self.allCommentView.setObjectName(u"allCommentView")
        self.subStackWidget.addWidget(self.allCommentView)
        self.categoryView = CategoryView()
        self.categoryView.setObjectName(u"categoryView")
        self.subStackWidget.addWidget(self.categoryView)
        self.historyView = HistoryView()
        self.historyView.setObjectName(u"historyView")
        self.subStackWidget.addWidget(self.historyView)
        self.remoteHistoryView = RemoteHistoryView()
        self.remoteHistoryView.setObjectName(u"remoteHistoryView")
        self.subStackWidget.addWidget(self.remoteHistoryView)
        self.myCommentView = MyCommentView()
        self.myCommentView.setObjectName(u"myCommentView")
        self.subStackWidget.addWidget(self.myCommentView)
        self.localFavoriteView = LocalFavoriteView()
        self.localFavoriteView.setObjectName(u"localFavoriteView")
        self.subStackWidget.addWidget(self.localFavoriteView)

        self.verticalLayout.addWidget(self.subStackWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.totalStackWidget.addWidget(self.subMainWindow)
        self.readView = ReadView()
        self.readView.setObjectName(u"readView")
        self.totalStackWidget.addWidget(self.readView)

        self.horizontalLayout.addWidget(self.totalStackWidget)

        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"JMComic", None))
        self.menuButton.setText(QCoreApplication.translate("Main", u"\u83dc\u5355", None))
        self.label.setText(QCoreApplication.translate("Main", u">", None))
    # retranslateUi

