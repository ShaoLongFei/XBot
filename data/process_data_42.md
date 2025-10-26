# 客服支持工单数据 - Part 42

**总问题数**: 114

---

## 是否能够将历史的文件批量转移存储空间

**分类**：对象存储｜数据迁移

### 问题描述

是否能够将历史的文件批量转移存储空间

### 详细对话

**客户**：是否能够将历史的文件批量转移存储空间

**客服**：您好，目标空间与原空间的存储区域相同吗

**客户**：是相同的，想要做批量的处理

**客服**：您好，一个账号相同存储区域的数据迁移方式：方法一：您可以使用最新的图形化工具kodo-browser一键勾选文件，批量移动到另一个空间。https://***.qiniu.com/kodo/tools/5972/kodo-browser注意：该工具目前使用源站域名进行上传/下载，流量费用为「外网流量」方法二：您可以使用 qshell 工具中的 batchmove 命令将一个空间中的文件批量移动到另一个空间。这个是 qshell 的说明文档：https://***.qiniu.com/kodo/tools/1302/qshell这是 qshell 列举空间中文件列表 https://***/qiniu/qshell/blob/master/docs/listbucket.md这个是 qshell 的 batchmove 方法文档：https://***/qiniu/qshell/blob/master/docs/batchmove.md方法三：代码调用接口 move 操作，接口参考：https://***.qiniu.com/kodo/api/1288/move ，涉及到多文件操作需要进行批量处理，批量处理参考：https://***.qiniu.com/kodo/api/1250/batch相关demo如下：* java：https://***/qiniu/java-sdk/blob/master/examples/move.java ，批量调用：https://***/qiniu/java-sdk/blob/master/examples/BatchDemo.java* php：https://***/qiniu/php-sdk/blob/master/examples/rs_batch_move.php* python：https://***/qiniu/python-sdk/blob/eb23e47587dc385c478815080e8c3ea3ec99236d/examples/batch_move.py* go:https://***/qiniu/api.v7/blob/master/examples/rs_batch_move.go* nodejs: https://***/qiniu/nodejs-sdk/blob/master/examples/rs_batch_move.js

### 客服解答

您好，一个账号相同存储区域的数据迁移方式：方法一：您可以使用最新的图形化工具kodo-browser一键勾选文件，批量移动到另一个空间。https://***.qiniu.com/kodo/tools/5972/kodo-browser注意：该工具目前使用源站域名进行上传/下载，流量费用为「外网流量」方法二：您可以使用 qshell 工具中的 batchmove 命令将一个空间中的文件批量移动到另一个空间。这个是 qshell 的说明文档：https://***.qiniu.com/kodo/tools/1302/qshell这是 qshell 列举空间中文件列表 https://***/qiniu/qshell/blob/master/docs/listbucket.md这个是 qshell 的 batchmove 方法文档：https://***/qiniu/qshell/blob/master/docs/batchmove.md方法三：代码调用接口 move 操作，接口参考：https://***.qiniu.com/kodo/api/1288/move ，涉及到多文件操作需要进行批量处理，批量处理参考：https://***.qiniu.com/kodo/api/1250/batch相关demo如下：* java：https://***/qiniu/java-sdk/blob/master/examples/move.java ，批量调用：https://***/qiniu/java-sdk/blob/master/examples/BatchDemo.java* php：https://***/qiniu/php-sdk/blob/master/examples/rs_batch_move.php* python：https://***/qiniu/python-sdk/blob/eb23e47587dc385c478815080e8c3ea3ec99236d/examples/batch_move.py* go:https://***/qiniu/api.v7/blob/master/examples/rs_batch_move.go* nodejs: https://***/qiniu/nodejs-sdk/blob/master/examples/rs_batch_move.js

### 根本原因分析

需要在相同存储区域内批量迁移文件，可使用kodo-browser、qshell工具或API实现

---

## 给空间换了一个域名 目前图片打不开

**分类**：CDN｜访问下载

### 问题描述

给空间换了一个域名 目前图片打不开

### 详细对话

**客户**：给空间换了一个域名 目前图片打不开

**客服**：稍等

**客服**：您好，这边测试可以访问的，您这边页面中有什么报错吗，可以换个浏览器或网络再试试吗[图片]

**客户**：开了个无痕 现在可以访问了 谢谢

### 客服解答

您好，这边测试可以访问的，您这边页面中有什么报错吗，可以换个浏览器或网络再试试吗[图片]

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 修改回源鉴权处理中

**分类**：CDN｜配置问题

### 问题描述

修改回源鉴权处理中,处理快1个小时了

### 详细对话

**客户**：修改回源鉴权处理中,处理快1个小时了

### 客服解答

问题记录中，等待客服响应

### 根本原因分析

回源配置问题，需检查源站设置和鉴权配置

---

## 申请解除20条域名解析问题

**分类**：CDN｜访问下载

### 问题描述

我们这边要一次性解析比较多域名，所以申请技术帮我申请解析到50条，谢谢

### 详细对话

**客户**：我们这边要一次性解析比较多域名，所以申请技术帮我申请解析到50条，谢谢

**客服**：您好，您这边是说的创建域名的数量是吗？

**客户**：是的

**客服**：您好，这个目前暂时调整不了的十分抱歉的

**客户**：你们技术不是可以搞定的吗

**客服**：这个是没权限的，是那边与您说的这个可以操作的呢？

### 客服解答

这个是没权限的，是那边与您说的这个可以操作的呢？

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 如何快速删除一个空间？

**分类**：对象存储｜其他类咨询

### 问题描述

我的空间目前有52万多条文件，一次只能删除50条，有什么快递删除文件的方法？

### 详细对话

**客户**：我的空间目前有52万多条文件，一次只能删除50条，有什么快递删除文件的方法？

**客服**：您好，您可以通过qshell批量删除，三条命令就可以了。1.先下载qshell工具并使用qshell account 命令登陆账户。下载及安装文档 https://***.qiniu.com/kodo/tools/1302/qshellwindows环境下安装qshell教程 https://***.qiniu.com/kodo/kb/5545/windows-environment-installation-qshell-tutorial2.使用listbucket2命令列举出空间内所有资源例如 qshell listbucket2 空间名 -o result.txt命令文档 https://***/qiniu/qshell/blob/master/docs/listbucket2.md3.使用batchdelete命令批量删除第2步列举出的列表文件。例如 qshell batchdelete --force 空间名 -i result.txt命令文档 https://***/qiniu/qshell/blob/master/docs/batchdelete.md注意：主动删除资源不可以恢复，请慎重

**客户**：直接删除空间可以吗？还是必须先删除空间里的所有文件？

**客服**：先把文件删除完毕 才能删除空间

### 客服解答

先把文件删除完毕 才能删除空间

### 根本原因分析

空间文件数量大，需通过qshell批量删除工具提高效率

---

## 最近时间很多大陆外的IP访问不了

**分类**：CDN｜配置问题

### 问题描述

用户反馈有加拿大，港澳都无法访问。之前一直是可以的，最近不行了，请问是有什么问题吗

### 详细对话

**客户**：用户反馈有加拿大，港澳都无法访问。之前一直是可以的，最近不行了，请问是有什么问题吗

**客服**：您好，您这边需要海外访问的话需要将CDN域名的覆盖范围切换到海外或者全球的，目前覆盖范围是中国大陆，海外访问国内节点的话会超时和访问慢的，您这边可以到CDN-域名管理-域名详情下修改一下域名覆盖范围

### 客服解答

您好，您这边需要海外访问的话需要将CDN域名的覆盖范围切换到海外或者全球的，目前覆盖范围是中国大陆，海外访问国内节点的话会超时和访问慢的，您这边可以到CDN-域名管理-域名详情下修改一下域名覆盖范围

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 帮我开通一下传输加速功能

**分类**：CDN｜其他类咨询

### 问题描述

帮我开通一下对象存储的传输加速功能，谢谢

### 详细对话

**客户**：帮我开通一下对象存储的传输加速功能，谢谢

**客服**：您好，开启了传输加速，且使用加速域名访问对象存储空间产生的流量费用。例如通过加速域名向开启加速功能的存储空间中上传了 1 GB 的数据，则会产生 1 GB 传输加速费用的

**客服**：您这边确认需要开通是吗

**客户**：1G的费用多少钱

**客户**：开通吧

**客服**：每个区域价格不同，您这边可以参考下对应区域的定价https://***.qiniu.com/prices/kodo

**客户**：没问题，您开通吧

**客服**：您好，嗯嗯好的这边帮您反馈一下

**客户**：大概多久能开通

**客服**：您好，这边产品反馈已经为您开通了，您这边确认一下

**客户**：好的，谢谢

**客服**：嗯嗯不客气的

### 客服解答

嗯嗯不客气的

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 尊敬的 七牛云用户（关联账号 [REDACTED_EMAIL] ），您好:  安全中心检测到您的实例I-超级(ip:121.40.79.111)出现了Webshell安全事件(Level:serious)

**分类**：云主机｜其他类咨询

### 问题描述

尊敬的 七牛云用户（关联账号 [REDACTED_EMAIL] ），您好:
                                    安全中心检测到您的实例I-超级(ip:121.40.***.***.***)出现了Webshell安全事件(Level:serious)
                                    具体是哪块的位置呢

### 详细对话

**客户**：尊敬的 七牛云用户（关联账号 [REDACTED_EMAIL] ），您好:
                                    安全中心检测到您的实例I-超级(ip:121.40.***.***.***)出现了Webshell安全事件(Level:serious)
                                    具体是哪块的位置呢

**客服**：您好，稍等下，这边看下

**客服**：您好在您的系统磁盘上发现了一个可疑文件，建议您先确认文件合法性并进行处理。
WebShell检测是根据文件内容的威胁程度进行打分，这个文件具备了一定的危险功能，本身具有一定的危险特征，但并不完全保证一定是一个网站后门，也可能是一些包含可疑代码的正常网站文件。
处置建议
如果您确定这个文件确定为WEBSHELL，请将恶意代码注释掉。如果您确定为误报，可以在前台选择忽略、加白或者标记为误报按钮。
更多信息
备注
木马文件路径
/home/wwwroot/www.uff5.com/public/writeudid.php
文件MD5
07085ec1a04c1cfdca811509ef29f904
文件扫描方式
定时回扫
木马类型
Webshell

**客户**：好的

### 客服解答

您好在您的系统磁盘上发现了一个可疑文件，建议您先确认文件合法性并进行处理。

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 文件上传失败，报错信息为SDK中的信息，关于XMLHttpRequest

**分类**：对象存储｜上传下载

### 问题描述

文件上传时报错，是对应SDK中的报错信息，应该是：fname invalid 抛出来的错误信息，关于七牛上传的文件名有什么特殊要求吗？是否有相关的API文档介绍？

### 详细对话

**客户**：文件上传时报错，是对应SDK中的报错信息，应该是：fname invalid 抛出来的错误信息，关于七牛上传的文件名有什么特殊要求吗？是否有相关的API文档介绍？

**客服**：js上传建议您参考下我们的demo表单上传：https://***lk.qbox.me/Fhdi5OkoBEXuYUJpwfrx5SbT4WhK?attname=%E8%A1%A8%E5%8D%95upload.html简单异步上传：ttps://dn-odum9helk.qbox.me/FgU8M7WJp--x2fYwMArUAkQBXe3_?attname=%E7%AE%80%E5%8D%95%E5%BC%82%E6%AD%A5upload2.html进度条上传：https://***ug.qbox.me/FsTQJZGnTNUpTUE9tNElGpH9xlRk?attname=%E8%BF%9B%E5%BA%A6%E6%9D%A1upload3.html

**客户**：demo中有关于文件名的处理是吧？或者说调用者不需要对文件名做任何处理，哪怕上传的文件中有一些特殊字符？

**客服**：您好，如果是需要指定上传后的文件名称，需要您在上传token中，savekey参数指定https://***.qiniu.com/kodo/1206/put-policy

### 客服解答

您好，如果是需要指定上传后的文件名称，需要您在上传token中，savekey参数指定https://***.qiniu.com/kodo/1206/put-policy

### 根本原因分析

上传失败，需检查网络连接、文件大小限制或存储空间配置

---

## 之前上传过的图片找不到了

**分类**：对象存储｜上传下载

### 问题描述

2024-05-21 19:01:12 上传的图片今天访问的时候，找不到文件如何查看上传日志，以及如何查看删除日志

### 详细对话

**客户**：2024-05-21 19:01:12 上传的图片今天访问的时候，找不到文件如何查看上传日志，以及如何查看删除日志

**客服**：您好，您需要开启事件通知功能，会将上传操作，删除操作回调通知给您，后续您可以开启后记录下。事件通知：https://***.qiniu.com/kodo/8541/set-the-event-notification之前的上传，删除，需要您提供下具体的文件链接，这边尝试查询下日志。

**客户**：https://***plants.com/FkmmuvUX2vJoh8wudindCndmzi7mhttps://***plants.com/FvoaxQ2TKhbel-ZdshYILuJ51KJj这两个

**客服**：好的，这边看下

**客服**：这两个文件都是2024-10-29删除的，操作端来自47.100.12.244

**客户**：还能找回吗  咱们这边有备份吗

**客服**：您好，对象存储的文件删除后无法找回的，我们这没有备份，如果您那边本地有备份可以重新上传下。

**客户**：好的 谢谢

**客服**：不客气的~

**客户**：请问，平台这边是否有什么方案，可以防止我们误删除。哪怕是删除图片后，也能通过什么渠道，将图片找回，并重新下载

**客服**：稍等

**客服**：您好，1、支持设置对象锁定功能，限制文件删除：https://***.qiniu.com/kodo/8545/set-the-object-lock仅对开启对象锁定后新上传的文件生效，请知悉2、只能你们在本地或者其他地方再备份一份数据，七牛这边删除了，再从备份重新上传下。

### 客服解答

您好，1、支持设置对象锁定功能，限制文件删除：https://***.qiniu.com/kodo/8545/set-the-object-lock仅对开启对象锁定后新上传的文件生效，请知悉2、只能你们在本地或者其他地方再备份一份数据，七牛这边删除了，再从备份重新上传下。

### 根本原因分析

空间文件数量大，需通过qshell批量删除工具提高效率

---

## 为什么图片删除了还能访问呢

**分类**：CDN｜访问下载

### 问题描述

为什么图片删除了还能访问呢：https://***mcloud.com/18d159cafcecfa588e591af5cc735aa7.png

### 详细对话

**客户**：为什么图片删除了还能访问呢：https://***mcloud.com/18d159cafcecfa588e591af5cc735aa7.png

**客服**：您好文件删除后，由于存在 CDN 缓存，会导致您还可以访问已经删除的文件，您可以先清除下 CDN 缓存，然后清除本地浏览器缓存进行访问1、CDN 刷新缓存方法请参考：https://***.qiniu.com/fusion/kb/1325/refresh-the-cache-and-the-effect-of-time方法1: portal.qiniu.com 控制台刷新缓存，点击左侧融合cdn => 刷新预取方法2: api 接口地址：https://***.qiniu.com/fusion/api/1229/cache-refreshTip : url 刷新，全网生效 10min 左右，目录刷新需要 30min 左右2、清除本地缓存方法添加随机参数进行访问 或者 禁用浏览器缓存[图片]

### 客服解答

您好文件删除后，由于存在 CDN 缓存，会导致您还可以访问已经删除的文件，您可以先清除下 CDN 缓存，然后清除本地浏览器缓存进行访问1、CDN 刷新缓存方法请参考：https://***.qiniu.com/fusion/kb/1325/refresh-the-cache-and-the-effect-of-time方法1: portal.qiniu.com 控制台刷新缓存，点击左侧融合cdn => 刷新预取方法2: api 接口地址：https://***.qiniu.com/fusion/api/1229/cache-refreshTip : url 刷新，全网生效 10min 左右，目录刷新需要 30min 左右2、清除本地缓存方法添加随机参数进行访问 或者 禁用浏览器缓存[图片]

### 根本原因分析

CDN缓存配置问题，需清理缓存或调整缓存策略

---

## 我需要开专票，一直驳回我的开票信息

**分类**：账户与财务｜发票问题

### 问题描述

我要怎么搞

### 详细对话

**客户**：[图片]我要怎么搞

**客服**：您好这边反馈下 请稍等

**客服**：附件里放的不是一般纳税人证明，「纳税人资质证明」您可以提供一般纳税人税务事项通知书。盖有「增值税一般纳税人」章的税务登记证副本复印件。若以上两项均无法提供，请登录各地区的国税网，查询一般纳税人资格，将此资格截图打印并加盖公司公章。「国家税务总局」https://***tax.gov.cn/

**客服**：您好纳税人资质再次提交审核一下「纳税人资质证明」您可以提供一般纳税人税务事项通知书。盖有「增值税一般纳税人」章的税务登记证副本复印件。若以上两项均无法提供，请登录各地区的国税网，查询一般纳税人资格，将此资格截图打印并加盖公司公章。「国家税务总局」https://***tax.gov.cn/

**客户**：我们没有

**客服**：专票是需要提交一般纳税人资质证明的

### 客服解答

专票是需要提交一般纳税人资质证明的

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 27ip,cn的ssl 一直配置中 麻烦处理一下

**分类**：对象存储｜其他类咨询

### 问题描述

27ip,cn的ssl 一直配置中 麻烦处理一下

### 详细对话

**客户**：27ip,cn的ssl 一直配置中 麻烦处理一下

**客服**：稍等

**客户**：大概要多久

**客服**：您好，配置已下发了哈

### 客服解答

您好，配置已下发了哈

### 根本原因分析

配置相关问题，需要调整或优化系统配置

---

## 这个资源为什么访问不了呢

**分类**：对象存储｜上传下载

### 问题描述

https://***nginfo.com/Uploads/Editor/2023-11-06/6548636a82478.jpg这个资源为什么访问不了呢； 链接没有问题啊

### 详细对话

**客户**：https://***nginfo.com/Uploads/Editor/2023-11-06/6548636a82478.jpg这个资源为什么访问不了呢； 链接没有问题啊

### 客服解答

问题记录中，等待客服响应

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 我需要一个模糊查询文件列表的接口

**分类**：对象存储｜SDK使用

### 问题描述

现在没有这个接口 或找到的接口一直报错

### 详细对话

**客户**：现在没有这个接口 或找到的接口一直报错

**客服**：您好参考 https://***/qiniu/java-sdk/blob/master/examples/ListDemo.java 列举即可

**客户**：只能通过前缀吗  有没有别的方案

**客服**：抱歉没有其他方式

**客户**：那这个前缀前面有个文件夹的话 怎么做处理呢

**客服**：您好，文件夹的本质是基于文件名 里面的 / 虚拟出来的 ，你们把全名称的前缀带上即可

**客户**：//要列举文件的空间名        String bucket = "yourbucket";        try {            //调用listFiles方法列举指定空间的指定文件            //参数一：bucket    空间名            //参数二：prefix    文件名前缀            //参数三：marker    上一次获取文件列表时返回的 marker            //参数四：limit     每次迭代的长度限制，最大1000，推荐值 100            //参数五：delimiter 指定目录分隔符，列出所有公共前缀（模拟列出目录效果）。缺省值为空字符串            FileListing fileListing = bucketManager.listFiles(bucket, null, null, 10, null);  如果我的前缀是yandex 您看看我放到哪里

**客服**：你们现在具体是要查那种前缀的文件，给个对应详细案列的文件URL外链，这边告诉你们前缀怎么设置才可以

**客服**：就是你们预期想通过________ , 查找到文件_______________ ,这个文件的外链是_____________________

**客户**：我们预期想通过前缀对的方式找到文件  我的bucket叫filepage，我想模糊查询filepage中yandex/132132.html   中间有一个文件夹yandex的文件夹

**客服**：您好，这个 yandex/132132.html  文件的完整外链麻烦复制出来提供下 ，如果外链就是 https://***/yandex/132132.html  前缀可以是 yan
yand
yandex
yandex/
yandex/132
等等，只要从前往后的，都是叫做前缀，获取到了文件列表后再过滤 FileListing fileListing = bucketManager.listFiles(bucket, "yandex/", null, 10, null);

**客户**：好的 谢谢

### 客服解答

您好，这个 yandex/132132.html  文件的完整外链麻烦复制出来提供下 ，如果外链就是 https://***/yandex/132132.html  前缀可以是 yan

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 小文件可以上传，大文件上传会报错

**分类**：对象存储｜上传下载

### 问题描述

网站使用了七牛云插件作为文件存储，上传图片或者较小的视频（测试过70m的视频）时可以上传到存储空间，但是上传几百兆的文件时会报错，是超时报错。

### 详细对话

**客户**：网站使用了七牛云插件作为文件存储，上传图片或者较小的视频（测试过70m的视频）时可以上传到存储空间，但是上传几百兆的文件时会报错，是超时报错。

**客服**：您好，您这边是使用的什么上传方式呢？是客户端上传还是服务端上传呢？

**客户**：客户端，我在服务器上搭建了一个网站，网站架构是ThinkCMF，使用了七牛云插件。[图片][图片]

**客服**：上传是走的服务端还是客户端的

**客服**：这个插件您需要咨询一下作者是否可以修改一下超时配置的，或者就是提升一下您的上传端的带宽的

**客户**：我不太了解，上传走的是哪边，有什么可以判断的依据吗

**客服**：您上传的插件是搭建在服务器上使用的还是本地客户端上使用的

**客户**：服务器上

**客户**：我想知道配置好七牛云存储后，上传的文件是怎么存到你们的存储空间的，这个流程是什么

**客服**：您好，通过上传接口上传的，您这边使用的插件，具体插件如何实现的上传您这边可以咨询一下插件开发团队的，看下插件团队是如何使用的我们这边的接口的可以参考下这个上传资源的文档的https://***.qiniu.com/kodo/1234/upload-types

**客户**：在哪能看到上传文件的日志

**客服**：您好，可以到我们的对象存储空间找到空间后打开空间设置的空间日志，开启后会保留的，没开启的话暂时是没有的

**客户**：七牛云有限制最大可上传的文件大小吗

**客服**：您好，我们这边是没有限制的，您上传是走的插件，您这边的话需要咨询一下插件开发团队这边是否有做限制的

**客服**：您好，第三方插件七牛这边提供的帮助有限；例如 wp插件和dz论坛等是第三方开发和维护的，使用过程中遇到的问题，建议向插件开发团队咨询。很多应用都是七牛的用户，或者使用了七牛的存储，加速，数据处理服务。他们有的自己调用七牛的接口，有的在工具包里放入七牛的sdk，根据自己的业务需求进行改写，开发，以实现各种功能。为方便用户间交流学习，七牛提供了此类工具，插件的共享平台，用户可自行上传下载：https://***.qiniu.com/download/index.html （社区插件/工具）使用过程中遇到的问题，建议向对应的开发团队咨询。

### 客服解答

您好，第三方插件七牛这边提供的帮助有限；例如 wp插件和dz论坛等是第三方开发和维护的，使用过程中遇到的问题，建议向插件开发团队咨询。很多应用都是七牛的用户，或者使用了七牛的存储，加速，数据处理服务。他们有的自己调用七牛的接口，有的在工具包里放入七牛的sdk，根据自己的业务需求进行改写，开发，以实现各种功能。为方便用户间交流学习，七牛提供了此类工具，插件的共享平台，用户可自行上传下载：https://***.qiniu.com/download/index.html （社区插件/工具）使用过程中遇到的问题，建议向对应的开发团队咨询。

### 根本原因分析

上传失败，需检查网络连接、文件大小限制或存储空间配置

---

## 七牛低延时直播

**分类**：直播云｜其他类咨询

### 问题描述

七牛低延时直播接入测试申请

### 详细对话

**客户**：七牛低延时直播接入测试申请

**客服**：您好可以使用 https://***.qiniu.com/pili/7741/low-latency-live-sdk-download-experience 的demo

### 客服解答

您好可以使用 https://***.qiniu.com/pili/7741/low-latency-live-sdk-download-experience 的demo

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 域名升级 HTTPS 处理中

**分类**：CDN｜配置问题

### 问题描述

修改cdn配置，域名升级 HTTPS 处理中一直不动

### 详细对话

**客户**：修改cdn配置，域名升级 HTTPS 处理中一直不动

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

**客户**：好的，谢谢

**客服**：嗯嗯好的不客气的

### 客服解答

嗯嗯好的不客气的

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 如何选

**分类**：CDN｜流量计费问题

### 问题描述

我配置https  域名走CDN  需要购买哪些类型的流量包   哪些CDN项目10G内免费  请告知下。

### 详细对话

**客户**：我配置https  域名走CDN  需要购买哪些类型的流量包   哪些CDN项目10G内免费  请告知下。

**客服**：您好，http协议才能使用免费10GB的免费流量的，资源包的话可以购买CDN中国大陆流量包即可的

**客户**：https  有哪些免费的流量包  存储和请求   CDN下行通用流量 是https 的Cdn流量 还是需要单独购买

**客户**：我的意思的 一个完整的存储 使用https 和CDN 需要购买哪些流量包   存储 请求数  cdn下行流量 还需购买什么包

**客服**：您好，免费额度须知：https://***.qiniu.com/af/kb/1574/free-credit-information可以留一下您的联系方式，这边商务同事和您对接下，为您评估资源包购买方案。

**客服**：对象存储计量与计费项：https://***.qiniu.com/kodo/6379/metering-and-billingCDN就只有cdn下行流量。

**客户**：如果只购买cdn下行流量包  https 还需单独购买吗  还是https 已经包括在 cdn下行流量包内了。

**客服**：您好，不需要的，cdn下行流量是通用资源包，能抵扣https的流量

**客户**：好的， 再问一下 PUT/DELETE 请求包 有单独购买的链接吗

**客服**：没有的，PUT/DELETE 是按量计费的。

**客户**：好的  结束工单吧

### 客服解答

没有的，PUT/DELETE 是按量计费的。

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 域名状态显示已停用

**分类**：对象存储｜其他类咨询

### 问题描述

域名状态显示已停用 小程序视频不能播放

### 详细对话

**客户**：域名状态显示已停用 小程序视频不能播放

**客服**：您好，需要使用的话，启用域名就好

### 客服解答

您好，需要使用的话，启用域名就好

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 已经对公充值成功，帐户中一直未体现。帐户随时有可能变成负的影响使用。

**分类**：账户与财务｜其他类咨询

### 问题描述

[REDACTED_EMAIL]

### 详细对话

**客户**：[REDACTED_EMAIL]

**客服**：您好，对公打款吗，可以提供下银行回执，这边同步为您加急处理下

**客户**：业务 类型:网银互联借记付款人名称:喆企网络科技(上海)有限公司付款人账号:50131****95396719付款行名称:上海农商银行收款人名称:上海七牛信息技术有限公司收款人账号:98120154****08821收款行名称:上海浦东发展银行小写 金额:CNY2,000.00大写 金额:人民币贰仟元整备注:充值账户:[REDACTED_EMAIL][图片]

**客服**：您好，稍等下，这边为您同步加急下

**客户**：为什么还未到帐呢

**客服**：这边帮您加急反馈

**客服**：这边帮您加急反馈内部处理打款

**客服**：您好，您的充值已经到账

### 客服解答

您好，您的充值已经到账

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 协助调查

**分类**：对象存储｜上传下载

### 问题描述

我单位存储空间因欠费导致空间被清除，请帮忙排查我单位原空间名称以便我单位重新配置，减少开发工作谢谢

### 详细对话

**客户**：我单位存储空间因欠费导致空间被清除，请帮忙排查我单位原空间名称以便我单位重新配置，减少开发工作谢谢

**客服**：稍等

**客服**：nxdzlog
nxvideo
gygqt
gyhnapp-shop
nxhcnykj
ptjyjy
wtskjcms
gysites-cms
gyzscms
wswgwsite
gyhncms
nxwtscms
nxwmdtcms
kcrhptj-cms
jcyappvideo
partybuild
ycctcms
nxgg
akncms
gywmwcms
gyfbapp
gywapplication
gywapp
mhxgg
szscms
bdgycms
gyzxqy

**客户**：这些按顺序都创建一级目录是吧吗

**客服**：您好，这些是存储空间名称，具体空间内部存储的目录查看不到了。

**客户**：好的谢谢

**客服**：您好，不客气的

**客户**：您好，我已配置空间文件为公有，且文件已经上传成功，但仍然访问不到我的文件

**客服**：文件链接能发一下吗

**客户**：https://***azy910.com/20241030195543_997.jpg

**客户**：域名也已配置，状态为处理中

**客服**：稍等

**客服**：https://***azy910.com/20241030195543_997.jpg用 http 协议访问看下呢

**客户**：可以访问到

**客服**：目前域名没有证书，只能 http 访问，您看下呢

**客户**：那我可以绑定一个https协议的吗

**客服**：有证书就可以

**客户**：www.gysites.qiniu.lazy910.com 这个域名也是我们这边自己买的是吗

**客服**：您好，手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://***.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://***.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide4.升级HTTPS配置https://***.qiniu.com/fusion/manual/4952/https-configuration注意事项升级https后，流量计费说明：https://***.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq

