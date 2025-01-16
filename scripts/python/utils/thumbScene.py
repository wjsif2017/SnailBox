import time
import hou
from .allSetting import ALLSET
from .snailFun import display_status


class Sence_Viewer:
    def __init__(self):
        self.win_mini = True

    def init_sc_tab(self, node_path=None, option=0):
        try:
            if option == 0:
                sc_tab2 = hou.ui.findPaneTab("Snail_sc")
                if not sc_tab2:
                    return
                self.sc_win2 = sc_tab2.qtParentWindow()
                if self.sc_win2:
                    self.sc_win2.showMinimized()
                    return sc_tab2
            for i in range(1):
                i += 1
                sc_tab2 = self.get_sc_tab(node_path)
                if not sc_tab2:
                    return
                time.sleep(0.2)
                self.sc_win2 = sc_tab2.qtParentWindow()
                if self.sc_win2:
                    if self.win_mini and option != 1:
                        self.sc_win2.showMinimized()
                    elif option == 1:
                        self.win_mini = False
                        self.sc_win2.showNormal()
                    return sc_tab2
        except Exception as e:
            display_status(f"Snail_error_ut: init_sc_tab _ {e}")
            return

    def get_view_node(self):
        try:
            obj = hou.node("/obj")
            node = hou.node("/obj/SnailBox_thumb")
            if node:
                node.destroy(1)
            h_version = float(ALLSET.h_version)
            if h_version > 18.5:
                node = obj.createNode("SnailBox::snail_thumb", "SnailBox_thumb")
            else:
                node = obj.createNode("SnailBox::snail_thumb_o", "SnailBox_thumb")
            node.setColor(
                hou.Color(
                    0.3,
                    0.3,
                    0.3,
                )
            )
            node.hide(1)
            display_node = hou.node("/obj/SnailBox_thumb/SnailBox_view")
            return display_node
        except Exception as e:
            display_status(f"Snail_error_uts: get_view_node _ {e}")
            return

    def get_sc_tab(self, option=0):
        try:
            sc_tab = hou.ui.findPaneTab("Snail_sc")
            view_node = self.get_view_node()
            if not view_node:
                return
            if sc_tab:
                sc_tab.close()

            sc_floatPanel = hou.ui.curDesktop().createFloatingPanel(hou.paneTabType.SceneViewer)

            sc_floatPanel.setSize((600, 750))

            sc_tab = sc_floatPanel.paneTabs()[0]
            sc_tab.setName("Snail_sc")
            sc_tab.setPin(True)
            sc_view = sc_tab.curViewport()
            sc_set = sc_view.settings()

            sc_set.setLighting(hou.viewportLighting.Headlight)
            sc_set.setDisplayEnvironmentBackgroundImage(0)
            sc_set.setDisplayBackgroundImage(0)
            sc_set.setVisibleObjects("/obj/SnailBox_thumb")

            return sc_tab
        except Exception as e:
            display_status(f"Snail_error_uts: get_sc_tab _ {e}")
            return


SC_VIEWER = Sence_Viewer()
