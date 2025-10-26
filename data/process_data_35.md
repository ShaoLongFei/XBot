# 七牛云客服工单处理记录 (Part 35)

本文档整理了七牛云客服系统中的问题工单,包含问题描述、解决方案和根因分析。

---

## 下面的图片链接无法访问

**问题分类**: CDN > 访问下载

### 问题描述

你好，这个图片链接无法访问，请看下是什么原因。

### 客服解答

**客户**：你好，这个图片链接无法访问，请看下是什么原因。

**客服**：您好，您这边刷新一下本地DNS缓存后再看下，这边目前看可以正常请求的

**客户**：好的

**客服**：您好，嗯嗯

### 根因分析

**根本原因**: 客户端DNS缓存未及时更新,仍解析到旧的CDN节点地址。

---

## 访问超时

**问题分类**: CDN > 访问下载

### 问题描述

https://img.showguide.cn/[REDACTED_PATH]?imageView2/1/w/208/h/120

### 客服解答

**客户**：https://img.showguide.cn/[REDACTED_PATH]?imageView2/1/w/208/h/120

**客服**：您好抱歉久等了，调整了覆盖节点，辛苦再观察看下

**客户**：https://img.showguide.cn/[REDACTED_PATH]

**客服**：您好这边测试已经正常了，您清理下本地dns缓存和客户端缓存，再访问看下[图片]

**客户**：好的

### 根因分析

**根本原因**: 客户端DNS缓存未及时更新,仍解析到旧的CDN节点地址。

---

## 批量获取加密空间里的文件，会相应非常慢

**问题分类**: 对象存储 > 上传下载

### 问题描述

批量下载慢

### 客服解答

**客户**：批量下载慢

**客服**：您好批量下载建议使用工具 会比较快