### 客服解答

您好，手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://***.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://***.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide4.升级HTTPS配置https://***.qiniu.com/fusion/manual/4952/https-configuration注意事项升级https后，流量计费说明：https://***.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq

### 根本原因分析

需要配置合适的上传策略和工具

---

## 为什么七牛云云开了证书，小程序的那边无法显示

**分类**：对象存储｜其他类咨询

### 问题描述

为什么七牛云云开了证书，小程序的那边无法显示，商品都显示，就是这个地方不显示，（必须开了  不验证域名合法性及https证书验证才会显示出来），正常就不显示，这个是啥问题！！如图。这个是正常时候，不开的话 就不如果开了。就显示这个是图片路径 （我已经强制开了https）https://***uaye818.cn/uploads/mall11/20241027/874692e0c25b63d90fcedce4236f4e87.png

### 详细对话

**客户**：为什么七牛云云开了证书，小程序的那边无法显示，商品都显示，就是这个地方不显示，（必须开了  不验证域名合法性及https证书验证才会显示出来），正常就不显示，这个是啥问题！！如图。这个是正常时候，不开的话 就不[图片]如果开了。就显示[图片]这个是图片路径 （我已经强制开了https）https://***uaye818.cn/uploads/mall11/20241027/874692e0c25b63d90fcedce4236f4e87.png

**客户**：我本地存储的图片 没有问题 是可以正常显示的 就七牛云的不显示

**客服**：稍等

**客服**：解析冲突，把主机记录ds 记录值是	iovip-z0.qbox.me的记录，删除或停用下，解析生效需要10分钟左右时间，之后再观察下

### 客服解答

解析冲突，把主机记录ds 记录值是	iovip-z0.qbox.me的记录，删除或停用下，解析生效需要10分钟左右时间，之后再观察下

### 根本原因分析

空间文件数量大，需通过qshell批量删除工具提高效率

---

## 感觉流量有问题，总共才450多M，这个月怎么 75.10 GB空间流出流量？

**分类**：对象存储｜其他类咨询

### 问题描述

感觉流量有问题，总共才450多M，这个月怎么 75.10 GB空间流出流量？能帮忙看看吗？

### 详细对话

**客户**：感觉流量有问题，总共才450多M，这个月怎么 75.10 GB空间流出流量？能帮忙看看吗？

**客服**：您这个数据是在哪看的，能方便截图给我们看下吗

**客户**：对象存储概览[图片]

**客服**：您是不是绑定了自定义源站域名去访问资源了

**客服**：sqllab_untitled_query_1_20241030T112717.csv这边帮您查了一下您的 weapp-ngclub-cn 空间的 top 100 ip 访问情况，时间是昨天，您看下呢

**客户**：对的，我用的自定义源站域名访问资源。这个不好吗？推荐其他的呢？

**客服**：您好，可以使用cdn支持更多防盗链配置

**客服**：您好，CDN上支持多种防盗链配置，不同的防盗链适用于不同的应用场景，建议可以在 融合cdn => 域名管理 => 配置 => 访问控制 中设置1：referer防盗链： 只有携带了相应referer 请求头 的 http请求才能访问资源，但是对于技术来说，referer都是可以伪造的，存在一定的风险2：时间戳防盗链，url带着e和token参数访问，e为过期时间，但是只要捕获到了url就可以访问资源了，只适用于访问xx次的场景3：回源鉴权，这个你们可以尝试下，每次访问cdn图片时，会携带你们自己定义的访问参数去你们自己的服务器上鉴权，只有你们服务器鉴权通过，返回 httpcode=200 ，才会将图片资源给用户访问，否则无法返回图片4：IP黑白名单，这个适合某一个网段内的ip访问资源，不适合官网使用，只有在 ip 白名单中的用户才可以访问你们的图片参考文档：https://***.qiniu.com/fusion/4960/access-control-configuration☆推荐使用第三种回源鉴权和第四种IP黑白名单进行访问限制。

### 客服解答

您好，CDN上支持多种防盗链配置，不同的防盗链适用于不同的应用场景，建议可以在 融合cdn => 域名管理 => 配置 => 访问控制 中设置1：referer防盗链： 只有携带了相应referer 请求头 的 http请求才能访问资源，但是对于技术来说，referer都是可以伪造的，存在一定的风险2：时间戳防盗链，url带着e和token参数访问，e为过期时间，但是只要捕获到了url就可以访问资源了，只适用于访问xx次的场景3：回源鉴权，这个你们可以尝试下，每次访问cdn图片时，会携带你们自己定义的访问参数去你们自己的服务器上鉴权，只有你们服务器鉴权通过，返回 httpcode=200 ，才会将图片资源给用户访问，否则无法返回图片4：IP黑白名单，这个适合某一个网段内的ip访问资源，不适合官网使用，只有在 ip 白名单中的用户才可以访问你们的图片参考文档：https://***.qiniu.com/fusion/4960/access-control-configuration☆推荐使用第三种回源鉴权和第四种IP黑白名单进行访问限制。

### 根本原因分析

配置相关问题，需要调整或优化系统配置

---

## 手机号不适用 ，更换手机号

**分类**：账户与财务｜账户问题

### 问题描述

[REDACTED_PHONE]更换成[REDACTED_PHONE]

### 详细对话

**客户**：[REDACTED_PHONE]更换成[REDACTED_PHONE]

**客服**：您好，修改手机号有如下三种方式，如果您的手机无法接受验证码可以使用方法二和方法三进行申请修改手机号：方法一：点击官网右上角的管理控制台——个人面板——个人中心的安全设置更改手机，发送手机验证码，验证之后就可以对手机号进行修改。[图片]方法二：点击官网右上角的管理控制台——个人面板——个人中心的安全设置更改手机，选择邮箱验证码，验证之后就可以对手机号进行修改。[图片]方法三：通过人工申诉提供相关资料进行修改，将材料发送邮件到 [REDACTED_EMAIL] ，需要提供的信息如下：a、个人实名认证：请提供注册邮箱、修改原因、手持与实名认证一致的身份证正面图片、新手机号码；b、企业实名认证：请提供注册邮箱、修改原因、实名认证的营业执照图片、申请人手持正面身份证图片、新手机号码。（注意：为了您的账号信息安全，修改手机号时需要您提供相关信息，这边为您审核处理，感谢您的理解与配合～）邮件发送后请工单上告知我们。我们后台操作完毕后，重新登录系统会提示您短信验证新的手机号，验证完毕后手机号即修改完成。

### 客服解答

您好，修改手机号有如下三种方式，如果您的手机无法接受验证码可以使用方法二和方法三进行申请修改手机号：方法一：点击官网右上角的管理控制台——个人面板——个人中心的安全设置更改手机，发送手机验证码，验证之后就可以对手机号进行修改。[图片]方法二：点击官网右上角的管理控制台——个人面板——个人中心的安全设置更改手机，选择邮箱验证码，验证之后就可以对手机号进行修改。[图片]方法三：通过人工申诉提供相关资料进行修改，将材料发送邮件到 [REDACTED_EMAIL] ，需要提供的信息如下：a、个人实名认证：请提供注册邮箱、修改原因、手持与实名认证一致的身份证正面图片、新手机号码；b、企业实名认证：请提供注册邮箱、修改原因、实名认证的营业执照图片、申请人手持正面身份证图片、新手机号码。（注意：为了您的账号信息安全，修改手机号时需要您提供相关信息，这边为您审核处理，感谢您的理解与配合～）邮件发送后请工单上告知我们。我们后台操作完毕后，重新登录系统会提示您短信验证新的手机号，验证完毕后手机号即修改完成。

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## ssl免费证书上传报错

**分类**：对象存储｜其他类咨询

### 问题描述

[    [        {            "title": "请求 ID",            "content": "CGDCDBDvhxJQOAMY"        },        {            "title": "日志栈",            "content": "fusionicp:2;fusionsslcert:30/400"        }    ]]

### 详细对话

**客户**：[    [        {            "title": "请求 ID",            "content": "CGDCDBDvhxJQOAMY"        },        {            "title": "日志栈",            "content": "fusionicp:2;fusionsslcert:30/400"        }    ]]

**客服**：这个报错的界面麻烦截图给看下呢

**客户**：上传了nginx的crt和pem格式证书，证书时从腾讯申请的免费证书。我核对了下8月2日上传的证书，是crt和key格式[图片][图片]

**客服**：您在证书厂商下载证书时，选择 Nginx 服务器类型的证书文件进入七牛云管理控制台：https://***.qiniu.com/certificate/ssl，点击 【上传自有证书】使用编辑器打开后续文件，并复制 .crt 或者 .pem 后缀的文件内容到证书内容 （公钥），复制 .key 后缀结尾的内容到 证书私钥 。[图片]如果需要把域名升级为 HTTPS 或者修改证书 的话，需要按照以下步骤绑定证书即可：https://***.qiniu.com/fusion/manual/4952/https-configuration

**客服**：是这种形式上传的自有证书吗

**客户**：已解决，感谢

**客服**：您客气了

### 客服解答

您客气了

### 根本原因分析

上传失败，需检查网络连接、文件大小限制或存储空间配置

---

## 下行流量包用得过快

**分类**：对象存储｜上传下载

### 问题描述

下行流量包用得过快帮忙查一下有没有什么异常

### 详细对话

**客户**：下行流量包用得过快帮忙查一下有没有什么异常

**客服**：是 cdn 流量包使用过快吗？

**客户**：是的

**客服**：稍等

**客服**：您可以在 控制台 - cdn - 统计分析 - 日志分析 中看到您的top访问情况，比如高频访问的URL和客户端IP。https://***.qiniu.com/cdn/statistics/log/top如有部分IP请求数/请求流量异常，不符合您的业务预期，您可以在域名管理 - 访问控制 中，开启IP黑白名单，对这部分IP进行封禁。[图片]

**客服**：您按照这个看下是不是有异常访问的ip呢，然后封禁掉

### 客服解答

您按照这个看下是不是有异常访问的ip呢，然后封禁掉

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 域名无法使用cdn 无法使用

**分类**：对象存储｜其他类咨询

### 问题描述

域名和cdn 都无法使用

### 详细对话

**客户**：域名和cdn 都无法使用

**客服**：有无法访问的资源链接吗？

**客户**：我是无法绑定cdn

**客户**：我域名cname 解析成功了，但是开启cdn 无法使用提示要开启cname

**客户**：而且我买了cdn 流量包

**客户**：oss.zbjls.com

**客户**：iovip-z2.qiniuio.com

**客服**：https://***.qiniu.com/prices/kodo

### 客服解答

https://***.qiniu.com/prices/kodo

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 需要下载工具

**分类**：对象存储｜工具使用

### 问题描述

下载过程容易中断，需要批量下载工具，进行数据备份

### 详细对话

**客户**：下载过程容易中断，需要批量下载工具，进行数据备份

**客服**：您好您可以使用最新的图形化工具kodo-browser上传/下载试下，支持批量管理。https://***.qiniu.com/kodo/tools/5972/kodo-browser注意：使用该工具目前进行上传/下载，如果不指定cdn域名的话，下载产生的流量费用为「外网流量」

### 客服解答

您好您可以使用最新的图形化工具kodo-browser上传/下载试下，支持批量管理。https://***.qiniu.com/kodo/tools/5972/kodo-browser注意：使用该工具目前进行上传/下载，如果不指定cdn域名的话，下载产生的流量费用为「外网流量」

### 根本原因分析

需要配置合适的上传策略和工具

---

## 限制图片大小功能如何使用

**分类**：对象存储｜其他类咨询

### 问题描述

https://***zoupai.com/109/z2u/2024_10_28/H22/IMG_3884.JPG?e=1730292480&token=QQNMAlmMYfLNU234-gCKKG8a8Z16F9HQrB0nrcTq ***:3ZM-9ISQkd4Tb24s2dcx5GGy6rA=这样形式的图片文件 如何使用 限制图片大小功能  怎么拼接后面的参数？

### 详细对话

**客户**：https://***zoupai.com/109/z2u/2024_10_28/H22/IMG_3884.JPG?e=1730292480&token=QQNMAlmMYfLNU234-gCKKG8a8Z16F9HQrB0nrcTq ***:3ZM-9ISQkd4Tb24s2dcx5GGy6rA=这样形式的图片文件 如何使用 限制图片大小功能  怎么拼接后面的参数？

**客服**：限制图片大小功能，是指 智能多媒体产品吗？

**客服**：如果是 只能多媒体的同步命令处理形式为 https://***zoupai.com/109/z2u/2024_10_28/H22/IMG_3884.JPG?fopsfops 就是执行的命令，然后用这个带有 fops 命令的 url 链接去鉴权私有链接即可

**客户**：https://***zoupai.com/109/z2u/2024_10_28/H22/IMG_3891.JPG?imageMogr2/format/jpeg/strip/size-limit/2m&e=1730326791&token=QQNMAlmMYfLNU234-gCKKG8a8Z16F9HQrB0nrcTq ***:pEdQR3UNuc6gxnAo912ncRptqzw=https://***zoupai.com/109/z2u/2024_10_28/H22/IMG_3891.JPG/imageMogr2/format/jpeg/strip/size-limit/2m?e=1730326791&token=QQNMAlmMYfLNU234-gCKKG8a8Z16F9HQrB0nrcTq ***:pEdQR3UNuc6gxnAo912ncRptqzw=对 是智能多媒体服务 但是私有链接怎么拼接这个参数   我看上面这两种形式都是会返回401

**客服**：当您将空间设置成私有时，必须获得授权，才能对空间内的资源进行访问。私有资源下载是通过HTTP GET的方式访问特定的 URL。私有资源URL与公开资源URL相比只是增加了两个参数e和token，分别表示过期时间和下载凭证。一个完整的私有资源 URL 如下所示：https://***/<key>?e=<deadline>&token=<downloadToken>
参数e表示 URL 的过期时间，采用Unix时间戳，单位为秒。超时的访问将返回 401 错误。参数token表示下载凭证。下载凭证是对资源访问的授权，不带下载凭证或下载凭证不合法都会导致 401 错误，表示验证失败。注意：如果请求方的时钟未校准，可能会造成有效期验证不正常，例如直接认为已过期。因此需要进行时钟校准。由于开发者无法保证客户端的时间都校准，所以应该在业务服务器上创建时间戳，并周期性校准业务服务器时钟。文档链接：https://***.qiniu.com/kodo/1656/download-private

**客户**：是的  所以如何在私有文件下载添加了 e 和 token *** 添加限制文件大小这个参数呢

**客服**：例如：直接对https://***zoupai.com/109/z2u/2024_10_28/H22/IMG_3891.JPG/imageMogr2/format/jpeg/strip/size-limit/2m 这个链接做私有化授权签算处理

**客户**：就是我先鉴权再添加 imageMogr2 这些处理参数就不行了是吗

**客服**：不行的 授权是对整个链接处理的 在程序侧实现

**客户**：ok

**客服**：好的

### 客服解答

好的

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## cdn 加速资源包退款

**分类**：对象存储｜其他类咨询

### 问题描述

订单号：dc1a99a7f686d0509bd35ca7dc6160a8

### 详细对话

**客户**：订单号：dc1a99a7f686d0509bd35ca7dc6160a8

**客服**：您联系方式也留一下，商务专员最迟明天为您操作退款申请

**客户**：明天，直接这里回复我，给我个电话我给你们打电话

**客服**：好的

**客服**：您好，这边已经反馈为您申请了，还请耐心等待审批通过后即可退回的

### 客服解答

您好，这边已经反馈为您申请了，还请耐心等待审批通过后即可退回的

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 七牛云的播放SDK

**分类**：直播云｜其他类咨询

### 问题描述

https://***.qiniu.com/qvs/7924/play-the-sdk七牛云的播放SDK  有DEMO，这样可以看一效果

### 详细对话

**客户**：https://***.qiniu.com/qvs/7924/play-the-sdk七牛云的播放SDK  有DEMO，这样可以看一效果

**客服**：是qplayer播放器还是什么

**客户**：QPlayer2 与PLDroidPlayer 有什么区别？

**客户**：？

**客服**：稍等

**客服**：这边反馈内部确认下

**客服**：您好，这两个播放器是服务不同产品的，您如果是直播服务就选择 qplayer2 呢，视频监控就选择另一个

