<?php
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
            'label' => app::get('AppName')->_('名称'),
            'width' => 110,
            'searchtype' => 'has',
            'in_list' => true,
            'default_in_list' => true,
        ),
        'modified_time' => array(
            'type' => 'last_modify',
            'label' => app::get('AppName')->_('更新时间'),
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
