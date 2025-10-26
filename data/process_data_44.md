# 七牛云客服Q&A知识库 - Part 44

本文档包含 114 个客服问答记录

---

## 免费证书申请，文件验证什么时候通过？

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

创建订单后，点击详情，底部显示域名所有权验证未通过。

### 客服解答内容

1. 您好，『域名所有权验证未通过』是需要您点击详情，然后根据提示进行文件或者 DNS TXT 验证，系统会自动轮询，轮询通过才会颁发证书参考文档：https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

### 根本原因分析

证书问题、文件问题、域名问题

---


## 七牛云存储 为什么上传文件目录后 会有一个未命名文件夹

**问题分类**: 对象存储｜上传下载

### 详细问题描述

七牛云存储 为什么上传文件目录后 会有一个未命名文件夹

### 客服解答内容

1. 您好，您上传时，指定key不要以/开头，就以你第一个文件夹名称开头就可以，开头斜杠去掉。

2. 您好，进入空间，在空间设置中删除空间

### 根本原因分析

配置问题、文件问题

---


## 短信11月1号开始无法发送

**问题分类**: 云短信｜短信发送问题

### 详细问题描述

你好，模板ID： [REDACTED_PHONE]17848320  ，短信11月1号开始无法发送提示502 错误

### 客服解答内容

1. 您好，这边资源包是否可以看到呢https://portal.qiniu.com/financial/orders/respack-mgr/current

2. 您好，您刷新看下资源包是否可以显示，是否可以正常发送

3. 您好，您这边是否是网络有问题？ping下sms.qiniuapi.com看下

4. 您好，没有的，您这边使用的是什么语言的SDK？什么版本呢

5. 您好，没有的，api这边没有修改的您看下您的sms.qiniuapi.com这个是否有进行本地host？

### 根本原因分析

缓存问题、证书问题、网络问题

---


## 资源包当月概括为什么空的

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

资源包当月概括为什么空的

### 客服解答内容

1. 您好，稍等下，资源包更新延迟，这边帮您处理下

### 根本原因分析

缓存问题、资源包问题

---


## 使用upload.qiniup.com上传图片成功但是为返回hash和key

**问题分类**: 对象存储｜上传下载

### 详细问题描述

