# 七牛云客服问答数据 - Part 31

本文档包含经过结构化处理的客服问答记录，共 114 条。

**数据处理说明**:
- 已对敏感信息进行脱敏处理（邮箱、电话、IP、密钥等）
- 每条记录包含问题分类、详细描述、客服解答和根因分析
- 数据来源: 七牛云客服工单系统

---

## 问题 1: 较长时间未配置完成

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
较长时间未配置完成

### 客服解答内容
**客户**：较长时间未配置完成

**客服**：您好这边帮你手动介入处理下，请稍等

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 2: 如何模拟上传文件失败的场景

**分类标签**: 对象存储｜上传下载

### 详细问题描述
需求：现在我们想测试一下线上用户在某种情况下上传文件失败的场景，想测试一下设置超时时间多少最合适

### 客服解答内容
**客户**：需求：现在我们想测试一下线上用户在某种情况下上传文件失败的场景，想测试一下设置超时时间多少最合适

**客服**：您好，这个你们简单的方式，可以上传大文件的时候，将网络断开试试即可

### 根本原因分析
上传超时时间设置过短或网络环境不稳定

---

## 问题 3: 公开空间为什么 error :  "referer forbidden"

**分类标签**: 对象存储｜上传下载

### 详细问题描述
http://img2.kwonglong.cn/cmsVideo.mp4

### 客服解答内容
**客户**：http://img2.kwonglong.cn/cmsVideo.mp4

**客服**：您好，可以检查下空间设置中的referer防盗链，调整或关闭

**客户**：之前就关了但是没有效果

**客户**：没有用的样子

**客服**：点这个，关闭后保存[图片]

**客户**：果然有效

**客户**：好像刷新又不行了呜呜

**客户**：有效了，谢谢

**客服**：不客气的，还有其他问题吗

**客户**：没有我关闭它

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 4: cdn回源鉴权设置保存一直处理中

**分类标签**: CDN｜配置问题

### 详细问题描述
cdn回源鉴权设置保存一直处理中，保存的配置好像不生效，麻烦处理下

### 客服解答内容
**客户**：cdn回源鉴权设置保存一直处理中，保存的配置好像不生效，麻烦处理下

**客服**：您好，请稍等，这边帮您确认下

**客服**：您好，久等，已处理完成

**客户**：还是未生效啊，都好几个小时过去了，你们今天的配置都不起作用啊[图片]

**客服**：请稍等

**客服**：您好，久等了，已处理完成

### 根本原因分析
系统配置任务处于处理队列中，需要手动介入加速处理流程

---

## 问题 5: 域名删除处理中

**分类标签**: CDN｜配置问题

### 详细问题描述
域名删除处理中

### 客服解答内容
**客户**：域名删除处理中

**客服**：稍等

**客服**：您好，已删除完成了

### 根本原因分析
系统配置任务处于处理队列中，需要手动介入加速处理流程

---

## 问题 6: 收费不合理，被刷量冻结后还在计费

**分类标签**: 账户与财务｜计费问题

### 详细问题描述
本身就是被刷故意刷量导致大量消耗流量，账户都冻结了，无法访问，但是冻结了还在计费。不合理，要求解冻把扣费金额消了

### 客服解答内容
**客户**：本身就是被刷故意刷量导致大量消耗流量，账户都冻结了，无法访问，但是冻结了还在计费。不合理，要求解冻把扣费金额消了

**客服**：您好，这边核实下，请稍等

**客服**：查询您这边主要是1-20号产生的cdn访问计费[图片]建议及时充值解冻您的账号自冻结之日起的第 31 个自然日，如现金账户仍然欠费，视作您默认放弃数据，七牛云存储将删除账户中的数据，并且不可恢复。在冻结帐号期间，因保存数据而使用的存储功能仍将计算费用，每逢扣费日相应的存储费用会被扣除。相关文档：付款和账单：https://portal.qiniu.com/financial/summary消费，欠费，余额情况：https://portal.qiniu.com/financial/overview欠费须知：https://developer.qiniu.com/af/kb/1543/lack-of-information

### 根本原因分析
计费规则理解偏差或资源使用量超出预期

---

## 问题 7: 申请了越南的储存空间，但一直无法开通

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
因为网站取消备案的缘故，继续使用海外空间，请帮忙开通一样

### 客服解答内容
**客户**：因为网站取消备案的缘故，继续使用海外空间，请帮忙开通一样

**客服**：您好，您这边辛苦留一下您的联系方式，这边反馈商务经理为您确认一下的

**客户**：[REDACTED_PHONE]另外，请问一下，http(s)://pincman.s3.cn-east-1.qiniucs.com，这个自动生成的二级域名也没有访问权限是什么原因<Error><Code>NotSupportAnonymous</Code><Message>request must have signature info</Message><Resource>/media[REDACTED_ID_CARD_15].png</Resource><RequestId>f0YAAAC2vI_frwAY</RequestId></Error>

**客服**：您好，这个S3域名的，空间的S3域名的作用通常是用于接口等的，而且s3域名是需要进行鉴权后使用的，无法直接访问资源的

**客户**：那麻烦帮我开通一个越南空间吧，我域名没备案啊

**客服**：您好，您创建北美-新加坡也是可以的，CDN域名覆盖选择海外覆盖即可的

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 8: 上传错误

**分类标签**: 对象存储｜上传下载

### 详细问题描述
不知道为啥cd-wb 空间中多了那么多文件

### 客服解答内容
**客户**：不知道为啥cd-wb 空间中多了那么多文件

**客服**：您好后台看您在2024-10-21上传了222635个文件

**客户**：并不是我自己上传的

**客户**：我上传的是thylove-video这个空间

**客服**：这边过滤下上传日志 请稍等

**客服**：日志记录上传的ua来自于（Golang qiniu/client package）上传IP是115.231.29.98  [REDACTED_IP]  [REDACTED_IP]

**客户**：这个并不是我上传的，能查到上传的AccessKey吗

**客服**：密钥就是您当前账号下的密钥 可以到https://portal.qiniu.com/developer/user/key查看如果密钥有在其他地方使用过 安全起见 建议周期性更改密钥使用

**客户**：我当前账下两个密钥有两个，我想知道是哪一个，

**客服**：ak是 D9SUhwIKiZj0YmcoSIWTFPgm92tlChSrsblVYkNz

**客户**：我刚才看了一下，是因为开了一个增量审核，把我上传到thylove-video空间的视频每一帧都截成图片检测并存到cd-wb空间中，导致我上传的视频都审核成广告了，还产生七百多的费用，我不愿承担这个费用。

**客服**：增量审核视频时每秒都会截帧存储  截帧落存储的空间也是根据您的配置来处理的 这个属于正常业务处理范畴

### 根本原因分析
上传接口配置、权限或网络问题

---

## 问题 9: 需要证书解析麻烦提供谢谢

**分类标签**: CDN｜证书问题

### 详细问题描述
需要证书解析麻烦提供谢谢

### 客服解答内容
**客户**：需要证书解析麻烦提供谢谢

**客服**：主机记录：_D788E2A043AE504A4FB13148F657BDF0.qiniu记录类型：cname记录值：057D270C952A61169818717C9335F058.8C5191CAB60B7ECD22030652A487E43E.cmcdt3tedyer8l.trust-provider.com

### 根本原因分析
SSL证书申请、验证或部署流程问题

---

## 问题 10: cdn回源鉴权设置保存一直处理中

**分类标签**: CDN｜配置问题

### 详细问题描述
cdn回源鉴权设置保存一直处理中，而且上个工单处理了 但是回源鉴权不起作用，我请求我设置的服务器地址

### 客服解答内容
**客户**：cdn回源鉴权设置保存一直处理中，而且上个工单处理了 但是回源鉴权不起作用，我请求我设置的服务器地址

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

**客户**：昨天配置了referer一天时间过去了还是不生效，你们最近的系统是不是有啥问题；防盗链回源鉴权配置了几天了没有效果 改为最简单的referer也没有效果[图片]

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析
系统配置任务处于处理队列中，需要手动介入加速处理流程

---

## 问题 11: 上传失败，返回的401上传凭证无效

**分类标签**: 对象存储｜上传下载

### 详细问题描述
上传失败，返回的401上传凭证无效：返回：error: "bad token"
error_code: "BadToken"golang申请uptoken的代码：func (m *StorageController) Qiniu(c *gin.Context) {    /* 获取当前用户 */    var currentUser *model.User = nil    currentUser = service.User.GetCurrentUser(c)    if currentUser == nil {       common.Log.Info("GetCurrentUser error, error: [currentUser is nil]")       tools.ErrorResponse(c, status_code.SYSTEM_ERROR)       return    }    accessKey := config.Conf.Storage.QiniuAccessKey    secretKey := config.Conf.Storage.QiniuAccessKey    mac := credentials.NewCredentials(accessKey, secretKey)    bucket := config.Conf.Storage.QiniuBucket    putPolicy, err := uptoken.NewPutPolicy(bucket, time.Now().Add(1*time.Hour))    if err != nil {       common.Log.Info("uptoken.NewPutPolicy, error: [" + err.Error() + "]")       tools.ErrorResponse(c, status_code.SYSTEM_ERROR)       return    }    upToken, err := uptoken.NewSigner(putPolicy, mac).GetUpToken(context.Background())    if err != nil {       common.Log.Info("uptoken.NewSigner, error: [" + err.Error() + "]")       tools.ErrorResponse(c, status_code.SYSTEM_ERROR)       return    }    random := tools.CreateId()[0:10] + strconv.FormatInt(time.Now().Unix(), 10)    fileName := fmt.Sprintf("user/%d/%s.jpg", currentUser.ID, random)    rsp := response.StorageQiniuRsp{       AccessKey: accessKey,       Token:     upToken,       FileName:  fileName,       URL:       config.Conf.Storage.QniuDomain + "/" + fileName,    }    tools.SuccessResponse(c, rsp)}uniapp代码：

### 客服解答内容
**客户**：上传失败，返回的401上传凭证无效：[图片]返回：error: "bad token"
error_code: "BadToken"golang申请uptoken的代码：func (m *StorageController) Qiniu(c *gin.Context) {    /* 获取当前用户 */    var currentUser *model.User = nil    currentUser = service.User.GetCurrentUser(c)    if currentUser == nil {       common.Log.Info("GetCurrentUser error, error: [currentUser is nil]")       tools.ErrorResponse(c, status_code.SYSTEM_ERROR)       return    }    accessKey := config.Conf.Storage.QiniuAccessKey    secretKey := config.Conf.Storage.QiniuAccessKey    mac := credentials.NewCredentials(accessKey, secretKey)    bucket := config.Conf.Storage.QiniuBucket    putPolicy, err := uptoken.NewPutPolicy(bucket, time.Now().Add(1*time.Hour))    if err != nil {       common.Log.Info("uptoken.NewPutPolicy, error: [" + err.Error() + "]")       tools.ErrorResponse(c, status_code.SYSTEM_ERROR)       return    }    upToken, err := uptoken.NewSigner(putPolicy, mac).GetUpToken(context.Background())    if err != nil {       common.Log.Info("uptoken.NewSigner, error: [" + err.Error() + "]")       tools.ErrorResponse(c, status_code.SYSTEM_ERROR)       return    }    random := tools.CreateId()[0:10] + strconv.FormatInt(time.Now().Unix(), 10)    fileName := fmt.Sprintf("user/%d/%s.jpg", currentUser.ID, random)    rsp := response.StorageQiniuRsp{       AccessKey: accessKey,       Token:     upToken,       FileName:  fileName,       URL:       config.Conf.Storage.QniuDomain + "/" + fileName,    }    tools.SuccessResponse(c, rsp)}uniapp代码：[图片]

**客服**：您好，你是直接复制的，如果是的话，那个token中间有一个空格您确定下[图片]

**客户**：实际是没有空格，可以看看请求的截图，这里是我粘贴的时候带的。

**客服**：您好，这边不对，这个过期时间正常是10位的[图片]

**客服**：您好，在 gopath 的src目录下安装go-sdkgo get u github.com/qiniu/api.v7 进入 src 目录，创建 go 文件调用 putPolicy.UploadToken(mac) 生成token https://github.com/qiniu/api.v7/blob/master/examples/create_uptoken.go

**客户**：我上面贴了golang代码，而且就是用你们官网的代码直接粘贴的，我实现有什么问题。

**客户**：accessKey := config.Conf.Storage.QiniuAccessKey    secretKey := config.Conf.Storage.QiniuAccessKey    mac := credentials.NewCredentials(accessKey, secretKey)    bucket := config.Conf.Storage.QiniuBucket    putPolicy, err := uptoken.NewPutPolicy(bucket, time.Now().Add(1*time.Hour))    if err != nil {       common.Log.Info("uptoken.NewPutPolicy, error: [" + err.Error() + "]")       tools.ErrorResponse(c, status_code.SYSTEM_ERROR)       return    }    upToken, err := uptoken.NewSigner(putPolicy, mac).GetUpToken(context.Background())    if err != nil {       common.Log.Info("uptoken.NewSigner, error: [" + err.Error() + "]")       tools.ErrorResponse(c, status_code.SYSTEM_ERROR)       return    }

**客户**：我这样实现有什么问题吗，你直接看看我的token有没有异常，而不是告知我要切换代码，我觉得这里可能是token验证异常导致的，可能是区域问题之类，好好查一下。

**客服**：您好，您查看下上面的回复，您的token时间有问题，正常是10位的[图片]

**客户**：我的代码就是拷贝你们官网的，是这里实现有问题？[图片]

**客户**：我的代码：accessKey := config.Conf.Storage.QiniuAccessKey    secretKey := config.Conf.Storage.QiniuAccessKey    mac := credentials.NewCredentials(accessKey, secretKey)    bucket := config.Conf.Storage.QiniuBucket    putPolicy, err := uptoken.NewPutPolicy(bucket, time.Now().Add(1*time.Hour))    if err != nil {       common.Log.Info("uptoken.NewPutPolicy, error: [" + err.Error() + "]")       tools.ErrorResponse(c, status_code.SYSTEM_ERROR)       return    }    upToken, err := uptoken.NewSigner(putPolicy, mac).GetUpToken(context.Background())    if err != nil {       common.Log.Info("uptoken.NewSigner, error: [" + err.Error() + "]")       tools.ErrorResponse(c, status_code.SYSTEM_ERROR)       return    }

**客户**：你看看这个对不对：NVf7h95TyhWlvipyuwLQxpyplaecr78O80VjOEYQ:bNAA_gwdfZcuU6fm9m4M5juuzjY=:eyJkZWFkbGluZSI6MTcyOTU4Mjg1MCwic2NvcGUiOiJpdHV0b3Itc3RvcmUifQ==

**客户**：如果对的话，应该就是我设置问题。

**客服**：您好，这个是对的qshell b64decode eyJkZWFkbGluZSI6MTcyOTU4Mjg1MCwic2NvcGUiOiJpdHV0b3Itc3RvcmUifQ==
{"deadline":1729582850,"scope":"itutor-store"}
[图片]

**客户**：好的，我试试。

**客户**：上传的url，我应该用哪个合适。我的空间是新加坡的，但是开发测试在大陆（广东），实际APP上线是在香港澳门，我看文档里面没有url说明

**客服**：您好，就是up-as0.qiniup.com，是对的

**客户**：上传成功了，但是有个比较奇怪的地方，我绑定了域名，为啥用域名访问不到，但是用测试域名是成功的。

**客户**：但是我[图片]但是我访问在网站上上传图片却是可以

**客服**：您好，qiniu-store.suninttech.com看起来访问是正常的，无法访问是有什么报错吗

**客户**：没有报错，现在突然可以了，是不是分发到CDN耗时比较久。

**客服**：您好，是从国内访问的吗？看您的域名使用的是海外线路，国内访问的话可能会存在访问慢的问题的

**客户**：是的，走海外路线的，我的空间也是海外的。如果我用户是香港，走这个路线会有问题吗

**客户**：但是我走你们测试域名就很快，我感觉不是这个原因？

**客户**：这个要配置吗？[图片]

**客服**：您好，刚刚给您优化了下海外回源，您再访问看下

**客户**：如果我访问都是通过CDN，是不是可以不用设置原站域名。

**客服**：您好，是的，cdn域名和源站域名选一个就好

**客户**：源站域名一般什么时候会用到，就是CDN没访问到，就用源站做兜底的时候吗？

**客服**：您好，不需要使用cdn加速的时候可以使用源站域名

**客户**：如果我的空间是国内的，我的域名是不是一定是要备案才能用？

**客服**：您好，是的，国内线路必须使用备案域名

### 根本原因分析
上传凭证生成错误或已过期

---

## 问题 12: 更新了 SSL 证书，域名一直在处理中

**分类标签**: CDN｜配置问题

### 详细问题描述
t.trmk-cdn.teachingrecord.comtrmk-cdn.teachingrecord.comcdn.teacherrecord.com账户下这 3 个域名一直是处理中

