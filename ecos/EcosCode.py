# -*- coding: utf-8 -*-
# coding: utf-8
# encoding="utf-8"
import os

class EcosCode:
    """docstring for EcosCode"""
    def __init__(self):
        super(EcosCode, self).__init__()
    def generate(self, create_type, className,fileName,ecos):
        if create_type == "model":
            code = """<?php

class DumnyClass extends dbeav_model
{

}"""
        elif create_type == "controller":
            code = """<?php
            
class DumnyClass extends desktop_controller
{
    
}

"""
        elif create_type == "api":
            code = """<?php
class DumnyClass 
{
    public $apiDescription = 'api description';

    public $use_strict_filter = true; // 是否严格过滤参数
  
    public function handle($params)
    {
        $result = kernel::single('xxxx')->handle($params);
        if($result)
        {
            //event::fire('xxx.xxxx', array($itemId));
        }
        return $result;
    }

    public function getParams()
    {
        $return['params'] = [
            'id' => ['type'=>'integer','valid'=>'required|min:1','description'=>'id','msg'=>'ID不能为空'],
        ];
        return $return;
    }
    
    /**
     * 返回json格式的例子
     * @return string 结果json串
     */
    public function returnJson()
    {
        return '{
          "error": null,
          "result": {
          }
        }';
    }

}

"""
            code = code.replace('FunctionName','')
        elif create_type == "dbschema":
            code = self.getDbschemaCode(ecos,fileName)
        else:
            code = """<?php

class DumnyClass
{

}"""
        name, ext = os.path.splitext(fileName)
        code = code.replace("DumnyClass",className)
        return code  
    def getDbschemaCode(self,ecos,fileName):
        if ecos.isBbc():
            code = """<?php
/**
 * ShopEx licence
 *
 * @copyright  Copyright (c) 2005-2014 ShopEx Technologies Inc. (http://www.shopex.cn)
 * @license  http://ecos.shopex.cn/ ShopEx License
 */
return array(
    'columns' => array(
        'id' => array(
            'type' => 'number',
            'required' => true,
            'autoincrement' => true,
            'comment' => app::get('AppName')->_('ID'),
            'width' => 110,
        ),
        'name' => array(
            'type' => 'string',
            'length' => 100,
            'required' => true,
            'is_title' => true,
            'default' => '',
            'label' => app::get('AppName')->_('name'),
            'width' => 110,
            'searchtype' => 'has',
            'in_list' => true,
            'default_in_list' => true,
        ),
        'created_time' => array(
            'type' => 'time',
            'in_list' => true,
            'default_in_list' => true,
            'filterdefault' => true,
            'width' => '150',
            'order' => 17,
            'label' => app::get('AppName')->_('创建时间'),
            'comment' => app::get('AppName')->_('创建时间'),
        ),
        'modified_time' => array(
            'type' => 'last_modify',
            'label' => app::get('AppName')->_('modified_time'),
            'width' => 110,
            'in_list' => true,
            'orderby' => true,
        ),
     ),
    'primary' => 'id',
    'index' => array(
        'ind_name' => ['columns' => ['name']],
        'ind_modified_time' => ['columns' => ['modified_time']],
    ),
    'comment' => app::get('AppName')->_('TableName'),
);

"""
        else:
            code= """<?php
/**
 * ShopEx licence
 *
 * @copyright  Copyright (c) 2005-2010 ShopEx Technologies Inc. (http://www.shopex.cn)
 * @license  http://ecos.shopex.cn/ ShopEx License
 */

$db['TableName']= array (
  'columns' => array (
    'id' => array (
      'type' => 'number',
      'required' => true,
      'pkey' => true,
      'extra' => 'auto_increment',
      'label' => app::get('AppName')->_('id'),
      'width' => 150,
      'comment' => app::get('AppName')->_('id'),
      'editable' => false,
      'in_list' => false,
      'default_in_list' => false,
    ),
    'name' => array (
      'type' => 'varchar(50)',
      'label' => app::get('AppName')->_('name'),
      'width' => 180,
      'is_title' => true,
      'required' => true,
      'comment' => app::get('AppName')->_('name'),
      'editable' => true,
      'searchtype' => 'has',
      'in_list' => true,
      'default_in_list' => true,
    ),
    'last_modify' => array (
      'type' => 'last_modify',
      'label' => app::get('AppName')->_('last_modify'),
      'width' => 110,
      'editable' => false,
      'in_list' => true,
      'orderby' => true,
    ),
  ),
  'index' =>  [
    'ind_name' => ['columns' => ['name']],
    'ind_last_modify' => ['columns' => ['last_modify']],
  ],
  'comment' => app::get('AppName')->_('TableName'),
);
"""
        tableName = fileName.replace('.php','')
        print(code)
        code = code.replace('AppName',ecos.getAppName()).replace('TableName',tableName)
        return code