**客户**：下面 LiveRoomActivity、RoomActivity 代码，之前主播在线，观众是可以听到声音的，  现在提示： 播放器打开失败，请确认是否在推流！ 代码没有变化，一时看不出问题在哪里，麻烦帮忙看下， LiveRoomActivity、RoomActivity 代码如下：package sas.hhsk.live.qiniu.activity;import android.annotation.SuppressLint;import android.app.AlertDialog;import android.content.Context;import android.content.DialogInterface;import android.content.Intent;import android.content.pm.PackageManager;import android.graphics.Color;import android.os.Build;import android.os.Bundle;import android.os.Handler;import android.os.Message;import android.os.SystemClock;import android.util.Log;import android.view.View;import android.view.Window;import android.view.WindowManager;import android.widget.Chronometer;import android.widget.ImageButton;import android.widget.ImageView;import android.widget.LinearLayout;import android.widget.TextView;import android.widget.Toast;import androidx.annotation.NonNull;import androidx.fragment.app.FragmentActivity;import androidx.fragment.app.FragmentManager;import androidx.fragment.app.FragmentTransaction;import com.alibaba.fastjson.JSON;import com.alibaba.fastjson.JSONObject;import com.pili.pldroid.player.PLOnErrorListener;import com.pili.pldroid.player.PLOnInfoListener;import com.pili.pldroid.player.widget.PLVideoView;import org.apache.commons.lang3.StringUtils;import java.util.List;import sas.hhsk.live.R;import sas.hhsk.live.biz.OnlineRecordBiz;import sas.hhsk.live.common.MyApplication;import sas.hhsk.live.domain.Member;import sas.hhsk.live.domain.Room;import sas.hhsk.live.fragment.LiveFragment;import sas.hhsk.live.fragment.MqttFragment;import sas.hhsk.live.helper.BizHelper;import sas.hhsk.live.helper.OnlineRecordHelper;import sas.hhsk.live.helper.PushPlayerHelper;import sas.hhsk.live.helper.RoomInfoHelper;import sas.hhsk.live.helper.SysParamHelper;import sas.hhsk.live.helper.TimerTaskHelper;import sas.hhsk.live.helper.UserInfoHelper;import sas.hhsk.live.net.NormalCommonCallback;import sas.hhsk.live.qiniu.helper.EnterRTCRoomHelper;import sas.hhsk.live.qiniu.net.QiniuBiz;import sas.hhsk.live.util.UIUtils;import static sas.hhsk.live.qiniu.utils.Utils.getSystemUiVisibility;public class LiveRoomActivity extends FragmentActivity {    private static final String TAG = MyApplication.LOG_PREFIX + LiveRoomActivity.class.getSimpleName();    public static final String EXTRA_ROOM_ID = "ROOM_ID";    //    private static final String BASE_URL = "rtmp://pili-rtmp.qnsdk.com/sdk-live/";    private static final String BASE_URL = "rtmp://pili-live-rtmp.ldcloud100.com/dzzg/test/"; //TODO 客户化代码, 换成自己的推流地址    private static final String[] MANDATORY_PERMISSIONS = {            "android.permission.MODIFY_AUDIO_SETTINGS",            "android.permission.RECORD_AUDIO",            "android.permission.INTERNET",            "android.permission.CAMERA"    };    private PLVideoView mVideoView;    private LinearLayout mLogView;    private TextView mAudioBitrateText;    private TextView mAudioFpsText;    private TextView mVideoBitrateText;    private TextView mVideoFpsText;    private TextView mPlayUrlText;    private TextView tvSsStaus; //显示上师是否在线    private Toast mLogToast;    //    private ImageButton mToggleMuteButton;    private ImageButton mDisconnectButton;    private ImageView tishiImageView,mToggleMuteButton;    private TextView tishiTextView,onlineCountTextView;    private Chronometer mTimer;    private TimerTaskHelper timerTaskHelper;    private OnlineRecordBiz onlineRecordBiz;    private boolean countOnlineFlag = true;    Member member;    Room room;    private boolean isPlay = false;    private String mRtmpUrl = "";    private String liveStatus = "";    private static final String ssks = "ssks";    @Override    protected void onCreate(Bundle savedInstanceState) {        super.onCreate(savedInstanceState);        requestWindowFeature(Window.FEATURE_NO_TITLE);        getWindow().addFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN | WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON                | WindowManager.LayoutParams.FLAG_DISMISS_KEYGUARD | WindowManager.LayoutParams.FLAG_SHOW_WHEN_LOCKED                | WindowManager.LayoutParams.FLAG_TURN_SCREEN_ON);        getWindow().getDecorView().setSystemUiVisibility(getSystemUiVisibility());        setContentView(R.layout.activity_live_room);        Intent intent = getIntent();        mRtmpUrl = BASE_URL + intent.getStringExtra(EXTRA_ROOM_ID);        String roomString = intent.getStringExtra("room");        room = JSON.parseObject(roomString, Room.class);        member = UserInfoHelper.readUser(this);        mTimer = findViewById(R.id.timer);        mLogView =  findViewById(R.id.log_text);        ImageButton mLogButton =  findViewById(R.id.log_shown_button);        mLogButton.setOnClickListener(new View.OnClickListener() {            @Override            public void onClick(View v) {                mLogView.setVisibility(mLogView.getVisibility() == View.VISIBLE ? View.GONE : View.VISIBLE);            }        });        tishiImageView = findViewById(R.id.iv_szs_fx2);        tishiTextView = findViewById(R.id.tv_mwts);        onlineCountTextView = findViewById(R.id.qn_tv_online_count);        mAudioBitrateText =  findViewById(R.id.audio_bitrate_log_text);        mAudioFpsText =  findViewById(R.id.audio_fps_log_text);        mVideoBitrateText =  findViewById(R.id.video_bitrate_log_text);        mVideoFpsText =  findViewById(R.id.video_fps_log_text);        mVideoView =  findViewById(R.id.PLVideoView);        TextView playUrlText = findViewById(R.id.play_url_text);        mToggleMuteButton = findViewById(R.id.microphone_button);        mDisconnectButton = findViewById(R.id.disconnect_button);        playUrlText.setText(mRtmpUrl);        mPlayUrlText = findViewById(R.id.play_url_text);        mPlayUrlText.setVisibility(View.INVISIBLE);        tvSsStaus = findViewById(R.id.tv_ss_staus);        String mRoomName = LiveFragment.mRoomName;        Log.d(TAG,"mRoomName: " + mRoomName);        if(StringUtils.equals(ssks,mRoomName)){            mToggleMuteButton.setVisibility(View.INVISIBLE);            findViewById(R.id.iv_szs_fx2).setVisibility(View.GONE);            findViewById(R.id.tv_mwts).setVisibility(View.GONE);        }        //权限校验        for (String permission : MANDATORY_PERMISSIONS) {            if (checkCallingOrSelfPermission(permission) != PackageManager.PERMISSION_GRANTED) {                logAndToast("Permission " + permission + " is not granted",true);                setResult(RESULT_CANCELED);                finish();                return;            }        }        //********************************客户化代码 start *******************************************        //TODO 客户化代码        mToggleMuteButton.setOnClickListener(new View.OnClickListener() {            @Override            public void onClick(View view) {                //抢麦功能                tipDialog("您确定要上麦吗？", LiveRoomActivity.this);            }        });        mDisconnectButton.setOnClickListener(new View.OnClickListener() {            @Override            public void onClick(View view) {                finish();            }        });        //播放器相关        mVideoView.setVideoPath(mRtmpUrl);        mVideoView.setOnErrorListener((errorCode, extraData) -> {            switch (errorCode) {                case PLOnErrorListener.ERROR_CODE_OPEN_FAILED:                    logAndToast("播放器打开失败，请确认主播是否在在线！",true);                    break;                case PLOnErrorListener.ERROR_CODE_IO_ERROR:                    logAndToast("网络异常",true);                    break;                default:                    logAndToast("PlayerError Code: " + errorCode,true);                    break;            }            return false;        });        mVideoView.setOnInfoListener((what, extra, extraData) -> {            switch (what) {                case PLOnInfoListener.MEDIA_INFO_VIDEO_RENDERING_START:                    break;                case PLOnInfoListener.MEDIA_INFO_VIDEO_BITRATE:                    mVideoBitrateText.setText("VideoBitrate: " + extra / 1000 + " kb/s");                    break;                case PLOnInfoListener.MEDIA_INFO_VIDEO_FPS:                    mVideoFpsText.setText("VideoFps: " + extra);                    break;                case PLOnInfoListener.MEDIA_INFO_AUDIO_BITRATE:                    mAudioBitrateText.setText("AudioBitrate: " + extra / 1000 + " kb/s");                    break;                case PLOnInfoListener.MEDIA_INFO_AUDIO_FPS:                    mAudioFpsText.setText("AudioFps: " + extra);                    break;                default:                    break;            }        });        mVideoView.start();//        mVideoView.start();  //TODO 这个功能在 refreshPlayer(); 方法启动        refreshPlayer(); //拉流        startTimer(); //启动定时任务        initSysParam(); //初始化系统参数        initFragment(); //初始化聊天模块        //********************************客户化代码 end *******************************************    }    /**     * 初始化系统参数     */    private void initSysParam() {        onlineRecordBiz = new OnlineRecordBiz();        timerTaskHelper = new TimerTaskHelper();        timerTaskHelper.initTimer(handler,100,5000);        OnlineRecordHelper.redisLogin(onlineRecordBiz,member,room.getRoomId());        String show_countOnline = SysParamHelper.getString("show_countOnline", getApplication());        if (StringUtils.isNotBlank(show_countOnline)) {            countOnlineFlag = Boolean.valueOf(show_countOnline);        }    }    /**     * 新增聊天模块     */    private void initFragment() {        FragmentManager fragmentManager = this.getSupportFragmentManager();        FragmentTransaction transaction = fragmentManager.beginTransaction();        MqttFragment mqttFragment = new MqttFragment();        Bundle bundle = new Bundle();        bundle.putString("roomId","R" + RoomInfoHelper.getRoomId(room,LiveRoomActivity.this) + ":");        bundle.putBoolean("isAudioOnly", RoomInfoHelper.getAudioOnly(room));        mqttFragment.setArguments(bundle);        transaction.add(R.id.mqtt_fragment_qn, mqttFragment);        transaction.show(mqttFragment);        transaction.commit();//提交事务    }    @Override    protected void onResume() {        super.onResume();    }    @Override    protected void onDestroy() {        stopTimer();        if(timerTaskHelper != null){            timerTaskHelper.stopTimer();            timerTaskHelper = null;        }        OnlineRecordHelper.redisLogout(onlineRecordBiz,member,room.getRoomId());        onlineRecordBiz = null;        super.onDestroy();        mVideoView.stopPlayback();        qiniuBiz = null;    }    @Override    protected void onPause() {        super.onPause();    }    @Override    public void onBackPressed() {        super.onBackPressed();    }    private void logAndToast(final String msg,boolean isPrint) {        if(!isPrint){            return;        }        runOnUiThread(() -> {            Log.d(TAG, msg);            if (mLogToast != null) {                mLogToast.cancel();            }            mLogToast = Toast.makeText(LiveRoomActivity.this, msg, Toast.LENGTH_SHORT);            mLogToast.show();        });    }  //********************************客户化代码 start *************************************************************************    //TODO 客户化代码    /**     * 提示对话框     */    //************************** 提示对话框 start *********************    public void tipDialog(String tipText, final Context mContext) {        AlertDialog.Builder builder = new AlertDialog.Builder(mContext);        builder.setTitle("温馨提示：");        builder.setMessage(tipText);        builder.setIcon(R.drawable.logo);        builder.setCancelable(true);            //点击对话框以外的区域是否让对话框消失        //设置正面按钮        builder.setPositiveButton("确定", new DialogInterface.OnClickListener() {            @Override            public void onClick(DialogInterface dialog, int which) {                attemptJoinAudio("");                dialog.dismiss();            }        });        //设置反面按钮        builder.setNegativeButton("取消", new DialogInterface.OnClickListener() {            @Override            public void onClick(DialogInterface dialog, int which) {                Toast.makeText(mContext, "您已经放弃连麦...", Toast.LENGTH_SHORT).show();                dialog.dismiss();            }        });        AlertDialog dialog = builder.create();      //创建AlertDialog对象        //对话框显示的监听事件        dialog.setOnShowListener(new DialogInterface.OnShowListener() {            @Override            public void onShow(DialogInterface dialog) {                Log.e(TAG, "对话框显示了");            }        });        //对话框消失的监听事件        dialog.setOnCancelListener(new DialogInterface.OnCancelListener() {            @Override            public void onCancel(DialogInterface dialog) {                Log.e(TAG, "对话框消失了");            }        });        dialog.show();    }    //************************** 提示对话框 end *********************    /**     * 连麦操作     * @param roomName 房间名     */    private void attemptJoinAudio(String roomName){        UIUtils.showTip("正在尝试连麦...",23);        QiniuBiz qiniuBiz = new QiniuBiz();        String legalName = member.getLegalName();        qiniuBiz.openAudio(member.getPhoneNumber(),legalName,roomName, new NormalCommonCallback() {            @Override            public void onError(Exception e) {            }            @Override            public void onSuccess(String response) {                boolean flag = Boolean.valueOf(response);                if(flag){                    UIUtils.showTip("连麦成功,您可以发言了", 23);                    finish();                    Room mRoom = RoomInfoHelper.getRoom(room,LiveRoomActivity.this);                    new EnterRTCRoomHelper().startConference(LiveRoomActivity.this,mRoom,member);                }else{                    UIUtils.showTip("抱歉！连麦失败,您可以再尝试一次.", 23);                }            }        });    }    /**     * 启动定时任务     */    public void startTimer() {        mTimer.setBase(SystemClock.elapsedRealtime());        mTimer.start();    }    /**     * 停止定时任务     */    public void stopTimer() {        mTimer.stop();    }    public void resetTimer() {        mTimer.start();        mTimer.setBase(SystemClock.elapsedRealtime());    }    /**     * 刷新     */    private void refresh() {        finish();        Intent intent = new Intent(LiveRoomActivity.this, LiveRoomActivity.class);        startActivity(intent);    }    //*********************************定时任务 start********************************************    @SuppressLint("HandlerLeak")    Handler handler = new Handler() {        @Override        public void handleMessage(@NonNull Message msg) {            refreshPlayer();   //TODO 观众 正在拉流            getRTCOnlineLegalName(); //TODO 显示当前上麦人员（展示法名）            countOnline();   //TODO 统计在线人数，并展示            getRoomStatus();            super.handleMessage(msg);            tvSsStaus.setText(liveStatus); //TODO 设置房间状态        }    };    //***************************定时end***************************************    QiniuBiz qiniuBiz;    /**     * 显示当前上麦人员（展示法名）     */    private void getRTCOnlineLegalName(){        if(null == qiniuBiz){            qiniuBiz = new QiniuBiz();        }        Integer roomId = RoomInfoHelper.getRoomId(room,LiveRoomActivity.this);        qiniuBiz.getRTCOnlineLegalName(roomId, new NormalCommonCallback() {            @Override            public void onError(Exception e) {            }            @Override            public void onSuccess(String response) {                if(StringUtils.isBlank(response)){                    tishiTextView.setText(R.string.mai_wei_ti_shi);                    tishiImageView.setImageResource(R.mipmap.microphone);                }else{                    List list = JSONObject.parseObject(response, List.class);                    StringBuilder stringBuilder = new StringBuilder();                    for(int i=0;i< list.size();i++){                        stringBuilder.append(list.get(i)).append(" ");                    }                    tishiTextView.setText("当前 " + stringBuilder.toString() + " 在麦上");                    tishiImageView.setImageResource(R.mipmap.microphone_disable);                }            }        });    }    /**     * 统计在线人数，并展示     */    private void countOnline(){        onlineRecordBiz = BizHelper.getOnlineRecordBiz(onlineRecordBiz);        onlineRecordBiz.countOnline(member.getToken(),room.getRoomId(), new NormalCommonCallback() {            @Override            public void onError(Exception e) {            }            @Override            public void onSuccess(String response) {                if(countOnlineFlag){                    onlineCountTextView.setText("在线:" + response);                }else {                    onlineCountTextView.setText("");                }            }        });    }    /**     * 获取房间状态（上师已在线 true | 今天的课已经结束了 end | 请耐心等待）     */    private void getRoomStatus() {        onlineRecordBiz = BizHelper.getOnlineRecordBiz(onlineRecordBiz);        onlineRecordBiz.getRoomStatus(member.getToken(),room.getRoomId(), new NormalCommonCallback() {            @Override            public void onError(Exception e) {            }            @Override            public void onSuccess(String response) {                String spaces = "                            ";                if (StringUtils.isNotBlank(response)) {                    if (StringUtils.endsWithIgnoreCase("true", response)) {                        liveStatus = spaces + "上师已在线..." + spaces;                    } else if(StringUtils.endsWithIgnoreCase("end", response)){                        liveStatus = spaces + "今天的课已经结束了..." + spaces;                    }else {                        liveStatus = spaces + "请耐心等待..." + spaces;                    }                }else {                    liveStatus = spaces + "请耐心等待..." + spaces;                }            }        });    }    private int i = 0;    /**     * 观众 正在拉流     */    private void refreshPlayer(){        if(!isPlay){            i++;            logAndToast("正在拉流...",false);            mVideoView.setBackgroundColor(Color.parseColor("#FFAA66CC"));            mVideoView.setVideoPath(mRtmpUrl);            mVideoView.setOnErrorListener(new PLOnErrorListener() {                @Override                public boolean onError(int errorCode,Object var2) {                    switch (errorCode) {                        case ERROR_CODE_OPEN_FAILED:                            isPlay = false;                            if(i<5){//只提示五次                                logAndToast("播放器打开失败，请确认主播是否在在线！",true);                            }                            break;                        case ERROR_CODE_IO_ERROR:                            logAndToast("网络异常",true);                            break;                        default:                            logAndToast("PlayerError Code: " + errorCode,true);                            break;                    }                    return false;                }            });            mVideoView.setOnInfoListener(new PLOnInfoListener() {                @SuppressLint("SetTextI18n")                @Override                public void onInfo(int what, int extra,Object var3) {                    switch (what) {                        case MEDIA_INFO_VIDEO_RENDERING_START:                            isPlay = true;                            logAndToast("拉流成功！",true);                            break;                        case MEDIA_INFO_VIDEO_BITRATE:                            isPlay = true;                            mVideoBitrateText.setText("VideoBitrate: " + extra / 1000 + " kb/s");                            break;                        case MEDIA_INFO_VIDEO_FPS:                            isPlay = true;                            mVideoFpsText.setText("VideoFps: " + extra);                            break;                        case MEDIA_INFO_AUDIO_BITRATE:                            isPlay = true;                            mAudioBitrateText.setText("AudioBitrate: " + extra / 1000 + " kb/s");                            break;                        case MEDIA_INFO_AUDIO_FPS:                            isPlay = true;                            mAudioFpsText.setText("AudioFps: " + extra);                            break;                        default:                            throw new IllegalStateException("Unexpected value: " + what);                    }                }            });            mVideoView.start();        }    }    //********************************客户化代码 start *******************************************************************************}============================================================================================================package sas.hhsk.live.qiniu.activity;import android.app.AlertDialog;import android.content.ComponentName;import android.content.Context;import android.content.DialogInterface;import android.content.Intent;import android.content.ServiceConnection;import android.content.SharedPreferences;import android.content.pm.PackageManager;import android.graphics.Color;import android.graphics.Point;import android.graphics.drawable.ColorDrawable;import android.os.Build;import android.os.Bundle;import android.os.Handler;import android.os.IBinder;import android.text.TextUtils;import android.util.DisplayMetrics;import android.util.Log;import android.view.Display;import android.view.Gravity;import android.view.LayoutInflater;import android.view.View;import android.view.ViewGroup;import android.view.Window;import android.view.WindowManager;import android.widget.PopupWindow;import android.widget.Toast;import androidx.annotation.Nullable;import androidx.core.content.ContextCompat;import androidx.fragment.app.FragmentActivity;import androidx.fragment.app.FragmentTransaction;import androidx.recyclerview.widget.RecyclerView;import com.alibaba.fastjson.JSON;import com.qiniu.droid.rtc.QNAudioQualityPreset;import com.qiniu.droid.rtc.QNAudioScene;import com.qiniu.droid.rtc.QNAudioVolumeInfo;import com.qiniu.droid.rtc.QNBeautySetting;import com.qiniu.droid.rtc.QNCameraEventListener;import com.qiniu.droid.rtc.QNCameraFacing;import com.qiniu.droid.rtc.QNCameraSwitchResultCallback;import com.qiniu.droid.rtc.QNCameraVideoTrack;import com.qiniu.droid.rtc.QNCameraVideoTrackConfig;import com.qiniu.droid.rtc.QNClientEventListener;import com.qiniu.droid.rtc.QNConnectionDisconnectedInfo;import com.qiniu.droid.rtc.QNConnectionState;import com.qiniu.droid.rtc.QNCustomMessage;import com.qiniu.droid.rtc.QNDegradationPreference;import com.qiniu.droid.rtc.QNDirectLiveStreamingConfig;import com.qiniu.droid.rtc.QNErrorCode;import com.qiniu.droid.rtc.QNLiveStreamingErrorInfo;import com.qiniu.droid.rtc.QNLiveStreamingListener;import com.qiniu.droid.rtc.QNLocalTrack;import com.qiniu.droid.rtc.QNMediaRelayState;import com.qiniu.droid.rtc.QNMicrophoneAudioTrack;import com.qiniu.droid.rtc.QNMicrophoneAudioTrackConfig;import com.qiniu.droid.rtc.QNNetworkQuality;import com.qiniu.droid.rtc.QNNetworkQualityListener;import com.qiniu.droid.rtc.QNPublishResultCallback;import com.qiniu.droid.rtc.QNRTC;import com.qiniu.droid.rtc.QNRTCClient;import com.qiniu.droid.rtc.QNRTCEventListener;import com.qiniu.droid.rtc.QNRTCSetting;import com.qiniu.droid.rtc.QNRemoteAudioTrack;import com.qiniu.droid.rtc.QNRemoteTrack;import com.qiniu.droid.rtc.QNRemoteVideoTrack;import com.qiniu.droid.rtc.QNScreenVideoTrack;import com.qiniu.droid.rtc.QNScreenVideoTrackConfig;import com.qiniu.droid.rtc.QNTrack;import com.qiniu.droid.rtc.QNTrackInfoChangedListener;import com.qiniu.droid.rtc.QNTranscodingLiveStreamingConfig;import com.qiniu.droid.rtc.QNTranscodingLiveStreamingTrack;import com.qiniu.droid.rtc.QNVideoCaptureConfig;import com.qiniu.droid.rtc.QNVideoEncoderConfig;import com.qiniu.droid.rtc.model.QNAudioDevice;import org.apache.commons.lang3.StringUtils;import org.qnwebrtc.Size;import java.util.ArrayList;import java.util.Arrays;import java.util.Collections;import java.util.LinkedList;import java.util.List;import java.util.Map;import java.util.Timer;import java.util.TimerTask;import java.util.concurrent.Semaphore;import java.util.concurrent.TimeUnit;import sas.hhsk.live.R;import sas.hhsk.live.biz.OnlineRecordBiz;import sas.hhsk.live.domain.Member;import sas.hhsk.live.domain.Room;import sas.hhsk.live.fragment.LiveFragment;import sas.hhsk.live.helper.PushPlayerHelper;import sas.hhsk.live.helper.UserInfoHelper;import sas.hhsk.live.net.NormalCommonCallback;import sas.hhsk.live.qiniu.fragment.ControlFragment;import sas.hhsk.live.qiniu.model.RTCRoomMergeOption;import sas.hhsk.live.qiniu.model.RTCTrackMergeOption;import sas.hhsk.live.qiniu.model.RTCUserMergeOptions;import sas.hhsk.live.qiniu.service.ForegroundService;import sas.hhsk.live.qiniu.ui.CircleTextView;import sas.hhsk.live.qiniu.ui.MergeLayoutConfigView;import sas.hhsk.live.qiniu.ui.UserTrackView;import sas.hhsk.live.qiniu.utils.Config;import sas.hhsk.live.qiniu.utils.QNAppServer;import sas.hhsk.live.qiniu.utils.SplitUtils;import sas.hhsk.live.qiniu.utils.ToastUtils;import sas.hhsk.live.qiniu.utils.TrackWindowManager;import sas.hhsk.live.qiniu.utils.Utils;import sas.hhsk.live.util.UIUtils;import static sas.hhsk.live.qiniu.utils.Config.DEFAULT_FPS;import static sas.hhsk.live.qiniu.utils.Config.DEFAULT_RESOLUTION;import static sas.hhsk.live.qiniu.utils.Utils.getSystemUiVisibility;public class RoomActivity extends FragmentActivity implements ControlFragment.OnCallEvents {    private static final String TAG = "RoomActivity";    public static final String TRACK_TAG_MIC = "MICROPHONE";    public static final String TRACK_TAG_CAMERA = "CAMERA";    public static final String TRACK_TAG_SCREEN = "SCREEN";    public static final String EXTRA_USER_ID = "USER_ID";    public static final String EXTRA_ROOM_TOKEN *** "ROOM_TOKEN";    public static final String EXTRA_ROOM_ID = "ROOM_ID";    private static final String CUSTOM_MESSAGE_KICKOUT = "KICKOUT";    private static final String[] MANDATORY_PERMISSIONS = {            "android.permission.MODIFY_AUDIO_SETTINGS",            "android.permission.RECORD_AUDIO",            "android.permission.INTERNET"    };    private Toast mLogToast;    private UserTrackView mTrackWindowFullScreen;    private List<UserTrackView> mTrackWindowsList;    private AlertDialog mKickOutDialog;    private QNRTCClient mClient;    private String mRoomToken;    private String mUserId;    private String mRoomId;    private boolean mMicEnabled = true;    private boolean mBeautyEnabled = false;    private boolean mVideoEnabled = true;    private boolean mSpeakerEnabled = true;    private boolean mIsAdmin = false;    private boolean mIsJoinedRoom = false;    private ControlFragment mControlFragment;    private List<QNLocalTrack> mLocalTrackList;    private QNCameraVideoTrack mCameraTrack;    private QNMicrophoneAudioTrack mMicrophoneTrack;    private QNScreenVideoTrack mLocalScreenTrack;    private int mCaptureMode = Config.CAMERA_CAPTURE;    private TrackWindowManager mTrackWindowManager;    private int mVideoWidth;    private int mVideoHeight;    private int mVideoFps;    private int mVideoBitrate;    /**     * 合流相关     * 注意：     * 一个房间仅需要一个用户可以配置合流布局即可，该用户可以基于 SDK 提供的远端用户相关回调对远端用户的动态进行监听，     * 进而进行合流布局的实时更改。     * demo 中默认 userID 为 "admin" 的用户可以控制合流布局的配置     */    private MergeLayoutConfigView mMergeLayoutConfigView;    private PopupWindow mPopWindow;    private UserListAdapter mUserListAdapter;    private RTCRoomMergeOption mRoomMergeOption;    private RTCUserMergeOptions mMergeOption;    private volatile boolean mIsMergeStreaming;    /**     * 如果 QNTranscodingLiveStreamingConfig 中的 StreamID 为 null，则表示使用默认合流配置     * 默认合流配置的宽高、码率等参数可以通过登录后台 https://***.qiniu.com/rtn 并对连麦应用进行编辑来配置     * 自定义合流转推可以通过自定义 {@link QNTranscodingLiveStreamingConfig} 并调用 {@link QNRTCClient#startLiveStreaming(QNTranscodingLiveStreamingConfig)} 接口来开始     * 注意：自定义合流转推需要在加入房间之后才可执行     */    private QNTranscodingLiveStreamingConfig mCurrentMergeConfig;    /**     * 单路转推相关     * 注意：     * 1. 单路转推仅支持配置一路音频和一路视频     * 2. 单路转推场景需要在初始化的时候保证配置了 "固定分辨率"{@link QNDegradationPreference#MAINTAIN_RESOLUTION} 选项的开启，否则会出问题！！！     * demo 中默认 userId 为 "admin" 的用户可以开启单路转推功能     */    private QNDirectLiveStreamingConfig mCurrentDirectConfig;    private volatile boolean mIsDirectStreaming;    /**     * 如果您的场景包括合流转推和单路转推的切换，那么务必维护一个 serialNum 的参数，代表流的优先级，     * 使其不断自增来实现 rtmp 流的无缝切换，否则可能会出现抢流的现象     * {@link QNDirectLiveStreamingConfig} 以及 {@link QNTranscodingLiveStreamingConfig} 中 Url 的格式为：rtmp://domain/app/stream?serialnum=xxx     * 切换流程推荐为：     * 1. 单路转推 -> 开始合流转推（以成功的回调为准） -> 停止单路转推     * 2. 合流转推 -> 开始单路转推（以成功的回调为准） -> 停止合流转推     * 注意：     * 1. 两种合流转推，推流地址应该保持一致，只有 serialnum 存在差异     * 2. 在两种推流切换的场景下，合流转推务必使用自定义合流配置，并指定推流地址的 serialnum     */    private int mSerialNum = 0;    /**     * {@link QNRTC#init} 和 {@link QNRTC#deinit()} 为静态方法，需要对称调用；     * 为了避免在页面退出进入时存在顺序问题，建议保存是否初始化状态     */    private static boolean mInitRTC;    //******************我新增的代码 start****************************    Room room;    private boolean isRoomConnection = false;    OnlineRecordBiz onlineRecordBiz;    private Member member;    private Handler mHandler;    //*****************我新增的代码 end***************************    private final Semaphore mCaptureStoppedSem = new Semaphore(1);    // 麦克风错误标志    private boolean mMicrophoneError;    @Override    protected void onCreate(Bundle savedInstanceState) {        super.onCreate(savedInstanceState);        requestWindowFeature(Window.FEATURE_NO_TITLE);        getWindow().addFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN | WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON                | WindowManager.LayoutParams.FLAG_DISMISS_KEYGUARD | WindowManager.LayoutParams.FLAG_SHOW_WHEN_LOCKED                | WindowManager.LayoutParams.FLAG_TURN_SCREEN_ON);        getWindow().getDecorView().setSystemUiVisibility(getSystemUiVisibility());        //********************************客户化代码 start *******************************************        //TODO 客户化代码        mHandler = new Handler();        member = UserInfoHelper.readUser(RoomActivity.this);        //********************************客户化代码 end *******************************************        final WindowManager windowManager = (WindowManager) getSystemService(Context.WINDOW_SERVICE);        DisplayMetrics outMetrics = new DisplayMetrics();        windowManager.getDefaultDisplay().getRealMetrics(outMetrics);        int screenWidth = outMetrics.widthPixels;        int screenHeight = outMetrics.heightPixels;        SharedPreferences preferences = getSharedPreferences(getString(R.string.app_name), Context.MODE_PRIVATE);        mVideoWidth = preferences.getInt(Config.WIDTH, DEFAULT_RESOLUTION[1][0]);        mVideoHeight = preferences.getInt(Config.HEIGHT, DEFAULT_RESOLUTION[1][1]);        mVideoFps = preferences.getInt(Config.FPS, DEFAULT_FPS[1]);        mVideoBitrate = preferences.getInt(Config.BITRATE, Config.DEFAULT_BITRATE[1]);        setContentView(R.layout.activity_muti_track_room);        Intent intent = getIntent();        mRoomToken ***.getStringExtra(EXTRA_ROOM_TOKEN);        mUserId = intent.getStringExtra(EXTRA_USER_ID);        mRoomId = intent.getStringExtra(EXTRA_ROOM_ID);//        mIsAdmin = mUserId.equals(QNAppServer.ADMIN_USER);        //********************************客户化代码 start *******************************************        //TODO 客户化代码        if (StringUtils.isNotBlank(member.getPermission())){            if(StringUtils.equals(QNAppServer.ADMIN_USER,member.getPermission().trim())){                mIsAdmin = true;            }        }        String roomString = getIntent().getStringExtra("room");        room = JSON.parseObject(roomString, Room.class);        //********************************客户化代码 end *******************************************        mTrackWindowFullScreen = findViewById(R.id.track_window_full_screen);        mTrackWindowsList = new LinkedList<>(Arrays.asList(                findViewById(R.id.track_window_a),                findViewById(R.id.track_window_b),                findViewById(R.id.track_window_c),                findViewById(R.id.track_window_d),                findViewById(R.id.track_window_e),                findViewById(R.id.track_window_f),                findViewById(R.id.track_window_g),                findViewById(R.id.track_window_h),                findViewById(R.id.track_window_i)        ));        for (final UserTrackView view : mTrackWindowsList) {            view.setOnLongClickListener(v -> {                if (mIsAdmin) {                    showKickoutDialog(view.getUserId());                }                return false;            });        }        // 初始化控制面板        mControlFragment = new ControlFragment();        mControlFragment.setArguments(intent.getExtras());        FragmentTransaction ft = getSupportFragmentManager().beginTransaction();        ft.add(R.id.control_fragment_container, mControlFragment);        ft.commitAllowingStateLoss();        // 权限申请        for (String permission : MANDATORY_PERMISSIONS) {            if (checkCallingOrSelfPermission(permission) != PackageManager.PERMISSION_GRANTED) {                logAndToast("Permission " + permission + " is not granted");                setResult(RESULT_CANCELED);                finish();                return;            }        }        if (mInitRTC) {            ToastUtils.showShortToast(RoomActivity.this, "RTC 未释放完成，当前页面不可用，请退出后重试！");        } else {            // 初始化 Client 和本地 Track 列表            initClient();            // 初始化本地音视频 track            initLocalTracks();            // 初始化合流相关配置            initMergeLayoutConfig();            // 多人显示窗口管理类            mTrackWindowManager = new TrackWindowManager(mUserId, screenWidth, screenHeight, outMetrics.density, mClient, mTrackWindowFullScreen, mTrackWindowsList);            List<QNTrack> localTrackListExcludeScreenTrack = new ArrayList<>(mLocalTrackList);            localTrackListExcludeScreenTrack.remove(mLocalScreenTrack);            mTrackWindowManager.addTrack(mUserId, localTrackListExcludeScreenTrack);            new Timer().schedule(mUpdateNetWorkQualityInfoTask, 5000, 10000);            mInitRTC = true;        }    }    @Override    protected void onResume() {        super.onResume();        // 开始视频采集        startCaptureAfterAcquire();        if (!mIsJoinedRoom && mClient != null) {            // 加入房间            mClient.join(mRoomToken);        }        if (mMicrophoneError && mClient != null && mMicrophoneTrack != null) {            mClient.unpublish(mMicrophoneTrack);            mClient.publish(new QNPublishResultCallback() {                @Override                public void onPublished() {                }                @Override                public void onError(int errorCode, String errorMessage) {                }            }, mMicrophoneTrack);            mMicrophoneError = false;        }    }    private void startCaptureAfterAcquire() {        boolean acquired = false;        try {            acquired = mCaptureStoppedSem.tryAcquire(2000, TimeUnit.MILLISECONDS);        } catch (InterruptedException e) {            e.printStackTrace();        }        if (acquired && mCameraTrack != null) {            mCameraTrack.startCapture();        }    }    @Override    protected void onPause() {        super.onPause();        // 停止视频采集        if (mCameraTrack != null) {            mCameraTrack.stopCapture();        }        if (mPopWindow != null && mPopWindow.isShowing()) {            mPopWindow.dismiss();        }    }    @Override    protected void onDestroy() {        mControlFragment.timerTaskHelper.stopTimer();   //TODO 这行是 客户化代码        super.onDestroy();        //********************************客户化代码 start *******************************************        //TODO 客户化代码        if(PushPlayerHelper.containsUser(member.getPhoneNumber())){            if("9".equals(member.getPhoneNumber())){                PushPlayerHelper.setRoomStatus("end",onlineRecordBiz,member.getToken(),room.getRoomId());            }            UIUtils.showTip("无需释放麦位 ", 23);        }else{            QNAppServer.getInstance().releaseAudio(member.getPhoneNumber(), "","onDestroy");        }        //********************************客户化代码 end *******************************************        if(mIsAdmin){            setQiniuAdminOnline("false");        }        releaseClient();        destroyLocalTracks();        if (mInitRTC) {            // 反初始化            QNRTC.deinit();            mInitRTC = false;        }        if (mTrackWindowFullScreen != null) {            mTrackWindowFullScreen.dispose();        }        for (UserTrackView item : mTrackWindowsList) {            item.dispose();        }        mTrackWindowsList.clear();        mPopWindow = null;    }    private void destroyLocalTracks() {        if (mLocalTrackList != null) {            for (QNLocalTrack localTrack : mLocalTrackList) {                localTrack.destroy();            }            mLocalTrackList.clear();        }        mCameraTrack = null;        mLocalScreenTrack = null;        mMicrophoneTrack = null;    }    private void releaseClient() {        mUpdateNetWorkQualityInfoTask.cancel();        if (mClient != null) {            if (mIsAdmin && mIsMergeStreaming) {                // 如果当前正在合流，则停止                mClient.stopLiveStreaming(mCurrentMergeConfig);                mIsMergeStreaming = false;            }            if (mIsAdmin && mIsDirectStreaming) {                // 如果当前正在单路转推，则停止                mClient.stopLiveStreaming(mCurrentDirectConfig);                mIsDirectStreaming = false;            }            // 离开房间            mClient.leave();            mClient = null;        }    }    /**     * 初始化 QNRTCClient     */    private void initClient() {        SharedPreferences preferences = getSharedPreferences(getString(R.string.app_name), Context.MODE_PRIVATE);        boolean isHwCodec = preferences.getInt(Config.CODEC_MODE, Config.SW) == Config.HW;        /**         * 设置音频场景，不同的音频场景，系统音量模式是不一样的         */        int audioScenePos = preferences.getInt(Config.AUDIO_SCENE, Config.DEFAULT_AUDIO_SCENE);        QNAudioScene audioScene;        if (audioScenePos == Config.DEFAULT_AUDIO_SCENE) {            audioScene = QNAudioScene.DEFAULT;        } else if (audioScenePos == Config.VOICE_CHAT_AUDIO_SCENE) {            audioScene = QNAudioScene.VOICE_CHAT;        } else {            audioScene = QNAudioScene.SOUND_EQUALIZE;        }        mCaptureMode = preferences.getInt(Config.CAPTURE_MODE, Config.CAMERA_CAPTURE);        QNRTCSetting setting = new QNRTCSetting();        setting.setHWCodecEnabled(isHwCodec)                .setAudioScene(audioScene);        QNRTC.init(this, setting, mRTCEventListener);        mClient = QNRTC.createClient(mClientEventListener);        mClient.setLiveStreamingListener(mLiveStreamingListener);        mClient.setNetworkQualityListener(mNetworkQualityListener);    }    /**     * 初始化本地音视频 track     * 关于 Track 的概念介绍 https://***.qnsdk.com/rtn/android/docs/preparation#5     */    private void initLocalTracks() {        mLocalTrackList = new ArrayList<>();        QNMicrophoneAudioTrackConfig microphoneAudioTrackConfig = new QNMicrophoneAudioTrackConfig(TRACK_TAG_MIC);        microphoneAudioTrackConfig.setAudioQuality(QNAudioQualityPreset.STANDARD);        mMicrophoneTrack = QNRTC.createMicrophoneAudioTrack(microphoneAudioTrackConfig);        mMicrophoneTrack.setMicrophoneEventListener((errorCode, errorMessage) -> mMicrophoneError = true);        mLocalTrackList.add(mMicrophoneTrack);        SharedPreferences preferences = getSharedPreferences(getString(R.string.app_name), Context.MODE_PRIVATE);        int videoDegradation = preferences.getInt(Config.VIDEO_DEGRADATION_POS, Config.DEFAULT_VIDEO_DEGRADATION_POS);        switch (mCaptureMode) {            case Config.CAMERA_CAPTURE:                // 创建 Camera 采集的视频 Track                QNCameraVideoTrackConfig cameraVideoTrackConfig = new QNCameraVideoTrackConfig(TRACK_TAG_CAMERA)                        .setCameraFacing(QNCameraFacing.FRONT)                        .setVideoCaptureConfig(new QNVideoCaptureConfig(mVideoWidth, mVideoHeight, mVideoFps))                        .setVideoEncoderConfig(new QNVideoEncoderConfig(mVideoWidth, mVideoHeight, mVideoFps, mVideoBitrate,                                Config.VIDEO_DEGRADATION_PRESET[videoDegradation]));                mCameraTrack = QNRTC.createCameraVideoTrack(cameraVideoTrackConfig);                mCameraTrack.setCameraEventListener(mCameraEventListener);                mLocalTrackList.add(mCameraTrack);                break;            case Config.ONLY_AUDIO_CAPTURE:                mControlFragment.setAudioOnly(true);                break;            case Config.SCREEN_CAPTURE:                // 创建屏幕录制的视频 Track                createScreenTrack();                mControlFragment.setAudioOnly(true);                break;            case Config.MUTI_TRACK_CAPTURE:                // 视频通话 + 屏幕共享两路 track                createScreenTrack();                QNCameraVideoTrackConfig videoTrackConfig = new QNCameraVideoTrackConfig(TRACK_TAG_CAMERA)                        .setCameraFacing(QNCameraFacing.FRONT)                        .setVideoCaptureConfig(new QNVideoCaptureConfig(mVideoWidth, mVideoHeight, mVideoFps))                        .setVideoEncoderConfig(new QNVideoEncoderConfig(mVideoWidth, mVideoHeight, mVideoFps, mVideoBitrate,                                Config.VIDEO_DEGRADATION_PRESET[videoDegradation]));                mCameraTrack = QNRTC.createCameraVideoTrack(videoTrackConfig);                mCameraTrack.setCameraEventListener(mCameraEventListener);                mLocalTrackList.add(mCameraTrack);                break;            default:                break;        }    }    // 录屏时建议分辨率和屏幕分辨率比例保存一致，避免录屏画面有黑边或者不清晰    private QNVideoEncoderConfig createScreenEncoderConfig() {        Display display = getWindowManager().getDefaultDisplay();        Point size = new Point();        display.getSize(size);        SharedPreferences preferences = getSharedPreferences(getString(R.string.app_name), Context.MODE_PRIVATE);        int videoDegradation = preferences.getInt(Config.VIDEO_DEGRADATION_POS, Config.DEFAULT_VIDEO_DEGRADATION_POS);        int width = (int) (size.x * Config.DEFAULT_SCREEN_VIDEO_TRACK_SIZE_SCALE);        int height = (int) (size.y * Config.DEFAULT_SCREEN_VIDEO_TRACK_SIZE_SCALE);        int bitrate = (int) (width * height * 1.0f / Config.DEFAULT_RESOLUTION[1][0] /                Config.DEFAULT_RESOLUTION[1][1] * Config.DEFAULT_BITRATE[1]);        return new QNVideoEncoderConfig(width, height,  Config.DEFAULT_FPS[0], bitrate, Config.VIDEO_DEGRADATION_PRESET[videoDegradation]);    }    private final ServiceConnection mServiceConnection = new ServiceConnection() {        @Override        public void onServiceConnected(ComponentName name, IBinder service) {            QNScreenVideoTrackConfig screenVideoTrackConfig = new QNScreenVideoTrackConfig(TRACK_TAG_SCREEN)                    .setVideoEncoderConfig(createScreenEncoderConfig());            mLocalScreenTrack = QNRTC.createScreenVideoTrack(screenVideoTrackConfig);            mLocalTrackList.add(mLocalScreenTrack);            if (mClient != null && (mClient.getConnectionState() == QNConnectionState.CONNECTED                    || mClient.getConnectionState() == QNConnectionState.RECONNECTED)) {                mClient.publish(mPublishResultCallback, Collections.singletonList(mLocalScreenTrack));            }        }        @Override        public void onServiceDisconnected(ComponentName name) {        }    };    // 处理 Build.VERSION_CODES.Q 及以上的兼容问题    private void createScreenTrack() {        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {            Intent intent = new Intent(this, ForegroundService.class);            startForegroundService(intent);            bindService(intent, mServiceConnection, Context.BIND_AUTO_CREATE);            Log.i(TAG, "start service for Q");        } else {            QNScreenVideoTrackConfig screenVideoTrackConfig = new QNScreenVideoTrackConfig(TRACK_TAG_SCREEN)                    .setVideoEncoderConfig(createScreenEncoderConfig());            mLocalScreenTrack = QNRTC.createScreenVideoTrack(screenVideoTrackConfig);            mLocalTrackList.add(mLocalScreenTrack);        }    }    /**     * 合流转推、单路转推相关处理     */    private void initMergeLayoutConfig() {        mMergeLayoutConfigView = new MergeLayoutConfigView(this);        mMergeLayoutConfigView.setRoomId(mRoomId);        mUserListAdapter = new UserListAdapter();        mRoomMergeOption = new RTCRoomMergeOption();        mMergeLayoutConfigView.getUserListView().setAdapter(mUserListAdapter);        mMergeLayoutConfigView.setOnClickedListener(() -> {            // 保存当前用户选择的配置信息            mMergeLayoutConfigView.updateMergeOptions();            if (mClient == null) {                return;            }            if (!mMergeLayoutConfigView.isStreamingEnabled()) {                // 处理停止合流逻辑                if (mIsMergeStreaming) {                    // 如果正在推流，则停止之前的合流转推                    mClient.stopLiveStreaming(mCurrentMergeConfig);                    mIsMergeStreaming = false;                    ToastUtils.showShortToast(RoomActivity.this, "停止合流！！！");                } else {                    ToastUtils.showShortToast(RoomActivity.this, "未开启合流，配置未生效！！！");                }                if (mPopWindow != null) {                    mPopWindow.dismiss();                }                return;            }            // 如果当前正在进行单路转推，那么切换到合流转推的时候，务必使用自定义合流配置，否则可能会出现抢流的现象            if (mIsDirectStreaming && !mMergeLayoutConfigView.isCustomMerge()) {                Utils.showAlertDialog(RoomActivity.this, getString(R.string.create_merge_warning));                mMergeLayoutConfigView.updateStreamingStatus(false);                if (mPopWindow != null) {                    mPopWindow.dismiss();                }                return;            }            if (mMergeLayoutConfigView.isCustomMerge()) {                // 处理自定义合流转推的逻辑                QNTranscodingLiveStreamingConfig mergeConfig = mMergeLayoutConfigView.getCustomMergeConfig();                if (mergeConfig != null) {                    // 如果正在推流，则停止之前的合流转推                    if (mIsMergeStreaming) {                        mClient.stopLiveStreaming(mCurrentMergeConfig);                    }                    mCurrentMergeConfig = mergeConfig;                    // 开始自定义合流转推                    mClient.startLiveStreaming(mCurrentMergeConfig);                } else {                    // 更新合流布局到自定义合流配置                    setMergeStreamLayouts();                }            } else {                // 更新合流布局到默认合流配置                mCurrentMergeConfig = new QNTranscodingLiveStreamingConfig();                setMergeStreamLayouts();            }            if (mPopWindow != null) {                mPopWindow.dismiss();            }        });    }    private void logAndToast(final String msg) {        Log.d(TAG, msg);        if (mLogToast != null) {            mLogToast.cancel();        }        mLogToast = Toast.makeText(this, msg, Toast.LENGTH_SHORT);        mLogToast.show();    }    private void disconnectWithErrorMessage(final String errorMessage) {        new AlertDialog.Builder(this)                .setTitle(getText(R.string.channel_error_title))                .setMessage(errorMessage)                .setCancelable(false)                .setNeutralButton(R.string.ok, (dialog, id) -> {                    dialog.cancel();                    finish();                })                .create()                .show();    }    private void showKickoutDialog(final String userId) {        if (mKickOutDialog == null) {            mKickOutDialog = new AlertDialog.Builder(this)                    .setNegativeButton(R.string.negative_dialog_tips, null)                    .create();        }        mKickOutDialog.setMessage(getString(R.string.kickout_tips, userId));        mKickOutDialog.setButton(DialogInterface.BUTTON_POSITIVE, getResources().getString(R.string.positive_dialog_tips), (dialog, which) -> {            if (mClient != null) {                mClient.sendMessage(Collections.singletonList(userId),CUSTOM_MESSAGE_KICKOUT,CUSTOM_MESSAGE_KICKOUT);            }        });        mKickOutDialog.show();    }    private void updateRemoteLogText(final String logText) {        Log.i(TAG, logText);        mControlFragment.updateRemoteLogText(logText);    }    /**     * 当新的本地、远端 Track 变化时，重新排列合流画面配置     */    private void resetMergeStream() {        Log.d(TAG, "resetMergeStream()");        // video tracks merge layout options.        List<RTCTrackMergeOption> roomVideoTrackList = mRoomMergeOption.getVideoMergeOptions();        boolean isDefaultStreaming = (mCurrentMergeConfig == null || TextUtils.isEmpty(mCurrentMergeConfig.getStreamID()));        if (!roomVideoTrackList.isEmpty()) {            List<QNTranscodingLiveStreamingTrack> mergeTrackOptions = SplitUtils.split(                    roomVideoTrackList.size(),                    isDefaultStreaming ?                            QNAppServer.STREAMING_WIDTH                            : mCurrentMergeConfig.getWidth(),                    isDefaultStreaming ?                            QNAppServer.STREAMING_HEIGHT                            : mCurrentMergeConfig.getHeight()            );            if (mergeTrackOptions.size() != roomVideoTrackList.size()) {                Log.e(TAG, "split option error.");                return;            }            for (int i = 0; i < mergeTrackOptions.size(); i++) {                RTCTrackMergeOption trackMergeOption = roomVideoTrackList.get(i);                if (!trackMergeOption.isTrackInclude()) {                    continue;                }                QNTranscodingLiveStreamingTrack item = mergeTrackOptions.get(i);                trackMergeOption.updateMergeTrack(item);            }        }        if (mIsMergeStreaming) {            updateMergeTrack();        }    }    private void userJoinedForStreaming(String userId, String userData) {        mRoomMergeOption.onUserJoined(userId, userData);        if (mUserListAdapter != null) {            mUserListAdapter.notifyDataSetChanged();        }    }    private void userLeftForStreaming(String userId, boolean localLeft) {        if (localLeft) {            mRoomMergeOption.onUserLeft();        } else {            mRoomMergeOption.onUserLeft(userId);        }        if (mUserListAdapter != null) {            mUserListAdapter.notifyDataSetChanged();        }    }    private int updateSerialNum() {        mMergeLayoutConfigView.updateSerialNum(++mSerialNum);        return mSerialNum;    }    /**     * 配置各个用户当前选中的 Track 信息到合流布局     */    private void setMergeStreamLayouts() {        updateMergeTrack();        mIsMergeStreaming = true;        ToastUtils.showShortToast(RoomActivity.this, "已发送合流配置，请等待合流画面生效");    }    private void updateMergeTrack() {        List<RTCTrackMergeOption> userOptions = new ArrayList<>();        for (int user = 0; user < mRoomMergeOption.size(); user++) {            RTCUserMergeOptions userMergeOptions = mRoomMergeOption.getUserMergeOptionByPosition(user);            if (userMergeOptions.getAudioMergeOption() != null) {                userOptions.add(userMergeOptions.getAudioMergeOption());            }            if (userMergeOptions.getVideoMergeOptions().size() > 0) {                userOptions.addAll(userMergeOptions.getVideoMergeOptions());            }        }        List<QNTranscodingLiveStreamingTrack> mergeTracks = new ArrayList<>();        List<QNTranscodingLiveStreamingTrack> removedTracks = new ArrayList<>();        for (RTCTrackMergeOption item : userOptions) {            if (item.isTrackInclude()) {                mergeTracks.add(item.getMergeTrack());            } else {                removedTracks.add(item.getMergeTrack());            }        }        if (!mergeTracks.isEmpty()) {            // 配置对应 Track 的合流配置信息            if (mMergeLayoutConfigView.isCustomMerge()) {                mClient.setTranscodingLiveStreamingTracks(mCurrentMergeConfig.getStreamID(), mergeTracks);            } else {                mClient.setTranscodingLiveStreamingTracks(null, mergeTracks);            }        }        if (!removedTracks.isEmpty()) {            // 移除对应 Track 的合流配置，移除后相应 Track 的数据将不会参与合流            if (mMergeLayoutConfigView.isCustomMerge()) {                mClient.removeTranscodingLiveStreamingTracks(mCurrentMergeConfig.getStreamID(), removedTracks);            } else {                mClient.removeTranscodingLiveStreamingTracks(null, removedTracks);            }        }    }    @Override    public void onCallHangUp() {        releaseClient();        finish();    }    @Override    public void onCameraSwitch() {        if (mCameraTrack != null) {            mCameraTrack.switchCamera(new QNCameraSwitchResultCallback() {                @Override                public void onSwitched(boolean isFrontCamera) {                }                @Override                public void onError(String errorMessage) {                }            });        }    }    @Override    public boolean onToggleMic() {        if (mMicrophoneTrack != null) {            mMicEnabled = !mMicEnabled;            mMicrophoneTrack.setMuted(!mMicEnabled);            if (mTrackWindowManager != null) {                mTrackWindowManager.onTrackMuted(mUserId);            }        }        return mMicEnabled;    }    @Override    public boolean onToggleVideo() {        if (mCameraTrack != null) {            mVideoEnabled = !mVideoEnabled;            mCameraTrack.setMuted(!mVideoEnabled);            if (mLocalScreenTrack != null) {                mLocalScreenTrack.setMuted(!mVideoEnabled);            }            mCameraTrack.setMuted(!mVideoEnabled);            if (mTrackWindowManager != null) {                mTrackWindowManager.onTrackMuted(mUserId);            }        }        return mVideoEnabled;    }    @Override    public boolean onToggleSpeaker() {        if (mClient != null) {            mSpeakerEnabled = !mSpeakerEnabled;            QNRTC.setSpeakerphoneMuted(!mSpeakerEnabled);        }        return mSpeakerEnabled;    }    @Override    public boolean onToggleBeauty() {        if (mCameraTrack != null) {            mBeautyEnabled = !mBeautyEnabled;            QNBeautySetting beautySetting = new QNBeautySetting(0.5f, 0.5f, 0.5f);            beautySetting.setEnable(mBeautyEnabled);            mCameraTrack.setBeauty(beautySetting);        }        return mBeautyEnabled;    }    @Override    public void onCallMerge() {        if (!mIsAdmin) {            ToastUtils.showShortToast(RoomActivity.this, "只有 \"admin\" 用户可以开启合流转推！！！");            return;        }        // 配置页        if (mRoomMergeOption.size() == 0) {            return;        }        mMergeOption = mRoomMergeOption.getUserMergeOptionByPosition(0);        mMergeLayoutConfigView.updateConfigInfo(mMergeOption);        mMergeLayoutConfigView.updateMergeConfigInfo();        mUserListAdapter.notifyDataSetChanged();        if (mPopWindow == null) {            mPopWindow = new PopupWindow(mMergeLayoutConfigView, ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT, true);            mPopWindow.setBackgroundDrawable(new ColorDrawable(ContextCompat.getColor(this, R.color.popupWindowBackground)));        }        mPopWindow.showAtLocation(getWindow().getDecorView().getRootView(), Gravity.BOTTOM, 0, 0);    }    @Override    public void onToggleDirectLiving() {        if (!mIsAdmin) {            ToastUtils.showShortToast(RoomActivity.this, "只有 \"admin\" 用户可以开启单流转推！！！");            return;        }        if (!mIsDirectStreaming) {            // 如果当前正在进行默认配置合流转推，则不允许切换成单路转推，需要停止默认配置合流转推或者使用自定义合流转推            if (mIsMergeStreaming && mCurrentMergeConfig == null) {                Utils.showAlertDialog(this, getString(R.string.create_direct_warning));                return;            }            if (mCurrentDirectConfig == null) {                mCurrentDirectConfig = new QNDirectLiveStreamingConfig();                mCurrentDirectConfig.setStreamID(mRoomId);                mCurrentDirectConfig.setAudioTrack(mMicrophoneTrack);                switch (mCaptureMode) {                    case Config.CAMERA_CAPTURE:                    case Config.MUTI_TRACK_CAPTURE:                        mCurrentDirectConfig.setVideoTrack(mCameraTrack);                        break;                    case Config.SCREEN_CAPTURE:                        mCurrentDirectConfig.setVideoTrack(mLocalScreenTrack);                        break;                    default:                        break;                }            }            mCurrentDirectConfig.setUrl(String.format(getResources().getString(R.string.publish_url), mRoomId, mSerialNum));            if (mClient != null) {                mClient.startLiveStreaming(mCurrentDirectConfig);            }        } else {            if (mClient != null) {                mClient.stopLiveStreaming(mCurrentDirectConfig);                mIsDirectStreaming = false;                mControlFragment.updateDirectText(getString(R.string.direct_btn_text));                ToastUtils.showShortToast(RoomActivity.this, "已停止 id=" + mCurrentDirectConfig.getStreamID() + " 的单流转推！！！");            }        }    }    @Override    public boolean onRoomStateChangedListener() {//        return false;        return isRoomConnection;    }    private final TimerTask mUpdateNetWorkQualityInfoTask = new TimerTask() {        @Override        public void run() {            if (mClient != null) {                Map<String, QNNetworkQuality> qualityMap = mClient.getUserNetworkQuality();                for (Map.Entry<String, QNNetworkQuality> entry : qualityMap.entrySet()) {                    Log.i(TAG, "remote user " + entry.getKey() + " " + entry.getValue().toString());                }            }        }    };    /**     * 用户合流配置相关     */    private class UserListAdapter extends RecyclerView.Adapter<ViewHolder> {        int[] mColor = {                Color.parseColor("#588CEE"),                Color.parseColor("#F8CF5F"),                Color.parseColor("#4D9F67"),                Color.parseColor("#F23A48")        };        @Override        public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {            return new ViewHolder(LayoutInflater.from(getApplicationContext()).inflate(R.layout.item_user, parent, false));        }        @Override        public void onBindViewHolder(final ViewHolder holder, int position) {            RTCUserMergeOptions RTCUserMergeOptions = mRoomMergeOption.getUserMergeOptionByPosition(position);            String userId = RTCUserMergeOptions.getUserID();            holder.username.setText(userId);            holder.username.setCircleColor(mColor[position % 4]);            if (mMergeOption != null && mMergeOption.getUserID().equals(userId)) {                holder.itemView.setBackground(getResources().getDrawable(R.drawable.white_background));            } else {                holder.itemView.setBackgroundResource(0);            }            holder.itemView.setOnClickListener(v -> {                mMergeOption = mRoomMergeOption.getUserMergeOptionByPosition(holder.getAdapterPosition());                mMergeLayoutConfigView.updateConfigInfo(mMergeOption);                notifyDataSetChanged();            });        }        @Override        public int getItemCount() {            return mRoomMergeOption.size();        }    }    private static class ViewHolder extends RecyclerView.ViewHolder {        CircleTextView username;        private ViewHolder(View itemView) {            super(itemView);            username = itemView.findViewById(R.id.user_name_text);        }    }    private final QNRTCEventListener mRTCEventListener = new QNRTCEventListener() {        /**         * 当音频路由发生变化时会回调此方法         *         * @param device 音频设备, 详情请参考{@link QNAudioDevice}         */        @Override        public void onAudioRouteChanged(QNAudioDevice device) {            updateRemoteLogText("onAudioRouteChanged: " + device.name());        }    };    private final QNClientEventListener mClientEventListener = new QNClientEventListener() {        /**         * 连接状态改变时会回调此方法         * 连接状态回调只需要做提示用户，或者更新相关 UI； 不需要再做加入房间或者重新发布等其他操作！         * @param state 连接状态，可参考 {@link QNConnectionState}         */        @Override        public void onConnectionStateChanged(QNConnectionState state, @Nullable QNConnectionDisconnectedInfo info) {            Log.i(TAG, "onConnectionStateChanged:" + state.name());            switch (state) {                case DISCONNECTED:                    /**                     *【TOKEN ***】                     * 1. {@link QNErrorCode.ERROR_TOKEN_ERROR} 表示您提供的房间 token *** token ***,                     *    详情请参考【服务端开发说明.RoomToken ***】https://***.qnsdk.com/rtn/docs/server_overview#1                     * 2. {@link QNErrorCode.ERROR_TOKEN_EXPIRED} 表示您的房间 token ***, 需要重新生成 token ***；                     *                     *【房间设置相关】以下情况可以与您的业务服务开发确认具体设置                     * 1. {@link QNErrorCode.ERROR_ROOM_FULL} 当房间已加入人数超过每个房间的人数限制触发；请确认后台服务的设置；                     * 2. {@link QNErrorCode.ERROR_PLAYER_ALREADY_EXIST} 后台如果配置为开启【禁止自动踢人】,则同一用户重复加入/未正常退出再加入会触发此错误，您的业务可根据实际情况选择配置；                     * 3. {@link QNErrorCode.ERROR_NO_PERMISSION} 用户对于特定操作，如合流需要配置权限，禁止出现未授权的用户操作；                     * 4. {@link QNErrorCode.ERROR_ROOM_CLOSED} 房间已被管理员关闭；                     *                     *【其他错误】                     * 1. {@link QNErrorCode.ERROR_AUTH_FAIL} 服务验证时出错，可能为服务网络异常。建议重新尝试加入房间；                     * 2. {@link QNErrorCode.ERROR_PUBLISH_FAIL} 发布失败, 会有如下3种情况:                     * 1 ）请确认成功加入房间后，再执行发布操作                     * 2 ）请确定对于音频/视频 Track，分别最多只能有一路为 master                     * 3 ）请确认您的网络状况是否正常                     * 3. {@link QNErrorCode.ERROR_RECONNECT_TOKEN_ERROR} 内部重连后出错，一般出现在网络非常不稳定时出现，建议提示用户并尝试重新加入房间；                     *    另外，当前用户之前进行的合流转推、单路转推的服务将会被销毁，重新加入房间后应该重新开始合流转推、单路转推 ！！！                     * 4. {@link QNErrorCode.ERROR_INVALID_PARAMETER} 服务交互参数错误，请在开发时注意合流、踢人动作等参数的设置。                     * 5. {@link QNErrorCode.ERROR_DEVICE_CAMERA} 系统摄像头错误, 建议提醒用户检查                     */                    if (info == null || info.getReason() != QNConnectionDisconnectedInfo.Reason.ERROR) {                        return;                    }                    switch (info.getErrorCode()) {                        case QNErrorCode.ERROR_AUTH_FAILED:                            logAndToast("服务验证时出错，可能为服务网络异常");                            mClient.join(mRoomToken);                            break;                        case QNErrorCode.ERROR_TOKEN_ERROR:                            logAndToast("roomToken ***，请检查后重新生成，再加入房间");                            break;                        case QNErrorCode.ERROR_TOKEN_EXPIRED:                            logAndToast("roomToken过期");                            Member member = UserInfoHelper.readUser(RoomActivity.this); //TODO 客户化代码                            mRoomToken ***.getInstance().requestRoomToken(RoomActivity.this, mUserId, member);                            mClient.join(mRoomToken);                            break;                        case QNErrorCode.ERROR_PLAYER_ALREADY_EXIST:                            logAndToast("不允许同一用户重复加入");                            break;                        case QNErrorCode.ERROR_MEDIA_CAP_NOT_SUPPORT:                            logAndToast("该设备不支持指定的音视频格式，无法进行连麦");                            break;                        case QNErrorCode.ERROR_FATAL:                            logAndToast("非预期错误");                            finish();                            break;                        case QNErrorCode.ERROR_RECONNECT_FAILED:                            logAndToast("内部重连失败");                            mClient.join(mRoomToken);                        default:                            logAndToast("errorCode:" + info.getErrorCode() + " description:" + info.getErrorMessage());                            break;                    }                    if (mIsAdmin) {                        userLeftForStreaming(mUserId, true);                    } else if (info.getReason() == QNConnectionDisconnectedInfo.Reason.KICKED_OUT) {                        ToastUtils.showShortToast(RoomActivity.this, getString(R.string.kicked_by_admin));                        finish();                    }                    break;                case RECONNECTING:                    logAndToast(getString(R.string.reconnecting_to_room));                    mControlFragment.stopTimer();                    break;                case CONNECTED:                    if (mIsAdmin) {                        userJoinedForStreaming(mUserId, "");                    }                    // 加入房间后可以进行 tracks 的发布                    mClient.publish(mPublishResultCallback, mLocalTrackList);                    logAndToast(getString(R.string.connected_to_room));                    mIsJoinedRoom = true;                    mControlFragment.startTimer();                    // 重连失败后再次加入房间后，恢复无效的合流转推                    if (mIsMergeStreaming && mMergeLayoutConfigView.isCustomMerge() && !mMergeLayoutConfigView.isMergeConfigValid()) {                        QNTranscodingLiveStreamingConfig mergeConfig = mMergeLayoutConfigView.getCustomMergeConfig();                        if (mergeConfig != null) {                            mCurrentMergeConfig = mergeConfig;                            // 开始自定义合流转推                            mClient.startLiveStreaming(mCurrentMergeConfig);                        }                    }                    break;                case RECONNECTED:                    logAndToast(getString(R.string.connected_to_room));                    mControlFragment.startTimer();                    break;                case CONNECTING:                    logAndToast(getString(R.string.connecting_to, mRoomId));                    break;                default:                    break;            }        }        /**         * 远端用户加入房间时会回调此方法         * @see QNRTCClient#join(String, String) 可指定 userData 字段         *         * @param remoteUserID 远端用户的 userId         * @param userData 透传字段，用户自定义内容         */        @Override        public void onUserJoined(String remoteUserID, String userData) {            updateRemoteLogText("onRemoteUserJoined:remoteUserId = " + remoteUserID + " ,userData = " + userData);            if (mIsAdmin) {                userJoinedForStreaming(remoteUserID, userData);            }        }        @Override        public void onUserReconnecting(String remoteUserID) {            logAndToast("远端用户: " + remoteUserID + " 重连中");        }        @Override        public void onUserReconnected(String remoteUserID) {            logAndToast("远端用户: " + remoteUserID + " 重连成功");        }        /**         * 远端用户离开房间时会回调此方法         *         * @param remoteUserID 远端离开用户的 userId         */        @Override        public void onUserLeft(String remoteUserID) {            updateRemoteLogText("onRemoteUserLeft:remoteUserId = " + remoteUserID);            if (mIsAdmin) {                userLeftForStreaming(remoteUserID, false);            }        }        /**         * 远端用户 tracks 成功发布时会回调此方法         *         * @param remoteUserID 远端用户 userId         * @param trackList 远端用户发布的 tracks 列表         */        @Override        public void onUserPublished(String remoteUserID, List<QNRemoteTrack> trackList) {            updateRemoteLogText("onRemotePublished:remoteUserId = " + remoteUserID);            mRoomMergeOption.onTracksPublished(remoteUserID, new ArrayList<>(trackList));            // 如果希望在远端发布音视频的时候，自动配置合流，则可以在此处重新调用 setMergeStreamLayouts 进行配置            if (mIsAdmin) {                resetMergeStream();            }        }        /**         * 远端用户 tracks 成功取消发布时会回调此方法         *         * @param remoteUserID 远端用户 userId         * @param remoteTracks 远端用户取消发布的 tracks 列表         */        @Override        public void onUserUnpublished(String remoteUserID, List<QNRemoteTrack> remoteTracks) {            updateRemoteLogText("onRemoteUnpublished:remoteUserId = " + remoteUserID);            List<QNTrack> trackList = new ArrayList<>(remoteTracks);            if (mTrackWindowManager != null) {                mTrackWindowManager.removeTrack(remoteUserID, trackList);            }            mRoomMergeOption.onTracksUnPublished(remoteUserID, trackList);            if (mIsAdmin) {                resetMergeStream();            }        }        /**         * 订阅远端用户 Track 成功时会回调此方法         *         * @param remoteUserID 远端用户 userId         * @param remoteAudioTracks 订阅的远端用户音频 tracks 列表         * @param remoteVideoTracks 订阅的远端用户视频 tracks 列表         */        @Override        public void onSubscribed(String remoteUserID, List<QNRemoteAudioTrack> remoteAudioTracks, List<QNRemoteVideoTrack> remoteVideoTracks) {            updateRemoteLogText("onSubscribed:remoteUserId = " + remoteUserID);            if (mTrackWindowManager != null) {                List<QNTrack> tracks = new ArrayList<>();                tracks.addAll(remoteAudioTracks);                tracks.addAll(remoteVideoTracks);                mTrackWindowManager.addTrack(remoteUserID, tracks);                for (QNTrack track : tracks) {                    ((QNRemoteTrack)track).setTrackInfoChangedListener(new QNTrackInfoChangedListener() {                        @Override                        public void onMuteStateChanged(boolean isMuted) {                            updateRemoteLogText("onRemoteUserMuted:remoteUserId = " + remoteUserID);                            if (mTrackWindowManager != null) {                                mTrackWindowManager.onTrackMuted(remoteUserID);                            }                        }                    });                }            }        }        /**         * 当收到自定义消息时回调此方法         *         * @param message 自定义信息，详情请参考 {@link QNCustomMessage}         */        @Override        public void onMessageReceived(QNCustomMessage message) {            if (message.getContent().equals(CUSTOM_MESSAGE_KICKOUT)){                ToastUtils.showShortToast(RoomActivity.this, "您被踢出房间！");                finish();            }        }        /**         * 跨房媒体转发状态改变时会回调此方法         *         * @param relayRoom 媒体转发的房间名         * @param state 媒体转发的状态         */        @Override        public void onMediaRelayStateChanged(String relayRoom, QNMediaRelayState state) {        }        /**         * 用户音量提示回调，本地远端一起回调，本地 user id 为空         *         * @param userVolumeList 用户音量信息，按音量由高到低排序，静音用户不在此列表中体现。         */        @Override        public void onUserVolumeIndication(List<QNAudioVolumeInfo> userVolumeList) {        }    };    private final QNCameraEventListener mCameraEventListener = new QNCameraEventListener() {        @Override        public int[] onCameraOpened(List<Size> sizes, List<Integer> fpsAscending) {            SharedPreferences preferences = getSharedPreferences(getString(R.string.app_name), Context.MODE_PRIVATE);            int videoWidth = preferences.getInt(Config.WIDTH, DEFAULT_RESOLUTION[1][0]);            int videoHeight = preferences.getInt(Config.HEIGHT, DEFAULT_RESOLUTION[1][1]);            int fps = preferences.getInt(Config.FPS, DEFAULT_FPS[1]);            // 根据设备能力选择匹配的采集参数            int wantSize = -1; // 选择的分辨率下标, -1 表示不做选择, 使用 QNCameraVideoTrackConfig 的设置            int wantFps = -1;  // 选择的帧率下标, -1 表示不做选择, 使用 QNCameraVideoTrackConfig 的设置            /**             * 以下代码仅示例：             * 当硬件可用分辨率和当前设置宽高一致时，直接选择该分辨率；当没有完全一致的宽高时，选择使用高度匹配的一个分辨率;             * 您也可以根据自己业务需要，选择宽高最接近的一个分辨率或其他匹配方式。             *             * 如果没有需要，也可以返回 -1 由 SDK 根据设置来匹配接近的分辨率。             */            for (int i = 0; i < sizes.size(); i++) {                if (sizes.get(i).height == videoHeight) {                    wantSize = i;                    if (sizes.get(i).width == videoWidth) {                        break;                    }                }            }            for (int value : fpsAscending) {                if (fps == value) {                    wantFps = fps;                    break;                }            }            return new int[]{wantSize, wantFps};        }        @Override        public void onCaptureStarted() {        }        @Override        public void onCaptureStopped() {            mCaptureStoppedSem.drainPermits();            mCaptureStoppedSem.release();        }        @Override        public void onError(int errorCode, String description) {        }        @Override        public void onPushImageError(int errorCode, String errorMessage) {        }    };    private final QNPublishResultCallback mPublishResultCallback = new QNPublishResultCallback() {        /**         * 本地 Track 成功发布时会回调         */        @Override        public void onPublished() {            updateRemoteLogText("onLocalPublished");            if (mIsAdmin) {                mRoomMergeOption.onTracksPublished(mUserId, new ArrayList<>(mLocalTrackList));                resetMergeStream();            }        }        /**         * 本地 Track 发布失败时回调         *         * @param errorCode    错误码         * @param errorMessage 详细错误信息         */        @Override        public void onError(int errorCode, String errorMessage) {        }    };    private final QNLiveStreamingListener mLiveStreamingListener = new QNLiveStreamingListener() {        /**         * 当自定义合流任务和直接转推任务开启成功的时候会回调此方法         *         * @param streamID 转推成功的 streamID         */        @Override        public void onStarted(String streamID) {            if (mCurrentMergeConfig != null && mCurrentMergeConfig.getStreamID() != null &&                    mCurrentMergeConfig.getStreamID().equals(streamID)) {                updateSerialNum();                ToastUtils.showShortToast(RoomActivity.this, "合流转推 " + streamID + " 创建成功！");                setMergeStreamLayouts();                // 取消单路转推                if (mIsDirectStreaming) {                    // 注意：A 房间中开始的单路转推，只能在 A 房间中进行停止，无法在其他房间中停止                    mClient.stopLiveStreaming(mCurrentDirectConfig);                    mIsDirectStreaming = false;                    mControlFragment.updateDirectText(getString(R.string.direct_btn_text));                }            } else {                updateSerialNum();                mControlFragment.updateDirectText(getString(R.string.stop_direct_text));                ToastUtils.showShortToast(RoomActivity.this, "单路转推 " + streamID + " 创建成功！");                mIsDirectStreaming = true;                // 取消合流转推                if (mIsMergeStreaming && mCurrentMergeConfig != null) {                    // 注意：A 房间中开始的合流转推，只能在 A 房间中进行停止，无法在其他房间中停止                    mClient.stopLiveStreaming(mCurrentMergeConfig);                    mIsMergeStreaming = false;                    mMergeLayoutConfigView.updateStreamingStatus(false);                    mMergeLayoutConfigView.updateMergeConfigValid(false);                }            }        }        @Override        public void onStopped(String streamID) {        }        @Override        public void onTranscodingTracksUpdated(String streamID) {        }        @Override        public void onError(String streamID, QNLiveStreamingErrorInfo errorInfo) {        }    };    private final QNNetworkQualityListener mNetworkQualityListener = new QNNetworkQualityListener() {        /**         * 当网络质量更新时会回调此方法         *         * {@link QNNetworkQuality#uplinkNetworkGrade} 代表上行网络质量         * {@link QNNetworkQuality#downlinkNetworkGrade} 代表下行网络质量         * 可以用来向用户提示自己网络状态不佳（比如连续一段时间网络质量为 {@link com.qiniu.droid.rtc.QNNetworkGrade#POOR}）。         *         * @param quality 网络质量，详情请参考 {@link QNNetworkQuality}         */        @Override        public void onNetworkQualityNotified(QNNetworkQuality quality) {            runOnUiThread(() -> mControlFragment.updateLocalVideoLogText(quality.toString()));        }    };  //********************************** 客户化代码 start **********************************************    //TODO 客户化代码  /*  @Override    public void onKickedOut(String userId) {        if(PushPlayerHelper.containsUser(member.getPhoneNumber())){            UIUtils.showTip("无需释放麦位 ", 23);        }else{            QNAppServer.getInstance().releaseAudio(member.getPhoneNumber(), "","onKickedOut");        }        ToastUtils.showShortToast(RoomActivity.this, getString(R.string.kicked_by_admin));        gotoLiveRoomActivity();        finish();    }*/    public void gotoLiveRoomActivity() {        Intent intent = new Intent(this, LiveRoomActivity.class);        intent.putExtra(RoomActivity.EXTRA_ROOM_ID, LiveFragment.mRoomName);        intent.putExtra(RoomActivity.EXTRA_ROOM_TOKEN, LiveFragment.token);        intent.putExtra(RoomActivity.EXTRA_USER_ID, LiveFragment.mUserName);        intent.putExtra("room",LiveFragment.roomJsonData);        startActivity(intent);    }    private void setQiniuAdminOnline(String status){        if(onlineRecordBiz == null){            onlineRecordBiz = new OnlineRecordBiz();        }        onlineRecordBiz.setQiniuAdminOnline(member.getToken(), status, new NormalCommonCallback() {            @Override            public void onError(Exception e) {            }            @Override            public void onSuccess(String response) {                if (Boolean.valueOf(response)){                }else{                    String msg = "您好，您是管理员，退出房间失败，您可以选择重试或者联系开发人员帮忙处理。";                    UIUtils.showTip(msg,23);                }            }        });    }    //************************************客户化代码 end *********************************************}

**客服**：QPlayer2是新版播放器sdk之后主要维护这个播放器sdk，和老版相比api不一样，实现的功能更多具体的可以参考文档﻿https://***.qiniu.com/pili/12221/qplayer2-integration-to-prepare

**客服**：现在提示： 播放器打开失败，请确认是否在推流！--------这个问题您的使用场景是rtc合流转推到直播云的吗，辛苦发一下appid，房间名称，以及时间点呢，这边查一下转推的情况

**客户**：QPlayer2是新版播放器sdk之后主要维护这个播放器sdk，和老版相比api不一样，实现的功能更多具体的可以参考文档﻿https://***.qiniu.com/pili/12221/qplayer2-integration-to-prepare您好： 上面两个类的代码 我是完全从贵公司的 QNRTC-Android-6.4.0 demo 拿过来，一模一样，几乎没有什么改动。 而且之前是可以的。

**客户**：现在提示： 播放器打开失败，请确认是否在推流！  答： 在推流，管理员登录上之后，然后一直有人上麦说话，但是观众听不到声音。--------这个问题您的使用场景是rtc合流转推到直播云的吗，辛苦发一下appid，房间名称，以及时间点呢，这边查一下转推的情况答：是的,使用场景是rtc合流转推到直播云， appid : fmd7iusef ,  房间名称:FXWD ,时间：10月31号晚上11点 到 11月1号 凌晨2点40 这个范围

**客户**：您好，这个问题能快点处理吗？已经好几个月了

**客服**：您好，这边同步下

**客户**：麻烦，这边有点着急

### 客服解答

您好，这边同步下

### 根本原因分析

配置相关问题，需要调整或优化系统配置

---

## 播放问题

**分类**：对象存储｜上传下载

### 问题描述

播放问题

### 详细对话

**客户**：播放问题

**客服**：是指云存储里视频资源播放有问题吗？

**客户**：是的

**客户**：就是我上传的视频复制链接放到后台去，播放不了

**客户**：https://***b7bgu.site/10%E6%9C%8830%E6%97%A5.mp4

**客服**：稍等

**客户**：好的

**客服**：您视频先缓存再播放看下呢，我这边是可以播放的，大文件，加载需要一点时间

**客户**：不能播放呢我前台和后台都播放不了

**客服**：这个页面缓存文件：https://***.qiniu.com/cdn/refresh-prefetch?tab=prefetchUrl选文件预取

**客户**：还是不行不能播放我短剧后台也播放不了这个链接我短剧后台的说的是填写M8U3地址

**客服**：https://***eedtest.cn 这里打开测一下速

**客户**：上传195下载125

**客户**：我后台播放显示的是这个文章The media could not be loaded, either because the server or network failed or because the format is not supported.

**客服**：可以尝试对视频进行转码

**客服**：https://***.qiniu.com/dora/6488/task-01您看下呢，编码选择 264 ，自定义码率 4000kbps

**客户**：这个是教程吗

**客服**：是的，这个是转码教程

**客户**：直到是看不懂

**客服**：https://***.qiniu.com/dora/media-gate/task这里打开，添加任务

**客服**：然后选择具体要转码的对象

**客服**：创建这个流程[图片]

**客服**：普通转码点击小画笔，然后自定义预设，封装格式您可以自己选了，自定义码率设置为 4000[图片]

**客户**：我这里没有工作流模块

**客服**：截图看下呢

**客服**：不需要工作流，选择任务模块即可

**客服**：不需要工作流呢，您直接自定义工作流即可

**客户**：这里发不过去截图

**客服**：任务定义那采用自定义工作流，点方框的加号即可创建普通转码和输出

**客户**：然后呢

**客户**：输出怎么设置

**客服**：然后编辑普通转码和输出模块

**客户**：我到前缀和后缀了

**客服**：普通转码的编辑方式在上面说了

**客户**：就是不用点输出的小画笔吗

**客服**：输出需要点，编辑一下输出文件的名字以及存储位置

**客户**：自定义的硥

**客户**：转码需要多久

**客服**：主要看任务本身大小

**客服**：转码会产生一点费用：https://***.qiniu.com/prices/dora具体您可以看下

**客户**：什么，费用

**客户**：我这个大概多少钱

**客服**：这里是费用文档：https://***.qiniu.com/prices/dora

**客服**：您转码的是这个视频吗：https://***b7bgu.site/10%E6%9C%8830%E6%97%A5.mp4

**客户**：是的

**客服**：稍等

**客户**：好的

**客户**：好了吗

**客服**：这个是按照 2k ，这个档位[图片]

**客服**：您那边视频链接在浏览器播放会卡吗？

**客户**：我没有试，我也不知道卡不卡

**客户**：我刚刚看了卡

**客服**：您播放看下呢

**客户**：我刚刚播放了卡

**客服**：稍等

**客服**：视频转码完成了吗

**客户**：没有

**客户**：太慢了

**客服**：其他视频卡吗，还是只有这一个

**客服**：如果其他视频也卡的话，您提供一下提供 ip、dns 信息：可以通过访问下述链接获取本地的 ip 和 dns 信息，然后截图通过工单提交给我们https://***tuo.qq.com/使用 chrome 浏览器，按照下述文档获取下信息https://***.qiniu.com/fusion/kb/1478/how-to-access-network-in-the-browser-request-information

**客户**：发不了截图

**客服**：发文本信息也可以

**客户**：先等转码完成吧还不知道需要多久

**客服**：您之前文件预取有做完吗

**客户**：嗯

**客服**：当前您问题还是打开链接，加载不出画面的卡对吧。不是播放过程中的卡

**客户**：转码成功了下一步是什么

**客服**：在浏览器访问一下转码后的文件

**客户**：不卡，但是我后台还是访问不了啊

**客服**：后台是指哪里

**客户**：你加我微信吧你们这里又发不了截图[图片]

**客服**：自行使用的播放器吗？

**客户**：发过去了，你看看

**客户**：你看看，地址也对，就是不能播放[图片]

**客服**：浏览器播放没问题吧？如果浏览器播放没问题，说明cdn访问服务是正常的，这边看域名也没有配置过什么限制您那边可以检查一下后台视频资源引入

**客户**：你仔细看我这个了吗

**客户**：播放地址需要M3U8地址[图片]

**客户**：这个[图片]

**客户**：？？？

**客服**：您好，后台需要播放m3u8地址的话，您的转码需要选择对应的m3u8格式这种[图片]

**客户**：你为什么不在之前说，现在转码完了说我之前也给你发了转码说明了啊

**客户**：这不是又得重新转码啊你们是不是都不认真看我们给你发的消息和截图的，老把我们往错误的方向引导

**客服**：您好，很抱歉，上面的工程师回复的有问题，如果需要m3u8的话，需要选择这种类型

**客户**：就是我得创新转码了这不是一次两次错误引导了很多次了

**客服**：您好，是的，需要您重新提交转码

**客户**：是的

**客服**：您好，您可以先提交，转码看下

**客户**：哎

**客服**：您好，有什么问题您再反馈

**客户**：为什么还播放不了

**客户**：转码后需要复制哪里的链接

**客服**：您好，在输出那边看下，这个key是输出后的文件名称，使用这个名称进行访问[图片]

**客户**：还是播放不了

**客户**：你看看[图片]

**客户**：错误的[图片]

**客服**：您好，文件外链提供下，这边访问看下

**客户**：dianyingzhuanma10月30日MP4.mp4

**客户**：dianying10月30日MP4.m3u8

**客服**：https://***b7bgu.site/dianying10月30日MP4.m3u8
您好，看起来是可以正常访问的播放的，您这边直接在浏览器的访问有什么报错吗

**客户**：可以了就是前面得加上域名吗

**客服**：您好，是的，需要使用完整的外链才能访问的

### 客服解答

您好，是的，需要使用完整的外链才能访问的

### 根本原因分析

上传失败，需检查网络连接、文件大小限制或存储空间配置

---

## 需要提供一下商户的联系方式

**分类**：对象存储｜其他类咨询

### 问题描述

由于之前人员变动，七牛这边的商户联系不到，麻烦提供一下商务的联系方式，或者加我一下微信 [REDACTED_PHONE]

### 详细对话

**客户**：由于之前人员变动，七牛这边的商户联系不到，麻烦提供一下商务的联系方式，或者加我一下微信 [REDACTED_PHONE]

**客服**：已经帮您反馈，最迟明天商务人员联系您

**客户**：好的，谢谢

**客服**：您客气了

**客服**：你好，商务反馈已与您联系

### 客服解答

你好，商务反馈已与您联系

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 申请将账号和账号绑定为合并费用父子账号，由父账号来结算子账号的费用

**分类**：账户与财务｜计费问题

### 问题描述

父账号：[REDACTED_EMAIL]子账号：[REDACTED_EMAIL]     申请将账号[REDACTED_EMAIL]和账号[REDACTED_EMAIL]绑定为合并费用父子账号，由父账号来结算子账号的费用。

### 详细对话

**客户**：父账号：[REDACTED_EMAIL]子账号：[REDACTED_EMAIL]     申请将账号[REDACTED_EMAIL]和账号[REDACTED_EMAIL]绑定为合并费用父子账号，由父账号来结算子账号的费用。

**客服**：好的，这边帮您反馈下

### 客服解答

好的，这边帮您反馈下

### 根本原因分析

计费或费用相关咨询

---

## 申请将账号父账号和子账号绑定为合并费用父子账号，由父账号来结算子账号的费用。

**分类**：账户与财务｜计费问题

### 问题描述

父账号：[REDACTED_EMAIL]子账号：[REDACTED_EMAIL]     申请将账号[REDACTED_EMAIL]和账号[REDACTED_EMAIL]绑定为合并费用父子账号，由父账号来结算子账号的费用。

### 详细对话

**客户**：父账号：[REDACTED_EMAIL]子账号：[REDACTED_EMAIL]     申请将账号[REDACTED_EMAIL]和账号[REDACTED_EMAIL]绑定为合并费用父子账号，由父账号来结算子账号的费用。

**客服**：好的，这边已经帮您反馈，预计最迟明天相关专员为您处理，您看下呢？

### 客服解答

好的，这边已经帮您反馈，预计最迟明天相关专员为您处理，您看下呢？

### 根本原因分析

计费或费用相关咨询

---

## 如何计算储存费用？

**分类**：账户与财务｜计费问题

### 问题描述

储存和流量费如何计算？

### 详细对话

**客户**：储存和流量费如何计算？

**客服**：https://***.qiniu.com/prices/qcdnhttps://***.qiniu.com/products/kodo

**客服**：您好您可以使用最新的图形化工具kodo-browser上传/下载试下，支持批量管理。https://***.qiniu.com/kodo/tools/5972/kodo-browser注意：使用该工具目前进行上传/下载，如果不指定cdn域名的话，下载产生的流量费用为「外网流量」

### 客服解答

您好您可以使用最新的图形化工具kodo-browser上传/下载试下，支持批量管理。https://***.qiniu.com/kodo/tools/5972/kodo-browser注意：使用该工具目前进行上传/下载，如果不指定cdn域名的话，下载产生的流量费用为「外网流量」

### 根本原因分析

计费或费用相关咨询

---

## 退款资源包

**分类**：账户与财务｜其他类咨询

### 问题描述

购买了500g的资源包但是暂时不需要了

### 详细对话

**客户**：购买了500g的资源包但是暂时不需要了

**客服**：订单号提供一下，还有您联系方式

**客服**：您好，麻烦资源包订单号提供下，这边帮您申请退订呢

**客户**：已经退款了，在申请提现

### 客服解答

您好，麻烦资源包订单号提供下，这边帮您申请退订呢

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 图片都看不了

**分类**：对象存储｜上传下载

### 问题描述

图片看不了

### 详细对话

**客户**：图片看不了[图片]

**客服**：资源链接提供下

**客户**：https://***iniucs.com/7ecce27cbef08c1caa182fe9020ee63dc0d6f17b20e274ab891120356c03b3a7.jpg

**客服**：您好，请稍等

**客服**：您好，s3域名不是给你们直接访问的，你们要使用空间的CDN 域名 或者 源站域名才可以，S3域名是AWS-S3的签算加密方式访问

**客户**：我添加了域名但是CNAME 都不通过[图片][图片]

**客户**：[图片]这个是阿里云

**客服**：主机记录是 @ , 然后记录值才是这边给你们分配的cname ，你们设置错了

**客户**：访问速度慢是什么原因，打开一个2M图要几分钟

**客服**：您好，您的域名现在是纯海外加速，国内访问慢是符合预期的，你们需要将域名调整为国内加速次啊可以

**客服**：您好，您的域名现在是纯海外加速，国内访问慢是符合预期的，你们需要将域名调整为国内加速才可以

### 客服解答

您好，您的域名现在是纯海外加速，国内访问慢是符合预期的，你们需要将域名调整为国内加速才可以

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 充值后是否可以进行开票？

**分类**：账户与财务｜发票问题

### 问题描述

我们想了解充值后是否可以进行开票？

### 详细对话

**客户**：我们想了解充值后是否可以进行开票？

**客服**：您好，可以的，在发票管理中申请开票：https://***.qiniu.com/financial/invoice-contract/invoice

**客户**：是充值以后就可以开票，还是说要消费后才能开票？我需要确认一下，这个涉及到我的报销流程。

**客服**：您好，充值后就能开票哈

**客户**：我个人在线充值，可以开公司发票吗？

**客服**：您好，普票可以的，专票需要账号企业认证。

**客户**：[图片]我们现在的账号是企业认证成功的状态吧？可以开专票吗？

**客服**：是的，可以开，在发票管理中申请就可以哈

### 客服解答

是的，可以开，在发票管理中申请就可以哈

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 配置回源地址提示域名「wx.30post.cn」测试未通过

**分类**：CDN｜访问下载

### 问题描述

我们的域名是 wx.30post.cn回源地址配置的是 https://***ost.cn但是提示 域名「wx.30post.cn」测试未通过 我不是很理解这是什么意思

### 详细对话

**客户**：我们的域名是 wx.30post.cn回源地址配置的是 https://***ost.cn但是提示 域名「wx.30post.cn」测试未通过 我不是很理解这是什么意思

**客服**：您好，您的回源地址可以测试访问到吗？

**客户**：可以测试访问到https://***.30post.cn/login.html

**客服**：完整的配置信息截图提供下 这边代理测试

**客户**：现在海外显示502 gateway bad,其他目前好了

**客服**：检查一下您的源站 cdnwx.30post.cn[图片]

**客户**：https://***.30post.cn/login.html

**客户**：我的源站没问题

**客服**：cdn域名是对您源站的资源加速的  您的源站直接访问就是这个报错[图片]

**客户**：你疯了么？你看我的链接，你会不会打字？？login.html，你眼瞎么？

**客户**：别瞎耽误功夫

**客户**：打了几遍都不看，就会个截图了是么？

**客服**：ping 一下 wx.30post.cn
[图片]

**客户**：47.246.42.165Ping wx.30post.cn.w.cdngslb.com [47.246.***.***.***]

**客服**：好的 这边代理检测下 请您稍等

**客服**：您好通过过滤日志看是回源502，对应源站IP是：211.149.***.***.***（您的源站域名解析IP）辛苦您核实下源站是否正常[图片]

**客户**：是的，是正常的，国内的没有问题

**客户**：用七牛云的cdn，在国内段不存在问题，在海外段存在问题，一个不出现502 一个出现502，用回源502解释不通吧？如果回源502了，那国内部分也会报错不是么？但是国内是好的

**客服**：您好，这个是海外回源您国内主机超时了，建议你将国内 和  海外CDN分开 ，可以国内使用CDN ，海外直接访问您的源站，或者您再设置一个海外海外国内CDN1 回源国内服务器海外CDN2 回源海外服务器这样效果会更好一些

**客户**：我们就是希望解决海外直接访问源站速度慢的问题，所以想用cdn解决，前天我们这么设置了以后，还可以也能访问，不过因为一些原因下掉了，昨天就不能访问了

**客服**：海外回源国内服务器是会有超时现象的目前针对您描述的业务场景 建议您专门配置一下海外使用的cdn域名 回源到海外服务器 这样部署对访问速度会有优化提高

### 客服解答

海外回源国内服务器是会有超时现象的目前针对您描述的业务场景 建议您专门配置一下海外使用的cdn域名 回源到海外服务器 这样部署对访问速度会有优化提高

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 状态一直处理中

**分类**：CDN｜配置问题

### 问题描述

应该卡了有好几个月了。

### 详细对话

**客户**：[图片]应该卡了有好几个月了。

**客服**：您好，很抱歉让你久等了，当前已经处理好了，您看一下

### 客服解答

您好，很抱歉让你久等了，当前已经处理好了，您看一下

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 证书审核加急

**分类**：CDN｜证书问题

### 问题描述

麻烦帮忙加急审核一下

### 详细对话

**客户**：麻烦帮忙加急审核一下

**客服**：您好，这边目前ca无法检测到验证值，您这边确认一下，验证值是否完成https://***kzmall.com/.well-known/pki-validation/68696956AFE8E62CDC1EF25D2EB415FE.txt

**客户**：已完成，你再试下

**客户**：已签发，谢谢

**客服**：访问502[图片]

**客户**：服务重启导致的，现在访问正常。我看到已签发了谢谢

**客服**：嗯嗯好的不客气的

### 客服解答

嗯嗯好的不客气的

### 根本原因分析

CDN访问问题，可能涉及域名解析、缓存、或浏览器缓存问题

---

## 免费 from 自动催单

**分类**：CDN｜证书问题

### 问题描述

长时间处于免费证书申请环节

### 详细对话

**客户**：长时间处于免费证书申请环节

### 客服解答

问题记录中，等待客服响应

### 根本原因分析

SSL证书配置问题，需检查证书状态和HTTPS配置

---

## 调用视频采样缩略图接口报错

**分类**：对象存储｜工具使用

### 问题描述

使用七牛云对象存储api——视频采样缩略图（vsample）接口时，采用对已有资源手动触发的使用api的方式，调用该接口报："error": "no such bucket"（status code 631）。        查阅文档发现是“资源空间”名称不对，然后从七牛云控制台—>对象存储 Kodo—>空间管理那里查到的空间名称是qfs-t-video，然后再发接口，还是报 "no such bucket"，到底是怎么回事？已经反复确认过资源空间名称存在且填写无误！麻烦帮忙看看是啥情况？      附图是数据报文

### 详细对话

**客户**：使用七牛云对象存储api——视频采样缩略图（vsample）接口时，采用对已有资源手动触发的使用api的方式，调用该接口报："error": "no such bucket"（status code 631）。        查阅文档发现是“资源空间”名称不对，然后从七牛云控制台—>对象存储 Kodo—>空间管理那里查到的空间名称是qfs-t-video，然后再发接口，还是报 "no such bucket"，到底是怎么回事？已经反复确认过资源空间名称存在且填写无误！麻烦帮忙看看是啥情况？      附图是数据报文[图片]

**客服**：您好，完整的请求提供下，这边看下

**客服**：您好，完整的请求复制提供下，这边看下

**客户**：请求报文见附件[图片]

**客服**：您好，麻烦复制提供下，这边看下您的文件链接这些信息或者处理的文件链接复制提供下可以吗

**客户**：哦哦，抱歉，忘了复制一份了，完整报文：POST /pfop/ HTTP/1.1Authorization: Qiniu 4Q97t-pe1ZrZhT7tf5CdSG5LL4SPmyHKUVA8gLtJ:HOCzzKgguHTOnD546GUkonZOByc=Content-Type: application/x-www-form-urlencodedCache-Control: no-cachePostman-Token: ***: api.qiniu.com bucket=qfs-t-video&key=411681%2F2021%2F12%2F3%2FYAP20211130****2052%2FYAP20211130****2052_163****801165.mp4&notifyURL=http%3A%2F%2Fuat.wjwcore.com%2FqiqiuNotify&workflowTemplateID=vsample HTTP/1.1 631 status code 631Server: openrestyDate: Thu, 31 Oct 2024 01:27:15 GMTContent-Type: application/jsonContent-Length: 26Connection: keep-aliveX-Log: redis.g;ZONEPROXY/631;APIS:1/631X-Reqid: DwsAAADc65xGZQMYX-Reqid: DwsAAADc65xGZQMY {"error":"no such bucket"}文件连接：相对路径：411681/2021/12/3/YAP20211130****2052/YAP20211130****2052_163****801165.mp4（相对qfs-t-video空间下的根路径）

**客服**：您好，这个key不要进行url安全编码呢，直接使用存储内保存的名称，回调地址也直接使用对应的链接这样才可以找到411681/2021/12/3/YAP20211130****2052/YAP20211130****2052_163****801165.mp4

**客户**：去掉url编码也是不行，哭。。。POST /pfop/ HTTP/1.1Authorization: Qiniu 4Q97t-pe1ZrZhT7tf5CdSG5LL4SPmyHKUVA8gLtJ:HOCzzKgguHTOnD546GUkonZOByc=Content-Type: application/x-www-form-urlencodedCache-Control: no-cachePostman-Token: ***: api.qiniu.com bucket=qfs-t-video&key=411681/2021/12/3/YAP20211130****2052/YAP20211130****2052_163****801165.mp4&notifyURL=https://***jwcore.com/qiqiuNotify&workflowTemplateID=vsample HTTP/1.1 631 status code 631Server: openrestyDate: Thu, 31 Oct 2024 02:16:09 GMTContent-Type: application/jsonContent-Length: 26Connection: keep-aliveX-Log: redis.g;ZONEPROXY/631;APIS:1/631X-Reqid: lu4AAADVIr7xZwMYX-Reqid: lu4AAADVIr7xZwMY {"error":"no such bucket"}

**客服**：您好，您这边使用的使用什么语言的SDK，这边直接给您一个demo您测试看下可以吗

**客服**：您好，您这边使用的ak和sk是对应账号下的吗

**客服**：您好，您这边使用的使用什么语言的SDK，这边直接给您一个demo您测试看下可以吗

**客户**：刚确认过，ak和sk没有问题，我们公司就这一个账号，只有一对密钥，否则鉴权也不会通过。发个nodejs的demo吧

**客服**：您好，参考下这个，修改下fops就好https://***/qiniu/nodejs-sdk/blob/master/examples/video_pfop.js

**客户**：老师，用demo调通了，还有个问题就是，怎么下载截图呢？现在回调url接收的参数如下：{  '{"id":"z0.01z022d59szwj1mwbv00mum3rr000g1s","pipeline":"1381675671.default.sys","code":0,"desc":"The fop was completed successfully","reqid":"wqcAAADGL_wleAMY","inputBucket":"qfs-t-video","inputKey":"220100/2023/12/8/HT202312071200000384121/HT202312071200000384121_170****187623.mp4","items":[{"cmd":"vsample/jpg/frames/12/savePattern/dmZyYW1lLSQoY291bnQp","code":0,"desc":"The fop was completed successfully","keys":["vframe-000001","vframe-000002","vframe-000003","vframe-000004","vframe-000005","vframe-000006","vframe-000007","vframe-000008","vframe-000009","vframe-000010","vframe-000011","vframe-000012"],"returnOld":0}],"creationDate":"2024-10-31T15:13:06.391595102 08:00"}': ''}现在只知道截图的名称，问题是怎么下载呢？

**客服**：您好，就是这些名称，但是您这个空间没有绑定域名，可以使用图形化工具，走外网流出流量下载vframe-000001，vframe-000002﻿[图片]

**客户**：哦哦，那我知道了，原来是放到根目录下了，我们空间有个绑定域名。就是这些截图能不能放到指定目录下呢？万一有重名的源文件，这样还好区分一下

**客服**：您好，可以的，这个参数可以指定参考文档https://***.qiniu.com/dora/1315/video-sampling-thumbnails-vsample[图片]

**客户**：OK，完美解决，多谢大佬（抱拳）！

**客服**：没事的，有什么问题您再反馈

### 客服解答

没事的，有什么问题您再反馈

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 资源包抵扣

**分类**：账户与财务｜计费问题

### 问题描述

现在买外网流出流量资源包，可以抵扣这个月的么

### 详细对话

**客户**：[图片]现在买外网流出流量资源包，可以抵扣这个月的么

**客服**：您好，您购买本月生效的资源包，可以抵扣的

### 客服解答

您好，您购买本月生效的资源包，可以抵扣的

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 根据这个账号目前的存储 和视频流量 可以提供一个 购买流量包的方案吗？ 谢谢

**分类**：对象存储｜其他类咨询

### 问题描述

根据这个账号目前的存储 和视频流量 可以提供一个 购买流量包的方案吗？ 谢谢

### 详细对话

**客户**：根据这个账号目前的存储 和视频流量 可以提供一个 购买流量包的方案吗？ 谢谢

**客服**：你好，好的，麻烦留一下您的联系方式，这边商务同事跟进对接

**客户**：[REDACTED_PHONE]

**客服**：好的，稍后联系您

**客户**：你好已经充值购买了。 不过  可能网络原因  支付的时候 提示超时 现在看账号余额 是负数。   资源包也没看到。麻烦帮忙看一下。   谢谢

**客服**：稍等

**客服**：您好，您重新购买下，余额和使用的券都退了哈

**客户**：我上午充值的时候 可用额是40多。  充值了200   然后 下单+优惠券后购买 220 现在看可用额只有204   ？？ 是什么原因

**客服**：稍等，这边确认下

**客服**：商务同事已跟进沟通，您这边还有其他问题吗

### 客服解答

商务同事已跟进沟通，您这边还有其他问题吗

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## QVS空间创建空间列表导出

**分类**：对象存储｜其他类咨询

### 问题描述

申请  QVS空间所创建空间内  导出 所有设备的所有通道ID及通道名称 列表

### 详细对话

**客户**：申请  QVS空间所创建空间内  导出 所有设备的所有通道ID及通道名称 列表

**客户**：您好，需要申请导出  QVS空间内 所创建空间【空间ID：lehefood】 设备管理内 的 设备国际ID 【该空间内所有的设备国际ID】的通道列表，导出所有通道ID，以及通道名称，请问需要如何操作获取结果

**客服**：您好，可以参考下这个api文档获取空间列表https://***.qiniu.com/qvs/6730/list-namespace获取批次列表https://***.qiniu.com/qvs/10170/get-batch-list

**客户**：如何获取通道列表？

**客服**：您好，通道列表是这个apihttps://***.qiniu.com/qvs/6906/query-channel-list

**客服**：设备列表https://***.qiniu.com/qvs/6902/Query-device-list

**客户**：请问支持一次性把所有通道列表都查询吗？还是只能查询某个设备国标ID下的通道列表？

**客服**：您好，国标ID下的通道

**客户**：是否支持同个空间内多个国标ID下的通道列表查询导出？

**客服**：您好，参考下文档，不支持的

### 客服解答

您好，参考下文档，不支持的

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 视频文件访问及下载问题

**分类**：CDN｜流量计费问题

### 问题描述

有个素材网站，需要存储大量视频及下载大文件，问一下资费情况

### 详细对话

**客户**：有个素材网站，需要存储大量视频及下载大文件，问一下资费情况

**客服**：您好，这个你参考下存储计费 https://***.qiniu.com/prices/kodo和 CDN下载流量计费即可https://***.qiniu.com/prices/qcdn

**客户**：我网站有访客上传视频素材，文件几百M到2G左右，先上传到oss空间， 再下载到我本地。这个下载流量怎么收费

**客服**：您好，按照实际下载的总流量大小进行计算，每个请求最终会流量累计汇总的

**客户**：收费标准是每gb多少，我看看想把业务迁移到七牛上来

**客服**：您好，单价您在官网可以看到的，流量计费 http 0.24 https0.28 每GB

### 客服解答

您好，单价您在官网可以看到的，流量计费 http 0.24 https0.28 每GB

### 根本原因分析

计费或费用相关咨询

---

## 免费 from 自动催单

**分类**：CDN｜证书问题

### 问题描述

长时间处于域名检测环节

### 详细对话

**客户**：长时间处于域名检测环节

**客服**：稍等

**客服**：您好，久等了，配置已下发

### 客服解答

您好，久等了，配置已下发

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## CDN流量计费是按时间还是按文件的大小计费？

**分类**：CDN｜流量计费问题

### 问题描述

比如1G的视频看了1小时，另1上100M的视频看了1小时，计费有具体区别吗

### 详细对话

**客户**：比如1G的视频看了1小时，另1上100M的视频看了1小时，计费有具体区别吗

**客服**：您好，CDN流量计费，按照客户端真实请求流量大小计费，如果1个100M的文件，连续请求3次，3次都下载完成，那么就会产生300M流量，这个主要看文件下载或者观看的真实大小，文件即便是1h的，但是客户端播放器会提前下载完成，主要影响的还是下载时长+文件大小

**客户**：这是14个视频的播放时间，每个文件最多1G，单位秒
  4218
  3757
  4292
  6602
  3091
  3958
  3657
  3570
  3598
  3989
  2807
  3409
  3727
  3296
，和
  14.27583333
小时，但是学生就费了400G流量怎么回事呢[图片][图片][图片]

**客户**：假如在视频过程中有拖拽，会另计费吗

**客户**：[REDACTED_PHONE]电话沟通可以吗

**客服**：您好，视频拖拽本身就是客户端在重新发起请求了，每次拖拽都会有流量产生，这个视频播放不是下载到本地播放，都是请求的数据流进行播放的

**客户**：那不对啊，我们后台看到这14个视频有12个是自然看完一次，有两个拖是两次但都是正向的向前拖拽比如一个视频1G1个小时，从零看了20分钟，然后又拖到40分钟处看到结速，0-20，40-60，这两段，那应该费多少流量呢？把我的问题全面的都回答完！

**客服**：您好，视频的播放流量要看客户端自身的播放逻辑的，这个这边无法给您具体准确数值，各个厂商都是这样的1：如果播放器/浏览器一直在请求资源，不使用本地缓存的情况下，20分钟就可以把资源全部下载下来了，假设下载速度10MB/s ，1024MB的文件，17分钟差不多就可以下载完成了0-20 ，1GB文件已经下载外出，流量1GB 40 - 60 ，拖拽播放，客户端再次发起请求获取资源，range：341MB - 结束，重新请求消耗流量 669MB左右两个加一起，流量1.66GB左右2：如果你们的播放器利用缓存，在第一次播放的时候，就将文件全部缓存到本地，拖拽的话都从本地缓存中播放，那么拖拽不再触发请求，不消耗流量，那么流量就只消耗1GB，0-20分钟1GB ，40 - 60 本地缓存/沙盒文件，不消耗

**客户**：那也不对啊，我这找了两个看到多的，就是刚才截图里的两个学生，后一个只拖了两次，就算是1个G（最大我们能上传的文件1G限制），14个应该是14G，就算是拖一次再加一个G，那12+2*2=16G，那怎么会出现400G呢，附件有观看日志记录[图片][图片]

**客服**：你们是从哪里看到两个学生请求400G的呢，观看的视频URL 是哪个呢

**客户**：https://***po.yzyw.cn/b7d88cf7ce8150874dec28263cf73003.mp4https://***po.yzyw.cn/a8ba885fce17e131e1f03cd91913434a.mp4https://***po.yzyw.cn/f6b8fc2fd7fb91645740f1e8c9ef29a1.mp4https://***po.yzyw.cn/dc4d062e238a027e0059dae144a85872.mp4https://***po.yzyw.cn/9faed1837f02524633d86a635d172e8e.mp4https://***po.yzyw.cn/cd9433c4d0e5c7da2fa9c8e665f65848.mp4https://***po.yzyw.cn/8ad84bf3461e2f978cd1de8faf4e68fb.mp4https://***po.yzyw.cn/fb586c29dbb9b8f239bf48a0a5d933f1.mp4https://***po.yzyw.cn/6241a1108290a4bfcfeadbb3e0daff1a.mp4https://***po.yzyw.cn/a134daf594947ee169****98172c83c8.mp4https://***po.yzyw.cn/9d64fbf485995b8d85a2e1d16fc3d911.mp4https://***po.yzyw.cn/1d1a89eb7693aab29b4328b79784eacc.mp4https://***po.yzyw.cn/b1e1b9f3ba4b10a4ed07968c57344f6d.mp4https://***po.yzyw.cn/4f92791b6582027c1e2ade00d317dad3.mp4

**客户**：这是徐正宽看的那14个视频

**客服**：您好，徐正宽的客户端ip是多少呢，这个您这边有记录么，400GB 是怎么统计出来的呢

**客户**：220.197.226.20220.197.226.113111.55.35.10221.213.17.228	较多221.213.17.227	较多221.213.17.229221.213.17.230119.62.19.96119.62.21.165119.62.13.52119.62.48.161119.62.13.73119.62.48.41221.213.17.228221.213.17.227

**客户**：总共用过这些IP，400是刚才截的图上面有

**客户**：学生给的，其也有说异常+1的，但没给载图[图片]

**客服**：您好，这边先帮您检查下您的CDN 流量您也可以在 控制台 - cdn - 统计分析 - 日志分析 中看到您的top访问情况，比如高频访问的URL和客户端IP。https://***.qiniu.com/cdn/statistics/log/top[图片]

**客户**：确实有问题，这个人的某个常用IP，看了一个600M的视频，就产生了42G的流量[图片]

**客户**：另外插一个问题，如果一个教室10个人共用一个IP自然看完一个1G一小时的视频，是收1G的流量还是10G的流量呢

**客服**：您好，这个是收10G ，因为是10个设备在观看，如果10个人都通过一个大屏 观看 ，那么才是只请求1次，产生1G流量

**客户**：“您好，这边先帮您检查下您的CDN 流量”，这个查了怎么回事了吗

**客服**：您那边可以到https://***.qiniu.com/cdn/statistics/log/top查看这边具体的统计信息情况，后台看有几个视频文件访问量比较高

**客服**：您好，目前日志还在核实中，有结论再给您反馈

**客服**：你好，你们的这些视频都是从哪里获取的呢，这边将你们的视频下载到本地上传到存储测试后，发现你们的视频，在播放的过程中，会大量不断的加载资源，导致流量持续增长
你们尝试使用七牛的转码服务，将视频转成标准的mp4试试呢
https://***po.yzyw.cn/f6b8fc2fd7fb91645740f1e8c9ef29a1.mp4
你们可以找到这个文件然后验证下
[图片]

### 客服解答

你好，你们的这些视频都是从哪里获取的呢，这边将你们的视频下载到本地上传到存储测试后，发现你们的视频，在播放的过程中，会大量不断的加载资源，导致流量持续增长

### 根本原因分析

CDN缓存配置问题，需清理缓存或调整缓存策略

---

## 上传文件重复

**分类**：对象存储｜上传下载

### 问题描述

$uploadMgr = new UploadManager();list($ret, $err) = $uploadMgr->putFile($upToken, $fileKey, $file['tmp_name']);我使用以上代码上传文件，其中$fileKey值为2024-10-31/6722dd0340002.35100647.mp4，$file['tmp_name']值是testvideo.mp4。但是使用以上代码上传到七牛云的时候，空间里既有2024-10-31/6722dd0340002.35100647.mp4文件，又有testvideo.mp4文件，是什么原因导致的呢？

### 详细对话

**客户**：$uploadMgr = new UploadManager();list($ret, $err) = $uploadMgr->putFile($upToken, $fileKey, $file['tmp_name']);我使用以上代码上传文件，其中$fileKey值为2024-10-31/6722dd0340002.35100647.mp4，$file['tmp_name']值是testvideo.mp4。但是使用以上代码上传到七牛云的时候，空间里既有2024-10-31/6722dd0340002.35100647.mp4文件，又有testvideo.mp4文件，是什么原因导致的呢？[图片][图片]

**客服**：您好，看下上下文还有其他上传方法执行吗，理论上只会上传key值文件名，

**客户**：public function upload()    {        $session_uid = session('suid');        if (empty($session_uid)) {            $this->error('请登录！');        }        //获取用户积分        $duration = I("post.duration");        $userPoint = $this->getUserPoint($duration);        if (!$userPoint['isSufficient']) {            $this->error('积分不足！');        }        $file_name = "";  //原始文件名        if ($_FILES['file']['name']) {            //视频文件上传            $file = $_FILES['file'];            $file_name = $file['name'];            // 定义允许的视频扩展名            $allowedExtensions = ['mp4', 'mkv', 'flv', 'avi', 'wmv', 'mov', 'rmvb', 'ts', 'webm', 'ogg', 'mpeg'];            // 定义允许的视频 MIME 类型            $allowedMimeTypes = ['video/mp4', 'video/mkv', 'video/flv', 'video/avi', 'video/wmv', 'video/mov', 'video/rmvb', 'video/ts', 'video/webm', 'video/ogg', 'video/mpeg', "video/quicktime"];            // 获取文件扩展名            $fileExtension = strtolower(pathinfo($file_name, PATHINFO_EXTENSION));            // 获取文件 MIME 类型            $fileMimeType = $file['type'];            // 获取文件大小            $fileSize = $file['size'];            // 检查文件扩展名            if (!in_array($fileExtension, $allowedExtensions) || !in_array($fileMimeType, $allowedMimeTypes)) {                $this->error('文件不是视频类型！');            }            // 检查文件大小是否超过 300MB            if (!$fileSize) {                $this->error('无法获取视频大小！');            }            $sizeInMB = $fileSize / (1024 * 1024);            if ($sizeInMB > 300) {                $this->error('视频超过 300MB！');            }            //生成文件key            $fileKey = generateFileKey($file_name);            //生成七牛云token            $upToken *** $this->getUpToken();            // 上传文件到七牛云            $uploadMgr = new UploadManager();            list($ret, $err) = $uploadMgr->putFile($upToken, $fileKey, $file['tmp_name']);        } else {            $this->error('请先选择一个视频文件或输入一个视频链接！');        }        if ($err !== null) {            //上传失败            $this->error('视频上传失败，请稍后再试');        } else {            //上传成功            //存储视频            $data = [                "uid" => $session_uid,                "url" => "https://***deo.ju1.cn/" . $fileKey,  //视频地址                "file_name" => $file_name,  //原始文件名                "size" => number_format($sizeInMB, 2),  //视频大小，MB                "duration" => number_format($duration, 2),  //视频时长，秒                "points" => $userPoint['pointsRequired'],  //扣除积分                "user_points" => $userPoint['pointsRequired'],  //扣除积分                "add_time" => date("Y-m-d H:i:s"),   //添加时间            ];            $id = M("Video")->add($data);            if ($id) {                //签名的七牛云视频地址                $config = C("qiniu");                $auth = new Auth($config['accessKey'], $config['secretKey']);                $signedUrl = $auth->privateDownloadUrl("https://***eo2.ju1.cn/" . $fileKey);                //提交检测任务                $this->yidunSubmit($signedUrl, $id, $data['points']);            } else {                $this->error("存储失败！");            }        }    }后端只有这里有上传文件到七牛云的代码。前端也只有一个地方：$("#myModal").on("click", "#disableButtons", uploadVideo); //添加绑定  function uploadVideo() {    login();    const videoSrc = $videoPreview.attr("src");    if (selectedFile || (videoSrc && videoSrc.startsWith("http"))) {      var formData = new FormData();      formData.append("duration", duration);      if (selectedFile) {        // 上传选择文件        var fileInput = document.getElementById("videoUpload");        if (fileInput.files.length === 0) {          layer.msg("请选择一个文件！", { icon: 2 });          return;        }        var file = fileInput.files[0];        formData.append("file", file);      } else if (videoSrc && videoSrc.startsWith("http")) {        // formData.append("videoUrl", videoSrc);        var fileInput = document.getElementById("videoUpload");        var file = fileInput.files[0];        formData.append("file", file);      }      $("#myModal").off("click", "#disableButtons", uploadVideo); //解绑      uploadVideoFuc(formData, file);    } else {      layer.msg("请先选择一个视频文件或输入一个视频链接！", { icon: 2 });      $("#myModal").on("click", "#disableButtons", uploadVideo); //添加绑定      return;    }  }function uploadVideoFuc(formData, file) {    // 重置进度条    $("#progressBar").text("0%");    $("#progressBar").data("lastPercent", 0); // 重置 lastPercent    $modalClose.prop("disabled", true);    $("#disableButtons").prop("disabled", true);    $.ajax({      url: "/Video/upload",      type: "POST",      data: formData,      processData: false,      contentType: false,      beforeSend: function () {        $("#video_uploading").show();        $.get(          "/Video/ajaxGetQiniuToken",          function (res) {            const putExtra = {              fname: file.name,              params: {},            };            const config = {              region: qiniu.region.z0,            };            // 创建上传可观察对象            const observable = qiniu.upload(              file,              file.name,              res,              putExtra,              config            );            // 订阅上传事件            observable.subscribe({              next(response) {                updateProgress(response.total.percent.toFixed(2));              },              error: function(){                layer.msg("上传失败！", { icon: 2 });                return false              }            });          },          "json"        );      },      success: handleDetectionSuccess,      error: function (jqXHR, textStatus, errorThrown) {        console.error("Error:", textStatus, JSON.stringify(errorThrown));        layer.msg("上传失败！", { icon: 2 });      },    });  }和进度条有关系吗？

**客服**：后端putFile和前端qiniu.upload去掉一个，这两个都是上传。

**客户**：好的明白了，谢谢~

### 客服解答

后端putFile和前端qiniu.upload去掉一个，这两个都是上传。

### 根本原因分析

上传失败，需检查网络连接、文件大小限制或存储空间配置

---

## 证书配置时间长

**分类**：CDN｜证书问题

### 问题描述

您好，很长时间了没有配置成功https证书

### 详细对话

**客户**：您好，很长时间了没有配置成功https证书

**客服**：您好，还请耐心等待一下，这边确认一下

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

**客户**：为什么访问超级慢，基本加载不出来，麻烦您看一下，服务器没问题

**客服**：您好，您这边是国内访问还是海外访问呢？

**客户**：国内访问

**客户**：海外访问没有问题

**客服**：您这边将访问的链接给一下，这边看下

**客户**：https://***11chegg.cn/q?v=9035eef3-2674-4faf-a120-bea826b0cf15&o=23492192****0746972

**客服**：稍等这边确认一下

**客户**：麻烦尽快亲

**客服**：您好，这边已经为您优化了，您这边再看下

**客户**：好了好了 感谢啦

**客服**：嗯嗯好的不客气的

### 客服解答

嗯嗯好的不客气的

### 根本原因分析

CDN访问问题，可能涉及域名解析、缓存、或浏览器缓存问题

---

## 我刚充值的100元怎么没有到账呢？

**分类**：账户与财务｜其他类咨询

### 问题描述

我刚充值的100元怎么没有到账呢？

### 详细对话

**客户**：我刚充值的100元怎么没有到账呢？

**客服**：您好，请您提供充值回单，这边同步商务为您跟进处理。

### 客服解答

您好，请您提供充值回单，这边同步商务为您跟进处理。

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 证书无法下发

**分类**：CDN｜证书问题

### 问题描述

fs-test.7moor.comfs-mail-resource.7moor.comfs-im-resources.7moor.comrecord.7moor.comfs-ivr-music.7moor.comfs-km.7moor.comfs-im.7moor.com

### 详细对话

**客户**：fs-test.7moor.comfs-mail-resource.7moor.comfs-im-resources.7moor.comrecord.7moor.comfs-ivr-music.7moor.comfs-km.7moor.comfs-im.7moor.com

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

**客户**：好的，感谢，已经完成了

**客服**：嗯嗯好的不客气的

### 客服解答

嗯嗯好的不客气的

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 免费 from 自动催单

**分类**：CDN｜证书问题

### 问题描述

长时间处于免费证书申请环节

### 详细对话

**客户**：长时间处于免费证书申请环节

**客服**：您好，域名已经处理完成了

### 客服解答

您好，域名已经处理完成了

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 你好，麻烦通知一下负责我们账号的商务同学，联系我一下

**分类**：账户与财务｜其他类咨询

### 问题描述

你好，麻烦通知一下负责我们账号的商务同学，联系我一下这个号码 [REDACTED_PHONE]

### 详细对话

**客户**：你好，麻烦通知一下负责我们账号的商务同学，联系我一下这个号码 [REDACTED_PHONE]

**客服**：您好，好的

### 客服解答

您好，好的

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 修改 HTTPS 配置处理中，免费证书申请耗时相对较长，平均 15 分钟完成，期间域名访问不受影响，部分配置不可修改，若长时间未配置完成，请提交工单反

**分类**：对象存储｜其他类咨询

### 问题描述

修改 HTTPS 配置处理中，免费证书申请耗时相对较长，平均 15 分钟完成，期间域名访问不受影响，部分配置不可修改，若长时间未配置完成，请提交工单反

### 详细对话

**客户**：修改 HTTPS 配置处理中，免费证书申请耗时相对较长，平均 15 分钟完成，期间域名访问不受影响，部分配置不可修改，若长时间未配置完成，请提交工单反

**客户**：已经半个小时了

**客户**：为什么上传了不附件工单，显示上传失败

**客服**：您好，请稍等，这边帮您确认下

**客户**：已经半个小时了[图片]

**客服**：您好，已处理完成，您确认下

### 客服解答

您好，已处理完成，您确认下

### 根本原因分析

上传失败，需检查网络连接、文件大小限制或存储空间配置

---

## ssl证书已经续费,到期时间还是原来的时间

**分类**：对象存储｜其他类咨询

### 问题描述

域名: lai.file.tsinghuacloud.cnssl证书已经续费,到期时间还是原来的时间

### 详细对话

**客户**：域名: lai.file.tsinghuacloud.cnssl证书已经续费,到期时间还是原来的时间[图片][图片]

**客服**：证书需要 补全信息-域名归属验证-之后审核签发部署域名订单管理中找到您购买的订单进行操作：https://***.qiniu.com/certificate/ssl#order

**客户**：文件校验一直验证不了https://***uacloud.cn/.well-known/pki-validation/2556199731919F8B323E1FB5E6094C97.txt

**客服**：稍等

**客服**：您好，这边查看订单已完成了，您确认下呢

### 客服解答

您好，这边查看订单已完成了，您确认下呢

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## node 上传视频

**分类**：对象存储｜上传下载

### 问题描述

上传报错

### 详细对话

**客户**：上传报错

**客服**：您好，您这边上传报错是什么

**客户**：https://***.zjcdn.com/c89b42e4c2bca875b5e09e42df86661b/67231466/video/tos/cn/tos-cn-ve-15/osfOdj7gBBDQPhcE1pFyfISpBCBOEACq0fQEEA/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=703&bt=703&cs=0&ds=3&ft=CZcaELO_DDhNF5VQ9wF6Q4ahd.W8xbP03-ApQX&mime_type=video_mp4&qs=0&rc=O2k5OjY8OTNkZjY8aDs3NkBpM3l5NG85cnF0djMzNGkzM0A0XjViL2EyX2MxM2JfMV40YSMuMGwuMmRzYGRgLS1kLS9zcw%3D%3D&btag=80000e00010000&cc=1f&cquery=100o_100w_100B_100H_100K&dy_q=1730341415&feature_id=aa7df520beeae8e397df15f38df0454c&l=20241031102335961E2C4B5A9E9D01EA98&req_cdn_type=

**客户**：我上传的是一个视频链接地址

**客服**：你好，是进行的链接抓取是吗，您这边抓取有什么报错吗？视频的话，建议使用异步抓取参考文档https://***.qiniu.com/kodo/4097/asynch-fetch

**客户**：是的 我抓取的视频数据 视频的链接已经抓取到了

**客户**：截图[图片]

**客服**：您好，抓取到本地，然后本地上传？看起来像是本地没有这个文件

**客户**：解决了不用本地存储

**客服**：您好，好的

### 客服解答

您好，好的

### 根本原因分析

上传失败，需检查网络连接、文件大小限制或存储空间配置

---

## 海外站点如何配置CDN

**分类**：CDN｜其他类咨询

### 问题描述

我的服务器在德国法兰克福，有3个域名解析到不同语言站，有个.cn的在国内做了备案，其他没有，现在需要对网站的大图片进行cdn处理，我想的是直接做个存储，然后再做cdn，但是你们的存储海外的我觉得适合的只有北美洛杉矶的，我觉得比较远，会不会对我关注地欧洲地区访问会出现慢的情况？？还有一个方案就是直接对站点做cdn，缓存配置只缓存图片，但是你们需要填备案的域名，我另外两个域名没有备案。请问我该如何选择？？感谢，希望能电话沟通

### 详细对话

**客户**：我的服务器在德国法兰克福，有3个域名解析到不同语言站，有个.cn的在国内做了备案，其他没有，现在需要对网站的大图片进行cdn处理，我想的是直接做个存储，然后再做cdn，但是你们的存储海外的我觉得适合的只有北美洛杉矶的，我觉得比较远，会不会对我关注地欧洲地区访问会出现慢的情况？？还有一个方案就是直接对站点做cdn，缓存配置只缓存图片，但是你们需要填备案的域名，我另外两个域名没有备案。请问我该如何选择？？感谢，希望能电话沟通

**客服**：您好，域名接入国内的话，你们需要用 备案域名接入，然后回源国内服务器效果会更好一点CDN使用纯海外加速，回源你们的站点，对站点整体加速，纯海外加速域名不需要备案你们这个最好是国内 和 国外的域名服务分开，北美存储的话，国内访问同样域名也得备案的

**客户**：我们不需要国内能多快去访问，国内可能只是进到后台上传一些东西“CDN使用纯海外加速，回源你们的站点，对站点整体加速，纯海外加速域名不需要备案”我使用这个方案的话，我国内还能打开我的站点吗

**客户**：我选择海外，但他还是提示我填写备案域名[图片]

**客服**：您好“CDN使用纯海外加速，回源你们的站点，对站点整体加速，纯海外加速域名不需要备案”
我使用这个方案的话，我国内还能打开我的站点吗 
您好，这个打不开的概率很高，国内访问效果极差的，如果域名回源无法创建，只能选海外存储 + 纯海外加速对空间资源加速处理了

**客户**：那其实就是我说的，做洛杉矶存储，然后做海外cdn加速，那就回到最开始的问题，我的服务器在法兰克福，那么我欧洲地区的用户访问会不会慢，能达到加速的效果吗

**客服**：您好，这个没问题的，有加速效果，不会慢的，北美存储就是给欧美访问使用的

**客户**：我cdn选的海外，那我国内访问是什么效果呢，直接从我服务器走吗，不走你们cdn是吧？然后存储和cdn资源包我该如何购买

**客服**：海外CDN ，国内无法访问，你们国内可能要直接走你们服务器了存储资源包购买标准存储资源包 https://***.qiniu.com/template/MTEy?spec_combo=MzA0Ng&ref=indexCDN购买海外流量资源包https://***.qiniu.com/template/NTU?ref=category&ref=index&spec_combo=MjE3Ng

**客户**：存储资源包我不应该是买海外的吗 不然怎么创建洛杉矶的

**客服**：您好，海外当前暂时没有存储资源包，非常抱歉，存储先不买资源包，买CDN海外资源包即可

**客户**：我一直不明白一个问题，就是我用国外存储，用国外cdn，国内访问我这个资源是看得到还是看不到？费用怎么收费的？我的诉求是，一个域名，全球都能访问，用国外存储，国外cdn，国内我不希望他走cdn，直接走回源

**客服**：您好1：国外存储，国外CDN ，国内能访问，但是失败的多，访问到的流量，按照海外流量计算，因为是海外CDN节点ip响应了资源2：一个域名，全球都能访问，用国外存储，国外cdn，国内我不希望他走cdn，直接走回源 ，这个当前不支持的，非常抱歉这个只能启用两个不同的域名分开的

**客户**：国外存储，cdn我买全球的呢

**客户**：还有一个方案就是，我用全球的cdn，加速全站，那么我的域名需要备案吗

**客服**：你好，全球CDN 涉及到了国内加速，域名就需要备案了

### 客服解答

你好，全球CDN 涉及到了国内加速，域名就需要备案了

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 访问不稳定

**分类**：CDN｜访问下载

### 问题描述

网络会有中断，这个是怎么回事呢

### 详细对话

**客户**：网络会有中断，这个是怎么回事呢[图片]

**客服**：您好，客户端ip，请求url，请求时间麻烦提供下

**客户**：客户端是美国的，请求时间不固定的示例地址如下https://***ess.com.cn//WaybillFiles/DeliveryLabel/20241023/92612903033497543475167389.pdfhttps://***ess.com.cn//WaybillFiles/DeliveryLabel/20241023/92612903033497543475167457.pdfhttps://***ess.com.cn//WaybillFiles/DeliveryLabel/20241023/92612903033497543475167464.pdfhttps://***ess.com.cn//WaybillFiles/DeliveryLabel/20241023/92612903033497543475167501.pdfhttps://***ess.com.cn//WaybillFiles/DeliveryLabel/20241023/92612903033497543475167839.pdf

**客服**：您好，出现异常的时间段需要给下，这边根据日志查看

**客户**：时间段大概是中国时间2024-10-30 22点45分左右

**客服**：好的，稍等

**客服**：您好，客户端能麻烦ping jgwy.goodexpress.com.cn 获取下连接ip提供这边确认下吗，这边看美国的客户端ip请求的都是国内的节点ip，可能是是设备端本地dns不符合预期。

**客户**：dns是感觉有点问题，从我们服务器访问有时到了美国，有时到了德国，我们服务器访问到德国的时候很有可能会超时[图片]

**客服**：本地dns修改到8.8.8.8后观察下试试

**客户**：我们这个是仓库操作的面单，仓库的人都不会操作的，有其他解决方案吗

**客服**：您好，需要客户端调整下的，这个主要是客户端问题，都得在客户端调整。

**客户**：你们有香港的空间没

**客服**：没有的，目前支持这些的[图片]

**客户**：客户那边是服务器，不能设置dns，怎么弄呢

**客服**：服务器也可以设置dns的，哪个系统的可以百度搜下调整方式。

### 客服解答

服务器也可以设置dns的，哪个系统的可以百度搜下调整方式。

### 根本原因分析

CDN访问问题，可能涉及域名解析、缓存、或浏览器缓存问题

---

## 忘记怎么更改密码

**分类**：对象存储｜其他类咨询

### 问题描述

忘记怎么更改密码

### 详细对话

**客户**：忘记怎么更改密码

**客服**：您好，退出登录后，可在登录页面下方「忘记密码」处，通过账号绑定的手机号或邮箱重置密码[图片]

**客户**：好的

### 客服解答

您好，退出登录后，可在登录页面下方「忘记密码」处，通过账号绑定的手机号或邮箱重置密码[图片]

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 中断处理

**分类**：CDN｜配置问题

### 问题描述

麻烦把这个处理中断下，已经配置2天了还没好

### 详细对话

**客户**：麻烦把这个处理中断下，已经配置2天了还没好[图片]

**客服**：稍等

**客服**：您好，已取消

### 客服解答

您好，已取消

### 根本原因分析

配置相关问题，需要调整或优化系统配置

---

## cdn访问不了

**分类**：CDN｜访问下载

### 问题描述

images.cdsb.com这个域名下的所有文件访问不了,

### 详细对话

**客户**：images.cdsb.com这个域名下的所有文件访问不了,[图片]

**客户**：刚好了下，又不行了[图片]

**客服**：您好，这边测试来看是没有问题的，您这边使用无痕浏览再看下呢？[图片]

**客户**：客服呢

**客户**：我和你不是同个节点啊，我都没法ping通

**客户**：[图片]还是超时

**客服**：您好，您这边刷新一下本地dns缓存看下，您请求的这个节点已经下掉了的，您这边应该是请求到该节点的dns缓存上了，刷新一下本地dns缓存后再看下

**客户**：不但是我这个地址，这栋楼 好多都访问不了

**客服**：这个节点可以明确的是已经下线了的，您可以将其他无法访问的节点给一下这边看下的，您这边刷新一下dns本地缓存一下就好了的

**客户**：a[图片]你说的这个节点下线了，但是现在可以访问了。我们成都服务器和杭州服务器，都是这个节点的问题

**客服**：嗯嗯所以说您这边请求到这个下线节点的dns缓存上了现在，这个已经操作下线了，﻿您现在刷新下本地dns缓存后刷新掉这个节点的缓存，然后重新请求到别的节点IP上就能恢复了

**客户**：[图片]现在换成了这个

**客服**：您好，这个是优化后的正常的节点的，您目前测试看下是否正常的

**客户**：请问后续还会出现这个问题吗。这个周都出现过几次了，有时几分钟，有时10多分钟，很影响体验

**客服**：您好，正常情况是不会的了，这边已经优化到了别的节点IP段上了的

### 客服解答

您好，正常情况是不会的了，这边已经优化到了别的节点IP段上了的

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 刚才购买了cdn,但是 钱扣了,订单状态确是未支付

**分类**：账户与财务｜计费问题

### 问题描述

刚才购买了cdn,但是 钱扣了,订单状态确是未支付

### 详细对话

**客户**：刚才购买了cdn,但是 钱扣了,订单状态确是未支付

**客户**：订单0934de5e22b9455841617841e29a6588

**客服**：您好，您稍等这边帮您确认一下

**客服**：您好，您这边麻烦辛苦留一下您的联系方式，这边反馈商务经理与您联系确认一下

**客户**：怎么样了

**客户**：[REDACTED_EMAIL]这个很简单啊,我购买了东西没收到,钱还给我扣了,肯定说你们这边出问题了啊

**客服**：您好，麻烦辛苦留一下您的电话或微信，这边让商务经理帮你确认一下，我这边技术，看不到您的账单和费用的相关情况的，需要商务经理介入确认一下的

**客户**：[图片]你看嘛,充值通知

**客户**：加我微信:woody113322

**客服**：您好，嗯嗯好的还请耐心等待一下

**客户**：1[图片]

**客服**：您好，嗯嗯好的这边确认中的

**客户**：怎么还没好啊,按理说这么基础的东西你们不应该出故障啊

**客服**：您好，还请耐心等待一下的，这边已经反馈产品确认中的，我们工单这边看不到这些信息的，只能等他们这边确认看下的

**客户**：怎么还没好?

**客服**：产品还未回复，这边催下

**客服**：您好，目前产品反馈查下来，钱确实扣了，但是订单状态没改，您这边看下能否接受先退款，再重新购买。如果可以的，我们这边为您处理下

**客户**：可以,直接退款到我的七牛账号

**客服**：您好，这边反馈已经退回到您的账号余额了的，您这边重新下单即可

### 客服解答

您好，这边反馈已经退回到您的账号余额了的，您这边重新下单即可

### 根本原因分析

计费或费用相关咨询

---

## 资源包类型购买错误

**分类**：对象存储｜其他类咨询

### 问题描述

订单号62a1c03fb9fc0e224c22ce720f348ee7

### 详细对话

**客户**：订单号62a1c03fb9fc0e224c22ce720f348ee7

### 客服解答

问题记录中，等待客服响应

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 协议降级https 转 http

**分类**：CDN｜配置问题

### 问题描述

麻烦把这两个域名www.xxmzzyy.com与xxmzzyy.com 的协议降为http

### 详细对话

**客户**：麻烦把这两个域名www.xxmzzyy.com与xxmzzyy.com 的协议降为http

**客服**：您好，很抱歉，月底无法操作降级，您可以等到下个月5号之后提交工单调整

**客户**：好的

**客服**：您好，有什么问题您再反馈

### 客服解答

您好，有什么问题您再反馈

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 添加加速域名一直是处理中的状态

**分类**：对象存储｜其他类咨询

### 问题描述

添加加速域名一直是处理中，已经30分钟了

### 详细对话

**客户**：添加加速域名一直是处理中，已经30分钟了

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

**客户**：好的，谢谢。这边显示已经正常了

### 客服解答

您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 图片都访问不到了

**分类**：对象存储｜其他类咨询

### 问题描述

图片都访问不到了

### 详细对话

**客户**：图片都访问不到了

**客服**：您好，麻烦您提供一个具体的无法访问的图片链接，这边帮你们确认下

**客户**：https://***huihua.com/main/about.mp4

**客户**：这个空间所有的东西都看不到，在七牛云也不行

**客户**：你先确认下是你们的问题还是我们的问题

**客服**：您好，已经可以观看，这个是监控到节点有抖动，已下线节点，您这边是有DNS缓存访问到非预期旧节点，您再试试

### 客服解答

您好，已经可以观看，这个是监控到节点有抖动，已下线节点，您这边是有DNS缓存访问到非预期旧节点，您再试试

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 一直在配置两天了

**分类**：CDN｜配置问题

### 问题描述

一直在配置什么的

### 详细对话

**客户**：一直在配置什么的

**客服**：稍等

**客服**：您好，您这边有个免费证书任务，需要重新提交下，历史任务超时了。

### 客服解答

您好，您这边有个免费证书任务，需要重新提交下，历史任务超时了。

### 根本原因分析

SSL证书配置问题，需检查证书状态和HTTPS配置

---

## 几个月前上传的文件存储现在打不开了

**分类**：对象存储｜上传下载

### 问题描述

https://***ucciot.com/uploads/20240725/QT3Rwtb12neKP4jxlrAMs0aucEOkd5pZ.mp4之前上传的文件现在打不开了 急急急！！！！

### 详细对话

**客户**：https://***ucciot.com/uploads/20240725/QT3Rwtb12neKP4jxlrAMs0aucEOkd5pZ.mp4之前上传的文件现在打不开了 急急急！！！！

**客服**：您好，1、麻烦提供下用户的 ip、dns 信息，和cdn节点信息，这边代理测试下可以通过访问这个链接 https://***tuo.qq.com/ 获取本地的 ip 和 dns 信息，在检测域名这边输入下cdn域名，点击提交检测，然后截图通过工单提交给我们[图片]2、建议让用户使用 chrome 浏览器，按照下述文档获取下 remote adress(对端节点ip)，request header(客户端请求头) 以及 response header(服务端响应头)信息，方便我们查询分析问题。https://***.qiniu.com/fusion/kb/1478/how-to-access-network-in-the-browser-request-information

**客户**：突然又好了 怎么回事啊

**客服**：您好，您这边是否是网络原因，这边看是正常的

### 客服解答

您好，您这边是否是网络原因，这边看是正常的

### 根本原因分析

需要配置合适的上传策略和工具

---

## 存储桶内视频地址打不开

**分类**：对象存储｜其他类咨询

### 问题描述

https://***dichat.com/acce2c7197****765300d9a4e7cae56e.mp4

### 详细对话

**客户**：https://***dichat.com/acce2c7197****765300d9a4e7cae56e.mp4

**客户**：存储桶内的文件通过外链都访问不到

**客服**：您好，当前已经可以了，您再试试呢

### 客服解答

您好，当前已经可以了，您再试试呢

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 图片访问慢，加载不出来

**分类**：对象存储｜上传下载

### 问题描述

图片访问慢，加载不出来，有时候很小的图片也要加载5秒以上

### 详细对话

**客户**：图片访问慢，加载不出来，有时候很小的图片也要加载5秒以上

**客户**：[图片]成功访问 ：https://***iyuyfs.com/upload/2024-08-13/ae77d7b923cfa60938b291ed54ade6eea7625fae.png   用时1分钟访问失败 https://***iyuyfs.com/static/img/index/sy***@***

**客户**：现在可以访问了，但是时间还是很慢[图片]

**客服**：稍等，这边看下

**客服**：您好经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您清理下客户端dns缓存，稍后再观察看看

### 客服解答

您好经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您清理下客户端dns缓存，稍后再观察看看

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 使用laravel框架编写的程序，上传文件大于2M以上就提示"Path cannot be empty"其他均正常，请帮忙核实是否为七牛云有限制？

**分类**：对象存储｜上传下载

### 问题描述

使用laravel框架编写的程序，上传文件大于2M以上就提示"Path cannot be empty"其他均正常，请帮忙核实是否为七牛云有限制？

### 详细对话

**客户**：使用laravel框架编写的程序，上传文件大于2M以上就提示"Path cannot be empty"其他均正常，请帮忙核实是否为七牛云有限制？

**客服**：你好，这个报错不是这边的报错，存储这边默认不做任何限制的，这个看起来是第三方插件的报错

**客户**：好的

**客服**：好的

### 客服解答

好的

### 根本原因分析

上传失败，需检查网络连接、文件大小限制或存储空间配置

---

## 网站经常不能访问

**分类**：CDN｜其他类咨询

### 问题描述

www.zuhaoguanjia.com这个域名发生经常不能访问，但是zuhaoguanjia.com可以访问我这两个都是通过七牛的，可以帮我查一下是什么原因吗？

### 详细对话

**客户**：www.zuhaoguanjia.com这个域名发生经常不能访问，但是zuhaoguanjia.com可以访问我这两个都是通过七牛的，可以帮我查一下是什么原因吗？

**客服**：稍等，这边查下

**客服**：您好经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您清理下客户端dns缓存，稍后再观察看看

**客户**：我的网站有的用户打不开，有的打的开。我的服务器没问题，通过ip是可以打开的。但是用户通过域名有少部分就打不开。

**客服**：稍等，这边看下

**客服**：您好，异常的网页地址麻烦提供下呢，这边检查下

**客户**：www.zuhaoguanjia.comwww.zuhaoguanjia.cn

**客服**：您好，域名整体看有部分源站的5xx状态码，异常访问的客户端ip能麻烦提供下吗

**客户**：现在我的www.zuhaoguanjia.com不能访问但是www.zuhaoguanjia.cn可以访问帮我查一下

**客服**：您好这边测试是正常的，您那边无法访问的客户端ip、CDN节点ip和错误状态码等信息给下，这边具体看下[图片]

### 客服解答

您好这边测试是正常的，您那边无法访问的客户端ip、CDN节点ip和错误状态码等信息给下，这边具体看下[图片]

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 域名配置一直显示"处理中"

**分类**：CDN｜配置问题

### 问题描述

域名配置一直显示"处理中"

### 详细对话

**客户**：域名配置一直显示"处理中"

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

### 客服解答

您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 域名长时间配置未生效

**分类**：CDN｜配置问题

### 问题描述

CNAME：jzkwxyycs-zmdmajiang-com-idvoyky.qiniudns.com

### 详细对话

**客户**：CNAME：jzkwxyycs-zmdmajiang-com-idvoyky.qiniudns.com

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客户**：还有一个域名：jzkwxfk.ctyoyo.comCNAME：jzkwxfk-ctyoyo-com-idvoyl1.qiniudns.com

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

**客户**：已经好了，感谢。

### 客服解答

您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 更换了CDN域名要怎么处理才能把所有文件打开

**分类**：对象存储｜其他类咨询

### 问题描述

更换了CDN域名要怎么处理才能把所有文件打开

### 详细对话

**客户**：更换了CDN域名要怎么处理才能把所有文件打开

**客服**：您好，您这边创建域名后配置cname绑定之前的存储空间后即可正常访问的

### 客服解答

您好，您这边创建域名后配置cname绑定之前的存储空间后即可正常访问的

### 根本原因分析

配置相关问题，需要调整或优化系统配置

---

## 资源访问不到

**分类**：对象存储｜其他类咨询

### 问题描述

资源经常访问不到

### 详细对话

**客户**：资源经常访问不到

**客服**：您好，无法访问的链接提供下，这边看下

### 客服解答

您好，无法访问的链接提供下，这边看下

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## static.k366.com域名下的资源访问不了

**分类**：CDN｜访问下载

### 问题描述

static.k366.com域名下的所有资源都加载不了

### 详细对话

**客户**：static.k366.com域名下的所有资源都加载不了

**客服**：您好，麻烦提供下您的 ip、dns 信息，和cdn节点信息，这边代理测试下可以通过访问这个链接 https://***tuo.qq.com/ 获取本地的 ip 和 dns 信息，在检测域名这边输入下cdn域名，点击提交检测，然后截图通过工单提交给我们[图片]

**客户**：11点多已经切到阿里cdn了

**客户**：你们七牛，怎么越来越不稳定了啊，时不时出点问题

**客户**：工单问你们一些问题，不是提供这个就提供那个，你们能不能再专业一点？

**客服**：您好，因为您提交的时候这边可以访问的，想看下您请求的节点信息，这边代理测试看下

### 客服解答

您好，因为您提交的时候这边可以访问的，想看下您请求的节点信息，这边代理测试看下

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## SSL证书已部署，要多久生效？目前访问文件，还是提示安全问题。

**分类**：对象存储｜其他类咨询

### 问题描述

域名：wechatfiles.wanfuwa.com.cn

### 详细对话

**客户**：域名：wechatfiles.wanfuwa.com.cn

**客服**：您好，请稍等

**客服**：你好，当前测试已经没有问题，你们确认下呢

### 客服解答

你好，当前测试已经没有问题，你们确认下呢

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 充值活动

**分类**：账户与财务｜其他类咨询

### 问题描述

你好，请问充值送抵扣券这个活动，抵扣券什么时间到账？能帮我催一下吗，要买服务了

### 详细对话

**客户**：你好，请问充值送抵扣券这个活动，抵扣券什么时间到账？能帮我催一下吗，要买服务了

**客服**：您好，充值后 7 天内到账哈

**客户**：能帮我催一下吗，要买服务了

**客服**：您好，已帮您加急催促了哈

### 客服解答

您好，已帮您加急催促了哈

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 标准存储包购买后没有正常抵扣

**分类**：对象存储｜其他类咨询

### 问题描述

标准存储包买了2.6T，仅抵扣了 1.8T，实时消费明细还有 0.8T没有抵扣

### 详细对话

**客户**：标准存储包买了2.6T，仅抵扣了 1.8T，实时消费明细还有 0.8T没有抵扣

**客服**：您好，您的存储这边有华东华南的，资源包抵扣这两个区域系数不同，华东这边是存储使用1g，资源包需要抵扣1.2g的是不是资源包使用完了[图片]

**客户**：我买的是 全国通用包，和地区没关系

**客户**：怎么还有这种规则？？ 我再核查一遍吧

**客服**：您好，是的，全国通用，但是抵扣系数不同，存储不同区域收费不一样，所以资源包这边抵扣系数也是不同的

**客户**：fe0ae0fa021ddac69f7e6266b7614d18  这笔订单什么时间能生效？目前没有抵扣效果

**客户**：外网流量订单

**客服**：你好，您是多久购买的？这边截图看下呢https://***.qiniu.com/financial/respack-mgr/current

### 客服解答

你好，您是多久购买的？这边截图看下呢https://***.qiniu.com/financial/respack-mgr/current

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 储存空间的解析地址

**分类**：CDN｜其他类咨询

### 问题描述

储存空间的那个解析地址在哪里找

### 详细对话

**客户**：储存空间的那个解析地址在哪里找

**客服**：您好，请问您具体是哪个域名需要做cname解析呢

**客户**：cdn.ymtff.cn    这个

**客服**：你好，主机记录 cdn ，记录类型 cname ，记录值 cdn-ymtff-cn-idvoir6.qiniudns.com

**客户**：为什么我已经配置了，还是显示没配置成功的[图片]

**客服**：记录值不对 应该是cdn-ymtff-cn-idvoir6.qiniudns.com
[图片]

**客户**：现在显示可以了，为什么视频还是打不开

**客服**：哪个视频打不开 给下链接

**客户**：https://***n.ymtff.cn/172****929000.mp4https://***n.ymtff.cn/172****909000.mp4这两个都打不开，急死人了，处理了2天都搞不定

**客户**：可以了谢谢哥

### 客服解答

哪个视频打不开 给下链接

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 我要修改私有空间为公开，但是出错了

**分类**：对象存储｜其他类咨询

### 问题描述

下面是出错的信息[    [        {            "title": "请求 ID",            "content": "nQngjwgYfbedbAMY"        },        {            "title": "日志栈",            "content": "PORTAL-PROXY:51/500"        }    ],    [        {            "title": "请求 ID",            "content": "nQngjwgYfbedbAMY"        },        {            "title": "日志栈",            "content": "PORTAL-PROXY:51/500"        }    ]]

### 详细对话

**客户**：下面是出错的信息[    [        {            "title": "请求 ID",            "content": "nQngjwgYfbedbAMY"        },        {            "title": "日志栈",            "content": "PORTAL-PROXY:51/500"        }    ],    [        {            "title": "请求 ID",            "content": "nQngjwgYfbedbAMY"        },        {            "title": "日志栈",            "content": "PORTAL-PROXY:51/500"        }    ]]

**客户**：估计你们暂时解决不了，请先帮我把xueqiyi的那个空间改成公开空间。

**客服**：你好，麻烦稍等下，正在处理了

**客服**：您好，已恢复，测试能够正常修改了，您再提交试下

**客户**：非常感谢，已经可以了。

### 客服解答

您好，已恢复，测试能够正常修改了，您再提交试下

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 丢失文件怎么找回

**分类**：对象存储｜其他类咨询

### 问题描述

原本上传的文件生成二维码，现在二维码扫不出原本上传的链接，怎么办？然后上传过的文件后期删除掉了怎么恢复

### 详细对话

**客户**：原本上传的文件生成二维码，现在二维码扫不出原本上传的链接，怎么办？然后上传过的文件后期删除掉了怎么恢复

**客户**：请及时解决

**客服**：您好，已删除的文件无法找回的，非常抱歉

### 客服解答

您好，已删除的文件无法找回的，非常抱歉

### 根本原因分析

空间文件数量大，需通过qshell批量删除工具提高效率

---

## 控制台或者什么工具可以直接将文件夹上传到对象存储中

**分类**：对象存储｜上传下载

### 问题描述

控制台或者什么工具可以直接将文件夹上传到对象存储中

### 详细对话

**客户**：控制台或者什么工具可以直接将文件夹上传到对象存储中

**客服**：您好您可以使用最新的图形化工具kodo-browser上传试下，支持拖动文件夹到工具页面，批量上传。https://***.qiniu.com/kodo/tools/5972/kodo-browser

### 客服解答

您好您可以使用最新的图形化工具kodo-browser上传试下，支持拖动文件夹到工具页面，批量上传。https://***.qiniu.com/kodo/tools/5972/kodo-browser

### 根本原因分析

需要配置合适的上传策略和工具

---

## cname配置失败

**分类**：对象存储｜其他类咨询

### 问题描述

在阿里云域名服务里面配置的，主机记录和记录值都是七牛提供的iovip-z0.qiniuio.com，没其他参数了

### 详细对话

**客户**：在阿里云域名服务里面配置的，主机记录和记录值都是七牛提供的iovip-z0.qiniuio.com，没其他参数了[图片]

**客服**：主机记录是域名前缀，您看下您域名前缀是什么

**客户**：什么意思，是自定义的还是空间绑定时填的域名，我在空间绑定填的没加前缀，是不是要加www这种

**客服**：没有前缀的话主机记录就填@参考这个文档https://***.qiniu.com/fusion/4941/cname-configuration

### 客服解答

没有前缀的话主机记录就填@参考这个文档https://***.qiniu.com/fusion/4941/cname-configuration

### 根本原因分析

配置相关问题，需要调整或优化系统配置

---

## 存储的视频问题

**分类**：对象存储｜其他类咨询

### 问题描述

存储的视频外链导入的系统中手机端能够正常播放，pc端无法播放.是我这边七牛云空间配置的不对，还是我服务器代码端的问题。我现在识别不出来，帮我看看截图。谢谢

### 详细对话

**客户**：存储的视频外链导入的系统中手机端能够正常播放，pc端无法播放.是我这边七牛云空间配置的不对，还是我服务器代码端的问题。我现在识别不出来，帮我看看截图。谢谢[图片]

**客服**：您好，您这边将访问链接给一下这边这边看下

**客户**：https://***sxhcwh.com/home/View/play/fid/40/aid/150.html

**客服**：您好，您这边给您的域名部署一下SSL证书后再看下，目前看只是http协议，无法放到https协议的网站下使用的

**客户**：我把网站的ssl证书关闭了。使用http协议访问网站，还是不能播放

**客服**：这边测试播放文件是可以正常播放的，应该是您的网站或者播放器有问题导致的，您可以使用其他播放器或者ffplay命令播放看下1https://***sxhcwh.com/1%E3%80%81%E6%90%AD%E5%BB%BA996%E5%BC%95%E6%93%8E%E6%9C%AC%E5%9C%B0%E6%95%B0%E6%8D%AE%E5%BA%93%E5%8D%95%E6%9C%BA%E7%8E%AF%E5%A2%83.mp4-cqhaha123.m3u8[图片]

**客户**：好的，我再试试

**客服**：嗯嗯好的

**客户**：我使用vlc网络串流试了一下。播放不了，我把外链又用了MP4的可以播放。m3u8后缀的外链就不能播放[图片][图片]

**客服**：这边使用ffplay测试是可以的，这个是不支持的，您这边可以使用ffplay命令测试一下的ffplay 'https://***sxhcwh.com/1%E3%80%81%E6%90%AD%E5%BB%BA996%E5%BC%95%E6%93%8E%E6%9C%AC%E5%9C%B0%E6%95%B0%E6%8D%AE%E5%BA%93%E5%8D%95%E6%9C%BA%E7%8E%AF%E5%A2%83.mp4-cqhaha123.m3u8'

### 客服解答

这边使用ffplay测试是可以的，这个是不支持的，您这边可以使用ffplay命令测试一下的ffplay 'https://***sxhcwh.com/1%E3%80%81%E6%90%AD%E5%BB%BA996%E5%BC%95%E6%93%8E%E6%9C%AC%E5%9C%B0%E6%95%B0%E6%8D%AE%E5%BA%93%E5%8D%95%E6%9C%BA%E7%8E%AF%E5%A2%83.mp4-cqhaha123.m3u8'

### 根本原因分析

配置相关问题，需要调整或优化系统配置

---

## 如何下载文件

**分类**：对象存储｜上传下载

### 问题描述

如何下载空间的文件，没有下载链接。临时下载使用。

### 详细对话

**客户**：如何下载空间的文件，没有下载链接。临时下载使用。

**客服**：您好，您可以使用最新的图形化工具kodo-browser上传/下载试下，支持批量管理。https://***.qiniu.com/kodo/tools/5972/kodo-browser注意：使用该工具目前进行上传/下载，如果不指定cdn域名的话，下载产生的流量费用为「外网流量」

**客户**：[图片]裁剪缩放不能居中等比缩放吗，裁掉多余的部分。如图所示，放大后按照720*1280裁剪

**客户**：原视频，裁剪成720*1280，居中方大后裁剪[图片]

**客服**：您好，可以的，您看下对象存储空间的多媒体样式内的图片处理的[图片]

**客户**：视频裁剪，不是图片

**客服**：视频裁剪的话目前是没有对应参数可以支持的，十分抱歉

### 客服解答

视频裁剪的话目前是没有对应参数可以支持的，十分抱歉

### 根本原因分析

需要配置合适的上传策略和工具

---

## 鸿蒙 sdk 上传图片报错

**分类**：对象存储｜SDK使用

### 问题描述

调用方法：createMultipartUploadV1Task{"name":"HttpRequestError","message":"no such bucket","reqId":"mbMAAADGslcIbQMY","stack":"    at UploadError (oh_modules/.ohpm/@qiniu+upload@1.0.2/oh_modules/@qiniu/upload/src/main/ets/components/@internal/types/error.ts:13:18)\n    at HttpRequestError (oh_modules/.ohpm/@qiniu+upload@1.0.2/oh_modules/@qiniu/upload/src/main/ets/components/@internal/types/error.ts:19:5)\n    at handleResponseError (oh_modules/.ohpm/@qiniu+upload@1.0.2/oh_modules/@qiniu/upload/src/main/ets/components/@internal/api/index.ts:154:21)\n    at mkfile (oh_modules/.ohpm/@qiniu+upload@1.0.2/oh_modules/@qiniu/upload/src/main/ets/components/@internal/api/index.ts:386:14)\n","httpCode":631}

### 详细对话

**客户**：调用方法：createMultipartUploadV1Task{"name":"HttpRequestError","message":"no such bucket","reqId":"mbMAAADGslcIbQMY","stack":"    at UploadError (oh_modules/.ohpm/@qiniu+upload@1.0.2/oh_modules/@qiniu/upload/src/main/ets/components/@internal/types/error.ts:13:18)\n    at HttpRequestError (oh_modules/.ohpm/@qiniu+upload@1.0.2/oh_modules/@qiniu/upload/src/main/ets/components/@internal/types/error.ts:19:5)\n    at handleResponseError (oh_modules/.ohpm/@qiniu+upload@1.0.2/oh_modules/@qiniu/upload/src/main/ets/components/@internal/api/index.ts:154:21)\n    at mkfile (oh_modules/.ohpm/@qiniu+upload@1.0.2/oh_modules/@qiniu/upload/src/main/ets/components/@internal/api/index.ts:386:14)\n","httpCode":631}

**客服**：您好，看起来是空间不存在，您的上传token提供下

**客户**：{"code":200,"data":"_Jeo0jfcDcSilO4jUsjBvlYRPhwJ-FWO60NJebrt:5YyQZbM6u_ZJ3R5s0HiaGVnrtDs=:eyJzY29wZSI6ImNoaXBzY2xvdWQtY29tbXVuaXR5PzppY29uL2xvZ28vcm9sZWlkLTE3MzAzNDY1NjM2OTgiLCJkZWFkbGluZSI6MTczMDM1MDE2M30=","msg":"","orgData":"{\"code\":200,\"data\":\"_Jeo0jfcDcSilO4jUsjBvlYRPhwJ-FWO60NJebrt:5YyQZbM6u_ZJ3R5s0HiaGVnrtDs=:eyJzY29wZSI6ImNoaXBzY2xvdWQtY29tbXVuaXR5PzppY29uL2xvZ28vcm9sZWlkLTE3MzAzNDY1NjM2OTgiLCJkZWFkbGluZSI6MTczMDM1MDE2M30=\"}"}

**客户**：空间是chipscloud-community，应该存在的

**客户**：token *** _Jeo0jfcDcSilO4jUsjBvlYRPhwJ-FWO60NJebrt:5YyQZbM6u_ZJ3R5s0HiaGVnrtDs=:eyJzY29wZSI6ImNoaXBzY2xvdWQtY29tbXVuaXR5PzppY29uL2xvZ28vcm9sZWlkLTE3MzAzNDY1NjM2OTgiLCJkZWFkbGluZSI6MTczMDM1MDE2M30=

**客服**：您好，您的这个token不对的，空间这边多了一个问号[图片]

**客户**：好的，知道什么问题了

### 客服解答

您好，您的这个token不对的，空间这边多了一个问号[图片]

### 根本原因分析

需要配置合适的上传策略和工具

---

## 已经配置了证书，一直在加载中

**分类**：CDN｜证书问题

### 问题描述

已经配置了证书，一直在加载中

### 详细对话

**客户**：已经配置了证书，一直在加载中[图片][图片]

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

### 客服解答

您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

SSL证书配置问题，需检查证书状态和HTTPS配置

---

## 域名停止报错

**分类**：CDN｜配置问题

### 问题描述

域名：jzkwxyycs.zmdmajiang.comCNAME：jzkwxyycs-zmdmajiang-com-idvoyky.qiniudns.com操作停用后，报错信息如下：[    [        {            "title": "请求 ID",            "content": "DChL_9wLwvmzbQMY, DChL_9wLwvmzbQMY, DChL_9wLwvmzbQMY, DChL_9wLwvmzbQMY"        },        {            "title": "日志栈",            "content": "FUSIONDOMAINCOVER:1990;FUSIONDOMAINCOVER:2208;BUCKET:2;CFGS:2;BUCKET:17;DOMAINCONF:14/404;FUSIONDOMAINCOVER:1745;FUSIONDOMAINCOVER:1771;BUCKET/404;CFGS:6;BUCKET:22;DOMAINCONF:1/404;fusiondomain_cud:7934/404;APIS:7957/404;PORTAL-PROXY:11013/404"        }    ]]

### 详细对话

**客户**：域名：jzkwxyycs.zmdmajiang.comCNAME：jzkwxyycs-zmdmajiang-com-idvoyky.qiniudns.com操作停用后，报错信息如下：[    [        {            "title": "请求 ID",            "content": "DChL_9wLwvmzbQMY, DChL_9wLwvmzbQMY, DChL_9wLwvmzbQMY, DChL_9wLwvmzbQMY"        },        {            "title": "日志栈",            "content": "FUSIONDOMAINCOVER:1990;FUSIONDOMAINCOVER:2208;BUCKET:2;CFGS:2;BUCKET:17;DOMAINCONF:14/404;FUSIONDOMAINCOVER:1745;FUSIONDOMAINCOVER:1771;BUCKET/404;CFGS:6;BUCKET:22;DOMAINCONF:1/404;fusiondomain_cud:7934/404;APIS:7957/404;PORTAL-PROXY:11013/404"        }    ]]

**客服**：您好，请稍等

**客服**：您好，是域名需要删除吗

**客户**：是的，要先操作停用。停用的时候报错。

**客户**：域名：jzkwxyy.ctykwx.comCNAME：jzkwxyy-ctykwx-com-idvoylx.qiniudns.com目前状态是，处理中，需要协助手动处理下。

**客服**：好的，收到

**客户**：麻烦有再处理吗？现在还是显示创建中

**客服**：您好，当前还在处理中

**客户**：还没处理好吗

**客服**：您好，久等了，已经处理完成

**客户**：jzkwxyycs.zmdmajiang.com这个域名无法操作停用。停用报 404 错误。

**客服**：您好，您这边重新登录一下再操作看下呢

**客户**：重新登录之后，操作停用，还是提示[404] 未知错误，请创建工单获取帮助

**客服**：您好，您稍等这边确认一下

**客服**：您好，这边已经为您操作成功了，您确认一下

### 客服解答

您好，这边已经为您操作成功了，您确认一下

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 开通目录刷新权限

**分类**：对象存储｜SDK使用

### 问题描述

开通目录刷新权限

### 详细对话

**客户**：开通目录刷新权限[图片]

**客服**：您好，目前是不需要单独开通的，可以直接用。这个文档地址提供下，我们同步文档站同事调整下。

### 客服解答

您好，目前是不需要单独开通的，可以直接用。这个文档地址提供下，我们同步文档站同事调整下。

### 根本原因分析

权限不足或权限配置问题

---

## 域名没有，怎么弄

**分类**：CDN｜其他类咨询

### 问题描述

需要域名才可以用，我这没有域名啊

### 详细对话

**客户**：需要域名才可以用，我这没有域名啊

**客服**：您好，可以创建空间，会赠送您一个30天有效期的测试域名使用

**客户**：可以 ，先给我一个测试用的也行

**客户**：该如何创建呢

**客户**：我需要分发下载，您这个只加载图片

**客服**：您好，测试域名不支持调整，需要您绑定自己的域名选择下载线路

**客户**：123[图片]

**客服**：您好，具体是什么操作的报错？控制台报错信息是什么？

**客户**：报错500

**客户**：就是跟改为公开空间，更改不过来

**客户**：wxxtpd

**客服**：可以了您看下

**客服**：您好，刷新下浏览器缓存，再提交看下呢

**客服**：您好，刷新下浏览器缓存，再提交看下呢

**客户**：可以了

**客服**：好的

**客户**：报错了，内容没有进去{"error":"Document not found"}

**客服**：你好，这个是正常的，访问空间没有这个资源就会出现这个报错

### 客服解答

你好，这个是正常的，访问空间没有这个资源就会出现这个报错

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 请审核

**分类**：对象存储｜上传下载

### 问题描述

请尽快审核 谢谢

### 详细对话

**客户**：请尽快审核 谢谢[图片][图片]

**客服**：您好，请问你这个申请的具体是什么呢

### 客服解答

您好，请问你这个申请的具体是什么呢

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 短信发送失败

**分类**：云短信｜短信发送问题

### 问题描述

发送短信报错提示{ResponseInfo:com.qiniu.http.Response@30a1c53c,status:429, reqId:RP51r6HpzouGcAMY, xlog:null, xvia:, adress:sms.qiniuapi.com/202.107.***.***.***:443, duration:0.040000 s, error:SendLIMIT}

### 详细对话

**客户**：发送短信报错提示{ResponseInfo:com.qiniu.http.Response@30a1c53c,status:429, reqId:RP51r6HpzouGcAMY, xlog:null, xvia:, adress:sms.qiniuapi.com/202.107.***.***.***:443, duration:0.040000 s, error:SendLIMIT}

**客服**：您好，收到，我们看下

**客户**：麻烦快点, 我们系统的所有用户都不能登录了

**客服**：您好，超出了您设置的每月最大数量 建议在控制台调整下https://***.qiniu.com/sms/system#page=send-limit

### 客服解答

您好，超出了您设置的每月最大数量 建议在控制台调整下https://***.qiniu.com/sms/system#page=send-limit

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 账号注销

**分类**：账户与财务｜账户问题

### 问题描述

账户重复，删除多余的账户

### 详细对话

**客户**：账户重复，删除多余的账户

**客服**：您好，目前注销可以在控制台操作https://***.qiniu.com/developer/user/security目前用户自助注销需满足以下所有条件：1、账号为普通账号（非财务父子账号、OEM账号）2、账号下实时消费无产品用量、无消费金额（数据需要您自己删除）对象存储：https://***.qiniu.com/kodo/bucketCDN：https://***.qiniu.com/cdn/domain3、账号下无各种欠费实时消费明细（查看您当月消费）https://***.qiniu.com/financial/bills/estimated-consume如有欠费，将在下月5号出账、8号扣款，结算后，您再提交账号注销。4、账号下没有正在处理的提现审批https://***.qiniu.com/financial/withdraw5、账号当前没有被冻结注意：账号注销后，账号无法找回

### 客服解答

您好，目前注销可以在控制台操作https://***.qiniu.com/developer/user/security目前用户自助注销需满足以下所有条件：1、账号为普通账号（非财务父子账号、OEM账号）2、账号下实时消费无产品用量、无消费金额（数据需要您自己删除）对象存储：https://***.qiniu.com/kodo/bucketCDN：https://***.qiniu.com/cdn/domain3、账号下无各种欠费实时消费明细（查看您当月消费）https://***.qiniu.com/financial/bills/estimated-consume如有欠费，将在下月5号出账、8号扣款，结算后，您再提交账号注销。4、账号下没有正在处理的提现审批https://***.qiniu.com/financial/withdraw5、账号当前没有被冻结注意：账号注销后，账号无法找回

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 账号注销

**分类**：账户与财务｜账户问题

### 问题描述

多余账户，注销不用了

### 详细对话

**客户**：多余账户，注销不用了

**客服**：您好，目前注销可以在控制台操作https://***.qiniu.com/developer/user/security目前用户自助注销需满足以下所有条件：1、账号为普通账号（非财务父子账号、OEM账号）2、账号下实时消费无产品用量、无消费金额（数据需要您自己删除）对象存储：https://***.qiniu.com/kodo/bucketCDN：https://***.qiniu.com/cdn/domain3、账号下无各种欠费实时消费明细（查看您当月消费）https://***.qiniu.com/financial/bills/estimated-consume如有欠费，将在下月5号出账、8号扣款，结算后，您再提交账号注销。4、账号下没有正在处理的提现审批https://***.qiniu.com/financial/withdraw5、账号当前没有被冻结注意：账号注销后，账号无法找回

### 客服解答

您好，目前注销可以在控制台操作https://***.qiniu.com/developer/user/security目前用户自助注销需满足以下所有条件：1、账号为普通账号（非财务父子账号、OEM账号）2、账号下实时消费无产品用量、无消费金额（数据需要您自己删除）对象存储：https://***.qiniu.com/kodo/bucketCDN：https://***.qiniu.com/cdn/domain3、账号下无各种欠费实时消费明细（查看您当月消费）https://***.qiniu.com/financial/bills/estimated-consume如有欠费，将在下月5号出账、8号扣款，结算后，您再提交账号注销。4、账号下没有正在处理的提现审批https://***.qiniu.com/financial/withdraw5、账号当前没有被冻结注意：账号注销后，账号无法找回

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## https证书配置后很长时间没生效

**分类**：CDN｜配置问题

### 问题描述

images.eletaxi.cn 这个域名证书，上午部署后很长时间状态还是在处理中，证书马上要到期了，请尽快处理。

### 详细对话

**客户**：images.eletaxi.cn 这个域名证书，上午部署后很长时间状态还是在处理中，证书马上要到期了，请尽快处理。

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

**客户**：好的，谢谢

**客服**：不客气的

### 客服解答

不客气的

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 卡创建域名

**分类**：对象存储｜其他类咨询

### 问题描述

你好，自定义域名卡在创建中

### 详细对话

**客户**：你好，自定义域名卡在创建中[图片]

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客户**：好的，谢谢

**客服**：嗯嗯不客气的

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

**客户**：好的，谢谢，但是我想问下，为什么图片加载那么慢，慢到一直没加载出来的样子

**客户**：这是已经打开很久的了[图片]

**客户**：还有加载失败的可能性

**客服**：给下您的访问链接

**客户**：www.duoyuo.com

**客户**：使用vercel免费搭建镜像网站  这是一个用的这个存储的，有的是用其它存储的

**客户**：使用vercel免费搭建镜像网站 这个篇用的是七牛云存储，有的不是

**客服**：www.duoyuo.com—— 您创建的cdn域名是 cdn.duoyuo.com 预期是要用www.duoyuo.com访问吗 这个域名解析不在七牛

**客户**：是的

**客户**：请问怎么解决？

**客服**：cdn.duoyuo.com的回源配置修改为www.duoyuo.com试下 这个目前不建议调整 系统侧在优化中 可以明天调整配置

**客户**：好的谢谢

**客服**：好的

**客服**：cdn.duoyuo.com的回源配置修改为www.duoyuo.com试下 这个目前不建议调整 系统侧在优化中 可以明天调整配置
抱歉忽略这条回复，您这边是页面内引用的七牛图片资源，问题理解错误了。已这边帮您优化了海外回源，预计10分钟生效，麻烦您再试下

**客户**：好的，请问下这个怎么设置[图片]

**客服**：上面有回复，您可以忽略昨晚那条回复内容，不是站点问题，已处理优化。您现在是有新需求，需要改成www.duoyuo.com，加速www.duoyuo.com整站是吗

**客户**：好的，不用了

**客服**：嗯嗯，您再观察下

**客户**：[图片]ng[图片]你好，这webp和jpg等这些图片都是在对象存储里，文件也不大，为什么会这么慢

**客服**：访问链接给下

**客户**：www.duoyuo.com

**客服**：您在七牛创建的cdn域名是cdn.duoyuo.com 这个域名您选择的加速范围是海外 国内访问慢是符合预期的 可以调整线路为全球访问自 2020年10月20日起，控制台 -【域名管理】目前已支持域名覆盖区域（中国大陆、全球、海外）切换，您可以在[图片]点击『修改』自助切换。

**客户**：好的

**客服**：嗯嗯

**客户**：请问怎么设置，我没找到全球这个选项

**客服**：截图看下

**客户**：只有海外[图片][图片]

**客服**：由于相关法律法规规定，未备案的域名不支持修改为国内或者海外，建议使用已备案域名

**客户**：好的

**客户**：但是之前海外也是在1s内出的

**客户**：今天突然这样

**客服**：域名纯海外配置，国内访问速度是无法保证的哈

**客户**：行吧

### 客服解答

域名纯海外配置，国内访问速度是无法保证的哈

### 根本原因分析

配置相关问题，需要调整或优化系统配置

---

## 上传自有证书失败，证书是cf的

**分类**：CDN｜证书问题

### 问题描述

[    [        {            "title": "请求 ID",            "content": "GoMOO7YkbjTOcgMY"        },        {            "title": "日志栈",            "content": "fusionsslcert/400"        }    ]]

### 详细对话

**客户**：[    [        {            "title": "请求 ID",            "content": "GoMOO7YkbjTOcgMY"        },        {            "title": "日志栈",            "content": "fusionsslcert/400"        }    ]]

**客服**：您好1、建议您在证书厂商下载证书时，选择 Nginx 服务器类型的证书文件2、进入七牛云管理控制台：https://***.qiniu.com/certificate/ssl，点击 【上传自有证书】3、使用编辑器打开后续文件，并复制 .crt 或者 .pem 后缀的文件内容到证书内容 （公钥），复制 .key 后缀结尾的内容到 证书私钥 。[图片]如果需要把域名升级为 HTTPS 或者修改证书 的话，需要按照以下步骤绑定证书即可：https://***.qiniu.com/fusion/manual/4952/https-configuration

### 客服解答

您好1、建议您在证书厂商下载证书时，选择 Nginx 服务器类型的证书文件2、进入七牛云管理控制台：https://***.qiniu.com/certificate/ssl，点击 【上传自有证书】3、使用编辑器打开后续文件，并复制 .crt 或者 .pem 后缀的文件内容到证书内容 （公钥），复制 .key 后缀结尾的内容到 证书私钥 。[图片]如果需要把域名升级为 HTTPS 或者修改证书 的话，需要按照以下步骤绑定证书即可：https://***.qiniu.com/fusion/manual/4952/https-configuration

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 无法关闭强制https

**分类**：CDN｜证书问题

### 问题描述

由于证书过期，我想关闭 强制https 开关，现在是关不了，确实按键没有任何反应，希望帮助处理一下，谢谢！

### 详细对话

**客户**：由于证书过期，我想关闭 强制https 开关，现在是关不了，确实按键没有任何反应，希望帮助处理一下，谢谢！

**客服**：您好，控制台操作有什么问题吗。是有报错吗

### 客服解答

您好，控制台操作有什么问题吗。是有报错吗

### 根本原因分析

SSL证书配置问题，需检查证书状态和HTTPS配置

---

## 配置进度时间过长

**分类**：CDN｜配置问题

### 问题描述

配置进度时间过长

### 详细对话

**客户**：配置进度时间过长

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客户**：OK谢谢

**客服**：您好，稍等

**客户**：你好，好像又卡住进度了

**客服**：您好，稍等下

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

### 客服解答

您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

配置相关问题，需要调整或优化系统配置

---

## 聚水潭上传压缩包后点击下载显示404

**分类**：对象存储｜上传下载

### 问题描述

下载提示404

### 详细对话

**客户**：下载提示404[图片]

**客服**：您好，你们确认下，你们是不是cname解析错了，这个域名解析没有解析到七牛的cname

**客户**：好的，我们这边没有技术，请问这个是聚水潭那边的问题吗？还是说我这七牛云的配置哪里做的不对

**客服**：您好，这个是你们域名没有做 cname解析，你们域名在哪里买的，就去哪里做cname解析即可主机记录 rmq记录类型 cname记录值 rmq-qiniu-sursung-com-idvox9j.qiniudns.com

### 客服解答

您好，这个是你们域名没有做 cname解析，你们域名在哪里买的，就去哪里做cname解析即可主机记录 rmq记录类型 cname记录值 rmq-qiniu-sursung-com-idvox9j.qiniudns.com

### 根本原因分析

配置相关问题，需要调整或优化系统配置

---

## 域名无法删除

**分类**：CDN｜配置问题

### 问题描述

域名删除时间过长

### 详细对话

**客户**：域名删除时间过长

**客服**：稍等

**客服**：您好，久等了，已删除完成

**客户**：感谢

### 客服解答

您好，久等了，已删除完成

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## CDN 加速域名cname的主机记录和记录值不知道怎么填写

**分类**：CDN｜配置问题

### 问题描述

CDN 加速域名cname的主机记录和记录值不知道怎么填写

### 详细对话

**客户**：CDN 加速域名cname的主机记录和记录值不知道怎么填写

**客户**：把A记录删除了，可以了，麻烦再看一下是否配置成功，域名总是卡主

**客户**：配置的时候总是卡主

**客服**：您好，主机记录是img记录值：img-zjusb-com-idvoyly.qiniudns.com

**客户**：这个问我知道了，现在域名还是在配置中，麻烦看一下

**客户**：之前https配置总是卡主，看是否卡住了

**客服**：您好，稍等下，这边看下

**客户**：还没好吗？半个小时了

**客服**：您好，稍等下，这边处理下

**客户**：还没好？一个小时了

**客户**：你们后台有问题吧？总是报错

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

**客户**：https://***.zjusb.com/WX20241030-141149%402x.png图片打不开

**客服**：您好，您没有进行cname解析主机记录是img记录值：img-zjusb-com-idvoyly.qiniudns.com

**客户**：可以了 谢谢 还有一个问题，我这个账号之前认证的是温州的企业，现在能变更吗？之前企业的法人和都找不到了，那个企业在15年就注销了

**客服**：您好，股东还在吗？如果都不在的话，没有办法修改尝试进行下数据迁移是否可以？

**客户**：注册一个新的账号，你们能协助迁移吗？有没有迁移流程？

**客服**：不同账号下相同存储区域的数据迁移方式您好，不同账号下相同存储区域的数据迁移，有两种方法1、您这边可以先使用空间授权，然后再使用 qshell 工具中的 batchcopy 命令将一个空间中的文件批量复制到另一个空间。这个是空间授权的操作文档：https://***.qiniu.com/kodo/manual/3647/authorization-of-the-space这个是 qshell 的说明文档：https://***.qiniu.com/kodo/tools/1302/qshell第一步：qshell 列举空间中文件列表 https://***/qiniu/qshell/blob/master/docs/listbucket.md第二步：qshell 的 batchcopy 方法把文件进行复制到新空间 https://***/qiniu/qshell/blob/master/docs/batchcopy.md2、您这边可以先使用空间授权，然后再使用图形化工具将一个空间中的文件批量复制到另一个空间。这个是空间授权的操作文档：https://***.qiniu.com/kodo/manual/3647/authorization-of-the-space图形化工具文档：https://***.qiniu.com/kodo/5972/kodo-browser 注意：使用该工具目前进行上传/下载，如果不指定cdn域名的话，下载产生的流量费用为「外网流量」

### 客服解答

不同账号下相同存储区域的数据迁移方式您好，不同账号下相同存储区域的数据迁移，有两种方法1、您这边可以先使用空间授权，然后再使用 qshell 工具中的 batchcopy 命令将一个空间中的文件批量复制到另一个空间。这个是空间授权的操作文档：https://***.qiniu.com/kodo/manual/3647/authorization-of-the-space这个是 qshell 的说明文档：https://***.qiniu.com/kodo/tools/1302/qshell第一步：qshell 列举空间中文件列表 https://***/qiniu/qshell/blob/master/docs/listbucket.md第二步：qshell 的 batchcopy 方法把文件进行复制到新空间 https://***/qiniu/qshell/blob/master/docs/batchcopy.md2、您这边可以先使用空间授权，然后再使用图形化工具将一个空间中的文件批量复制到另一个空间。这个是空间授权的操作文档：https://***.qiniu.com/kodo/manual/3647/authorization-of-the-space图形化工具文档：https://***.qiniu.com/kodo/5972/kodo-browser 注意：使用该工具目前进行上传/下载，如果不指定cdn域名的话，下载产生的流量费用为「外网流量」

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 配置域名一直没有成功

**分类**：CDN｜配置问题

### 问题描述

配置域名一直没有成功

### 详细对话

**客户**：配置域名一直没有成功[图片]

**客服**：您好，请稍等

**客户**：咋样了？

**客服**：您好，还在处理中，请稍等

**客户**：还没好吗

**客服**：您好，久等了，已经处理完成，您确认下呢

**客户**：可以了

### 客服解答

您好，久等了，已经处理完成，您确认下呢

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## ssl 问题

**分类**：CDN｜证书问题

### 问题描述

我人在外 身上没电脑 域名 ssl 到期了 贵公司能代申请免费的域名绑定吗

### 详细对话

**客户**：我人在外 身上没电脑 域名 ssl 到期了 贵公司能代申请免费的域名绑定吗

**客服**：您好，代申请免费证书需要您在控制台操作下的，看下您那边有没有其他同事协助下呢您可以在 [域名管理] 中，点击您想要配置https的域名右侧的 [配置] 按钮，在新的页面中，在 [https配置] 下点击 [修改配置] ,点击开启->免费证书→勾选 [同意七牛云代申请免费证书] →确认，之后输入您账号的密码即可。域名管理：https://***.qiniu.com/cdn/domain

### 客服解答

您好，代申请免费证书需要您在控制台操作下的，看下您那边有没有其他同事协助下呢您可以在 [域名管理] 中，点击您想要配置https的域名右侧的 [配置] 按钮，在新的页面中，在 [https配置] 下点击 [修改配置] ,点击开启->免费证书→勾选 [同意七牛云代申请免费证书] →确认，之后输入您账号的密码即可。域名管理：https://***.qiniu.com/cdn/domain

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

## 更换邮箱

**分类**：账户与财务｜账户问题

### 问题描述

原邮箱[REDACTED_EMAIL]已不可用，需要更换为[REDACTED_EMAIL]

### 详细对话

**客户**：原邮箱[REDACTED_EMAIL]已不可用，需要更换为[REDACTED_EMAIL]

**客服**：您好，方法1：请登陆官网——点击官网右上角的管理控制台——个人面板——个人中心的安全设置更改邮箱，输入密码，填写邮箱进行修改。单击进入修改地址：https://***.qiniu.com/user/security方法二：如果您因为邮箱已经无法登陆，可以通过人工申诉提供相关资料进行修改，将材料发送邮件到 [REDACTED_EMAIL] ，抄送[REDACTED_EMAIL](商务邮箱)需要提供的信息如下：a、个人实名认证：请提供注册邮箱、修改原因、手持与实名认证一致的身份证正面图片、新注册邮箱；邮件发送后请工单上告知我们，提供发件邮箱和联系电话。这边同步给商务为您审核处理

**客户**：你好，我们是企业实名认证，是提供营业执照吗？

**客服**：企业实名认证：账号认证的资质信息，公司企业营业执照副本、与修改账号邮箱的说明并加盖公司公章，将资料以扫描件的形式发送到support@qiniu.com邮箱，抄送[REDACTED_EMAIL]

**客户**：你好，邮件已发，请帮我处理吧。

**客服**：好的

**客户**：你好，请问在帮我修改了吗

**客服**：您好，请稍等

**客服**：你好，已完成修改，您登出后重新登录，使用 [REDACTED_EMAIL] 登录即可，密码不变

**客户**：好的，感谢

**客户**：没有其它问题了

**客服**：好的

### 客服解答

好的

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 需要开今年5月7前的所有消费发票

**分类**：账户与财务｜发票问题

### 问题描述

系统没有办法开5月7前的所有消费发票

### 详细对话

**客户**：系统没有办法开5月7前的所有消费发票

**客服**：您好，提供下发票信息，这边帮您申请超出6个月充值金额，或低于1000元金额的发票，您无法自行申请，不清楚金额的话可以在开票金额栏填写全部金额还请您在控制台提前申请准备好对应的发票抬头信息，添加对应的专票抬头信息审核通过后，如果您已经有了专票的抬头信息，可以不用再次添加，另外，给您开的发票默认是数电发票，需要纸质发票可以说明需求，提供收件地址。根据《增值税专用发票使用规定》申请专票必须要和实名认证公司名保持一致。-------------开票信息-----------开票金额:发票抬头: 发票类型: 纳税人识别号: 开户银行名称: 开户账号: 公司名称: 公司地址: 联系电话:

**客户**：如何查看超过6个月的可开票全部金额？

**客户**：我的开票信息里面已经有抬头了，你直接帮我申请，6个月前的全部金额都开，普票即可。

**客服**：您好，好的，抬头信息麻烦工单提供下，人工申请时需要二次确认的

**客户**：公司：广西雄持科技有限公司 信用代码：91450100MABXXFR34L联系人：王浩 电话：[REDACTED_PHONE]

**客服**：收到

**客服**：您好，已提交申请，您可以在发票管理中关注发票进度以及后续下载发票：https://***.qiniu.com/financial/invoice-contract/invoice

### 客服解答

您好，已提交申请，您可以在发票管理中关注发票进度以及后续下载发票：https://***.qiniu.com/financial/invoice-contract/invoice

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 我这域名处理一直不完成-+

**分类**：对象存储｜上传下载

### 问题描述

我这域名处理一直不完成-+

### 详细对话

**客户**：我这域名处理一直不完成-+[图片]

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

### 客服解答

您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

需要根据具体情况分析问题原因并提供解决方案

---

## 配置加速访问不了

**分类**：CDN｜配置问题

### 问题描述

配置加速访问不了

### 详细对话

**客户**：配置加速访问不了

**客服**：您好，您这边将访问链接给一下，这边测试访问下看下

**客户**：48063482.admin.aijdtmos.com

**客服**：您好，这个是域名，不是资源访问链接，您这边不是说访问不了吗？具体是哪个链接访问不了，这边需要测试下的

**客户**：https://***jdtmos.com/001b5369c896cf1a09e483a7dd45d1a69da8d051.png

**客服**：您好，私有空间的话需要使用私有鉴权链接才行的，您这边需要使用直接访问的话需要将空间修改为公开空间才行的

**客户**：好的谢谢，但是现在七牛云登录不了[图片]

**客服**：您好，控制台目前的话在处理中了，您这边可以刷新后重新登录看下

**客户**：[图片]能直接改成公开吗

**客服**：您好，点击空间名称，到空间设置下修改即可

**客户**：me[图片]没有反应呢

**客户**：[图片]提交不了麻烦给看看

**客服**：您好，您稍等这边确认一下

**客服**：您好，您这边再看下目前是否可以正常修改了的

**客户**：可以了谢谢

**客服**：好的

### 客服解答

好的

### 根本原因分析

域名配置或DNS解析问题，需检查域名绑定状态和DNS记录

---

