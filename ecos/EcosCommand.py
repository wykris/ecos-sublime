# -*- coding: utf-8 -*-
# coding: utf-8
# encoding="utf-8"
import sublime
import sublime_plugin
import os,shutil
import functools
from .SideBarAPI import SideBarItem, SideBarSelection, SideBarProject
from .EcosSideBar import EcosSideBar
from .EcosCode import EcosCode

def Window(window = None):
    #window 是一个窗口，就是通过subl打开的 打开的一个文件就是一个view
    return window if window else sublime.active_window()

#新建class
class NewecosclassCommand(sublime_plugin.WindowCommand):

    def is_visible(self, paths = [], create_type = "auto"):
        ecos = EcosSideBar(paths)
        return ecos.isEcos() and ecos.isDir()

    def run(self, paths = [], create_type = "auto"):
        ecos = EcosSideBar(paths)

        leaf = "classname.php"
        #显示底部输入面板 functools.partial设置用户输入完名称
        v = Window().show_input_panel("New Ecos Class:", leaf, functools.partial(self.on_done, ecos,create_type), None, None)
        # name, ext = os.path.splitext(leaf)
        name = 'classname'
        v.sel().clear()
        v.sel().add(sublime.Region(0, len(name)))
    def on_done(self, ecos,create_type, fileName):
        filePath = ecos.getFileAbsolutePath(fileName)
        className = ecos.getClassFullName(fileName)

        if create_type == "auto":
            create_type = ecos.getClassType(className)
        #print(filePath,className,create_type)
        code = EcosCode().generate(create_type,className,fileName,ecos)
        # print(code)
        # return 
        file = open(filePath,'w', encoding="utf-8")
        file.write(code)
        file.close()
        
        try:
            Window().open_file(filePath, sublime.ENCODED_POSITION);
            v = self.view.window().find_open_file(filePath)
            if v:
                v.retarget(filePath)
            sublime.status_message("create laravel class success!")
        except:
            sublime.status_message("Unable to rename")
#一键二开
class CustomCommand(sublime_plugin.TextCommand):
    def is_visible(self):
        paths = self.view.file_name()
        if len(paths) < 1:
            return False
        ecos = EcosSideBar([paths])
        return ecos.isEcos()
    def run(self, edit):
        file_name = self.view.file_name();
        ecos = EcosSideBar([file_name])
        custom_name = ecos.getCustomPath()
        custom_path = os.path.dirname(custom_name);
        if not os.path.exists(custom_path):
            os.makedirs(custom_path);
        pass
        if os.path.exists(file_name) and not os.path.exists(custom_name):  
            shutil.copy(file_name,custom_name);
            self.view.window().open_file(custom_name, sublime.ENCODED_POSITION);
            #sublime.active_window().open_file(custom_name, sublime.ENCODED_POSITION);
        else:               
            self.view.window().open_file(custom_name, sublime.ENCODED_POSITION);
            #sublime.active_window().open_file(custom_name, sublime.ENCODED_POSITION);
        pass   
#Go To Api
class GotoapiCommand(sublime_plugin.TextCommand):
    def is_visible(self):
        paths = self.view.file_name()
        print("go to api is_visible",paths)
        if len(paths) < 1:
            return False
        ecos = EcosSideBar([paths])
        return ecos.isBbc()
    def run(self, edit):
        paths = self.view.file_name()
        print("go to api ",paths)
        ecos = EcosSideBar([paths])
        select_text = self.view.substr(sublime.Region(self.view.sel()[0].a,self.view.sel()[0].b));
        className = ecos.getApiClassNameByApiName(select_text)
        if className == '':
            return False
        path = ecos.getClassPathByClassName(className)

        ecosnew = EcosSideBar([path])
        customPath = ecosnew.getCustomPath()
        if os.path.exists(customPath):
            path = customPath
        pass
        self.view.window().open_file(path, sublime.ENCODED_POSITION);



    def is_visible(self):
        select = self.view.substr(sublime.Region(self.view.sel()[0].a,self.view.sel()[0].b))
        return len(select) > 1 and select.find(".")>0

class EcosgotoanythingCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        select_text = self.view.substr(sublime.Region(self.view.sel()[0].a,self.view.sel()[0].b));
        if len(select_text) < 1:
            return False
        pass
        if select_text.find('/')> 0 :
            print(select_text)
        return True

class GotoecosviewCommand(sublime_plugin.TextCommand):
    def is_visible(self):
        paths = self.view.file_name()
        print("go to api is_visible",paths)
        if len(paths) < 1:
            return False
        select_text = self.view.substr(sublime.Region(self.view.sel()[0].a,self.view.sel()[0].b));
        if len(select_text) < 1:
            return False
        pass
        ecos = EcosSideBar([paths])
        return ecos.isEcos()
    def run(self, edit):
        paths = self.view.file_name()
        ecos = EcosSideBar([paths])
        select_text = self.view.substr(sublime.Region(self.view.sel()[0].a,self.view.sel()[0].b));
        if len(select_text) < 1:
            return False
            pass
        path = ecos.getViewPath(select_text)
        if path == '':
            return False
        ecosnew = EcosSideBar([path])
        customPath = ecosnew.getCustomPath()
        if os.path.exists(customPath):
            path = customPath
        pass
        self.view.window().open_file(path, sublime.ENCODED_POSITION);

class AppSnippetHandler(sublime_plugin.EventListener):
    def on_query_context(self, view, key, op, operand, match_all):
        # print(key,op,operand,match_all)
        return None
    def on_query_completions(self, view, prefix, locations):
        # print(locations,prefix)
        ecos = EcosSideBar([view.file_name()])
        if prefix.find('app') == 0:
            return [
                ["app_\t app::get('name')->_('name')", "app::get('"+ecos.getAppName()+"')->_('$1')"], 
                ["apprpc\t app::get('name')->rpcCall('name')", "app::get('${1:"+ecos.getAppName()+"}')->rpcCall('$2'${3:, []})"], 
                ["appmodel\t app::get('name')->model('name')", "\$$1Model = app::get('"+ecos.getAppName()+"')->model('$1')"], 
            ]
        pass

        return []
        

class MytesttestCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        #self.view.window().show_input_panel("hahaha","heiheihei",self.on_done,self.on_change,self.on_cancel)
        self.view.window().show_quick_panel("hahaha","heiheihei",self.on_done,self.on_change,self.on_cancel)
        return False
    def on_done(self,args):
        pass
    def on_change(self,args):
        pass
    def on_cancel(self,args):
        pass

