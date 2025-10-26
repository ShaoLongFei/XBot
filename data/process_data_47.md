# 客服工单数据集 - Part 47

本文件包含 114 个已处理的客服工单，已进行隐私脱敏处理。

---

## 为什么我的资源包没抵扣

**分类**：对象存储｜其他类咨询

### 问题描述

为什么我的ch 储存资源包没抵扣

### 客服解答

您好，您这边是什么时候购买的呢？目前月初出账期的，这个月的账单还没有出来的，您这边可以等明天再看下的，目前出的是10月份的账单的

### 根本原因分析

用户操作不当或产品使用方法咨询

---

## 可视化迁移工具

**分类**：对象存储｜数据迁移

### 问题描述

有没有可视化的迁移工具

### 客服解答

您好您这边是不同账号下不同存储区域的数据迁移吗 不同情况的数据迁移方式是不一样的

您好A、不同账号下相同存储区域的数据迁移，有两种方法1、您这边可以先使用空间授权，然后再使用 qshell 工具中的 batchcopy 命令将一个空间中的文件批量复制到另一个空间。这个是空间授权的操作文档：https://developer.qiniu.com/kodo/manual/3647/authorization-of-the-space这个是 qshell 的说明文档：https://developer.qiniu.com/kodo/tools/1302/qshell第一步：qshell 列举空间中文件列表 https://github.com/qiniu/qshell/blob/master/docs/listbucket.md第二步：qshell 的 batchcopy 方法把文件进行复制到新空间 https://github.com/qiniu/qshell/blob/master/docs/batchcopy.md2、您这边可以先使用空间授权，然后再使用图形化工具将一个空间中的文件批量复制到另一个空间。这个是空间授权的操作文档：https://developer.qiniu.com/kodo/manual/3647/authorization-of-the-space图形化工具文档：https://developer.qiniu.com/kodo/5972/kodo-browser 注意：使用该工具目前进行上传/下载，如果不指定cdn域名的话，下载产生的流量费用为「外网流量」B、不同账号下不同存储区域的数据迁移方式您这边可以先使用空间授权服务，把账号下A空间授权给B账号，然后开启跨区域同步功能把数据同步过去，注意勾选上需要同步历史数据。空间授权的操作文档：https://developer.qiniu.com/kodo/manual/3647/authorization-of-the-space跨区域同步参考文档：https://developer.qiniu.com/kodo/manual/1700/cross-regional-synchronization

您好会产生put/delete请求次数费用，价格参考：https://www.qiniu.com/prices/kodo[图片]

### 根本原因分析

用户操作不当或产品使用方法咨询

---

## https证书问题

**分类**：对象存储｜其他类咨询

### 问题描述

zhengsh证书修改了  为什么不生效

### 客服解答

您好这边帮您手动介入处理下 请稍等

已经处理好了

### 根本原因分析

系统自动处理流程异常，需人工介入

---

## 域名解析一直在处理中

**分类**：CDN｜配置问题

### 问题描述

域名解析一直在处理中

### 客服解答

稍等

### 根本原因分析

用户操作不当或产品使用方法咨询

---

## tech.jingyueai.com 域名证书即将过期

**分类**：CDN｜证书问题

### 问题描述

您的账号 [REDACTED_EMAIL] 在七牛云 CDN 加速平台有以下域名绑定的 SSL 证书即将过期

### 客服解答

您好，申请一个新的证书替换旧的过期证书哈如果您目前还没有新证书，建议可以使用七牛代申请证书来申请新证书配置您可以在 [域名管理] 中，点击您想要配置https的域名右侧的 [配置] 按钮，在新的页面中，在 [https配置] 下点击 [修改配置] ,点击开启->免费证书→勾选 [同意七牛云代申请免费证书] →确认，之后输入您账号的密码即可。域名管理：https://portal.qiniu.com/cdn/domain

不客气的，您这边还有其他问题吗

### 根本原因分析

证书配置/部署异常

---

## 充了1T流量还只测试了一下就欠费了，请问一下原因

**分类**：账户与财务｜计费问题

### 问题描述

充了1T流量，没正式投入使用就显示欠费了，查询一下原因

### 客服解答

您好，您可以根据账单确认 使用明细， 如果计费项 不在所购资源包抵扣范围内，会产生扣费。查看上月账单明细：您可以登录七牛云管理控制台 - 财务中心 - 账单和消费详情，点击账单编号查看详细的消费明细：https://portal.qiniu.com/financial/summary查看实时消费明细：您可以登录七牛云管理控制台 - 财务中心 - 实时消费明细：https://portal.qiniu.com/financial/estimated-consume

### 根本原因分析

用户操作不当或产品使用方法咨询

---

