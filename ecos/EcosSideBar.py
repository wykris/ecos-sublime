# encoding="utf-8"

import sublime
import os,sys
import re
import shutil
from .SideBarAPI import SideBarItem, SideBarSelection, SideBarProject



class EcosSideBar():

    """ 当前操作的文件路径 """
    path = "" #/data/httpd/ecstore/app/base/lib/http.php
    """ 当前操作的文件基本路径 """
    basePath = "" #/data/httpd/ecstore/
    selectRelativePath = ""#app/base/lib/http.php or app/base/lib/
    sideBarItem = ""
    customPathName = "custom"
    appPathName    = "app"
    apiConfigName = 'config/apis.php'
    classDict = {'controller':'_ctl_','model':'_mdl_','api':'_api_','dbschema':'_dbschema_'}

    def __init__(self, paths):
        self.path = SideBarSelection(paths)._paths[0]
        self.initPath()

    def initPath(self):
        self.sideBarItem = SideBarItem(self.path,os.path.isdir(self.path))
        self.selectRelativePath = self.sideBarItem.pathRelativeFromProjectEncoded()
        self.basePath = self.path.replace(self.selectRelativePath,"")
        print(self.selectRelativePath,self.basePath)

    def getAppName(self):
        paths = self.selectRelativePath.split(os.sep,2)
        return paths[1]

    def getFileAbsolutePath(self,classFileName):
        return os.path.join(self.path,classFileName) 

    ## 根据文件名获取ECOS的类名
    def getClassFullName(self,classFileName):
        fullName = os.path.join(self.selectRelativePath,classFileName) 
        return self.getClassByPath(fullName)

    def getClassType(self,className):
        for k,v in self.classDict.items():
            if className.find(v) > 0:
                return k
        return 'lib'

    def getViewPath(self,viewName):
        if viewName.find('/')< 1:
            pass
        viewName = viewName.replace('/',os.sep)
        if self.isBbc():
            appName ,viewPath = viewName.split(os.sep,1)
            return os.path.join(self.basePath,self.appPathName,self.getAppName(),'view',viewPath)
        else:
            return os.path.join(self.basePath,self.appPathName,self.getAppName(),'view',viewName)
        pass
    def getApiClassNameByApiName(self,name):
        path = os.path.join(self.basePath,self.apiConfigName)
        content = open(path, 'r', encoding="utf-8").read()
        content = content.split(os.linesep)
        for line in content:
            if line.find(name) > 0 :
                newline = line.replace('"','\'').split('\'')
                return newline[5].split('@')[0]
            pass
        return "";

    def getClassByPath(self,path):
        prefix,classPath = path.split(os.sep,1)
        className = classPath.replace(self.packPath('controller'),self.packPath('ctl'))
        className = className.replace(self.packPath('model'),self.packPath('mdl'))
        className = className.replace(self.packPath('lib'),os.sep)
        className = className.replace(self.packPath('dbschema'),self.packPath('dbschema'))
        className = className.replace(self.packPath('api'),self.packPath('api'))
        className = className.replace('.php','').replace('/','_')
        return className

    def getClassPathByClassName(self,className):
        classNameNew = ''
        for k,v in self.classDict.items():
            if className.find(v) > 0:
                classNameNew = className.replace(v,'_' + k + '_')
        if classNameNew == '':
            classNametpm = className.split('_',1)
            classNameNew = classNametpm[0] + '_lib_' + classNametpm[1]
            pass
        return os.path.join(self.basePath, self.appPathName, classNameNew.replace('_', os.sep))+'.php'

    def getCustomPath(self):
        paths = self.selectRelativePath.split(os.sep,1)
        return os.path.join(self.basePath ,self.customPathName , paths[1])

    def packPath(self,path):
        return os.sep+path+os.sep

    def isEcos(self):
        return os.path.isdir(os.path.join(self.basePath,'app','base')) 

    def isBbc(self):
        return self.isEcos() and os.path.isdir(self.basePath+'vendor') 

    def isEcstore(self):
        return self.isEcos() and self.isBbc() == False

    def isDir(self):
        return self.sideBarItem.isDirectory()
  