### 客服解答内容
**客户**：t.trmk-cdn.teachingrecord.comtrmk-cdn.teachingrecord.comcdn.teacherrecord.com账户下这 3 个域名一直是处理中

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

**客户**：OK，可以了

### 根本原因分析
系统配置任务处于处理队列中，需要手动介入加速处理流程

---

## 问题 13: OSS的存量审核能否停止任务？

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
我刚刚启动了一个存量审核任务，然后发现购买的资源包不够用，现在请求停止

### 客服解答内容
**客户**：我刚刚启动了一个存量审核任务，然后发现购买的资源包不够用，现在请求停止

**客户**：[图片]麻烦处理一下

**客户**：我之前没看懂计费规则，以为10万的审核包够用了，能撤回这次存量审核任务吗？超预算了

**客服**：您好，稍等下，这边同步下，看下是否可以停止

**客服**：您好，很抱歉久等了，已经关闭了

**客户**：我看现在的检测量显示是5万，那实际上消耗的应该是50000*3=15万审核次数吗？

**客户**：我现在账户里有一个10万的资源包，是否有免费额度？我还需要再买一个资源包吗

**客服**：您好，请稍等，这边帮您确认下

**客服**：您好，内容审核没有免费额度的，您当前是买的 每个月 10w的资源包，使用的是 三鉴服务，检测量5.2 ，也就是消耗了 15.6万次审核次数您这个建议直接买个 16w的资源包，不需要买每个月10w的自动分配资源包，你们资源包买错了买错的资源包，这边可以帮您申请退款，您重新购买即可

**客户**：麻烦帮我申请下退款吧，有16w资源包的购买链接吗？

**客户**：[图片]我看购买页面只有10万和100万

**客服**：您好，抱歉，之前的资源包订单回复有问题，您现在买的是  1次分配的 10w 资源包，6个月内有效，资源包购买是正确的 ，当前帮您看了下，没有6w条的资源包
这个要再买个10w的资源包叠加抵扣，如果不买的话，走账号现金余额计费
0.085 * 530 + 0.085 * 530 + 0.075 * 530 = 129.85
再买个10w的资源包更划算些

**客服**：您好，抱歉，之前的资源包订单回复有问题，您现在买的是1次分配的 10w 资源包，6个月内有效，资源包购买是正确的 ，当前帮您看了下，没有5.6w条的资源包
如果不买资源包的话， 0.085 * 560   = 47.6 
大概还需要支付47.6左右，您看下是否需要再买个10w的资源包

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 14: 用户反馈图片资源加载速度慢

**分类标签**: CDN｜其他类咨询

### 详细问题描述
桶名称： vipdocimg

### 客服解答内容
**客户**：桶名称： vipdocimg

**客服**：您好，1、麻烦提供下用户的 ip、dns 信息，和cdn节点信息，这边代理测试下可以通过访问这个链接 http://ping.huatuo.qq.com/ 获取本地的 ip 和 dns 信息，在检测域名这边输入下cdn域名，点击提交检测，然后截图通过工单提交给我们[图片]2、建议让用户使用 chrome 浏览器，按照下述文档获取下 remote adress(对端节点ip)，request header(客户端请求头) 以及 response header(服务端响应头)信息，方便我们查询分析问题。https://developer.qiniu.com/fusion/kb/1478/how-to-access-network-in-the-browser-request-information

**客户**：这个[图片][图片]

**客服**：您好，建议提高下本地网络带宽或者切换其他网络试下，您网络延时比较高。

**客户**：通过媒体资源生成的m3u8有些播放器播放不了啊：https://vipimg.daliqx.com/vipdoc/vinBaoyang/%E5%A5%94%E9%A9%B0/%E4%B8%AD%E5%9B%BD/GLC%20260%204MATIC/2018/2.0T/9a9932718e4aa6fb87efe72af2bd2b38b978f19794b913d1242c643d3a4d927cfa02e8e1eee6191dbc3999e6e2ad249b/%E6%AD%A3%E6%97%B6%E7%BB%B4%E6%8A%A4/1[REDACTED_PHONE]54-prox.m3u8

**客户**：有些播放器能播放，有些播放器播放不了，ios端微信小程序就播放不了，

**客服**：稍等

**客服**：您好，这边测试从苹果微信打开这个链接可以播放的呢，您检查下您小程序播放器兼容性呢，能否支持hls的

**客户**：是小小程序的么？

**客服**：这边是直接微信中打开视频链接测试播放的

**客户**：我配置这个样式，最后添加/format/jpg后访问提示格式无效watermark/3/image/a29kbzovL3ZpcGRvY2ltZy9sb2dvLnBuZw/dissolve/20/gravity/Center/dx/20/dy/20/ws/0.2|watermark/4/text/5L-u6L2m5Yqp5omL/fontsize/800/fill/Z3JheQ==/dissolve/10/rotate/30/uw/180/uh/180/resize/1|watermark/4/format/jpg/text/5L-u6L2m5Yqp5omL/fontsize/200/fill/cmVk/dissolve/10/rotate/30/uw/180/uh/180/resize/1

**客服**：您好，稍等

**客服**：您这边可以这样使用，需要什么格式，后面单独加一下格式转换处理 imageView2/0/format/jpgwatermark/3/image/a29kbzovL3ZpcGRvY2ltZy9sb2dvLnBuZw/dissolve/20/gravity/Center/dx/20/dy/20/ws/0.2|watermark/4/text/5L-u6L2m5Yqp5omL/fontsize/800/fill/Z3JheQ==/dissolve/10/rotate/30/uw/180/uh/180/resize/1|watermark/4/text/5L-u6L2m5Yqp5omL/fontsize/200/fill/cmVk/dissolve/10/rotate/30/uw/180/uh/180/resize/1|imageView2/0/format/jpg当前水印参数内无法使用的问题这边内部反馈下。

**客户**：好的谢谢

### 根本原因分析
客户端网络环境或本地DNS配置问题

---

## 问题 15: 歌词文件lrc属于什么类型

**分类标签**: 对象存储｜上传下载

### 详细问题描述
'mimeLimit'  => 'audio/*;video/*;application/*;text/plain',这块要怎么写才能支持上传lrc文件呢

### 客服解答内容
**客户**：'mimeLimit'  => 'audio/*;video/*;application/*;text/plain',这块要怎么写才能支持上传lrc文件呢

**客服**：您好，先不指定，上传后看这边存储类型是什么再进行指定是否可以

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 16: 同一个空间的两个域名一个能访问一个不能访问

**分类标签**: CDN｜访问下载

### 详细问题描述
oa-web空间中的网页，使用绑定的两个域名，其中一个永远白屏，并且两个域名下载速度都非常慢。从昨天开始遇到该问题，刷新目录也不管用。

### 客服解答内容
**客户**：oa-web空间中的网页，使用绑定的两个域名，其中一个永远白屏，并且两个域名下载速度都非常慢。从昨天开始遇到该问题，刷新目录也不管用。

**客服**：您好哪个域名访问显示的白屏 这边测试打开是正常的 麻烦提供下您那边的复现截图

**客户**：就是白的，什么都没有，多数人访问都这样。什么都不显示。

**客服**：这边访问打开如下，您可以换个网络环境试下[图片]

**客户**：我总不能让全公司的人换网吧...之前都正常，昨天开始就不行了

**客服**：域名的cname等解析配置没有问题 可以修改一下您本地网络的dns试下 建议修改dns为 [REDACTED_IP]，备用选择 [REDACTED_IP]

**客户**：而且无论用哪个域名打开，文件加载速度都很慢，是不是你们的CDN节点有挂掉的...我们的更新操作跟以往没区别，应该是CDN本身的问题

**客户**：不是我一个人的问题...不在杭州的也打不开

**客户**：这是个普遍现象，基本上我们公司的人都打不开

**客服**：ping 一下 这个域名 把您那边的节点反馈过来 这边代理测试下

**客户**：ping oaweb.zjdljt.comPING allcdn.lv2.qnydns.com ([REDACTED_IP]): 56 data bytes64 bytes from [REDACTED_IP]: icmp_seq=0 ttl=51 time=101.974 ms64 bytes from [REDACTED_IP]: icmp_seq=1 ttl=51 time=55.722 ms64 bytes from [REDACTED_IP]: icmp_seq=2 ttl=51 time=32.482 ms

**客户**：跟oaweb.dllpjt.com的ping的ip一样，但是zjdljt.com的time特别长ping oaweb.dllpjt.comPING allcdn.lv2.qnydns.com ([REDACTED_IP]): 56 data bytes64 bytes from [REDACTED_IP]: icmp_seq=0 ttl=51 time=10.768 ms64 bytes from [REDACTED_IP]: icmp_seq=1 ttl=51 time=20.062 ms64 bytes from [REDACTED_IP]: icmp_seq=2 ttl=51 time=10.204 ms64 bytes from [REDACTED_IP]: icmp_seq=3 ttl=51 time=9.898 ms64 bytes from [REDACTED_IP]: icmp_seq=4 ttl=51 time=11.983 ms

**客服**：代理cdn节点测试是正常的 您那边是否开的有代理 关闭一下再访问[图片]

**客户**：没有代理，完全一样的机器，ping这两个不同的域名dllpjt.com的time都是10ms，zjdljt.com的time都是好几百ms

**客户**：绑定的同一个空间，不应该完全一样吗？现在跟其他的都没关系，dllpjt.com的域名是正常访问的，zjdljt.com的域名就是不行

**客服**：运行下方这个 这边看下您的耗时
curl -svo /dev/null  -w "dns时间: %{time_namelookup}s \ntcp连接时间: %{time_connect}s  \n传输时间: %{time_pretransfer}s \n首字节时间: %{time_starttransfer}s \n跳转时间: %{time_redirect}s  \n下载用时: %{time_total}s \n下载速度: %{speed_download}B/s\n\n" http://oaweb.zjdljt.com/

