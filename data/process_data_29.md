# 客户服务问答知识库 - Part 29

> 本文档整理了客户服务中的常见问题及解决方案

## 已上传图片资源无法访问

**分类**：对象存储｜其他类咨询

### 问题描述

比如  我账号下yht-applet 空间的 image/20220802/7eef5ce6746d7843a1bbd700f24949a4.jpg

### 客服解答

1. 您好测试这个文件不存在 您再确认下[图片]

2. 您好，您目前绑定的域名已经有A记录解析到您的网站IP了，再做七牛的CNAME会有解析冲突。https://developer.qiniu.com/fusion/manual/1367/custom-domain-name-binding-process一个具体的域名只能解析到一个地方，不能同时配置 A 记录和 CNAME 解析。1. 重新添加，一个未使用过未解析过的二级域名，直接做CNAME解析，例如您原本在七牛绑定的是 xxx.com ，这个时候您重新绑定一个 cdn.xxx.com 到七牛，然后配置这个域名对应的解析即可。2. 删除您直接的A记录就可做CNAME解析(注意：A记录删除会导致您域名中的内容无法访问，需要谨慎操作)[图片]

### 根本原因分析

域名同时配置了A记录和CNAME解析导致冲突

---

## 周五创建的证书

**分类**：CDN｜证书问题

### 问题描述

等待 CA 机构审核后颁发证书  一直显示这个，这个是谁审核的

### 客服解答

1. 您好，您这边需要确认一下，域名下是否有CAA记录呢

2. 您好，如果您的域名解析下有CAA记录的话会导致解析失败也就是一直审核不到的的，需要将CAA记录删除或暂停一下的

### 根本原因分析

域名解析配置了CAA记录导致SSL证书审核失败

---

## 域名处理时间长

**分类**：CDN｜配置问题

### 问题描述

域名处理时间长

### 客服解答

您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

系统处理时间较长

---

## 侵犯了用户隐私 要求删除

**分类**：人工智能｜内容安全

### 问题描述

通过API审核的照片被存放在了 内容审核列表。侵犯了用户隐私 要求提供删除功能。

### 客服解答

1. 您好，只会保留七天，七天后自动删除的。

2. 您好，目前还没有的，您这边如果需要这个功能，这边反馈内部提下需求

### 根本原因分析

产品功能限制，不支持手动删除

---

## 域名绑走的 SSL 证书即将过期，怎么操作申请免费证书

**分类**：CDN｜证书问题

### 问题描述

经查询，您的账号 [REDACTED_EMAIL] 在七牛云 CDN 加速平台有以下域名绑走的 SSL 证书即将过期，证书过期会导致您的 Https 域名无法正常访问。为保证您的服务正常使用，请您尽快更换证书。如证书已弃用请忽略。

### 客服解答

1. 您好，手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide4.升级HTTPS配置https://developer.qiniu.com/fusion/manual/4952/https-configuration注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

2. 『待确认』是需要您点击详情，然后根据提示进行文件或者 DNS TXT 验证，系统会自动轮询，轮询通过才会颁发证书参考文档：https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide

3. 在您的域名服务商后台配置

4. 您的域名在哪里买的 就到对应厂商后台配置 这个不是在七牛后台配置

5. 好的

6. cdn.7979jlzg.com这个证书已经签发了

7. cdn—域名列表—https配置—更换证书

8. 好的

### 根本原因分析

SSL证书即将过期需要更换

---

## 域名的CNAME在哪配置

**分类**：CDN｜证书问题

### 问题描述

域名是在牛小七上申请的，但是没找到CNAME配置

### 客服解答

1. 在您域名厂商云解析处配置，具体配置操作可以咨询下域名商配置如下一条记录：主机记录： zfhcdn记录类型：CNAME记录值：zfhcdn-odb-sh-cn-idvmnq6.qiniudns.com

2. 稍等

3. 重新提交订单申请下，免费证书订单超过两天就过期了，当前的已过期。手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide4.升级HTTPS配置https://developer.qiniu.com/fusion/manual/4952/https-configuration注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

4. 上周五的订单可以关闭掉，ca侧已经标记过期了。重新提交订单申请

5. 到域名厂商云解析处添加如下记录，进行证书验证主机记录：_5897D023030F88E315BA5AF6337B3C87.zfhcdn记录类型：CNAME记录值：[REDACTED_KEY].871D03CE2776E97D1628F36EBE7871AD.cmcdt3u18usnqz.trust-provider.com

6. 没有验证过，您配置验证记录的页面截图提供我们确认下

7. 域名厂商云解析处配置的记录页面截图我们确认下，公网上没有生效的验证解析。

8. 解析目前还是空的，公网解析不出验证记录，证书订单无法审核通过，咨询下域名商解析未生效呢[图片]

9. 证书配置是需要配置解析的哈，您如果配置了还是无法生效，需要找域名厂商确认下解析为何不生效

### 根本原因分析

SSL证书即将过期需要更换

---

## SSL證書問題

**分类**：对象存储｜其他类咨询

### 问题描述

請問一下確認時間大概需要多久，謝謝，幫我加急一下。

### 客服解答

您好，『待确认』是需要您点击详情，然后根据提示进行文件或者 DNS TXT 验证，系统会自动轮询，轮询通过才会颁发证书参考文档：https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 證書過期，重新申請待確認狀態

**分类**：CDN｜证书问题

### 问题描述

證書過期，重新申請了，目前待確認狀態

### 客服解答

1. 您好，『待确认』是需要您点击详情，然后根据提示进行文件或者 DNS TXT 验证，系统会自动轮询，轮询通过才会颁发证书参考文档：https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

2. 这个是域名的配置 不是证书的配置 参考 https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide 这个到您的域名服务商后台配置

### 根本原因分析

配置相关问题

---

## 对象存储在华南-广东，国外可以正常使用吗

**分类**：对象存储｜其他类咨询

### 问题描述

对象存储在华南-广东，国外可以正常使用吗

### 客服解答

您好，您可以配置一下CDN域名的，域名配置的覆盖范围选择全球即可的

### 根本原因分析

配置相关问题

---

## private-cdn.successchannel.net证书迟迟不生效

**分类**：CDN｜证书问题

### 问题描述

private-cdn.successchannel.net证书迟迟不生效

### 客服解答

1. 您好这边帮您手动介入处理下 请稍等

2. 已经处理完成

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 验证不通过

**分类**：CDN｜证书问题

### 问题描述

申请七牛云免费证书，解析cname类型后不通过

### 客服解答

1. 您好，参考这个配置主机记录 _53CE2920A134DCD0C1944D95BAE50E5A.upload记录值 [REDACTED_KEY].D9009A26C6C9C73B87E4117E4416869B.cmcdt3wwfqootp.trust-provider.com

2. 配置截图给一下

3. 后台看证书已经签发了

4. 您的bucket是 weimans 您打错了

5. cdn域名管理[图片]

### 根本原因分析

SSL证书即将过期需要更换

---

## 关于自定义变量问题

**分类**：对象存储｜SDK使用

### 问题描述

使用的是让客户端直穿七牛，spring这边只做一个token授权，但是需要七牛callback用户的uidStringMap putPolicy = new StringMap();putPolicy.put("forceSaveKey", true);putPolicy.put("saveKey", saveKey);putPolicy.put("callbackUrl", qiNiuYunConfig.getCallbackUrl());putPolicy.put("callbackBodyType", "application/json");putPolicy.put("callbackBody", "{\"key\":\"$(key)\",\"userId:\":\"" + user.getUid() + "\"}");    麻烦帮忙看一下为什么userid还是null，是需要$x这样去定义自定义变量吗？但是我看那个自定义变量时客户端传入的，感谢解答。

### 客服解答

1. 您好，您可以参考下这个的，需要定义的https://developer.qiniu.com/kodo/1235/vars#xvar

2. 您好，这个的话我们就不太清楚了的，我们这边的话目前就只有魔法变量和自定义变量的，您说的这种的话目前我们也没有具体的方案的

3. 您好，您这个说的就是上面自定义变量的呀，只是这个是returnBody，不是callbackbody的，callbackbody是返回回调服务器的returnBody是上传成功后，自定义七牛云最终返回給上传端（在指定 returnUrl 时是携带在跳转路径参数中）的数据。支持魔法变量和自定义变量。returnBody 要求是合法的 JSON 文本。例如 {“key”: $(key), “hash”: $(etag), “w”: $(imageInfo.width), “h”: $(imageInfo.height)}。

4. 您好，userid这个属于您的自定义响应内容的，这个自定义响应内容的的话，目前我们这边只有两种的，一个是returnbody客户端返回内容，一个是callbackbody回调业务服务器返回内容您的需求是您这边生成对应包含userid的上传token用户这边上传后返回用户的userid的信息，返回到您的上传token到业务服务器，这个不就是callbackbody回调响应内容吗？您可以参考下上传策略的文档，所以策略都在这里的https://developer.qiniu.com/kodo/1206/put-policy[图片]

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 数据迁移

**分类**：对象存储｜数据迁移

### 问题描述

现在要将数据迁移到另一个账号下！如何操作。

### 客服解答

1. 您好，您可以参考下这个文档，使用这种方法的https://developer.qiniu.com/kodo/12666/set-data-migration

2. 您好，这个就是迁移单个空间的，迁移空间级别的

3. 您好，费用的话参考下这个：全托管迁移模式中，从第三方源对象存储拉取数据会产生公网出流量费用，具体费用需要参考源存储云厂商的定价数据迁移在上传期间会产生 PUT/DELETE 请求次数，成功上传到 Kodo 后会产生存储费用

4. 您好，文档有具体操作步骤的，您这边直接按照文档操作即可的，这边也都是按照文档来的

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 账号注销

**分类**：账户与财务｜账户问题

### 问题描述

为公司授权子帐号，目前人员已离职，可以注销

### 客服解答

1. 您好，目前注销可以在控制台操作https://portal.qiniu.com/developer/user/security目前用户自助注销需满足以下所有条件：1、账号为普通账号（非财务父子账号、OEM账号）2、账号下实时消费无产品用量、无消费金额（数据需要您自己删除）对象存储：https://portal.qiniu.com/kodo/bucketCDN：https://portal.qiniu.com/cdn/domain3、账号下无各种欠费实时消费明细（查看您当月消费）https://portal.qiniu.com/financial/bills/estimated-consume如有欠费，将在下月5号出账、8号扣款，结算后，您再提交账号注销。4、账号下没有正在处理的提现审批https://portal.qiniu.com/financial/withdraw5、账号当前没有被冻结注意：账号注销后，账号无法找回

