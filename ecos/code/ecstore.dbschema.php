<?php
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
      'label' => app::get('AppName')->_('名称'),
      'width' => 180,
      'is_title' => true,
      'required' => true,
      'comment' => app::get('AppName')->_('名称'),
      'editable' => true,
      'searchtype' => 'has',
      'in_list' => true,
      'default_in_list' => true,
    ),
    'last_modify' => array (
      'type' => 'last_modify',
      'label' => app::get('AppName')->_('更新时间'),
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