**客服**：您好，七牛后台界面操作不支持批量下载的，批量下载，可以通过以下几种方式实现：方法1.调用list接口，遍历空间，获得空间内的文件信息，然后下载。代码逻辑是先调用 list 接口获得文件名的集合，再与空间域名拼接成url(https://domain/[REDACTED_PATH] 是空间域名，key是文件名)，循环调用 download 方法下载文件。https://developer.qiniu.com/[REDACTED_PATH] qshell 工具进行批量下载操作；qshell 工具下载地址：https://github.com/[REDACTED_PATH] 工具批量下载命令：https://github.com/[REDACTED_PATH] 的 qdownload 命令时，如果指定使用CDN域名下载时，建议将 public 参数置为true，下载时击中CDN缓存时产生CDN流量费用，未击中CDN缓存回源下载资源时产生的是CDN回源流量费用；如不指定，下载资源产生的全部是CDN回源流量费用。方法3:使用图形化工具kodo browser工具批量下载，勾选想要下载的文件/目录后点击【下载】即可。参考：https://developer.qiniu.com/[REDACTED_PATH]

**客户**：是批量请求

**客户**：折是我们pc端[图片]

**客户**：好多请求都慢

**客服**：文件链接提供下

**客户**：今天刚出现，也是偶尔的，因为我们今天刚把这些图片从开放空间移动到私密空间，刚开始用私密空间的链接，会不会是cdn的问题啊

**客户**：https://files.guojian88.com/[REDACTED_PATH]?e=1729767153&token=[REDACTED_TOKEN]=https://files.guojian88.com/cus/s/01/58/671a0f7b283c61fd363128e5.png?e=1729767153&token=[REDACTED_TOKEN]=https://files.guojian88.com/cus/s/01/58/671a0f11283c61fd363128af.jpg?e=1729767153&token=[REDACTED_TOKEN]=https://files.guojian88.com/cus/s/01/58/671a0524283cf80af492056f.png?e=1729767153&token=[REDACTED_TOKEN]=

**客服**：您好非常抱歉给您造成不便，经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您清理下客户端dns缓存，稍后再观察看看

**客户**：1

**客户**：有个问题

**客户**：移动文件参数原空间 : yangxu_3km,原key : file_emp/20220917/1663403974505Na4kfiCR6DP5kmoR4cC.jpg,移动后的空间 guojian-encryption,移动后的key: cus/s/01/63/671af7b2283c61fd36319256.jpg移动文件失败612,----{ResponseInfo:com.qiniu.http.Response@3018e41,status:612, reqId:rkMAAGn99ouqjgEY, xlog:-, xvia:, adress:rs.qbox.me/[REDACTED_IP]:443, duration:0.109000 s, error:no such file or directory}

**客服**：您好，您这边看您的原空间下没有这个资源的file_emp/20220917/1663403974505Na4kfiCR6DP5kmoR4cC.jpg

**客户**：必须有啊 https://file.yangxu88.com/[REDACTED_PATH]

**客户**：卧槽 这个是缓存

**客户**：我知道了

**客服**：您好，嗯嗯好的

**客户**：好的谢谢暂时没有其他问题了

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 无法访问图片了

**问题分类**: 对象存储 > 上传下载

### 问题描述

所有图片，无法访问图片了

### 客服解答

**客户**：所有图片，无法访问图片了

**客服**：您好，您这边刷新一下本地DNS缓存后再看下，这边目前看可以正常请求的

**客户**：不行，有的好使，有的不好使。www.xiaojiangy.com这个网站你访问下试试

**客户**：现在全部不好使了

**客服**：您好，这边目前看已经恢复了的，需要您这边刷新一下本地dns缓存或者切换网络环境后再看下的[图片]

### 根因分析

**根本原因**: 客户端DNS缓存未及时更新,仍解析到旧的CDN节点地址。

---

## 刚刚发现有一段时间图片资源全部无法访问

**问题分类**: CDN > 其他类咨询

### 问题描述

刚刚发现有一段时间图片资源全部无法访问，但是现在已经恢复，检查了证书也没有过期，资源包也还有余量，是什么原因导致的？

### 客服解答

**客户**：刚刚发现有一段时间图片资源全部无法访问，但是现在已经恢复，检查了证书也没有过期，资源包也还有余量，是什么原因导致的？

**客户**：现在又有用户反馈看不到图片了，时好时坏，是什么原因导致的？

**客服**：您好，您这边刷新一下本地DNS缓存后再看下，这边目前看可以正常请求的，应该是请求到了旧节点缓存导致的

**客户**：具体要如何操作？不是只有一两个用户这样，我刚刚收到七牛云的报警了：账号[REDACTED_EMAIL], 您的域名tarotpic.zhiangit.***于2024-10-24 16:30-16:35的5xx状态码比例为20.79%, 已高于您的预设值5%

**客服**：您好非常抱歉给您造成不便，经确认是由于个别节点网络抖动导致的，异常节点已剔除下线导致，正常清理下本地缓存后即可恢复正常的，或者切换一下网络环境看下的

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 静态文件cdn不可访问

**问题分类**: CDN > 访问下载

### 问题描述

域名foundationassets.iautos.cn所有的都不可访问

### 客服解答

**客户**：域名foundationassets.iautos.cn所有的都不可访问

**客服**：您好抱歉久等了，这边调整了覆盖节点，辛苦再观察看下

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 配置的证书

**问题分类**: CDN > 配置问题

### 问题描述

地址打不开

### 客服解答

**客户**：地址打不开

**客服**：您好刷新下本地缓存再看下呢，这边看是正常的

**客户**：现在好了刚才域名打不开

**客户**：ping 的时候还是有丢包

**客户**：现在ping 也正常了

**客服**：您好，好的，现在正常就好，您再观察看下，有什么问题及时反馈

**客户**：好的

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 客户反馈上传图片异常，请帮忙看下是否有异常

**问题分类**: 对象存储 > 上传下载

### 问题描述

客户反馈上传图片异常，请帮忙看下是否有异常

### 客服解答

**客户**：客户反馈上传图片异常，请帮忙看下是否有异常

**客户**：上传完成的图片url有时候打不开，过了一会才可以访问，是不是CDN节点出现了问题

**客服**：您好，当前已恢复，您稍后再确认下呢

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 图片加载失败

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

北京地区 何时恢复

### 客服解答

**客户**：北京地区 何时恢复[图片][图片]

**客户**：图片加载失败 北京地区何时恢复

**客服**：稍等

**客服**：您好，麻烦再访问试下呢

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 域名Cname解析有问题

**问题分类**: 对象存储 > 上传下载

### 问题描述

我们的资源域名https://resource.51beauty.com.cn

### 客服解答

**客户**：我们的资源域名https://resource.51beauty.com.cn

**客服**：您好，是不会配置cname解析吗？

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## cdn全部无法访问

**问题分类**: CDN > 访问下载

### 问题描述

所有请求一直在pending

### 客服解答

**客户**：所有请求一直在pending

**客户**：所有cdn地址都访问不了

**客服**：您好目前测试打开正常 您可以换个网络再试下[图片]

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 存储的资源访问不了啦

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

https://oss.taobaojingpin.top/[REDACTED_PATH]  访问不了

### 客服解答

**客户**：https://oss.taobaojingpin.top/[REDACTED_PATH]  访问不了

**客户**：空间名称:  juejinxitong

**客服**：您好，当前已恢复，您稍后再确认下呢

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## dongzhounet仓库所有图片都打不开了

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

这是截图

### 客服解答

**客户**：这是截图[图片]

**客户**：我看了另一个仓库也打不开

**客户**：华东地区的仓库

**客户**：请尽快i

**客服**：稍等

**客服**：您好，麻烦再访问试下呢

**客户**：可以了 是什么原因呢

**客服**：您好经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您后续再观察看看

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 现在看不了图片

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

移动网络无法访问图片

### 客服解答

**客户**：移动网络无法访问图片

**客服**：您好，当前已恢复，您稍后再确认下呢

**客户**：一部分可以了，还有一部分还是不行，是在逐步恢复吗？

**客服**：您好，这个可能是客户端有DNS缓存，访问到了非预期的节点，可能需要等待客户端缓存失效才可以的

### 根因分析

**根本原因**: 客户端DNS缓存未及时更新,仍解析到旧的CDN节点地址。

---

## 无法访问

**问题分类**: CDN > 访问下载

### 问题描述

我们天津和北京的用户反馈，无法访问网站（网站静态文件CDN无法访问）

### 客服解答

**客户**：我们天津和北京的用户反馈，无法访问网站（网站静态文件CDN无法访问）

**客服**：稍等

**客服**：您好，麻烦用户侧再访问试下呢

**客户**：现在是恢复了，请问刚才是什么原因

**客服**：您好经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您后续再观察看看

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 网页打不开，或者打开非常慢

**问题分类**: CDN > 访问下载

### 问题描述

有些资源完全加载不进来

### 客服解答

**客户**：有些资源完全加载不进来

**客服**：您好测试响应正常 您再试下[图片]

**客户**：刚才整个域名是不可以访问的。然后现在我同事在厦门的电信的ip。也是不能访问。现在还是不行。

**客户**：我同事的ip： [REDACTED_IP]。他现在访问不了这个文件： https://s2.tb5.fun/[REDACTED_PATH]

**客服**：您好非常抱歉给您造成不便，经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您清理下客户端dns缓存，稍后再观察看看

**客户**：好的，谢谢

**客服**：好的

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 图片无法展示

**问题分类**: CDN > 访问下载

### 问题描述

ping 域名无响应不适用wifi，使用手机流量是同样的问题

### 客服解答

**客户**：[图片]ping 域名无响应不适用wifi，使用手机流量是同样的问题

**客服**：您好，您这边刷新一下本地DNS缓存后再看下，这边目前看可以正常请求的

### 根因分析

**根本原因**: 客户端DNS缓存未及时更新,仍解析到旧的CDN节点地址。

---

## 图片无法打开

**问题分类**: 对象存储 > 上传下载

### 问题描述

突然外链就无法打开了，但是我看图片是存在的https://webfilm.sfilmmaker.com/[REDACTED_PATH]

### 客服解答

**客户**：[图片]突然外链就无法打开了，但是我看图片是存在的https://webfilm.sfilmmaker.com/[REDACTED_PATH]

**客服**：您好这边测试可以访问，辛苦您那边清理下本地浏览器缓存，再访问请求看下[图片]

**客户**：你回复时已经能打开了，但是会经常性的打不开图片，已经成为经常性的问题了

**客服**：您好，这边已经为您优化了下，您这边可以后续再观察看下

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## SSL证书申请

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

证书过期

### 客服解答

**客户**：证书过期

**客服**：您好，手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/[REDACTED_PATH]

### 根因分析

**根本原因**: SSL证书已过期,需要重新申请或上传新的证书。

---

## 本月put请求暴涨

**问题分类**: 对象存储 > 上传下载

### 问题描述

本月put请求暴涨

### 客服解答

**客户**：本月put请求暴涨[图片]

**客服**：您好，这边看您这边两个操作了大批量的删除的

**客户**：大批量删除，会算在 put请求里吗？

**客服**：您好，嗯嗯是的

**客户**：删除的请求次数，会统计在 put的请求次数里？是这样吗？

**客户**：好奇怪啊.......

**客服**：您好，这边看和您的删除量是对的上的

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 访问图片非常慢

**问题分类**: CDN > 访问下载

### 问题描述

访问异常慢

### 客服解答

**客户**：[图片]访问异常慢

**客服**：您好，您这边多少访问几次看下，初访问的话节点上是没有缓存的，会进行回源拉取缓存的，这个会比较耗时，拉取后即可正常的

**客户**：重复访问还是这么久时间需要

**客户**：[图片]这会又访问不到了

**客服**：您好，您这边刷新一下本地DNS缓存后再看下，这边看您这边应该是请求到了旧节点的缓存了的

**客户**：你们更新节点了？现在好了

**客服**：您好，是您那边的本地dns旧缓存过期了的，重新拉取了新的缓存了的，我们这边正常目前，所以上面让您直接操作刷新本地DNS缓存的，目前是缓存自动过期了的

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 图片无法访问

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

无法访问图片

### 客服解答

**客户**：无法访问图片

**客服**：您好，无法访问的链接提供下，这边看下

**客户**：https://image.59cdn.com/[REDACTED_PATH]

**客服**：您好，这边看是可以访问的，您这边访问有什么报错？[图片]

**客户**：其他工程师回复了,异常节点已经修复了

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 页面超时

**问题分类**: CDN > 访问下载

### 问题描述

客户访问该地址响应特别慢，帮忙分析cdn的分发是否有波动

### 客服解答

**客户**：客户访问该地址响应特别慢，帮忙分析cdn的分发是否有波动[图片][图片]

**客服**：您好，1、麻烦提供下用户的 ip、dns 信息，和cdn节点信息，这边代理测试下可以通过访问这个链接 http://ping.huatuo.qq.com/ 获取本地的 ip 和 dns 信息，在检测域名这边输入下cdn域名，点击提交检测，然后截图通过工单提交给我们[图片]2、建议让用户使用 chrome 浏览器，按照下述文档获取下 remote adress(对端节点ip)，request header(客户端请求头) 以及 response header(服务端响应头)信息，方便我们查询分析问题。https://developer.qiniu.com/[REDACTED_PATH]

**客户**：目前已恢复了，但是有区间出现过

**客服**：您好，好的，您再观察下，有什么问题您及时反馈

**客户**：现在还是很慢哦，[图片]

**客服**：您好非常抱歉给您造成不便，经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您清理下客户端dns缓存，稍后再观察看看

**客户**：好的  谢谢

**客服**：没事的

**客户**：这几天又出现了该问题了河北地区和山西地区,麻烦帮忙看看[图片]

**客户**：河北地区的[图片]

**客服**：代理节点测试是正常的[图片]

**客户**：都是正常的吗  那为啥会出现这个错误呀有其他的解决办法不

**客户**：错误[图片]

**客服**：报错这个是您本地网络dns 的问题，建议修改dns为 [REDACTED_IP]，备用选择 [REDACTED_IP]

**客户**：让客户修改不现实,客户使用我们的能力

**客服**：换个网络试下是否可以

**客户**：我先让客户尝试一下看行不行

**客服**：好的 如果有异常的话 可以及时同步我们排查

**客户**：还有其他的方案的吗 从我们这侧入手,不从客户那

**客服**：您那边现在是业务高峰期吗  帮您调整优化下访问线路

**客户**：一直是高峰期,我们是个交易平台

**客户**：晚上你们会有人值班不,优化访问线路,会短暂性关闭吗

**客服**：晚上有人值班的 您需要优化的话 可以直接工单反馈 或者 直接拨打400-808-9176转2号线联系我们处理优化

**客户**：如果不会断线 那其实中午就可以帮忙优化一下

**客服**：现在调整可以吗

**客户**：会有哪些影响,麻烦告知一下哈 如果是无感的那就现在帮忙优化吧 谢谢

**客服**：已经优化 20分钟后 再观察看下

**客户**：优化之后出现的频率更高了 麻烦帮忙看看

**客服**：本地的缓存清除之后 再去访问

**客户**：是客户访问,我们这边访问都是正常的,多个客户都在反馈这个问题了

**客服**：优化线路后  如果没有清除旧的缓存 请求的还是旧节点  需要清除本地缓存 再去访问

**客户**：只能客户方处理吗

**客服**：是的 把缓存清除一下再访问 或者换个浏览器再访问

**客户**：频发了 还有一些其他处理方法不,感觉优化之后更高了故障率

**客服**：有异常的客户  可以让打开  http://ping.huatuo.qq.com/ 获取本地的 ip 和 dns 信息，在检测域名这边输入下cdn域名，点击提交检测，然后截图通过工单提交给我们 这边代理节点测试看下[图片]

**客户**：好 我找客户调试一下

**客服**：好的

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 图片段时间内无法访问

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

图片段时间内无法访问

### 客服解答

**客户**：图片段时间内无法访问

**客服**：您好，这个是CDN节点下线，客户端访问到了非预期节点导致的，当前应该已经可以访问了，您再试试呢

**客户**：现在可以了，刚才都不能访问

**客服**：您好非常抱歉给您造成不便，经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您清理下客户端dns缓存，稍后再观察看看

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 七牛对象存储

**问题分类**: 对象存储 > 上传下载

### 问题描述

新疆地区用户反馈无法联通这个域名，这是为何？

### 客服解答

**客户**：新疆地区用户反馈无法联通这个域名，这是为何？

**客户**：如果是cdn服务器出问题，贵公司产品不会自动切换到源ip地址吗？

**客服**：稍等

**客服**：您好，麻烦您再访问试下呢自动切换到源ip地址，目前还不支持。

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 北方客户上传和查看不了图片

**问题分类**: 对象存储 > 上传下载

### 问题描述

北方客户上传和查看不了图片

### 客服解答

**客户**：北方客户上传和查看不了图片

**客服**：您好，1、麻烦提供下用户的 ip、dns 信息，和cdn节点信息，这边代理测试下可以通过访问这个链接 http://ping.huatuo.qq.com/ 获取本地的 ip 和 dns 信息，在检测域名这边输入下cdn域名，点击提交检测，然后截图通过工单提交给我们[图片]2、建议让用户使用 chrome 浏览器，按照下述文档获取下 remote adress(对端节点ip)，request header(客户端请求头) 以及 response header(服务端响应头)信息，方便我们查询分析问题。https://developer.qiniu.com/[REDACTED_PATH]

**客服**：您好，无法访问的链接提供一个这边测试看下

**客户**：是一部分客户不能使用，我们这是可以：https://photo.edingzi.cn/[REDACTED_PATH]

**客服**：您好非常抱歉给您造成不便，经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您清理下客户端dns缓存，稍后再观察看看

**客户**：小程序、网页分别怎么清理客户端dns缓存？

**客服**：您好可以切换网络看下

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 请问 刚才 域名 是不是有问题了

**问题分类**: CDN > 证书问题

### 问题描述

刚才有一段时间 域名访问 白屏了

### 客服解答

**客户**：刚才有一段时间 域名访问 白屏了

**客服**：您好调整了覆盖节点，辛苦再观察看下

**客户**：好的好的

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 国内请求连接下载报错请求超时

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

今天17点05之前，使用国内请求连接下载报错请求超时，海外网络去测试下载是正常的

### 客服解答

**客户**：今天17点05之前，使用国内请求连接下载报错请求超时，海外网络去测试下载是正常的

**客服**：您好，非常抱歉给您造成不便，经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，如果现在还有异常的话，辛苦您清理下客户端dns缓存即可

**客户**：好的

**客服**：嗯嗯好的

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## CDN地址访问超时

**问题分类**: CDN > 访问下载

### 问题描述

如图所示资源无法访问

### 客服解答

**客户**：如图所示资源无法访问[图片]

**客服**：您好非常抱歉，上述节点网络有短暂波动导致的，异常节点已做剔除下线，辛苦清理下本地dns缓存，稍后再访问观察看下

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 这边域名所有权验已经通过怎么还是待确认状态

**问题分类**: 视频监控 > 其他类咨询

### 问题描述

这边域名所有权验已经通过怎么还是待确认状态

### 客服解答

**客户**：这边域名所有权验已经通过怎么还是待确认状态[图片]

**客服**：您好目前看证书已经签发 可以再观察下

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 资源无法访问

**问题分类**: CDN > 访问下载

### 问题描述

https://codeyn.com/[REDACTED_PATH]

### 客服解答

**客户**：https://codeyn.com/[REDACTED_PATH]

**客服**：您好，您这边刷新一下本地DNS缓存后再看下，这边目前看可以正常请求的[图片]

**客户**：我的和客户都无法访问。

**客服**：您好，所有需要您这边刷新一下本地DNS缓存后再看下的，应该是请求到旧节点的缓存了的

### 根因分析

**根本原因**: 客户端DNS缓存未及时更新,仍解析到旧的CDN节点地址。

---

## app-img.xiongmaopeilian.com

**问题分类**: CDN > 访问下载

### 问题描述

CDN加速域名大面积使用4G网络打开特别慢，请赶快帮看下

### 客服解答

**客户**：CDN加速域名大面积使用4G网络打开特别慢，请赶快帮看下

**客服**：您好，您这边刷新一下本地DNS缓存后再看下，这边目前看可以正常请求了的

**客户**：现在大面积用户反馈，不是一个人问题

**客户**：沈阳、太原、北京都有问题其中沈阳的换过联通、移动网络也不行

**客服**：您好，嗯嗯这边已经拨测看了下的，目前看可以正常请求了，只是您这边还请求在旧节点的缓存上的，所以需要您这边刷新一下本地DNS缓存后再看下的

**客户**：那刚才是什么问题呢？七牛那边是出故障了吗？

**客服**：您好非常抱歉给您造成不便，经确认是由于个别节点网络抖动导致的，异常节点已剔除下线的

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 资源访问下载非常慢

**问题分类**: CDN > 访问下载

### 问题描述

从今天中午开始，图片等下载非常慢，见附件图，请问是否有异常？

### 客服解答

**客户**：从今天中午开始，图片等下载非常慢，见附件图，请问是否有异常？

**客服**：您好，1、麻烦提供下用户的 ip、dns 信息，和cdn节点信息，这边代理测试下可以通过访问这个链接 http://ping.huatuo.qq.com/ 获取本地的 ip 和 dns 信息，在检测域名这边输入下cdn域名，点击提交检测，然后截图通过工单提交给我们[图片]2、建议让用户使用 chrome 浏览器，按照下述文档获取下 remote adress(对端节点ip)，request header(客户端请求头) 以及 response header(服务端响应头)信息，方便我们查询分析问题。https://developer.qiniu.com/[REDACTED_PATH]

**客户**：我工单中添加不了图片，是什么原因？一直提示什么触发 IP 限制，停留两分钟

**客服**：您好，可以复制结果提供下url

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## cdn无法访问

**问题分类**: CDN > 配置问题

### 问题描述

cdn 无法访问

### 客服解答

**客户**：cdn 无法访问[图片][图片]

**客服**：您好非常抱歉给您造成不便，经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您清理下客户端dns缓存，稍后再观察看看

**客户**：目前  dl.mljia.cn、static.mljia.cn 还是ping 不通

**客服**：您好，刷下本地dns缓存看下

**客户**：现在可以了

**客服**：您好，好的，您再观察下，有什么问题您及时反馈

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 文件无法访问

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

今天有出现很多数据无法访问的情况例如：https://qn-vote.yuanmingyuanpark.cn/[REDACTED_PATH]?imageView2/1/q/10

### 客服解答

**客户**：今天有出现很多数据无法访问的情况例如：https://qn-vote.yuanmingyuanpark.cn/[REDACTED_PATH]?imageView2/1/q/10

**客服**：您好非常抱歉给您造成不便，经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您稍后再观察看看

**客户**：https://qn-vote.yuanmingyuanpark.cn/[REDACTED_PATH]

**客户**：已经2个小时了

**客服**：这个文件是heic格式的 生成heic原图的设备是ios18吗[图片]

**客户**：应该是的，有什么问题吗

**客服**：这个格式的图片无法直接打开 参考 https://developer.qiniu.com/[REDACTED_PATH] 这个接口 转换一下格式打开

**客户**：好的，谢谢

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 空间绑定了两个域名，其中一个访问不正常

**问题分类**: CDN > 访问下载

### 问题描述

发现问题出现时间：2024-10-24 16:47   至 2024-10-24 17:17问题一：   登录七牛云控制台，无法查看图片详情问题二：空间绑定了两个域名：https://files.scjswk.com   文件无法正常访问，加载不出图片https://testfile.scjswk.com 可以访问

### 客服解答

**客户**：发现问题出现时间：2024-10-24 16:47   至 2024-10-24 17:17问题一：   登录七牛云控制台，无法查看图片详情问题二：空间绑定了两个域名：https://files.scjswk.com   文件无法正常访问，加载不出图片https://testfile.scjswk.com 可以访问

**客户**：提交工单时，突然恢复访问，控制台文件管理查看图片详情也正常了。 无法提供截图等信息。麻烦帮忙核查下是什么原因导致的

**客服**：您好非常抱歉给您造成不便，经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您清理下客户端dns缓存，稍后再观察看看

**客户**：好的

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 图片上传后无法访问

**问题分类**: 对象存储 > 上传下载

### 问题描述

16：37分客户来找的，到5点左右,这期间客户说上传后不显示，

### 客服解答

**客户**：16：37分客户来找的，到5点左右,这期间客户说上传后不显示，[图片]

**客服**：您好非常抱歉给您造成不便，经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您清理下客户端dns缓存，稍后再观察看看

**客户**：还需要清理dns缓存吗，如果不清理会怎样？会过多久自动清理呢？现在倒是没有人反映问题

**客服**：您好如果观察没有异常 可以先不用清除dns缓存

**客户**：您好，今天又出现了，https://img.kqyun.com/[REDACTED_PATH]

**客户**：另外我们在客户机器执行了：ipconfig /flushdns 还是不行

**客服**：ping 一下域名 将节点反馈我们代理测试下

**客户**：[图片]ping都是超时的

**客服**：124.236.97.251这个节点昨天已经剔除了，辛苦您清理下客户端dns缓存，再去访问

**客户**：如果清理呢，我上面说已经执行ipconfig /flushdns清理过了

**客户**：如何清理？我上面那种ipconfig不起作用的

**客服**：是您的客户解析到了这个节点 还是您这边解析到的

**客服**：如果无法清理  可以修改dns为 [REDACTED_IP]，备用选择 [REDACTED_IP]

**客户**：客户的电脑上解析到的，也是在客户电脑上cmd，然后fulshdns的，只能一个个客户处理吗

**客户**：修改完dns可以了，这个只能一个个客户改吗？是不是过2天dns缓存会自动失效，那样的就不用改了

**客服**：是不是过2天dns缓存会自动失效，那样的就不用改了——是的

**客户**：能批量怎么处理吗？客户不太会改，很多客户，总不能一个个改吧？有其他方式批量处理吗

**客服**：这个没有批量处理的方式 是客户端的缓存导致的

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 今天有较多用户反馈播放视频类文件卡顿

**问题分类**: CDN > 其他类咨询

### 问题描述

今天有较多用户反馈播放视频类文件卡顿，监控图看在那时间之后确实带宽明显下降了

### 客服解答

**客户**：今天有较多用户反馈播放视频类文件卡顿，监控图看在那时间之后确实带宽明显下降了[图片]

**客服**：您好，是哪个域名呢，这边查询下

**客户**：res.study.itaojin.cn目前反馈的有这个域名

**客服**：您好是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您后续再观察看看

**客户**：用户那边要刷新DNS缓存吗

**客服**：您好，如果访问还非预期，可以刷新下，正常情况下dns已经自动刷新了。

**客户**：好的，我们再观察下

**客服**：嗯嗯好的，有问题给我们反馈

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 今天图片有段时间打不开，是你们的原因吗

**问题分类**: 对象存储 > 上传下载

### 问题描述

今天下午4点30左右有用户反馈图片打不开

### 客服解答

**客户**：今天下午4点30左右有用户反馈图片打不开

**客服**：您好非常抱歉给您造成不便，是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您再观察看看

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 七牛云存储图片打不开

**问题分类**: 对象存储 > 上传下载

### 问题描述

七牛云存储图片打不开xunhua2-spa668-com-idvmrug.qiniudns.com举例：https://xunhua2.spa668.com/[REDACTED_PATH]

### 客服解答

**客户**：七牛云存储图片打不开xunhua2-spa668-com-idvmrug.qiniudns.com举例：https://xunhua2.spa668.com/[REDACTED_PATH]

**客户**：C:\Users\Administrator>ping xunhua2.spa668.com正在 Ping allcdn.lv2.qnydns.com [[REDACTED_IP]] 具有 32 字节的数据:请求超时。请求超时。请求超时。请求超时。ping了一下，ping不通呀，我看了下好像证书也没过期?麻烦技术大佬看下

**客服**：您好非常抱歉给您造成不便，经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您清理下客户端dns缓存，稍后再观察看看

**客户**：收到，谢谢

**客户**：https://xunhua2.spa668.com/[REDACTED_PATH]   这个好像还打不开呀？

**客服**：把您本地的dns清除一下 目前访问是正常的[图片]

**客户**：好

**客服**：好的

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 麻烦帮忙上传持久化处理视频截图报错是什么原因

**问题分类**: 对象存储 > SDK使用

### 问题描述

$thumbnailKey = 'video/eyy/' . date("Y") . '/' . date("m") . '/' . date("d") . '/' . time() . uniqid() . '.jpg';			$fops = 'vframe/jpg/offset/5/w/320/h/240'; 			$encodedThumbnailKey = urlencode($thumbnailKey);			$saveasKey = $auth->privateDownloadUrl($bucket . ':' . $encodedThumbnailKey);			$fops .= '|saveas/' . $saveasKey;			list($ret, $err) = $pfop->execute($bucket, $key, $fops);请问fop命令格式错误吗，如果错误，该怎么写才是正确的。

### 客服解答

**客户**：$thumbnailKey = 'video/eyy/' . date("Y") . '/' . date("m") . '/' . date("d") . '/' . time() . uniqid() . '.jpg';			$fops = 'vframe/jpg/offset/5/w/320/h/240'; 			$encodedThumbnailKey = urlencode($thumbnailKey);			$saveasKey = $auth->privateDownloadUrl($bucket . ':' . $encodedThumbnailKey);			$fops .= '|saveas/' . $saveasKey;			list($ret, $err) = $pfop->execute($bucket, $key, $fops);请问fop命令格式错误吗，如果错误，该怎么写才是正确的。

**客服**：您好，您这边参考下这个demo的，这边看报错是您的saveas参数有误的https://github.com/[REDACTED_PATH]

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 我查询域名有备案的，但是CDN显示为备案，冻结

**问题分类**: CDN > 其他类咨询

### 问题描述

86iis.comCDN显示为备案冻结，但是我查询备案在的呀

### 客服解答

**客户**：86iis.comCDN显示为备案冻结，但是我查询备案在的呀

**客服**：您好看您域名icp备案是在 2024-10-18 审核通过的，域名备案恢复后，您可以在控制台自主解冻请点击『解冻』，一般在 15 - 20 分钟内会解冻完成，线上服务恢复正常。https://portal.qiniu.com/[REDACTED_PATH]

**客户**：我这些，86iis.com比如这个的ssl过期了，然后我倒ssl证书那边，我直接点击续费，就可以了是吗。我怎么感觉点击续费了，他也没续上

**客户**：[图片]jiu 就是像这样

**客服**：您好您申请的是免费证书，证书到期后不需要续费，重新下单购买新的证书即可手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/[REDACTED_PATH]

**客户**：el1.cnfenjinshi.cnoa678.com021tzsb.com100orange.cnyigaocnc.cngoldcatch.cnzjgzfw.cnzsjcjrzx.comfrrenli.comzhdgyl.comxiaobailab.comwisdomj.comyijianrumian.comwuzhouchuguolaowu.comrandengbaota.comwuhanfenbi.comxkjmzj.comiewo.cnwxgp.cnbaliphoto.cn168cz.cnpnlss.cngd-photo.cngxhongxin.cndaoshanglianmeng.com.cnhohgroup.cnyhjbx.cnhd-whpc.com.cnartseed.cn

**客户**：你好，我的域名早早就提交解冻了，为什么过了这么久，还是在解冻中

**客服**：稍等，这边看下

**客服**：img.pnlss.cn需要您在「对象存储』产品，绑定空间的域名管理中手动解冻下域名。其他已解冻完成。[图片]

**客户**：img.pnlss.cn 点解冻了

**客服**：好的，已解冻完成了

**客户**：爱你

**客户**：img.originalstudio.com.cn  你好这个域名证书要过期了但是我重建了一条 ssl证书为什么我再存储空间中，要绑定证书的时候，找不到 这条证书呢

**客户**：[图片]你看

**客服**：证书通用名称需要与待配置域名匹配，才能显示选择

**客户**：如何匹配，这条域名的证书昨天就加好了

**客户**：之前我加的时候，有的证书快过期了，我直接添加一个证书，然后来这里替换就好，现在却找不到了。

**客户**：img.originalstudio.com.cn你看这条域名

**客服**：稍等

**客服**：目前前端是列举了100条证书，您这边证书比较多，您到证书管理这边来绑定试下：https://portal.qiniu.com/[REDACTED_PATH] kodo源站域名-点击「部署」[图片]

**客户**：[图片]部署了也一样，也是无法去选择，挑不出来 我再更新的证书，可是有的域名就可以选择

**客户**：img.xjaml.cn比如这个

**客户**：你看[图片]

**客户**：我明明加的新的证书，因为旧的要过期了但是这域名，我去空间里面选择绑定证书的时候，却不会跳出新的证书给我选择但是有的域名可以，有的域名就不行

**客服**：您参考下这边给您的上条回复呢，在「我的证书」那边部署试下

**客户**：我试过了不行

**客户**：你看，我点击部署，就跳出这个旧了，新的证书就没有，但是你看截图，我明明有加了个新的[图片]

**客户**：img.yigaocnc.cn
  img.goldcatch.cn
  img.zjgzfw.cn
 比如这些域名就能换绑证书，更新

**客服**：稍等

**客户**：比如这些就是点证书那边，没有新的证书挑出来，就很奇怪
  img.xjaml.cn
  img.y06.top
  img.zyugat.cn
  img.0530kt.cn

**客服**：这边的部署您点一下呢[图片]

**客户**：[图片]这样对吧

**客户**：[图片]然后还是没有啊

**客服**：稍等

**客服**：您好，点了那个部署就更新好了。img.xjaml.cn已经是新证书了。存储那边的域名管理页面只能列出100条证书记录，证书较多就列不到，产品已经有计划更新优化，后面会更新。您可以在我的证书那边点击部署或者我的证书中，把那些过期的证书清理删除一下，100个以内就能读取到。

**客户**：[图片]可是CDN这里还是这样显示

**客户**：过期的域名怎么清理，没看到删除的地方

**客服**：cdn的点到这个，再点部署[图片]

**客服**：是过期的证书清理。我的证书这边，到期时间已经过期的证书可以删除下https://portal.qiniu.com/[REDACTED_PATH]

**客户**：cdn的点到这个，再点部署   在哪里没找到，你这个图片，我都不能方法

**客户**：我点击部署了img.xjaml.cn

**客户**：你看一下，我的证书有没有更新进去

**客服**：稍等

**客服**：img.xjaml.cncdn侧已经更新好证书了

**客户**：你好，我已经把域名都部署了新的证书，但是还号几个域名，在CDN里面，显示过期，或者期限不足不然我把域名全都给你，你能帮我更新吗？

**客户**：[图片]可以吗

**客户**：这是全部的，里面有很多，我已经部署好了新的证书，但是cdn里面，还是要嘛过期了，要嘛快过期
  img.yongxiongwood.cn
  img.originalstudio.com.cn
  img.ybyinpu.cn
  img.doland.cn
  img.seovps.cn
  img.leenow.cn
  img.yjksjx.com.cn
  img.dmdpro.com.cn
  img.nayiduo.cn
  img.40crhjyg.com
  img.qqsaas.cn
  img.zhugejiejingqu.com
  img.czqcjy.cn
  img.ntsjswkj.com
  img.zaizhangw.com
  img.ou3wb.cn
  img.czycgykj.cn
  img.100orange.cn
  img.86iis.com
  img.lovtec.com.cn
  img.t765.cn
  img.t876.cn
  img.shuolian.com.cn
  img.qqjzy.cn
  img.yzvsr.cn
  img.imanke.cn
  img.rich100.cn
  img.tianjinkeyou.cn
  img.dibain.cn
  img.lexkj.cn
  img.xnyqccyw.cn
  img.fanglaowang.com.cn
  img.kuaizhuanjia.com
  img.shangpinyouhuo.com
  img.topwoa.com
  img.cheli99.com
  img.kuaidianjie.com
  img.xianlewan.com
  img.hbmkdj.com
  img.sqjsgs.com
  img.yingkouliangyushangmao.com
  img.wubahaoche.com
  img.qiangweibaihuodian.com
  img.gckxjscx.com
  img.suoruisi.com
  img.nkjwtn.com
  img.chengquanyuju.com
  img.sybingyu.com
  img.honghedu.com
  img.ituen.com.cn
  img.qqhrhf.cn
  img.vrdh.cn
  img.stellarmodels.com.cn
  img.jssotae.cn
  img.weyooz.cn
  img.vastone.com.cn
  img.ehsoft.cn
  img.52kkj.cn
  img.xingchen023.cn
  img.cxbsa1.cn
  img.bailiqi.cn
  img.yunhuijinrong.com.cn
  img.cdnk.com.cn
  img.myhongjia.cn
  img.b-ha.com.cn
  img.toscra.com.cn
  img.jczsw.cn
  img.mingard.cn
  img.7dyu.cn
  img.fenjinshi.cn
  img.niurouhuoguo.cn
  img.vrta.cn
  img.floormat.com.cn
  img.el1.cn
  img.jxyxzg.cn
  img.9ixyun.cn
  img.yunsuizhushou.cn
  img.luxike.cn
  img.qqysmy.com
  img.ophsc.com
  img.gzjcrcyj.com
  img.shanxiqianchi.com
  img.kaimiyatc.cn
  img.szythenergy.com
  img.cangmage.com
  img.czxylh.com
  img.ytyjgjg.com
  img.bqkpa.com
  img.wydmba.com
  img.yzzy88.cn
  img.car18.cn
  img.xjaml.cn
  img.y06.top
  img.zyugat.cn
  img.0530kt.cn
  img.hzzvap.cn
  img.lxj800.cn
  img.sadya.cn
  img.ysxdl.cn
  img.bjcgj.cn
  img.aldl.cn
  img.wxgp.cn
  img.baliphoto.cn
  img.168cz.cn
  img.lacie.com.cn
  img.vassey.cn
  img.kjdb.cn
  img.pnlss.cn
  img.gd-photo.cn
  img.gxhongxin.cn
  img.hd-whpc.com.cn
  img.jzjiu.cn
  img.21youqie.cn
  img.paining.com.cn
  img.sh-skyline.com.cn
  img.9ctong.cn
  img.daoshanglianmeng.com.cn
  img.hohgroup.cn
  img.shhaier.cn
  img.blueku.com.cn
  img.yhjbx.cn
  img.ibonline.cn
  img.kts-online.com.cn
  img.lemove.cn
  img.artseed.cn
  img.yigaocnc.cn
  img.goldcatch.cn
  img.zjgzfw.cn
  img.szanbj.com
  img.ytshz-1.cn
  img.shtbgs.cn
  img.magelinegw.cn
  img.zsjcjrzx.com
  img.frrenli.com
  img.zhdgyl.com
  img.xiaobailab.com
  img.wisdomj.com
  img.yijianrumian.com
  img.wuzhouchuguolaowu.com
  img.huibeiok.com
  img.randengbaota.com
  img.xfqingyuan.com
  img.taiwanplum.com
  img.xldgl.com
  img.wuhanfenbi.com
  img.xkjmzj.com
  img.iewo.cn
  img.wantouguanjian.com.cn
  img.wuhwuhfhxyx.cn
  img.cdtsjdyp.com
  img.oa678.com
  img.hndcjxgs.com
  img.021tzsb.com
  img.whssdp.com
  img.szyzdf.com
  img.[REDACTED_PHONE].com
  img.qujinggl.com
  img.gzhjql.com
  img.yyxdcxx.com
  img.hybiosource.com
  img.jiaceluoen.com.cn
  img.pasenk.com
  img.tpco304.com
  img.vgmn.cn
  img.surpriseltd.cn
  img.sjst.org.cn
  img.youtuo100.com
  img.intle1.com
  img.whxylg.com
  img.tjjashy.com
  img.yiyidianqi.com
  img.bluechao.com
  img.maydian.com
  img.hanyuangame.com
  img.zbyztc.com
  img.slangstop.com
  img.jingchutc.com
  img.yuxicapital.com
  img.czpfmr.com
  img.124cn.cn
  img.xjdm.net.cn
  img.depkg.cn
  img.zhuanwangtong.com
  img.rwib.cn
  img.592cx.cn
  img.xjrskcp.cn
  img.amk07.cn
  img.your-it-people.com
  img.wxgygg.com
  img.fzwgd.com
  img.hzsdxm.com
  img.zhongchoukeji.com
  img.skywangjjj.com
  img.xftsgg.com
  img.yyfeite.com
  img.52hyj.com
  img.wymj.net
  img.tianjinzikaobenke.com
  img.zjxpdq.com
  img.nmxingnong.com
  img.cxgzkj.com
  img.jinxiufenglin.com
  img.hbcdzy.com
  img.hntjwh.com

**客服**：稍等

**客户**：更新好了，请跟我说一声

**客服**：您好，提示证书过期的是还没部署的，您之前应该是部署的源站域名，没有部署cdn的域名，需要部署下cdn域名

**客户**：我部署了呀[图片]

**客户**：我觉得，你这个更新证书，有不少bug呀，你们得优化优化了

**客户**：你可以把我那些已经过期的，域名发给我吗

**客服**：选cdn域名[图片]

**客服**：您一直在部署源站域名，源站倒是都部署了，但实际解析的cdn域名服务

**客户**：我又都部署了一遍CDN你再看看

**客户**：后台网络太慢了

**客户**：有很多其实点了，但是网络太卡了，估计就没点着

**客服**：稍等

**客服**：img.pnlss.cn这个域名证书未上传，您上传了部署下，其他都好了

**客户**：好的，感谢

**客户**：你好，你们的存储空间，跳不出证书的那个bug还没修复好啊

**客户**：[图片]我现在要加新的域名，还是挑不出来这个我知道可以去ssl证书那边去部署，但是你们那个部署的界面很卡，加载很慢，也改优化优化了把

**客服**：是域名管理界面，给域名部署证书的时候，加载不出对应证书吗？

**客户**：是的这个情况，已经出现很久了

**客户**：我以前加的时候都不会出现这样的情况，但是在最近的这一个月的时间，一直有这个问题

**客服**：是给哪个域名加证书？

**客户**：img.cdhhsc.comimg.forbrilliant.com.cnimg.yjlchild.cnimg.hd23.cnimg.synz168.cnimg.esnuo.cnimg.suichuanlvshi.comimg.hhtydl.comimg.donaa.cnimg.shzsfc.comimg.qianlijun.cnimg.syywxms.cnimg.yzsymj.cnimg.mocosj.cnimg.longluw.cnimg.zbju.cnimg.kdc-jpn.comimg.housewifery.net.cnimg.gpcccopier.comimg.seihoeigyo.comimg.chu-rong.cnimg.yinjijx.comimg.mxmht.cnimg.exhoo.cnimg.520fanke.comimg.chenxiawujin.comimg.xdnhs.com

**客户**：这些是我现在要加的我之前加的那些也是只样子，我至今去 ssl证书那边。Kodo 源站域名  这里去部署，很麻烦，而且又慢

**客服**：这些已经部署到最新的证书了

**客户**：你已经帮我部署进去了？

**客服**：你那边刷新页面检查一下

**客户**：你这个聊天窗口，还总数传不了图片没有全部绑上

**客户**：[图片]你看

**客户**：绑上的那些，是我自己去部署 Kodo 源站域名 才有的，不然都没有

**客户**：特别慢

**客服**：你图片里没榜上的域名发一个呢

**客户**：img.zbju.cnimg.yzsymj.cn比如这两个

**客服**：看着是显示有问题，实际上域名已经有证书了[图片]

**客户**：那这样，我图片能显示出来吗如果我不在这里面去操作绑定证书的话

**客服**：可以在 CDN 模块 —— 域名管理处确认一下这些域名的情况

**客户**：img.sjqclm.com那你看一下这条是已经部署了证书的，还是没部署，我刚加的

**客服**：也是部署了 https

**客服**：使用 cdn 服务的话，需要给域名配置好 CNAME 解析

**客服**：那这样，我图片能显示出来吗----------------------------------------当前你那边给cdn域名配置上 CNAME 解析之后[图片]正常情况是可以显示，如后续有问题的话可以反馈这里

**客户**：[图片]你说的那个我知道，但是空间这里要绑定上证书，才能显示出来图片，你看，我的号里的，2024xin5就能显示出证书，然后那个2024xin4就显示不出来证书，你帮忙看看，肯定是哪里有bug

**客服**：显示不出图片是指？

**客服**：您当前情况是，有的域名可以显示证书，有的域名无法显示证书然后不能显示证书的，访问也是有问题吗？麻烦再提供几个无法显示证书的域名和截图呢，我这里反馈内部确认一下问题

**客户**：[图片]img.zbju.cn

**客户**：img.yinjijx.com

**客服**：好的

**客户**：img.zbju.cn  我留了这条域名 给你查看其他跳不出来证书的，我自己去ssl那边去 部署 Kodo 源站域名 绑上了证书

**客服**：好的，这边已经反馈到内部进一步确认问题了

**客服**：您好，您那边方便浏览器抓包一下 network 的信息吗，找到关于 img.zbju.cn  这部分请求的 reqid

**客户**：86iis.com100orange.cniewo.cnrandengbaota.comwuzhouchuguolaowu.comyijianrumian.comwisdomj.comxiaobailab.comzhdgyl.comfrrenli.comzsjcjrzx.comzjgzfw.cngoldcatch.cnyigaocnc.cnartseed.cnhd-whpc.com.cnyhjbx.cnhohgroup.cndaoshanglianmeng.com.cn021tzsb.comoa678.comxkjmzj.comwuhanfenbi.com这些DNS是要删除了，删了好久了，都没反应

**客服**：麻烦稍等，这边处理

**客服**：您好，久等了，已删除完成

**客户**：iewo.cn这条没删

**客服**：稍等

**客服**：您好，已删除完成了哈

**客户**：86iis.com100orange.cniewo.cnrandengbaota.comwuzhouchuguolaowu.comyijianrumian.comwisdomj.comxiaobailab.comzhdgyl.comfrrenli.comzsjcjrzx.comzjgzfw.cngoldcatch.cnyigaocnc.cnartseed.cnhd-whpc.com.cnyhjbx.cnhohgroup.cndaoshanglianmeng.com.cn021tzsb.comoa678.comxkjmzj.comwuhanfenbi.com我加了CDN，一直在处理中，咋回事，你们后台今天好慢

**客服**：都创建完成了哈

**客户**：randengbaota.combaliphoto.cn这两条删除一下

**客服**：稍等

**客服**：您好，当前域名没有待处理的删除任务，您可以操作下停用删除哈

### 根因分析

**根本原因**: 客户端DNS缓存未及时更新,仍解析到旧的CDN节点地址。

---

## 域名

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

配置中

### 客服解答

**客户**：配置中

**客服**：您好已经帮您手动介入处理完成

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 今天推送断了几次

**问题分类**: 直播云 > 推流问题

### 问题描述

半小时看看这个为啥断了3，4次

### 客服解答

**客户**：半小时看看这个为啥断了3，4次

**客户**：1[图片][图片]

**客户**：网络ping  连接超时的时候ping qq.com是没有断过的

**客服**：您好，这边看推流断开原因是客户端主动断开的，您这边确认一下您这边的网络是否有波动等情况的，目前来看我们这边是没有问题的NetworkError(read,tcp i/o timeout),EOF

**客户**：没有啊，我的ping 很稳定

**客服**：但是这边目前查看的话是主动断开的，您这边可以换一个网络环境测试一下看下呢？

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 七牛云获取静态资源获取不到

**问题分类**: CDN > 访问下载

### 问题描述

{error:"bad gateway": getsrc reach max try times}

### 客服解答

**客户**：{error:"bad gateway": getsrc reach max try times}

**客服**：您好，您这边换一个网络环境再看下呢？这边测试正常的，看报错应该是网络的问题的[图片]

**客户**：这个只是其中一个资源https://cdn.dougongcloud.com/[REDACTED_PATH]

**客服**：cdn.dougongcloud.com这个域名的话应该是请求到了旧节点的缓存了的，目前这个已经调整了，您这边可以刷新一下本地dns缓存后再看下的

**客户**：没有明白，旧节点的缓存是指文件历史记录还是什么意思？然后已经调整了，是什么时候调整的？我们需要这个时间节点和用户确认一下，因为我们很多客户在曝，我们需要和客户进行反馈

**客服**：您好，节点是CDN的节点IP的，这边已经将您请求到的旧节点下线了的，预计5点左右调整下线的，可以让用户切换一下网络后看下的，wifi切数据、数据切wifi看下的

**客户**：后续需要采取什么措施可以避免此类意外的发生，或者我们需要配合你们做哪些动作，因为这个基础服务的影响对于我们来说比较重要，我们需要做好防护

**客服**：您好，这个的话我们这边帮您优化一下节点看下，后续正常的话不会有这种情况的后续再有这种情况可以看下修改下本地dns看下，修改dns为 [REDACTED_IP]，备用选择 180.76.76.76的

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 国内下载失败

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

又出现这个问题，国内的下载不了

### 客服解答

**客户**：又出现这个问题，国内的下载不了

**客服**：您好，无法访问的链接提供下，具体报错信息麻烦也提供下呢

**客户**：一会好一会坏的，辛苦下请保持持久稳定

**客户**：所有的链接都是无法下载，一会好一会坏的

**客户**：我们这边在进行视频功能，把视频上传到七牛，上传视频不会导致无法下载吧？

**客户**：广东节点：https://qiniu.newmine.net/[REDACTED_PATH]?attname=  无法下载河北节点：https://qiniuadmin.newmine.net/[REDACTED_PATH]   可以下载，但下载非常慢

**客服**：您好，您这边下载还有什么报错呢？

**客户**：时好时坏，目前是又好了

**客服**：您好，无法访问的时候有什么报错吗？

**客户**：提示超时

**客服**：您好，1、麻烦提供下用户的 ip、dns 信息，和cdn节点信息，这边代理测试下可以通过访问这个链接 http://ping.huatuo.qq.com/ 获取本地的 ip 和 dns 信息，在检测域名这边输入下cdn域名，点击提交检测，然后截图通过工单提交给我们[图片]2、建议让用户使用 chrome 浏览器，按照下述文档获取下 remote adress(对端节点ip)，request header(客户端请求头) 以及 response header(服务端响应头)信息，方便我们查询分析问题。https://developer.qiniu.com/[REDACTED_PATH]

**客户**：目前正常

**客服**：您好好的，您再观察看看

### 根因分析

**根本原因**: 客户端网络带宽限制或上传节点响应慢。

---

## 如何上传wav文件

**问题分类**: 对象存储 > 上传下载

### 问题描述

配置了 audio/wav;audio/*,但还是上传不了

### 客服解答

**客户**：配置了 audio/wav;audio/*,但还是上传不了[图片]

**客服**：您好，您先不设置，直接上传看下文件类型是什么，再设定对应的类型上传看下

**客户**：是audio/wav[图片]

**客服**：给下您有设置文件类型的上传token 这边看下

**客户**：多謝，有同事解決了

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 有没有办法批量的导出我空间里的文件

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

我想要大批量的把空间里保存的文件都导出到我本地进行压缩保存，有没有办法实现

### 客服解答

**客户**：我想要大批量的把空间里保存的文件都导出到我本地进行压缩保存，有没有办法实现

**客服**：您好，批量下载，可以通过以下几种方式实现：方法1.调用list接口，遍历空间，获得空间内的文件信息，然后下载。代码逻辑是先调用 list 接口获得文件名的集合，再与空间域名拼接成url(https://domain/[REDACTED_PATH] 是空间域名，key是文件名)，循环调用 download 方法下载文件。https://developer.qiniu.com/[REDACTED_PATH] qshell 工具进行批量下载操作；qshell 工具下载地址：https://github.com/[REDACTED_PATH] 工具批量下载命令：https://github.com/[REDACTED_PATH] 的 qdownload 命令时，如果指定使用CDN域名下载时，建议将 public 参数置为true，下载时击中CDN缓存时产生CDN流量费用，未击中CDN缓存回源下载资源时产生的是CDN回源流量费用；如不指定，下载资源产生的全部是CDN回源流量费用。方法3:使用图形化工具kodo browser工具批量下载，勾选想要下载的文件/目录后点击【下载】即可。参考：https://developer.qiniu.com/[REDACTED_PATH]

**客户**：好的谢谢

**客服**：好的

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 有些ip访问不了链接

**问题分类**: CDN > 其他类咨询

### 问题描述

之前配置的ip限制，请问都关掉了吗？我这边的客户有反馈请求不了链接image.jexiu.com 这个域名

### 客服解答

**客户**：之前配置的ip限制，请问都关掉了吗？我这边的客户有反馈请求不了链接image.jexiu.com 这个域名

**客服**：您好，无法访问的是什么报错？

**客户**：就是访问不了链接，应该是链接报错了

**客户**：ip限制有全部帮我关掉了吗

**客户**：之前有叫你们帮我开限制测试，但是最后不知道有没有全部关闭了

**客服**：您好，您多久有说需要关闭呢

**客服**：这边核实下

**客户**：可能是10.19号说需要关闭的，没有关闭的话，请问还有哪个限制没有关闭？然后再帮我全部关闭

**客服**：您好，核实已经关闭了，没有配置的

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 存储在对象存储的资源下载异常

**问题分类**: CDN > 访问下载

### 问题描述

1,上传文件到对象存储后，多长时间可以正常下载？2，解析IP异常是否正常？3，如何解决这个问题，比如说刷新缓存或者上传下载间隔周期多少？

### 客服解答

**客户**：1,上传文件到对象存储后，多长时间可以正常下载？2，解析IP异常是否正常？3，如何解决这个问题，比如说刷新缓存或者上传下载间隔周期多少？[图片]

**客服**：您好1、上传文件落存储后 可以直接访问2、如果是下午16点后的访问异常，经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您清理下客户端dns缓存，稍后再观察看看

**客户**：关于这次的事件，我们收到了大量投诉，请问贵方以后如何避免出现此类问题，出现此类问题如何解决？能否发布相关通知，公告事后是否有相应的补偿机制

**客服**：cdn节点是智能调度的 对于检测到的异常节点 这边会立即剔除优化处理 您可以再观察下补偿机制商务会与您联系 请保持电话通畅

**客服**：您那边电话未接通 给下可联系的电话

**客户**：[REDACTED_PHONE]原绑定号码人员已离职，能否后台帮忙更换一下绑定手机号码

**客服**：您好，修改手机号有如下三种方式，如果您的手机无法接受验证码可以使用方法二和方法三进行申请修改手机号：方法一：点击官网右上角的管理控制台——个人面板——个人中心的安全设置更改手机，发送手机验证码，验证之后就可以对手机号进行修改。[图片]方法二：点击官网右上角的管理控制台——个人面板——个人中心的安全设置更改手机，选择邮箱验证码，验证之后就可以对手机号进行修改。[图片]方法三：通过人工申诉提供相关资料进行修改，将材料发送邮件到 [REDACTED_EMAIL] ，需要提供的信息如下：a、个人实名认证：请提供注册邮箱、修改原因、手持与实名认证一致的身份证正面图片、新手机号码；b、企业实名认证：请提供注册邮箱、修改原因、实名认证的营业执照图片、申请人手持正面身份证图片、新手机号码。（注意：为了您的账号信息安全，修改手机号时需要您提供相关信息，这边为您审核处理，感谢您的理解与配合～）邮件发送后请工单上告知我们。我们后台操作完毕后，重新登录系统会提示您短信验证新的手机号，验证完毕后手机号即修改完成。

**客户**：联系使用[REDACTED_PHONE]这个号码目前服务正常吗？我们这边又出现了拉取图片异常

**客服**：哪个图片访问异常 给下链接地址

**客服**：哪个图片访问异常 给下链接地址

**客户**：正在排查，现象类似，所以先问一下是否有异常

**客服**：目前没有检测到有异常 您可以再观察下

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## CDN图片访问不了

**问题分类**: CDN > 访问下载

### 问题描述

https://kehuqiniu.jiwebshop.cn/[REDACTED_PATH]

### 客服解答

**客户**：https://kehuqiniu.jiwebshop.cn/[REDACTED_PATH]

**客服**：稍等

**客服**：您好，切换网络试下呢，这边测试可以正常打开的[图片]

**客户**：很不稳定  一会能打开  一会不能打开的   影响业务啊

**客户**：刚才可以 这会又不行

**客服**：把本地dns缓存清除一下再访问

### 根因分析

**根本原因**: 客户端DNS缓存未及时更新,仍解析到旧的CDN节点地址。

---

## 创建迁移任务失败了

**问题分类**: 对象存储 > 数据迁移

### 问题描述

创建迁移任务失败了，提示的信息看不懂，麻烦看看

### 客服解答

**客户**：创建迁移任务失败了，提示的信息看不懂，麻烦看看

**客服**：您好，麻烦提示信息或页面错误信息提供我们确认下呢

**客户**：list objects failed: RequestError: send request failed caused by: Get "https://aipukeji.qiniu.aipupower.cn/?max-keys=1": dial tcp: lookup aipukeji.qiniu.aipupower.cn on [REDACTED_IP]:53: no such host

**客服**：您好，本地开了代理吗

**客户**：没有呢

**客服**：aipukeji.qiniu.aipupower.cn这个域名没解析呢，get不到数据。

**客户**：我填写的是qiniu.aipupower.cn这个域名，怎么会自动加上存储空间名称的？

**客服**：检查下配置信息，重新创建个任务试下呢

**客户**：我上传不了图片，配置的区域 Endpoint是：https://aipupower.cn

**客户**：配置的区域 Endpoint是：https://app.aipupower.cn

**客服**：您好，aipupower.cn这个是s3源站域名吗，需要s3的app.aipupower.cn域名没解析

**客户**：是https://qiniu.aipupower.cn这个域名才对，打错了；一直提示list objects failed: RequestError: send request failed caused by: Get "https://aipukeji.qiniu.aipupower.cn/?max-keys=1": dial tcp: lookup aipukeji.qiniu.aipupower.cn on [REDACTED_IP]:53: no such host这个错误，重新创建了迁移任务还是不行

**客服**：您这边是不同账号间数据迁移处理吗

**客户**：是的，不同帐号的迁移

**客服**：您好迁移的源信息中的空间名、对应空间所属七牛账号邮箱给下，这边看下[图片]

**客户**：空间名：aipukeji区域endpoint:https://qiniu.aipupower.cn

**客服**：您好空间名：aipukeji    这个空间所属七牛账号邮箱也给下

**客户**：[REDACTED_EMAIL]

**客服**：您好区域endpoint填写：http://s3.cn-south-1.qiniucs.com/ 这个

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 修改了域名的配置没生效

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

修改了2个域名的https配置，一直没生效帮忙看看。

### 客服解答

**客户**：修改了2个域名的https配置，一直没生效帮忙看看。

**客服**：您好这边帮您手动介入处理下 请稍等

**客服**：已经处理完成

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 预计搞到几点呢 这个部署的

**问题分类**: CDN > 证书问题

### 问题描述

https://grey-in.easybii.com/[REDACTED_PATH]

### 客服解答

**客户**：https://grey-in.easybii.com/[REDACTED_PATH]

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 图片异常丢失[紧急]

**问题分类**: 对象存储 > 上传下载

### 问题描述

今约17点40分左右，突然发现图片无法加载。如https://file.weikechina.com/[REDACTED_PATH] { "error": "Document not found"} 且 七牛控制台无法预览此图片为 2024-10-16 17:16:38 上传

### 客服解答

**客户**：今约17点40分左右，突然发现图片无法加载。如https://file.weikechina.com/[REDACTED_PATH] { "error": "Document not found"} 且 七牛控制台无法预览此图片为 2024-10-16 17:16:38 上传

**客户**：控制台见照片[图片]

**客服**：您好请稍等，这边看下

**客服**：您好抱歉久等了，辛苦清理下本地dns缓存再访问看下

**客户**：什么原因?

**客服**：您好非常抱歉久等了，看下来是个别节点回源异常导致的，异常节点已剔除下线，辛苦稍后再观察看下

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 配置https一直处理中

**问题分类**: CDN > 配置问题

### 问题描述

配置https一直处理中

### 客服解答

**客户**：配置https一直处理中

**客服**：您好这边帮您手动介入处理下 请稍等

**客服**：已经处理好了

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## vps不用了，买了年付套餐，请问怎么退费

**问题分类**: 云主机 > 其他类咨询

### 问题描述

47.100.57.33101.132.165.144这两个ip及绑定的云主机都不需要使用，请问怎么销毁呢

### 客服解答

**客户**：47.100.57.33101.132.165.144这两个ip及绑定的云主机都不需要使用，请问怎么销毁呢

**客服**：您好，麻烦针对如下问题做一下填写确认：1.退款原因（以便我方改进产品不足）：2.申请退款的产品实例ID：3.已使用时长所对应的费用不退回，请您确认已知晓；4.代金券支付部分无法退回，请您确认已知晓：5.主机或实例是否已备份？若已备份，请回复“数据已备份”；若无需备份，请回复“数据无需备份” 。（退款后服务器实例立即被清除，数据不再保留，请提前备份数据）6.主机退款是将整个实例全部退订，不是单独退订主机升级的部分，请您确认知晓？注意：a.如需退款多个实例，需要注明多个实例ID，退款资源会按照填写上述表单为准b.云主机和弹性公网ip属于两个实例，需要分别填写两个实例IDc.云主机退款时间预期1-3个工作日

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 大量资源报错502 (Bad Gateway)

**问题分类**: CDN > 访问下载

### 问题描述

GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:252     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:284     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:220     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:380     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:316     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:412     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:444     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:476     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:540     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:508     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:604     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:764     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:636     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:796     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:700     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:828     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:860     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)

### 客服解答

**客户**：GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:252     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:284     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:220     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:380     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:316     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:412     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:444     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:476     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:540     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:508     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:604     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:764     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:636     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:796     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:700     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:828     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)list_works:860     GET https://imgs.kusima.me/[REDACTED_PATH] 502 (Bad Gateway)

**客服**：您好抱歉久等了，调整了CDN覆盖节点，辛苦清理下本地dns缓存，稍后再观察看下

**客户**：你们这样不行啊，严重影响业务运行，好几个客户因为这个退款了

**客服**：您好非常抱歉给您造成不便，经确认是由于个别节点网络抖动导致的，异常节点已自动剔除下线，辛苦您清理下客户端dns缓存，稍后再观察看看

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 部分文件无法下载

**问题分类**: 对象存储 > 上传下载

### 问题描述

空间中为公共空间，10月24日起，间断性无法访问资源。

### 客服解答

**客户**：空间中为公共空间，10月24日起，间断性无法访问资源。

**客服**：您好有无法访问的链接什么 今天有复现到吗 这边看下

**客户**：刚刚才复现了，返回502错误，是多地均出现这种情况。 参考：GET https://ecp-work-order-prod.cdn.cgzj.cc/[REDACTED_PATH] HTTP/1.1Host: ecp-work-order-prod.cdn.cgzj.ccProxy-Connection: keep-aliveUpgrade-Insecure-Requests: 1User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[REDACTED_IP] Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7Accept-Encoding: gzip, deflateAccept-Language: zh-CN,zh;q=0.9HTTP/1.1 502 Fiddler - Connection FailedDate: Thu, 24 Oct 2024 10:59:10 GMTContent-Type: text/html; charset=UTF-8Connection: closeCache-Control: no-cache, must-revalidateTimestamp: 18:59:10.555[Fiddler] The connection to 'ecp-work-order-prod.cdn.cgzj.cc' failed. <br />Error: TimedOut (0x274c). <br />System.Net.Sockets.SocketException 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。 [REDACTED_IP]:80

**客服**：您好非常抱歉给您造成不便，经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您清理下客户端dns缓存，稍后再观察看看

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 解析有问题。

**问题分类**: CDN > 访问下载

### 问题描述

我在四川，四川联通，pingCDN域名节点是163.177.221.142，能给我解析到广东去？而且网站还打不开。。。

### 客服解答

**客户**：我在四川，四川联通，pingCDN域名节点是163.177.221.142，能给我解析到广东去？而且网站还打不开。。。[图片]

**客服**：您好非常抱歉给您造成不便，经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您清理下客户端dns缓存，稍后再观察看看

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 获取上传token时, returnBody可以写固定值吗? 服务端固定值不让客户端上传时另外修改

**问题分类**: 对象存储 > 上传下载

### 问题描述

1

### 客服解答

**客户**：1

**客服**：您好只要是json文本就可以[图片]

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 访问缓慢

**问题分类**: 对象存储 > 上传下载

### 问题描述

图片访问缓慢

### 客服解答

**客户**：图片访问缓慢

**客服**：您好麻烦给下访问慢的文件链接 这边测试下

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 主机无法释放

**问题分类**: 云主机 > 主机

### 问题描述

主机资源不能释放，释放按钮为灰色的，为什么不能释放呢？ID:i-hp3iasgn4oiknyk3tvia服务器Ip：[REDACTED_IP]

### 客服解答

**客户**：[图片]主机资源不能释放，释放按钮为灰色的，为什么不能释放呢？ID:i-hp3iasgn4oiknyk3tvia服务器Ip：[REDACTED_IP]

**客服**：您好可以通过退款的方式释放麻烦针对如下问题做一下填写确认：1.退款原因（以便我方改进产品不足）：2.申请退款的产品实例ID：3.已使用时长所对应的费用不退回，请您确认已知晓；4.代金券支付部分无法退回，请您确认已知晓：5.主机或实例是否已备份？若已备份，请回复“数据已备份”；若无需备份，请回复“数据无需备份” 。（退款后服务器实例立即被清除，数据不再保留，请提前备份数据）6.主机退款是将整个实例全部退订，不是单独退订主机升级的部分，请您确认知晓？注意：a.如需退款多个实例，需要注明多个实例ID，退款资源会按照填写上述表单为准b.云主机和弹性公网ip属于两个实例，需要分别填写两个实例IDc.云主机退款时间预期1-3个工作日

**客户**：1.退款原因（以便我方改进产品不足）： 获取区域IP，但通过IP查询后，该IP不属于对应区域2.申请退款的产品实例ID： i-hp3iasgn4oiknyk3tvia3.已使用时长所对应的费用不退回，请您确认已知晓；已知晓4.代金券支付部分无法退回，请您确认已知晓： 已知晓5.主机或实例是否已备份？若已备份，请回复“数据已备份”；若无需备份，请回复“数据无需备份” 。（退款后服务器实例立即被清除，数据不再保留，请提前备份数据） 数据无需备份6.主机退款是将整个实例全部退订，不是单独退订主机升级的部分，请您确认知晓？ 已知晓

**客服**：云主机和弹性公网ip属于两个实例，需要分别填写两个实例ID  ，您确认下IP退不退

**客户**：IP也要退掉

**客服**：好的

**客服**：您好，经查询，主机已释放了。弹性公网ip是按量计费的，您可以在弹性公网ip实例页面自行释放该ip。

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 河北区域夜间上传图片速度慢

**问题分类**: 对象存储 > 上传下载

### 问题描述

近几日  一到晚上19点以后  会出现图片上传缓慢的情况  只有河北的同事有这种情况，其他城市的同事没有遇到这种情况

### 客服解答

**客户**：近几日  一到晚上19点以后  会出现图片上传缓慢的情况  只有河北的同事有这种情况，其他城市的同事没有遇到这种情况

**客服**：您好，一、如果是客户端上传方式，首先要确认下您的设备网络环境是否ok1)  ping一下对应存储空间域名，例如 华东存储 ping up.qiniup.com 或者 upload.qiniup.com 看能否 ping 通。其他地区参考：https://developer.qiniu.com/[REDACTED_PATH] 测试设备的上行出口带宽（网页端或者服务端上传）https://www.speedtest.net/[REDACTED_PATH] 在服务器上 ping一下对应存储空间域名，例如 华东存储 ping up.qiniup.com 或者 upload.qiniup.com 看能否 ping 通。其他地区参考：https://developer.qiniu.com/[REDACTED_PATH] 核实下 服务器的出口带宽大小，理论上传速度 = 文件大小 / (出口带宽 / 8) s ，根据出口带宽和理论上传速度对比看下是否符合预期。三、判断是否是上传的cdn节点有问题。麻烦把 ping 到的节点信息提供给到我们，我们排查一下

**客户**：测试时间 10.24日 21：20一到晚上19点以后  会出现图片上传缓慢的情况河北 节点  希望老师帮忙处理一下[图片][图片]

**客服**：上传的文件大小是多少

**客户**：最大不超过10MB

**客户**：这是昨晚上传截图[图片]

**客服**：麻烦把 ping 到的节点信息提供给到我们，我们排查一下

**客户**：C:\Users\Administrator>ping uc.qiniuapi.com正在 Ping uc.qiniuapi.com [[REDACTED_IP]] 具有 32 字节的数据:来自 [REDACTED_IP] 的回复: 字节=32 时间=40ms TTL=50来自 [REDACTED_IP] 的回复: 字节=32 时间=40ms TTL=50来自 [REDACTED_IP] 的回复: 字节=32 时间=40ms TTL=50来自 [REDACTED_IP] 的回复: 字节=32 时间=40ms TTL=50153.99.246.131 的 Ping 统计信息:    数据包: 已发送 = 4，已接收 = 4，丢失 = 0 (0% 丢失)，往返行程的估计时间(以毫秒为单位):    最短 = 40ms，最长 = 40ms，平均 = 40msC:\Users\Administrator>ping up-z1.qiniup.com正在 Ping up-z1.qiniup.com [[REDACTED_IP]] 具有 32 字节的数据:来自 [REDACTED_IP] 的回复: 字节=32 时间=15ms TTL=51来自 [REDACTED_IP] 的回复: 字节=32 时间=15ms TTL=51来自 [REDACTED_IP] 的回复: 字节=32 时间=15ms TTL=51来自 [REDACTED_IP] 的回复: 字节=32 时间=15ms TTL=51221.194.151.135 的 Ping 统计信息:    数据包: 已发送 = 4，已接收 = 4，丢失 = 0 (0% 丢失)，往返行程的估计时间(以毫秒为单位):    最短 = 15ms，最长 = 15ms，平均 = 15msC:\Users\Administrator>ping iovip-z1.qiniuio.com正在 Ping bc-gate-io.qiniu.com [[REDACTED_IP]] 具有 32 字节的数据:来自 [REDACTED_IP] 的回复: 字节=32 时间=13ms TTL=55来自 [REDACTED_IP] 的回复: 字节=32 时间=13ms TTL=55来自 [REDACTED_IP] 的回复: 字节=32 时间=13ms TTL=55来自 [REDACTED_IP] 的回复: 字节=32 时间=14ms TTL=55110.242.48.123 的 Ping 统计信息:    数据包: 已发送 = 4，已接收 = 4，丢失 = 0 (0% 丢失)，往返行程的估计时间(以毫秒为单位):    最短 = 13ms，最长 = 14ms，平均 = 13msC:\Users\Administrator>ping rs-z1.qiniuapi.com正在 Ping rs-z1.qiniuapi.com [[REDACTED_IP]] 具有 32 字节的数据:来自 [REDACTED_IP] 的回复: 字节=32 时间=22ms TTL=50来自 [REDACTED_IP] 的回复: 字节=32 时间=22ms TTL=50来自 [REDACTED_IP] 的回复: 字节=32 时间=22ms TTL=50来自 [REDACTED_IP] 的回复: 字节=32 时间=21ms TTL=50110.242.48.107 的 Ping 统计信息:    数据包: 已发送 = 4，已接收 = 4，丢失 = 0 (0% 丢失)，往返行程的估计时间(以毫秒为单位):    最短 = 21ms，最长 = 22ms，平均 = 21msC:\Users\Administrator>ping rsf-z1.qiniuapi.com正在 Ping rsf-z1.qiniuapi.com [[REDACTED_IP]] 具有 32 字节的数据:来自 [REDACTED_IP] 的回复: 字节=32 时间=22ms TTL=50来自 [REDACTED_IP] 的回复: 字节=32 时间=22ms TTL=50来自 [REDACTED_IP] 的回复: 字节=32 时间=22ms TTL=50来自 [REDACTED_IP] 的回复: 字节=32 时间=22ms TTL=50110.242.48.107 的 Ping 统计信息:    数据包: 已发送 = 4，已接收 = 4，丢失 = 0 (0% 丢失)，往返行程的估计时间(以毫秒为单位):    最短 = 22ms，最长 = 22ms，平均 = 22msC:\Users\Administrator>ping api.qiniuapi.com正在 Ping kodo-elb-z0.qiniuapi.com [[REDACTED_IP]] 具有 32 字节的数据:来自 [REDACTED_IP] 的回复: 字节=32 时间=36ms TTL=50来自 [REDACTED_IP] 的回复: 字节=32 时间=35ms TTL=50来自 [REDACTED_IP] 的回复: 字节=32 时间=35ms TTL=50来自 [REDACTED_IP] 的回复: 字节=32 时间=35ms TTL=50124.160.115.103 的 Ping 统计信息:    数据包: 已发送 = 4，已接收 = 4，丢失 = 0 (0% 丢失)，往返行程的估计时间(以毫秒为单位):    最短 = 35ms，最长 = 36ms，平均 = 35ms[图片][图片]

**客服**：收到，我们排查下

**客服**：您好，可能是河北本地网络链路限制或者阻塞，目前检查这边出入口服务是没有限制的。存储空间支持开启传输加速功能：https://developer.qiniu.com/[REDACTED_PATH]

### 根因分析

**根本原因**: 客户端网络带宽限制或上传节点响应慢。

---

## 删除

**问题分类**: CDN > 配置问题

### 问题描述

www.hylegen.comhylegen.com请删除CDN对应的以上域名，状态长时间一直在处理中，

### 客服解答

**客户**：www.hylegen.comhylegen.com请删除CDN对应的以上域名，状态长时间一直在处理中，

**客户**：海禾西生物（科技）上海有限公司2024-10-24 20:22www.hylegen.comhylegen.com请删除CDN对应的以上域名，状态长时间一直在处理中，

**客服**：您好， 请稍等

**客户**：www.hylegen.comhylegen.com请删除CDN对应的以上域名，状态长时间一直在处理中。谢谢[图片]

**客服**：已经处理好了

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## ping网站大面积地区无法打开，不是我服务器的问题，我用服务器ip可以正常打开

**问题分类**: CDN > 访问下载

### 问题描述

ping网站大面积地区无法打开，不是我服务器的问题，我用服务器ip可以正常打开，这个状态维持一下午了

### 客服解答

**客户**：ping网站大面积地区无法打开，不是我服务器的问题，我用服务器ip可以正常打开，这个状态维持一下午了

**客户**：下午提交了个工单，没能解决，结果到现在这个点，404的地区更多了

**客服**：您好经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您清理下客户端dns缓存，稍后再观察看看

**客户**：收到！

**客服**：好的

### 根因分析

**根本原因**: CDN节点网络抖动导致部分用户访问异常,异常节点已被自动剔除下线。

---

## 能给我降低一下出站流量价格吗？

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

你好，我是做网盘的，出站流量价格能否降低一些？跟我的同行比，目前的价格太高了。

### 客服解答

**客户**：你好，我是做网盘的，出站流量价格能否降低一些？跟我的同行比，目前的价格太高了。

**客服**：您好给下您的联系方式 这边同步商务与您联系

**客户**：[REDACTED_EMAIL]

**客服**：目前非工作时间 这边记录下 明天商务会联系您对接

**客服**：商务未联系上您 麻烦给一个可联系的手机号

**客户**：[REDACTED_PHONE]

**客服**：好的 请保持电话通畅

**客服**：电话停机状态 您可以直接拨打400-808-9176转1号线联系我们

**客户**：刚电话你们了，没人接。待会你们打过来吧？

**客服**：直接拨打400-808-9176转1号线 会有同事对接

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 香港无法正常访问 CDN

**问题分类**: CDN > 访问下载

### 问题描述

有香港用户反馈无法访问网站，通过测速工具测试发现国内其他地区都能正常访问，只有香港不能访问。我自己亲测也是同样的问题

### 客服解答

**客户**：有香港用户反馈无法访问网站，通过测速工具测试发现国内其他地区都能正常访问，只有香港不能访问。我自己亲测也是同样的问题[图片]

**客服**：您好这个域名的覆盖范围是中国大陆地区 如果需要香港地区访问 可以调整覆盖范围为全球自 2020年10月20日起，控制台 -【域名管理】目前已支持域名覆盖区域（中国大陆、全球、海外）切换，您可以在[图片]点击『修改』自助切换。

**客户**：我知道覆盖范围是大陆，但之前能访问的，近期才变成不能访问的，这是为啥呢？

**客服**：把覆盖范围调整一下 再访问看看是否可以

**客户**：好的，明白啦

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 图片不显示，或者显示异常

**问题分类**: 对象存储 > 上传下载

### 问题描述

后台用户头像的图片，以前上传过的商品的图片，新上传的图片，显示为空白，铅酸小程序商品图像显示空白，图片显示一会正常一会不正常的

### 客服解答

**客户**：后台用户头像的图片，以前上传过的商品的图片，新上传的图片，显示为空白，铅酸小程序商品图像显示空白，图片显示一会正常一会不正常的

**客服**：您好给下图片链接地址 这边看下

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 视频手机端无法播放，电脑端正常播放

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

视频手机端无法播放，电脑端正常播放https://www.meishujia.net/[REDACTED_PATH]?nid=100

### 客服解答

**客户**：视频手机端无法播放，电脑端正常播放https://www.meishujia.net/[REDACTED_PATH]?nid=100

**客服**：您好给下无法正常播放的报错截图 这边看下

**客户**：好多天没登陆电脑，麻烦你了[图片][图片]

**客服**：您这个域名的证书过期了 换个新证书即可[图片][图片]

**客户**：传图慢了，多传了

**客户**：域名证书在哪弄新的？

**客服**：您好，手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/[REDACTED_PATH]

### 根因分析

**根本原因**: SSL证书已过期,需要重新申请或上传新的证书。

---

## 报MA00002发送失败是什么原因

**问题分类**: 云短信 > 短信发送问题

### 问题描述

发送失败报ma00002

### 客服解答

**客户**：发送失败报ma00002[图片]

**客户**：好几条都是网关黑名单

**客服**：您好这边后台核查下 请稍等

**客服**：签名需要报备运营商审批 审批通过后再发送 请耐心等待

**客户**：没理解  我的签名都审批通过了之前发送都是好好的

**客服**：给下您的法人身份证号 签名需要向运营商那边报备处理

**客户**：好的  我这边要一下

**客户**：[图片]提交审核的时候提供身份证号来着

**客户**：牛伟锋[REDACTED_ID_CARD_18]

**客户**：给您发过去了牛伟锋[REDACTED_ID_CARD_18]

**客户**：[图片]为什么会有发送成功也有发送失败的呢  如果是运营商那边的问题应该是全部都是失败啊

**客服**：这边帮您提交一下报备 报备通过后再发送

**客户**：好的

**客服**：好的

**客户**：报备通过了您记得给我反馈一下

**客服**：好的 已经提交报备审批 还没有生效 生效之后这边会工单同步您的

**客服**：已经报备通过 再次发送一下

**客户**：又发送失败了[图片]

**客服**：这边反馈下 请稍等

**客户**：好的

**客服**：被拦截 已经处理 您再看下

**客户**：后面还会被拦截吗  这样我以后都不知道发没发过去

**客服**：是运营商那边拦截的  短信发送失败的原因是多种的 您再观察下 有问题随时反馈我们

**客户**：好的

**客服**：好的

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 卡此界面

**问题分类**: CDN > 其他类咨询

### 问题描述

卡此界面

### 客服解答

**客户**：卡此界面[图片]

**客服**：您好您刷新页面再看下 后台看这个域名的状态是正常的

**客户**：域名正常，卡此界面数周了

**客服**：稍等

**客服**：您好，已处理，麻烦再看下

**客户**：现在新问题是配置修改不成功[图片]

**客服**：配置已下发了哈

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 加速域名SSL证书上传了八九个小时都没配置完成，催一下

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

加速域名SSL证书上传了八九个小时都没配置完成，催一下

### 客服解答

**客户**：加速域名SSL证书上传了八九个小时都没配置完成，催一下[图片][图片]

**客服**：您好已经帮您手动介入处理完成

**客户**：SSL设置了强制https，3个小时了，还是在配置中，也帮我介入处理一下

**客服**：已经处理好了

**客户**：上传https证书后，很多客户的手机无法播放，课程链接：https://xx.yuxuankeji.com/[REDACTED_PATH]?i=5591&c=entry&uid=449858&do=index&m=fy_lessonv2

**客服**：有报错吗 给下截图

**客户**：没有报错，应该时间直显示是0，播放不了。您那边可以试下能否播放

**客服**：播放哪个 您这个设置是付费才可以打开[图片]

**客户**：https://xx.yuxuankeji.com/[REDACTED_PATH]?i=5591&c=entry&id=157770629&do=lesson&m=fy_lessonv2&clear=1&sectionid=9818624&uid=475006

**客户**：这个链接您看下，设置有免费试听，可以直接打开播放

**客服**：测试可以正常播放[图片]

**客户**：有没可能跟地区有关，我这边也能播放，但客户反馈播放不了

**客服**：让客户把本地dns修改一下再访问 建议修改dns为 [REDACTED_IP]，备用选择 [REDACTED_IP]

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## ssl证书更新半天

**问题分类**: CDN > 证书问题

### 问题描述

ssl证书更新半天还没好

### 客服解答

**客户**：ssl证书更新半天还没好

**客服**：您好这边帮您手动介入处理下 请稍等

**客服**：已经处理完成

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 怎么获取Authorization

**问题分类**: CDN > 其他类咨询

### 问题描述

我需要获取Authorization，但是文档描述不清楚。例如我需要访问的接口地址：https://api.qiniu.com/[REDACTED_PATH] ,		"common_name": ,		"pri": ,		"ca": }那我应该怎么生成

### 客服解答

**客户**：我需要获取Authorization，但是文档描述不清楚。例如我需要访问的接口地址：https://api.qiniu.com/[REDACTED_PATH] <Name>,		"common_name": <CommonName>,		"pri": <Pri>,		"ca": <Ca>}那我应该怎么生成

**客户**：无

**客服**：您好是要用上传证书的接口吗 使用的哪种语言

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## ssl证书域名所有权验证未通过

**问题分类**: CDN > 证书问题

### 问题描述

设置了qny.lim14.com域名可以更换即将过期的ssl证书，也没有自动更换我手动申请了免费的ssl证书后，证书那里也选了部署cdn到qny.lim14.com域名上但是一直显示域名所有权验证未通过你们这上传图片，上传附件也是不行，要么失败，要么触发ip限制不让传了

### 客服解答

**客户**：设置了qny.lim14.com域名可以更换即将过期的ssl证书，也没有自动更换我手动申请了免费的ssl证书后，证书那里也选了部署cdn到qny.lim14.com域名上但是一直显示域名所有权验证未通过你们这上传图片，上传附件也是不行，要么失败，要么触发ip限制不让传了

**客服**：您好域名所有权验证未通过是您没有配置文件验证，验证通过才会签发证书请根据提示进行文件 TXT 验证，系统会自动轮询，轮询通过才会颁发证书参考文档：https://developer.qiniu.com/[REDACTED_PATH]

### 根因分析

**根本原因**: SSL证书已过期,需要重新申请或上传新的证书。

---

## 请问域名冻结是什么意思

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

dui xian这个域名冻结是什么意思？有什么影响，为什么会这样？

### 客服解答

**客户**：dui xian[图片]这个域名冻结是什么意思？有什么影响，为什么会这样？

**客服**：您好您空间绑定的测试域名已经在近期进行回收了，并且是无法恢复的。测试域名是七牛提供用于功能测试的域名，请勿用于线上生产环境，同时，测试域名仅有30天的生命周期，到期后会进行自动回收。我们会在回收前一周和回收当天向您发送回收告知邮件，您可以确认邮箱中的邮件核实具体回收时间。解决方法：回收测试域名对您的存储资源没有影响，不会删除您的资源，也不需要重新上传资源。您绑定自定义域名后，通过自定义域名访问即可。如果您的域名已经在工信部备案，请参考域名绑定教程：https://developer.qiniu.com/[REDACTED_PATH]

### 根因分析

**根本原因**: 域名ICP备案状态异常或未完成备案。

---

## 上传的mp4无法预览

**问题分类**: 对象存储 > 上传下载

### 问题描述

上传的MP4无法预览，前天晚上还可以正常预览的https://videos.cnppe.cn/[REDACTED_PATH] 这个视频下载到本地是可以正常预览的，但是在web上无法预览，

### 客服解答

**客户**：上传的MP4无法预览，前天晚上还可以正常预览的https://videos.cnppe.cn/[REDACTED_PATH] 这个视频下载到本地是可以正常预览的，但是在web上无法预览，

**客服**：您好，请稍等，这边帮您确认下

**客服**：您好，您说的web不能播放具体是指的什么呢，方便将具体的报错截图这边看下么

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 想开通传输加速

**问题分类**: 对象存储 > 上传下载

### 问题描述

开通传输加速

### 客服解答

**客户**：开通传输加速

**客服**：您好传输加速功能为收费项，请悉知价格参考：https://www.qiniu.com/[REDACTED_PATH]

**客户**：好的。确认开通。谢谢

**客服**：收到，稍等

**客服**：已开通

**客户**：好的 谢谢

**客户**：请问在哪里 可以看到了。上传域名是什么了

**客服**：参考 https://developer.qiniu.com/[REDACTED_PATH]

**客户**：好的谢谢

**客服**：好的

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 归档文件设置指定天数后被删除，如果在删除钱状态发生了改变，那么删除会不会失效？

**问题分类**: 对象存储 > SDK使用

### 问题描述

https://developer.qiniu.com/[REDACTED_PATH]

### 客服解答

**客户**：https://developer.qiniu.com/[REDACTED_PATH]

**客服**：您好，文件属性会默认携带，这个到期还是会删除的

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 上传自有证书出现报错

**问题分类**: CDN > 证书问题

### 问题描述

我上传的是通配符证书，错误信息如下[    [        {            "title": "请求 ID",            "content": "0oIIFlpQRIWuiQEY"        },        {            "title": "日志栈",            "content": "fusionicp;fusionsslcert:9/400"        }    ]]

### 客服解答

**客户**：我上传的是通配符证书，错误信息如下[    [        {            "title": "请求 ID",            "content": "0oIIFlpQRIWuiQEY"        },        {            "title": "日志栈",            "content": "fusionicp;fusionsslcert:9/400"        }    ]]

### 根因分析

**根本原因**: 域名ICP备案状态异常或未完成备案。

---

## 对象存储资费问题咨询

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

对象存储，主要用于播放一些100M左右的视频，如果每天要播放100次左右这样的视频，一个月的流量算下来需要多少费用！

### 客服解答

**客户**：对象存储，主要用于播放一些100M左右的视频，如果每天要播放100次左右这样的视频，一个月的流量算下来需要多少费用！

**客服**：您好，访问的话是产生访问流量的。100MB的视频播放一次就是100MB的流量的，10次就是1GB了，100次就是10GB流量费用了的，具体定价可以参考官网的CDN定价的

**客户**：就是这个页面是吗？每个用户每月10G容量，然后“标准存储每月免费 CDN 回源流量” 10G  额外的 0.15 元/GB是吗？我看还有一个 外网流出流量费用0.29 元/GB 是什么意思？是第三方网站应用链接地址播放的流量吗？

**客服**：您好，是CDN加速流量，不是回源流量，国内：HTTP协议CDN加速流量0.24/元每GB，HTTPS协议CDN加速流量0.28/元每GB外网流出流量就是使用自定义源站域名会产生的流量的

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 七牛云可以通过远程视频连接，直接上传吗

**问题分类**: 对象存储 > SDK使用

### 问题描述

视频文件，是一个远程链接地址，可以在不下载到本地服务器的情况下，直接将远程视频文件，通过php sdk，上传到七牛云视频中吗

### 客服解答

**客户**：视频文件，是一个远程链接地址，可以在不下载到本地服务器的情况下，直接将远程视频文件，通过php sdk，上传到七牛云视频中吗

**客服**：您好，您可以参考下这个接口文档的https://developer.qiniu.com/[REDACTED_PATH]

**客户**：有没有对应的 sdk提供的

**客服**：您好，您可以参考下这个demo的https://github.com/[REDACTED_PATH]

**客户**：好的，感谢！

**客户**：上面参考文档中的 callbackbody 自定义参数，要如何实现，不是通过表单提交的方式[图片]

**客服**：您好，callbackbody不支持自定义变量的。callbackbody是在生成上传token时传递，需要与callbackurl一起使用。

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 配置进度时间过长

**问题分类**: CDN > 配置问题

### 问题描述

域名配置时间过长

### 客服解答

**客户**：域名配置时间过长[图片]

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客户**：好的，处理好了请回复

**客服**：嗯嗯好的，还请稍等

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

**客户**：好的，谢谢

**客服**：嗯嗯不客气的

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 域名证书一直显示在配置中

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

我已经购买新的证书配置，还是给我弹域名证书要过期，点播证书已经好几天一直显示在配置中

### 客服解答

**客户**：我已经购买新的证书配置，还是给我弹域名证书要过期，点播证书已经好几天一直显示在配置中[图片][图片][图片]

**客户**：你好，在吗

**客服**：您好，请稍等

**客服**：您好，域名当前已处理完成

### 根因分析

**根本原因**: SSL证书已过期,需要重新申请或上传新的证书。

---

## 提示证书过期了

**问题分类**: CDN > 证书问题

### 问题描述

提示证书过期了，但是我记得我续费过了~

### 客服解答

**客户**：提示证书过期了，但是我记得我续费过了~

**客服**：证书是有有效期的，您可以重新申请一个新的证书部署到域名。

### 根因分析

**根本原因**: SSL证书已过期,需要重新申请或上传新的证书。

---

## 证书续签，域名不能访问了

**问题分类**: CDN > 证书问题

### 问题描述

证书续签，域名不能访问了

### 客服解答

**客户**：证书续签，域名不能访问了

**客服**：您好，请稍等

**客服**：您好，久等了，已处理完成

**客户**：还是不能正常访问

**客户**：https://images.scshangpu.com/[REDACTED_PATH]

**客户**：[图片]怎么还是没有部署成功呢[图片]

**客户**：有技术在处理吗？

**客服**：请稍等

**客户**：查到是哪里的问题了吗？

**客户**：有技术在处理吗？

**客户**：[图片]这个已经解析了 怎么提示让配置呢

**客服**：解析记录配置界面能截图给看下吗？

**客户**：[图片]这个就是

**客服**：有其他主机记录为 images 的解析配置吗

**客户**：没有的

**客户**：[图片][图片]这已经部署完了 怎么刷新还是要让部署呢

**客服**：您好，这个无需重复部署，已经部署成功了

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 海外访问非常慢

**问题分类**: CDN > 访问下载

### 问题描述

最近一段时间海外用户访问时加载非常慢

### 客服解答

**客户**：最近一段时间海外用户访问时加载非常慢

**客服**：稍等

**客服**：您好，代理节点测试能保持在毫秒级，基本符合预期的。[图片][图片]

**客服**：您好，是个别用户吗，还是某片区域的用户集中访问慢。可以提供下访问慢客户端ip，请求url，请求时间，这边具体分析

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 已设置防止盗链后，别人访问是否还耗费我们的流量？

**问题分类**: CDN > 流量计费问题

### 问题描述

因为平常未注意防护，被别有用人之人几个月前恶意上传一个文件，用作他们的批量网站的一个图片资源，结果形成盗链，每天晚上八点至十点之间集中访问，耗费我们的流量，昨天下午发现此问题，后来设置REFRER来阻止此问题，但是今天发现还是在访问，查日志，对方访问时已经已经返回403码阻止了对方的访问，但是流量计费是否还算作我们的计费？

### 客服解答

**客户**：因为平常未注意防护，被别有用人之人几个月前恶意上传一个文件，用作他们的批量网站的一个图片资源，结果形成盗链，每天晚上八点至十点之间集中访问，耗费我们的流量，昨天下午发现此问题，后来设置REFRER来阻止此问题，但是今天发现还是在访问，查日志，对方访问时已经已经返回403码阻止了对方的访问，但是流量计费是否还算作我们的计费？[图片][图片]

**客服**：您好，403也会产生访问量的防止别人恶意访问你的资源产生大量流量，单纯的从cdn的层面上来处理，是不能完全规避掉的。CDN上支持多种防盗链配置，不同的防盗链适用于不同的应用场景，建议可以在 融合cdn => 域名管理 => 配置 => 访问控制 中设置1：referer防盗链： 只有携带了相应referer 请求头 的 http请求才能访问资源，但是对于技术来说，referer都是可以伪造的，存在一定的风险2：时间戳防盗链，url带着e和token参数访问，e为过期时间，但是只要捕获到了url就可以访问资源了，只适用于访问xx次的场景3：回源鉴权，这个你们可以尝试下，每次访问cdn图片时，会携带你们自己定义的访问参数去你们自己的服务器上鉴权，只有你们服务器鉴权通过，返回 httpcode=200 ，才会将图片资源给用户访问，否则无法返回图片4：IP黑白名单，这个适合某一个网段内的ip访问资源，不适合官网使用，只有在 ip 白名单中的用户才可以访问你们的图片参考文档：https://developer.qiniu.com/[REDACTED_PATH]

**客户**：好的，明白了，修改程序仿佛比较麻烦，暂时考虑考虑怎么弄吧。限制IP的方式也不可行，对方的客户IP太多了，无法控制

**客服**：好的 您结合下您的业务情况考虑下方案进行配置

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 上传视频报错502

**问题分类**: 对象存储 > 上传下载

### 问题描述

上传报错

### 客服解答

**客户**：[图片]上传报错

**客户**：用的是php+nginx的 上传大文件就不行了。哪里需要设置还是怎么的？

**客户**：POST /index.php/admins/Common/uploads.html HTTP/1.1＂ 502 552 ＂https://video.3r8.cn/[REDACTED_PATH] ＂Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[REDACTED_IP] Safari/537.36＂

**客服**：您好，您这个502不是请求的七牛上传域名。应该是上传到您服务器失败了 video.3r8.cn，您可以检查下您这个源站服务器七牛这边能支持上传大文件的，且没有限制php sdk：https://developer.qiniu.com/[REDACTED_PATH]

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 下载文件

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

下载文件出现 (502) 错误的网关

### 客服解答

**客户**：下载文件出现 (502) 错误的网关

**客服**：您好，您这边将下载链接给一下，这边看下确认一下

**客户**：这个情况经常会出现，过一段时间又正常了。https://cdn.ad2800.cn/[REDACTED_PATH]

**客服**：您好，这边看昨晚上该域名线路节点有网络波动的情况的，这边已经优化了的，您这边可以刷新下本地dns缓存看下后续再观察下的

**客户**：这种情况是不定时出现的，这个是同一个客户的文件，上午和晚上都有出现。其他的客户也出现过。

**客服**：您好，是本地请求到了旧节点的缓存了的，这边目前一下将其清理了的，需要刷新一下本地dns缓存再看下的，这个昨天晚上的时候就已经处理了

**客户**：今天下午开始文件下载慢，无响应。

**客服**：您好帮忙给一个资源外链，这边具体看下

### 根因分析

**根本原因**: 客户端DNS缓存未及时更新,仍解析到旧的CDN节点地址。

---

## 返回{"error":"bad gateway: EOF"}

**问题分类**: CDN > 刷新缓存问题

### 问题描述

{"error":"bad gateway: EOF"}

### 客服解答

**客户**：{"error":"bad gateway: EOF"}

**客户**：[图片] 其他文件存在， 但 apk 缓存不了

**客户**：[图片]{"error":"failed to read response body, progress: 0/58370474, err: unexpected EOF"}  另外一种响应内容

**客服**：您空间下有这个文件的：https://cdnpic.qipeipu.com/[REDACTED_PATH]

**客服**：您空间下有这个文件的：https://pic.qipeipu.com/[REDACTED_PATH]

**客户**：我是走回源的。 但不知道为什么回源拿不到文件

**客服**：您好，您这边将回源host也就是nginx站点设置为您的CDN域名看下的

**客户**：我能知道哪个回源IP抛出的异常吗？

**客服**：您好，这个502的话获取不到，建议您可以调整一下镜像回源源站策略测试看下的

**客户**：定位到问题了

**客服**：您好，是什么原因呢？

**客户**：源站新增的 nginx 成为了默认源站。 但这个源站的配置有点问题，导致回源异常。

**客服**：嗯嗯好的

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 新增域名一直处理中

**问题分类**: CDN > 配置问题

### 问题描述

对象存储绑定域名，状态一直在处理中，已经过了半小时了。

### 客服解答

**客户**：对象存储绑定域名，状态一直在处理中，已经过了半小时了。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 上传慢

**问题分类**: 对象存储 > 上传下载

### 问题描述

对象存储的空间，如果选择在亚太新加坡，从国内上传，会不会慢

### 客服解答

**客户**：对象存储的空间，如果选择在亚太新加坡，从国内上传，会不会慢

**客服**：您好，这个会变慢的

**客户**：如果原来选择了亚太新加坡，能再把空间转到国内吗

**客服**：您好，这个空间是不能改变的，这个你们后面可以将文件迁移到国内即可

**客户**：迁移有什么批量上传和下载的工具吗

**客服**：您好，您这边是需要进行数据迁移还是批量操作呢？

**客户**：数据量不大，迁移和批量操作都可以

**客服**：您好，那您这边可以使用最新的图形化工具kodo-browser上传/下载试下，支持批量管理。https://developer.qiniu.com/[REDACTED_PATH]

### 根因分析

**根本原因**: 客户端网络带宽限制或上传节点响应慢。

---

## 下载xuexisd空间下所有文件

**问题分类**: 对象存储 > 上传下载

### 问题描述

如何下载xuexisd空间下所有文件

### 客服解答

**客户**：如何下载xuexisd空间下所有文件

**客服**：您好，七牛后台界面操作不支持批量下载的，批量下载，可以通过以下几种方式实现：方法1.调用list接口，遍历空间，获得空间内的文件信息，然后下载。代码逻辑是先调用 list 接口获得文件名的集合，再与空间域名拼接成url(https://domain/[REDACTED_PATH] 是空间域名，key是文件名)，循环调用 download 方法下载文件。https://developer.qiniu.com/[REDACTED_PATH] qshell 工具进行批量下载操作；qshell 工具下载地址：https://github.com/[REDACTED_PATH] 工具批量下载命令：https://github.com/[REDACTED_PATH] 的 qdownload 命令时，如果指定使用CDN域名下载时，建议将 public 参数置为true，下载时击中CDN缓存时产生CDN流量费用，未击中CDN缓存回源下载资源时产生的是CDN回源流量费用；如不指定，下载资源产生的全部是CDN回源流量费用。方法3:使用图形化工具kodo browser工具批量下载，勾选想要下载的文件/目录后点击【下载】即可。参考：https://developer.qiniu.com/[REDACTED_PATH]

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 国外空间速度慢

**问题分类**: 对象存储 > 上传下载

### 问题描述

我要用你们的存储空间，想用国外空间，但是需要在国内维护，但是速度太慢，有没有一种方法让国内维护的时候速度快一点。只是维护用，有几个人能用就行了。

### 客服解答

**客户**：我要用你们的存储空间，想用国外空间，但是需要在国内维护，但是速度太慢，有没有一种方法让国内维护的时候速度快一点。只是维护用，有几个人能用就行了。

**客服**：您好，国内使用海外慢是符合预期的，国内使用国内的话才是正常的，您这边是访问慢吗？链接给一下这边测试看下

**客户**：我知道正常，但是这给我的维护带来了麻烦。维护的人是在国内的。有没什么方案方便维护人员用。

**客服**：您好，十分抱歉跨境链路是无法优化的，维护人员在国内的话建议您这边使用下国内的存储空间和域名的

**客户**：你这种客服完全可以用机器人替代。我说的意思是维护人只有2个人，客户是国外客户。你让我用国内存储空间。

**客服**：您好，还请您这边可以将问题描述清楚一下的这种情况维护人员需要进行什么操作？维护什么？是访问慢吗？链接给一下这边测试看下

**客户**：维护是要国内上传商品。类似跨境电商。针对的是国外。但是技术人员在国内。现在是上传个图片都特别慢。

**客服**：您好，上传慢的话您需要看下是哪种的一、如果是客户端上传方式，首先要确认下用户的设备网络环境是否ok1) 让客户 ping一下对应存储空间域名，例如 华东存储 ping up.qiniup.com 或者 upload.qiniup.com 看能否 ping 通。其他地区参考：https://developer.qiniu.com/[REDACTED_PATH] 测试客户设备的上行出口带宽（网页端或者服务端上传）https://www.speedtest.net/[REDACTED_PATH] 在服务器上 ping一下对应存储空间域名，例如 华东存储 ping up.qiniup.com 或者 upload.qiniup.com 看能否 ping 通。其他地区参考：https://developer.qiniu.com/[REDACTED_PATH] 核实下 服务器的出口带宽大小，理论上传速度 = 文件大小 / (出口带宽 / 8) s ，根据出口带宽和理论上传速度对比看下是否符合预期。三、判断是否是上传的cdn节点有问题。麻烦把 ping 到的节点信息提供给到我们，我们排查一下

**客户**：再不好好说话我准备投诉你。你这叫解答问题吗？你这叫自言自语，复制粘贴。

**客服**：您好，我在解决您上传慢的问题的，上传慢首先需要看是客户端上传还是服务端上传，需要针对性的去确认您的问题，还望您这边理解一下配合一下的

### 根因分析

**根本原因**: 客户端网络带宽限制或上传节点响应慢。

---

## 图片无法预览，访问链接也访问不了

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

https证书未过期 域名解析正常https://i1.nzw6.com/[REDACTED_PATH]

### 客服解答

**客户**：https证书未过期 域名解析正常https://i1.nzw6.com/[REDACTED_PATH]

### 根因分析

**根本原因**: SSL证书已过期,需要重新申请或上传新的证书。

---

## 关于http换成https

**问题分类**: CDN > 配置问题

### 问题描述

最早我们应用的是http，现在换成https已经失效了，能否协助处理一下。

### 客服解答

**客户**：最早我们应用的是http，现在换成https已经失效了，能否协助处理一下。[图片]

**客服**：您好，手动申请并使用免费SSL证书步骤如下，需要申请证书后才能部署的1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/[REDACTED_PATH]

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 退资源包

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

如何退未使用的回流资源包？

### 客服解答

**客户**：如何退未使用的回流资源包？

**客服**：您好，您这边可以将订单号给一下这边确认一下

**客户**：订单号：e0f7a36826f3a989b2e67b3e6853ab29

**客服**：您好，您稍等这边确认一下

**客服**：您好，这边商务经理杨军为您提交退款申请了，还请耐心等待审核通过后即可退回的

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 回源流量

**问题分类**: 对象存储 > 上传下载

### 问题描述

购买了回源流量包没效果,可以不可以退款.而且现在流量费用太高,买什么套餐才能便宜点.最好打电话联系,这费用伤不起,打算换移动的了

### 客服解答

**客户**：购买了回源流量包没效果,可以不可以退款.而且现在流量费用太高,买什么套餐才能便宜点.最好打电话联系,这费用伤不起,打算换移动的了

**客服**：麻烦您提供一个电话联系方式，这边安排商务与您联系

**客户**：[REDACTED_PHONE]

**客服**：您好，稍等下，这边同步下商务和您联系下

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 上传证书失败

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

上传证书失败

### 客服解答

**客户**：[图片]上传证书失败

**客服**：您好复制 .crt 或者 .pem 后缀的文件内容到证书内容 （公钥），复制 .key 后缀结尾的内容到 证书私钥 。

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 账户提现，发票额度不够的问题

**问题分类**: 账户与财务 > 发票问题

### 问题描述

你好，想问下为什么提现不了，我提现之前已经申请了退7千的发票，红冲发票也已经开好了，为什么提现7千提现不了，而且发票额度只有3千多，已经申请退票7千了发票额度正常不是7千吗，这是什么原因，麻烦你们核对清楚数据，谢谢。

### 客服解答

**客户**：你好，想问下为什么提现不了，我提现之前已经申请了退7千的发票，红冲发票也已经开好了，为什么提现7千提现不了，而且发票额度只有3千多，已经申请退票7千了发票额度正常不是7千吗，这是什么原因，麻烦你们核对清楚数据，谢谢。[图片][图片]

**客服**：您好给下您的联系方式 这边商务跟进处理

**客户**：[REDACTED_PHONE]林小姐

**客服**：好的 请保持电话通畅

**客户**：已经重新提交提现申请，麻烦审核尽快提现谢谢

**客服**：原路提现预计需3～5个工作日，线下提现预计需要5~15个工作日，七牛打款后具体到账时间以银行为准，请耐心等待

**客服**：已经打款了 请注意查收

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## HTTPS配置

**问题分类**: CDN > 配置问题

### 问题描述

HTTPS配置中免费申请证书 不能确定 是为什么？

### 客服解答

**客户**：[图片]HTTPS配置中免费申请证书 不能确定 是为什么？[图片]

**客户**：域名：img.huitongzx.cn

**客服**：您好，这个你们开启 HTTP/2 后即可[图片]

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 访问七牛云的静态资源巨慢

**问题分类**: 对象存储 > 上传下载

### 问题描述

我们最近发现放在七牛云上的资源访问巨慢，甚至有时候打开一个JS要超过一分钟

### 客服解答

**客户**：我们最近发现放在七牛云上的资源访问巨慢，甚至有时候打开一个JS要超过一分钟

**客户**：图片和附件都上传不了，你们这个网站做的太垃圾了

**客服**：您好，麻烦提供一两个访问慢的资源地址，这边分析

**客户**：https://resource-cdn.xdfgk.cn/[REDACTED_PATH]

**客服**：您好，首次访问需要回源，预取后再观察下呢预取方法请参考：1. api 接口地址：https://developer.qiniu.com/[REDACTED_PATH] portal.qiniu.com 控制台进行资源预取，点击左侧cdn => 刷新预取3. url 资源预取，全网生效 10min 左右

**客户**：这个都放在七牛云上好几年了，不是首次

**客户**：而且我们现在是每个人打开都有机会特别慢，慢到一二分钟才能加载

**客服**：您好，麻烦稍等

**客服**：您好，尝试了请求几次没有复现慢请求，这边先帮您优化了下，您再观察下呢

**客户**：https://m.xdfgk.cn/[REDACTED_PATH]?exchange_products_id=738409041295089664https://m.xdfgk.cn/exchange_manage/?exchange_products_id=738409041295089664你访问这个地址，用新设备打开时，有很多几率会卡半天，发现就是那二个JS加载慢

**客服**：这边测试是秒开的。

**客服**：[图片]

### 根因分析

**根本原因**: CDN回源链路出现问题或源站响应缓慢。

---

## 帮忙查询一下文件是在何时被删除的

**问题分类**: 对象存储 > 上传下载

### 问题描述

帮忙查询一下文件是在何时删除的，其上传时间是2023-12-25 12:03:34。文件如下：https://img.loafish.com/[REDACTED_PATH]

### 客服解答

**客户**：帮忙查询一下文件是在何时删除的，其上传时间是2023-12-25 12:03:34。文件如下：https://img.loafish.com/[REDACTED_PATH]

**客服**：您好大致的丢失时间有吗 这边过滤下日志

**客户**：昨天客户开始反馈有图片不显示，今天表示大量的图片都不显示。可以查询当前10月的试试看

**客服**：好的 日志过滤需要一些时间 辛苦耐心等待

**客服**：您好查询这个文件是在1009号通过java sdk删除的 具体日志可以查看 https://dn-odum9helk.qbox.me/[REDACTED_PATH]?attname=1381471689.xlsx

**客户**：谢谢

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 域名提示删除，

**问题分类**: CDN > 配置问题

### 问题描述

域名还有，为什么提示域名删除，如何恢复正常视使用

### 客服解答

**客户**：域名还有，为什么提示域名删除，如何恢复正常视使用[图片]

**客服**：无量域名，持续三个月未产生用量会自动清理。您需要恢复使用，重新创建该域名即可。

**客户**：如何从新创建域名，又操作流程吗，

**客服**：您好，绑定CDN加速域名图文教程文档，您可以参考：https://developer.qiniu.com/[REDACTED_PATH]

**客户**：按照上面那个流程还是没操作明白

**客服**：您好，查看您已经创建了域名了，您是要加速您的网站吗，还是网页中的图片视频等静态资源地址呢

**客户**：对，我要在网站上链接七牛云的视频，在网站能点击播放，以前链接过，这不是原先的域名过期了吗，现在新建域名，怎么链接的流程忘了

**客服**：您好，你网站现在还在运行中吗，现在用的是哪个域名，你有个qiniu.aobeicm.com域名在用的，看看是不是这个

**客户**：问题已解决感谢

**客服**：好的

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 字体cdn提示我跨域，前几天还是正常的

**问题分类**: CDN > 访问下载

### 问题描述

前几天字体还是正常，帮忙看看，域名是https://www.whpdesign.com/ 配置的存储是 https://whp.ovmao.com/

### 客服解答

**客户**：前几天字体还是正常，帮忙看看，域名是https://www.whpdesign.com/ 配置的存储是 https://whp.ovmao.com/[REDACTED_PATH]

**客户**：图片是正常的，但是字体不行 cors[图片]

**客服**：您好跨域要在cdn域名侧配置 把存储的跨域关闭掉 参考 https://developer.qiniu.com/[REDACTED_PATH]

**客户**：可以了

**客服**：好的

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 证书过期如何更新

**问题分类**: CDN > 证书问题

### 问题描述

我的证书过期了,新的下来了,如何更新

### 客服解答

**客户**：我的证书过期了,新的下来了,如何更新

**客服**：您好，您这边到域名管理下找到https配置，然后修改配置更换最新证书即可的

### 根因分析

**根本原因**: SSL证书已过期,需要重新申请或上传新的证书。

---

## 接入CDN后接口会出现502

**问题分类**: CDN > 其他类咨询

### 问题描述

https://www.puyuanmaoshan.com/[REDACTED_PATH]?r=common%2Fattachment%2Fupload上传接口https://www.puyuanmaoshan.com/web/shoproot.php?r=common%2Fattachment%2Flist&page=0&type=video&is_recycle=0&keyword=查询接口通过上传接口上传完成以后,页面会自动调用查询接口刷新数据通过CDN访问,在上传完成以后,查询接口会出现502

### 客服解答

**客户**：https://www.puyuanmaoshan.com/[REDACTED_PATH]?r=common%2Fattachment%2Fupload上传接口https://www.puyuanmaoshan.com/web/shoproot.php?r=common%2Fattachment%2Flist&page=0&type=video&is_recycle=0&keyword=查询接口通过上传接口上传完成以后,页面会自动调用查询接口刷新数据通过CDN访问,在上传完成以后,查询接口会出现502

**客服**：您好cdn域名是用来访问资源的 不是上传处理 您用的是哪个接口出现的502

**客户**：单独访问查询接口不会报错,只有在调用上传接口以后页面自动刷新会报错

**客户**：cdn域名是用来访问资源的 不是上传处理 你这句话是回复我哪个描述?

**客服**：调用上传接口不需要用到cdn域名 用每个区域固定的上传域名即可 您这步操作是怎么处理的

**客服**：客户 ping一下对应存储空间域名，例如 华东存储 ping up.qiniup.com 或者 upload.qiniup.com 看能否 ping 通其他地区参考：https://developer.qiniu.com/[REDACTED_PATH]

**客服**：可以ping一下对应存储空间域名，例如 华东存储 ping up.qiniup.com 或者 upload.qiniup.com 看能否 ping 通其他地区参考：https://developer.qiniu.com/[REDACTED_PATH]

**客户**：用户->CDN->站点->对象存储用户不直接上传到对象存储

**客服**：意思是用fetch的方式上传到存储吗

**客户**：[图片]然后这个超时,之前工单有给我调整,为啥还是20秒呢?

**客服**：后台帮您确认了 tcp 链接时间是30秒，回源加载的超时时间是60秒 这个没有调整过

**客户**：那这个20秒超时是哪里的问题?我大概知道是什么问题了,服务器上传到对象存储桶太慢了用户上传文件会先暂存在服务器,服务器再上传到对象存储桶,服务器上传的过程中,查询接口就会保持长链接,然后20秒超时就GG了

**客服**：您这个上传交互太多 建议直接上传落存储 这个体验感会比较好

### 根因分析

**根本原因**: CDN回源链路出现问题或源站响应缓慢。

---

## 域名一直处于配置中

**问题分类**: CDN > 配置问题

### 问题描述

cdnlq.7qrx.comcdnzq.7qrx.com

### 客服解答

**客户**：cdnlq.7qrx.comcdnzq.7qrx.com

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 接下来如何操作？

**问题分类**: CDN > 配置问题

### 问题描述

接下来要如何操作 绑定？

### 客服解答

**客户**：[图片]接下来要如何操作 绑定？

**客服**：您好，您需要创建您自己的CDN域名使用的，点击上方添加域名创建的，这个是测试域名的

**客户**：要如何对应相关信息[图片][图片]

**客服**：您好，重新添加记录的，添加完成后点击验证的，完成后即可通过的记录类型选择：TXT主机记录：复制主机记录记录值：复制记录值的[图片]

**客户**：这个要怎么配置[图片]

**客服**：再添加一条CNAME的记录记录类型：CNAME主机记录：cdn记录值：点击未配置后面的小链接复制记录值即可

**客户**：后面的图片访问是通过cdn.survey-plat.top访问还是survey-plat.top？

**客服**：这个的cdn.survey-plat.top

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 图片水印字体的支持

**问题分类**: 智能多媒体 > 图片处理

### 问题描述

字体不支持数字123、英文字母。在国内完全不适用啊。这个文字汉字部分是最柔和的了，突然发现没有适用性Droid Sans Fallback

### 客服解答

**客户**：字体不支持数字123、英文字母。在国内完全不适用啊。这个文字汉字部分是最柔和的了，突然发现没有适用性Droid Sans Fallback

**客服**：稍等

**客服**：抱歉无法支持，版权问题

**客户**：文字水印，字体可以支持备用字体这种写法吗？中文字体基本都可以实现，但是不带数字就太麻烦了

**客服**：不支持的https://image.baiducpt.com/[REDACTED_PATH]?imageMogr2/auto-orient/thumbnail/!800x800r/gravity/center/crop/800x800|watermark/3/image/a29kbzovL2IyYi1iYWlkdWNwdC90cGwvMG0zYy5wbmc=/dx/0/dy/0/ws/1/text/IOS8geS4mmFzMSA=/fontsize/920/fill/IzE3MTYxNg==/gravity/NorthWest/dx/60/dy/33不带字体和字体样式可以吗，这样可以显示数字和字母

**客户**：默认字体太丑了， 我们就是希望使用这个字体。

**客服**：您好，抱歉，这个还无法支持的。

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 咨询归档删除的资费

**问题分类**: 对象存储 > 其他类咨询

### 问题描述

当前有一批数据都迁移到了特定的bucket若将bucket转为深度存储一周后直接删除bucket，会产生提前删除文件的资费吗

### 客服解答

**客户**：当前有一批数据都迁移到了特定的bucket若将bucket转为深度存储一周后直接删除bucket，会产生提前删除文件的资费吗

**客服**：您好，会产生的深度归档存储，Object 最短存储期限为 180 天，早于 180 天删除、修改、覆盖 Object，需要补足未满 180 天的剩余天数的存储费用，超过 180 天不需要补。定价：https://www.qiniu.com/[REDACTED_PATH]

**客户**：那么不产生额外费用的情况下是否可以 当前标准存储30天后转为低频访问存储 30天之后转为深度归档 180天之后再删除bucket呢

**客户**：中间是否需要转为归档直读存储呢

**客服**：按您需求转存储类型，系统机制上没有特殊条件，您直接从标准转到深度归档都可以的。标准，低频和归档直读是可以直接访问的，深度归档需要解冻后才能访问。

**客户**：我描述的方案会有额外的费用么

**客服**：不会产生额外的费用，存储超过最短期限，只会产生对应存储的费用

**客户**：好的

**客服**：您好，您这边还有其他问题吗

**客户**：如果归档之后，要恢复的话恢复的维度是单个文件还是整个bucket呢

**客服**：您好，是单个文件级别的解冻恢复。

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

## 数据迁移，被清空了文件目录，是否可以恢复？

**问题分类**: 对象存储 > 数据迁移

### 问题描述

操作jxn-zsb空间tiku/problem目录下文件(其还有2级目录)移动到jxnedu空间app-xiaojiatiku/topic/下，移动后jxn-zsb空间tiku/problem目录下的2级目录消失，能否恢复？

### 客服解答

**客户**：操作jxn-zsb空间tiku/problem目录下文件(其还有2级目录)移动到jxnedu空间app-xiaojiatiku/topic/下，移动后jxn-zsb空间tiku/problem目录下的2级目录消失，能否恢复？

**客服**：您好，清空的文件目录是不支持恢复的

**客户**：为什么会自动把目录给删掉

**客服**：控制台的目录实际是虚拟目录，是基于文件名的路径自动扩展出来的虚拟文件夹，实际不存在

### 根因分析

**根本原因**: 需要进一步分析具体情况。

---

