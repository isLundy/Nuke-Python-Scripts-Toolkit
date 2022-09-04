#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Plugins Path
#
#----------------------------------------------------------------------------------------------------------

import nuke
import nukescripts
import os
import platform
import subprocess
from PySide2 import QtGui

class PluginsPath(nukescripts.PythonPanel):
    def __init__(self):
        nukescripts.PythonPanel.__init__(self, "Path of All Plugins", "com.ohufx.Pathofplugins")
        self.panelWidth_min = 1500
        self.panelHeight_min = 340
        self.setMinimumSize(self.panelWidth_min, self.panelHeight_min)
        self.setMaximumSize(5120, 1440)
        self.setFloat = 0
        self.floatPane = nuke.PyScript_Knob("floatPane", "Flaot Pane")
        self.spacer3 = nuke.Text_Knob("spacer3", "")
        self.method = nuke.Enumeration_Knob("method", "By", ["Selected Node", "KeyWord"])
        self.keyWord = nuke.String_Knob("keyWord", "")
        self.keyWord.setEnabled(False)
        self.keyWord.clearFlag(nuke.STARTLINE)
        self.to = nuke.Text_Knob("to", " ", "to ")
        self.to.clearFlag(nuke.STARTLINE)
        self.search = nuke.PyScript_Knob("search", "Search")
        self.search.clearFlag(nuke.STARTLINE)
        self.keyWord_tips = nuke.Text_Knob("keyWord_tips", " ")
        self.keyWord_tips.setValue("Tips: Keyword length must be at least 3 characters (excluding spaces).")
        self.keyWord_tips.setEnabled(False)
        self.spacer0 = nuke.Text_Knob("spacer0", "")
        self.types = nuke.Enumeration_Knob("types", "Types", ["For Nodes", "All"])

        self.allPath = sorted([path for path in (set(nuke.plugins() + nuke.plugins(nuke.ALL))) if os.path.isfile(path)])
        self.allExt = sorted(set([os.path.basename(path).split('.')[-1] for path in self.allPath]))
        self.nodesCheckBoxs = []
        self.otherCheckBoxs = []
        
        # keyWord, search, keyWord_tips, types
        for k in (self.floatPane, self.spacer3, self.method, self.keyWord, self.to, self.search, self.keyWord_tips, self.spacer0, self.types):
            self.addKnob(k)
        
        # gizmo, nk 
        for ext in self.allExt:
            if ext in ['gizmo', 'nk']:
                self.sinExt = nuke.Boolean_Knob(ext, ".{}".format(ext), True)
                self.addKnob(self.sinExt)
                self.nodesCheckBoxs.append(self.sinExt)
        
        # hide or show
        self.types_hide = []
        
        # other ext
        self.other = nuke.Text_Knob("other", " ", " ")
        self.other.setFlag(nuke.STARTLINE)
        self.other.setVisible(False)
        self.addKnob(self.other)
        self.types_hide.append(self.other)
        
        for ext in self.allExt:
            if ext not in ['gizmo', 'nk']:
                self.sinExt = nuke.Boolean_Knob(ext, ".{}".format(ext), False)
                self.sinExt.setVisible(False)
                self.addKnob(self.sinExt)
                self.otherCheckBoxs.append(self.sinExt)
                self.types_hide.append(self.sinExt)
        
        # selected, deselected
        self.types_tips = nuke.Text_Knob("types_tips", " ", "All file types in all plugin directories was listed.")
        self.types_tips.setFlag(nuke.STARTLINE)
        self.types_tips.setEnabled(False)
        self.types_tips.setVisible(False)
        self.spacer1 = nuke.Text_Knob("spacer1", "", " ")
        self.spacer1.setFlag(nuke.STARTLINE)
        self.spacer1.setVisible(False)
        self.selectAllTypes = nuke.PyScript_Knob("selectAllTypes", "Select  All  Types")
        self.selectAllTypes.setFlag(nuke.STARTLINE)
        self.selectAllTypes.setVisible(False)
        self.deselectAllTypes = nuke.PyScript_Knob("deselectAllTypes", "deSelect  All  Types")
        self.deselectAllTypes.clearFlag(nuke.STARTLINE)
        self.deselectAllTypes.setVisible(False)
        for k in (self.types_tips, self.spacer1, self.selectAllTypes, self.deselectAllTypes):
            self.addKnob(k)
            self.types_hide.append(k)
        
        # result
        self.spacer2 = nuke.Text_Knob("spacer2", "")
        self.search_result_title = nuke.Text_Knob("search_result_title", "Result", " ")
        self.search_result_clear = nuke.PyScript_Knob("search_result_clear", "Clear")
        self.search_result_clear.setVisible(False)
        for k in ( self.spacer2, self.search_result_title, self.search_result_clear):
            self.addKnob(k)
        
        # list of search result
        self.search_result = {}
        
        # first open
        try:
            nuke.selectedNode()
        except:
            self.method.setValue(1)
            self.keyWord.setEnabled(True)
        else:
            self.searchBySelectedNode()

    def add_knobs(self, n, fullPath, basename):
        self.plugin_path = nuke.String_Knob("plugin_path_{}".format(n), "{} path".format(n), os.path.dirname(fullPath).replace('\\', '/') + "/")
        self.plugin_path.setFlag(nuke.STARTLINE)
        self.plugin_path.setFlag(0x0000000010000000)
        self.plugin_name = nuke.String_Knob("plugin_name_{}".format(n), "", basename)
        self.plugin_name.clearFlag(nuke.STARTLINE)
        self.plugin_name.setFlag(0x0000000010000000)
        self.open_folder = nuke.PyScript_Knob("open_folder_{}".format(n), "Open Folder")
        self.open_file = nuke.PyScript_Knob("open_file_{}".format(n), "Open File")
        self.copy_fullPath = nuke.PyScript_Knob("copy_fullPath_{}".format(n), "Copy Full Path")
        
        # add result knobs for search
        for k in (self.plugin_path, self.plugin_name, self.open_folder, self.open_file, self.copy_fullPath):
            self.addKnob(k)
            
        self.search_result[n] = [self.plugin_path, self.plugin_name, self.open_folder, self.open_file, self.copy_fullPath]

    def selectedTypes(self):
        selectedExt = []
        
        if self.types.getValue() == 0:
                for checkBox in self.nodesCheckBoxs:
                    if checkBox.getValue() == True:
                        selectedExt.append(checkBox.name())
        else:
            for checkBox in (self.nodesCheckBoxs + self.otherCheckBoxs):
                if checkBox.getValue() == True:
                    selectedExt.append(checkBox.name())
                        
        return selectedExt

    def getNode_CN(self):
        # get class and name from node
        node = nuke.selectedNode()
        node_class = node.Class()
        node_name = node.name()
        org_name = node.name()
        
        for other in nuke.selectedNodes():
            other.setSelected(False)

        node.setSelected(True)
        
        # remove number or symbol from node name
        while node_name[-1].isalpha() == False:
            node_name = node_name[:-1]
        
        # minimum length of node name
        if len(node_class) >= 3 and len(node_name) >= 3:
            return node_class, node_name, org_name
       
    def searchByKeyWord(self):
        # define variable
        n = 0
        
        # confirm keyWord
        word = self.keyWord.getValue().strip()
        self.keyWord.setValue(word)
        self.keyWord.setEnabled(True)
        
        # check keyWord
        if word != "" and len(word)>=3:
            
            selectedExt = self.selectedTypes()

            # check selected ext
            if selectedExt:
                for fullPath in self.allPath:
                    basename = os.path.basename(fullPath)
                    ext = basename.split(".")[-1]
                    
                    # confirm word
                    if word.lower() in basename.lower() and ext in selectedExt:
                        n += 1
                        self.add_knobs(n, fullPath, basename)
                
                # setting result title and layout size
                if n == 0:
                    if "gizmo" in selectedExt or "nk" in selectedExt:
                        self.search_result_title.setValue("<span style='color:#ff4d4d'>No exit !</span> (Maybe you can recreate the node and try agin.)")
                    else:
                        self.search_result_title.setValue("<span style='color:#ff4d4d'>No exit !</span>")
                        
                    self.search_result_clear.setVisible(False)
                    if self.setFloat == 0:
                        self.setMinimumSize(self.panelWidth_min, self.panelHeight_min)
                else:
                    self.search_result_title.setValue("total: {} ".format(n))
                    self.search_result_clear.setVisible(True)
                    
                    if self.setFloat == 0:
                        panelHeight = self.panelHeight_min + (n-1)*25
                        if panelHeight <= 600:
                            self.setMinimumSize(self.panelWidth_min, panelHeight)
                        else:
                            panelHeight = 600
                            self.setMinimumSize(self.panelWidth_min, panelHeight)

            # no selected ext
            else:
                self.search_result_title.setValue("<span style='color:#ff4d4d'>Please select at least one file type !</span>")
                self.search_result_clear.setVisible(False)
                if self.setFloat == 0:
                    self.setMinimumSize(self.panelWidth_min, self.panelHeight_min)

        # check 0 < keyWord < 3        
        elif len(word) > 0 and len(word) < 3:
            self.search_result_title.setValue("<span style='color:#ff4d4d'>Missing KeyWord !</span>")
            self.search_result_clear.setVisible(False)
            if self.setFloat == 0:
                self.setMinimumSize(self.panelWidth_min, self.panelHeight_min)
        
        # check keyWord == 0
        elif len(word) == 0:
            self.search_result_title.setValue(" ")
            self.search_result_clear.setVisible(False)
            if self.setFloat == 0:
                self.setMinimumSize(self.panelWidth_min, self.panelHeight_min)
            
    def searchBySelectedNode(self):
        # get info of node
        node_class, node_name, org_name = self.getNode_CN()
        self.keyWord.setValue(org_name)
        self.keyWord.setEnabled(False)
        
        selectedExt = self.selectedTypes()
        
        # define variable
        n = 0
        
        # check selected ext
        if selectedExt:
            # verify that the node is a group
            if node_class.lower != "group":
                for fullPath in self.allPath:
                    basename = os.path.basename(fullPath)
                    ext = basename.split('.')[-1]
                
                    if (node_class.lower() in basename.lower() or node_name.lower() in basename.lower()) and ext in selectedExt:
                        n += 1
                        self.add_knobs(n, fullPath, basename)

            else:
                for fullPath in self.allPath:
                    basename = os.path.basename(fullPath)
                    ext = basename.split('.')[-1]
                    
                    if node_name.lower() in basename.lower() and ext in selectedExt:
                        n += 1
                        self.add_knobs(n, fullPath, basename)
                    
            if n == 0:
                if "gizmo" in selectedExt or "nk" in selectedExt:
                    self.search_result_title.setValue("<span style='color:#ff4d4d'>Maybe you can recreate the node and try agin.</span> (or try searching by KeyWord.)")
                else:
                    self.search_result_title.setValue("<span style='color:#ff4d4d'>No exit !</span>")
                    
                self.search_result_clear.setVisible(False)
                
            else:
                self.search_result_title.setValue("total: {} ".format(n))
                self.search_result_clear.setVisible(True)
                
        # no selected ext
        else:
            self.search_result_title.setValue("<span style='color:#ff4d4d'>Please select at least one file type !</span>")
            self.search_result_clear.setVisible(False)
            if self.setFloat == 0:
                self.setMinimumSize(self.panelWidth_min, self.panelHeight_min)

    def removeSearchResult(self):
        # remove knobs
        if self.search_result:
            for knobs in self.search_result.values():
                for k in knobs:
                    self.removeKnob(k)

            self.search_result = {}

    def searchPath(self):
        # remove knobs
        self.removeSearchResult()
        
        if self.method.getValue() == 0:
            try:
                nuke.selectedNode()
            except:
                self.keyWord.setValue("")
                self.search_result_title.setValue("<span style='color:#ff4d4d'>No node selected !</span>")
                self.search_result_clear.setVisible(False)
            else:
                self.searchBySelectedNode()
        else:
            self.searchByKeyWord()
        
    def openThePath(self, path):
        # open folder
        operatingSystem = platform.system()
        
        if operatingSystem == "Windows":
            subprocess.Popen("explorer {}".format(path.replace('/', '\\')))
        elif operatingSystem == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])
          
    def knobChanged(self, knob):
        # button_float pane
        if knob == self.floatPane:
            self.finishModalDialog(False)
            ppPanel = PluginsPath()
            ppPanel.floatPane.setVisible(False)
            ppPanel.setMinimumSize(0, 0)
            ppPanel.setFloat = 1
            ppPanel.show()
            
        # button_method
        elif knob == self.method:
            if self.method.getValue() == 0:
                self.keyWord.setEnabled(False)
                for checkBox in self.nodesCheckBoxs:
                    checkBox.setValue(1)
            else:
                self.keyWord.setEnabled(True)
                
        # button_Search
        elif knob == self.search:
            self.searchPath()

        # button_Types
        elif knob == self.types:
            if self.types.getValue() == 0.0:
                for k in self.types_hide:
                    k.setVisible(False)
                
                for checkBox in self.nodesCheckBoxs:
                    checkBox.setValue(True)
            else:
                for k in self.types_hide:
                    k.setVisible(True)

        # button_selectAllTypes
        elif knob == self.selectAllTypes: 
            for checkBox in (self.nodesCheckBoxs + self.otherCheckBoxs):
                checkBox.setValue(True)
        
        # button_deselectAllTypes
        elif knob == self.deselectAllTypes: 
            for checkBox in (self.nodesCheckBoxs + self.otherCheckBoxs):
                checkBox.setValue(False)
              
        # button_Clear 
        elif knob == self.search_result_clear:
            self.removeSearchResult()
            self.search_result_title.setValue(" ")
            self.search_result_clear.setVisible(False)
            if self.setFloat == 0:
                self.setMinimumSize(self.panelWidth_min, self.panelHeight_min)
        
        # button_Open the Folder
        elif "open_folder" in knob.name():
            for list_knobs in self.search_result.values():
                if knob in list_knobs:
                    path = list_knobs[0].getValue()
                    self.openThePath(path)

        # button_open the file
        elif "open_file" in knob.name():
            for list_knobs in self.search_result.values():
                if knob in list_knobs:
                    path = list_knobs[0].getValue() + list_knobs[1].getValue()
                    self.openThePath(path)

        # button_copy the full path
        elif "copy_fullPath" in knob.name():
            for list_knobs in self.search_result.values():
                if knob in list_knobs:
                    fullPath = list_knobs[0].getValue() + list_knobs[1].getValue()
                    QtGui.QGuiApplication.clipboard().setText(fullPath)
                    
ppPanel = PluginsPath()
ppPanel.showModal()