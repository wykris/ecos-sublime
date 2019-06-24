# 商派ECOS框架开发插件
此插件专门针对EOOS框架开发，其支持Ecstore、ERP、OMS等基于ECOS开发的产品。
此插件包含以下功能：
## 一键跳转
### Go To API 一键打开API
商派BBC是基于微服务设计的一个多用户商城系统，在模块间通信时，是通过app::get('topm')->rpcCall('xxx.xxx.xxx')这种方式调用的。在日常开发中，经常会通过api名称去查找对应的源文件，此功能可以实现选中api名称，一键打开API对应的源文件。
### Go To View 一键打开模板
 选中需要打开的模板路径，右键
## 文件创建
### Customize This File 一键二开
为了适应产品二开的需求ECOS采用复制源文件到二开目录的方式，此功能可以实现一键复制二开文件，并在编辑器中打开二开文件。
### New ECOS Class 新建ECOS类
创建符合ECOS规范的class，支持ecstore和bbc，可以创建 Controller Model Api Lib 的Class，及Dbschema文件