2. 您好，控制台这个链接您无法进行提交吗

3. 您好，稍等下，这边为您同步处理下

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 免费 from 自动催单

**分类**：CDN｜证书问题

### 问题描述

长时间处于域名检测环节

### 客服解答

1. 您好，这边手动介入下处理，麻烦稍等。

2. 您好，您这边文件验证，没有对应的信息，麻烦进行下文件验证您需要根据提示进行文件验证，系统会自动轮询，轮询通过才会颁发证书参考文档：https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

3. 您好，已经给您回滚任务，证书申请已经超时，或者您这边试试手动申请免费证书看下

4. 您好，手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide4.升级HTTPS配置https://developer.qiniu.com/fusion/manual/4952/https-configuration注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

5. 稍等下，这边处理下

6. 您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

系统处理时间较长

---

## 照片

**分类**：对象存储｜上传下载

### 问题描述

上传成功返回路径后，照片显示404，七牛的路劲对象存储空间有照片了，但是无法显示

### 客服解答

1. 您好，分配的测试域名过期了，绑定您自己的域名后访问使用绑定CDN加速域名图文教程文档，您可以参考：https://developer.qiniu.com/fusion/manual/4939/the-domain-name-to-access

2. sk1yrnoq5.hn-bkt.clouddn.com 该测试域名已过期删除了，需要您绑定一个域名使用

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 取消HTTPS访问，取消不了

**分类**：CDN｜配置问题

### 问题描述

我想启用http访问，不要HTTPS了，实现不了。

### 客服解答

1. 您好，您目前是支持http访问的，您开启https是支持http和https访问的

2. 您好，稍等下，这边处理下，需要处理的域名是xxzrjzx.com对吗，稍等

3. 您好，已经完成降级

4. www.xxzrjzx.com对吗

5. 您好，域名已经完成降级

6. 您好，您的本地ip是多少，是不是加入您的ip黑名单了？

7. 您好，自己看下，这个ip网段，您设置了ip黑名单

8. 您好，ping下域名，看下您这边请求的节点，这边代理看下

9. 您好，这边代理看了下

10. 您好，看您这边403都是进行回源了，您这边源站是否正常[图片]

11. 您好，您先看下

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 无法删除域名

**分类**：CDN｜其他类咨询

### 问题描述

删除报错如下[    [        {            "title": "请求 ID",            "content": "iawAehpD-S0NVwAY, iawAehpD-S0NVwAY, iawAehpD-S0NVwAY, iawAehpD-S0NVwAY"        },        {            "title": "日志栈",            "content": "fusiondomain_cud:7/400;APIS:50/400;PORTAL-PROXY:90/400"        }    ]]

### 客服解答

1. 您好删除的域名是什么 这边后台看下

2. 这个域名目前是未备案冻结的状态，冻结的域名无法删除处理， 需要解冻后才能删除

3. 您好，先删除下泛子域名，在删除泛域名看下是否可以删除？

4. 在控制台看下

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 续费已交还是提示过期

**分类**：账户与财务｜计费问题

### 问题描述

已经交了三千多，还是提示续费，10月22到期

### 客服解答

1. 您好，您当前收到的，或者 看到的 和费用有关的信息，方便发一下吗

2. 还没补全信息，到订单管理中补全下，补全信息后-上传确认函-域名验证，证书购买流程：https://developer.qiniu.com/ssl/3663/ssl-the-buying-process订单管理：https://portal.qiniu.com/certificate/ssl#order

3. 您好，您购买成功后，还需要实际 添加域名。https://developer.qiniu.com/ssl/3666/ssl-certificate-of-purchase-process[图片]

4. 「证书通用名称」填写您需要部署证书的域名『证书备注名』自定义其他按照实际情况填写。

5. 对的，就是这个域名列表的域名

6. 您购买的是DigiCert企业型(OV)证书，需要对申请者做严格的身份审核验证,提供可信身份证明，才会签发证书。没有公司的话，您订单退款重新购买TrustAsia的DV域名型证书，公司信息填满即可，不校验。域名归属验证通过就会签发

7. 这边订单管理 关闭订单自动会退款：https://portal.qiniu.com/certificate/ssl#order证书都能用的。

8. 稍等

9. https://portal.qiniu.com/certificate/ssl#order左上角进入「购买证书」[图片]

10. 忽略自动回复，您这边有问题，继续回复即可

11. 关闭订单重新买就行。未签发的订单都能关闭

12. 最左侧的 带限免标记的是免费的，其他需要付费购买

13. 525的是一年有效，免费的是三个月有效，您自行选择。买好了之后，订单『补全』信息-「详情」域名所有权验证-验证通过后签发证书部署域名。

14. 到域名商云解析处添加下这条验证记录[图片]

15. 当前不受影响，还没过期，明天过期就影响了

16. 您好，稍等

17. 没检测到验证记录，您要到你买域名的地方，添加一下红框这条记录，添加好后等待ca检测到就会签发证书了[图片]

18. 前往您购买域名的地方添加解析记录，不在我们平台，我们这边是提供记录信息，要在你买域名的地方配置这条解析记录

19. 您好，目前已支持，自助申请原路提现(支付宝，微信，网上银行)，线下提现(银行卡)功能。提现入口链接：https://portal.qiniu.com/financial/withdraw提现注意事项：1、申请提现前，需将该笔提现充值对应的增值税发票退回至七牛云。发票退票流程2、原路提现预计需3～5个工作日，线下提现预计需要5~15个工作日，七牛打款后具体到账时间以银行为准。3、可提现金额需要扣除实时消费金额、欠票金额、赠送金额和未支付金额。提现说明4、支持未认证用户申请原路提现，不支持申请线下提现5、原路提现充值：微信充值（充值时间小于 330 天）、支付宝充值（充值时间小于 330 天）、网上银行充值（充值时间小于 80 天）

20. 这边看下

21. 订单完成签发了，在我的证书这边「部署」即可https://portal.qiniu.com/certificate/ssl#cert

22. 部署完就好了，退款的应该是您之前的吧，您选能部署的

23. 您好，目前已下发了，证书配置好了。

24. 您好，购买证书提交订单，选择一年期的证书购买，按照之前流程，补全信息-域名验证-部署

25. 是的，一样的。

26. 可以的

27. 不客气的，您这边还有其他问题吗

### 根本原因分析

SSL证书即将过期需要更换

---

## 有些发票未开，平台已不能申请

**分类**：账户与财务｜发票问题

### 问题描述

2023年10月至2024年4月的发票未开，我这边算出来是1000元，请核对下，如果数额正确请帮忙开下增值税专用发票，谢谢。

### 客服解答

1. 您好，提供下开票信息，这边帮您申请超出6个月充值金额，或低于1000元金额的发票，您无法自行申请，不清楚金额的话可以在开票金额栏填写全部金额还请您在控制台提前申请准备好对应的发票抬头信息，添加对应的专票抬头信息审核通过后，如果您已经有了专票的抬头信息，可以不用再次添加，另外，给您开的发票默认是数电发票，需要纸质发票可以说明需求，提供收件地址。根据《增值税专用发票使用规定》申请专票必须要和实名认证公司名保持一致。-------------开票信息-----------开票金额:发票抬头: 发票类型: 纳税人识别号: 开户银行名称: 开户账号: 公司名称: 公司地址: 联系电话:

2. 收到

3. 已提交申请，后续可以在发票管理中关注进度以及后续下载发票https://portal.qiniu.com/financial/invoice-contract/invoice

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 上传图片时无法联系DNS服务器

**分类**：对象存储｜上传下载

### 问题描述

使用api.jiutoubiao.com上传文件到空间时概率出现错误如下:array (  0 => NULL,  1 =>   Qiniu\Http\Error::__set_state(array(     'url' => 'https://[REDACTED_DOMAIN]/v4/query?ak=kXDt__a5sFqlVi6VB0Jc1NPgGtMAc3ioVQ1ahj3l&bucket=yst-files',     'response' =>     Qiniu\Http\Response::__set_state(array(       'statusCode' => -1,       'headers' =>       array (      ),       'normalizedHeaders' => NULL,       'body' => NULL,       'error' => 'Could not resolve: api.qiniu.com (Could not contact DNS servers)',       'jsonData' => NULL,       'duration' => 0.0,    )),  )),)

### 客服解答

1. 您好ping一下对应存储空间域名，例如 华东存储 ping up.qiniup.com 或者 upload.qiniup.com 看能否 ping 通。其他地区参考：https://developer.qiniu.com/kodo/manual/1671/region-endpoint

2. 可以用我们的sdk上传试下 您使用的是哪种语言

3. 有可能

4. 用这个demo上传测试下是否可以https://[REDACTED_DOMAIN]/qiniu/php-sdk/blob/master/examples/upload_simple_file.php

5. 服务器重启一下再上传

6. 好的

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 请增加一个公网ip

**分类**：云主机｜主机

### 问题描述

[配额不足]：您的 弹性公网IP带宽 配额不足，请清理资源后重新尝试，或提交[工单]联系我们。

### 客服解答

1. 您好，您这边是需要创建一个多大的弹性公网IP呢？

2. 您好，多少带宽的弹性公网IP呢？

3. 您好，您这边目前IP带宽还有100MB的额度，建议您这边可以看下创建100MB以内进行使用看下的，100MB以内的应该是可以正常创建的

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 更换手机号

**分类**：账户与财务｜账户问题

### 问题描述

更换安全手机号，找不到原来的手机号，和邮箱。

### 客服解答