**客户**：* Host oaweb.zjdljt.com:80 was resolved.* IPv6: (none)* IPv4: [REDACTED_IP], [REDACTED_IP], [REDACTED_IP], [REDACTED_IP], [REDACTED_IP]*   Trying [REDACTED_IP]:80...* Connected to oaweb.zjdljt.com ([REDACTED_IP]) port 80> GET / HTTP/1.1> Host: oaweb.zjdljt.com> User-Agent: curl/8.7.1> Accept: */*>* Request completely sent off< HTTP/1.1 200 OK< Server: openresty< Date: Tue, 22 Oct 2024 07:03:46 GMT< Content-Type: text/html< Content-Length: 26706< Connection: keep-alive< Accept-Ranges: bytes< Access-Control-Allow-Origin: *< Access-Control-Expose-Headers: X-Log, X-Reqid< Access-Control-Max-Age: 2592000< Age: 1358< Cache-Control: public, max-age=31536000< Content-Disposition: inline; filename="index.html"; filename*=utf-8''index.html< Content-Md5: Fq8yTUNvvyXaLda7jKVOcw==< Content-Transfer-Encoding: binary< Etag: "Ft-DCQSLNNDJ7_B26iYxTSLMt0Y5"< Last-Modified: Mon, 21 Oct 2024 06:36:42 GMT< Vary: Accept-Encoding< X-Log: X-Log< X-M-Log: QNM:cdn-cache-dls-zjwz-wz-5;QNM3< X-M-Reqid: KTiSVMgeF< X-Qiniu-Zone: 0< X-Qnm-Cache: Hit< X-Reqid: yHsAAACN6jkuswAY< X-Svr: IO<{ [8893 bytes data]* Connection #0 to host oaweb.zjdljt.com left intactdns时间: 3.003487stcp连接时间: 3.593085s传输时间: 3.593313s首字节时间: 4.330214s跳转时间: 0.000000s下载用时: 5.192905s下载速度: 5142B/s

**客服**：您那边下行网络带宽有其他业务占用吗[图片]

**客户**：网速快不快不重要，反正就是oaweb.zjdljt.com这个网址打不开,但是oaweb.dllpjt.com能打开

**客服**：这边帮您优化一下线路 您20分钟后再访问看下

**客户**：不管怎么说...反正现在出来了...

**客服**：好的 可以再观察下

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 17: 买了流量包，免费的10G没有了吗？

**分类标签**: CDN｜流量计费问题

### 详细问题描述
购买了中国大陆全时段加速流量100GB， 每月免费的10G流量就没有了？

### 客服解答内容
**客户**：购买了中国大陆全时段加速流量100GB， 每月免费的10G流量就没有了？

**客服**：您好，每月免费的 10G 一直有的，只是只有 HTTP 的 CDN域名才有的

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 18: 图片打不开

**分类标签**: 对象存储｜上传下载

### 详细问题描述
图片打不开http://seven7oss.ztdy.cc/images/202306/02141504_95927816.jpg

### 客服解答内容
**客户**：图片打不开http://seven7oss.ztdy.cc/images/202306/02141504_95927816.jpg

**客服**：您好，这边测试可以打开的，您切换个设备或网络试下呢[图片]

**客户**：欠费充值之后多久能正常访问

**客服**：您好，10分钟左右

### 根本原因分析
访问权限、网络路由或CDN配置问题

---

## 问题 19: 文件上传出现大量超时情况

**分类标签**: 对象存储｜上传下载

### 详细问题描述
小程序上传报错后会往我们后台添加一条日志，以作数据分析，图片上传功能，今日已接受到大量报错信息，反馈的问题几乎都是上传图片超时，请求调取日志协助排查超时原因  {"error":"","data":{"type":"mini_upload_error_fail","error":{"errno":5,"errMsg":"uploadFile:fail fail:time out"}},"systemInfoSync":{"screenWidth":360,"cpuType":"unknown","phoneCalendarAuthorized":true,"windowHeight":709,"bluetoothEnabled":true,"bluetoothAuthorized":false,"language":"zh_CN","microphoneAuthorized":true,"fontSizeScaleFactor":1,"locationAuthorized":true,"notificationAuthorized":true,"model":"PJE110","statusBarHeight":40,"safeArea":{"width":360,"right":360,"top":0,"left":0,"bottom":792,"height":792},"brand":"OnePlus","windowWidth":360,"locationEnabled":true,"benchmarkLevel":31,"screenHeight":792,"abi":"arm64-v8a","version":"8.0.51","cameraAuthorized":true,"deviceAbi":"arm64-v8a","system":"Android 14","memorySize":15181,"fontSizeSetting":16,"pixelRatio":3,"deviceOrientation":"portrait","wifiEnabled":true,"screenTop":83,"platform":"android","SDKVersion":"3.6.2","enableDebug":false,"devicePixelRatio":3,"host":{"env":"WeChat","version":671101753},"mode":"default"}}

### 客服解答内容
**客户**：[图片]小程序上传报错后会往我们后台添加一条日志，以作数据分析，图片上传功能，今日已接受到大量报错信息，反馈的问题几乎都是上传图片超时，请求调取日志协助排查超时原因  {"error":"","data":{"type":"mini_upload_error_fail","error":{"errno":5,"errMsg":"uploadFile:fail fail:time out"}},"systemInfoSync":{"screenWidth":360,"cpuType":"unknown","phoneCalendarAuthorized":true,"windowHeight":709,"bluetoothEnabled":true,"bluetoothAuthorized":false,"language":"zh_CN","microphoneAuthorized":true,"fontSizeScaleFactor":1,"locationAuthorized":true,"notificationAuthorized":true,"model":"PJE110","statusBarHeight":40,"safeArea":{"width":360,"right":360,"top":0,"left":0,"bottom":792,"height":792},"brand":"OnePlus","windowWidth":360,"locationEnabled":true,"benchmarkLevel":31,"screenHeight":792,"abi":"arm64-v8a","version":"8.0.51","cameraAuthorized":true,"deviceAbi":"arm64-v8a","system":"Android 14","memorySize":15181,"fontSizeSetting":16,"pixelRatio":3,"deviceOrientation":"portrait","wifiEnabled":true,"screenTop":83,"platform":"android","SDKVersion":"3.6.2","enableDebug":false,"devicePixelRatio":3,"host":{"env":"WeChat","version":671101753},"mode":"default"}}

**客服**：您好，请稍等，这边帮您确认下

**客服**：您好，这个报错不是这边返回的报错，这个看起来是微信里面的报错，你们使用的上传域名是哪个呢

**客户**：https://yun.vitavp.com/

**客户**：设置的超时时间是5秒，一般的文件5秒应该就传完了呀，关键是报这个错误的人员比较分散，又是同一个问题

**客户**：这里上传的都是图片，基本上在5MB以内

**客服**：您好，yun.vitavp.com 这个是CDN访问域名，不是上传域名，华北存储空间的上传域名是 upload-z1.qiniup.com ，你们要看下这个上传域名的具体报错才可以

**客户**：https://up-z1.qiniup.com

**客户**：使用的是  NCN 区域， 域名为  https://up-z1.qiniup.com

**客服**：您好，这个你们将客户端的超时时间设置成30秒试试，看下是否会有所改善呢

### 根本原因分析
上传超时时间设置过短或网络环境不稳定

---

## 问题 20: 删除一个不用的桶，删除对应域名已经过了一天了

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
要删除的域名为 storage81544752-2410211716.online-office.net对应的桶为：storage81544752-2410211716停用那个域名一天了，还是在请配置 CNAME 步骤，但是是要删除的 ，不配置cname了。帮我处理下这个域名的状态到正确的位置，我自行删除

### 客服解答内容
**客户**：要删除的域名为 storage81544752-2410211716.online-office.net对应的桶为：storage81544752-2410211716停用那个域名一天了，还是在请配置 CNAME 步骤，但是是要删除的 ，不配置cname了。帮我处理下这个域名的状态到正确的位置，我自行删除

**客服**：稍等

**客户**：我补下图[图片]

**客服**：您好，刷新下页面，域名已删除。

**客户**：可以了

### 根本原因分析
资源删除流程或权限配置问题

---

## 问题 21: 已开启HTTP/2 访问为什么没有生效？

**分类标签**: CDN｜配置问题

### 详细问题描述
https配置，已开启HTTP/2 访问，为什么访问的时候走的还是http/1.1？请帮忙检查一下是哪里的问题

### 客服解答内容
**客户**：https配置，已开启HTTP/2 访问，为什么访问的时候走的还是http/1.1？请帮忙检查一下是哪里的问题

**客服**：您好这边测试看下 请稍等

**客服**：这个域名您配置的有referer 这边测试打开显示的协议是h2 可以刷新cdn缓存后再看下[图片]

**客户**：谢谢，看来是缓存问题。

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 22: 你好，对象存储不是10g内免费吗，为什么我被扣费了

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
你好，对象存储不是10g内免费吗，为什么我被扣费了，还是说存储空间10g内不收费，然后流量另算？

### 客服解答内容
**客户**：你好，对象存储不是10g内免费吗，为什么我被扣费了，还是说存储空间10g内不收费，然后流量另算？

**客服**：您好，存储10GB内不计费的，CDN的访问流量的话，http协议有10GB免费额度的，https协议是没有免费额度的

**客户**：http是每月10G免费额度吗？就是说我存在里面的文件，我正常访问都是算cdn访问流量吗

**客服**：您好，看您这边是通过什么域名访问的，您这边绑定的是CDN域名还是自定义源站域名呢

**客户**：是cdn域名，

**客服**：您好，那正常访问就是算cdn访问流量的

**客户**：改成自定义源站域名的话是不是就不算流量了

**客服**：您好，自定义源站域名计费的是外网流量的，比CDNhttp流量贵一些的

**客户**：那cdn是每月10G免费流量吗

**客服**：您好，CDN的话使用http协议是有免费10GB的，使用https协议的话就没有的

**客户**：是每月刷新10G 还是整个账号一共10G

**客服**：您好，每个月都有

**客户**：那能帮我查查我怎么扣费了吗，好像没用够10G 还是我用到了https？

**客服**：这边看您的域名cdn.dgq63136.icu走的是https协议的

**客户**：还有一个问题，是一个对象存储库每月10G，还是整个账号一个月10G

**客服**：每个区域的

**客户**：就是说我在华北建一个库有10g，然后华南建一个库也有10g

**客服**：您好，嗯嗯是的

### 根本原因分析
计费规则理解偏差或资源使用量超出预期

---

## 问题 23: fast-file.huadianf.com

**分类标签**: CDN｜访问下载

### 详细问题描述
fast-file.huadianf.com 配置成功，但是无法使用

### 客服解答内容
**客户**：fast-file.huadianf.com 配置成功，但是无法使用

**客服**：您好您可以换个网络再次访问看下 测试打开是正常的[图片]

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 24: 修改文件的存储类型后该文件的生命周期是怎么样的

**分类标签**: 对象存储｜上传下载

### 详细问题描述
qshell 修改文件的存储类型由深度归档变成归档直读后，该文件得生命周期是从修改开始算 还是按照上传时间算（设置新的生命周期，在七牛官网设置）

### 客服解答内容
**客户**：qshell 修改文件的存储类型由深度归档变成归档直读后，该文件得生命周期是从修改开始算 还是按照上传时间算（设置新的生命周期，在七牛官网设置）

**客服**：您好，生命周期规则设置成功后，仅对新上传的文件有效果，空间内旧有文件不会通过生命周期规则执行变更。生命周期规则设置成功后，新上传的文件，会在设置在xx天后的当天内删除文件。当portal中设置对整个空间生效的生命周期规则，接口或SDK中设置了单个文件生命周期规则，其接口或SDK中单个文件的生命周期设置优先级最高详情参考：https://developer.qiniu.com/kodo/manual/3699/life-cycle-management

**客户**：不是  麻烦你再看看我的问题呢  我对文件修改了存储类型 就是一个文件本来按照生命周期已经到了深度归档  然后我把他解冻修改成归档直读   那么这个文件还会变成深度归档吗

**客服**：就是一个文件本来按照生命周期已经到了深度归档 然后我把他解冻修改成归档直读——》一个文件触发生命周期后就不会再触发了的生命周期规则设置成功后，仅对设置后新上传的文件有效果，空间内旧有文件变动不会通过生命周期规则执行变更

**客户**：好的 我明白了 那如果我对这个文件用qshell设置新的生命周期 就是按照设置的时间开始计算对吧

**客服**：您好，嗯嗯是的

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 25: 访问对象存储的文件显示跨域

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
Access to XMLHttpRequest at 'https://imgcdn.mijian360.com/uploads/2024/9/4/[REDACTED_PHONE]10/704057.wav' from origin 'https://testadmin666.mijian360.com' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.

### 客服解答内容
**客户**：Access to XMLHttpRequest at 'https://imgcdn.mijian360.com/uploads/2024/9/4/[REDACTED_PHONE]10/704057.wav' from origin 'https://testadmin666.mijian360.com' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.

**客服**：您好，您这边配置一下跨域响应头看下，值为*号https://developer.qiniu.com/fusion/6778/the-http-response-header-configuration[图片]

**客户**：配置完大概多久生效？

**客户**：配置完还是一样[图片][图片]

**客服**：配置完成后清理一下CDN缓存使用无痕浏览看下的刷新缓存方法请参考：https://developer.qiniu.com/fusion/kb/1325/refresh-the-cache-and-the-effect-of-time方法1: portal.qiniu.com 控制台刷新缓存，点击左侧 cdn => 刷新预取方法2: api 接口地址：https://developer.qiniu.com/fusion/api/1229/cache-refreshTip : url 刷新，全网生效 10min 左右，目录刷新需要 30min 左右

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 26: 删除空间cd-edu及其所有文件

**分类标签**: 对象存储｜工具使用

### 详细问题描述
想删除空间cd-edu，但提示要先删除空间中的文件。一共有4万多文件，怎么操作？目前的批量操作，一次只能删除50个文件。

### 客服解答内容
**客户**：想删除空间cd-edu，但提示要先删除空间中的文件。一共有4万多文件，怎么操作？目前的批量操作，一次只能删除50个文件。

**客服**：您好，您可以通过qshell批量删除，三条命令就可以了。1.先下载qshell工具并使用qshell account 命令登陆账户。下载及安装文档 https://developer.qiniu.com/kodo/tools/1302/qshellwindows环境下安装qshell教程 https://developer.qiniu.com/kodo/kb/5545/windows-environment-installation-qshell-tutorial2.使用listbucket2命令列举出空间内所有资源例如 qshell listbucket2 空间名 -o result.txt命令文档 https://github.com/qiniu/qshell/blob/master/docs/listbucket2.md3.使用batchdelete命令批量删除第2步列举出的列表文件。例如 qshell batchdelete --force 空间名 -i result.txt命令文档 https://github.com/qiniu/qshell/blob/master/docs/batchdelete.md注意：主动删除资源不可以恢复，请慎重

**客服**：您好您也可以使用最新的图形化工具kodo-browser进行删除，支持批量管理。https://developer.qiniu.com/kodo/tools/5972/kodo-browser注意：使用该工具目前进行上传/下载，如果不指定cdn域名的话，下载产生的流量费用为「外网流量」

**客户**：你能否帮忙删除呢？

**客户**：使用Kodo浏览器，AccessKeyId、AccessKeySecret 在哪个界面上可以看到？

**客服**：您好，可以在这边获取ak和skhttps://portal.qiniu.com/developer/user/key

### 根本原因分析
资源删除流程或权限配置问题

---

## 问题 27: 上传的图片在手机上访问不到，在电脑上可以访问

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
https://img.cmdoujiao.com/douquan/20240919/ac09aefb625f40ec96b44be1fb2c4ac7.jpg

### 客服解答内容
**客户**：https://img.cmdoujiao.com/douquan/20240919/ac09aefb625f40ec96b44be1fb2c4ac7.jpg

**客户**：联系[REDACTED_PHONE]

**客服**：您好，您这边手机访问有什么报错？

### 根本原因分析
SSL证书配置问题或HTTPS协议未正确部署

---

## 问题 28: 域名一直未创建成功

**分类标签**: CDN｜其他类咨询

### 详细问题描述
CNMAE 已配置过

### 客服解答内容
**客户**：CNMAE 已配置过[图片]

**客服**：您好，请稍等，这边帮您确认下

**客服**：你好，久等，域名已处理完成

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 29: 删除一天了, 还是不行

**分类标签**: 对象存储｜镜像存储

### 详细问题描述
删除一天了, 还是不行

### 客服解答内容
**客户**：删除一天了, 还是不行[图片]

**客服**：稍等

**客服**：您好，已删除完成

### 根本原因分析
资源删除流程或权限配置问题

---

## 问题 30: 域名一直显示配置中，一天了还是这样

**分类标签**: CDN｜配置问题

### 详细问题描述
我需要配置ssl证书，域名一直显示配置中

### 客服解答内容
**客户**：我需要配置ssl证书，域名一直显示配置中[图片]

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 31: 无法开具发票

**分类标签**: 账户与财务｜发票问题

### 详细问题描述
2023年3月27日充值了1000，之后每个月都在扣费。但一直都无法开具发票

### 客服解答内容
**客户**：2023年3月27日充值了1000，之后每个月都在扣费。但一直都无法开具发票[图片][图片][图片]

**客服**：您好，超出6个月充值金额，或低于1000元金额的发票，您无法自行申请，不清楚金额的话可以在开票金额栏填写全部金额还请您在控制台提前申请准备好对应的发票抬头信息，添加对应的专票抬头信息审核通过后，如果您已经有了专票的抬头信息，可以不用再次添加，另外，给您开的发票默认是数电发票，需要纸质发票可以说明需求，提供收件地址。根据《增值税专用发票使用规定》申请专票必须要和实名认证公司名保持一致。-------------开票信息-----------开票金额:发票抬头: 发票类型: 纳税人识别号: 开户银行名称: 开户账号: 公司名称: 公司地址: 联系电话:

**客户**：已经在控制台提交过开票信息，并也已审核通过了的。[图片]

**客服**：开票金额1000，电子发票可以吗

**客户**：电子票可以。需要开增值税专用发票

**客服**：好的 这边同步财务处理 请稍等

**客户**：请问是否以后都是小于等于1000，都需要通过工单联系你们才能开票？

**客服**：超出6个月充值金额，或低于1000元金额的发票都需要工单来申请

**客服**：已经告知财务帮您开具电子发票 您可以到https://portal.qiniu.com/financial/invoice-contract/invoice 留意发票进度 开具完成后直接下载即可

**客户**：那怎么才能开具呢

**客服**：1000元的发票 已经开具了 你到 https://portal.qiniu.com/financial/invoice-contract/invoice  看下

**客户**：大哥，我要23年1000块的发票，开具的是24年的

**客服**：稍等这边确认下

**客服**：麻烦您提供一下可以联系到您的联系方式，商务经理需要联系您处理

**客户**：[REDACTED_PHONE]

**客服**：好的您保持电话畅通

**客服**：商务经理打您电话还是没有打通哈，加您微信了您通过一下

**客服**：您好，您的发票已经申请，您可以在发票管理查看您的开票进度https://portal.qiniu.com/financial/invoice-contract/invoice

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 32: 新增CDN域名无法访问

**分类标签**: CDN｜访问下载

### 详细问题描述
空间是有该文件的， 临时域名可以访问， 新增的CDN域名无法访问

### 客服解答内容
**客户**：空间是有该文件的， 临时域名可以访问， 新增的CDN域名无法访问

**客服**：您好，请稍等，这边帮您确认下

**客服**：您好，当前已经可以访问，您试试呢

### 根本原因分析
访问权限、网络路由或CDN配置问题

---

## 问题 33: 充值未到账

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
财务充值忘了备注账号，目前付款了，但是未充值到账，麻烦处理一下谢谢。需充值账号：[REDACTED_EMAIL]

### 客服解答内容
**客户**：财务充值忘了备注账号，目前付款了，但是未充值到账，麻烦处理一下谢谢。需充值账号：[REDACTED_EMAIL][图片]

**客服**：您好，收到，这边同步商务为您跟进处理。

**客户**：好的，尽快，谢谢

**客服**：您好，已到账了哈

**客户**：谢谢

### 根本原因分析
充值转账信息未正确备注或财务系统处理延迟

---

## 问题 34: 证书即将到期

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
麻烦帮忙处理下证书即将过期问题

### 客服解答内容
**客户**：麻烦帮忙处理下证书即将过期问题[图片]

**客服**：您好，这个您直接重新申请一个免费证书即可，手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide

**客户**：接下来如何操作[图片]

**客服**：你好，你基于提示，去添加对应的 TXT 解析，然后验证等待签发证书即可[图片]

**客户**：已经部署成功，感谢

**客服**：好的

### 根本原因分析
域名所有权验证未通过或DNS记录配置错误

---

## 问题 35: 企业认证

**分类标签**: 账户与财务｜账户问题

### 详细问题描述
授权人扫码按照提示提交认证后；就重新回到打开摄像头这个页面重新换浏览器认证、刷新都是这样

### 客服解答内容
**客户**：授权人扫码按照提示提交认证后；就重新回到打开摄像头这个页面重新换浏览器认证、刷新都是这样[图片][图片]

**客服**：稍等

**客服**：您好，能方便将手机端操作录个屏提供下吗

**客户**：稍等

**客户**：用对公账号进行企业认证；也收到了七牛的小额打款；请问在认证页面哪里去填写这个小额？？

**客户**：用对公账号进行企业认证；也收到了七牛的小额打款；请问在认证页面哪里去填写这个小额？？[图片]

**客服**：稍等

**客服**：当前需要人工审核的，稍等这边已催促专员加急，审核后认证页面中可以回填金额。

**客户**：已收到打款   认证页面哪里填写[图片][图片]

**客服**：刷新下页面呢，这边看已经是待回填状态了

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 36: 修改 HTTPS 配置处理卡住了

**分类标签**: CDN｜证书问题

### 详细问题描述
修改 HTTPS 配置处理卡住了

### 客服解答内容
**客户**：修改 HTTPS 配置处理卡住了

**客服**：稍等

**客服**：久等了，配置已下发

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 37: SSL证书续期好久一直在处理中

**分类标签**: CDN｜证书问题

### 详细问题描述
一直处理中怎么回事啊

### 客服解答内容
**客户**：一直处理中怎么回事啊[图片]

**客服**：您好wpqiniu.940216.top 这个证书您是在2024-07-01 00:08:53申请的 没有配置所有权验证 证书未签发部署

**客服**：可以申请一个新的证书 签发后部署到域名手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide4.升级HTTPS配置https://developer.qiniu.com/fusion/manual/4952/https-configuration注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

### 根本原因分析
系统配置任务处于处理队列中，需要手动介入加速处理流程

---

## 问题 38: 账号注销

**分类标签**: 账户与财务｜账户问题

### 详细问题描述
本来想用七牛云把思源笔记同步的，试了一下发现不是我这个电脑小白能玩的明白的，遂请求注销账号。

### 客服解答内容
**客户**：本来想用七牛云把思源笔记同步的，试了一下发现不是我这个电脑小白能玩的明白的，遂请求注销账号。

**客服**：您好，目前注销可以在控制台操作https://portal.qiniu.com/developer/user/security目前用户自助注销需满足以下所有条件：1、账号为普通账号（非财务父子账号、OEM账号）2、账号下实时消费无产品用量、无消费金额（数据需要您自己删除）对象存储：https://portal.qiniu.com/kodo/bucketCDN：https://portal.qiniu.com/cdn/domain3、账号下无各种欠费实时消费明细（查看您当月消费）https://portal.qiniu.com/financial/bills/estimated-consume如有欠费，将在下月5号出账、8号扣款，结算后，您再提交账号注销。4、账号下没有正在处理的提现审批https://portal.qiniu.com/financial/withdraw5、账号当前没有被冻结注意：账号注销后，账号无法找回

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 39: 配置证书无法配置

**分类标签**: CDN｜证书问题

### 详细问题描述
配置证书无法配置

### 客服解答内容
**客户**：配置证书无法配置

**客服**：您好qiniu.laobingchuxing.com已经配置好了 您再看下

### 根本原因分析
SSL证书申请、验证或部署流程问题

---

## 问题 40: 上传记录

**分类标签**: 对象存储｜上传下载

### 详细问题描述
10月22日的上传记录是否能够查到？

### 客服解答内容
**客户**：10月22日的上传记录是否能够查到？

**客服**：您好开启存储空间日志 可以下载查看

**客户**：如果没有开启的话，就无法查看了？

**客服**：这边后台可以帮您查询一下  大概是几点的上传

**客户**：2024-10-22 08:05:10  大概这个时间段左右，有未经我们上传的文件覆盖。

**客服**：可以打开 https://dn-odum9helk.qbox.me/FiqKpnlv6zvXqWM7m7r7z-WuydOL?attname=jzmj-pkg.xlsx 查看具体日志记录

**客户**：这个记录里的时间不对，这个记录里的时间是今天10月22日13点~14点左右的。我需要的是上午的时间段的上传或覆盖记录。

**客服**：上午时段没有相关日志

**客户**：查不到日志，是说明商务没有上传记录，还是说你们的日志策略只能查近几个小时的？

**客服**：没有上传记录

**客户**：那方便我给个文件名帮我看下吗？

**客户**：jzmj-pkg/b347920b41579a69cf6eeb52f1e7d6fd/这个路径下的修改记录有吗？

**客服**：jzmj-pkg是空间名b347920b41579a69cf6eeb52f1e7d6fd——是文件名前缀吗 最好给一个具体的文件名

**客户**：/b347920b41579a69cf6eeb52f1e7d6fd/project.manifest这个文件

**客服**：存储里现在有（/b347920b41579a69cf6eeb52f1e7d6fd/project.manifest）这个文件吗  把完整文件名给下 这边查询上传日志

**客户**：https://jzmjpkg.ctyoyo.com/b347920b41579a69cf6eeb52f1e7d6fd/project.manifest

**客户**：是这个文件

**客服**：这个可以查询到 是用python上传的  上传IP是 [REDACTED_IP]  具体时间是 2024-10-22T00:05:09.878000 +8小时

**客户**：如果我使用空间锁定功能，当我需要删除的时候，如何操作呢？

**客服**：您是说设置为私有空间吗？

**客户**：不是，空间有一个锁定的功能，可以一次写入多次读取的功能。

**客户**：https://developer.qiniu.com/kodo/8545/set-the-object-lock就是这个功能。

**客户**：如因特殊原因，如果我们需要删除的话，就没有其他方案了？只能等待保护期？

**客服**：在对象锁定启用后，不可删除或覆盖文件，包括元数据和文件数据内容本身，如修改文件名、修改文件类型、修改文件元信息

**客户**：七牛空间上传如何配置白名单？

**客服**：可以配置空间的referer白名单配置方式可以参考 https://developer.qiniu.com/kodo/8618/dev-preventing-hotlinking

**客户**：你好，我们空间设置了锁定空间功能，能够帮我们手动将之前的内容同步下锁定和时限吗？我们重新上传的话，涉及到的文件实在过多了。

**客服**：很抱歉这个无法实现  对象锁定启用后 数据是无法修改调整处理的

**客户**：那我之前设置锁定7天，改成了锁定1年，前面的时间会生效吗？

**客服**：最新修改锁定1年 就是以新的时间点为准 锁定存量文件1年时间

**客服**：改为锁定1年后，这个设置的保留周期仅作用在设置完成后空间内新上传的文件上

**客户**：那请问，我设置内容锁定后，通过同步的方式将另一个空间的内容迁移过来，是否可以应用这个内容锁定的规则呢？

**客服**：迁移过来的属于新文件适用这个规则的

**客户**：请问我使用菜单里的提供的数据迁移，总提示失败是哪里配置有问题呢？

**客服**：您好是在七牛控制台 - 数据迁移 界面提交的迁移任务吗？是的话，辛苦点击详情给下具体错误信息，这边看下

**客户**：[图片]任务 ID：6718de0fc27a4a9ceee86515

**客服**：您好看报错是空间名错误，您那边看下空间名是否有多余空格啥的？

**客户**：新任务 ID：6718e54007afce44f78ccce6确定空间名没有空格，是直接用的空间名复制来的。也复制在文档里检查没发现空格。

**客户**：报错信息：list objects failed: NoSuchBucket: The specified bucket does not exist status code: 404, request id: 9bIAAADmUy0yEwEY, host id:

**客服**：您好麻烦给下数据迁移的配置信息，我看下

**客户**：[图片][图片]提供了截图配置信息

**客服**：您好[图片]这个信息不对，应该填写 http://s3.cn-south-1.qiniucs.com

**客户**：收到，感谢，已经迁移成功。

**客服**：您好不客气呢，您的问题解决就好

**客户**：[图片]这种完整之有有多个失败的怎么办？多传输几次吗？

**客服**：你好，这个您看下失败的具体原因是什么

**客户**：TooManyRequests: too many requests, please retry later, status code: 429

**客服**：您好，这个重试几次即可

**客户**：就一直点重试，直至迁移完为止？

**客户**：只能重试一次，之后就没有重试按钮了。

**客户**：任务 ID67199d6c07afce44f78ccceb

**客服**：创建相同迁移任务，「同名文件」配置可以指定『跳过』

**客服**：创建相同迁移任务，「同名文件」配置可以指定『跳过』，不重复拉取

**客户**：有可靠的迁移方式推荐吗？150G+的空间，从昨天迁移到今天，也才迁移了20G+

**客服**：您好，您可以使用 qshell 工具中的 batchmove 命令将一个空间中的文件批量移动或复制到另一个空间。这个是 qshell 的说明文档：https://developer.qiniu.com/kodo/tools/1302/qshell这是 qshell 列举空间中文件列表 https://github.com/qiniu/qshell/blob/master/docs/listbucket.mdbatchmove批量移动 方法文档：https://github.com/qiniu/qshell/blob/master/docs/batchmove.mdbatchcopy批量复制：https://github.com/qiniu/qshell/blob/master/docs/batchcopy.md

**客户**：请问事件通知应该如何使用？我们根据文档配置好了，然后接入钉钉机器人，空间操作并不会通知在群里？

**客服**：事件通知是发送通知信息到您填写的回调地址上的，不是钉钉机器人。

### 根本原因分析
上传接口配置、权限或网络问题

---

## 问题 41: cdn的站源配置一直不通过

**分类标签**: CDN｜配置问题

### 详细问题描述
网站能够正常打开，m端的域名cdn都配置完成了，但是www的一直测试未通过，网页能够正常打开

### 客服解答内容
**客户**：网站能够正常打开，m端的域名cdn都配置完成了，但是www的一直测试未通过，网页能够正常打开

**客户**：站源配置的ip地址测试一直未通过

**客服**：您好，请问你们具体是怎么配置的呢，麻烦截图这边看下

**客户**：图片[图片]

**客服**：您好，这个测试资源，你们写 qiniu_do_not_test.gif 试试，跳过测试先

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 42: v.i12320.com

**分类标签**: CDN｜证书问题

### 详细问题描述
创建证书，还没有审核通过，是否我操作有误

### 客服解答内容
**客户**：创建证书，还没有审核通过，是否我操作有误

**客服**：您好，目前看已经配置完成了的

**客户**：可以了，谢谢

**客服**：嗯嗯好的不客气的

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 43: CDN Very Very slow sometimes

**分类标签**: CDN｜其他类咨询

### 详细问题描述
Hi,The issue happening is that sometimes during the links cdn link stop working, and get stuck in loading... loading ... loading.. continously, and this is not only happening on the cdn links but even the qiniu login, when I click on login it takes 2-3 minutes then it says reload error refresh the page and try again. when this happening I am unable to use neither the qiniu dashboard nor the qiniu cdn files.

### 客服解答内容
**客户**：Hi,The issue happening is that sometimes during the links cdn link stop working, and get stuck in loading... loading ... loading.. continously, and this is not only happening on the cdn links but even the qiniu login, when I click on login it takes 2-3 minutes then it says reload error refresh the page and try again. when this happening I am unable to use neither the qiniu dashboard nor the qiniu cdn files.

**客户**：This very same issue happened from half hour ago from now and was resolved just 5 minutes ago

**客服**：Hello, what area is used here? Your local IP address here to confirm, you can look at another network environment and look again, according to your description here should be the problem of network environment

**客服**：Hello, what country is used here?  Give your local IP address, you can look at another network environment again, according to your description here should be the network environment problem

**客户**：My ip is 103.163.248.195I'm from Chennai, Tamil Nadu, India region, and i've tried both wifi and mobile data and with 4 different devices all yield the same result during that time.

**客服**：Hello, at present, there is no problem on our side, and no other users have reported this problem for the time being.  It should be caused by fluctuations in your local networkYour side is now normal is itWhether the recovery is automatic

**客户**：yes it is normal now but it keeps coming again and again from the last 2 days i've been getting issue and it's only in Qiniu dashboard,Qinu Support and cdn links no other place/website any where i'm getting this issue

**客服**：First of all, to open the CDN console is to use your own local network, this is the reason for the local network, CDN link to access the Caton you can provide your domain name and access url here to test

**客户**：Hey, right now I'm getting same issue, while access this link please check https://cdn.funshot.online/admin/20241022/3b4ae720b725adfc84126508452d6285.png

**客服**：Wait a moment, let me take a look

**客户**：waiting

**客服**：We have optimized the route for you and it will take effect in ten minutes. You can check again later to see if there is any improvement.

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 44: 七牛手机端H5上传接口返回错误

**分类标签**: 对象存储｜上传下载

### 详细问题描述
七牛手机端上传接口：返回{    "error": "file exists",    "fileUrl": "http://img1.maitianqiche.com/undefined",    "imageURL": "http://img1.maitianqiche.com/undefined"}

### 客服解答内容
**客户**：七牛手机端上传接口：返回{    "error": "file exists",    "fileUrl": "http://img1.maitianqiche.com/undefined",    "imageURL": "http://img1.maitianqiche.com/undefined"}

**客服**：您好，这个报错是说您空间内有这个名称的文件了空间文件是唯一的

### 根本原因分析
上传接口配置、权限或网络问题

---

## 问题 45: 云主机扩容不会

**分类标签**: 云主机｜主机

### 详细问题描述
如何将/dev/vdb 合并到 /dev/vda下

### 客服解答内容
**客户**：如何将/dev/vdb 合并到 /dev/vda下

**客服**：您好，是扩容还是需要合并？只是合并的话，可以参考下文档﻿https://blog.csdn.net/zixuan_zhao/article/details/119455954

**客户**：我们已经扩容了，有两块硬盘 /dev/vda 和 /deb/vdb 现在想将两个空间合并，怎么操作

**客户**：我也试挂载了。但是空间没有变化

**客户**：这个是挂载截图[图片]

**客户**：重启后挂载还没有了

**客服**：您好，具体的方式您可以参考下这些文档看下https://blog.csdn.net/echizao1839/article/details/103751860?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-1-103751860-blog-119455954.235^v43^pc_blog_bottom_relevance_base2&spm=1001.2101.3001.4242.2&utm_relevant_index=4

**客户**：已经挂载了，磁盘空间还是没有变化呢应该是500g[图片]

**客户**：/etc/fstab文件[图片]

**客服**：您好，挂载好后需要分区完整的流程文档https://developer.qiniu.com/qvm/7417/online-expansion-cloud-disk-linux#3

**客户**：不行呢[图片]

**客服**：你好，您现在只是挂载了，后续进行下扩容分区呢https://developer.qiniu.com/qvm/7417/online-expansion-cloud-disk-linux#3[图片]

**客服**：你好，输入下看下df -Th

**客户**：1[图片]

**客服**：您好，稍等下，这边看下

**客户**：好的

**客服**：您好，您这边400g和100g是两个盘，无法合并您目前是没有挂载上去的您先mount下

**客户**：试过了，不能挂载到根目录里？

**客户**：但是挂载到已有目录，会把我原有的文件覆盖了

**客服**：您好，两个磁盘需要挂载在不同目录下才可以，您可以在根目录下创建一个新的目录进行挂载

**客户**：但是我们项目文件是保存到一个目录里面的啊，无法分开

**客户**：有没有其他办法啊

**客服**：您好，那您只能扩展下您之前的系统盘，不能扩容新的磁盘的

**客户**：这个是可以选择的吗？

**客服**：您好，可以的

**客户**：怎么操作呢

**客户**：知道了，谢谢

**客服**：您好，好的

**客户**：我刚刚买了100g，选择在线扩容，什么时候能好啊

**客服**：您好，在线扩容就参考这个文档进行后续操作就行https://developer.qiniu.com/qvm/7417/online-expansion-cloud-disk-linux#3

**客户**：growpart /dev/vda 1执行成功了但df -Th这个命令还是400g

**客服**：您好，这边也执行成功了吗[图片]

**客户**：是的

**客户**：fdisk -l显示是500g[图片]

**客户**：1[图片]

**客服**：您好，稍等下，这边看下

**客服**：您好，您使用lsblk查看下，确认分区设备名称和文件系统类型是否匹配。

**客户**：是一样的这里也显示500g[图片]

**客服**：您好，稍等下，这边看下

**客服**：您好，您这边实例方便重启下吗？

**客户**：现在不行

**客户**：下午

**客服**：您好，您之前操作的时候有做快照吗？

**客服**：您好，好的，可以先重启试下，如果还不行，可能需要您将系统盘卸载挂到其他实例上，用fsck修复一下系统分区试下

**客服**：您好，重启前，记得做快照备份数据

**客户**：你好重启了还是显示400g

**客服**：您好，稍等下，这边核实下

**客服**：您好，重启后，再执行一下resize2fs命令

**客服**：是否可以执行

**客户**：不行执行不了[图片]

**客户**：你们那边能帮忙看下吗，直接操作，这样问来问去好浪费时间啊

**客户**：我也不知道什么问题

**客户**：只要不重启服务都可以的

**客服**：您好，参考下这个文档，进行下磁盘修复看下https://help.aliyun.com/zh/ecs/how-to-check-and-fix-the-file-systems-of-linux-instances

**客服**：你好，操作前，记得做快照备份数据

**客户**：我没有第二台服务器

**客服**：您好，是否可以授权这边操作这边挂盘，然后您修复一下？

**客户**：可以啊，我已经创建镜像了

**客户**：怎么授权

**客户**：大概要多久时间

**客服**：您好，稍等下，这边同步核实看下

**客户**：好

**客户**：开始弄了告诉我下

**客户**：会不会影响我们正常使用

**客服**：您好，这边反馈下，您稍等下

**客服**：您好，实例是否可以停止，麻烦先停止一下实例

**客服**：您好，然后麻烦提供下实例vnc密码和实例密码这边为您操作下先进行快照备份下

**客户**：你好现在不行呢，现在正是使用高峰期

**客户**：下周吧

**客服**：您好，好的，如果可以操作工单回复下

**客服**：您好，或者您创建一台按量的临时实例，卸载系统盘挂载到临时实例上操一下?操作完成再释放按量的实例？

**客户**：好，现在可能没有时间弄了。等下周我有时间才能弄了

**客服**：您好，好的，如果可以操作工单回复下

**客户**：嗯呢，谢谢

**客服**：没事的

**客户**：hello

**客户**：上次那个扩展硬盘空间没有完成，现在能指导一下怎么配置吗

**客户**：之前没有时间操作后来忘记了，现在空间不足能在教下怎么配置吗

**客服**：您好，磁盘在线扩容，您可以参考下https://developer.qiniu.com/qvm/7417/online-expansion-cloud-disk-linux

**客户**：之前试过，不行呢你看下之前的沟通记录

**客服**：您好，时间比较久远，这边核实看下

**客户**：[图片]我这有两块盘，一块系统盘500g，实际显示400g，一块挂载盘100g，在服务器上没有显示

**客户**：[图片][图片]这个是磁盘空间查看状态

**客服**：您好麻烦执行一下blkid看下

**客户**：好[图片]

**客服**：您好麻烦执行xfs_growfs /dev/vda1

**客户**：1[图片]

**客户**：现在那系统盘100g已经到了，我刚刚看到已经是500g了

**客服**：您再执行df看下

**客户**：[图片]1

**客户**：挂载盘的100g没有显示

**客服**：您好，好的，已经完成了，文件系统是xfs的，所以要用xfs_growfs命令扩容文件系统

**客户**：好的

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 46: 视频播放卡顿

**分类标签**: CDN｜访问下载

### 详细问题描述
视频是放在七牛云存储，也使用了cdn加速，用户播放视频的时候还是经常遇到卡顿的现象，有没有什么办法能优化解决

### 客服解答内容
**客户**：视频是放在七牛云存储，也使用了cdn加速，用户播放视频的时候还是经常遇到卡顿的现象，有没有什么办法能优化解决

**客服**：您好，请稍等

### 根本原因分析
CDN节点性能、网络带宽或路由优化问题

---

## 问题 47: 目录里面的文件全都删除后目录会被自动删除？

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
目录中的文件我全都清理了，系统会自动删除我的目录吗？这个怎么控制？

### 客服解答内容
**客户**：目录中的文件我全都清理了，系统会自动删除我的目录吗？这个怎么控制？

**客服**：会的。我们是key-value结构，文件夹结构是根据key中“/”模拟显示的，资源删除后，就没目录了。

**客户**：这个可以控制不删除目录吗？

**客服**：您好，需要的目录下，您可以留一个文件。

### 根本原因分析
资源删除流程或权限配置问题

---

## 问题 48: 所有保存的图片视频都没办法预览

**分类标签**: 对象存储｜上传下载

### 详细问题描述
保存在fiksvideo空间中的所有文件都没办法正常预览，而且下载不到本地

### 客服解答内容
**客户**：保存在fiksvideo空间中的所有文件都没办法正常预览，而且下载不到本地[图片]

**客服**：您好，访问的链接提供下，这边访问看下

**客户**：http://video.fotile.com/snapshot/jpg/2xenzweetxzqq/zss_test/ondemand/[REDACTED_PHONE]85.jpg

**客服**：您好，这个域名解析不在七牛的，您确定下[图片]

**客户**：好的，我看看，谢谢

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 49: HTTPS 配置处理中

**分类标签**: CDN｜证书问题

### 详细问题描述
HTTPS 配置长时间处于处理中，请尽快解决

### 客服解答内容
**客户**：HTTPS 配置长时间处于处理中，请尽快解决

**客服**：您好这边帮您手动介入处理下 请稍等

**客户**：不分图片视频访问不到呢

**客服**：已经处理好了

**客服**：您再访问试下

### 根本原因分析
系统配置任务处于处理队列中，需要手动介入加速处理流程

---

## 问题 50: apk文件怎么下载

**分类标签**: CDN｜访问下载

### 详细问题描述
apk文件下载不了

### 客服解答内容
**客户**：apk文件下载不了

**客服**：你好，请稍等，这边帮您确认下

**客服**：您好，这边测试可以正常下载，您这边下载失败主要是什么报错呢

**客户**：This XML file does not appear to have any style information associated with it. The document tree is shown below."); vertical-align: bottom; height: 10px;"><Error><Code>ApkDownloadForbidden</Code><Message>The APK file is not allowed to be distributed in a public network using the OSS endpoint, please use CNAME instead.</Message><RequestId>67176601482D373133652998</RequestId><HostId>mofangx-oss1.oss-cn-hangzhou.aliyuncs.com</HostId><EC>[REDACTED_LANDLINE]</EC><RecommendDoc>https://api.aliyun.com/troubleshoot?q=[REDACTED_LANDLINE]</RecommendDoc></Error>[图片]

**客服**：好的，请稍等

**客服**：您好，这个是您的阿里源站禁止下载，您确认下呢curl -o 1.apk http://mofangx-oss1.oss-cn-hangzhou.aliyuncs.com/mofang.apk -v                                                
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying [REDACTED_IP]:80...
* Connected to mofangx-oss1.oss-cn-hangzhou.aliyuncs.com ([REDACTED_IP]) port 80 (#0)
> GET /mofang.apk HTTP/1.1
> Host: mofangx-oss1.oss-cn-hangzhou.aliyuncs.com
> User-Agent: curl/7.77.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 400 Bad Request
< Server: AliyunOSS
< Date: Tue, 22 Oct 2024 08:59:46 GMT
< Content-Type: application/xml
< Content-Length: 448
< Connection: keep-alive
< x-oss-request-id: 67176982E001B4313986A2C5
< Accept-Ranges: bytes
< ETag: "EA83FCB8A91775E12308E39D72C12491-5"
< Last-Modified: Tue, 22 Oct 2024 07:45:36 GMT
< x-oss-object-type: Multipart
< x-oss-hash-crc64ecma: [REDACTED_ID_CARD]5540
< x-oss-storage-class: Standard
< x-oss-server-side-encryption: AES256
< x-oss-server-time: 4
< x-oss-ec: [REDACTED_LANDLINE]
< 
{ [448 bytes data]
100   448  100   448    0     0   9128      0 --:--:-- --:--:-- --:--:-- 10181
* Connection #0 to host mofangx-oss1.oss-cn-hangzhou.aliyuncs.com left intact

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 51: 总是弹出未登录，退出重新登录还是弹出！

**分类标签**: 账户与财务｜账户问题

### 详细问题描述
[    [        {            "title": "请求 ID",            "content": "DBQ4QG2GBL4qtwAY"        }    ]]

### 客服解答内容
**客户**：[    [        {            "title": "请求 ID",            "content": "DBQ4QG2GBL4qtwAY"        }    ]]

**客户**：[    [        {            "title": "请求 ID",            "content": "GHK2AQkyxMRGtwAY"        }    ],    [        {            "title": "请求 ID",            "content": "0oIIFtRTgsZGtwAY"        }    ]]

**客户**：[    [        {            "title": "请求 ID",            "content": "GHK2AUqxBPlKtwAY"        }    ]]

**客服**：您好，恢复浏览器默认设置，或者切换其他浏览器观察下呢

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 52: 启用域名卡住了

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
启用域名处理中，通常情况下 8-15 分钟完成，期间域名访问不受影响，部分配置不可修改，若较长时间未配置完成，请提交工单反馈域名：h5pic.86542.com启用域名卡住了

### 客服解答内容
**客户**：启用域名处理中，通常情况下 8-15 分钟完成，期间域名访问不受影响，部分配置不可修改，若较长时间未配置完成，请提交工单反馈域名：h5pic.86542.com启用域名卡住了[图片]

**客服**：您好，请稍等，这边帮您确认下

**客服**：您好，久等了，已处理完成

### 根本原因分析
系统配置任务处于处理队列中，需要手动介入加速处理流程

---

## 问题 53: locahost测试正常，换成远程HTTPS时出错

**分类标签**: 实时互动｜其他类咨询

### 详细问题描述
https://qn.cnabs.net:4430/svr_video_meeting? 出错信息enterRoom error, can not get accessToken. Error: 
 please check enterRoom arguments

### 客服解答内容
**客户**：https://qn.cnabs.net:4430/svr_video_meeting? 出错信息enterRoom error, can not get accessToken. Error: 
 please check enterRoom arguments

**客户**：error"token expired"明明刚生成的，为什么会超时k？

**客服**：您好，重新生成下，或者可以将有效期设置长一点的

**客户**：您好，请帮我看一下。如附件中的网页。只能看到本地视频。远程同一房间的视频并不能在本地显示出来。请问错在哪了？谢谢！

**客户**：发现了一个问题，无法在哪台电脑上访问这个网页，调用的都是开发机上的那个摄像头

**客户**：直接引用你们网络SDK也没有用 ，还是那样的 。这个网页就是你们例子中的 一个，只是移到了我的WEB环境下。其它没有动过

**客户**：请上班后帮我看一下啊，谢谢，现在卡这了，不 如如何进行了。远程也可以的

**客服**：您好，具体有什么报错信息吗？

**客户**：没报错

**客户**：所有电脑访问，调用的都是开发机上的摄像头

**客户**：https://qn.cnabs.net:4430//svr_video_meeting?roomName=1002&userId=test2

**客户**：你可以用以上链接试试，调用的都是我这边的摄像头

**客服**：您好稍等下，这边同步看下

**客服**：您好， 方便远程看下吗？ 使用向日葵 上面的链接，我这里打不开

**客户**：好

**客户**：我的识别码:383551237 使用向日葵即可对我发起远程协助 向日葵下载地址:http://url.oray.com/tGJdas/

**客服**：您好，稍等

**客服**：您好，这个是枚举https://webrtc.github.io/samples/src/content/devices/input-output/sdk也有提供枚举接口：getDevice ，getCameras 等等https://developer.qiniu.com/rtc/9070/WebQNRTC#getCameras[图片]

**客服**：[图片]

**客户**：您好，我实现在一个房间里，同时只和一个人对话，其它人静音，请问这个如何实现？喇叭又是如何静音的呢？谢谢

**客服**：您好，获取到  音视频 track ，都会有mute接口，mute 参数为true，就是 静默自己的音频，或者视频， 之后 对方 就看不到了。

**客户**：这个知道的，我的意思是，一个房间中多个人在，如果只与 指定人通话，其它人静音？而不是让其他人点 一下静音？

**客户**：admin可以一下子把所有USER静音呢

**客服**：您好，您稍等这边确认一下

**客服**：您好， sdk 有提供sendMessage 接口，可以给发给指定用户，用户在回调里 收到信息后，执行 mute接口。

**客户**：好的，谢

**客服**：嗯嗯不客气的

**客户**：请问如何关闭本地喇叭

**客服**：还请耐心等待一下，这边确认一下

**客服**：您好，可以通过控制 音量 ，比如设置为0 ，就是没有声音。音频 track 有 setVolume 接口

**客户**：音频 track  使用setMuted 有具体用法吗？没有使用的例子，也无智能提示，实在不清楚如何用，如如何取音频track。谢谢

**客服**：您好，很抱歉，现在是非工作时间，相关工程师不在线，预计下周一和您回复

**客服**：您好， 您前面调用了  create 接口，这个就会 返回具体 音频，或者 视频track 。智能提示 ，需要使用 npm方式。直接script 引入，肯定是没有任何 代码提示的。以下是 获取track，并执行 setMute方法。 https://developer.qiniu.com/rtc/9070/WebQNRTC[图片]

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 54: 绑定邮箱错误

**分类标签**: 账户与财务｜账户问题

### 详细问题描述
该账号绑定的邮箱非主体所有，疑似上一个开发团队的遗留问题，现需绑定新的邮箱。

### 客服解答内容
**客户**：该账号绑定的邮箱非主体所有，疑似上一个开发团队的遗留问题，现需绑定新的邮箱。

**客户**：尽快处理，谢谢

**客服**：您好，方法1：请登陆官网——点击官网右上角的管理控制台——个人面板——个人中心的安全设置更改邮箱，输入密码，填写邮箱进行修改。单击进入修改地址：https://portal.qiniu.com/user/security方法二：如果您因为邮箱已经无法登陆，可以通过人工申诉提供相关资料进行修改，将材料发送邮件到 [REDACTED_EMAIL]需要提供的信息如下：a、个人实名认证：请提供注册邮箱、修改原因、手持与实名认证一致的身份证正面图片、新注册邮箱；b、企业实名认证：账号认证的资质信息，公司企业营业执照副本、与修改账号邮箱的说明并加盖公司公章，将资料以扫描件的形式发送到support@qiniu.com邮箱邮件发送后请工单上告知我们，提供发件邮箱和联系电话。这边同步给商务为您审核处理

**客户**：方法一，只能邮箱验证诶，但是这个邮箱非主体所有，死锁咯

**客服**：可以方法二提供认证材料到support邮箱，走下人工的方式。

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 55: 音频审核接口

**分类标签**: 智能多媒体｜其他类咨询

### 详细问题描述
内容审核 > API 文档 > API调用音频审核

### 客服解答内容
**客户**：内容审核 > API 文档 > API调用音频审核

**客户**：这个 有php demo  吗

**客服**：您好，这个没有音频审核的现成demo的，您可以参考下这个图片审核的demo修改一下相关参数测试看下的https://github.com/qiniu/php-sdk/blob/master/examples/censor_image.php

**客户**：？？？？

**客户**：ok

**客户**：这个不是图片审核吗

**客户**：我要音频审核接口

**客服**：您好，这边目前没有现成的音频审核的demo，您需要参考下这个图片审核的demo修改一下相关参数测试看下的音频审核文档https://developer.qiniu.com/censor/8061/audio-censor

**客户**：有php demo 吗

**客户**：这个地址我知道

**客户**：视频审核 会审核视频中的声音吗

**客服**：您好，没有音频审核的demo的，只有图片审核的demo，只能参考图片审核的demo自行修改一下参数这个就是图片审核的demohttps://github.com/qiniu/php-sdk/blob/master/examples/censor_image.php

**客户**：视频审核 会审核视频中的声音吗

**客服**：不会，只会审核视频播放内容

**客户**：视频审核 直接扣的余额吗

**客户**：有资源包吗

**客服**：您好，您这边可以参考下这个的https://qmall.qiniu.com/template/MTA5?spec_combo=MjkzNQ

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 56: 配额不足

**分类标签**: 云主机｜其他类咨询

### 详细问题描述
购买主机时提示配额不足

### 客服解答内容
**客户**：购买主机时提示配额不足

**客服**：您好，您的联系方式提供下，这边同步商务和您联系为您提升配额

**客户**：[REDACTED_PHONE]

**客服**：您好，稍等下，这边同步下

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 57: 为什么视频链接地址每次刷新后都会改变？

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
为什么对象存储里的视频，每次刷新页面后链接地址都会改变？

### 客服解答内容
**客户**：为什么对象存储里的视频，每次刷新页面后链接地址都会改变？

**客服**：您好，您空间是私有空间，访问链接需要进行私有空间签算，所以刷新会修改刷新会重新进行签算

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 58: tls1.0 1.1关闭

**分类标签**: CDN｜配置问题

### 详细问题描述
之前提过工单关闭tls低版本，并且测试通过，现在看又开着工单号375799

### 客服解答内容
**客户**：之前提过工单关闭tls低版本，并且测试通过，现在看又开着工单号375799

**客服**：您好，麻烦你提供一个具体的域名，这边帮您确认下

**客户**：web.99bill.com

**客户**：3月份的工单里 也有域名列表

**客服**：您好，请稍等，这边帮您确认下

**客户**：还没解决吗

**客服**：您好，目前还在配置中，配置完成后，这边再给您反馈

**客服**：你好，已配置完成

**客户**：你们自己测试下[root@10-23-44-190 tls]# ping web.99bill.comPING opencdnqiniustaticv6.jomodns.com ([REDACTED_IP]) 56(84) bytes of data.64 bytes from [REDACTED_IP].broad.xw.sh.dynamic.163data.com.cn ([REDACTED_IP]): icmp_seq=1 ttl=45 time=7.22你们自己看看这个ip 低版本有没有禁止掉，我这里测试是没有

**客服**：您好，这边测试是可以的➜ ~ curl -IL web.99bill.comHTTP/1.1 302 Moved TemporarilyServer: JSP3/2.0.14Date: Thu, 24 Oct 2024 01:27:52 GMTContent-Type: text/htmlContent-Length: 144Connection: keep-aliveLocation: https://web.99bill.com/X-Cache-Status: MISSHTTP/2 404 server: JSP3/2.0.14

**客户**：web.99dmp.cn 低版本tls也关一下

**客服**：稍等

**客服**：您好，已处理，预计10分钟生效

**客户**：后续怎么保证 已经关过tls低版本的域名  不会发生类似的情况？

**客服**：您好，可以提交工单这边帮您检查处理。

**客服**：正常情况不会变

**客户**：这次变的原因是什么？

**客服**：稍等

**客服**：有新节点上线，历史特殊需求配置未更新上来。已单独记录配置，后续新节点也会同步配置。

**客户**：好的，希望同样的问题不要发生第二次。

**客服**：好的，您这边还有其他问题吗

**客户**：目前没有了

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 59: 网站打不开

**分类标签**: CDN｜访问下载

### 详细问题描述
网站打不开

### 客服解答内容
**客户**：网站打不开

**客服**：稍等

**客服**：您好，再试下呢，这边测试可以打开的[图片]

### 根本原因分析
访问权限、网络路由或CDN配置问题

---

## 问题 60: 怎么通过自己的域名访问存储桶

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
新创建的空间，域名只有一个月使用，怎么绑定自己的域名，自己试了，还是不行

### 客服解答内容
**客户**：新创建的空间，域名只有一个月使用，怎么绑定自己的域名，自己试了，还是不行

**客服**：您好，绑定CDN加速域名图文教程文档，您可以参考：https://developer.qiniu.com/fusion/manual/4939/the-domain-name-to-access需要注意您要绑定工信部备案的域名。

**客户**：[图片]我是在这里配置的这个，然后阿里云配置的如下：[图片]

**客服**：您好，记录值是iovip.qiniuio.com

**客服**：您好，可以的，这样也行，这个是源站域名

**客户**：我直接配置这个就可以吗

**客户**：[图片]访问这个链接好像不行

**客服**：您好，访问的链接提供下，这边看下

**客户**：http://oss.jingangxiche.com/crmebimage/public/1/2024/10/22/1f34f63b8060459f94a61d0766985c014ixjgt0kmi.jpg而且总是被重定向到https

**客服**：您好，这边访问是可以访问的，本地缓存刷新看下

**客户**：收到，我这样配置是对的吗

**客服**：您好，配置是对的如果需要https访问的话，可以参考下这个文档https配置这个文档https://developer.qiniu.com/kodo/8556/set-the-custom-source-domain-name

**客户**：收到，非常感谢

**客服**：没事的，有什么问题您再反馈

**客服**：您好，还是和您说下，源站域名产生的外网流出流量是没有免费额度的如果您需要使用http访问，可以使用cdn域名，cdn域名 http 协议有10g的免费额度cdn 的 https 协议是没有免费额度的

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 61: 忘记密码

**分类标签**: 账户与财务｜账户问题

### 详细问题描述
忘记密码

### 客服解答内容
**客户**：忘记密码

**客服**：您好在登陆界面通过忘记密码找回[图片]

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 62: 如何实现画中画功能

**分类标签**: 直播云｜直播SDK问题

### 详细问题描述
如何在PLPlayerKit的库中，实现画中画功能

### 客服解答内容
**客户**：如何在PLPlayerKit的库中，实现画中画功能

**客服**：您好，请稍等

**客服**：目前不支持这个功能

**客户**：你们介绍里面不是说支持画中画吗

**客服**：您好，当前此功能已经不支持了，您在哪里看到的呢

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 63: 证书续期

**分类标签**: CDN｜证书问题

### 详细问题描述
证书续期

### 客服解答内容
**客户**：证书续期

**客服**：您好，证书无法续期，过期后申请一个新的证书替换旧证书手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide4.升级HTTPS配置https://developer.qiniu.com/fusion/manual/4952/https-configuration注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

**客户**：域名一直启动不了

**客服**：稍等这边看下

**客服**：已启动

### 根本原因分析
域名所有权验证未通过或DNS记录配置错误

---

## 问题 64: SSL证书绑定问题

**分类标签**: 云主机｜其他类咨询

### 详细问题描述
申请的SSL证书通过了域名所有权验证，但是订单状态显示待确认（域名所有权未确认），请帮忙检查是什么问题，谢谢！

### 客服解答内容
**客户**：申请的SSL证书通过了域名所有权验证，但是订单状态显示待确认（域名所有权未确认），请帮忙检查是什么问题，谢谢！[图片]

**客服**：您好，请稍等

**客服**：您好，订单已失效，您需要重新申请一个证书，然后做验证才可以

### 根本原因分析
域名所有权验证未通过或DNS记录配置错误

---

## 问题 65: 无法绑定微信

**分类标签**: 对象存储｜上传下载

### 详细问题描述
个人中心-安全设置中，我没办法绑定微信，系统提示“非法请求”

### 客服解答内容
**客户**：个人中心-安全设置中，我没办法绑定微信，系统提示“非法请求”

**客服**：稍等

**客服**：测试绑定正常的，方便换个浏览器重新登录尝试下吗

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 66: 充值到账问题

**分类标签**: 账户与财务｜其他类咨询

### 详细问题描述
充值到账问题 ，怎么没到账

### 客服解答内容
**客户**：充值到账问题 ，怎么没到账[图片]

**客服**：您好这边帮您同步才财务 请稍等

**客户**：请尽快，谢谢

**客服**：好的

**客服**：已经到账

### 根本原因分析
充值转账信息未正确备注或财务系统处理延迟

---

## 问题 67: 主域名可以绑定  吗？

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
主域名可以绑定  吗？  如何绑定？  主域名已经解析到其他服务器了

### 客服解答内容
**客户**：主域名可以绑定  吗？  如何绑定？  主域名已经解析到其他服务器了

**客服**：您好，如果已经解析到其他解析地址了就无法绑定了的，需要使用二级域名绑定了的

**客户**：是不是需要购买SSL

**客户**：如果购买的有其他ssl  如何配置？

**客服**：您好，看您是否需要使用https协议访问的，不需要的话使用http协议的话就不用部署SSL证书的手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide4.升级HTTPS配置https://developer.qiniu.com/fusion/manual/4952/https-configuration注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 68: 无法查看密钥sk

**分类标签**: 对象存储｜上传下载

### 详细问题描述
非法请求

### 客服解答内容
**客户**：[图片]非法请求

**客户**：手机号和邮箱都尝试了，都无法正常接收验证码，请求发不出去

**客户**：麻烦立刻与我联系，电话

**客服**：您好这边查询下 请稍等

**客服**：重启一下手机试试，后台查询这个手机号验证码在2024-10-22 17:22:29已经送达 发送状态是成功的

**客户**：我更换了一下浏览器，解决了，谢谢宝贝

**客服**：好的

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 69: JAVA SDK 方法废弃，但是没有文档说明用什么替代

**分类标签**: CDN｜证书问题

### 详细问题描述
使用qiniu官方sdk进行更新ssl证书。authorization这个方法提示被废弃了，但是官方文档中还是使用这个方法，请问应该用什么方法替换这个授权方法？

### 客服解答内容
**客户**：使用qiniu官方sdk进行更新ssl证书。authorization这个方法提示被废弃了，但是官方文档中还是使用这个方法，请问应该用什么方法替换这个授权方法？

**客户**：StringMap stringMap = auth.authorization(url, null, "application/x-www-form-urlencoded");

**客服**：您好，您这边目前是使用的什么操作的接口呢？

**客户**：更新domain的配置 String url = server + "/domain/" + name + "/httpsconf";HashMap<String, Object> req = new HashMap<>();req.put("certId", certId);req.put("forceHttps", forceHttps);req.put("http2Enable", https2Enable);byte[] body = Json.encode(req).getBytes(Constants.UTF_8);StringMap stringMap = auth.authorization(url, body, Client.JsonMime);Response response = client.put(url, body, stringMap, Client.JsonMime);

**客户**：Auth类下面的 authorization 标记为废弃，但是并没有写用什么方法替换。

**客服**：您好，管理凭证的话目前是正常使用的，这个是没有修改的https://developer.qiniu.com/kodo/1201/access-token

**客户**：我知道凭证的算法没有变化，但是你们SDK里面标记为了废弃。我问的是替代方法，没有问你们算法是否改变。下面是你们SDK中 Auth.java的代码@Deprecatedpublic StringMap authorization(String url, byte[] body, String contentType) {    String authorization = "QBox " + signRequest(url, body, contentType);    return new StringMap().put("Authorization", authorization);}

**客户**：如果手都没有取代方法，为啥要把这个方法标记为废弃？不会这么随意吧？

**客服**：您这边使用的是什么版本的SDK

**客户**：<dependency>    <groupId>com.qiniu</groupId>    <artifactId>qiniu-java-sdk</artifactId>    <version>7.16.0</version></dependency>

**客服**：您好，目前域名相关接口使用的是以前的QBox鉴权的，这个目前已经没有更新了的，目前其他相关接口使用的是Qiniu鉴权的，这个鉴权可以正常使用的，但是没有维护了的

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 70: gb28181级联接入支持吗

**分类标签**: 视频监控｜业务咨询

### 详细问题描述
gb28181级联接入支持吗

### 客服解答内容
**客户**：gb28181级联接入支持吗

**客服**：您好，目前国标设备是支持接入的，您这边可以参考下这个的https://developer.qiniu.com/qvs/7448/gb-access-process

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 71: 二级域名已购SSL，，之前新增的域名 协议是http，  如何修改为https

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
二级域名已购SSL，，之前新增的域名 协议是http，  如何修改为https请协助修改

### 客服解答内容
**客户**：二级域名已购SSL，，之前新增的域名 协议是http，  如何修改为https请协助修改

**客服**：您好，看您这边域名已经在进行https处理了，目前看已经处理完成了，您刷新后再看下呢

### 根本原因分析
SSL证书申请、验证或部署流程问题

---

## 问题 72: 现已充值，因工作需要，要求能否尽快解冻，何时能正式解冻？

**分类标签**: 账户与财务｜账户问题

### 详细问题描述
现已充值，因工作需要，要求能否尽快解冻，何时能正式解冻？附件为本司的出账回单，请帮忙尽快解冻，工作需要很急

### 客服解答内容
**客户**：现已充值，因工作需要，要求能否尽快解冻，何时能正式解冻？附件为本司的出账回单，请帮忙尽快解冻，工作需要很急[图片]

**客服**：您好，稍等下，这边同步下商务加急处理下

**客服**：您好，您的充值已经到账，账号已经解冻

### 根本原因分析
充值转账信息未正确备注或财务系统处理延迟

---

## 问题 73: 无法下载存储空间的东西

**分类标签**: 对象存储｜上传下载

### 详细问题描述
报错ERROR: ACCESS DENIED

### 客服解答内容
**客户**：报错ERROR: ACCESS DENIED

**客服**：您好，麻烦您将不能下载的文件链接提供下，这边帮您确认核实下

**客户**：https://portal.qiniu.com/api/proxy/resource?target=http%3A%2F%2Fqn.xingji.pro%2Fbt_backup%2Fsite%2Fxjcloud.host%2Fweb_xjcloud.host_20240930_013055_utvuIl.tar.gz%3Fattname%3D

**客服**：您好，请稍等

**客服**：您好，你们域名配置了referer防盗链，把空间设置 和 CDN设置里面的referer防盗链关闭即可

**客户**：空间设置里  referer是关闭的

**客服**：请稍等

**客服**：您好，久等了，已帮您优化完成，您现在再试试呢

**客户**：好的 可以了 谢谢

**客户**：这个下载速度也太慢了  龟速啊 就几kb 怎么下载啊

**客服**：您好，这个是由于您的域名是纯海外加速，访问比较慢，您将域名设置成全球加速即可

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 74: 买错了

**分类标签**: 云主机｜主机

### 详细问题描述
我本来要扩容磁盘的，但是之前挂载了一个100G的磁盘，现在我已经在原有的基础上扩容了100G，ID：d-wz9h5swgnpcn57w1jibs为这个的磁盘需要退掉，钱也需要退回来

### 客服解答内容
**客户**：我本来要扩容磁盘的，但是之前挂载了一个100G的磁盘，现在我已经在原有的基础上扩容了100G，ID：d-wz9h5swgnpcn57w1jibs为这个的磁盘需要退掉，钱也需要退回来

**客服**：您好，云盘随实例释放，无法单独退云盘。

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 75: 免费 from 自动催单

**分类标签**: CDN｜证书问题

### 详细问题描述
长时间处于域名检测环节

### 客服解答内容
**客户**：长时间处于域名检测环节

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，您的域名无法进行文件验证，您尝试手动申请下证书看下呢

**客服**：您好，手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide4.升级HTTPS配置https://developer.qiniu.com/fusion/manual/4952/https-configuration注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 76: 除了通过域名访问还有哪些途径可以访问

**分类标签**: CDN｜流量计费问题

### 详细问题描述
除了通过域名访问还有哪些途径可以访问

### 客服解答内容
**客户**：[图片]除了通过域名访问还有哪些途径可以访问

**客服**：您好
存储的文件可以通过绑定cdn域名和源站域名来访问 没有其他方式
外网流出流量的费用属于对象存储的费用。
如果使用了七牛测试域名或者融合 CDN 域名访问资源，是不会计算外网流出流量的。
只有以下五种情况会计算外网流出流量：
使用第三方 CDN 回源七牛对象存储空间的回源请求。
使用 qshell 工具的 qdownload 命令下载，但没有指定 cdn_domain 。
使用 kodo-browser 工具不使用自有域名下载资源。
调用 AWS S3协议 下载空间资源。
使用 空间源站域名 下载资源。

**客户**：专业的词语我不理解，如何能让我更好的理解呢

**客服**：存储的文件只能通过域名访问

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 77: 小程序图片偶尔不加载

**分类标签**: 对象存储｜上传下载

### 详细问题描述
小程序图片偶尔全部不加载，空白

### 客服解答内容
**客户**：小程序图片偶尔全部不加载，空白[图片]

**客户**：站点所有小程序图片不加载，

**客服**：图片链接提供一下

**客服**：以及小程序访问方式 这边看下

**客服**：这边测试看域名cname配置的有问题哈，cname值应该是img-hansuixcx-com.qiniudns.com，您确认下

**客户**：图片地址：http://img.hansuixcx.com/images/1/2024/10/dqxZ55912N8555rLxL5qlKB1Xr92oq.jpg

**客户**：小程序访问方式较多就是最近使用进入

**客服**：您cname配置检查一下呢

**客户**：好的 我看下

**客服**：嗯嗯

**客户**：1

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 78: 这个链接的资源是什么时候删除的能知道吗？

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
https://img.saihuitong.com/4028/img/184843/18e0c40ca88.jpg

### 客服解答内容
**客户**：https://img.saihuitong.com/4028/img/184843/18e0c40ca88.jpg

**客服**：稍等

**客服**：您好，您这边有大致删除时间吗这边查询了近七天的日志，没有这个文件的删除记录，超过七天的就需要精确到天的范围来过滤查询了

**客户**：我这边就是不清楚是什么时候删除的，图片就没了

**客服**：您好，文件是什么时候上传的呢

**客户**：大概这个时间左右2024-03-05 09:35:56

**客服**：您好，这个时间很久了，追溯比较困难，您这个图片最后一次访问的时间大概是什么时候呢

**客户**：这个最后访问的时候不清楚，只是今天看到了突然没了

**客服**：您无法提供大概的时间范围我们这边追溯较困难，资源删除无法恢复，您本地如果有备份可以重新上传一下哈

**客户**：好吧.....

**客服**：嗯嗯

### 根本原因分析
资源删除流程或权限配置问题

---

## 问题 79: 配置时间过长

**分类标签**: CDN｜证书问题

### 详细问题描述
配置时间已经过半小时未完成

### 客服解答内容
**客户**：配置时间已经过半小时未完成

**客服**：您好，请稍等

**客服**：您好，这个是由于您备案缺失导致的经查询域名ICP备案被注销。工信部规定未备案域名不得提供服务，请办理「工信部」ICP 备案。取得备案号后通知我们进行验证解封，即可访问。工信部官网查询方式：1.登录 https://beian.miit.gov.cn/#/Integrated/recordQuery2.选择「ICP备案查询」3.输入网站域名，点击搜索

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 80: 咨询一下访问计费问题

**分类标签**: 账户与财务｜计费问题

### 详细问题描述
我们每次用户访问做了图片转换的地址，如https://qn-image.zhongyingtougu.com/images/2024/10/17/3e929073f4e44fcc8d898d29a0c54e0e?imageMogr2/format/webp，是不是访问都计费（统计流量），流量收费是否为图片大小*当天访问人次，即这个链接今天有2w人次访问，那么流量收费就是图片大小*2w

### 客服解答内容
**客户**：我们每次用户访问做了图片转换的地址，如https://qn-image.zhongyingtougu.com/images/2024/10/17/3e929073f4e44fcc8d898d29a0c54e0e?imageMogr2/format/webp，是不是访问都计费（统计流量），流量收费是否为图片大小*当天访问人次，即这个链接今天有2w人次访问，那么流量收费就是图片大小*2w

**客服**：您好，是的

**客服**：您好，您的说法是对的，您具体是还有什么问题？

### 根本原因分析
计费规则理解偏差或资源使用量超出预期

---

## 问题 81: 目前我这边存储丢失大量图片，请帮忙检查一下

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
https://cust-storag-cdn.v6c.cc/images/14/2023/04/LgRBHQq1r5CaqhGgKrsSH2B2t3YHYY.jpghttps://cust-storag-cdn.v6c.cc/images/14/2023/04/uWQBWCCYQkAWki30GWaq3c27wlCyVl.jpg不知道为什么这图片不见了

### 客服解答内容
**客户**：https://cust-storag-cdn.v6c.cc/images/14/2023/04/LgRBHQq1r5CaqhGgKrsSH2B2t3YHYY.jpghttps://cust-storag-cdn.v6c.cc/images/14/2023/04/uWQBWCCYQkAWki30GWaq3c27wlCyVl.jpg不知道为什么这图片不见了

**客服**：大概什么时候发现不见的，能否确定一个时间范围方便排查呢

**客服**：这边查询了近三个月的访问日志并未查询到删除记录哈 麻烦您确定一下时间范围

**客户**：应该是21号 22号这两天时间， 服务器那边数据都在 就是图片没了， 我来这里查询 也没找到这个图片

**客服**：文件大致是什么时间上传的 还记得吗

**客户**：链接上有， 2023年4月14日

**客服**：2023年4月14日——上传日志的保留时间没有那么久 目前无法核查后台看最近180天内 您这个空间是没有操作过删除文件的建议您确认下这个文件名是否准确

**客户**：文件名确定无误， 不止这两张图片。 是丢了很多图片。

**客服**：空间信息对不对 查看您账号下是有多个空间的

**客户**：空间也没问题，我这么跟您说吧， 就是网站那边 和 我们这边的空间 我起码1年没有改动过，除了进来续费

**客服**：有没有操作过数据迁移处理 目前从日志的角度去查找 没有过滤到这个文件名

**客户**：没有的， 问题是 我现在七牛的文件不在 跟域名应该没关系

**客服**：这个空间里近半年是没有操作过删除处理的 只有两种情况 一是没有上传成功落存储  二是文件名不对

**客户**：您看一下， 现在是大量流失。 说不清楚了[图片]

**客户**：这全丢了[图片]

**客服**：稍等

**客服**：日志无法追溯到了，查询了最近180天的日志，没有您这几个文件的记录您这边有备份的话，可以重新上传下资源。

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 82: 视频卡顿

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
https://deyixueyuan.com/wechat/course/details/series?goods_sn=XL102385&is_single=1&share_source=wechat

### 客服解答内容
**客户**：https://deyixueyuan.com/wechat/course/details/series?goods_sn=XL102385&is_single=1&share_source=wechat

**客户**：APP用户打开视频卡顿 什么原因造成的

**客服**：您好，请稍等

**客户**：麻烦快一些 幸苦

**客服**：您好，您这个具体是哪个视频链接播放卡顿呢，麻烦您将视频外链提供下，这边帮您检查下

**客户**：https://deyixueyuan.com/wechat/course/details/series?goods_sn=XL102385&is_single=1&share_source=wechatAPP里所有的视频都有卡顿的现象

**客户**：大约多久可以有结果

**客服**：稍等这边跟进下，有结果第一时间给您同步

**客服**：有具体视频外链可以提供一下吗，您提供的网站视频无法直接访问需要收费

**客户**：https://deyixueyuan.com/wechat/course/details/video?goods_sn=SP102436&is_single=1&share_source=wechat

**客户**：这个是免费的

**客服**：您好，您这个视频这边测试看起来是没问题的，您用户那边换个网络试试呢

### 根本原因分析
客户端网络环境或本地DNS配置问题

---

## 问题 83: 删除文件

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
删除时，提示输入密码是什么密码，我输入登陆密码不对

### 客服解答内容
**客户**：删除时，提示输入密码是什么密码，我输入登陆密码不对

**客服**：您好，这个是账号登录密码，您是不是弄错了呢

### 根本原因分析
资源删除流程或权限配置问题

---

## 问题 84: 存储视频无法打开，下载可以正常播放

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
https://source.0515you.com/dszclszy.mp4空间名称web-xuweiqing存储区域华东-浙江

### 客服解答内容
**客户**：https://source.0515you.com/dszclszy.mp4空间名称web-xuweiqing存储区域华东-浙江

**客户**：刚看了下 ，这个空间里好多视频放不起来

**客服**：稍等这边看下

**客服**：这边测试看正常访问的，您有无法访问的报错信息提供一下吗

**客户**：目前好像好了

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 85: 一直卡在免费证书申请中

**分类标签**: CDN｜配置问题

### 详细问题描述
[    [        {            "title": "请求 ID",            "content": "CVE8EsAcPOR6wQAY, CVE8EsAcPOR6wQAY, CVE8EsAcPOR6wQAY, CVE8EsAcPOR6wQAY"        },        {            "title": "日志栈",            "content": "fusiondomain_cud:3/400;APIS:46/400;PORTAL-PROXY:88/400"        }    ]]

### 客服解答内容
**客户**：[    [        {            "title": "请求 ID",            "content": "CVE8EsAcPOR6wQAY, CVE8EsAcPOR6wQAY, CVE8EsAcPOR6wQAY, CVE8EsAcPOR6wQAY"        },        {            "title": "日志栈",            "content": "fusiondomain_cud:3/400;APIS:46/400;PORTAL-PROXY:88/400"        }    ]]

**客服**：稍等这边看下

**客户**：这个域名添加错了，我要添加到另一个七牛云帐号里

**客服**：纯海外域名国内访问慢是预期内的

**客服**：您需要国内国外都正常访问，就设置为全球覆盖哈

**客服**：添加错了您可以删除，去另一个账号重新添加

**客服**：域名添加错了您可以删除后在另一个账号重新添加哈，需要给您回滚任务您删除域名重新添加吗

**客户**：现在是我点删除就卡在这里了

**客户**：域名管理界面看到是处理中（删除域名处理中），点域名进入子页面就提示：删除域名处理中，免费证书申请耗时相对较长，平均 15 分钟完成，期间域名访问不受影响，部分配置不可修改，若长时间未配置完成，请提交工单反馈

**客服**：好的这边看下

**客服**：删除成功了您再看下

**客户**：但是另一个账号添加这个域名的时候提示：“域名冲突，该域名在其他账号被创建过或被某个泛域名覆盖。如果需要找回该域名，可点击找回”

**客户**：配置好 TXT 记录点击找回 -> 重新验证，提示：“[400129] 未知错误，请创建工单获取帮助”

**客户**：[    [        {            "title": "请求 ID",            "content": "qw6kP6DACxcaxAAY, qw6kP6DACxcaxAAY, qw6kP6DACxcaxAAY, qw6kP6DACxcaxAAY"        },        {            "title": "日志栈",            "content": "fusiondomain_cud:9/400;APIS:21/400;PORTAL-PROXY:84/400"        }    ]]

**客服**：您这边删除域名后需要清理相关配置的哈比如解析什么都要删除

### 根本原因分析
域名所有权验证未通过或DNS记录配置错误

---

## 问题 86: 资源访问下载问题

**分类标签**: CDN｜访问下载

### 详细问题描述
https://cdn.funstar6688.com/ScrewStory/Android/story_11_assets_all_32ad9a009606a567629ed76eecc7e878.bundle上述链接为七牛云资源中心洛杉矶站点。国内访问资源下载速度极慢，其他资源不知道是不是因为文件大小而引起的下载过忙导致。

### 客服解答内容
**客户**：https://cdn.funstar6688.com/ScrewStory/Android/story_11_assets_all_32ad9a009606a567629ed76eecc7e878.bundle上述链接为七牛云资源中心洛杉矶站点。国内访问资源下载速度极慢，其他资源不知道是不是因为文件大小而引起的下载过忙导致。

**客服**：稍等这边看下

**客服**：纯海外域名国内访问慢是预期内的吗，您需要国内国外都正常访问，就设置为全球覆盖哈

**客户**：这个可以改全球么

**客户**：该全球需要域名备案啊？

**客户**：这个跟文件大小有关系吗？同一个域名 1-4M内的访问正常，10M以上就开始慢下来了。

**客服**：是的需要备案的

**客户**：这个跟文件大小有关系吗？同一个域名 1-4M内的访问正常，10M以上就开始慢下来了

**客服**：您如果未备案域名只能设置为海外覆盖，国内访问情况无法保证，访问慢访问卡顿都是符合预期的，和图片大小无关

**客户**：好的 明白了。

**客服**：嗯嗯

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 87: 如何知道哪个是七牛回源的ip，有列表吗？

**分类标签**: CDN｜访问下载

### 详细问题描述
如何知道哪个是七牛回源的ip

### 客服解答内容
**客户**：如何知道哪个是七牛回源的ip

**客服**：您说的回源ip是指？

**客户**：举个例子：用户先访问七牛，如果七牛上面没有该文件七牛放回我们的服务器获取该文件，总是有很多恶意的请求所以我们想识别下哪个是七牛的请求加入白名单中。

**客服**：您可以直接设置回源鉴权哈

**客服**：回源鉴权，这个你们可以尝试下，每次访问cdn图片时，会携带你们自己定义的访问参数去你们自己的服务器上鉴权，只有你们服务器鉴权通过，返回 httpcode=200 ，才会将图片资源给用户访问，否则无法返回图片参考文档：https://developer.qiniu.com/fusion/4960/access-control-configuration

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 88: cdn更换ssl证书

**分类标签**: CDN｜配置问题

### 详细问题描述
更换ssl证书卡住了

### 客服解答内容
**客户**：更换ssl证书卡住了[图片]

**客服**：您好，请稍等

**客服**：您好，久等，已处理完成

### 根本原因分析
SSL证书申请、验证或部署流程问题

---

## 问题 89: 请帮忙快速处理域名

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
请帮忙快速处理域名

### 客服解答内容
**客户**：请帮忙快速处理域名

**客服**：域名提供一下

**客户**：img.3rcd.comassets.3rcd.com

**客服**：好的稍等这边看下

**客服**：assets.3rcd.com这个好了哈，另一个还在处理中，有结果同步给您

**客服**：处理完毕了您看下

**客户**：谢谢

**客服**：您客气了

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 90: 图片打开不

**分类标签**: 对象存储｜上传下载

### 详细问题描述
https://pengyouquan.dgydwlkj.com/uploads/20241022/81a89c9c977c226c2bfc3be8df08bd91.jpeg

### 客服解答内容
**客户**：https://pengyouquan.dgydwlkj.com/uploads/20241022/81a89c9c977c226c2bfc3be8df08bd91.jpeg

**客服**：您好，当您将空间设置成私有时，必须获得授权，才能对空间内的资源进行访问。您试一下这样访问呢：http://pengyouquan.dgydwlkj.com/uploads/20241022/[REDACTED_KEY].jpeg?e=1729600281&token=[REDACTED] GET的方式访问特定的 URL。私有资源URL与公开资源URL相比只是增加了两个参数e和token，分别表示过期时间和下载凭证。一个完整的私有资源 URL 如下所示：http://<domain>/<key>?e=<deadline>&token=[REDACTED]
参数e表示 URL 的过期时间，采用Unix时间戳，单位为秒。超时的访问将返回 401 错误。参数token表示下载凭证。下载凭证是对资源访问的授权，不带下载凭证或下载凭证不合法都会导致 401 错误，表示验证失败。注意：如果请求方的时钟未校准，可能会造成有效期验证不正常，例如直接认为已过期。因此需要进行时钟校准。由于开发者无法保证客户端的时间都校准，所以应该在业务服务器上创建时间戳，并周期性校准业务服务器时钟。文档链接：https://developer.qiniu.com/kodo/1656/download-private

**客户**：好的

**客服**：嗯嗯

**客户**：cnd加速可以降低配置吗

**客户**：cdn

**客户**：跑的有猛   十几分钟跑几个十个G

**客服**：您说的降低配置是指？

**客服**：您是说流量消耗大的话，可以通过访问控制来限制流量

**客服**：您好，防止别人恶意访问你的资源产生大量流量，单纯的从cdn的层面上来处理，是不能完全规避掉的。CDN上支持多种防盗链配置，不同的防盗链适用于不同的应用场景，建议可以在cdn => 域名管理 => 配置 => 访问控制 中设置1：referer防盗链： 只有携带了相应referer 请求头 的 http请求才能访问资源，但是对于技术来说，referer都是可以伪造的，存在一定的风险2：时间戳防盗链，url带着e和token参数访问，e为过期时间，但是只要捕获到了url就可以访问资源了，只适用于访问xx次的场景3：回源鉴权，这个你们可以尝试下，每次访问cdn图片时，会携带你们自己定义的访问参数去你们自己的服务器上鉴权，只有你们服务器鉴权通过，返回 httpcode=200 ，才会将图片资源给用户访问，否则无法返回图片4：IP黑白名单，这个适合某一个网段内的ip访问资源，不适合官网使用，只有在 ip 白名单中的用户才可以访问你们的图片参考文档：https://developer.qiniu.com/fusion/4960/access-control-configuration☆推荐使用第三种回源鉴权和第四种IP黑白名单进行访问限制。

**客服**：您也可以在 控制台 - cdn - 统计分析 - 日志分析 中看到您的top访问情况，比如高频访问的URL和客户端IP。不符合预期的可以删除/拉黑https://portal.qiniu.com/cdn/statistics/log/top

**客户**：都是正常访问的我只想不要那么快

**客服**：您流量产生和访问速度非正比关系，如果您是因为流量增高想要降低访问速度可能效果没有那么明显哈

**客服**：您确认一下目前需要解决的问题是流量高还是访问太快

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 91: 权限验证

**分类标签**: 直播云｜推流问题

### 详细问题描述
苹果获取推流地址。报错Pili-Streaming stream authentication status is PLAuthenticationResultDenied! -[PLStreamingSession

### 客服解答内容
**客户**：苹果获取推流地址。报错Pili-Streaming stream authentication status is PLAuthenticationResultDenied! -[PLStreamingSession

**客服**：不好意思，目前非正式工作时间，相关工作人员不在线，最迟明天上午给您回复您看可以吗

**客服**：app 包名是什么？

**客户**：com.onekeysolution.app

**客服**：包名没有授权 上一个工单里您给的联系方式 商务同步多次联系您电话拒接 推流需要授权后使用

**客户**：已经联系说了， 授权好了

**客服**：现在推流还报错吗？应用卸载重装一下

**客户**：这个是苹果的， com.oks.oks。 我以为苹果和Android是一样的

**客户**：企业账号  一掌控（上海）互联网科技有限公司

**客服**：现在是要对 com.oks.oks 添加推流授权处理吗

**客户**：是的，

**客服**：这边同步商务对接处理 请保持电话通畅

**客服**：com.oks.oks 已经授权

**客户**：苹果有没有做好的demo参考一下。 最好是成品。

**客服**：iOS Demo 下载：（若使用微信扫码失败，可使用苹果手机自带相机、QQ、支付宝尝试扫码）[图片]

**客户**：有源码吗？

**客户**：扫描上面二维码， 没有测试权限不能下载

**客服**：稍等

**客服**：demo可以使用github上的源码安装一下 https://github.com/pili-engineering/PLMediaStreamingKit   目前扫码无法安装

**客户**：好的

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 92: 空间名称为：morteng ，mortengen，sem-no1 的这3个空间帮删除下

**分类标签**: 对象存储｜上传下载

### 详细问题描述
空间管理中的空间名称为：morteng ，mortengen，sem-no1 的这3个空间帮删除下，我删除不了，谢谢

### 客服解答内容
**客户**：空间管理中的空间名称为：morteng ，mortengen，sem-no1 的这3个空间帮删除下，我删除不了，谢谢

**客服**：您空间文件清理了嘛

**客户**：这几个空间文件清理不掉

**客服**：稍等这边看下

**客服**：您好，删除文件属于高危操作，空间删除后，文件将无法恢复，请您慎重操作。如果您确认需要由我们操作本次空间删除，您可以留下联系方式，这边安排商务经理明天联系和您确认下，确认无误后，将由商务经理帮您发起删除申请。

**客户**：[REDACTED_PHONE] 詹先生

**客服**：好的，明天商务同事上班会联系您，还请您耐心等待一下

**客户**：另外域名管理中的这个域名帮我删除下，cms1.sem-no1.com

**客服**：好的稍等

**客服**：可以了看下

**客服**：您好，已帮您开启非空删除，您现在删除试试

**客户**：空间名称为：morteng ，mortengen，sem-no1 的这3个空间里的文件夹删除了还是存在

**客服**：您好，你们直接删除空间，你们是怎么删除的呢

### 根本原因分析
资源删除流程或权限配置问题

---

## 问题 93: 上传的图片不能正常访问

**分类标签**: CDN｜其他类咨询

### 详细问题描述
图片上传后 不能通过绑定的域名访问到图片，打开速度特别慢

### 客服解答内容
**客户**：图片上传后 不能通过绑定的域名访问到图片，打开速度特别慢

**客服**：图片链接提供一下

**客户**：https://bdyhres.hanhoukeji.cn/2[REDACTED_LANDLINE]4fbd3a9722.png

**客服**：这边测试看可以正常访问，您无法访问的报错是什么

**客户**：浏览器一直在加载中 超时后提示加载失败，页面空白或是显示一小部分[图片]

**客户**：可以用了

### 根本原因分析
上传超时时间设置过短或网络环境不稳定

---

## 问题 94: 上传后找不到文件

**分类标签**: 对象存储｜上传下载

### 详细问题描述
filekey是这个：/qinui/matchmaking/2024_10_22/[REDACTED_PHONE]08/20241017-111533.jpg通过sdk上传成功后通过在oig-test-img桶中找不到该文件

### 客服解答内容
**客户**：filekey是这个：/qinui/matchmaking/2024_10_22/[REDACTED_PHONE]08/20241017-111533.jpg通过sdk上传成功后通过在oig-test-img桶中找不到该文件

**客服**：稍等这边看下

**客户**：好的，我看下午16：00多的时候 oig-test-img下还能看到 ：/qinui/matchmaking/2024_10_22 这个目录下有上传的文件

**客服**：http://qiniu-test.worldrou.com//qinui/matchmaking/2024_10_22/[REDACTED_PHONE]08/20241017-111533.jpg

**客服**：上传成功的哈，您看下，在您的存储空间中

**客户**：好的

### 根本原因分析
上传接口配置、权限或网络问题

---

## 问题 95: 添加域名提示域名冲突

**分类标签**: CDN｜配置问题

### 详细问题描述
添加域名提示："域名冲突，该域名在其他账号被创建过或被某个泛域名覆盖。如果需要找回该域名，可点击找回"

### 客服解答内容
**客户**：添加域名提示："域名冲突，该域名在其他账号被创建过或被某个泛域名覆盖。如果需要找回该域名，可点击找回"

**客服**：稍等这边看下

**客服**：您现在再试一下呢

**客户**：还是一样的提示[图片]

**客服**：您在域名申请厂商处的解析是否删除，您检查一下

**客户**：已经删除了有半个小时多了

**客服**：您好，这边操作一下域名找回试试呢，域名找回操作有两种：1.系统自动找回，参考图文操作文档：https://developer.qiniu.com/fusion/manual/5857/the-domain-name-back2.人工找回，需要您设置一个 TXT 解析验证，然后提交给我们确认后，我们手动帮您过户到当前账号，验证配置如下主机记录 qn-verification
记录类型 TXT
记录值  cWluaXUtMjAyNDEwMjItMTM4MzAzMzQ1Mgo=
注意：每月1-3号为出账期，不支持域名过户。

**客户**：这个 qn-verification的TXT记录添加好了

**客服**：好的稍等

**客服**：可以了您试下

**客户**：可以了

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 96: 新加坡空间有问题，无法通过绑定的域名访问图片

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
绑定新域名后，无法通过域名访问图片https://assets.3rcd.com/media/[REDACTED_ID_CARD].jpg而用自带的域名可以访问http://slqzhe4d0.sabkt.gdipper.com/media/[REDACTED_ID_CARD].jpg

### 客服解答内容
**客户**：绑定新域名后，无法通过域名访问图片https://assets.3rcd.com/media/[REDACTED_ID_CARD].jpg而用自带的域名可以访问http://slqzhe4d0.sabkt.gdipper.com/media/[REDACTED_ID_CARD].jpg

**客服**：稍等这边看下

**客服**：这边看是证书未正常下发导致，后端反馈当前平台有升级，暂停下发，预计22点从新开始下发，22.30完成，还请再耐心等待一下

**客户**：仍然打不开。。。

**客服**：还未处理完成 我再跟进下哈

**客服**：可以了您再看下

**客户**：还是不行

**客户**：666，一直卡在那边打不开，不信你可以试试

**客服**：我这边测试是可以打开但是访问速度很慢，因为您这个是纯海外域名，国内访问慢是预期内的，需要提升国内访问速度建议将域名修改为全球覆盖或者大陆覆盖

**客户**：我的域名是dnspod买的，不是海外域名，。。。

**客户**：只是没备案而已

**客户**：可以看到顶级域名的网站 3rcd.com 是秒开的

**客户**：cdn是好的[图片]

**客户**：已确认，是新加坡节点的问题，因为我用 img.3rcd.com 又绑定了一个美国空间，可以正常打开https://img.3rcd.com/media[REDACTED_ID_CARD].png速度是正常的美国服务器速度，而新加坡是火星的速度了。。。

**客服**：这个域名您选择的是海外加速覆盖 国内访问慢是符合预期的

**客服**：自 2020年10月20日起，控制台 -【域名管理】目前已支持域名覆盖区域（中国大陆、全球、海外）切换，您可以在[图片]点击『修改』自助切换。

**客户**：由于没备案，只能选择海外[图片]

**客服**：海外加速覆盖是只在海外地区有加速效果的分配的也是海外的加速节点  您现在是在国内访问慢 还是在海外地区访问慢

**客户**：都慢，目前美国节点正常，先用着了

**客服**：好的 您再观察下

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 97: 存储时间

**分类标签**: 对象存储｜上传下载

### 详细问题描述
申请的外链使用有时间限制，时间一过就用不了了

### 客服解答内容
**客户**：申请的外链使用有时间限制，时间一过就用不了了

**客服**：您好，当您将空间设置成私有时，必须获得授权，才能对空间内的资源进行访问。私有资源下载是通过HTTP GET的方式访问特定的 URL。私有资源URL与公开资源URL相比只是增加了两个参数e和token，分别表示过期时间和下载凭证。一个完整的私有资源 URL 如下所示：http://<domain>/<key>?e=<deadline>&token=[REDACTED]
参数e表示 URL 的过期时间，采用Unix时间戳，单位为秒。超时的访问将返回 401 错误。参数token表示下载凭证。下载凭证是对资源访问的授权，不带下载凭证或下载凭证不合法都会导致 401 错误，表示验证失败。注意：如果请求方的时钟未校准，可能会造成有效期验证不正常，例如直接认为已过期。因此需要进行时钟校准。由于开发者无法保证客户端的时间都校准，所以应该在业务服务器上创建时间戳，并周期性校准业务服务器时钟。文档链接：https://developer.qiniu.com/kodo/1656/download-private

**客服**：如果想要不受限建议设置为公开的空间

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 98: 删除域名等了快2个小时了还没删完

**分类标签**: CDN｜配置问题

### 详细问题描述
删除域名等了快2个小时了还没删完

### 客服解答内容
**客户**：删除域名等了快2个小时了还没删完

**客服**：稍等这边看下

**客服**：可以了您看下

### 根本原因分析
资源删除流程或权限配置问题

---

## 问题 99: 创建域名处理中

**分类标签**: CDN｜配置问题

### 详细问题描述
域名处理时间长

### 客服解答内容
**客户**：域名处理时间长

**客服**：稍等这边看下

**客服**：可以了您看下哈

**客户**：嗯，是可以。我可以问一下什么原因导致的吗？之前好像也会这样

**客服**：域名配置后台卡住，需要人工介入

**客户**：好的 谢谢

### 根本原因分析
系统配置任务处于处理队列中，需要手动介入加速处理流程

---

## 问题 100: 需要继续使用测试域名

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
没有加速域名可以转，加速域名需要备案是什么意思

### 客服解答内容
**客户**：没有加速域名可以转，加速域名需要备案是什么意思

**客服**：测试域名是七牛提供用于功能测试的域名，请勿用于线上生产环境，同时，测试域名仅有30天的生命周期，到期后会进行自动回收。我们会在回收前一周和回收当天向您发送回收告知邮件，您可以确认邮箱中的邮件核实具体回收时间。解决方法：回收测试域名对您的存储资源没有影响，不会删除您的资源，也不需要重新上传资源。您绑定自定义域名后，通过自定义域名访问即可。如果您的域名已经在工信部备案，请参考域名绑定教程：https://developer.qiniu.com/kodo/kb/5158/how-to-transition-from-test-domain-name-to-a-custom-domain-name如果您需要了解测试域名的使用规范请参考：https://developer.qiniu.com/fusion/kb/1319/test-domain-access-restriction-rules

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 101: 云图片又加载不出来了，如果隔三差五这样的话，体验就真的差了

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
云图片又加载不出来了，如果隔三差五这样的话，体验就真的差了

### 客服解答内容
**客户**：云图片又加载不出来了，如果隔三差五这样的话，体验就真的差了

**客服**：图片链接提供一下

**客户**：https://www.kaicz.com/sucai/18502.html

**客户**：https://img.kaicz.com/img/2022/08/11/1660201906.jpeg?imageView2/2/w/250/q/90/interlace/1/format/webp

**客服**：[图片]

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 102: 修改IP黑名单，一直处理中

**分类标签**: CDN｜配置问题

### 详细问题描述
修改IP黑名单，又是一直处理中bbs.ybvv.comwww.ybvv.com

### 客服解答内容
**客户**：修改IP黑名单，又是一直处理中bbs.ybvv.comwww.ybvv.com

**客服**：稍等这边看下

**客服**：可以了您看下

### 根本原因分析
系统配置任务处于处理队列中，需要手动介入加速处理流程

---

## 问题 103: xiaokechuang对象存储空间自定义域名

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
ycc.52fuyang.top对象存储怎么修改回源协议为https，证书我已经配置好了强制ssl，但是域名配置到对象存储后回源协议貌似不能改了，能否帮我改下回源https

### 客服解答内容
**客户**：ycc.52fuyang.top对象存储怎么修改回源协议为https，证书我已经配置好了强制ssl，但是域名配置到对象存储后回源协议貌似不能改了，能否帮我改下回源https

**客服**：稍等这边看下

**客户**：这里[图片]

**客服**：您要修改为https是吧

**客户**：是的

**客户**：我这里好像没法修改

**客服**：好的这边确认下能否帮您修改哈

**客户**：可以修改吗，如果可以修改的话麻烦直接帮我改了

**客服**：还在内部确认哈，有结果给您同步

**客服**：这边确认了，您用的源站用的存储，回源协议都是http无法修改的如果要用https，需要您设置自定义源站，才可以修改回源协议

**客户**：我把这个域名删除了ycc.52fuyang.top，一直还是删除中，麻烦看一下

**客服**：稍等这边看下

**客服**：可以了您看下

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 104: 为什么上传自己的域名证书就老出错？

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
[    [        {            "title": "请求 ID",            "content": "HLwROv9Xs5mgyQAY"        },        {            "title": "日志栈",            "content": "fusionsslcert/400"        }    ],    [        {            "title": "请求 ID",            "content": "GHK2AdOsZC2hyQAY"        },        {            "title": "日志栈",            "content": "fusionsslcert/400"        }    ]]我的秘钥：[REDACTED_PRIVATE_KEY]证书：[REDACTED_CERTIFICATE][REDACTED_CERTIFICATE]

### 客服解答内容
**客户**：[    [        {            "title": "请求 ID",            "content": "HLwROv9Xs5mgyQAY"        },        {            "title": "日志栈",            "content": "fusionsslcert/400"        }    ],    [        {            "title": "请求 ID",            "content": "GHK2AdOsZC2hyQAY"        },        {            "title": "日志栈",            "content": "fusionsslcert/400"        }    ]]我的秘钥：[REDACTED_PRIVATE_KEY]证书：[REDACTED_CERTIFICATE][REDACTED_CERTIFICATE]

**客户**：帮忙给上传一下

**客服**：您好，检查一下是否按如下步骤操作1、建议您在证书厂商下载证书时，选择 Nginx 服务器类型的证书文件2、进入七牛云管理控制台：https://portal.qiniu.com/certificate/ssl，点击 【上传自有证书】3、使用编辑器打开后续文件，并复制 .crt 或者 .pem 后缀的文件内容到证书内容 （公钥），复制 .key 后缀结尾的内容到 证书私钥 。[图片]如果需要把域名升级为 HTTPS 或者修改证书 的话，需要按照以下步骤绑定证书即可：https://developer.qiniu.com/fusion/manual/4952/https-configuration

### 根本原因分析
SSL证书申请、验证或部署流程问题

---

## 问题 105: uploadFile:fail 小程序要求的 TLS 版本必须大于等于 1.2

**分类标签**: 对象存储｜SDK使用

### 详细问题描述
小程序使用 @qiniu/wechat-miniprogram-upload 的 createDirectUploadTask  上传图片出现错误：uploadFile:fail 小程序要求的 TLS 版本必须大于等于 1.2请求域名为：https://upload-z2.qiniup.com

### 客服解答内容
**客户**：小程序使用 @qiniu/wechat-miniprogram-upload 的 createDirectUploadTask  上传图片出现错误：uploadFile:fail 小程序要求的 TLS 版本必须大于等于 1.2请求域名为：https://upload-z2.qiniup.com[图片]

**客服**：小程序域名提供一下

**客服**：您是要设置域名cdn.virtual7.ren支持只支持tls1.2及以上版本吗

**客户**：或许不是小程序域名的问题，可能是@qiniu/wechat-miniprogram-upload 包的问题，这个问题一时有一时没有

**客服**：您好wechat-miniprogram-upload 这个不是我们官方的SDK，您在该SDK提供方那边看下是否有类似问题和解决方案？或者也可以尝试引入我们的js SDK：https://developer.qiniu.com/kodo/1283/javascript

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 106: 显示8-15分钟，现在还没搞定

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
一直卡在这里

### 客服解答内容
**客户**：[图片]一直卡在这里

**客服**：稍等这边看下

**客服**：可以了您看下

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 107: 域名「gary-fivem.cc」测试未通过

**分类标签**: CDN｜配置问题

### 详细问题描述
是域名有问题吗?

### 客服解答内容
**客户**：是域名有问题吗?

**客服**：您好，请稍等，这边帮您确认下

**客服**：你好，你们是怎么配置的，麻烦您将您的具体配置复制出来提供下，这边帮您核实下

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 108: 域名升级 HTTPS 长时间未配置完成

**分类标签**: 对象存储｜其他类咨询

### 详细问题描述
好几个小时都没有配置完成

### 客服解答内容
**客户**：好几个小时都没有配置完成[图片]

**客服**：稍等

**客服**：抱歉久等了，配置已下发

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 109: 后台所有的mp4格式的视频突然不能播放了

**分类标签**: 智能多媒体｜音视频处理

### 详细问题描述
视频播放不了

### 客服解答内容
**客户**：视频播放不了

**客户**：上传的所有mp4链接都不能播放了

**客服**：您好，请稍等

**客服**：您好，你们这个域名的cname解析不对，你们确认下呢

**客服**：[图片]

**客户**：域名有没有解析要求

**客服**：您要将域名解析到我们这边才能正常使用的cname配置方式https://developer.qiniu.com/fusion/4941/cname-configuration

### 根本原因分析
具体问题需根据日志和配置进一步排查分析

---

## 问题 110: 无法备案

**分类标签**: 云主机｜主机

### 详细问题描述
就是在这里面继续填写这里点出来的，下一步就提交不了下一步

### 客服解答内容
**客户**：[图片]就是在这里面继续填写这里点出来的，下一步就提交不了下一步

**客服**：您好，第一次在我们这边提交吗，有在阿里那边提交过吗，备案系统是和阿里合作的，数据同步的。

### 根本原因分析
域名ICP备案未完成或备案信息未同步到工信部系统

---

## 问题 111: 无法提交备案  说有进行中，

**分类标签**: 云主机｜主机

### 详细问题描述
无法提交备案  说有进行中

### 客服解答内容
**客户**：无法提交备案  说有进行中

**客服**：您好给下相关截图 这边看下

### 根本原因分析
域名ICP备案未完成或备案信息未同步到工信部系统

---

## 问题 112: 我的域名进行了app备案，为什么无法添加绑定？

**分类标签**: CDN｜配置问题

### 详细问题描述
无法添加绑定，提示域名没有备案，但是我在阿里云已经备案好了，如下图所示

### 客服解答内容
**客户**：无法添加绑定，提示域名没有备案，但是我在阿里云已经备案好了，如下图所示[图片]

**客服**：您好，您这边创建的是主域名吗？创建的时候报错是什么？创建CDN域名吗？

**客户**：无论是主域名还是子域名都是报错[图片][图片]

**客服**：您这边什么时候完成的备案的呢？目前工信部暂未查询到您的备案的，这边是以工信部为准的[图片]

**客户**：WOSHIZAI [图片]

**客户**：我是在阿里云里面申请备案的，时间是2个月前

**客服**：您好，建议您这先咨询一下阿里这边，问下他们为什么该域名的备案在工信部查不到的

**客户**：好吧

### 根本原因分析
域名ICP备案未完成或备案信息未同步到工信部系统

---

## 问题 113: 视频观看卡顿，请技术人员配合查询及修复或者修改下cdn配置

**分类标签**: CDN｜配置问题

### 详细问题描述
https://xz.vo88.top/yzd_kp/uniacid6/u0/video/2024/10/2/[REDACTED_PHONE]19357535.mp4其中一个视频地址

### 客服解答内容
**客户**：https://xz.vo88.top/yzd_kp/uniacid6/u0/video/2024/10/2/[REDACTED_PHONE]19357535.mp4其中一个视频地址

**客服**：您好，1、麻烦提供下您的 ip、dns 信息，和cdn节点信息，这边代理测试下可以通过访问这个链接 http://ping.huatuo.qq.com/ 获取本地的 ip 和 dns 信息，在检测域名这边输入下cdn域名，点击提交检测，然后截图通过工单提交给我们[图片]2、建议使用 chrome 浏览器，按照下述文档获取下 remote adress(对端节点ip)，request header(客户端请求头) 以及 response header(服务端响应头)信息，方便我们查询分析问题。https://developer.qiniu.com/fusion/kb/1478/how-to-access-network-in-the-browser-request-information

**客户**：视频看一段就卡 看一段就卡 可能是自己场景选择的图片/小文件的原因，想要后台给他改成“视频点播”场景试下效果辛苦技术后台帮更改下

**客服**：好的 请稍等

**客服**：已经切换完成 可以再看下

### 根本原因分析
CDN节点性能、网络带宽或路由优化问题

---

## 问题 114: 无法进行备案   点了继续填写，然后无法点下一步说有订单进行中   ，我根本就没有在别的地方去备案过，根本就没有订单，

**分类标签**: 云主机｜其他类咨询

### 详细问题描述
无法进行备案   点了继续填写，然后无法点下一步说有订单进行中   ，我根本就没有在别的地方去备案过，根本就没有订单，

### 客服解答内容
**客户**：无法进行备案   点了继续填写，然后无法点下一步说有订单进行中   ，我根本就没有在别的地方去备案过，根本就没有订单，

**客服**：您好，您这边域名是再哪家购买的呢？您这看下到您的域名的厂商是哪家无法备案的截图给一下这边看下报错

### 根本原因分析
域名ICP备案未完成或备案信息未同步到工信部系统

---