## 资源访问不了

**分类**：CDN｜访问下载

### 问题描述

所有资源都访问不了

### 客服解答

您好，这边看您的域名解析没有走我们这边的，域名解析是A记录的，我们的解析是cname记录的

### 根本原因分析

CNAME配置问题

---

## 域名不可访问

**分类**：CDN｜访问下载

### 问题描述

又出现不可访问的情况， 域名都不通了，啥情况啊啊！！！！，之前就出现过一次

### 客服解答

您好，您这边访问有什么报错吗？这边看是正常的1、麻烦提供下用户的 ip、dns 信息，和cdn节点信息，这边代理测试下可以通过访问这个链接 http://ping.huatuo.qq.com/*** 获取本地的 ip 和 dns 信息，在检测域名这边输入下cdn域名，点击提交检测，然后截图通过工单提交给我们[图片]2、建议让用户使用 chrome 浏览器，按照下述文档获取下 remote adress(对端节点ip)，request header(客户端请求头) 以及 response header(服务端响应头)信息，方便我们查询分析问题。https://developer.qiniu.com/fusion/kb/1478/how-to-access-network-in-the-browser-request-information

### 根本原因分析

证书格式或内容错误

---

## 历史数据批量转码

**分类**：对象存储｜其他类咨询

### 问题描述

如何处理已上传的视频。做批量视频转码

### 客服解答

您好，对现有文件转码，文件必须已经在空间中，转码未完成时，不可以删除文件，否则会导致转码失败1.转码规格参数 fops 可以替换，转码参数规格文档参考这里https://developer.qiniu.com/dora/manual/1248/audio-and-video-transcoding-avthumb实例java-sdk: https://github.com/qiniu/java-sdk/blob/master/examples/pfop_vframe.javaphp-sdk:https://github.com/qiniu/php-sdk/blob/master/examples/pfop_vframe.phppythons-sdk: https://github.com/qiniu/python-sdk/blob/master/examples/pfop_vframe.pynode-sdk: https://github.com/qiniu/nodejs-sdk/blob/master/examples/video_pfop.jsgo-sdk: https://github.com/qiniu/api.v7/blob/master/examples/video_pfop.go2.通过qshell工具进行转码qshell工具下载：https://github.com/qiniu/qshellqshell pfop命令提交转码任务：https://github.com/qiniu/qshell/blob/master/docs/pfop.mdqshell prefop命令查询转码任务：https://github.com/qiniu/qshell/blob/master/docs/prefop.md3.控制台，多媒体队列转码https://developer.qiniu.com/dora/6486/submit-transcoding-task-quicklyx

您好，现有文件无法触发触发器的功能的，触发器目前只支持新上传文件的除非您这边重新上传一遍的

您好，您这边可以看下您的任务的，找到之前触发器处理的任务打开后可以获取到之前让我触发器的任务参数的，后续操作根据这个参数来即可的

您好，您鼠标点击普通转码看下是否有命令

您好，如果这个任务就是您的任务触发器的任务的话那么这个就是您的参数命令的，转码等操作使用这个命令即可的avthumb/mp4/ss/0/t/180/vcodec/libx264/acodec/libfdk_aac

输出就是定义文件输出名称的，可以自定义输出文件名称的

您好，您参考下这个示例把 qiniutest 空间下的文件 test.avi 转码成 mp4 文件，转码后的结果保存到 qiniutest 空间中$ qshell pfop qiniutest test.avi 'avthumb/mp4'

您好，您这边是不是还没有绑定账号的，先qshell绑定账号的，看下account参数绑定账号

这边看已经完成了的Code是任务状态Desc任务信息Hash文件的hash值新生成的文件Key﻿https://developer.qiniu.com/dora/kb/3643/how-to-acquire-persistent-id

您好是这个ID的Id: z2.01z211d5d7rm218qhp00mv8cdt000wfx https://api.qiniu.com/status/get/prefop?id=z2.01z211d5d7rm218qhp00mv8cdt000wfx

您好，您可以使用下saveas参数，来指定生成后的文件名称的qshell pfop deyi video_0.9254250202054624.mp4 'avthumb/mp4/vcodec/libx264/s/480x360|saveas/base64编码后的文件名称'

### 根本原因分析

证书配置/部署异常；证书格式或内容错误

---

## 绑定了SSL证书，但是经常访问失败

**分类**：CDN｜访问下载

### 问题描述

绑定了SSL证书，但是经常访问失败

### 客服解答

您好

*.*.*.* 这个节点已经下掉了 预期是不会解析到这个节点的 您把您那边的dns刷新一下域名的证书这边看了一下是没有问题的 在有效期内

好的 您观察下

### 根本原因分析

证书格式或内容错误

---