您好，修改手机号有如下三种方式，如果您的手机无法接受验证码可以使用方法二和方法三进行申请修改手机号：方法一：点击官网右上角的管理控制台——个人面板——个人中心的安全设置更改手机，发送手机验证码，验证之后就可以对手机号进行修改。[图片]方法二：点击官网右上角的管理控制台——个人面板——个人中心的安全设置更改手机，选择邮箱验证码，验证之后就可以对手机号进行修改。[图片]方法三：通过人工申诉提供相关资料进行修改，将材料发送邮件到 [REDACTED_EMAIL] ，需要提供的信息如下：a、个人实名认证：请提供注册邮箱、修改原因、手持与实名认证一致的身份证正面图片、新手机号码；b、企业实名认证：请提供注册邮箱、修改原因、实名认证的营业执照图片、申请人手持正面身份证图片、新手机号码。（注意：为了您的账号信息安全，修改手机号时需要您提供相关信息，这边为您审核处理，感谢您的理解与配合～）邮件发送后请工单上告知我们。我们后台操作完毕后，重新登录系统会提示您短信验证新的手机号，验证完毕后手机号即修改完成。

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 使用抓取网络资源到空间报错

**分类**：对象存储｜上传下载

### 问题描述

httpGet url failed: E502n{"error":"Get "http://[REDACTED_IP]:9090/sffile/z/SvW/OW/[REDACTED_KEY]/anYAZWbhhaPlA": circuit breaker is open"}httpGet url failed: E502n{"error":"Get "http://[REDACTED_IP]:9090/sffile/u/Yvn/oBH/[REDACTED_KEY]/zlXyqldtxxZkM": dial tcp [REDACTED_IP]:0-u003e36.137.79.200:9090: i/o timeout"}使用抓取网络资源到空间报这个问题，具体是什么原因，跟对方网络有关吗

### 客服解答

1. 您好，需要公网环境可以访问获取到的url链接才行的您的这个链接公网访问不到的http://[REDACTED_IP]:9090/sffile/z/SvW/OW/NeoklgBWquZzzOvvmzvegvuZPrBLmzDIBbOUExrkGXxXpzrYuhyHQzLc/anYAZWbhhaPlA

2. 您好，502的话基本上就是拉取超时，或者请求超时了的，是资源url的问题导致的

3. 嗯嗯好的

4. 您这个链接是多久有效期的

5. 您好，您给时间设置为1个小时看下，顺便看下您的客户端和服务器的时间等是否一致的

6. 您好，您给时间设置为1天看下，顺便看下您的客户端和服务器的时间等是否一致的

7. 您好，那您这边可以测试一下其他正常公网地址都是否正常的

8. 您好，这个502的话是链接超时的，您这边看下让他这边生成一个时间为1天甚至更久的看下的

9. 您好，那这个是没有办法的，拉取其他资源都没有问题的话说明接口是正常的，第三方这边17号后是否有调整过什么呢？

10. 您好，您可以看下报错的502错误的网关的，这个问题属于源站的，您这边需要与第三方确认一下的，这个错误类型不属于我们这边的您这边可以访问下载的话建议您这边可以自行下载到本地上传到存储空间的，如果被抓取的源站屏蔽（屏蔽可能是抓取源站有 IP、UA 等限制策略）来自七牛的抓取操作，那么我们是不能确保一定可以抓取成功。[图片]

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 处理时间超时

**分类**：CDN｜配置问题

### 问题描述

处理时间超时

### 客服解答

您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

系统处理时间较长

---

## 现在这一步一直停在这里

**分类**：账户与财务｜账户问题

### 问题描述

你好现在一直在这个页面，要审核多久

### 客服解答

1. 这边帮您催下，稍等

2. 您好，刷新下页面，会有提交页面的

3. 您好，重新登录看下，目前看状态是需要您填写金额

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 使用qiniu-js 里面的upload接口（版本号：3.3.3）时，会出现network error. 的报错

**分类**：对象存储｜上传下载

### 问题描述

您好，在我们使用qiniu-js 里面的upload接口（版本号：3.3.3）时，会有时出现network error. 的报错，请问可以帮忙查一下更具体的错误信息吗？最近的一次出现时间是：2024-10-17 16:00:07.921

### 客服解答

1. 您好，network error就是网络错误的

2. 您好，没有的，这种报错是是没有请求到七牛的，这边没有记录的

3. 您好，因为网络原因，没有请求上这种没有请求到我们这边是没有记录的

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 账号注销

**分类**：账户与财务｜账户问题

### 问题描述

账号注销

### 客服解答

您好，目前注销可以在控制台操作https://portal.qiniu.com/developer/user/security目前用户自助注销需满足以下所有条件：1、账号为普通账号（非财务父子账号、OEM账号）2、账号下实时消费无产品用量、无消费金额（数据需要您自己删除）对象存储：https://portal.qiniu.com/kodo/bucketCDN：https://portal.qiniu.com/cdn/domain3、账号下无各种欠费实时消费明细（查看您当月消费）https://portal.qiniu.com/financial/bills/estimated-consume如有欠费，将在下月5号出账、8号扣款，结算后，您再提交账号注销。4、账号下没有正在处理的提现审批https://portal.qiniu.com/financial/withdraw5、账号当前没有被冻结注意：账号注销后，账号无法找回

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 域名https配置7个小时了还未完成，麻烦看下

**分类**：CDN｜配置问题

### 问题描述

麻烦看下这个域名处理，配置了SSL证书，设置了https。之前都很快的，这次时间太长了，没遇到过这么长时间。。。

### 客服解答

1. 您好，这边手动介入下处理，麻烦稍等。

2. 您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

系统处理时间较长

---

## 这两个地方的统计总是对不上，文件已经转过去好些天了。

**分类**：对象存储｜其他类咨询

### 问题描述

这两个地方的统计总是对不上，文件已经转过去好些天了。

### 客服解答

您好存储计费是按照每天的存储容量累加，然后除以 30天，算出本月平均每天存储量，然后基于这个量进行扣费

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 域名加速删除

**分类**：CDN｜其他类咨询

### 问题描述

请问如何恢复域名加速

### 客服解答

1. 您好，是哪个域名呢，已经被删除了的域名吗

2. 您好，已删除的域名和空间，您可以重新创建下

3. 您好，删除后是无法恢复的

4. 您好，重新创建该域名哈绑定CDN加速域名图文教程文档，您可以参考：https://developer.qiniu.com/fusion/manual/4939/the-domain-name-to-access

5. 您好，是的，删除后就没有了，重新创建的是空的空间

6. 您好，好的，您这边还有什么问题吗

### 根本原因分析

产品功能限制，不支持手动删除

---

## 给图片增加水印费用怎么算

**分类**：对象存储｜工具使用

### 问题描述

想给一张图片在左下角加一个文字水印,想了解下费用情况.比如:一张500kb的图片想知道费用主要体现在哪些方面?

### 客服解答

1. 稍等

2. 您好文字水印处理-使用：https://developer.qiniu.com/dora/1316/image-watermarking-processing-watermark#3文档后面有使用示例。定价：https://developer.qiniu.com/dora/1316/image-watermarking-processing-watermark#3图片水印处理-价格：每月 0 - 10 TB：免费10 TB 以上：0.025 元/GB

3. 您好，是的，处理一次算一次费用访问的话，有缓存的情况是直接返回处理后的缓存资源，相同链接在缓存有效期内 不会产生二次处理费用。

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 更换证书卡住

**分类**：CDN｜配置问题

### 问题描述

img.zjjcts.com更换证书卡住

### 客服解答

您好目前看已经配置完成

### 根本原因分析

配置相关问题

---

## bad gateway: getsrc reach max try times

**分类**：对象存储｜上传下载

### 问题描述

https://[REDACTED_DOMAIN]/attach/202410041700/e331cfe3/202013020098%20%E5%BC%A0%E9%83%A1%20%E4%B8%8B%E9%A2%8C%E7%89%99%E5%88%97%E7%BC%BA%E5%A4%B1%E6%82%A3%E8%80%85%E7%9A%84%E8%AF%8A%E7%96%97%E6%96%B9%E6%A1%88%E8%AE%BE%E8%AE%A1.pdf?sign=96326eb3dbe4efab466ed9c3f9c65d1a&t=6715d4d7这个链接，在个别电脑上显示不正常，提示bad gateway: getsrc reach max try times（该电脑打开百度等网站均正常）其它电脑上又能正常下载该链接

### 客服解答

1. 您好，使用这个链接测试看下呢https://[REDACTED_DOMAIN]/attach/202410041700/e331cfe3/202013020098%20%E5%BC%A0%E9%83%A1%20%E4%B8%8B%E9%A2%8C%E7%89%99%E5%88%97%E7%BC%BA%E5%A4%B1%E6%82%A3%E8%80%85%E7%9A%84%E8%AF%8A%E7%96%97%E6%96%B9%E6%A1%88%E8%AE%BE%E8%AE%A1.pdf

2. 您好，这个报错是网关有问题的，需要确认一下那台电脑的本地网络缓存的，应该是本地网络有问题的

3. 您好，嗯嗯好的不客气的

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 不清楚为什么消耗越来越高

**分类**：对象存储｜其他类咨询

### 问题描述

储存消耗相对比往期消耗越来越大 想问下是什么情况

### 客服解答

您好查看上月账单明细：您可以登录七牛云管理控制台 - 财务中心 - 账单和消费详情，点击账单编号查看详细的消费明细：https://portal.qiniu.com/financial/summary查看实时消费明细：您可以登录七牛云管理控制台 - 财务中心 - 实时消费明细：https://portal.qiniu.com/financial/estimated-consume如果您对某个部分有疑问，可以截图到工单中，这边帮您解释下

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 无法连接主机

**分类**：云主机｜主机

### 问题描述

续费后无法连接主机,ssh 和  宝塔 都连接不上

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 数据恢复

**分类**：对象存储｜其他类咨询

### 问题描述

有几个文件删除错了还能恢复吗

### 客服解答

您好，十分抱歉目前这边不支持恢复数据的，建议您这边重新上传一下的

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 我想把我其中一个空间的对象迁移到一个新的帐号里，请问如何处理？

**分类**：对象存储｜数据迁移

### 问题描述

我想把我其中一个空间的对象迁移到一个新的帐号里，请问如何处理？请问咱们七牛有没有提供什么工具来操作？

### 客服解答

1. 不同账号下相同存储区域的数据迁移方式您好，不同账号下相同存储区域的数据迁移，有两种方法1、您这边可以先使用空间授权，然后再使用 qshell 工具中的 batchcopy 命令将一个空间中的文件批量复制到另一个空间。这个是空间授权的操作文档：https://developer.qiniu.com/kodo/manual/3647/authorization-of-the-space这个是 qshell 的说明文档：https://developer.qiniu.com/kodo/tools/1302/qshell第一步：qshell 列举空间中文件列表 https://[REDACTED_DOMAIN]/qiniu/qshell/blob/master/docs/listbucket.md第二步：qshell 的 batchcopy 方法把文件进行复制到新空间 https://[REDACTED_DOMAIN]/qiniu/qshell/blob/master/docs/batchcopy.md2、您这边可以先使用空间授权，然后再使用图形化工具将一个空间中的文件批量复制到另一个空间。这个是空间授权的操作文档：https://developer.qiniu.com/kodo/manual/3647/authorization-of-the-space图形化工具文档：https://developer.qiniu.com/kodo/5972/kodo-browser 注意：使用该工具目前进行上传/下载，如果不指定cdn域名的话，下载产生的流量费用为「外网流量」

2. 您好，相同区域的迁移，上面的方式都是没有收费的

### 根本原因分析

配置相关问题

---

## 更改绑定手机号

**分类**：云短信｜短信发送问题

### 问题描述

原手机号[REDACTED_PHONE]所属员工已离职，无法获取验证码，现需要修改绑定手机号为[REDACTED_PHONE]

### 客服解答

您好，邮箱是否可以收验证码？可以的话，可以使用邮箱接收验证码，进行修改

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 修改文件存储类型 c#8.6.0.0接口版本  要求不一致

**分类**：对象存储｜SDK使用

### 问题描述

修改文件存储类型 c#8.6.0.0接口版本  要求不一致

### 客服解答

1. 您好，bucket，key是EncodedEntryURI传参 ，filetype 是 type传参 和接口文档传参一致的。您的疑惑可以具体描述下吗

2. 具体错误信息提供下呢

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 费用问题

**分类**：对象存储｜其他类咨询

### 问题描述

你们企微恢复太慢了, 我用工单提问:1. 对象存储只使用了外网流出流量, 实时费用不够扣了, 如果别人继续刷流量, 是否一直欠费下去? 还是说到达欠费多少就不能访问?2. 如果使用CDN, 费用对比起只用外网流出流量, 费用是增加还是减少的, 费用构成有哪些?

### 客服解答

1. 您好1、是的，欠费冻结之后才会停止访问，不再产生费用2、正常来说是降低的您当前使用了七牛的存储服务和七牛的 CDN 服务；在此过程中可能产生的费用有：1、数据存储费用2、CDN 的下载流量费用3、从 CDN 节点回七牛存储源站产生的回源流量费用；当前七牛的免费额度策略为：存储空间免费额度：10G/月CDN 下载流量费用免费额度：10GB/月回源流出流量费用免费额度：10GB/月问题：CDN 流量和 CDN 回源流量的区别是什么？答：用户访问 CDN 时，CDN 节点与用户的网络通信过程产生的流量，是 CDN 流量。CDN 节点与源站的网络通信过程产生的流量，是 CDN 回源流量。

2. 您好，是的账号欠费会进入欠费保护期，欠费保护期内是可以正常访问的，这个期间没有补齐欠款就会进行账号冻结

3. 您好，个人认证是3天的

4. 您好，停止解析不太行，因为dns解析可能存在缓存。需要在七牛停用。且删除域名，停用域名解析才行

5. 您好，也是可以的

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 图片上传成功了， 但是不显示

**分类**：对象存储｜上传下载

### 问题描述

https://[REDACTED_DOMAIN]/[REDACTED_KEY].pnghttps://[REDACTED_DOMAIN]/[REDACTED_KEY].pnghttps://[REDACTED_DOMAIN]/[REDACTED_KEY].pnghttps://[REDACTED_DOMAIN]/1729403473007982104654.png这四个链接的图片不显示

### 客服解答

1. 您好图片元信息是heic的 需要用指定的应用程序打开[图片]

2. 建议转换一下图片格式打开 https://developer.qiniu.com/dora/8258/format-conversion[图片]

3. 是您的图片元信息的问题 格式是heic 看下工单的第一条回复截图

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 加载速度

**分类**：CDN｜其他类咨询

### 问题描述

目前有购买cdn加速资源包，我方APP的图片和视频都存储在七牛云上，部分时段会有用户集中上传视频和图片的情况，此时其他用户查看APP内的视频和图片时加载速度较慢，有卡顿的情况是否还有其他，如购买资源包等提速方法?当前可用带宽上限是多少，能否提升？

### 客服解答

1. 您好，图片视频访问使用的是哪个域名呢，这边检查下

2. 稍等

3. 上传和访问下载没有关联性，不会因为集中上传导致访问慢，上传和访问用的不是用一个域名。域名配置检查没有什么异常。可以提供下加载慢的客户端ip，请求url 和请求时间，reqid ，我们核对日志分析具体原因。

4. 您好，cdn没有固定的带宽额，有智能调度分发的，足够达到客户端的带宽上限。没有其他的服务购买。视频卡顿大部分原因都是客户端本地网络带宽低，达不到视频码率要求。可以参考下：https://developer.qiniu.com/fusion/kb/4082/video-playback-caton-unable-to-play

### 根本原因分析

配置相关问题

---

## 无法访问

**分类**：CDN｜访问下载

### 问题描述

403  无法访问 https://[REDACTED_DOMAIN]/

### 客服解答

1. 稍等

2. 这边测试可以访问的呢[图片]

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 图片链接失效

**分类**：对象存储｜其他类咨询

### 问题描述

今天全部的图片链接都失效了，官网没有详细问题解释不知道怎么处理

### 客服解答

您好，根据您的描述可以判断您的问题是由于空间使用的测试域名被回收导致的。原因：您空间绑定的测试域名已经在近期进行回收了，并且是无法恢复的。测试域名是七牛提供用于功能测试的域名，请勿用于线上生产环境，同时，测试域名仅有30天的生命周期，到期后会进行自动回收。我们会在回收前一周和回收当天向您发送回收告知邮件，您可以确认邮箱中的邮件核实具体回收时间。解决方法：回收测试域名对您的存储资源没有影响，不会删除您的资源，也不需要重新上传资源。您绑定自定义域名后，通过自定义域名访问即可。如果您的域名已经在工信部备案，请参考域名绑定教程：https://developer.qiniu.com/kodo/kb/5158/how-to-transition-from-test-domain-name-to-a-custom-domain-name如果您需要了解测试域名的使用规范请参考：https://developer.qiniu.com/fusion/kb/1319/test-domain-access-restriction-rules--------------------------------------Q:部分资源可以访问，新资源无法访问。A:旧资源可以访问是因为cdn缓存未失效，您刷新cdn缓存后现象会保持一致。

### 根本原因分析

产品功能限制，不支持手动删除

---

## 已设置域名验证但是校验始终未生效

**分类**：CDN｜证书问题

### 问题描述

订单号：6715d3305f6374b135e20629已配置cname，并测试已生效：https://[REDACTED_DOMAIN]/detect/dns/9e9fb142f0ba41bc9fd88db81e7fc16a

### 客服解答

1. 您好，您这边将您的解析配置截图给一下，这边看下

2. 您好，目前看您的订单已经完成了的

### 根本原因分析

配置相关问题

---

## 上传图片和存储图片的时候显示 expired token

**分类**：对象存储｜上传下载

### 问题描述

上传图片，微信小程序端保存头像是显示微信小程序在获取头像和上传相册照片都无法保存，显示expired token

### 客服解答

1. 您好上传token过期了 重新生成一下

2. 需要后端程序侧实现

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 批量删除某个日期之前的存储数据需要怎么操作

**分类**：对象存储｜其他类咨询

### 问题描述

请问批量删除某个日期之前的存储数据需要怎么操作？有没有可视化的管理工具来操作

### 客服解答

您好，这个目前没有可视化工具的，目前的话可视化工具暂无法列举时间的，可以批量删除可视化工具可以使用图形化工具 图形化工具 Kodo Browser 勾选您需要删除的文件或前缀目录一键删除kodo browser 参考文档：https://developer.qiniu.com/kodo/tools/5972/kodo-browser正常可以使用命令行工具的，您可以通过qshell批量删除，三条命令就可以了。1.先下载qshell工具并使用qshell account 命令登陆账户。下载及安装文档 https://developer.qiniu.com/kodo/tools/1302/qshellwindows环境下安装qshell教程 https://developer.qiniu.com/kodo/kb/5545/windows-environment-installation-qshell-tutorial2.使用listbucket2命令列举出空间内具体时间范围内的文件的命令文档 https://[REDACTED_DOMAIN]/qiniu/qshell/blob/master/docs/listbucket2.md3.使用batchdelete命令批量删除第2步列举出的列表文件。例如 qshell batchdelete --force 空间名 -i result.txt命令文档 https://[REDACTED_DOMAIN]/qiniu/qshell/blob/master/docs/batchdelete.md注意：主动删除资源不可以恢复，请慎重

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 你好，幫我看下，我配置域名管理的問題

**分类**：对象存储｜其他类咨询

### 问题描述

[    [        {            "title": "请求 ID",            "content": "gAeQw4SQozkxYAAY, gAeQw4SQozkxYAAY, gAeQw4SQozkxYAAY, gAeQw4SQozkxYAAY"        },        {            "title": "日志栈",            "content": "fusiondomain_cud:3/400;APIS:49/400;PORTAL-PROXY:135/400"        }    ]]

### 客服解答

1. 您好，您稍等这边确认一下

2. 您好，抱歉让您久等了，已经处理完成，您确认下。

3. 您好，这边看您操作了删除域名了，您这边删除后重新创建上线一下的，不要删除域名的，目前是域名验证未通过的，需要使用域名验证的

### 根本原因分析

域名所有权验证未通过

---

## 域名卡顿

**分类**：CDN｜访问下载

### 问题描述

网站非常卡  上传照片卡。

### 客服解答

1. 您好，您这边网站使用的是什么域名？qn.tpjiaze7777.top的话，看起来是没有进行解析的

2. qn.tpjiaze2024.top访问看起来很快是正常的

3. 您好，qn.tpjiaze2024.top只是访问，上传卡顿的话，您这边ping下您的上传域名看下

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 被恶意刷流量

**分类**：CDN｜流量计费问题

### 问题描述

天天被刷流量，怎么看是从哪个域名访问得、统计根本看不出

### 客服解答

1. 您好分析具体的访问量和访问行为，建议在控制台 https://portal.qiniu.com/cdn/log 下载CDN日志后进行分析或者通过API来下载，参考文档：https://developer.qiniu.com/fusion/api/1226/download-the-logCDN日志的下载方式，以及日志中字段的含义参考文档：https://developer.qiniu.com/fusion/manual/3847/cdn-log-fusion这边可以查看到访问量前100的流量和ip：https://portal.qiniu.com/cdn/statistics/log/top针对非法的请求和访问，建议配置 referer 和 ip 黑白名单等方式来进行访问限制。

2. 您好，是不需要使用这个域名？如果不需要访问存储内的资源，其实可以不绑定域名的防止别人恶意访问你的资源产生大量流量，单纯的从cdn的层面上来处理，是不能完全规避掉的。CDN上支持多种防盗链配置，不同的防盗链适用于不同的应用场景，建议可以在 融合cdn => 域名管理 => 配置 => 访问控制 中设置1：referer防盗链： 只有携带了相应referer 请求头 的 http请求才能访问资源，但是对于技术来说，referer都是可以伪造的，存在一定的风险2：时间戳防盗链，url带着e和token参数访问，e为过期时间，但是只要捕获到了url就可以访问资源了，只适用于访问xx次的场景3：回源鉴权，这个你们可以尝试下，每次访问cdn图片时，会携带你们自己定义的访问参数去你们自己的服务器上鉴权，只有你们服务器鉴权通过，返回 httpcode=200 ，才会将图片资源给用户访问，否则无法返回图片4：IP黑白名单，这个适合某一个网段内的ip访问资源，不适合官网使用，只有在 ip 白名单中的用户才可以访问你们的图片参考文档：https://developer.qiniu.com/fusion/4960/access-control-configuration☆推荐使用第三种回源鉴权和第四种IP黑白名单进行访问限制。

### 根本原因分析

配置相关问题

---

## 修改 HTTPS 配置处理中，较长时间未配置完成，也无法停用

**分类**：CDN｜配置问题

### 问题描述

修改 HTTPS 配置处理中，通常情况下 8-15 分钟完成，期间域名访问不受影响，部分配置不可修改，若较长时间未配置完成，请提交工单反馈

### 客服解答

1. 稍等

2. 久等了，配置已下发

### 根本原因分析

系统处理时间较长

---

## amr转mp3文件失败

**分类**：智能多媒体｜音视频处理

### 问题描述

amr转mp3文件报错，execute fop cmd failed: invalid media

### 客服解答

https://[REDACTED_DOMAIN]/[REDACTED_KEY].amr这个文件原文件有问题的无法正常获取文件的信息https://[REDACTED_DOMAIN]/c88f15800d384e73add4493a5e5c176c.amr?avinfo

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 如果对象储存里面删除了

**分类**：对象存储｜其他类咨询

### 问题描述

有回收站机制吗

### 客服解答

您好存储侧没有回收站机制的

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 文件下载添加v=123刷新cdn缓存

**分类**：对象存储｜上传下载

### 问题描述

下载文件时候通过下载链接追加v=123强制刷新缓存  在私有空间不能生效嘛https://[REDACTED_DOMAIN]/TestDataForSafe_%E4%B8%8B%E5%8F%91%E5%B1%A5%E5%8E%86_2024-10-21-10-21-38.%E6%B5%8B%E8%AF%95%E6%95%B0%E6%8D%AE1.zip?e=1730785779&token=[REDACTED_KEY]:y8WTlyKb8TcUtskFmvFY0Kra4kA=?v=1729489780000

### 客服解答

1. 私有链接中参数也是需要签算的内容需要先加参数，再进行私有签算生成链接

2. 是的，私有空间需要先加参数，再私有签算加参后的链接。

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 800的充值提交不了发票

**分类**：账户与财务｜发票问题

### 问题描述

800的充值提交不了发票，没有发票财务不给新的充值

### 客服解答

1. 您好，提供下开票信息，这边帮您申请超出6个月充值金额，或低于1000元金额的发票，您无法自行申请，不清楚金额的话可以在开票金额栏填写全部金额还请您在控制台提前申请准备好对应的发票抬头信息，添加对应的专票抬头信息审核通过后，如果您已经有了专票的抬头信息，可以不用再次添加，另外，给您开的发票默认是数电发票，需要纸质发票可以说明需求，提供收件地址。根据《增值税专用发票使用规定》申请专票必须要和实名认证公司名保持一致。-------------开票信息-----------开票金额:发票抬头: 发票类型: 纳税人识别号: 开户银行名称: 开户账号: 公司名称: 公司地址: 联系电话:

2. 收到

3. 已提交申请，后续可以在发票管理中关注进度以及后续下载发票https://portal.qiniu.com/financial/invoice-contract/invoice

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 存储

**分类**：对象存储｜工具使用

### 问题描述

https://[REDACTED_DOMAIN]/2024/10/21/6715eb54aa6fd.jpg?e=1729490406&token=fCPfUS8vYSYrDdOX_EqCu6vpSHZHjKJaNvTXZAwJ:[REDACTED_KEY]=你好我这个客户那边给的链接  怎么要跟上后面一个token   不加https://[REDACTED_DOMAIN]/2024/10/21/6715eb54aa6fd.jpg就打不开 是存储那边设置了什么吗

### 客服解答

您好开启私有空间需要授权访问 把私有空间调整为公开的不需要加参数

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 推流限时鉴权SK的方式h5项目可以用吗？

**分类**：直播云｜推流问题

### 问题描述

https://developer.qiniu.com/pili/kb/1332/broadcast-authentication-mode?category=kb         web h5项目 可以直接通过该链接的方式推流吗？

### 客服解答

您好，您这边是为什么需要使用推流鉴权呢？

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 免费 from 自动催单

**分类**：CDN｜证书问题

### 问题描述

长时间处于域名发布环节

### 客服解答

您好已经处理好了 您再看下

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 文件无法通过https访问?

**分类**：对象存储｜上传下载

### 问题描述

https://[REDACTED_DOMAIN]/jihezheneng_images/[REDACTED_KEY].jpg可以访问,但https://[REDACTED_DOMAIN]/jihezheneng_images/94d75f35f114484bb2f8577924253d9b.jpg却无法访问

### 客服解答

1. 您好，需要部署SSL证书后开启https才能使用https协议的，您这边需要先购买证书的您好，手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide4.升级HTTPS配置https://developer.qiniu.com/fusion/manual/4952/https-configuration注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

2. 您好，这个是缓存的，您这边清理一下缓存后再看下

3. 您好，1.该文件是否有进行过删除操作？您检查一下上传时候是否指定了 deleteAfterDays，或者是存储空间设置了生命周期( https://developer.qiniu.com/kodo/manual/3699/life-cycle-management )2.是否有对文件做过 move 操作 ( https://developer.qiniu.com/kodo/api/1288/move )3.是否有大致的文件上传时间和删除时间

### 根本原因分析

配置相关问题

---

## 申请合同的流程

**分类**：CDN｜其他类咨询

### 问题描述

申请合同的详细流程是怎么样的

### 客服解答

1. 您好，您这边可以参考下这个的https://developer.qiniu.com/af/12440/electronic-contract-documentation-and-operation-manuals

2. 您好，您这边可以留一下您的联系方式，这边反馈一下商务经理与您确认一下的

3. 您好，嗯嗯好的您稍等

4. 嗯嗯

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 企业认证审核，请尽快帮忙处理下、

**分类**：账户与财务｜账户问题

### 问题描述

急需要用到贵公司的全站加速产品，请尽快帮忙处理企业认证

### 客服解答

1. 您好，稍等下，这边催下进度

2. 您好，您的认证已经审核，您稍等下，系统会进行打款，完成打款验证就好

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## www.zdushi.com不能访问

**分类**：CDN｜配置问题

### 问题描述

www.zdushi.com不能访问

### 客服解答

您好，nslookup查看下您的域名解析呢

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 消防类摄像头

**分类**：视频监控｜业务咨询

### 问题描述

1、海康的消防类摄像头 没有火警报警的事件2、如何获取摄像头里报警的实时截图

### 客服解答

1. 稍等

2. 可以参考下 最佳实践-报警联动(收到报警触发录制截图)：https://developer.qiniu.com/qvs/12511/alarm-linkage

3. 您好，没有的话，就是不支持，报警需要设备发通知到我们服务端。

4. 是的，不支持

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 取消这个域名的创建

**分类**：CDN｜配置问题

### 问题描述

取消这个域名的创建

### 客服解答

您好，已停止创建，您可以直接在控制台删除域名

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 修改文件存储类型

**分类**：对象存储｜SDK使用

### 问题描述

修改文件存储类型时，使用接口  BucketManager bucketManager = new BucketManager(mac,config,null); HttpResult httpResult = bucketManager.ChangeType(bucketName, filename, 3);返回结果必须使用适当的属性 或方法修改“content-type”标头。 参数名: name

### 客服解答

1. 您好，存储类型转换比较推荐工具实现您这边可以使用qhsell工具进行批量转存储类型的qshell工具：https://developer.qiniu.com/kodo/1302/qshell#9batchexpire命令：https://[REDACTED_DOMAIN]/qiniu/qshell/blob/master/docs/batchchtype.md

2. 需要您先参考文件类型修改的接口：https://developer.qiniu.com/kodo/api/3710/chtype然后再参考批量处理的接口，进行批量修改：https://developer.qiniu.com/kodo/api/1250/batch

3. 是的 可以参考 ：[图片]

4. 程序侧您那边是怎么写的 给下截图

5. 用 https://developer.qiniu.com/kodo/1237/csharp 这个里面改存储类型的demo试下

6. 可能是您用的sdk是老版本的问题 升级到8.6看下[图片]

7. 建议安装最新版8.6 这个

8. 好的 您再观察下

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 域名状态：处理中

**分类**：CDN｜刷新缓存问题

### 问题描述

一直显示处理中。导致我很多客户现在是系统都访问不到图片

### 客服解答

1. 稍等

2. 久等了，配置已下发

### 根本原因分析

系统处理时间较长

---

## 能否关闭掉这个流量计费

**分类**：CDN｜流量计费问题

### 问题描述

每个月有很多CDN的流量，计费，不清楚是哪里产生的。看能不能关掉。目前这个账号里面的存储 只是测试用的。

### 客服解答

1. 您好，可以在这边停用-删除域名。cdn域名管理：https://portal.qiniu.com/cdn/domain

2. 您好，请求域名相关的资源url，产生使用量了才会计费。

3. 您好，一样也会产生流量费用的。

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## S3兼容上传报找不到桶

**分类**：对象存储｜SDK使用

### 问题描述

package com.ikingtech.framework.sdk.oss.embedded.core;import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;import software.amazon.awssdk.auth.credentials.[REDACTED_KEY];import software.amazon.awssdk.core.sync.RequestBody;import software.amazon.awssdk.regions.Region;import software.amazon.awssdk.services.s3.S3Client;import software.amazon.awssdk.services.s3.model.PutObjectResponse;import software.amazon.awssdk.services.s3.presigner.S3Presigner;import software.amazon.awssdk.services.s3.presigner.model.[REDACTED_KEY];import java.io.File;import java.net.URI;import java.time.Duration;public class App {    public static void main(String[] args) {        final S3Client s3 = S3Client.builder().region(Region.of("cn-south-1")) // 华东-浙江区 region id                .endpointOverride(URI.create("https://[REDACTED_DOMAIN]")) // 华东-浙江区 endpoint                .credentialsProvider(                        [REDACTED_KEY].create(                                AwsBasicCredentials.create("[REDACTED_LONG_KEY]", "[REDACTED_LONG_KEY]")))                .build();        final PutObjectResponse putObjectResponse = s3.putObject(b -> b.bucket("rsq").key("test.png"),                RequestBody.fromFile(new File("C:\\Users\\PC\\Downloads\\Snipaste_2024-10-16_14-55-01.png")));        System.out.printf("ETag: %s\n", putObjectResponse.eTag());    }}

### 客服解答

您好，试下这个demo上传

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 我忘记了以前的密码

**分类**：账户与财务｜账户问题

### 问题描述

现在没有办法修改密码

### 客服解答

您好，退出登录后，可在登录页面下方「忘记密码」处，通过账号绑定的手机号或邮箱重置密码[图片]

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 图片资源在浏览器上无法展示

**分类**：对象存储｜其他类咨询

### 问题描述

上传的七牛图片资源在谷歌浏览器上一直显示不出来怎么回事，请过缓存也不行

### 客服解答

1. 您好麻烦粘贴一下您的图片链接地址 这边看下

2. 查看证书是在有效期内的 清除一下缓存再看下

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 免费 from 自动催单

**分类**：CDN｜证书问题

### 问题描述

长时间处于免费证书申请环节

### 客服解答

1. 您好，这边手动介入下处理，麻烦稍等。

2. 您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

系统处理时间较长

---

## 使用listbucket 产生的文件在哪个目录

**分类**：对象存储｜工具使用

### 问题描述

schoolallpic.txt 文件不知道产生在什么地方，没有和qshell在同一个目录下

### 客服解答

您好，这个正常是生成在您的本地地址的，这个我们也确认不到的，您这边需要自行查找一下的，您看下到本地文件中搜索一下呢

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 在域名下访问链接403

**分类**：CDN｜访问下载

### 问题描述

我在https://[REDACTED_DOMAIN]/域名下访问https://[REDACTED_DOMAIN]/1729072165828.png?imageslim/zlevel/1&e=1729496686&token=vmkXHu93POBCiStQpDc3VLCO9t_sQtGbZzKLPmJm:qQtrHbZHkPa1HdCsAFaqd8WRBEY=这个地址，报出403，这个地址单独在浏览器上是可以打开的.

### 客服解答

你好，*.boyuebsc.com是不包括boyuebsc.com，需要加一个boyuebsc.com

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 忘记登陆密码

**分类**：账户与财务｜账户问题

### 问题描述

忘记登陆密码

### 客服解答

您好，退出登录后，可在登录页面下方「忘记密码」处，通过账号绑定的手机号或邮箱重置密码[图片]

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 无法配置Cname，自有网站的存储功能无法链接到七牛云的云盘里

**分类**：对象存储｜上传下载

### 问题描述

我这边设置了域名解析和自定义CDN加速域名，但是还是没办法正常使用CNAME，并且云存储里的文件没办法使用外链访问，想知道我这边问题出在哪里

### 客服解答

您好，主机记录修改成cdn[图片]

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 镜像回源

**分类**：对象存储｜镜像存储

### 问题描述

镜像回源在拉取资源的时候，能不能限制只对某些格式进行回源，比如只回源js和css，禁止回源png和jpg，这里只是举个例子。

### 客服解答

您好，很抱歉，不行的

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 对象存储可以使用第三方cdn吗

**分类**：对象存储｜其他类咨询

### 问题描述

对象存储可以使用第三方cdn吗

### 客服解答

您好不支持，不使用我们的cdn您可以绑定源站域名使用

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 删除five-time.cn 子域名

**分类**：CDN｜配置问题

### 问题描述

七牛之前同事，需要删除five-time.cn 子域名

### 客服解答

您好，稍等

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 充值忘记备注账号了

**分类**：账户与财务｜账户问题

### 问题描述

充值忘记备注账号了

### 客服解答

1. 好的 ，收到，这边商务会尽快协助您完成入账的

2. 您好，您不用谢的

3. 您好，久等了，已入账，您确认下

### 根本原因分析

系统处理时间较长

---

## 已存在的数据批量从标准存储或低频存储转换到智能分层存储

**分类**：对象存储｜工具使用

### 问题描述

申请试用智能分层工具

### 客服解答

1. 稍等

2. 您好，1.存量文件调用接口修改：https://developer.qiniu.com/kodo/3710/chtype2.使用生命周期将已存在的数据批量从标准存储或低频存储转换到智能分层存储，该能力处于测试阶段，需要您提供『空间名称』以及「到期日期」，在此日期之前创建的文件将自动转为智能分层存储

3. 好的，这边处理完成了同步您

4. 不客气的，完成后同步您

5. 您是指最新文件的上传时间吗

6. 您可以开启事件通知，有上传行为会回调通知给您，您那边可以记录下https://developer.qiniu.com/kodo/8541/set-the-event-notification智能分层存储包含智能分层存储容量费用和智能分层对象监控费用。其中：智能分层存储容量费用会根据所处的存储层收取不同的存储费用，具体定价请参见 产品定价智能分层对象监控费用按存储的文件数来计算，小于 64KB 的文件不收取，具体定价请参见 产品定价上传和下载文件过程中还会产生请求费用和流量费用，这些费用计算示例请参见 计费案例

7. 您好，没有相关的示例。处理逻辑：这块需要多个接口配合调用首先是列举，列举出空间文件（会包含文件时间），筛选出您需要的时间段的文件列表https://developer.qiniu.com/kodo/1284/list然后是批量操作，修改存储类型的：https://developer.qiniu.com/kodo/1250/batchhttps://developer.qiniu.com/kodo/3710/chtype

8. 好的

9. 可以的qshell工具：https://developer.qiniu.com/kodo/1302/qshell#9batchexpire命令：https://[REDACTED_DOMAIN]/qiniu/qshell/blob/master/docs/batchchtype.md

10. 可以的 用listbucket2命令：https://[REDACTED_DOMAIN]/qiniu/qshell/blob/master/docs/listbucket2.md﻿[图片]

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 域名创建数量已达每日上限

**分类**：CDN｜配置问题

### 问题描述

域名创建数量已达每日上限。能否调高每日上线，或临时调高我先配置上。谢谢！

### 客服解答

您好，这个是单日只能创建20个，触发上限后24h内无法继续创建，这个您要明天这个时间才可以上线域名的

### 根本原因分析

配置相关问题

---

## 照片检索

**分类**：智能多媒体｜其他类咨询

### 问题描述

我有个业务需求：一个马拉松活动赛事，拍了很多照片，上传至七牛云；参赛用户通过小程序，将自己的头像上传至云端，将包含用户的照片检索出来，给用户返回这些照片这个功能需求，能通过七牛云的api实现么？谢谢

### 客服解答

1. 稍等

2. 您好，没有直接的功能支持。提供了人脸检测接口，您可以使用测试下是否满足您的需求：https://developer.qiniu.com/dora/6817/facedetect

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 无法通过maven导入依赖包

**分类**：对象存储｜其他类咨询

### 问题描述

找不到依赖项 'com.qiniu:qiniu-java-sdk:7.16.0'

### 客服解答

您好可以手动下载一下 参考 https://developer.qiniu.com/kodo/1239/java

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 可用额度退费

**分类**：对象存储｜其他类咨询

### 问题描述

因公司停业时间久，盖系统目前用不上，现申请七牛云里面的可用额度退费，麻烦问一下退费流程

### 客服解答

您好，目前已支持，自助申请原路提现(支付宝，微信，网上银行)，线下提现(银行卡)功能。提现入口链接：https://portal.qiniu.com/financial/withdraw提现注意事项：1、申请提现前，需将该笔提现充值对应的增值税发票退回至七牛云。发票退票流程2、原路提现预计需3～5个工作日，线下提现预计需要5~15个工作日，七牛打款后具体到账时间以银行为准。3、可提现金额需要扣除实时消费金额、欠票金额、赠送金额和未支付金额。提现说明4、支持未认证用户申请原路提现，不支持申请线下提现5、原路提现充值：微信充值（充值时间小于 330 天）、支付宝充值（充值时间小于 330 天）、网上银行充值（充值时间小于 80 天）

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## KODO所绑域名证书过期，应该如何更新

**分类**：对象存储｜其他类咨询

### 问题描述

通过自定义域名访问KODO内容时显示https的证书过期，导致通过浏览器无法正常访问存储内容，应该如何更新域名证书

### 客服解答

您好，可以手动申请手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide4.升级HTTPS配置https://developer.qiniu.com/fusion/manual/4952/https-configuration注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

### 根本原因分析

SSL证书即将过期需要更换

---

## 开票金额问题

**分类**：账户与财务｜发票问题

### 问题描述

未达到1000的订单如何开票？

### 客服解答

1. 您好，超出6个月充值金额，或低于1000元金额的发票，您无法自行申请，不清楚金额的话可以在开票金额栏填写全部金额还请您在控制台提前申请准备好对应的发票抬头信息，添加对应的专票抬头信息审核通过后，如果您已经有了专票的抬头信息，可以不用再次添加，另外，给您开的发票默认是数电发票，需要纸质发票可以说明需求，提供收件地址。根据《增值税专用发票使用规定》申请专票必须要和实名认证公司名保持一致。-------------开票信息-----------开票金额:发票抬头: 发票类型: 纳税人识别号: 开户银行名称: 开户账号: 公司名称: 公司地址: 联系电话:

2. 您好，这边商务经理反馈为您处理，您这边还请耐心等待一下发票开具完成后即可，这边审核通过后即可为您成功开具的，您这边后续可在控制台发票管理下确认发票任务，开具完成后可在发票管理处进行下载，控制台-右上角-费用-发票与合同-发票管理发票管理：https://portal.qiniu.com/financial/invoice-contract/invoice

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 提前开票申请

**分类**：账户与财务｜发票问题

### 问题描述

您好，我这边需要申请提前开票 2000 元，开票后一周内付款，需要商务人员跟我对接，谢谢，因账户即将欠费，还请尽快与我联系。

### 客服解答

1. 您好，麻烦辛苦您这边给一下您的联系方式，这边反馈一下商务经理

2. 您好，那是您接收通知的，我们获取不到的，这边帮您反馈一下

3. 您这边耐心等待一下商务经理稍后会与您联系确认一下的

4. 嗯嗯不客气的

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 空间如果选北美，上传文件的接口域名是什么？

**分类**：对象存储｜上传下载

### 问题描述

空间如果选北美，上传文件的接口域名是什么？

### 客服解答

您好，对应的上传域名是http(s)://up-na0.qiniup.com

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 任务触发器视频编码一直提示规则策略不能为空，

**分类**：对象存储｜上传下载

### 问题描述

作业配置是不是可有可无的

### 客服解答

1. 您好，完整的配置截图看下

2. 您好，这里取消重新选择看下是否可以提交？[图片]

3. 您好，很抱歉不行的，您这边是需要保持文件的原名吗，如果是的话，可以切换下自定义文件名称，设置这个参数{{.key}}

4. 您好，具体是什么解码？

5. 您好，因为原视频分辨率和转码后的分辨率比例不一样，如果需要对应的分辨率建议您这边自己调整下

6. 您好，您的视频原链接提供下，这边看下

### 根本原因分析

配置相关问题

---

## 前端上传url地址

**分类**：对象存储｜上传下载

### 问题描述

请问一下，我的这个空间应该使用哪个上传域名了？我使用https://[REDACTED_DOMAIN]这个地址好像不对

### 客服解答

1. 您好，这个是 东南亚存储的上传域名，没有问题的，您这个上传是有什么报错么

2. 您好，可以的，这个是覆盖上传的token，上传文件 404.png 专用的token

3. 您好，这个是你们设置了 mimeLimit ，把这个去除即可

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## https://[REDACTED_DOMAIN]/17293286823350.mp4

**分类**：对象存储｜上传下载

### 问题描述

这个视频上传IP 是啥，我们密钥已经更换过了，还是有其他的IP在上传内容

### 客服解答

1. 稍等

2. 这边查询下日志

3. [REDACTED_IP]

4. 建议可以开下事件通知：https://developer.qiniu.com/kodo/8541/set-the-event-notification上传行为会有信息回调

5. 您好，可以从以下两个角度处理1.上传需要您的后端生成上传凭证，后端可以禁止向非预期的客户端ip响应上传凭证2.指定上传策略 scope为 bucket:key 形式，只能指定的key上传。 insertOnly 属性值设为 1，不允许覆盖。https://developer.qiniu.com/kodo/1206/put-policy

6. 您好，上传凭证中上传策略可以限制[图片]

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 充值错误，充错账号

**分类**：账户与财务｜账户问题

### 问题描述

金额充值错误了，把余额150.35转入正常使用账号，慕创旅拍[REDACTED_PHONE]，[REDACTED_EMAIL]。需要转入这个账号

### 客服解答

您好，不同账号之间，充值金额进行转移的话，需要进行余额转移申请，请提供以下信息，随后商务即为您处理转移余额麻烦您分别在转出和转入两个账号下提交工单回复提供以下信息转出账号：转入账号：转移金额：转移原因：如果您是企业认证，您还需要填写完成此表单【余额转移申请.docx 】，邮寄到以下地址（快递寄出后，麻烦工单提供下快递单号，以便及时为您跟进处理）收件人：王俊瑛电话：[REDACTED_PHONE]地址：上海市浦东新区张江高科技园区亮秀路81号浦东软件园Q座 (南门)

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 如果将归档存储批量改为归档存储直读

**分类**：对象存储｜上传下载

### 问题描述

如果将归档存储批量改为归档存储直读

### 客服解答

1. 您好，您这边可以使用qhsell工具进行批量转存储类型的qshell工具：https://developer.qiniu.com/kodo/1302/qshell#9batchexpire命令：https://[REDACTED_DOMAIN]/qiniu/qshell/blob/master/docs/batchchtype.md

2. 上述方法就是批量转换的处理方式

3. 可以用 https://developer.qiniu.com/kodo/1284/list 这个接口列举出对应的存储类型文件

4. 先列举 再转换处理方式：可以使用接口或者用qshell命令行工具qshell工具：https://developer.qiniu.com/kodo/1302/qshell#9batchexpire命令：https://[REDACTED_DOMAIN]/qiniu/qshell/blob/master/docs/batchchtype.md

5. 归档文件需要解冻A、单个归档文件解冻，有以下几种方法1.portal上空间管理中，进行解冻2.调用单文件 归档解冻接口：https://developer.qiniu.com/kodo/api/6380/restore-archive3.图形化工具 Kodo Browser方法解冻：https://[REDACTED_DOMAIN]/solutions?ref=developer.qiniu.com4.qsuits工具方法：https://[REDACTED_DOMAIN]/NigelWu95/qiniu-suits-java/blob/master/docs/restorear.mdB、如需进行批量解冻，您可以调用批量解冻接口实现：https://developer.qiniu.com/kodo/api/1250/batch

6. 批量解冻目前需要调接口实现

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 删除域名证书错误

**分类**：对象存储｜其他类咨询

### 问题描述

[    [        {            "title": "请求 ID",            "content": "AFj-oOEkOX7baAAY, AFj-oOEkOX7baAAY, AFj-oOEkOX7baAAY, AFj-oOEkOX7baAAY"        },        {            "title": "日志栈",            "content": "fusiondomain_cud/400;APIS:75/400;PORTAL-PROXY:127/400"        }    ]]

### 客服解答

1. 您好，请稍等，这边帮您确认下

2. 您好，久等了，已处理完成

### 根本原因分析

系统处理时间较长

---

## 隐私合规问题

**分类**：对象存储｜SDK使用

### 问题描述

我们在APP上传应用商城，遇到驳回问题，主要如下：
APP未经用户同意，SDK在静默状态下或在后台运行时，（HappyDNS，GdtAd）SDK仍收集用户个人信息((SDK: 七牛云存储) 读取设备IP)。麻烦帮我们看看，谢谢。
堆栈信息如下：at java.net.NetworkInterface.getInetAddresses()	at com.qiniu.android.utils.AndroidNetwork.getHostIP(AndroidNetwork.java:62)	at com.qiniu.android.http.dns.DnsPrefetcher.prepareToPreFetch(DnsPrefetcher.java:140)	at com.qiniu.android.http.dns.DnsPrefetcher.[REDACTED_KEY](DnsPrefetcher.java:121)	at com.qiniu.android.http.dns.[REDACTED_KEY]$3.run([REDACTED_KEY].java:69)	at com.qiniu.android.transaction.TransactionManager$Transaction.handleAction(TransactionManager.java:190)	at com.qiniu.android.transaction.TransactionManager$Transaction.access$200(TransactionManager.java:130)	at com.qiniu.android.transaction.TransactionManager.handleTransaction(TransactionManager.java:101)	at com.qiniu.android.transaction.TransactionManager.[REDACTED_KEY](TransactionManager.java:93)	at com.qiniu.android.transaction.TransactionManager.timerAction(TransactionManager.java:125)	at com.qiniu.android.transaction.TransactionManager.access$300(TransactionManager.java:12)	at com.qiniu.android.transaction.TransactionManager$1.run(TransactionManager.java:113)	at java.util.TimerThread.mainLoop(Timer.java:555)	at java.util.TimerThread.run(Timer.java:505)

### 客服解答

1. 稍等

2. 您好，关闭dns预解析就不会在后台读取ip了GlobalConfiguration.getInstance().isDnsOpen = false 关闭 DNS 预解析。

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 下载报 http statuscode 597

**分类**：对象存储｜上传下载

### 问题描述

下载文件过程中报http status code 597

### 客服解答

1. 您好，您方便将 597的链接提供下么，这边帮您确认核实下

2. 请稍等

3. 您好，597的问题这边还在帮您核实中，有结论后这边再给您反馈

4. 您好，这边看属于内部报错的，这个目前已经处理了，您这边后续可以再观察看下

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 为什么某些资源调用截图接口一直都是失败

**分类**：智能多媒体｜音视频处理

### 问题描述

截图一直提示这个无法截图！

### 客服解答

1. 稍等

2. 您好，w修改成整数再试下呢vframe/jpg/offset/0.5/w/722/h/1280

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 域名验证总是失败

**分类**：CDN｜配置问题

### 问题描述

域名验证总是提示失败。不知道是不是设置不对。

### 客服解答

1. 您好主机记录不对 应该是verification[图片]

2. 好的

### 根本原因分析

域名所有权验证未通过

---

## 证书验证类型：DNS(CNAME 记录)

**分类**：CDN｜证书问题

### 问题描述

订单：6708e6efce27951dbff8d4bf，能否修改为文件认证，DNS提示不合法

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 账号注销

**分类**：账户与财务｜账户问题

### 问题描述

注销账号

### 客服解答

1. 您好，目前注销可以在控制台操作https://portal.qiniu.com/developer/user/security目前用户自助注销需满足以下所有条件：1、账号为普通账号（非财务父子账号、OEM账号）2、账号下实时消费无产品用量、无消费金额（数据需要您自己删除）对象存储：https://portal.qiniu.com/kodo/bucketCDN：https://portal.qiniu.com/cdn/domain3、账号下无各种欠费实时消费明细（查看您当月消费）https://portal.qiniu.com/financial/bills/estimated-consume如有欠费，将在下月5号出账、8号扣款，结算后，您再提交账号注销。4、账号下没有正在处理的提现审批https://portal.qiniu.com/financial/withdraw5、账号当前没有被冻结注意：账号注销后，账号无法找回

2. 存储空间还有文件 麻烦删除一下您可以通过qshell批量删除，三条命令就可以了。1.先下载qshell工具并使用qshell account 命令登陆账户。下载及安装文档 https://developer.qiniu.com/kodo/tools/1302/qshellwindows环境下安装qshell教程 https://developer.qiniu.com/kodo/kb/5545/windows-environment-installation-qshell-tutorial2.使用listbucket2命令列举出空间内所有资源例如 qshell listbucket2 空间名 -o result.txt命令文档 https://[REDACTED_DOMAIN]/qiniu/qshell/blob/master/docs/listbucket2.md3.使用batchdelete命令批量删除第2步列举出的列表文件。例如 qshell batchdelete --force 空间名 -i result.txt命令文档 https://[REDACTED_DOMAIN]/qiniu/qshell/blob/master/docs/batchdelete.md注意：主动删除资源不可以恢复，请慎重

3. 您好如果您不再使用，需要您将账号下对应存储资源删除，并将空间绑定域名也删除下批量删除有以下几种方法：1.使用图形化工具 图形化工具 Kodo Browser 勾选您需要删除的文件或前缀目录一键删除kodo browser 参考文档：https://developer.qiniu.com/kodo/tools/5972/kodo-browser2.使用工具qshell ，参考文档https://developer.qiniu.com/kodo/tools/1302/qshellhttps://[REDACTED_DOMAIN]/qiniu/qshell/blob/master/docs/batchdelete.md3.用代码删除，把所以资源list出来，用个循环全部删除，可参考：https://developer.qiniu.com/kodo/api/1284/listhttps://developer.qiniu.com/kodo/api/1257/delete注意：用户主动删除资源不可以恢复，请慎重空间域名删除在域名管理界面操作解绑：https://developer.qiniu.com/kodo/8527/kodo-domain-name-management

4. 您好，已为您申请注销当前账号，注销流程会需要些时间，待注销完成将会邮件通知您，请知悉，

5. 您好抱歉久等了，经确认该账号目前还有欠费，无法注销账号，需要您将欠费补齐后，才可以为您继续走注销流程

6. 您好，已为您申请注销当前账号，注销流程会需要些时间，待注销完成将会邮件通知您，请知悉，

### 根本原因分析

系统处理时间较长

---

## 命令报错

**分类**：对象存储｜工具使用

### 问题描述

为什么不能执行成功

### 客服解答

您好，您稍等这边确认一下

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 多媒体样式添加视频样式后，通过样式链接无法直接访问视频

**分类**：对象存储｜其他类咨询

### 问题描述

我新增了一个视频样式处理接口为：avcvt/3/format/m3u8/segtime/10/r/30/vb/2500k/vcodec/libx264/acodec/libfdk_aac；但是保存后无法通过样式链接直接访问，通过浏览器访问直接就下载了一个m3u8后缀的文件我的原始链接为：https://[REDACTED_DOMAIN]/file_name_58ea6c861d7d3146db1b6cd15b19d63b255c.mp4样式链接是：https://[REDACTED_DOMAIN]/file_name_58ea6c861d7d3146db1b6cd15b19d63b255c.mp4-video1.m3u8

### 客服解答

1. 您好，因为正常浏览器是不支持直接播放m3u8文件的，您需要使用播放器或者相关插件才能播放的

2. 您好，您这边原视频的分辨率应该是就是这个的吧，这边查看的您的原视频的编码的[图片]

3. 您好，这边看下来应该是原视频的编码有问题的，您这边可以看下原视频的元信息参数的，访问下面的即可，看下w和h的，我们这边是根据视频的元信息来处理的，您这边可以上传一个其他视频再测试看下的https://[REDACTED_DOMAIN]/file_name_58ea6c861d7d3146db1b6cd15b19d63b255c.mp4?avinfo

4. 您好，嗯嗯不客气的

5. 您好，实时转码的话目前有相关限制的，建议您这边走下普通转码操作的不支持av1编码格式的视频输入不支持H.265 HDR 编码的视频输入输入封装格式暂时仅支持 mp4、mov，输出封装格式暂时仅支持 m3u8输出分辨率不超过2K（2560×1440）不支持管道命令目前仅限国内华东-浙江、华南-广东、华北-河北区域使用控制台：https://developer.qiniu.com/dora/6488/task-01新建任务，然后选择对应空间然后选择对应对象文件，然后点击➕号选择普通转码，然后点击普通转码再点击自定义预设然后封装格式MP4、编码格式H.264即可点击确认，设置完成后点击➕号选择输出，然后点击输出选择保存的空间然后保存的文件名后点击确认，最后点击下方保存即可开始任务[图片][图片][图片][图片][图片]

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 对象云储存域名一直在配置中

**分类**：对象存储｜其他类咨询

### 问题描述

对象云储存域名一直在配置中

### 客服解答

1. 您好，这边手动介入下处理，麻烦稍等。

2. 您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

系统处理时间较长

---

## qiniu.aipupower.cn这个申请ssl怎么会提示配置cname,cname都配置好了

**分类**：对象存储｜其他类咨询

### 问题描述

qiniu.aipupower.cn这个申请ssl怎么会提示配置cname,cname都配置好了

### 客服解答

您好，不需要进行cname解析修改，您需要进行下文件验证https://[REDACTED_DOMAIN]/.well-known/pki-validation/EFFFA12B717AD28D643286B1B9544C88.txt

### 根本原因分析

配置相关问题

---

## 为什么开不了发票？

**分类**：CDN｜其他类咨询

### 问题描述

去年充值50，用完了也开不了发票，发票记录也都是空的

### 客服解答

1. 您好，超出6个月充值金额，或低于1000元金额的发票，您无法自行申请，不清楚金额的话可以在开票金额栏填写全部金额还请您在控制台提前申请准备好对应的发票抬头信息，添加对应的专票抬头信息审核通过后，如果您已经有了专票的抬头信息，可以不用再次添加，另外，给您开的发票默认是数电发票，需要纸质发票可以说明需求，提供收件地址。根据《增值税专用发票使用规定》申请专票必须要和实名认证公司名保持一致。-------------开票信息-----------开票金额:发票抬头: 发票类型: 纳税人识别号: 开户银行名称: 开户账号: 公司名称: 公司地址: 联系电话:

2. 好的

3. 您好，发票预计需要1-2日帮您完成开具，您到时候去发票列表查看即可

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 长时间删除不掉

**分类**：CDN｜配置问题

### 问题描述

如题

### 客服解答

1. 稍等

2. 已删除完成了哈

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 免费 from 自动催单

**分类**：CDN｜证书问题

### 问题描述

长时间处于域名发布环节

### 客服解答

1. 您好，这边手动介入下处理，麻烦稍等。

2. 您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

系统处理时间较长

---

## cdn的缓存默认时间是多少，怎么修改

**分类**：CDN｜其他类咨询

### 问题描述

cdn的缓存默认时间是多少，在哪里能修改cdn的缓存时间

### 客服解答

1. 您好默认缓存时间是1个月，可以到图示这个地方修改[图片]

2. 不影响

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

## 证书申请长时间未配置完成

**分类**：CDN｜证书问题

### 问题描述

证书申请长时间未配置完成，我看提示信息说一般15分钟，我等了有1个小时了。

### 客服解答

1. 您好，请稍等，这边帮您确认下

2. 你好，久等了，已处理完成，您确认下呢

3. 您好，您不用谢的

### 根本原因分析

系统处理时间较长

---

## 域名防盗链配置处理时间长

**分类**：CDN｜配置问题

### 问题描述

您好，我修改了防盗链配置，已经过去 1 小时了还没好，能否帮忙通过防盗链修改，谢谢！

### 客服解答

稍等

### 根本原因分析

配置相关问题

---

## 免费 from 自动催单

**分类**：CDN｜证书问题

### 问题描述

长时间处于域名发布环节

### 客服解答

1. 您好，请稍等

2. 您好，久等了，已处理完成

3. 您好，您使用的是一键升级 https，该操作需要七牛帮您申请一个免费的 ssl 证书， 当前证书正在等待CA机构颁发，期间您不要操作 ssl 证书服务，一般会在 2 小时左右处理升级完成，请耐心等待。

### 根本原因分析

系统处理时间较长

---

## 域名升级 HTTPS 处理中，一直卡在这个状态很久了

**分类**：CDN｜配置问题

### 问题描述

域名升级 HTTPS 处理中，一直卡在这个状态很久了

### 客服解答

1. 稍等

2. 机器正在部署中的，完成了这边同步哈

3. 您好，久等了，配置已下发

### 根本原因分析

系统处理时间较长

---

## 开启了图片压缩，但是查看上传的库中的图片，体积并没有压缩

**分类**：对象存储｜上传下载

### 问题描述

开启了图片压缩，但是查看上传的库中的图片，体积并没有压缩

### 客服解答

1. 您好压缩是在访问时压缩处理的

2. 给下您的图片链接 这边看下

3. 图片自动瘦身价格参考https://[REDACTED_DOMAIN]/prices?source=dora ：0.1 元/千次。用户访问您存储在七牛云中的文件时，如果 CDN 节点上有缓存的时候不会重复触发瘦身，无缓存回源触发瘦身时计算次数，触发1次计算1次。

4. 您的空间是私有的 私有bucket 不支持 CDN中间源的图片瘦身处理

5. 空间属性调整为公开再访问 私有空间不支持

6. 您开启的是图片瘦身功能，私有bucket 不支持 CDN中间源的图片瘦身处理。https://developer.qiniu.com/dora/kb/4077/image-thin-body-is-invalid

### 根本原因分析

其他技术问题，需要根据具体情况分析

---