使用upload.qiniup.com上传图片成功但是为返回hash和key，七牛后台能看到上传成功的图片。上传代码：code...        const file = {
            uri: asset.uri, // 获取到的图片URI
            type: asset.type, // MIME类型
            name: asset.fileName , // 文件名
          };
          const myHeaders = {
            'Content-Type': 'multipart/form-data', // 注意设置Content-Type,
            "Host": "upload.qiniup.com",
            "sec-ch-ua-platform": "\"macOS\"",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[REDACTED_IP] Safari/537.36",
            "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "accept": "*/*",
            "origin": "https://public.buydance.com",
            "sec-fetch-site": "cross-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://public.buydance.com/",
            "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "priority": "u=1, i"
          };
          const formData = new FormData();
          formData.append("file", file); // 上传的文件
          formData.append("key", "cms_share/20241031/"+asset.fileName); // 资源名称
          formData.append("token", token); // 上传凭证
          formData.append("fname", asset.fileName);
          formData.append("resource_key", "cms_share/20241031/"+asset.fileName);
          console.log('formdata=', JSON.stringify(formData));
          // 发送请求
         return fetch('https://upload.qiniup.com/', {
            method: 'POST',
            headers: myHeaders,
            body: formData,
            redirect: "follow"
          });相关日志：code... LOG  formdata= {"_parts":[["file",{"uri":"file:///data/user/0/com.dataoke.union/cache/rn_image_picker_lib_temp_5d290c99-5f49-4124-8329-bb131cd62433.jpg","type":"image/jpeg","name":"dtk[REDACTED_PHONE]164zsEtmU1Jh.jpg"}],["key","cms_share/20241031/dtk[REDACTED_PHONE]164zsEtmU1Jh.jpg"],["token","293gst8MyH6rkMR59msNf_ZNhLMKSNPPaxdz_xah:tDqDTUx8D88JRTooU8BPAE73Zso=:eyJzY29wZSI6InN0YXRpY3Jlc291cmNlLWZmcXVhbi1jb20iLCJkZWFkbGluZSI6MTczMDQyNzEwOX0="],["fname","dtk[REDACTED_PHONE]164zsEtmU1Jh.jpg"],["resource_key","cms_share/20241031/dtk[REDACTED_PHONE]164zsEtmU1Jh.jpg"]]}
 LOG  res== {"type":"default","status":200,"ok":true,"statusText":"","headers":{"map":{"access-control-allow-origin":"*","access-control-expose-headers":"X-Log, X-Reqid","cache-control":"no-store, no-cache, must-revalidate","content-length":"97","content-type":"application/json","date":"Fri, 01 Nov 2024 02:01:50 GMT","pragma":"no-cache","server":"openresty/[REDACTED_IP]","vary":"Origin","x-alt-svc":"h3=\":443\"; ip=\"[REDACTED_IP]\"; ma=3600","x-content-type-options":"nosniff","x-log":"X-Log","x-reqid":"ExUAAAAUFya-tQMY","x-svr":"UP"}},"url":"https://upload.qiniup.com/","bodyUsed":false,"_bodyInit":{"_data":{"size":97,"offset":0,"blobId":"8883dbc7-0d09-4951-a740-be82a5665ac9","__collector":{}}},"_bodyBlob":{"_data":{"size":97,"offset":0,"blobId":"8883dbc7-0d09-4951-a740-be82a5665ac9","__collector":{}}}}

### 客服解答内容

1. 您好时间戳过期了 重新生成一下[图片]

2. 用新token上传有报错吗 您这边上传用的哪种语言 这边给您找个demo测试下

3. 您好，可以使用七牛的 js-sdk上传，可以参考这个

4. 很抱歉这边没有权限介入用户的操作 建议您每一步上传处理打印下返回的信息  需要检查下程序逻辑

### 根本原因分析

配置问题、缓存问题、证书问题

---


## 访问慢

**问题分类**: CDN｜其他类咨询

### 详细问题描述

https://mademine-user.maiyuan.online/20241031/FxLGt50WFYVZcQDXEbmMvombPXbMQTgu这个域名资源在美国访问很慢，其他区域访问也是

### 客服解答内容

1. 我们优化了下海外的回源策略，您可以后续再观察下

### 根本原因分析

证书问题、域名问题

---


## CDN域名配置进度反馈

**问题分类**: CDN｜配置问题

### 详细问题描述

域名m.yqudown.com配置CDN进度半个小时未完成，麻烦帮忙看一下

### 客服解答内容

1. 您好，这边手动介入下处理，麻烦稍等。

### 根本原因分析

配置问题、域名问题

---


## 麻烦处理一下证书问题

**问题分类**: CDN｜证书问题

### 详细问题描述

已经有证书，但是数据无法正常访问

### 客服解答内容

1. 您好给下无法访问的链接地址 这边看下

2. 您好，后台看已经部署好了

### 根本原因分析

证书问题、网络问题、域名问题

---


## ssl.c.weihaidi.cn   域名有什么问题吗？一直显示续费中

**问题分类**: CDN｜证书问题

### 详细问题描述

ssl.c.weihaidi.cn   域名有什么问题吗？一直显示续费中

### 客服解答内容

1. 您好ssl.c.weihaidi.cn 这个域名的证书临近过期 可以申请新证书部署配置手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide4.升级HTTPS配置https://developer.qiniu.com/fusion/manual/4952/https-configuration注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

### 根本原因分析

配置问题、证书问题、域名问题

---


## 打包失败，提示文件GET不到，但是文件正常

**问题分类**: 智能多媒体｜自定义数据处理

### 详细问题描述

{
  "id": "z0.01z001d59vkhtfgieb00mupxaf002k3t",
  "pipeline": "1381853895.default.sys",
  "code": 3,
  "desc": "The fop is failed",
  "reqid": "zPEAAADJEl6_fgMY",
  "inputBucket": "fotoo",
  "inputKey": "205810[REDACTED_PHONE]50146818",
  "items": [
    {
      "cmd": "mkzip/4/encoding/dXRmLTg=|saveas/Zm90b28644CQMeOAkS3nq6Xlv4PnrZHmoqborrLlpb3kuK3lm73mlYXkuovnrKzkuInlsYrkuZbni5Dni7jmna_lsJHlubTlhL_nq6XmlYXkuovlpKfkvJrmiqXlkI3kuK0yMDI0MTAzMTE3MTM1Ny56aXA=",
      "code": 3,
      "desc": "The fop is failed",
      "error": "execute fop cmd failed: failed to GET http://qn004.pfotoo.com/FgbsLuZtgGhx4bZfzWdVa5d4xnLA",
      "errorIndex": 0,
      "returnOld": 0
    }
  ],
  "creationDate": "2024-10-31T17:14:02.234999218+08:00"
}

### 客服解答内容

1. 您好，您当前重试下，看下是否可以呢

### 根本原因分析

文件问题

---


## 亲，想问下充值的7777啥时候返券呀

**问题分类**: 账户与财务｜其他类咨询

### 详细问题描述

准备新购买几个CDN流量包，等券下来能叠加一下么

### 客服解答内容

1. 您好，您方便提供一个电话联系方式么，这边安排商务与您联系

### 根本原因分析

资源包问题

---


## 一直在配置

**问题分类**: CDN｜配置问题

### 详细问题描述

一直在配置

### 客服解答内容

1. 您好，久等了，配置已下发

### 根本原因分析

配置问题

---


## 空间里全部设备都离线了

**问题分类**: 视频监控｜其他类咨询

### 详细问题描述

麻烦尽快处理，空间全部视频设备都离线了

### 客服解答内容

1. 您好，sip地址都更新过了吗为了提升网络服务质量，我方近期将对机房进行运维调整，计划于 2024 年 10 月 31 日 下线旧 SIP 服务器并启用新的 SIP 服务器，届时连接至旧 SIP 服务器的设备将无法正常使用。

2. 您好，sip地址都更新过了吗确认下当前是设备 sip地址是否使用的是：[REDACTED_IP] 或 [REDACTED_IP]

3. 您好，麻烦您那边修改到新的sip地址 用这个47.98.160.100

4. 您好，是的，需要调整下，调整到新的sip地址。

### 根本原因分析

网络问题

---


## 账号注销

**问题分类**: 账户与财务｜账户问题

### 详细问题描述

更换账号，手机号不用了

### 客服解答内容

1. 您好，目前注销可以在控制台操作https://portal.qiniu.com/developer/user/security目前用户自助注销需满足以下所有条件：1、账号为普通账号（非财务父子账号、OEM账号）2、账号下实时消费无产品用量、无消费金额（数据需要您自己删除）对象存储：https://portal.qiniu.com/kodo/bucketCDN：https://portal.qiniu.com/cdn/domain3、账号下无各种欠费实时消费明细（查看您当月消费）https://portal.qiniu.com/financial/bills/estimated-consume如有欠费，将在下月5号出账、8号扣款，结算后，您再提交账号注销。4、账号下没有正在处理的提现审批https://portal.qiniu.com/financial/withdraw5、账号当前没有被冻结注意：账号注销后，账号无法找回

### 根本原因分析

证书问题、账号问题、文件问题

---


## 文档转换接口问题

**问题分类**: 智能多媒体｜其他类咨询

### 详细问题描述

我看到我的消费里面还有文档转换的扣费，这代表文档转换接口是还可以使用吗？如果可以使用，还可以使用多久，您们的政策是怎么样的？目前文档接口使用的费用是怎么计算，有没有对于的文档介绍。另外之前的文档转换使用文档好像已经下线了，目前有新的文档吗？

### 客服解答内容

1. 您好，已经对外下线，具体的收费您可以在您的实时消费那边看下，是会有说明的https://portal.qiniu.com/financial/bills/estimated-consume

2. 您好，还能使用，但是没有接新，没有维护了，建议还是进行迁移吧

### 根本原因分析

证书问题、SDK问题

---


## 上传视频到对像存储，如正常在小程序端播放？

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

你好，因为小程序的云储存对接了七牛云，想了解一下上传到对像云的视频，可以正常在小程序端播放吗？要达到播放流畅又能省流，具体设置步骤是怎样的？是不是我在对像云新建个转码样式，当有视频上传是就会自动转码？这样就可以流畅播放？流量又如何计算？谢谢

### 客服解答内容

1. 您好，您的视频格式可以支持播放的话，就可以播放您可以降低视频分辨率，但是会降低画质不是转码样式，是任务触发器参考文档https://developer.qiniu.com/dora/6489/task-workflow

2. 您好，任务触发器设置后，小程序端是不是不需要再对接额外的接口？是的并且客户端观看是自动调取转码后的视频观看？短时间没办法，转码需要一定时间如果您的转码后是同名文件的话，会将转码后的文件覆盖掉老文件，但是如果之前有访问老文件，会有cdn缓存，无法直接访问到新文件，您还需要刷新下cdn缓存

3. 您好，如果缓存时间您没有修改，默认是30天刷新设置变量，可以设置为{{.key}}[图片]

4. 您好，转码任务id不是工作流这边复制https://portal.qiniu.com/dora/media-gate/task

5. 您好，您的输出截图提供下，应该是保存原名的

### 根本原因分析

配置问题、缓存问题、证书问题

---


## 用了cdn经常获取的ip是0.0.0.0

**问题分类**: CDN｜配置问题

### 详细问题描述

用了cdn经常获取的ip是0.0.0.0，日志里面经常有为0的ip

### 客服解答内容

1. 您好，客户端ip吗？您下载我们的日志看下呢也有吗？https://portal.qiniu.com/dcdn/log

2. 您说的是获取到我们cdn节点是这个吗？如果是这样的话，应该是没有请求到我们这边，是不是有报错？

3. 您好，直接解压，拖动到浏览器就可以查看

### 根本原因分析

证书问题、文件问题、域名问题

---


## 域名配置半小时未完成

**问题分类**: CDN｜配置问题

### 详细问题描述

新增域名一直显示配置中

### 客服解答内容

1. 您好这边帮您手动介入处理下 请稍等

2. cdn.zjfenghong.cc的证书验证您没有配置 证书未签发无法升级至https

3. 免费证书验证步骤：https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide

### 根本原因分析

配置问题、证书问题、域名问题

---


## SSL证书续费

**问题分类**: 账户与财务｜计费问题

### 详细问题描述

2024年11月16号ssl证书到期需要续费

### 客服解答内容

1. 您好，付费证书您重新购买就好如果需要更换免费证书可以参考手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide4.升级HTTPS配置https://developer.qiniu.com/fusion/manual/4952/https-configuration注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

### 根本原因分析

配置问题、证书问题、域名问题

---


## 反馈之前存储的一张图片找不到了

**问题分类**: 对象存储｜上传下载

### 详细问题描述

https://image.317hu.com/nc_cloud/njgl.png这个图片今天突然反馈说访问不了，查看了oss上没这个图片，对应的存储空间是qqhlimage帮忙查询下记录是否之前有这个png

### 客服解答内容

1. 您好，1.该文件是否有进行过删除操作？您检查一下上传时候是否指定了 deleteAfterDays，或者是存储空间设置了生命周期( https://developer.qiniu.com/kodo/manual/3699/life-cycle-management )2.是否有对文件做过 move 操作 ( https://developer.qiniu.com/kodo/api/1288/move )3.是否有大致的文件上传时间和删除时间

2. 后台看您这个空间每天都有在删除文件处理  这边帮您查询下近期的删除日志

3. 最近一段时间没有查到这个文件，近期您的文件是通过java 删除的  操作IP是 [REDACTED_IP]

### 根本原因分析

配置问题、证书问题、文件问题

---


## a.meishujia.net  我已经安装了证书也签发了，但是还是没部署上去

**问题分类**: CDN｜证书问题

### 详细问题描述

a.meishujia.net  我已经安装了证书也签发了，但是还是没部署上去，然后上传那里也点了也说不对

### 客服解答内容

1. 您好这个域名的证书过期了 您需要申请一个新的证书去部署手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide4.升级HTTPS配置https://developer.qiniu.com/fusion/manual/4952/https-configuration注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

### 根本原因分析

配置问题、证书问题、文件问题

---


## https问题

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

为什么上传了新的ssl证书，已经配置完了，https还是提示证书已过期？

### 客服解答内容

1. 您好，证书上传了之后需要部署到域名。https://portal.qiniu.com/certificate/ssl#cert在证书管理这边，选择您新上传到证书，右侧点击部署，部署到域名即可

### 根本原因分析

配置问题、证书问题、文件问题

---


## 访问不了

**问题分类**: CDN｜配置问题

### 详细问题描述

配置好，访问不了

### 客服解答内容

（客服已协助处理）

### 根本原因分析

配置问题

---


## 手机端app

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

有没有手机app跟阿里云一样可以手机端管理在线文档，cdn等等的手机app，网页端有没有h5网页的控制台平时在外突发事件，手机端访问控制台很难使用app也没有，小程序也不支持控制文件或者查看文件

### 客服解答内容

1. 您好，目前我们还没有手机端appweb端搜索七牛云官网登录，或者这边控制台登录页面登录：https://sso.qiniu.com/

### 根本原因分析

证书问题、账号问题、文件问题

---


## 视频文件上传后播放时没有图像

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

视频文件上传后播放时没有图像，只有声音https://online.sxhcwh.com/2%E3%80%81%E8%AF%A6%E8%A7%A3m2%E5%8A%9F%E8%83%BD.mp4这个是链接，放到浏览器中只有声音没有图形。https://online.sxhcwh.com/1%E3%80%81%E6%90%AD%E5%BB%BA996%E5%BC%95%E6%93%8E%E6%9C%AC%E5%9C%B0%E6%95%B0%E6%8D%AE%E5%BA%93%E5%8D%95%E6%9C%BA%E7%8E%AF%E5%A2%83.mp4这个就好使，是正常的。这种情况我应该怎么调整

### 客服解答内容

1. 您好，视频一般有编码格式和封装格式。我们常说的 “MP4 格式” 是一种视频封装格式，比较常见的视频编码格式有 H264（大部分浏览器支持）、MPEG-4（大部分浏览器不支持）、H265（大部分浏览器不支持）等。就目前的视频市场环境来说，使用以下方案的视频兼容性最好：视频封装格式：MP4； 视频编码格式：H264； 音频编码格式：AAC 或 MP3。建议使用七牛的转码接口处理：https://developer.qiniu.com/dora/manual/1248/audio-and-video-transcoding-avthumb已经上传的文件可以通过持久化数据处理转码，您可以在对应后端语言的github文档中找到对应的pfop demo：https://developer.qiniu.com/dora/manual/1291/persistent-data-processing-pfopTip：如果您不清楚如何使用转码接口1.可以使用控制台的转码样式，在上传前进行处理。https://developer.qiniu.com/dora/6486/submit-transcoding-task-quickly2.针对已上传的文件转码，也可以通过qshell工具进行pfop处理，使用详情参考https://github.com/qiniu/qshell/blob/master/docs/pfop.md。qshell account 此处填写ak 此处填写sk 此处填写自定义的用户名 （ak sk可以在控制台右上角的个人面板，密钥管理里找到）

2. 没事的，有什么问题您再反馈

### 根本原因分析

证书问题、文件问题、SDK问题

---


## 设备异常

**问题分类**: 视频监控｜其他类咨询

### 详细问题描述

3101[REDACTED_PHONE]54506

### 客服解答内容

1. 您好，稍等下，这边核实下

2. 您好，在线拉流有什么报错吗

3. 您好，点击启用拉流没有反应是吗，也没有报错？

4. 您好，您的空间都开启了按需拉流的，没有人观看就会离线的

5. 您好，您的空间都开启了按需拉流的，视频流没有人观看就会离线的

### 根本原因分析

配置问题、直播问题

---


## 能否把relang-all空间下的douyin/video 这个目录的数据删除掉

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

能否把relang-all空间下的douyin/video 这个目录的数据删除掉，这个比较着急，占用量大概有30G，太大了，想要快速的删掉，

### 客服解答内容

1. 您好，您可以通过qshell批量删除，三条命令就可以了。1.先下载qshell工具并使用qshell account 命令登陆账户。下载及安装文档 https://developer.qiniu.com/kodo/tools/1302/qshellwindows环境下安装qshell教程 https://developer.qiniu.com/kodo/kb/5545/windows-environment-installation-qshell-tutorial2.使用listbucket2命令列举出空间内您需要删除的资源[图片]命令文档 https://github.com/qiniu/qshell/blob/master/docs/listbucket2.md3.使用batchdelete命令批量删除第2步列举出的列表文件。例如 qshell batchdelete --force 空间名 -i result.txt命令文档 https://github.com/qiniu/qshell/blob/master/docs/batchdelete.md注意：主动删除资源不可以恢复，请慎重

2. 这边授权加白的删除是删除整个空间 不是只删除部分文件的

3. 控制台的目录实际是虚拟目录，是基于文件名的路径自动扩展出来的虚拟文件夹，实际不存在

4. 导出需要一些时间  预估要到下午了 这边处理好后会工单发给您

5. 文件太多了需要时间 目前已经处理好了 在您的存储空间里 https://img-qiniuyun.relangdata.cn/list.csv

### 根本原因分析

证书问题、文件问题

---


## 放行广告标签

**问题分类**: 人工智能｜内容安全

### 详细问题描述

将涉及到广告的标签放行，因为我本身做的就是一个圈子网站

### 客服解答内容

1. 您好，稍等下，这边同步下

2. 您好，已经调整，您再看下

### 根本原因分析

其他问题

---


## cname配置后，还未生效？

**问题分类**: CDN｜证书问题

### 详细问题描述

提示cname未配置，cname我已经在阿里云配置了，什么情况？

### 客服解答内容

1. 您好后台看证书已经部署好了 是域名的cname解析没有配置[图片]

2. 您配置的是证书的cname解析现在要配置的是域名的cname解析  主机记录img 记录值 img-maitoutiao-com-idvfir6.qiniudns.com

### 根本原因分析

配置问题、证书问题、域名问题

---


## 账户余额对不上

**问题分类**: 账户与财务｜账户问题

### 详细问题描述

我充值了180元，花费了125.07买了一个CDN流量包。余额还剩20多，怎么算都对不上

### 客服解答内容

1. 您好查看上月账单明细：您可以登录七牛云管理控制台 - 财务中心 - 账单和消费详情，点击账单编号查看详细的消费明细：https://portal.qiniu.com/financial/summary查看实时消费明细：您可以登录七牛云管理控制台 - 财务中心 - 实时消费明细：https://portal.qiniu.com/financial/estimated-consume如果您对某个部分有疑问，可以截图到工单中，这边帮您解释下

### 根本原因分析

证书问题、账号问题、资源包问题

---


## 存储数据用的测试域名到期如何续期

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

存储数据用的测试域名，一个月就会到期，如果我想继续使用的话该怎么操作付费，我没有自己的域名，有没有什么简单的方法，如购买七牛云的什么空间服务之类？

### 客服解答内容

1. 您好，测试域名过期后，需要您到域名厂商 购买域名，在我们这边绑定使用，没有其他方法哈。

### 根本原因分析

证书问题、文件问题、域名问题

---


## 视频实时转码不生效

**问题分类**: 智能多媒体｜音视频处理

### 详细问题描述

原视频地址：https://qlinedu-oss.custma.top/test.mp4?e=1730431896&token=[REDACTED_KEY]&token=[REDACTED_KEY]

### 客服解答内容

1. 您好，换个其他视频试下，是您这个视频开头有点问题，处理后播放读取第一个片读不到数据。

2. 您好，现在是过期了，刚刚这边测试访问能访问到的，不是403的。您重新生成一个链接，换个设备访问试试。

3. url已经不同了，你需要重新url签算，而不是直接在签算后链接里加处理参数

4. 因为您是私有的空间，链接需要签算后访问。拼接了m3u8处理参数，再对链接私有签算签算：https://developer.qiniu.com/kodo/1656/download-private

5. 每个url签算出来的token是不一样的，是基于url签算的。https://qlinedu-oss.custma.top/%E9%80%BB%E8%BE%91%E7%AC%AC%E4%B8%89%E8%AE%B2%20%E5%8A%A0%E5%BC%BA%E5%89%8A%E5%BC%B1%EF%BC%883%29.mp4

### 根本原因分析

配置问题、缓存问题、证书问题

---


## 删除web.qoocam.net加速域名的进度卡住了

**问题分类**: CDN｜配置问题

### 详细问题描述

删除web.qoocam.net加速域名的进度卡住了

### 客服解答内容

（客服已协助处理）

### 根本原因分析

文件问题、域名问题

---


## 对象存储服务收费标准咨询

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

1、能否提供9月份对象存储服务的明细，PUT/GET请求明细2、视频上传到对象存储服务后（上传、使用上传后的链接播放这个流程）包含哪些收费项、收费标准是什么、是否提供收费明细（例：视频播放时长等）

### 客服解答内容

1. 您好，无法提供一个月的，可以提供您某一天一个小时的日志如果需要完整的日志，后续可以开通下空间日志空间日志，访问日志：https://developer.qiniu.com/kodo/8546/set-the-space-log事件通知，上传删除等：https://developer.qiniu.com/kodo/8610/dev-event-notification收费文档，你可以参考下https://portal.qiniu.com/financial/price?product=kodo

### 根本原因分析

证书问题、文件问题

---


## 域名审批（ecmp.coonga.cn）

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

麻烦  域名（ecmp.coonga.cn）审批通过下   谢谢！

### 客服解答内容

1. 您好，这边手动介入下处理，麻烦稍等。

2. 您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

域名问题

---


## SSL证书审核

**问题分类**: CDN｜证书问题

### 详细问题描述

请加速审核，谢谢

### 客服解答内容

1. 已经处理完成 您再看下

### 根本原因分析

证书问题

---


## qshell工具使用问题

**问题分类**: 对象存储｜工具使用

### 详细问题描述

qshell 命令怎么引用参数

### 客服解答内容

1. 您好，可以参考下https://github.com/qiniu/qshell/blob/master/docs/listbucket2.md

2. qshell不支持变量的，您得给到确定的值，然后还有空间名称需要指定下

3. 获取 2018-10-30 到 2018-11-02 上传的文件qshell listbucket2 --start 2018-10-30 --end 2018-11-03 <Bucket>

### 根本原因分析

配置问题、证书问题、文件问题

---


## 相同 key 上传以后马上下载可能会下载到老的数据

**问题分类**: 对象存储｜上传下载

### 详细问题描述

想咨询一下是否有办法可以避免上传后马上下载确保下载的是最新数据。比如我有个 key： refs/latest，上传了新数据内容，但是马上下载 refs/latest 后得到的可能是之前的老数据，如何避免这种情况？比如使用 key：refs/latest?r=随机数 是否能避免？

### 客服解答内容

1. 您好同名文件覆盖上传的话由于存在 CDN 缓存，会导致您访问的还是旧文件，您可以先清除下 CDN 缓存，然后清除本地浏览器缓存进行访问1、CDN 刷新缓存方法请参考：https://developer.qiniu.com/fusion/kb/1325/refresh-the-cache-and-the-effect-of-time方法1: portal.qiniu.com 控制台刷新缓存，点击左侧融合cdn => 刷新预取方法2: api 接口地址：https://developer.qiniu.com/fusion/api/1229/cache-refreshTip : url 刷新，全网生效 10min 左右，目录刷新需要 30min 左右2、清除本地缓存方法添加随机参数进行访问 或者 禁用浏览器缓存[图片]

2. 空间siyuan-cloud 绑定的是cdn域名 访问下载走的是cdn的策略

3. 链接后加随机数去本地缓存看下是否符合预期

4. 您那边程序侧是通过上传策略设置的覆盖上传逻辑吗

5. 链接后拼接随机数去除本地缓存看下 应该是您本地有缓存导致的

### 根本原因分析

配置问题、缓存问题、证书问题

---


## 设置waf问题

**问题分类**: CDN｜配置问题

### 详细问题描述

你好，https://assets.10lun.com/xml/tenlun.xml根据合作方反馈，以上资源不能被正常抓取到。

### 客服解答内容

1. 您好很抱歉目前这边暂时不支持配置waf功能

### 根本原因分析

配置问题、证书问题

---


## 磁盘扩容咨询

**问题分类**: 云主机｜主机

### 详细问题描述

我买了两块磁盘，一块100，一块300，服务器查询也能查询到有两块磁盘，但是我宝塔上面只能监测到100G得这块，另外一块300得读取不到请我我要把这块300得磁盘也使用起来，是需要扩容还是什么样的操作，扩容我看还需要再次收费，是我选择的不对，还是就是需要这么操作

### 客服解答内容

1. 您好，需要分区扩容文件系统，可以参考下扩容后操作：https://developer.qiniu.com/qvm/7417/online-expansion-cloud-disk-linux#3

### 根本原因分析

证书问题、文件问题

---


## 域名处理时间长

**问题分类**: CDN｜配置问题

### 详细问题描述

修改缓存配置时间过长

### 客服解答内容

（客服已协助处理）

### 根本原因分析

配置问题、缓存问题

---


## cdn 异常

**问题分类**: CDN｜访问下载

### 详细问题描述

后端是S3，什么情况下会有500以上的错？特别是502

### 客服解答内容

1. 您好，这边看的5xx是在图片处理机器这边产生了耗时较长，请求超时产生的5xx您这边如果没有强依赖图片处理相关，可以域名配置中关闭了图片瘦身和图片处理后再观察下。

### 根本原因分析

配置问题、网络问题、域名问题

---


## 无法添加域名

**问题分类**: 对象存储｜上传下载

### 详细问题描述

无法添加域名

### 客服解答内容

1. 您好，您这边创建域名有什么报错吗？还是有什么问题

### 根本原因分析

域名问题

---


## 资源使用 资源到期是否有接口可以查看

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

资源使用 资源到期是否有接口可以查看

### 客服解答内容

1. 您好，资源没有到期一说的，您是需要查看最后访问时间吗？

2. 您好，资源包没有查看的api，快到期会给您发送邮件提醒的

### 根本原因分析

资源包问题、SDK问题

---


## 混淆后闪退

**问题分类**: 对象存储｜SDK使用

### 详细问题描述

No virtual method n(JLjava/lang/String;)J in class Lorg/json/JSONObject; or its super classes (declaration of 'org.json.JSONObject' appears in /apex/com.android.art/javalib/core-libart.jar)                                                                                                    	at com.qiniu.android.storage.serverConfig.ServerConfig.(ServerConfig.java:17)                                                                                                    	at com.qiniu.android.storage.serverConfig.ServerConfigCache.getConfigFromDisk(ServerConfigCache.java:30)                                                                                                    	at com.qiniu.android.storage.serverConfig.ServerConfigMonitor.monitor(ServerConfigMonitor.java:16)                                                                                                    	at com.qiniu.android.storage.serverConfig.ServerConfigMonitor.access$100(ServerConfigMonitor.java:1)                                                                                                    	at com.qiniu.android.storage.serverConfig.ServerConfigMonitor$1.run(ServerConfigMonitor.java:5)                                                                                                    	at com.qiniu.android.transaction.TransactionManager$Transaction.handleAction(TransactionManager.java:24)                                                                                                    	at com.qiniu.android.transaction.TransactionManager$Transaction.access$000(TransactionManager.java:1)                                                                                                    	at com.qiniu.android.transaction.TransactionManager.handleTransaction(TransactionManager.java:1)                                                                                                    	at com.qiniu.android.transaction.TransactionManager.handleAllTransaction(TransactionManager.java:19)                                                                                                    	at com.qiniu.android.transaction.TransactionManager.timerAction(TransactionManager.java:8)                                                                                                    	at com.qiniu.android.transaction.TransactionManager.access$100(TransactionManager.java:1)                                                                                                    	at com.qiniu.android.transaction.TransactionManager$1.run(TransactionManager.java:3)                                                                                                    	at java.util.TimerThread.mainLoop(Timer.java:563)                                                                                                    	at java.util.TimerThread.run(Timer.java:513)

### 客服解答内容

1. 您好这个是做哪步操作时出现的报错

2. 给下复现过程说明 这边排查下

3. 升级下sdk版本试试  目前最新版是7.17

4. 好的 这边同步安卓工程师看下 请稍等

5. 在确认中 有进展会同步您

### 根本原因分析

缓存问题、SDK问题

---


## 访问不能命中

**问题分类**: CDN｜访问下载

### 详细问题描述

https://pvn.longpean.com/[REDACTED_PHONE]20_2024110157787_0.png?imageView2/0/w/350https://ptw.longpean.com/[REDACTED_PHONE]04_2024103157638_0.png?imageView2/0/w/350cdn访问不能命中缓存

### 客服解答内容

1. 您好，有命中缓存的[图片]

### 根本原因分析

缓存问题、证书问题

---


## 修改 HTTPS 配置处理中，长时间未配置完成

**问题分类**: CDN｜配置问题

### 详细问题描述

修改 HTTPS 配置处理中，强制https长时间未配置完成

### 客服解答内容

1. 您好这边帮您手动介入处理下 请稍等

2. 您好这边帮您手动介入处理下 请稍等

### 根本原因分析

配置问题、证书问题

---


## 选错了，退订

**问题分类**: 云主机｜主机

### 详细问题描述

订单cc9d4d9add74e6226bc7e11157ab0576选错了，麻烦帮我退订

### 客服解答内容

1. 您好，麻烦针对如下问题做一下填写确认：1.退款原因（以便我方改进产品不足）：2.申请退款的产品实例ID：3.已使用时长所对应的费用不退回，请您确认已知晓；4.代金券支付部分无法退回，请您确认已知晓：5.主机或实例是否已备份？若已备份，请回复“数据已备份”；若无需备份，请回复“数据无需备份” 。（退款后服务器实例立即被清除，数据不再保留，请提前备份数据）6.主机退款是将整个实例全部退订，不是单独退订主机升级的部分，请您确认知晓？注意：a.如需退款多个实例，需要注明多个实例ID，退款资源会按照填写上述表单为准b.云主机和弹性公网ip属于两个实例，需要分别填写两个实例IDc.云主机退款时间预期1-3个工作日

2. 好的 这边帮您提交流程审批处理

3. i-uf68h838zs65jt12opa3 已经退款完成eip-uf6n03o25rrnelucgncqm——是按量付费的实例 控制台停用即可

4. 刷新页面再看下 已经退了

### 根本原因分析

缓存问题

---


## 申请 SSL 免费证书配置时间很长？

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

昨天晚上申请了免费证书，到现在都还没有配置成功，希望尽快处理一下

### 客服解答内容

（客服已协助处理）

### 根本原因分析

配置问题、证书问题

---


## 对象存储外链无法使用

**问题分类**: 对象存储｜上传下载

### 详细问题描述

同时我先前sftw空间创建的外链地址也无法使用：http://skd2vim9o.hn-bkt.clouddn.com/kafka/2.11-2.4.0/kafka_2.11-2.4.0.tgz

### 客服解答内容

1. 您好，新创建的空间会分配一个测试域名，测试域名有效期为1个月。测试域名过期后，您可以绑定自己的域名后再访问使用。绑定CDN加速域名图文教程文档，您可以参考：https://developer.qiniu.com/fusion/manual/4939/the-domain-name-to-access

### 根本原因分析

证书问题、域名问题

---


## 注销账号

**问题分类**: 账户与财务｜账户问题

### 详细问题描述

原手机号已丢失

### 客服解答内容

1. 您好，目前注销可以在控制台操作https://portal.qiniu.com/developer/user/security目前用户自助注销需满足以下所有条件：1、账号为普通账号（非财务父子账号、OEM账号）2、账号下实时消费无产品用量、无消费金额（数据需要您自己删除）对象存储：https://portal.qiniu.com/kodo/bucketCDN：https://portal.qiniu.com/cdn/domain3、账号下无各种欠费实时消费明细（查看您当月消费）https://portal.qiniu.com/financial/bills/estimated-consume如有欠费，将在下月5号出账、8号扣款，结算后，您再提交账号注销。4、账号下没有正在处理的提现审批https://portal.qiniu.com/financial/withdraw5、账号当前没有被冻结注意：账号注销后，账号无法找回

### 根本原因分析

证书问题、账号问题、文件问题

---


## 免费 from 自动催单

**问题分类**: CDN｜证书问题

### 详细问题描述

长时间处于域名发布环节

### 客服解答内容

1. 您好，这边手动介入下处理，麻烦稍等。

2. 您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

域名问题

---


## 域名配置进度很慢，感觉不太正常

**问题分类**: CDN｜证书问题

### 详细问题描述

域名配置进度很慢，感觉不太正常

### 客服解答内容

1. 您好，这边手动介入下处理，麻烦稍等。

### 根本原因分析

配置问题、域名问题

---


## 配置卡住了

**问题分类**: CDN｜配置问题

### 详细问题描述

取消

### 客服解答内容

1. 您好已经将您的域名回滚处理

### 根本原因分析

域名问题

---


## 对象储存免费空间额度是多少

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

对象储存免费空间额度是多少

### 客服解答内容

（客服已协助处理）

### 根本原因分析

其他问题

---


## 华东-浙江 云储存在西藏无法访问.

**问题分类**: 对象存储｜上传下载

### 详细问题描述

华东-浙江 云储存在西藏无法访问.

### 客服解答内容

1. 您好，1、麻烦提供下您的 ip、dns 信息，和cdn节点信息，这边代理测试下可以通过访问这个链接 http://ping.huatuo.qq.com/ 获取本地的 ip 和 dns 信息，在检测域名这边输入下cdn域名，点击提交检测，然后截图通过工单提交给我们[图片]2、建议使用 chrome 浏览器，按照下述文档获取下 remote adress(对端节点ip)，request header(客户端请求头) 以及 response header(服务端响应头)信息，方便我们查询分析问题。https://developer.qiniu.com/fusion/kb/1478/how-to-access-network-in-the-browser-request-information

### 根本原因分析

证书问题、网络问题、域名问题

---


## qshell批量删除失败

**问题分类**: 对象存储｜工具使用

### 详细问题描述

您好，    请帮忙看下，批量删除失败是怎么回事？[zwtx@VM-0-16-centos bak]$ qshell batchdelete openwhy -i todelete.txt[W]   Input ihigjc to confirm operation:scan error:unexpected newline[I]  job dir:/home/zwtx/.qshell/users/openwhy/batchdelete/135bfdf509141e82e473fe1dca61875d, there is a cache related to this command in this folder, which will also be used next time the same command is executed. If you are sure that you don’t need it, you can delete this folder.--------------- Batch Result ---------------              Total:         0            Success:         0            Failure:         0            Skipped:         0           Duration:         1s--------------------------------------------

### 客服解答内容

1. 您好报错是本地缓存的问题 您清除一下

2. 另外给下您的todelete.txt 这边看下

3. 本地检查一下有没有同名的todelete.txt文件，或者换个文件名重试下 注意ak sk输入完整

4. 把todelete.txt 换成result1.txt试下

5. 把--force 这个带上运行命令

### 根本原因分析

配置问题、缓存问题、文件问题

---


## 账户绑定信息更换

**问题分类**: 账户与财务｜账户问题

### 详细问题描述

您好，    本账号为公司企业认证账号，该账号之前认证的手机号码和邮箱号码，是之前负责人个人手机号码和邮箱。    由于该负责人离职，先要求更换绑定手机号码和邮箱号，绑定新账号号码如下：    手机号：[REDACTED_PHONE]    邮箱： [REDACTED_EMAIL] 请帮忙处理下，谢谢！

### 客服解答内容

1. 您好，支持人工申诉修改邮箱，后续可以使用新邮箱验证自助变更手机号可以通过人工申诉提供相关资料进行修改，将材料发送邮件到 [REDACTED_EMAIL] 需要提供的信息如下：a、个人实名认证：请提供注册邮箱、修改原因、手持与实名认证一致的身份证正面图片、新注册邮箱；b、企业实名认证：账号认证的资质信息，公司企业营业执照副本、与修改账号邮箱的说明并加盖公司公章，[REDACTED_EMAIL]，提供发件邮箱。这边同步给专员为您审核处理

### 根本原因分析

账号问题

---


## 我们还没怎么用，就已经开始计费，请帮忙查下这些是什么费用？怎么产生的？

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

我们还没怎么用，就已经开始计费，请帮忙查下这些是什么费用？怎么产生的？另外，avinfo是要额外收费的吗？

### 客服解答内容

1. 您好，对应区域（南美洲，亚洲，如计费项信息描述）的 cdn流量费用。是客户端请求您绑定的cdn域名资源，产生的流量费用。可以在cdn产品处 统计分析，日志分析查看详细数据：https://portal.qiniu.com/cdn/overviewavinfo是收费的，0.1元/千次

### 根本原因分析

证书问题、域名问题

---


## 模板审核

**问题分类**: 云短信｜签名模板审核

### 详细问题描述

模板审核

### 客服解答内容

（客服已协助处理）

### 根本原因分析

其他问题

---


## 资源无法加载

**问题分类**: CDN｜其他类咨询

### 详细问题描述

国外泰国用户，无法加载课程图片信息；该泰国用户的出口ip是27.55.93.144，国内网络是可以正常加载课程信息，根据用户提交问题截图来看，是部分图片资源无法正常加载导致的界面异常；麻烦看下，是否国外的cdn节点有问题；出现时间，2024-10-30 19:35左右；

### 客服解答内容

1. 您好，访问链接提供下，这边过滤下日志

2. 您好，这个域名30号19点没有非200的日志，是不是网络原因没有加载出来？

### 根本原因分析

网络问题、域名问题

---


## 有4个域名找回，正在处理中，麻烦帮我加速处理一下

**问题分类**: CDN｜配置问题

### 详细问题描述

我有四个域名，已经在后台提交了找回，显示处理中，麻烦帮我尽快处理一下image.0523114.comimage.0523555.compic.dn58.cntu.dn58.cn

### 客服解答内容

1. 您好，域名在其他账号下创建，会导致当前账号下创建失败，域名找回操作有两种：1.系统自动找回，参考图文操作文档：https://developer.qiniu.com/fusion/manual/5857/the-domain-name-back2.人工找回，需要您设置一个 TXT 解析验证，然后提交给我们确认后，我们手动帮您过户到当前账号，验证配置如下主机记录 qn-verification

2. 您好，稍等下，这边核实下

3. 您好，已经处理完成了，您查看下

### 根本原因分析

配置问题、证书问题、账号问题

---


## 域名配置一直不生效

**问题分类**: CDN｜配置问题

### 详细问题描述

xtconfig.xintiangui.comxtconfig-xintiangui-com-idvoysm.qiniudns.com

### 客服解答内容

1. 您好这边帮您手动介入处理下 请稍等

2. 您好把存储空间配置的referer关闭一下 再访问[图片]

### 根本原因分析

配置问题、证书问题、文件问题

---


## 创建cdn域名一直处理中

**问题分类**: CDN｜配置问题

### 详细问题描述

两小时了 卡在哪里了 帮忙看下

### 客服解答内容

1. 您好，这边手动介入下处理，麻烦稍等。

### 根本原因分析

其他问题

---


## 工单号: 399627 这个工单里面之前设置了个windows服务器备份上传到七牛云的工具

**问题分类**: 对象存储｜上传下载

### 详细问题描述

您好 老师我现在用命令行工具 Qshell上传windows备份盘里面的备份，但是现在有个问题，七牛云里面全部保存下来了，我想保留最新的三份，麻烦问一下我应该怎样设置呢，Qshell里面怎么写命令，写哪里呢，麻烦回复一下哈。谢谢啦

### 客服解答内容

1. 您好保留最新的三份——是要根据时间列举出最新上传的文件吗

2. 备份盘是指您服务器上的资源吗，如果是的话 直接将最新时间的内容 上传到存储空间就行

3. 您好您可以使用qshell工具的listbucket2命令，列举空间所有文件名到一个本地的txt文件中，在本地对文件时间做一下列举qshell下载安装:https://developer.qiniu.com/kodo/tools/1302/qshelllistbucket2命令：https://github.com/qiniu/qshell/blob/master/docs/listbucket2.md[图片]

4. 这一步不需要与前面的操作有链接 直接列举您的空间里指定时间段内的文件就行

5. 参考示例 把时间点换成您需要的时间就可以

### 根本原因分析

配置问题、证书问题、权限问题

---


## 短信無法正常發送

**问题分类**: 云短信｜短信发送问题

### 详细问题描述

短信域名 http://sms.qiniuapi.com/ 發送後顯示  502 Bad Gateway

### 客服解答内容

1. 您好这边核查下 请稍等

2. 有没有复现502时的reqid  大概几点出现的这个报错

3. 好的 这边内部反馈下 请稍等

4. 您这边重试下 把最新的发送日志给我们 这边内部反馈下

5. ping sms.qiniuapi.com执行看下

### 根本原因分析

证书问题、网络问题、域名问题

---


## qiniu.cdn.wxapp.guoran100.com 更换证书时间超时

**问题分类**: CDN｜证书问题

### 详细问题描述

qiniu.cdn.wxapp.guoran100.com 更换证书时间超时

### 客服解答内容

（客服已协助处理）

### 根本原因分析

配置问题、证书问题、网络问题

---


## ssl证书长时间未配置完成

**问题分类**: CDN｜证书问题

### 详细问题描述

ssl证书长时间未配置完成，已经超过2个小时，还是没有完成配置，已经影响到系统的使用域名：liftadstorage.shaxuntech.com

### 客服解答内容

（客服已协助处理）

### 根本原因分析

配置问题、证书问题、域名问题

---


## 从昨晚到现在一直不成功

**问题分类**: CDN｜配置问题

### 详细问题描述

从昨晚到现在一直不成功

### 客服解答内容

（客服已协助处理）

### 根本原因分析

配置问题

---


## 有用户反馈刷不出视频，对方运营商在常州，我们在北京可以正常看，什么原因

**问题分类**: CDN｜刷新缓存问题

### 详细问题描述

有用户反馈刷不出视频，对方运营商在常州，我们在北京可以正常看，什么原因

### 客服解答内容

1. 您好，1、麻烦提供下用户的 ip、dns 信息，和cdn节点信息，这边代理测试下可以通过访问这个链接 http://ping.huatuo.qq.com/ 获取本地的 ip 和 dns 信息，在检测域名这边输入下cdn域名，点击提交检测，然后截图通过工单提交给我们[图片]2、建议让用户使用 chrome 浏览器，按照下述文档获取下 remote adress(对端节点ip)，request header(客户端请求头) 以及 response header(服务端响应头)信息，方便我们查询分析问题。https://developer.qiniu.com/fusion/kb/1478/how-to-access-network-in-the-browser-request-information

2. 您好，麻烦提供下上面的ip节点信息

3. 您好，只需要访问下链接，然后在搜索框输入下cdn域名检测下

### 根本原因分析

证书问题、域名问题

---


## 上传到rl-web空间的index.html 页面，已经【刷新CDN缓存】，访问页面内容更新不一样？

**问题分类**: 对象存储｜上传下载

### 详细问题描述

上传覆盖文件到rl-web空间的index.html页面已经【刷新CDN缓存】，同时访问 https://www.reliancejk.com/ （旧内容）和 https://reliancejk.com/index.html （最新内容） ，怎么统一？已经等了一个星期，还是不同。

### 客服解答内容

1. 您好，您是需要访问https://www.reliancejk.com/出现新内容？那您需要提交下这个链接对应的刷新

2. 刷新下https://www.reliancejk.com/和https://www.reliancejk.com/

3. 您好，需要需要访问https://www.reliancejk.com/和https://www.reliancejk.com/ 需要刷新的链接也是https://www.reliancejk.com/和https://www.reliancejk.com/

4. 您好，提交刷新链接https://www.reliancejk.com/才能刷新https://www.reliancejk.com/这个链接的缓存

5. 没事的，有什么问题您再反馈

### 根本原因分析

缓存问题、证书问题、文件问题

---


## 如何给普通用户授权提工单的权限

**问题分类**: 账户与财务｜账户问题

### 详细问题描述

新建用户看不到工单的选项，无法提交工单。

### 客服解答内容

1. 您好新建用户是指创建的子账号吗 这个目前还不支持工单权限

2. 给下您的联系方式 这边同步商务对接您

3. 把指定前缀的资源list出来，用个循环全部删除，可参考：https://developer.qiniu.com/kodo/api/1284/list[图片]https://developer.qiniu.com/kodo/api/1257/delete注意：用户主动删除资源不可以恢复，请慎重

4. 控制台的目录实际是虚拟目录，是基于文件名的路径自动扩展出来的虚拟文件夹，实际不存在

### 根本原因分析

配置问题、证书问题、权限问题

---


## 怎么样查询对应格式的文件

**问题分类**: 对象存储｜工具使用

### 详细问题描述

怎么样查询对应格式的文件

### 客服解答内容

1. 您好qshell安装包及文档请参考https://developer.qiniu.com/kodo/tools/1302/qshellwindows环境下安装教程参考 https://developer.qiniu.com/kodo/kb/5545/windows-environment-installation-qshell-tutorial

2. 可以使用qshell来列举对应后缀的文件https://github.com/qiniu/qshell/blob/master/docs/listbucket2.md

3. 您好，很抱歉，这边无法为您操作查看的，qshell会列举全部文件之后，单独列举对应后缀的文件需要一定时间，您耐心等待下

4. 您好非常抱歉，数据操作需要您那边自己处理

5. 您好，1、qshell工具的listbucekt2命令可以实现列举文件，列举完成后调用qshell的batchdelete命令批量删除，可参考下 https://developer.qiniu.com/kodo/tools/1302/qshella、列举对应时间的文件列表qshell listbucket2 <Bucket> -o list.txt

### 根本原因分析

配置问题、缓存问题、证书问题

---


## cdn域名停用相关问题

**问题分类**: CDN｜其他类咨询

### 详细问题描述

cdn域名www.yqudown.com停用之后，网站很长时间都无法展现，请问怎么处理快速恢复网站访问

### 客服解答内容

1. 您好域名停用后是无法访问的 需要使用的话在控制台点击启用即可

### 根本原因分析

网络问题、域名问题

---


## 新存储空间的文件访问速度超级慢

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

昨天新创建的一个存储空间，上传后的图片文件超级慢。但是以前创建的就很快对比例子：旧空间的文件：https://hunyaji-dns01.oexy.cn/23qin0upload644258e347087.jpg新空间的文件：https://brokerqn.oephp.com/240f6c220cfe7dc440e2f8c940e9263da55_J1fw.jpg

### 客服解答内容

1. 您好brokerqn.oephp.com的加速覆盖范围是海外 国内访问慢是符合预期的 您可以调整线路为国内﻿自 2020年10月20日起，控制台 -【域名管理】目前已支持域名覆盖区域（中国大陆、全球、海外）切换，您可以在[图片]点击『修改』自助切换。

### 根本原因分析

证书问题、文件问题、域名问题

---


## 录制直播回放 视频长度不够

**问题分类**: 直播云｜点播问题

### 详细问题描述

有部分 录制直播回放 视频长度应该是40秒 结果打开只有24秒回放地址https://play.rpzhileyun.com/recordings/z1.rpkj.sanming/yadjzx/damen/in/1730441981_1730442021.m3u8

### 客服解答内容

1. 您好，能重新生成试下吗，怀疑是ts片还没落存储的时候生成了回放，m3u8文件里少了后面几个ts片的索引。

2. 那可能就是没落存储时候生成的重新生成前，先到存储空间中recordings/z1.rpkj.sanming/yadjzx/damen/in/1730441981_1730442021.m3u8这个文件删除掉再重新生成对应时间回放

### 根本原因分析

证书问题、文件问题、转码问题

---


## 怎么禁用特殊格式的文件上传

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

怎么禁用特殊格式的文件上传

### 客服解答内容

1. 您好，一，这个如果前端语言判断，可在用户发送请求之前进行，用户体验比较好。各种前端语言都有相关的限定方法，不属于七牛业务，请自行查找相关资料。例如，js可参考：http://www.cnblogs.com/2050/p/3913184.html （ 可以检索 filters 字段）二，上传策略限定，只能用户上传之后，由服务端判断，再响应给他上传失败，具体可参考：http://developer.qiniu.com/docs/v6/api/reference/security/put-policy.htmlmimeLimit ● 限定用户上传的文件类型指定本字段值，七牛服务器会侦测文件内容以判断MimeType，再用判断值跟指定值进行匹配，匹配成功则允许上传，匹配失败返回403状态码● 示例1. “image/*“表示只允许上传图片类型；2. “image/jpeg;image/png”表示只允许上传jpg和png类型的图片；3. “!application/json;text/plain”表示禁止上传json文本和纯文本（注意最前面的感叹号）。

2. 您好，mimelimit是对方法二的说明哈，生成token时，上传策略中指定

3. 您好，七牛这边控制的话，就是通过上传策略的mimeLimit限制文件类型哈您需要的是什么样的呢

4. 您好，上传前是前端限制，上传时是上传策略限制，如果上传上来了，就得删除了。建议你们可以开一下事件通知，回调的方式，有上传行为回调通知给你们，通知会有上传ip信息，文件名信息，文件名过滤到exe结尾的你们删除和告警。https://developer.qiniu.com/kodo/8541/set-the-event-notification

5. 您好非常抱歉，存储空间不支持这样的限制。需要您参考 2024-11-01 14:59:24  的2种方法来处理下

### 根本原因分析

配置问题、证书问题、权限问题

---


## Android 无法推流

**问题分类**: 直播云｜推流问题

### 详细问题描述

Android 无法推流

### 客服解答内容

1. 辛苦帮忙用adb抓取个完整日志呢android 抓取log 的方法：unix-like 系统：adb shell logcat -v time thread | tee logplayer.logwin 系统：adb shell logcat -v time thread > log.log命令敲上之后，进行复现，复现完成之后，停止命令，然后把对应的 log.log 发过来。

2. 您有调用推流吗，看日志没有调用推流的方法呢

3. 是的，所以目前您那边是没哦哟ready的回调吗

4. 那您本地预览有吗，摄像头和麦克风权限都有吗

5. 摄像头画面有正常预览吗

### 根本原因分析

证书问题、权限问题、文件问题

---


## 域名修改证书处理中

**问题分类**: CDN｜配置问题

### 详细问题描述

在七牛云ssl服务商创建了了新的https证书，并修改到这个域名的https证书配置，一直处理中

### 客服解答内容

1. 您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

配置问题、证书问题、域名问题

---


## 上传同一个文件，怎么才能让KEY不重复？

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

上传同一个文件，怎么才能让KEY不重复？要在哪里设置？

### 客服解答内容

1. 您好，根据上传时间不同设置不同的前缀？

2. 您好，上传文件名称您可以在商场token，savekey指定

3. 您好，您自己指定下，为不同的key就好，设置下savekey

4. 您好，是的，在上传token中指定下savekey就好

5. 您好，指定时间后面的文件名称可以拼接下，key这个参数不行

### 根本原因分析

配置问题、缓存问题、证书问题

---


## 访问course.tmtpost.com405错误

**问题分类**: CDN｜配置问题

### 详细问题描述

访问course.tmtpost.com这个的时候是405错误。我们的key之类的有黑白名单之类的吗？

### 客服解答内容

1. 您好您这个访问是401 这个是私有空间的问题[图片]

2. 当您将空间设置成私有时，必须获得授权，才能对空间内的资源进行访问。私有资源下载是通过HTTP GET的方式访问特定的 URL。私有资源URL与公开资源URL相比只是增加了两个参数e和token，分别表示过期时间和下载凭证。一个完整的私有资源 URL 如下所示：http://<domain>/<key>?e=<deadline>&token=[REDACTED_KEY]

### 根本原因分析

配置问题、证书问题、网络问题

---


## 域名ssl，域名所有权验证，可以加速一些吗，你好

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

域名ssl，域名所有权验证，可以加速一些吗，你好

### 客服解答内容

1. 您好，您刷新下页面呢，这边看账号下证书订单都签发了

### 根本原因分析

缓存问题、证书问题、账号问题

---


## 一直显示正在处理，启动不了，也停用不了

**问题分类**: CDN｜配置问题

### 详细问题描述

一直显示正在处理，启动不了，也停用不了

### 客服解答内容

1. 您要停止哪个域名，这边操作测试下

### 根本原因分析

域名问题

---


## 控制台用不了

**问题分类**: 智能多媒体｜音视频处理

### 详细问题描述

你好，你们后台打不开，页面是：https://portal.qiniu.com/dora/media-gate/overview报错[500] 请求失败

### 客服解答内容

1. 您好，概览这边请求异常，影响使用数据查看，后端正在处理您目前是需要什么操作，不影响创建转码任务和机器处理

### 根本原因分析

证书问题、转码问题

---


## 活动购买的资源包在内容审核-增量审核能使用吗

**问题分类**: 账户与财务｜计费问题

### 详细问题描述

麻烦帮我看下，我买的这俩资源包，能抵扣【内容审核-增量审核】的用量吗因为我现在看资源包详情里抵扣量还是0，帮我确认下能不能抵扣，谢谢。

### 客服解答内容

1. 您好，这个可以抵扣增量审核的https://static.zsort.cn/mqrcode/4106/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_[REDACTED_PHONE]685.png

2. 您好，因为今天的使用量还没有统计出来的，需要到明天8点

3. 您好，因为今天的使用量还没有统计出来的，需要到明天8点

### 根本原因分析

证书问题、权限问题、资源包问题

---


## 免费 from 自动催单

**问题分类**: CDN｜证书问题

### 详细问题描述

长时间处于域名检测环节

### 客服解答内容

1. 您好，这边手动介入下处理，麻烦稍等。

2. 您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

域名问题

---


## 配置域名卡住

**问题分类**: CDN｜配置问题

### 详细问题描述

*.yes515.com配置域名卡住

### 客服解答内容

（客服已协助处理）

### 根本原因分析

配置问题、域名问题

---


## 我们换了账号，旧的账号数据要怎么转移到新的

**问题分类**: 对象存储｜数据迁移

### 详细问题描述

我们换了账号，旧的账号数据要怎么转移到新的，旧的账号也找不到了，只有空间的授权key了config.setQiniuDomain("https://pic.oointer.com");config.setQiniuAccessKey("[REDACTED_LONG_KEY]");config.setQiniuSecretKey("[REDACTED_LONG_KEY]");config.setQiniuPrefix("upload");config.setQiniuBucketName("vvdaren");

### 客服解答内容

1. 您这边可以参考下这个方法迁移的https://developer.qiniu.com/kodo/12666/set-data-migration

2. 看下您的源存储空间是哪个区域的，以及对应的endpoint的https://developer.qiniu.com/kodo/4088/s3-access-domainname[图片]

3. 不可以的，必须是原来的存储空间地区的

4. 这边看源存储空间是华南的，您使用华南的看下

### 根本原因分析

证书问题、账号问题、文件问题

---


## 直播时，会不定时的自动重新推流

**问题分类**: 直播云｜推流问题

### 详细问题描述

用手机端推流，并没有退出直播间，但是在七牛后台会看到多个直播记录，最长的是5分钟，最短的34秒

### 客服解答内容

1. 您好，您稍等这边确认一下

2. 您好，这边看应该是推流端网络不稳定的导致的异常断开的，您这边换一个稳定的网络再测试看下呢？网络失败的原因导致的

### 根本原因分析

网络问题、直播问题

---


## 小米应用商店隐私合规上架被拒

**问题分类**: 直播云｜直播SDK问题

### 详细问题描述

2024-11-01 10:41:03.559 -> [测试动作] 启动史宾格隐私合规检测2024-11-01 10:47:47.355 -> (SDK: 七牛云存储) 读取设备IP2024-11-01 10:47:47.373 -> (SDK: 七牛云存储) 读取设备IP2024-11-01 10:47:47.403 -> (SDK: 七牛云存储) 读取设备IP2024-11-01 10:47:47.445 -> (SDK: 七牛云存储) 读取设备IP2024-11-01 10:47:47.490 -> (SDK: 七牛云存储) 读取设备IP2024-11-01 10:47:47.531 -> (SDK: 七牛云存储) 读取设备IP2024-11-01 10:47:47.587 -> (SDK: 七牛云存储) 读取设备IP2024-11-01 10:47:47.620 -> (SDK: 七牛云存储) 读取设备IP小米客服说：此问题场景可通过描述解决的，仅地图导航应用的实时定位功能隐私指引专员-03其他场景均不允许发生后台行为隐私指引专员-03仅可做关闭处理

### 客服解答内容

1. 您好，您这边看下关闭dns预解析就可以了GlobalConfiguration.getInstance().isDnsOpen = false 关闭 DNS 预解析

### 根本原因分析

权限问题、文件问题、域名问题

---


## 文件上传

**问题分类**: 对象存储｜上传下载

### 详细问题描述

海外用户上传需要什么配置吗

### 客服解答内容

1. 您好，没有什么特别需求的，可以直接上传的

### 根本原因分析

配置问题、文件问题

---


## 主播端正常推流，直播的活跃流会消失

**问题分类**: 直播云｜推流问题

### 详细问题描述

主播端一直正常直播，没有退出直播间。但是活跃流会突然的消失

### 客服解答内容

1. 您好复现的时间是什么时候 有没有报错 这边核查

2. 您好，当前 LIVE20241101[REDACTED_PHONE]8  从后台看是在线的。 如果是官网控制台访问，您再刷新下看看。

3. 给下复现录屏 这边看下

4. 您好，当前有两条流在线。[图片]

### 根本原因分析

缓存问题、直播问题

---


## 配置添加域名一直处理中

**问题分类**: CDN｜配置问题

### 详细问题描述

添加后，一直卡在处理中

### 客服解答内容

（客服已协助处理）

### 根本原因分析

配置问题、证书问题、域名问题

---


## 冻结了解冻后恢复了部分链接，还有一部分提示下线或者冻结

**问题分类**: CDN｜访问下载

### 详细问题描述

{    "error": "该域名目前已被 CDN 服务暂时下线或冻结。如果您是该网站的拥有者，请查看七牛云 CDN 近期邮件提示，并按要求恢复服务。如果您是该网站的一般访问者，请忽略该问题或稍后重试。"}

### 客服解答内容

1. 您好，可以了，您再试下呢

### 根本原因分析

域名问题

---


## 对象存储免费下载额度的疑问

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

在《关于七牛云的计费和账单说明》（https://developer.qiniu.com/af/1361/about-seven-niuyun-stored-billing-and-billing-instructions）中提到“对于认证的客户，七牛云存储提供免费的存储空间 10GB，每月下载流量 10GB”，这个10GB流量指的是外网流出流量还是CDN回源流量？还是说两者相加总共免费10GB？谢谢！

### 客服解答内容

1. 您好，cdn http流量，cdn回源流量都有10G免费额度。没有外网流出流量的免费额度具体可参看免费额度须知：https://developer.qiniu.com/af/kb/1574/free-credit-information

### 根本原因分析

证书问题、文件问题

---


## 之前的域名没备案删除了，现在备案通过了，但是图片没办法访问

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

之前的域名没备案删除了，现在备案通过了，但是图片没办法访问

### 客服解答内容

1. 您好，检查服务正常的。麻烦提供一个图片地址，这边具体分析下，

### 根本原因分析

文件问题、域名问题

---


## 更换绑定手机号

**问题分类**: 账户与财务｜账户问题

### 详细问题描述

原技术经理离职了，我是新的技术经理。无法通过验证码更换手机号，请协助更换为我的手机号和邮箱[REDACTED_PHONE]

### 客服解答内容

1. 您好，方法1：请登陆官网——点击官网右上角的管理控制台——个人面板——个人中心的安全设置更改邮箱，输入密码，填写邮箱进行修改。单击进入修改地址：https://portal.qiniu.com/user/security方法二：如果您因为邮箱已经无法登陆，可以通过人工申诉提供相关资料进行修改，将材料发送邮件到 [REDACTED_EMAIL] ，抄送[REDACTED_EMAIL]需要提供的信息如下：a、个人实名认证：请提供注册邮箱、修改原因、手持与实名认证一致的身份证正面图片、新注册邮箱；b、企业实名认证：账号认证的资质信息，公司企业营业执照副本、与修改账号邮箱的说明并加盖公司公章，[REDACTED_EMAIL]，抄送[REDACTED_EMAIL]邮件发送后请工单上告知我们，提供发件邮箱和联系电话。这边同步给商务为您审核处理

2. 邮件说明下新手机号码，旧手机号码新邮箱，旧邮箱

### 根本原因分析

配置问题、证书问题、账号问题

---


## 上传文件

**问题分类**: CDN｜配置问题

### 详细问题描述

上传视频文件之后，导出链接，为什么同一个文件下的链接长度不一样，有的文件夹里的链接长度一样。不一样长的链接在APP中播放的时候会出现卡顿现象，一样长的就不会卡

### 客服解答内容

1. 您好，中文名称的文件需要进行url编码，如果您需要都一样长，建议文件名称选择字母+数字，不要使用中文

2. 你好，播放卡顿的文件链接提供下

3. 您好，全部都卡顿吗？随便提供一个可以吗？这边看下视频编码等信息

4. 您好，看编码和视频测试播放都是很快的，您尝试预取下文件之后再访问看下会不会好些？预取方法请参考：1. api 接口地址：https://developer.qiniu.com/fusion/api/1227/file-prefetching2. portal.qiniu.com 控制台进行资源预取，点击左侧融合cdn => 刷新预取3. url 资源预取，全网生效 10min 左右

5. 您好，证书过期就没有用了

### 根本原因分析

缓存问题、证书问题、文件问题

---


## 视频拆条是以什么维度拆的

**问题分类**: 智能多媒体｜音视频处理

### 详细问题描述

需要对接视频拆剪功能，我们这边视频拆剪的功能是以什么维度来拆的，语义 还是场景 或者是其他什么场景

### 客服解答内容

1. 您好您要使用的是https://developer.qiniu.com/dora/7509/video-capture01 这个接口吗

2. https://developer.qiniu.com/dora/4154/dora-segment ——这个是根据视频时长来分段处理的

3. 是的 这个时间您可以自由调整[图片]

### 根本原因分析

配置问题、证书问题、SDK问题

---


## 更新证书后，修改 HTTPS 配置处理时间长

**问题分类**: CDN｜证书问题

### 详细问题描述

更新证书，修改 HTTPS 配置处理时间长，麻烦处理下

### 客服解答内容

1. 您好，这边手动介入下处理，麻烦稍等。

2. 您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

配置问题、证书问题

---


## 创建域名卡住

**问题分类**: CDN｜配置问题

### 详细问题描述

m.yc.yes515.com创建卡住

### 客服解答内容

1. 您好，这边手动介入下处理，麻烦稍等。

2. 您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

其他问题

---


## 充值

**问题分类**: 账户与财务｜发票问题

### 详细问题描述

下午两点打款 预计什么时候到账

### 客服解答内容

（客服已协助处理）

### 根本原因分析

其他问题

---


## 修改域名源站处理中，免费证书申请耗时相对较长，平均 15 分钟完成，期间域名访问不受影响，部分配置不可修改，若长时间未配置完成，请提交工单反馈

**问题分类**: CDN｜配置问题

### 详细问题描述

[    [        {            "title": "请求 ID",            "content": "6g_zAYDxHbU6yQMY, 6g_zAYDxHbU6yQMY, 6g_zAYDxHbU6yQMY, 6g_zAYDxHbU6yQMY"        },        {            "title": "日志栈",            "content": "fusiondomain_cud:1/400;APIS:215/400;PORTAL-PROXY:234/400"        }    ]]

### 客服解答内容

1. 】您好，这边手动介入下处理，麻烦稍等。

2. 您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

SDK问题

---


## 修改了https证书一直未生效

**问题分类**: CDN｜配置问题

### 详细问题描述

msdn.miaoshouai.com

### 客服解答内容

1. 您好这边处理下 请稍等

### 根本原因分析

其他问题

---


## api中源站域名为什么找不到

**问题分类**: CDN｜证书问题

### 详细问题描述

api获取域名列表（GET /domain）以及修改证书（PUT /domain//httpsconf）无法找到我配置的自定义源站域名，这样的话使用letsencrypt证书的就无法在证书到期前自动更新，只能手动操作吗？请告诉我是否有别的api可使用

### 客服解答内容

1. 您好源站域名没有部署证书的API 需要手动处理

### 根本原因分析

配置问题、证书问题、域名问题

---


## 全站加速

**问题分类**: CDN｜其他类咨询

### 详细问题描述

域名一直显示配置中，麻烦尽快解决下网站打不开

### 客服解答内容

1. 源站强制https，全站加速强制https，http回源就成环了，已帮您调整了，您再访问试下

### 根本原因分析

配置问题、证书问题、域名问题

---


## 图片删除后能正常访问

**问题分类**: 对象存储｜SDK使用

### 详细问题描述

https://hd.qiniu.box365.cn/commonFolder/[REDACTED_PHONE]390g4vKyJJh/组 [REDACTED_EMAIL]https://hd.qiniu.box365.cn/commonFolder/[REDACTED_PHONE]21y6wpZMIoQ.png用代码删除上述图片后，七牛云存储空间的图片确实被删除了，但是这个链接还是能访问到图片是什么问题

### 客服解答内容

1. 您好，访问到的是这张图片在CDN节点的缓存。图片从源站删除之后，它的缓存仍然会在CDN节点保存，所以用户仍然可以访问到。刷新下cdn缓存就可以哈方法请参考：https://developer.qiniu.com/fusion/kb/1325/refresh-the-cache-and-the-effect-of-time方法1: portal.qiniu.com 控制台刷新缓存，点击左侧 cdn => 刷新预取方法2: api 接口地址：https://developer.qiniu.com/fusion/api/1229/cache-refreshTip : url 刷新，全网生效 10min 左右，目录刷新需要 30min 左右

### 根本原因分析

缓存问题、证书问题、文件问题

---


## 创建 cdn 域名，一直处于创建中

**问题分类**: CDN｜其他类咨询

### 详细问题描述

帮忙看下xyqbcdn.91xr.cn 这个 cdn 域名管理一直处于创建中

### 客服解答内容

1. 您好，久等了，已创建完成

### 根本原因分析

域名问题

---


## imageInfo并发数的问题

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

批量获取图片信息的时候经常出现获取失败，这边是不是对这块有限制

### 客服解答内容

1. 您好，您获取的并发是多少，获取的是哪个空间？具体报错信息是什么

2. 这个报错，看起来是解析的原因，主机网络异常，DNS解析失败

### 根本原因分析

网络问题、域名问题

---


## 密码忘记

**问题分类**: CDN｜其他类咨询

### 详细问题描述

域名设定了cdn，打算停用时要输入密码？忘记密码了如何找回密码或者重置密码呢？我记得当时设置时好像没有要求设定密码之类的操作。

### 客服解答内容

1. 您好，退出登录后，可在登录页面下方「忘记密码」处，通过账号绑定的手机号或邮箱重置密码[图片]

### 根本原因分析

配置问题、账号问题、域名问题

---


## RTC 合有问题

**问题分类**: 实时互动｜RTC合流问题

### 详细问题描述

附件  LiveRoomActivity、RoomActivity 代码，之前主播在线，观众是可以听到声音的，现在提示： 播放器打开失败，请确认是否在推流！七牛技术回复：QPlayer2是新版播放器sdk之后主要维护这个播放器sdk，和老版相比api不一样，实现的功能更多具体的可以参考文档﻿https://developer.qiniu.com/pili/12221/qplayer2-integration-to-prepare我回答:上面两个类的代码 我是完全从贵公司的 QNRTC-Android-6.4.0 demo 拿过来，一模一样，几乎没有什么改动。 而且之前是可以的。七牛技术回复：这个问题您的使用场景是rtc合流转推到直播云的吗，辛苦发一下appid，房间名称，以及时间点呢，这边查一下转推的情况答：是的,使用场景是rtc合流转推到直播云， appid : fmd7iusef ,  房间名称:FXWD ,时间：10月31号晚上11点 到 11月1号 凌晨2点40 这个范围

### 客服解答内容

1. 您好，当前的问题，是调用合流转推到直播云后，完全有问题，还是只 10月31号晚上11点 到 11月1号 凌晨2点40 这个范围 内出现了 偶现的问题？

2. 您好，你调用的合流参数  提供一下。

3. 您好，您限制 实际 创建房间，并合流转推，我来看下。

4. 这边看下 辛苦耐心等待

5. 您好，为您处理的工程师预计明天晚间会上线确认一下的，这边会为您统一安排确认一下的，还请耐心等待一下

### 根本原因分析

配置问题、证书问题、账号问题

---


## 怎么欠费一下这么多？？？

**问题分类**: 账户与财务｜计费问题

### 详细问题描述

新买的流量。

### 客服解答内容

1. 您好，这边看您的流量产生较高导致的您可以在 控制台 - cdn - 统计分析 - 日志分析 中看到您的top访问情况，比如高频访问的URL和客户端IP。https://portal.qiniu.com/cdn/statistics/log/top如有部分IP请求数/请求流量异常，不符合您的业务预期，您可以在域名管理 - 访问控制 中，开启IP黑白名单，对这部分IP进行封禁。[图片]

2. 您看下实时消费明细是不是CDN流量导致的，这边看是CDN流量产生的计费，是上个月的流量账单出账了的，您可以看下您上个月到目前产生了10多个TB的流量的，我们这边是月初出账的，今天出账期的

3. 流量包是正常抵扣了的，看着像超出流量包的流量产生了计费的，您这边留一下您的联系方式，这边让商务经理与您确认一下，这边工单看不到您的资源包和计费相关的

4. https://portal.qiniu.com/financial/estimated-consume

5. 您好，您稍等这边帮您反馈一下

### 根本原因分析

证书问题、域名问题、资源包问题

---


## 获取svga文件时，部分文件跨域 部分文件不跨域

**问题分类**: 对象存储｜其他类咨询

### 详细问题描述

获取svga文件时，部分文件跨域 部分文件不跨域

### 客服解答内容

1. 您好，您这边给CDN域名配置一下跨域响应头后再确认一下看下，值为*号即可的https://developer.qiniu.com/fusion/6778/the-http-response-header-configuration[图片]

### 根本原因分析

配置问题、证书问题、文件问题

---


## 上传多个文件怎么生成压缩文件

**问题分类**: 对象存储｜上传下载

### 详细问题描述

上传多个文件怎么生成压缩文件或者对已经上传过的文件url转成一个压缩包

### 客服解答内容

1. 您好，如果需要压缩文件的话，需要使用接口的，您可以参考下我们的多文件压缩接口的https://developer.qiniu.com/dora/1667/mkzip

2. 接口返回json数据，返回任务ID

3. 压缩是保存到存储空间的，您这边就和下载存储空间的文件一样找到压缩文件下载到本地即可的

4. 给您个java的demo看下public class mkzip {

### 根本原因分析

配置问题、证书问题、账号问题

---

