# 七牛云技术支持工单数据集 - Part 9

本文档包含经过处理和脱敏的客户服务工单数据，用于技术支持知识库建设。

---

## 1. 个体工商户可以认证为企业用户吗

**问题分类**: 云短信｜其他类咨询

### 问题描述

个体工商户可以认证为企业用户吗

### 客服解答

**客户**：个体工商户可以认证为企业用户吗
**客服**：您好您那边要做什么 目前看您的当前账号已经是企业认证了
**客户**：我帮别人问问
**客服**：参考 [URL已脱敏] 这三种方式都可以做企业认证处理
**客户**：那个体工商户有营业执照可以认证企业用户吗
**客服**：有社会信用代码认证，营业执照号认证，非盈利组织认证这些可以 除此之外不能
**客服**：有社会信用代码 营业执照号 这些可以 除此之外不能
**客户**：好的，感谢

### 根本原因分析

企业认证需要提供社会信用代码或营业执照号

---

## 2. putExtra.resumeRecordFile = 'progress.log';

**问题分类**: 对象存储｜上传下载

### 问题描述

putExtra.resumeRecordFile = 'progress.log';上传的这个文件存在的形式是怎么样的 ，目录还是只是这个名称

### 客服解答

**客户**：putExtra.resumeRecordFile = 'progress.log';上传的这个文件存在的形式是怎么样的 ，目录还是只是这个名称
**客服**：您好存储的是文件名称，控制台的目录实际是虚拟目录，是基于文件名的路径自动扩展出来的虚拟文件夹，实际不存在
**客户**：const resumeUploader = new qiniu.resume_up.ResumeUploader(config);const putExtra = new qiniu.resume_up.PutExtra();const readableStream = xxx; // 可读的流const readableStreamLen = xxx; // 可读流长度// 如果指定了断点记录文件，那么下次会从指定的该文件尝试读取上次上传的进度，以实现断点续传putExtra.resumeRecordFile = 'progress.log';// 分片上传可指定 version 字段，v2 表示分片上传 v2putExtra.version = 'v2'// 当使用分片上传 v2 时，默认分片大小为 4MB，也可自定义分片大小，单位为 Bytes。例如设置为 6MB// putExtra.partSize = 6 * 1024 * 1024resumeUploader.putStream(    uploadToken,    key,    readableStream,    readableStreamLen,    putExtra,)    .then(({ data, resp }) => {        if (resp.statusCode === 200) {            console.log(data);        } else {            console.log(resp.statusCode);            console.log(data);        }    })    .catch(err => {        console.log('failed', err);    });
**客户**：putExtra.resumeRecordFile = 'progress.log';也就是说这个文件其实是不需要去创建的么
**客服**：上传文件指定一下key 不指定生成的文件名称是一个hash值
**客户**：为啥回丢包
**客服**：用哪种语言上传的  这边给您找个demo测试下
**客户**：nodejs
**客户**：100kb一下的 小文件 没有丢包，超过100多的基本多多少少都会丢点包
**客服**：您好，npm install qiniu --save 安装qiniu-model，引入qiniuconst qiniu = require("qiniu")调用uploadToken 生成上传tokenlet uploadToken = putPolicy.uploadToken(mac);简单上传参考这里[URL已脱敏]
**客户**：export const uploadToQiniu = async (filePath, key) => {    const [密钥已脱敏] = QNConfig.[密钥已脱敏];    const [密钥已脱敏] = QNConfig.[密钥已脱敏];    const mac = new qiniu.auth.digest.Mac([密钥已脱敏], [密钥已脱敏]);    const options = {        scope: QNConfig.bucket,    };    const putPolicy = new qiniu.rs.PutPolicy(options);    const uploadToken = putPolicy.uploadToken(mac);    const config = new qiniu.conf.Config();    config.regionsProvider = qiniu.httpc.Region.fromRegionId("z2");    const localFile = filePath;    const formUploader = new qiniu.form_up.FormUploader(config);    const putExtra = new qiniu.form_up.PutExtra();    putExtra.resumeRecordFile = "progress.log";    putExtra.version = "v2";    // 文件上传    return new Promise((resolved, reject) => {        formUploader.putStream(uploadToken, key, localFile, putExtra, function (respErr, respBody, respInfo) {            if (respErr) {                reject(respErr);            } else {                resolved(respBody);            }        });    });};这个是我封装的
**客服**：先用我们的demo测试看下是否正常
**客户**：const uploadToken = putPolicy.uploadToken(mac);const config = new qiniu.conf.Config();const localFile = os.homedir() + '[密钥已脱敏].css';// config.zone = qiniu.zone.Zone_z0;const formUploader = new qiniu.form_up.FormUploader(config);const putExtra = new qiniu.form_up.PutExtra();// file// putExtra.fname = 'frontend-static-resource/widgets/_[密钥已脱敏].css';// putExtra.metadata = {//     'x-qn-meta-name': 'qiniu'// };formUploader.putFile(    uploadToken,    'frontend-static-resource/widgets/_[密钥已脱敏].css',    localFile,    putExtra)    .then(({ data, resp }) => {        if (resp.statusCode === 200) {            console.log(data);        } else {            console.log(resp.statusCode);            console.log(data);        }    })    .catch(err => {        console.log('put failed', err);    });
**客户**：'frontend-static-resource/widgets/_[密钥已脱敏].css'这一串是什么
**客户**：key 么
**客服**：上传后的key
**客户**：不太明白
**客服**：就是上传后的文件名
**客户**：这个不会丢包了，为撒putStream 就会丢包
**客服**：检查一下上行网络状态
**客户**：那为啥这个不丢包 不都是一样的么，只是一个是流，一个是file 文件
**客户**：好吧，一个是持续的，一个一次性的 ，估计是网络波动吧
**客服**：网络波动会影响上传效果 您可以再观察下

### 根本原因分析

网络波动导致上传不稳定，建议使用断点续传功能

---

## 3. 充值忘记写备注了怎么办？

**问题分类**: 账户与财务｜计费问题

### 问题描述

今天用 北京易动纷享科技有限责任公司 主体充值了1000元，充值忘记备注帐号了怎么办？

### 客服解答

**客户**：今天用 北京易动纷享科技有限责任公司 主体充值了1000元，充值忘记备注帐号了怎么办？
**客服**：您好，您这边提供下充值回单

### 根本原因分析

充值时未填写备注信息，需要提供充值回单进行人工处理

---

## 4. 对象存储上线新区域 西北-陕西1，立即申请使用。

**问题分类**: 对象存储｜上传下载

### 问题描述

为何一直审核无果呢？

### 客服解答

**客户**：为何一直审核无果呢？
**客服**：您好，目前还暂时处于搜集需求阶段的，目前还无法开通的，还请耐心等待后续开通的

### 根本原因分析

具体问题需要根据实际场景分析

---

## 5. 删除云上的图片后，用地址仍然能够访问

**问题分类**: 对象存储｜其他类咨询

### 问题描述

@Testpublic void qiniuDelTest(){    QiNiuConfiguration qiNiuConfiguration = SpringUtil.getBean(QiNiuConfiguration.class);    Configuration cfg = new Configuration(Region.region0());    String [密钥已脱敏] = qiNiuConfiguration.get[密钥已脱敏]();    String [密钥已脱敏] = qiNiuConfiguration.get[密钥已脱敏]();    String bucket = "hx-qrcode-dev";    //[URL已脱敏]    String key = "[密钥已脱敏].png";   //七牛云中保存的文件名  Auth auth = Auth.create([密钥已脱敏], [密钥已脱敏]);    BucketManager bucketManager = new BucketManager(auth, cfg);    try {        bucketManager.delete(bucket, key);    } catch (QiniuException ex) {        //如果遇到异常，说明删除失败        System.err.println(ex.code());        System.err.println(ex.response.toString());    }}执行上述代码后，七牛云控制台中看到图片文件已经删除，但通过地址仍然能访问到图片，更换浏览器清除缓存后也可以打开图片，我希望删除图片后就不能通过地址访问了，该怎么做?

### 客服解答

**客户**：@Testpublic void qiniuDelTest(){    QiNiuConfiguration qiNiuConfiguration = SpringUtil.getBean(QiNiuConfiguration.class);    Configuration cfg = new Configuration(Region.region0());    String [密钥已脱敏] = qiNiuConfiguration.get[密钥已脱敏]();    String [密钥已脱敏] = qiNiuConfiguration.get[密钥已脱敏]();    String bucket = "hx-qrcode-dev";    //[URL已脱敏]    String key = "[密钥已脱敏].png";   //七牛云中保存的文件名  Auth auth = Auth.create([密钥已脱敏], [密钥已脱敏]);    BucketManager bucketManager = new BucketManager(auth, cfg);    try {        bucketManager.delete(bucket, key);    } catch (QiniuException ex) {        //如果遇到异常，说明删除失败        System.err.println(ex.code());        System.err.println(ex.response.toString());    }}执行上述代码后，七牛云控制台中看到图片文件已经删除，但通过地址仍然能访问到图片，更换浏览器清除缓存后也可以打开图片，我希望删除图片后就不能通过地址访问了，该怎么做?
**客服**：您好，访问到的是这张图片在CDN节点的缓存。图片从源站删除之后，它的缓存仍然会在CDN节点保存，所以仍然可以访问到。您可以刷新下缓存：1.控制台>> 融合CDN>>刷新预取界面下刷新；2.可以调用接口:[URL已脱敏]

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 6. 视频误删怎么找回

**问题分类**: 对象存储｜其他类咨询

### 问题描述

视频误删怎么找回，

### 客服解答

**客户**：视频误删怎么找回，
**客服**：您好，很抱歉，已经删除的文件是无法恢复找回的

### 根本原因分析

具体问题需要根据实际场景分析

---

## 7. 定时推流

**问题分类**: 直播云｜推流问题

### 问题描述

问题如下图，在pub推流时，我设置的次日某点开始推送，保存后，是否还需要在2图界面上，打开开关？还是系统会自动在设置的时间点打开？

### 客服解答

**客户**：问题如下图，在pub推流时，我设置的次日某点开始推送，保存后，是否还需要在2图界面上，打开开关？还是系统会自动在设置的时间点打开？[图片][图片]
**客服**：您好，不需要点运行，点了就是马上启动的
**客户**：明白了，那就是我只要设置好定时开启就可以了对吧，系统会自动启动
**客户**：另外，关于CDN加速，我这边有个费用截图，但是我想知道这是那条加速域名产生的，如何查看？[图片]
**客服**：您好，down.631r.com和zhibo.631r.xyz，主要是down.631r.com可以在这边查看您的用量统计[URL已脱敏]
**客户**：收到谢谢

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 8. 账号很久不用了，余额退款问题

**问题分类**: 账户与财务｜其他类咨询

### 问题描述

账号 ID        1002142836240上海蓝指网络科技有限公司我们这边的七牛账号好多年已经没有使用了 现在上面还有99.64余额    麻烦帮忙退款处理需要提供什么材料？

### 客服解答

**客户**：账号 ID        1002142836240上海蓝指网络科技有限公司我们这边的七牛账号好多年已经没有使用了 现在上面还有99.64余额    麻烦帮忙退款处理需要提供什么材料？
**客服**：您好，目前已支持，自助申请原路提现(支付宝，微信，网上银行)，线下提现(银行卡)功能。提现入口链接：[URL已脱敏] 330 天）、支付宝充值（充值时间小于 330 天）、网上银行充值（充值时间小于 80 天）
**客户**：我们的余额  应该是2020年之前的    不支持线上退款了
**客户**：附件是截图[图片][图片]
**客服**：您好，麻烦辛苦给一下以下信息提现金额：提现原因：原充值所使用的银行卡或支付宝账号：-----此行在原微信充值情况可删除，提供附件信息收款账号，提供原充值实名信息一致的银行账号。------原支付宝充值时也需要，历史的充值 财务不一定能原路退成功。银行卡填写：收款户名、收款银行、收款账号附件 原微信充值需求：原微信支付的截图，以及支付使用的微信钱包的实名信息截图（需要与现在要求的退回账户一致）

### 根本原因分析

企业认证需要提供社会信用代码或营业执照号

---

## 9. 无法续签证书

**问题分类**: CDN｜证书问题

### 问题描述

申请证书确定按钮为灰色

### 客服解答

**客户**：申请证书确定按钮为灰色[图片]
**客服**：您好，点击强制https 试试

### 根本原因分析

SSL证书配置或过期问题

---

## 10. 通过sdk获取的token在调用资源包列表接口时一直报错401

**问题分类**: 对象存储｜SDK使用

### 问题描述

通过sdk获取的token在调用资源包列表接口时一直报错401url:[URL已脱敏] Qiniu [密钥已脱敏]-pZIDEGYAOIUrveZXq:8JQ5fY3_vauOChcJU1h6udf[密钥已脱敏]LA=:[密钥已脱敏]

### 客服解答

**客户**：通过sdk获取的token在调用资源包列表接口时一直报错401url:[URL已脱敏] Qiniu [密钥已脱敏]-pZIDEGYAOIUrveZXq:8JQ5fY3_vauOChcJU1h6udf[密钥已脱敏]LA=:[密钥已脱敏]
**客户**：通过sdk 的 String token = auth.uploadToken("hde2018"); 方式获取token 是这个获取的token方法不对嘛还是什么原因？
**客服**：您好，上传token只用于上传，你们用错了token ，试试这个@Test
public void sslGet() throws Exception {
    Auth auth = Auth.create(ACCESS_KEY, SECRET_KEY);
    // 获取签名
    String url = "[URL已脱敏]
    String accessToken = "Qiniu " + (String) auth.[密钥已脱敏](url,"GET",null, "application/x-www-form-urlencoded");
    Client client = new Client();
    StringMap headers = new StringMap();
    headers.put("Authorization", accessToken);
    try {
        com.qiniu.http.Response resp = client.get(url,headers);
        System.out.println(resp.bodyString());
    } catch (Exception e) {
        throw new Exception(e.getMessage());
    }
}
**客户**：你好，用了你上面的方法还是会报错401url:[URL已脱敏] [密钥已脱敏]-pZIDEGYAOIUrveZXq:[密钥已脱敏]报错信息：com.qiniu.common.QiniuException: GET [URL已脱敏]  {ResponseInfo:com.qiniu.http.Response@1b3572b,status:401, reqId:I2UAAADCm1EmEfkX, xlog:APIS/401, xvia:, adress:api.qiniu.com/[IP已脱敏]:443, duration:0.299000 s, error:null}
**客服**：检查一下您的[密钥已脱敏] [密钥已脱敏]是否输入准确

### 根本原因分析

SSL证书配置或过期问题

---

## 11. ios sdk真机编译不过

**问题分类**: 对象存储｜上传下载

### 问题描述

报下面这个错误Showing Recent Errors OnlyAssertion failed: (aliasSectionNum == sectionNum && "alias and its target must be located in the same section"), function [密钥已脱敏], file Layout.cpp, line 4390.

### 客服解答

**客户**：报下面这个错误Showing Recent Errors OnlyAssertion failed: (aliasSectionNum == sectionNum && "alias and its target must be located in the same section"), function [密钥已脱敏], file Layout.cpp, line 4390.
**客服**：你好，请稍等
**客户**：不用了
**客服**：好的

### 根本原因分析

具体问题需要根据实际场景分析

---

## 12. 将系统域名修改为自定义域名后提示401错误

**问题分类**: 对象存储｜SDK使用

### 问题描述

使用自定义域名:oss.mengdaidai.cn1.   使用七牛云的系统域名，sdk使用io.minio.MinioClient 自定义实现的S3Client 客户端，可以正常上传文件，然后调用sdk里的生成外链方法，也能拿到[URL已脱敏]  开头的外链。2.  但是我想用【自定义域名】去访问文件，所以我配置了【自定义域名】，使用了ssl证书，密钥也是正常可用的，但是我再次调用客户端提示401错误，经我排查，猜测可能自定义域名是否只是用于图片访问，无法支持上传下载？（第一个问题）3. 如果第一个问题成立，那我将域名地址修改为【系统域名】，我将桶设置为了私有，我需要生成好的外链，访问控制台图片外链已经成为我指定的域名链接但是我在使用sdk的时候，访问图片链接生成接口，使用domin 是  [URL已脱敏]  开头的外链，与我的要求不符，所以我不知道怎么才能生成我自定义域名的外链。3. cdn问题，假设我配置了cdn指向了这个桶，cdn域名是否和源站域名不能是同一个？如果不是同一个，我怎么直接拿到  以  cdn  域名开头的外链？4.   最终期望结果就是拿到例如[URL已脱敏]  的外链，目前只能拿到  [URL已脱敏]   开头的外链，请帮忙解答我应该需要做哪些配置，然后java 的 io.minio.clinet   的sdk是否支持这种操作？还是我拿到外链后需要在前端自行处理将这个链接修改为cdn链接。另外，如果最终还是只能返回  [URL已脱敏]   开头的外链，自定义域名和cdn加速域名我是否只需要配一个？

### 客服解答

**客户**：使用自定义域名:oss.mengdaidai.cn1.   使用七牛云的系统域名，sdk使用io.minio.MinioClient 自定义实现的S3Client 客户端，可以正常上传文件，然后调用sdk里的生成外链方法，也能拿到[URL已脱敏]  开头的外链。2.  但是我想用【自定义域名】去访问文件，所以我配置了【自定义域名】，使用了ssl证书，密钥也是正常可用的，但是我再次调用客户端提示401错误，经我排查，猜测可能自定义域名是否只是用于图片访问，无法支持上传下载？（第一个问题）3. 如果第一个问题成立，那我将域名地址修改为【系统域名】，我将桶设置为了私有，我需要生成好的外链，访问控制台图片外链已经成为我指定的域名链接[图片]但是我在使用sdk的时候，访问图片链接生成接口，使用domin 是  [URL已脱敏]  开头的外链，与我的要求不符，所以我不知道怎么才能生成我自定义域名的外链。3. cdn问题，假设我配置了cdn指向了这个桶，cdn域名是否和源站域名不能是同一个？如果不是同一个，我怎么直接拿到  以  cdn  域名开头的外链？4.   最终期望结果就是拿到例如[URL已脱敏]  的外链，目前只能拿到  [URL已脱敏]   开头的外链，请帮忙解答我应该需要做哪些配置，然后java 的 io.minio.clinet   的sdk是否支持这种操作？还是我拿到外链后需要在前端自行处理将这个链接修改为cdn链接。另外，如果最终还是只能返回  [URL已脱敏]   开头的外链，自定义域名和cdn加速域名我是否只需要配一个？[图片][图片][图片][图片]
**客服**：您好用[URL已脱敏] 生成私有下载链接当您将空间设置成私有时，必须获得授权，才能对空间内的资源进行访问。私有资源下载是通过HTTP GET的方式访问特定的 URL。私有资源URL与公开资源URL相比只是增加了两个参数e和token，分别表示过期时间和下载凭证。一个完整的私有资源 URL 如下所示：[URL已脱敏]
参数e表示 URL 的过期时间，采用Unix时间戳，单位为秒。超时的访问将返回 401 错误。参数token表示下载凭证。下载凭证是对资源访问的授权，不带下载凭证或下载凭证不合法都会导致 401 错误，表示验证失败。注意：如果请求方的时钟未校准，可能会造成有效期验证不正常，例如直接认为已过期。因此需要进行时钟校准。由于开发者无法保证客户端的时间都校准，所以应该在业务服务器上创建时间戳，并周期性校准业务服务器时钟。文档链接：[URL已脱敏]

### 根本原因分析

网络波动导致上传不稳定，建议使用断点续传功能

---

## 13. 某个几点下载文件非常慢

**问题分类**: 对象存储｜上传下载

### 问题描述

文件：[URL已脱敏]

### 客服解答

**客户**：文件：[URL已脱敏]
**客户**：[图片]这是我们抓包的记录
**客服**：您好，大概访问是几点？这边过滤日志看下
**客户**：15:56:29.460
**客服**：您好，稍等下，这边测试看下
**客服**：您好，这边代理节点，测试是正常很快的
**客服**：查看日志响应时间也是很快的[图片]
**客户**：好的，估计是4G网络问题了。

### 根本原因分析

具体问题需要根据实际场景分析

---

## 14. 在使用idea生成java后端文件上传

**问题分类**: 对象存储｜上传下载

### 问题描述

E:\JAVA\bin\java.exe -agentlib:jdwp=transport=dt_socket,address=[IP已脱敏]:65284,suspend=y,server=n -XX:TieredStopAtLevel=1 -Dspring.output.ansi.enabled=always -Dcom.sun.management.jmxremote -Dspring.jmx.enabled=true -Dspring.liveBeansView.mbeanDomain -Dspring.application.admin.enabled=true "-Dmanagement.endpoints.jmx.exposure.include=*" -javaagent:C:\Users\oscar\AppData\Local\JetBrains\IntelliJIdea2024.1\captureAgent\debugger-agent.jar=file:/C:[密钥已脱敏].props -Dfile.encoding=UTF-8 -classpath "E:\JAVAProject\JAVAProject\[密钥已脱敏]y-t[密钥已脱敏]e-out\[密钥已脱敏]y-server\target\classes;E:\JAVAProject\JAVAProject\[密钥已脱敏]y-t[密钥已脱敏]e-out\[密钥已脱敏]y-common\target\classes;E:\MVN_repository\commons-lang\commons-lang\2.6\commons-lang-2.6.jar;E:\MVN_repository\org\springframework\boot\spring-boot-starter-json\2.7.3\spring-boot-starter-json-2.7.3.jar;E:\MVN_repository\com\fasterxml\jackson\datatype\jackson-datatype-jdk8\2.13.3\jackson-datatype-jdk8-2.13.3.jar;E:\MVN_repository\com\fasterxml\jackson\datatype\jackson-datatype-jsr310\2.13.3\jackson-datatype-jsr310-2.13.3.jar;E:\MVN_repository\com\fasterxml\jackson\module\jackson-module-parameter-names\2.13.3\jackson-module-parameter-names-2.13.3.jar;E:\MVN_repository\io\jsonwebtoken\jjwt\0.9.1\jjwt-0.9.1.jar;E:\MVN_repository\com\aliyun\oss\aliyun-sdk-oss\3.10.2\aliyun-sdk-oss-3.10.2.jar;E:\MVN_repository\org\apache\httpcomponents\httpclient\4.5.13\httpclient-4.5.13.jar;E:\MVN_repository\org\apache\httpcomponents\httpcore\4.4.15\httpcore-4.4.15.jar;E:\MVN_repository\org\jdom\jdom2\[IP已脱敏]\jdom2-[IP已脱敏].jar;E:\MVN_repository\org\codehaus\jettison\jettison\1.1\jettison-1.1.jar;E:\MVN_repository\stax\stax-api\1.0.1\stax-api-1.0.1.jar;E:\MVN_repository\com\aliyun\aliyun-java-sdk-core\3.4.0\aliyun-java-sdk-core-3.4.0.jar;E:\MVN_repository\com\aliyun\aliyun-java-sdk-ram\3.0.0\aliyun-java-sdk-ram-3.0.0.jar;E:\MVN_repository\com\aliyun\aliyun-java-sdk-sts\3.0.0\aliyun-java-sdk-sts-3.0.0.jar;E:\MVN_repository\com\aliyun\aliyun-java-sdk-ecs\4.2.0\aliyun-java-sdk-ecs-4.2.0.jar;E:\MVN_repository\com\aliyun\aliyun-java-sdk-kms\2.7.0\aliyun-java-sdk-kms-2.7.0.jar;E:\MVN_repository\com\github\wechatpay-apiv3\wechatpay-apache-httpclient\0.4.8\wechatpay-apache-httpclient-0.4.8.jar;E:\MVN_repository\org\apache\httpcomponents\httpmime\4.5.13\httpmime-4.5.13.jar;E:\JAVAProject\JAVAProject\[密钥已脱敏]y-t[密钥已脱敏]e-out\[密钥已脱敏]y-pojo\target\classes;E:\MVN_repository\com\fasterxml\jackson\core\jackson-databind\2.13.3\jackson-databind-2.13.3.jar;E:\MVN_repository\com\fasterxml\jackson\core\jackson-annotations\2.13.3\jackson-annotations-2.13.3.jar;E:\MVN_repository\com\fasterxml\jackson\core\jackson-core\2.13.3\jackson-core-2.13.3.jar;E:\MVN_repository\org\springframework\boot\spring-boot-starter\2.7.3\spring-boot-starter-2.7.3.jar;E:\MVN_repository\org\springframework\boot\spring-boot\2.7.3\spring-boot-2.7.3.jar;E:\MVN_repository\org\springframework\spring-context\5.3.22\spring-context-5.3.22.jar;E:\MVN_repository\org\springframework\boot\spring-boot-autoconfigure\2.7.3\spring-boot-autoconfigure-2.7.3.jar;E:\MVN_repository\org\springframework\boot\spring-boot-starter-logging\2.7.3\spring-boot-starter-logging-2.7.3.jar;E:\MVN_repository\ch\qos\logback\logback-classic\1.2.11\logback-classic-1.2.11.jar;E:\MVN_repository\ch\qos\logback\logback-core\1.2.11\logback-core-1.2.11.jar;E:\MVN_repository\org\apache\logging\log4j\log4j-to-slf4j\2.17.2\log4j-to-slf4j-2.17.2.jar;E:\MVN_repository\org\apache\logging\log4j\log4j-api\2.17.2\log4j-api-2.17.2.jar;E:\MVN_repository\org\slf4j\jul-to-slf4j\1.7.36\jul-to-slf4j-1.7.36.jar;E:\MVN_repository\j[密钥已脱敏]arta\annotation\j[密钥已脱敏]arta.annotation-api\1.3.5\j[密钥已脱敏]arta.annotation-api-1.3.5.jar;E:\MVN_repository\org\springframework\spring-core\5.3.22\spring-core-5.3.22.jar;E:\MVN_repository\org\springframework\spring-jcl\5.3.22\spring-jcl-5.3.22.jar;E:\MVN_repository\org\yaml\sn[密钥已脱敏]eyaml\1.30\sn[密钥已脱敏]eyaml-1.30.jar;E:\MVN_repository\net\bytebuddy\byte-buddy\1.12.13\byte-buddy-1.12.13.jar;E:\MVN_repository\org\springframework\boot\spring-boot-starter-web\2.7.3\spring-boot-starter-web-2.7.3.jar;E:\MVN_repository\org\springframework\boot\spring-boot-starter-tomcat\2.7.3\spring-boot-starter-tomcat-2.7.3.jar;E:\MVN_repository\org\apache\tomcat\embed\tomcat-embed-core\9.0.65\tomcat-embed-core-9.0.65.jar;E:\MVN_repository\org\apache\tomcat\embed\tomcat-embed-el\9.0.65\tomcat-embed-el-9.0.65.jar;E:\MVN_repository\org\apache\tomcat\embed\tomcat-embed-websocket\9.0.65\tomcat-embed-websocket-9.0.65.jar;E:\MVN_repository\org\springframework\spring-web\5.3.22\spring-web-5.3.22.jar;E:\MVN_repository\org\springframework\spring-beans\5.3.22\spring-beans-5.3.22.jar;E:\MVN_repository\org\springframework\spring-webmvc\5.3.22\spring-webmvc-5.3.22.jar;E:\MVN_repository\org\springframework\spring-aop\5.3.22\spring-aop-5.3.22.jar;E:\MVN_repository\org\springframework\spring-expression\5.3.22\spring-expression-5.3.22.jar;E:\MVN_repository\mysql\mysql-connector-java\8.0.30\mysql-connector-java-8.0.30.jar;E:\MVN_repository\org\mybatis\spring\boot\mybatis-spring-boot-starter\2.2.0\mybatis-spring-boot-starter-2.2.0.jar;E:\MVN_repository\org\springframework\boot\spring-boot-starter-jdbc\2.7.3\spring-boot-starter-jdbc-2.7.3.jar;E:\MVN_repository\com\zaxxer\HikariCP\4.0.3\HikariCP-4.0.3.jar;E:\MVN_repository\org\springframework\spring-jdbc\5.3.22\spring-jdbc-5.3.22.jar;E:\MVN_repository\org\mybatis\spring\boot\mybatis-spring-boot-autoconfigure\2.2.0\mybatis-spring-boot-autoconfigure-2.2.0.jar;E:\MVN_repository\org\mybatis\mybatis\3.5.7\mybatis-3.5.7.jar;E:\MVN_repository\org\mybatis\mybatis-spring\2.0.6\mybatis-spring-2.0.6.jar;E:\MVN_repository\org\projectlombok\lombok\1.18.20\lombok-1.18.20.jar;E:\MVN_repository\com\alibaba\fastjson\1.2.76\fastjson-1.2.76.jar;E:\MVN_repository\com\alibaba\druid-spring-boot-starter\1.2.1\druid-spring-boot-starter-1.2.1.jar;E:\MVN_repository\com\alibaba\druid\1.2.1\druid-1.2.1.jar;E:\MVN_repository\javax\annotation\javax.annotation-api\1.3.2\javax.annotation-api-1.3.2.jar;E:\MVN_repository\org\slf4j\slf4j-api\1.7.36\slf4j-api-1.7.36.jar;E:\MVN_repository\com\github\pagehelper\pagehelper-spring-boot-starter\1.3.0\pagehelper-spring-boot-starter-1.3.0.jar;E:\MVN_repository\com\github\pagehelper\pagehelper-spring-boot-autoconfigure\1.3.0\pagehelper-spring-boot-autoconfigure-1.3.0.jar;E:\MVN_repository\com\github\pagehelper\pagehelper\5.2.0\pagehelper-5.2.0.jar;E:\MVN_repository\com\github\jsqlparser\jsqlparser\3.2\jsqlparser-3.2.jar;E:\MVN_repository\org\aspectj\aspectjrt\1.9.4\aspectjrt-1.9.4.jar;E:\MVN_repository\org\aspectj\aspectjweaver\1.9.4\aspectjweaver-1.9.4.jar;E:\MVN_repository\com\github\xiaoymin\knife4j-spring-boot-starter\3.0.2\knife4j-spring-boot-starter-3.0.2.jar;E:\MVN_repository\com\github\xiaoymin\knife4j-spring-boot-autoconfigure\3.0.2\knife4j-spring-boot-autoconfigure-3.0.2.jar;E:\MVN_repository\com\github\xiaoymin\knife4j-spring\3.0.2\knife4j-spring-3.0.2.jar;E:\MVN_repository\com\github\xiaoymin\knife4j-annotations\3.0.2\knife4j-annotations-3.0.2.jar;E:\MVN_repository\io\swagger\swagger-annotations\1.5.22\swagger-annotations-1.5.22.jar;E:\MVN_repository\io\swagger\core\v3\swagger-annotations\2.1.2\swagger-annotations-2.1.2.jar;E:\MVN_repository\com\github\xiaoymin\knife4j-core\3.0.2\knife4j-core-3.0.2.jar;E:\MVN_repository\org\javassist\javassist\3.25.0-GA\javassist-3.25.0-GA.jar;E:\MVN_repository\io\springfox\springfox-swagger2\3.0.0\springfox-swagger2-3.0.0.jar;E:\MVN_repository\io\springfox\springfox-spi\3.0.0\springfox-spi-3.0.0.jar;E:\MVN_repository\io\springfox\springfox-schema\3.0.0\springfox-schema-3.0.0.jar;E:\MVN_repository\io\springfox\springfox-swagger-common\3.0.0\springfox-swagger-common-3.0.0.jar;E:\MVN_repository\io\springfox\springfox-spring-web\3.0.0\springfox-spring-web-3.0.0.jar;E:\MVN_repository\io\github\classgraph\classgraph\4.8.83\classgraph-4.8.83.jar;E:\MVN_repository\io\springfox\springfox-spring-webflux\3.0.0\springfox-spring-webflux-3.0.0.jar;E:\MVN_repository\org\mapstruct\mapstruct\1.3.1.Final\mapstruct-1.3.1.Final.jar;E:\MVN_repository\io\springfox\springfox-spring-webmvc\3.0.0\springfox-spring-webmvc-3.0.0.jar;E:\MVN_repository\io\springfox\springfox-core\3.0.0\springfox-core-3.0.0.jar;E:\MVN_repository\io\springfox\springfox-oas\3.0.0\springfox-oas-3.0.0.jar;E:\MVN_repository\io\swagger\core\v3\swagger-models\2.1.2\swagger-models-2.1.2.jar;E:\MVN_repository\io\springfox\springfox-bean-validators\3.0.0\springfox-bean-validators-3.0.0.jar;E:\MVN_repository\io\swagger\swagger-models\1.5.22\swagger-models-1.5.22.jar;E:\MVN_repository\io\swagger\swagger-core\1.5.22\swagger-core-1.5.22.jar;E:\MVN_repository\org\apache\commons\commons-lang3\3.12.0\commons-lang3-3.12.0.jar;E:\MVN_repository\com\fasterxml\jackson\dataformat\jackson-dataformat-yaml\2.13.3\jackson-dataformat-yaml-2.13.3.jar;E:\MVN_repository\com\google\guava\guava\27.0.1-android\guava-27.0.1-android.jar;E:\MVN_repository\com\google\guava\failureaccess\1.0.1\failureaccess-1.0.1.jar;E:\MVN_repository\com\google\guava\listenablefuture\9999.0-empty-to-avoid-conflict-with-guava\listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar;E:\MVN_repository\com\google\code\findbugs\jsr305\3.0.2\jsr305-3.0.2.jar;E:\MVN_repository\org\checkerframework\checker-compat-qual\2.5.2\checker-compat-qual-2.5.2.jar;E:\MVN_repository\com\google\errorprone\error_prone_annotations\2.2.0\error_prone_annotations-2.2.0.jar;E:\MVN_repository\com\google\j2objc\j2objc-annotations\1.1\j2objc-annotations-1.1.jar;E:\MVN_repository\org\codehaus\mojo\animal-sniffer-annotations\1.17\animal-sniffer-annotations-1.17.jar;E:\MVN_repository\javax\validation\validation-api\2.0.1.Final\validation-api-2.0.1.Final.jar;E:\MVN_repository\io\springfox\springfox-boot-starter\3.0.0\springfox-boot-starter-3.0.0.jar;E:\MVN_repository\io\springfox\springfox-data-rest\3.0.0\springfox-data-rest-3.0.0.jar;E:\MVN_repository\com\fasterxml\classmate\1.5.1\classmate-1.5.1.jar;E:\MVN_repository\org\springframework\plugin\spring-plugin-core\2.0.0.RELEASE\spring-plugin-core-2.0.0.RELEASE.jar;E:\MVN_repository\org\springframework\plugin\spring-plugin-metadata\2.0.0.RELEASE\spring-plugin-metadata-2.0.0.RELEASE.jar;E:\MVN_repository\com\github\xiaoymin\knife4j-spring-ui\3.0.2\knife4j-spring-ui-3.0.2.jar;E:\MVN_repository\org\springframework\boot\spring-boot-starter-data-redis\2.7.3\spring-boot-starter-data-redis-2.7.3.jar;E:\MVN_repository\org\springframework\data\spring-data-redis\2.7.2\spring-data-redis-2.7.2.jar;E:\MVN_repository\org\springframework\data\spring-data-keyvalue\2.7.2\spring-data-keyvalue-2.7.2.jar;E:\MVN_repository\org\springframework\data\spring-data-commons\2.7.2\spring-data-commons-2.7.2.jar;E:\MVN_repository\org\springframework\spring-tx\5.3.22\spring-tx-5.3.22.jar;E:\MVN_repository\org\springframework\spring-oxm\5.3.22\spring-oxm-5.3.22.jar;E:\MVN_repository\io\lettuce\lettuce-core\6.1.9.RELEASE\lettuce-core-6.1.9.RELEASE.jar;E:\MVN_repository\io\netty\netty-common\4.1.79.Final\netty-common-4.1.79.Final.jar;E:\MVN_repository\io\netty\netty-handler\4.1.79.Final\netty-handler-4.1.79.Final.jar;E:\MVN_repository\io\netty\netty-resolver\4.1.79.Final\netty-resolver-4.1.79.Final.jar;E:\MVN_repository\io\netty\netty-buffer\4.1.79.Final\netty-buffer-4.1.79.Final.jar;E:\MVN_repository\io\netty\netty-transport-native-unix-common\4.1.79.Final\netty-transport-native-unix-common-4.1.79.Final.jar;E:\MVN_repository\io\netty\netty-codec\4.1.79.Final\netty-codec-4.1.79.Final.jar;E:\MVN_repository\io\netty\netty-transport\4.1.79.Final\netty-transport-4.1.79.Final.jar;E:\MVN_repository\io\projectreactor\reactor-core\3.4.22\reactor-core-3.4.22.jar;E:\MVN_repository\org\reactivestreams\reactive-streams\1.0.4\reactive-streams-1.0.4.jar;E:\MVN_repository\org\springframework\boot\spring-boot-starter-cache\2.7.3\spring-boot-starter-cache-2.7.3.jar;E:\MVN_repository\org\springframework\spring-context-support\5.3.22\spring-context-support-5.3.22.jar;E:\MVN_repository\org\springframework\boot\spring-boot-starter-websocket\2.7.3\spring-boot-starter-websocket-2.7.3.jar;E:\MVN_repository\org\springframework\spring-messaging\5.3.22\spring-messaging-5.3.22.jar;E:\MVN_repository\org\springframework\spring-websocket\5.3.22\spring-websocket-5.3.22.jar;E:\MVN_repository\javax\xml\bind\jaxb-api\2.3.1\jaxb-api-2.3.1.jar;E:\MVN_repository\javax\activation\javax.activation-api\1.2.0\javax.activation-api-1.2.0.jar;E:\MVN_repository\org\apache\poi\poi\3.16\poi-3.16.jar;E:\MVN_repository\commons-codec\commons-codec\1.15\commons-codec-1.15.jar;E:\MVN_repository\org\apache\commons\commons-collections4\4.1\commons-collections4-4.1.jar;E:\MVN_repository\org\apache\poi\poi-ooxml\3.16\poi-ooxml-3.16.jar;E:\MVN_repository\org\apache\poi\poi-ooxml-schemas\3.16\poi-ooxml-schemas-3.16.jar;E:\MVN_repository\org\apache\xmlbeans\xmlbeans\2.6.0\xmlbeans-2.6.0.jar;E:\MVN_repository\com\github\virtuald\curvesapi\1.04\curvesapi-1.04.jar;E:\MVN_repository\com\qiniu\qiniu-java-sdk\7.16.0\qiniu-java-sdk-7.16.0.jar;E:\MVN_repository\com\squareup\okhttp3\okhttp\3.14.2\okhttp-3.14.2.jar;E:\MVN_repository\com\squareup\okio\okio\1.17.2\okio-1.17.2.jar;E:\MVN_repository\com\google\code\gson\gson\2.8.5\gson-2.8.5.jar;E:\IDEA\IntelliJ IDEA 2024.1.6\lib\idea_rt.jar" com.[密钥已脱敏]y.[密钥已脱敏] to the target VM, address: '[IP已脱敏]:65284', transport: 'socket'17:32:33.919 [main] DEBUG reactor.util.Loggers - Using Slf4j logging framework17:32:33.923 [main] DEBUG reactor.core.publisher.Hooks - Enabling stacktrace debugging via onOperatorDebug  .   ____          _            __ _ _ /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \ \\/  ___)| |_)| | | | | || (_| |  ) ) ) )  '  |____| .__|_| |_|_| |_\__, | / / / / =========|_|==============|___/=/_/_/_/ :: Spring Boot ::                (v2.7.3)2024-09-27 17:32:34.715  INFO 23344 --- [           main] com.[密钥已脱敏]y.[密钥已脱敏]yApplication                   : Starting [密钥已脱敏]yApplication using Java 17.0.12 on DE[密钥已脱敏]TOP-5AUC532 with PID 23344 (E:\JAVAProject\JAVAProject\[密钥已脱敏]y-t[密钥已脱敏]e-out\[密钥已脱敏]y-server\target\classes started by oscar in E:\JAVAProject\JAVAProject\[密钥已脱敏]y-t[密钥已脱敏]e-out)2024-09-27 17:32:34.716  INFO 23344 --- [           main] com.[密钥已脱敏]y.[密钥已脱敏]yApplication                   : The following 1 profile is active: "dev"2024-09-27 17:32:35.874  INFO 23344 --- [           main] .s.d.r.c.[密钥已脱敏] : Multiple Spring Data modules found, entering strict repository configuration mode2024-09-27 17:32:35.879  INFO 23344 --- [           main] .s.d.r.c.[密钥已脱敏] : Bootstrapping Spring Data Redis repositories in DEFAULT mode.2024-09-27 17:32:35.924  INFO 23344 --- [           main] .s.d.r.c.[密钥已脱敏] : Finished Spring Data repository scanning in 22 ms. Found 0 Redis repository interfaces.2024-09-27 17:32:36.758  INFO 23344 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 8080 (http)2024-09-27 17:32:36.767  INFO 23344 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]2024-09-27 17:32:36.767  INFO 23344 --- [           main] org.apache.catalina.core.StandardEngine  : Starting Servlet engine: [Apache Tomcat/9.0.65]2024-09-27 17:32:36.857  INFO 23344 --- [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded [密钥已脱敏]-09-27 17:32:36.857  INFO 23344 --- [           main] w.s.c.[密钥已脱敏] : Root [密钥已脱敏]: initialization completed in 2104 ms2024-09-27 17:32:36.972  INFO 23344 --- [           main] c.a.d.s.b.a.[密钥已脱敏] : Init DruidDataSource2024-09-27 17:32:37.092  INFO 23344 --- [           main] com.alibaba.druid.pool.DruidDataSource   : {dataSource-1} inited2024-09-27 17:32:37.317  INFO 23344 --- [           main] com.[密钥已脱敏]y.config.OssConfiguration          : 开始创建七牛云文件上传工具类对象:QiniuOssProperties(endpoint=s3.cn-north-1.qiniucs.com, [密钥已脱敏]Id=[密钥已脱敏], [密钥已脱敏]Secret=[密钥已脱敏], bucketName=[密钥已脱敏]y-kdb)2024-09-27 17:32:37.616  INFO 23344 --- [           main] com.[密钥已脱敏]y.config.WebMvcConfiguration       : 开始注册自定义拦截器...2024-09-27 17:32:37.719  INFO 23344 --- [           main] com.[密钥已脱敏]y.config.WebMvcConfiguration       : 准备生成接口文档...2024-09-27 17:32:37.756  INFO 23344 --- [           main] com.[密钥已脱敏]y.config.WebMvcConfiguration       : 扩展消息转换器...2024-09-27 17:32:37.761  INFO 23344 --- [           main] com.[密钥已脱敏]y.config.WebMvcConfiguration       : 开始设置静态资源映射...2024-09-27 17:32:38.434  INFO 23344 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http) with context path ''2024-09-27 17:32:38.661  INFO 23344 --- [           main] com.[密钥已脱敏]y.[密钥已脱敏]yApplication                   : Started [密钥已脱敏]yApplication in 4.397 seconds (JVM running for 5.161)2024-09-27 17:32:38.663  INFO 23344 --- [           main] com.[密钥已脱敏]y.[密钥已脱敏]yApplication                   : server started2024-09-27 17:32:52.113  INFO 23344 --- [nio-8080-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring DispatcherServlet 'dispatcherServlet'2024-09-27 17:32:52.113  INFO 23344 --- [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Initializing Servlet 'dispatcherServlet'2024-09-27 17:32:52.116  INFO 23344 --- [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Completed initialization in 3 ms当前线程的id：482024-09-27 17:32:52.133  INFO 23344 --- [nio-8080-exec-1] c.s.i.[密钥已脱敏]           : jwt校验:[REDACTED_JWT_TOKEN] 17:32:52.134  WARN 23344 --- [nio-8080-exec-2] o.s.web.servlet.PageNotFound             : No mapping for GET [密钥已脱敏]-09-27 17:32:52.241  INFO 23344 --- [nio-8080-exec-1] c.s.i.[密钥已脱敏]           : 当前员工id：2024-09-27 17:32:52.314  WARN 23344 --- [nio-8080-exec-3] o.s.web.servlet.PageNotFound             : No mapping for GET /ws/s8tp96fqw92024-09-27 17:32:52.445 DEBUG 23344 --- [nio-8080-exec-1] com.[密钥已脱敏]y.mapper.CategoryMapper.list       : ==>  Preparing: select * from category where status = 1 and type = ? order by sort asc,create_time desc2024-09-27 17:32:52.469 DEBUG 23344 --- [nio-8080-exec-1] com.[密钥已脱敏]y.mapper.CategoryMapper.list       : ==> Parameters: 1(Integer)2024-09-27 17:32:52.498 DEBUG 23344 --- [nio-8080-exec-1] com.[密钥已脱敏]y.mapper.CategoryMapper.list       :   Preparing: insert into dish(name, category_id, price, image, description, create_time, update_time, create_user, update_user,status) VALUES (?,?,?,?,?,?,?,?,?,?)2024-09-27 17:33:40.057 DEBUG 23344 --- [nio-8080-exec-5] com.[密钥已脱敏]y.mapper.DishMapper.insert         : ==> Parameters: null, null, null, null, null, null, null, null, null, null

### 客服解答

**客户**：E:\JAVA\bin\java.exe -agentlib:jdwp=transport=dt_socket,address=[IP已脱敏]:65284,suspend=y,server=n -XX:TieredStopAtLevel=1 -Dspring.output.ansi.enabled=always -Dcom.sun.management.jmxremote -Dspring.jmx.enabled=true -Dspring.liveBeansView.mbeanDomain -Dspring.application.admin.enabled=true "-Dmanagement.endpoints.jmx.exposure.include=*" -javaagent:C:\Users\oscar\AppData\Local\JetBrains\IntelliJIdea2024.1\captureAgent\debugger-agent.jar=file:/C:[密钥已脱敏].props -Dfile.encoding=UTF-8 -classpath "E:\JAVAProject\JAVAProject\[密钥已脱敏]y-t[密钥已脱敏]e-out\[密钥已脱敏]y-server\target\classes;E:\JAVAProject\JAVAProject\[密钥已脱敏]y-t[密钥已脱敏]e-out\[密钥已脱敏]y-common\target\classes;E:\MVN_repository\commons-lang\commons-lang\2.6\commons-lang-2.6.jar;E:\MVN_repository\org\springframework\boot\spring-boot-starter-json\2.7.3\spring-boot-starter-json-2.7.3.jar;E:\MVN_repository\com\fasterxml\jackson\datatype\jackson-datatype-jdk8\2.13.3\jackson-datatype-jdk8-2.13.3.jar;E:\MVN_repository\com\fasterxml\jackson\datatype\jackson-datatype-jsr310\2.13.3\jackson-datatype-jsr310-2.13.3.jar;E:\MVN_repository\com\fasterxml\jackson\module\jackson-module-parameter-names\2.13.3\jackson-module-parameter-names-2.13.3.jar;E:\MVN_repository\io\jsonwebtoken\jjwt\0.9.1\jjwt-0.9.1.jar;E:\MVN_repository\com\aliyun\oss\aliyun-sdk-oss\3.10.2\aliyun-sdk-oss-3.10.2.jar;E:\MVN_repository\org\apache\httpcomponents\httpclient\4.5.13\httpclient-4.5.13.jar;E:\MVN_repository\org\apache\httpcomponents\httpcore\4.4.15\httpcore-4.4.15.jar;E:\MVN_repository\org\jdom\jdom2\[IP已脱敏]\jdom2-[IP已脱敏].jar;E:\MVN_repository\org\codehaus\jettison\jettison\1.1\jettison-1.1.jar;E:\MVN_repository\stax\stax-api\1.0.1\stax-api-1.0.1.jar;E:\MVN_repository\com\aliyun\aliyun-java-sdk-core\3.4.0\aliyun-java-sdk-core-3.4.0.jar;E:\MVN_repository\com\aliyun\aliyun-java-sdk-ram\3.0.0\aliyun-java-sdk-ram-3.0.0.jar;E:\MVN_repository\com\aliyun\aliyun-java-sdk-sts\3.0.0\aliyun-java-sdk-sts-3.0.0.jar;E:\MVN_repository\com\aliyun\aliyun-java-sdk-ecs\4.2.0\aliyun-java-sdk-ecs-4.2.0.jar;E:\MVN_repository\com\aliyun\aliyun-java-sdk-kms\2.7.0\aliyun-java-sdk-kms-2.7.0.jar;E:\MVN_repository\com\github\wechatpay-apiv3\wechatpay-apache-httpclient\0.4.8\wechatpay-apache-httpclient-0.4.8.jar;E:\MVN_repository\org\apache\httpcomponents\httpmime\4.5.13\httpmime-4.5.13.jar;E:\JAVAProject\JAVAProject\[密钥已脱敏]y-t[密钥已脱敏]e-out\[密钥已脱敏]y-pojo\target\classes;E:\MVN_repository\com\fasterxml\jackson\core\jackson-databind\2.13.3\jackson-databind-2.13.3.jar;E:\MVN_repository\com\fasterxml\jackson\core\jackson-annotations\2.13.3\jackson-annotations-2.13.3.jar;E:\MVN_repository\com\fasterxml\jackson\core\jackson-core\2.13.3\jackson-core-2.13.3.jar;E:\MVN_repository\org\springframework\boot\spring-boot-starter\2.7.3\spring-boot-starter-2.7.3.jar;E:\MVN_repository\org\springframework\boot\spring-boot\2.7.3\spring-boot-2.7.3.jar;E:\MVN_repository\org\springframework\spring-context\5.3.22\spring-context-5.3.22.jar;E:\MVN_repository\org\springframework\boot\spring-boot-autoconfigure\2.7.3\spring-boot-autoconfigure-2.7.3.jar;E:\MVN_repository\org\springframework\boot\spring-boot-starter-logging\2.7.3\spring-boot-starter-logging-2.7.3.jar;E:\MVN_repository\ch\qos\logback\logback-classic\1.2.11\logback-classic-1.2.11.jar;E:\MVN_repository\ch\qos\logback\logback-core\1.2.11\logback-core-1.2.11.jar;E:\MVN_repository\org\apache\logging\log4j\log4j-to-slf4j\2.17.2\log4j-to-slf4j-2.17.2.jar;E:\MVN_repository\org\apache\logging\log4j\log4j-api\2.17.2\log4j-api-2.17.2.jar;E:\MVN_repository\org\slf4j\jul-to-slf4j\1.7.36\jul-to-slf4j-1.7.36.jar;E:\MVN_repository\j[密钥已脱敏]arta\annotation\j[密钥已脱敏]arta.annotation-api\1.3.5\j[密钥已脱敏]arta.annotation-api-1.3.5.jar;E:\MVN_repository\org\springframework\spring-core\5.3.22\spring-core-5.3.22.jar;E:\MVN_repository\org\springframework\spring-jcl\5.3.22\spring-jcl-5.3.22.jar;E:\MVN_repository\org\yaml\sn[密钥已脱敏]eyaml\1.30\sn[密钥已脱敏]eyaml-1.30.jar;E:\MVN_repository\net\bytebuddy\byte-buddy\1.12.13\byte-buddy-1.12.13.jar;E:\MVN_repository\org\springframework\boot\spring-boot-starter-web\2.7.3\spring-boot-starter-web-2.7.3.jar;E:\MVN_repository\org\springframework\boot\spring-boot-starter-tomcat\2.7.3\spring-boot-starter-tomcat-2.7.3.jar;E:\MVN_repository\org\apache\tomcat\embed\tomcat-embed-core\9.0.65\tomcat-embed-core-9.0.65.jar;E:\MVN_repository\org\apache\tomcat\embed\tomcat-embed-el\9.0.65\tomcat-embed-el-9.0.65.jar;E:\MVN_repository\org\apache\tomcat\embed\tomcat-embed-websocket\9.0.65\tomcat-embed-websocket-9.0.65.jar;E:\MVN_repository\org\springframework\spring-web\5.3.22\spring-web-5.3.22.jar;E:\MVN_repository\org\springframework\spring-beans\5.3.22\spring-beans-5.3.22.jar;E:\MVN_repository\org\springframework\spring-webmvc\5.3.22\spring-webmvc-5.3.22.jar;E:\MVN_repository\org\springframework\spring-aop\5.3.22\spring-aop-5.3.22.jar;E:\MVN_repository\org\springframework\spring-expression\5.3.22\spring-expression-5.3.22.jar;E:\MVN_repository\mysql\mysql-connector-java\8.0.30\mysql-connector-java-8.0.30.jar;E:\MVN_repository\org\mybatis\spring\boot\mybatis-spring-boot-starter\2.2.0\mybatis-spring-boot-starter-2.2.0.jar;E:\MVN_repository\org\springframework\boot\spring-boot-starter-jdbc\2.7.3\spring-boot-starter-jdbc-2.7.3.jar;E:\MVN_repository\com\zaxxer\HikariCP\4.0.3\HikariCP-4.0.3.jar;E:\MVN_repository\org\springframework\spring-jdbc\5.3.22\spring-jdbc-5.3.22.jar;E:\MVN_repository\org\mybatis\spring\boot\mybatis-spring-boot-autoconfigure\2.2.0\mybatis-spring-boot-autoconfigure-2.2.0.jar;E:\MVN_repository\org\mybatis\mybatis\3.5.7\mybatis-3.5.7.jar;E:\MVN_repository\org\mybatis\mybatis-spring\2.0.6\mybatis-spring-2.0.6.jar;E:\MVN_repository\org\projectlombok\lombok\1.18.20\lombok-1.18.20.jar;E:\MVN_repository\com\alibaba\fastjson\1.2.76\fastjson-1.2.76.jar;E:\MVN_repository\com\alibaba\druid-spring-boot-starter\1.2.1\druid-spring-boot-starter-1.2.1.jar;E:\MVN_repository\com\alibaba\druid\1.2.1\druid-1.2.1.jar;E:\MVN_repository\javax\annotation\javax.annotation-api\1.3.2\javax.annotation-api-1.3.2.jar;E:\MVN_repository\org\slf4j\slf4j-api\1.7.36\slf4j-api-1.7.36.jar;E:\MVN_repository\com\github\pagehelper\pagehelper-spring-boot-starter\1.3.0\pagehelper-spring-boot-starter-1.3.0.jar;E:\MVN_repository\com\github\pagehelper\pagehelper-spring-boot-autoconfigure\1.3.0\pagehelper-spring-boot-autoconfigure-1.3.0.jar;E:\MVN_repository\com\github\pagehelper\pagehelper\5.2.0\pagehelper-5.2.0.jar;E:\MVN_repository\com\github\jsqlparser\jsqlparser\3.2\jsqlparser-3.2.jar;E:\MVN_repository\org\aspectj\aspectjrt\1.9.4\aspectjrt-1.9.4.jar;E:\MVN_repository\org\aspectj\aspectjweaver\1.9.4\aspectjweaver-1.9.4.jar;E:\MVN_repository\com\github\xiaoymin\knife4j-spring-boot-starter\3.0.2\knife4j-spring-boot-starter-3.0.2.jar;E:\MVN_repository\com\github\xiaoymin\knife4j-spring-boot-autoconfigure\3.0.2\knife4j-spring-boot-autoconfigure-3.0.2.jar;E:\MVN_repository\com\github\xiaoymin\knife4j-spring\3.0.2\knife4j-spring-3.0.2.jar;E:\MVN_repository\com\github\xiaoymin\knife4j-annotations\3.0.2\knife4j-annotations-3.0.2.jar;E:\MVN_repository\io\swagger\swagger-annotations\1.5.22\swagger-annotations-1.5.22.jar;E:\MVN_repository\io\swagger\core\v3\swagger-annotations\2.1.2\swagger-annotations-2.1.2.jar;E:\MVN_repository\com\github\xiaoymin\knife4j-core\3.0.2\knife4j-core-3.0.2.jar;E:\MVN_repository\org\javassist\javassist\3.25.0-GA\javassist-3.25.0-GA.jar;E:\MVN_repository\io\springfox\springfox-swagger2\3.0.0\springfox-swagger2-3.0.0.jar;E:\MVN_repository\io\springfox\springfox-spi\3.0.0\springfox-spi-3.0.0.jar;E:\MVN_repository\io\springfox\springfox-schema\3.0.0\springfox-schema-3.0.0.jar;E:\MVN_repository\io\springfox\springfox-swagger-common\3.0.0\springfox-swagger-common-3.0.0.jar;E:\MVN_repository\io\springfox\springfox-spring-web\3.0.0\springfox-spring-web-3.0.0.jar;E:\MVN_repository\io\github\classgraph\classgraph\4.8.83\classgraph-4.8.83.jar;E:\MVN_repository\io\springfox\springfox-spring-webflux\3.0.0\springfox-spring-webflux-3.0.0.jar;E:\MVN_repository\org\mapstruct\mapstruct\1.3.1.Final\mapstruct-1.3.1.Final.jar;E:\MVN_repository\io\springfox\springfox-spring-webmvc\3.0.0\springfox-spring-webmvc-3.0.0.jar;E:\MVN_repository\io\springfox\springfox-core\3.0.0\springfox-core-3.0.0.jar;E:\MVN_repository\io\springfox\springfox-oas\3.0.0\springfox-oas-3.0.0.jar;E:\MVN_repository\io\swagger\core\v3\swagger-models\2.1.2\swagger-models-2.1.2.jar;E:\MVN_repository\io\springfox\springfox-bean-validators\3.0.0\springfox-bean-validators-3.0.0.jar;E:\MVN_repository\io\swagger\swagger-models\1.5.22\swagger-models-1.5.22.jar;E:\MVN_repository\io\swagger\swagger-core\1.5.22\swagger-core-1.5.22.jar;E:\MVN_repository\org\apache\commons\commons-lang3\3.12.0\commons-lang3-3.12.0.jar;E:\MVN_repository\com\fasterxml\jackson\dataformat\jackson-dataformat-yaml\2.13.3\jackson-dataformat-yaml-2.13.3.jar;E:\MVN_repository\com\google\guava\guava\27.0.1-android\guava-27.0.1-android.jar;E:\MVN_repository\com\google\guava\failureaccess\1.0.1\failureaccess-1.0.1.jar;E:\MVN_repository\com\google\guava\listenablefuture\9999.0-empty-to-avoid-conflict-with-guava\listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar;E:\MVN_repository\com\google\code\findbugs\jsr305\3.0.2\jsr305-3.0.2.jar;E:\MVN_repository\org\checkerframework\checker-compat-qual\2.5.2\checker-compat-qual-2.5.2.jar;E:\MVN_repository\com\google\errorprone\error_prone_annotations\2.2.0\error_prone_annotations-2.2.0.jar;E:\MVN_repository\com\google\j2objc\j2objc-annotations\1.1\j2objc-annotations-1.1.jar;E:\MVN_repository\org\codehaus\mojo\animal-sniffer-annotations\1.17\animal-sniffer-annotations-1.17.jar;E:\MVN_repository\javax\validation\validation-api\2.0.1.Final\validation-api-2.0.1.Final.jar;E:\MVN_repository\io\springfox\springfox-boot-starter\3.0.0\springfox-boot-starter-3.0.0.jar;E:\MVN_repository\io\springfox\springfox-data-rest\3.0.0\springfox-data-rest-3.0.0.jar;E:\MVN_repository\com\fasterxml\classmate\1.5.1\classmate-1.5.1.jar;E:\MVN_repository\org\springframework\plugin\spring-plugin-core\2.0.0.RELEASE\spring-plugin-core-2.0.0.RELEASE.jar;E:\MVN_repository\org\springframework\plugin\spring-plugin-metadata\2.0.0.RELEASE\spring-plugin-metadata-2.0.0.RELEASE.jar;E:\MVN_repository\com\github\xiaoymin\knife4j-spring-ui\3.0.2\knife4j-spring-ui-3.0.2.jar;E:\MVN_repository\org\springframework\boot\spring-boot-starter-data-redis\2.7.3\spring-boot-starter-data-redis-2.7.3.jar;E:\MVN_repository\org\springframework\data\spring-data-redis\2.7.2\spring-data-redis-2.7.2.jar;E:\MVN_repository\org\springframework\data\spring-data-keyvalue\2.7.2\spring-data-keyvalue-2.7.2.jar;E:\MVN_repository\org\springframework\data\spring-data-commons\2.7.2\spring-data-commons-2.7.2.jar;E:\MVN_repository\org\springframework\spring-tx\5.3.22\spring-tx-5.3.22.jar;E:\MVN_repository\org\springframework\spring-oxm\5.3.22\spring-oxm-5.3.22.jar;E:\MVN_repository\io\lettuce\lettuce-core\6.1.9.RELEASE\lettuce-core-6.1.9.RELEASE.jar;E:\MVN_repository\io\netty\netty-common\4.1.79.Final\netty-common-4.1.79.Final.jar;E:\MVN_repository\io\netty\netty-handler\4.1.79.Final\netty-handler-4.1.79.Final.jar;E:\MVN_repository\io\netty\netty-resolver\4.1.79.Final\netty-resolver-4.1.79.Final.jar;E:\MVN_repository\io\netty\netty-buffer\4.1.79.Final\netty-buffer-4.1.79.Final.jar;E:\MVN_repository\io\netty\netty-transport-native-unix-common\4.1.79.Final\netty-transport-native-unix-common-4.1.79.Final.jar;E:\MVN_repository\io\netty\netty-codec\4.1.79.Final\netty-codec-4.1.79.Final.jar;E:\MVN_repository\io\netty\netty-transport\4.1.79.Final\netty-transport-4.1.79.Final.jar;E:\MVN_repository\io\projectreactor\reactor-core\3.4.22\reactor-core-3.4.22.jar;E:\MVN_repository\org\reactivestreams\reactive-streams\1.0.4\reactive-streams-1.0.4.jar;E:\MVN_repository\org\springframework\boot\spring-boot-starter-cache\2.7.3\spring-boot-starter-cache-2.7.3.jar;E:\MVN_repository\org\springframework\spring-context-support\5.3.22\spring-context-support-5.3.22.jar;E:\MVN_repository\org\springframework\boot\spring-boot-starter-websocket\2.7.3\spring-boot-starter-websocket-2.7.3.jar;E:\MVN_repository\org\springframework\spring-messaging\5.3.22\spring-messaging-5.3.22.jar;E:\MVN_repository\org\springframework\spring-websocket\5.3.22\spring-websocket-5.3.22.jar;E:\MVN_repository\javax\xml\bind\jaxb-api\2.3.1\jaxb-api-2.3.1.jar;E:\MVN_repository\javax\activation\javax.activation-api\1.2.0\javax.activation-api-1.2.0.jar;E:\MVN_repository\org\apache\poi\poi\3.16\poi-3.16.jar;E:\MVN_repository\commons-codec\commons-codec\1.15\commons-codec-1.15.jar;E:\MVN_repository\org\apache\commons\commons-collections4\4.1\commons-collections4-4.1.jar;E:\MVN_repository\org\apache\poi\poi-ooxml\3.16\poi-ooxml-3.16.jar;E:\MVN_repository\org\apache\poi\poi-ooxml-schemas\3.16\poi-ooxml-schemas-3.16.jar;E:\MVN_repository\org\apache\xmlbeans\xmlbeans\2.6.0\xmlbeans-2.6.0.jar;E:\MVN_repository\com\github\virtuald\curvesapi\1.04\curvesapi-1.04.jar;E:\MVN_repository\com\qiniu\qiniu-java-sdk\7.16.0\qiniu-java-sdk-7.16.0.jar;E:\MVN_repository\com\squareup\okhttp3\okhttp\3.14.2\okhttp-3.14.2.jar;E:\MVN_repository\com\squareup\okio\okio\1.17.2\okio-1.17.2.jar;E:\MVN_repository\com\google\code\gson\gson\2.8.5\gson-2.8.5.jar;E:\IDEA\IntelliJ IDEA 2024.1.6\lib\idea_rt.jar" com.[密钥已脱敏]y.[密钥已脱敏] to the target VM, address: '[IP已脱敏]:65284', transport: 'socket'17:32:33.919 [main] DEBUG reactor.util.Loggers - Using Slf4j logging framework17:32:33.923 [main] DEBUG reactor.core.publisher.Hooks - Enabling stacktrace debugging via onOperatorDebug  .   ____          _            __ _ _ /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \ \\/  ___)| |_)| | | | | || (_| |  ) ) ) )  '  |____| .__|_| |_|_| |_\__, | / / / / =========|_|==============|___/=/_/_/_/ :: Spring Boot ::                (v2.7.3)2024-09-27 17:32:34.715  INFO 23344 --- [           main] com.[密钥已脱敏]y.[密钥已脱敏]yApplication                   : Starting [密钥已脱敏]yApplication using Java 17.0.12 on DE[密钥已脱敏]TOP-5AUC532 with PID 23344 (E:\JAVAProject\JAVAProject\[密钥已脱敏]y-t[密钥已脱敏]e-out\[密钥已脱敏]y-server\target\classes started by oscar in E:\JAVAProject\JAVAProject\[密钥已脱敏]y-t[密钥已脱敏]e-out)2024-09-27 17:32:34.716  INFO 23344 --- [           main] com.[密钥已脱敏]y.[密钥已脱敏]yApplication                   : The following 1 profile is active: "dev"2024-09-27 17:32:35.874  INFO 23344 --- [           main] .s.d.r.c.[密钥已脱敏] : Multiple Spring Data modules found, entering strict repository configuration mode2024-09-27 17:32:35.879  INFO 23344 --- [           main] .s.d.r.c.[密钥已脱敏] : Bootstrapping Spring Data Redis repositories in DEFAULT mode.2024-09-27 17:32:35.924  INFO 23344 --- [           main] .s.d.r.c.[密钥已脱敏] : Finished Spring Data repository scanning in 22 ms. Found 0 Redis repository interfaces.2024-09-27 17:32:36.758  INFO 23344 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 8080 (http)2024-09-27 17:32:36.767  INFO 23344 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]2024-09-27 17:32:36.767  INFO 23344 --- [           main] org.apache.catalina.core.StandardEngine  : Starting Servlet engine: [Apache Tomcat/9.0.65]2024-09-27 17:32:36.857  INFO 23344 --- [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded [密钥已脱敏]-09-27 17:32:36.857  INFO 23344 --- [           main] w.s.c.[密钥已脱敏] : Root [密钥已脱敏]: initialization completed in 2104 ms2024-09-27 17:32:36.972  INFO 23344 --- [           main] c.a.d.s.b.a.[密钥已脱敏] : Init DruidDataSource2024-09-27 17:32:37.092  INFO 23344 --- [           main] com.alibaba.druid.pool.DruidDataSource   : {dataSource-1} inited2024-09-27 17:32:37.317  INFO 23344 --- [           main] com.[密钥已脱敏]y.config.OssConfiguration          : 开始创建七牛云文件上传工具类对象:QiniuOssProperties(endpoint=s3.cn-north-1.qiniucs.com, [密钥已脱敏]Id=[密钥已脱敏], [密钥已脱敏]Secret=[密钥已脱敏], bucketName=[密钥已脱敏]y-kdb)2024-09-27 17:32:37.616  INFO 23344 --- [           main] com.[密钥已脱敏]y.config.WebMvcConfiguration       : 开始注册自定义拦截器...2024-09-27 17:32:37.719  INFO 23344 --- [           main] com.[密钥已脱敏]y.config.WebMvcConfiguration       : 准备生成接口文档...2024-09-27 17:32:37.756  INFO 23344 --- [           main] com.[密钥已脱敏]y.config.WebMvcConfiguration       : 扩展消息转换器...2024-09-27 17:32:37.761  INFO 23344 --- [           main] com.[密钥已脱敏]y.config.WebMvcConfiguration       : 开始设置静态资源映射...2024-09-27 17:32:38.434  INFO 23344 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http) with context path ''2024-09-27 17:32:38.661  INFO 23344 --- [           main] com.[密钥已脱敏]y.[密钥已脱敏]yApplication                   : Started [密钥已脱敏]yApplication in 4.397 seconds (JVM running for 5.161)2024-09-27 17:32:38.663  INFO 23344 --- [           main] com.[密钥已脱敏]y.[密钥已脱敏]yApplication                   : server started2024-09-27 17:32:52.113  INFO 23344 --- [nio-8080-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring DispatcherServlet 'dispatcherServlet'2024-09-27 17:32:52.113  INFO 23344 --- [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Initializing Servlet 'dispatcherServlet'2024-09-27 17:32:52.116  INFO 23344 --- [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Completed initialization in 3 ms当前线程的id：482024-09-27 17:32:52.133  INFO 23344 --- [nio-8080-exec-1] c.s.i.[密钥已脱敏]           : jwt校验:[REDACTED_JWT_TOKEN]2024-09-27 17:32:52.134  WARN 23344 --- [nio-8080-exec-2] o.s.web.servlet.PageNotFound             : No mapping for GET [密钥已脱敏]-09-27 17:32:52.241  INFO 23344 --- [nio-8080-exec-1] c.s.i.[密钥已脱敏]           : 当前员工id：2024-09-27 17:32:52.314  WARN 23344 --- [nio-8080-exec-3] o.s.web.servlet.PageNotFound             : No mapping for GET /ws/s8tp96fqw92024-09-27 17:32:52.445 DEBUG 23344 --- [nio-8080-exec-1] com.[密钥已脱敏]y.mapper.CategoryMapper.list       : ==>  Preparing: select * from category where status = 1 and type = ? order by sort asc,create_time desc2024-09-27 17:32:52.469 DEBUG 23344 --- [nio-8080-exec-1] com.[密钥已脱敏]y.mapper.CategoryMapper.list       : ==> Parameters: 1(Integer)2024-09-27 17:32:52.498 DEBUG 23344 --- [nio-8080-exec-1] com.[密钥已脱敏]y.mapper.CategoryMapper.list       : <==      Total: 8当前线程的id：512024-09-27 17:33:27.172  INFO 23344 --- [nio-8080-exec-4] c.s.i.[密钥已脱敏]           : jwt校验:[REDACTED_JWT_TOKEN]2024-09-27 17:33:27.173  INFO 23344 --- [nio-8080-exec-4] c.s.i.[密钥已脱敏]           : 当前员工id：2024-09-27 17:33:27.174  INFO 23344 --- [nio-8080-exec-4] c.[密钥已脱敏]y.controller.admin.CommonController  : 文件上传：org.springframework.web.multipart.support.[密钥已脱敏]$[密钥已脱敏]@12e31c582024-09-27 17:33:27.958 ERROR 23344 --- [nio-8080-exec-4] com.[密钥已脱敏]y.utils.QiniuOssUtil               : 文件上传失败: {ResponseInfo:com.qiniu.http.Response@145f980f,status:401, reqId:xdcAAADgnEUUEPkX, xlog:X-Log, xvia:, adress:upload.qiniup.com/[IP已脱敏]:443, duration:0.636000 s, error:bad token}2024-09-27 17:33:27.958 ERROR 23344 --- [nio-8080-exec-4] com.[密钥已脱敏]y.utils.QiniuOssUtil               : {"error":"bad token","error_code":"BadToken"}2024-09-27 17:33:27.959  INFO 23344 --- [nio-8080-exec-4] com.[密钥已脱敏]y.utils.QiniuOssUtil               : 文件上传到:[URL已脱敏] 17:33:34.293  INFO 23344 --- [nio-8080-exec-5] c.s.i.[密钥已脱敏]           : jwt校验:[REDACTED_JWT_TOKEN]2024-09-27 17:33:34.294  INFO 23344 --- [nio-8080-exec-5] c.s.i.[密钥已脱敏]           : 当前员工id：2024-09-27 17:33:34.319  INFO 23344 --- [nio-8080-exec-5] com.[密钥已脱敏]y.controller.admin.DishController  : 新增菜品：DishDTO(id=null, name=测试菜品, categoryId=17, price=15, image=[URL已脱敏] description=123, status=0, flavors=[DishFlavor(id=null, dishId=null, name=甜味, value=["无糖","少糖","半糖","多糖","全糖"]), DishFlavor(id=null, dishId=null, name=温度, value=["热饮","常温","去冰","少冰","多冰"])])2024-09-27 17:33:39.159  INFO 23344 --- [nio-8080-exec-5] com.[密钥已脱敏]y.service.impl.DishServiceImpl     : 新增菜品：DishDTO(id=null, name=测试菜品, categoryId=17, price=15, image=[URL已脱敏] description=123, status=0, flavors=[DishFlavor(id=null, dishId=null, name=甜味, value=["无糖","少糖","半糖","多糖","全糖"]), DishFlavor(id=null, dishId=null, name=温度, value=["热饮","常温","去冰","少冰","多冰"])])2024-09-27 17:33:40.040  INFO 23344 --- [nio-8080-exec-5] com.[密钥已脱敏]y.aspect.AutoFillAspect            : 开始进行公共字段的填充...2024-09-27 17:33:40.053 DEBUG 23344 --- [nio-8080-exec-5] com.[密钥已脱敏]y.mapper.DishMapper.insert         : ==>  Preparing: insert into dish(name, category_id, price, image, description, create_time, update_time, create_user, update_user,status) VALUES (?,?,?,?,?,?,?,?,?,?)2024-09-27 17:33:40.057 DEBUG 23344 --- [nio-8080-exec-5] com.[密钥已脱敏]y.mapper.DishMapper.insert         : ==> Parameters: null, null, null, null, null, null, null, null, null, null
**客服**：您好，java的话，直接使用maven pom.xml 引入依赖或者 gradle import 依赖maven 安装依赖建议手动引入依赖包，导入需要的版本[URL已脱敏] uploadToken 生成tokneString upToken = auth.uploadToken(bucket);上传参考这个试下[URL已脱敏]
**客户**：2024-09-27 18:11:25.775 ERROR 5616 --- [nio-8080-exec-3] com.[密钥已脱敏]y.utils.QiniuOssUtil               : 文件上传失败: {ResponseInfo:com.qiniu.http.Response@3a0af29e,status:400, reqId:JHkAAAD--a8mEvkX, xlog:X-Log, xvia:, adress:upload.qiniup.com/[IP已脱敏]:443, duration:0.343000 s, error:incorrect region, please use up-z1.qiniup.com, bucket is: [密钥已脱敏]y-kdb}2024-09-27 18:11:25.775 ERROR 5616 --- [nio-8080-exec-3] com.[密钥已脱敏]y.utils.QiniuOssUtil               : {"error":"incorrect region, please use up-z1.qiniup.com, bucket is: [密钥已脱敏]y-kdb"}仍然显示上传失败，我所有都检查了一边
**客服**：incorrect region, please use up-z1.qiniup.com——这个报错说明是上传域名和空间所在的区域不匹配，多发生在旧的sdk、工具和插件上。后面的 xxx.qiniu.com是正确的上传域名。存储区域和上传域名的对应关系见[URL已脱敏]
**客户**：收到
**客服**：嗯嗯好的

### 根本原因分析

网络波动导致上传不稳定，建议使用断点续传功能

---

## 15. CDN 流量封顶策略

**问题分类**: CDN｜其他类咨询

### 问题描述

我们这个 CDN流量 ，回源流量有封顶策略吗？或者其它什么限制

### 客服解答

**客户**：我们这个 CDN流量 ，回源流量有封顶策略吗？或者其它什么限制
**客服**：您好，没有流量封顶策略CDN上支持多种防盗链配置，不同的防盗链适用于不同的应用场景，建议可以在 cdn => 域名管理 => 配置 => 访问控制 中设置1：referer防盗链： 只有携带了相应referer 请求头 的 http请求才能访问资源，但是对于技术来说，referer都是可以伪造的，存在一定的风险2：时间戳防盗链，url带着e和token参数访问，e为过期时间，但是只要捕获到了url就可以访问资源了，只适用于访问xx次的场景3：回源鉴权，这个你们可以尝试下，每次访问cdn图片时，会携带你们自己定义的访问参数去你们自己的服务器上鉴权，只有你们服务器鉴权通过，返回 httpcode=200 ，才会将图片资源给用户访问，否则无法返回图片4：IP黑白名单，这个适合某一个网段内的ip访问资源，不适合官网使用，只有在 ip 白名单中的用户才可以访问你们的图片参考文档：[URL已脱敏]
**客户**：这个是针对CDn的下行注流量吧，回源流量有没有效呢？我看回源流量划分到对象存储里面的
**客服**：您好，回源流量是cdn没有缓存时，回源请求产生的流量，限制cdn就能限制到回源流量。

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 16. 空间绑定源站域名一直是‘未配置’状态

**问题分类**: 对象存储｜其他类咨询

### 问题描述

我在【域名管理】中绑定了一个子域名 image.yqsj.net在服务器DNS上做了cname解析，为什么一直提示‘未配置’ 呢？恳请指点，谢谢！

### 客服解答

**客户**：我在【域名管理】中绑定了一个子域名 image.yqsj.net[图片]在服务器DNS上做了cname解析，[图片]为什么一直提示‘未配置’ 呢？恳请指点，谢谢！
**客服**：您好，主机名称 修改成 image
**客户**：服务器DNS解析添加cname主机名称是 image 没错啊,  还是指另外哪个地方的主机名称要改？
**客服**：您好，修改为单image
**客户**：[图片]是这个地方修改吗？
**客服**：您好，嗯嗯是的，您这边再确认看下是否有开启过代理呢？
**客户**：没有代理。 始终不成功。换成自定义加速域名也一样，CNAME始终是未配置状态。会不会是网站没有备案的原因？[图片]
**客服**：您好，这个和网站备案没有关系的，这边看解析是未解析到的，您这边咨询一下域名厂商这边，为什么解析未生效image.yqsj.net﻿[图片]

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 17. oss镜像存储能混合使用吗

**问题分类**: 对象存储｜其他类咨询

### 问题描述

下行流量用别家公司的

### 客服解答

**客户**：下行流量用别家公司的
**客服**：您好，稍等
**客服**：您好是支持混合使用的

### 根本原因分析

具体问题需要根据实际场景分析

---

## 18. 怎么这么久了 用户点击链接 还是黑屏？

**问题分类**: CDN｜访问下载

### 问题描述

为什么有很多用户 反映 打开是黑屏状态 这个问题很久了 一直不解决 隔一段时间 就出现这个问题 为什么？？？？？？？

### 客服解答

**客户**：为什么有很多用户 反映 打开是黑屏状态 这个问题很久了 一直不解决 隔一段时间 就出现这个问题 为什么？？？？？？？
**客户**：非逼着我 换一家平台吗 ？
**客户**：到底能不能行  一直在看的客户 突然今天看不了 点开就是黑屏状态 今天出现黑屏人数最起码有几十个
**客户**：速度能解决吗
**客服**：您好这边没有复现您的情况，麻烦搜集下 无法播放的错误信息（请求头、响应头、状态码等信息给下）--- 浏览器右键打开检查模式，在network中获取 以及 对应客户端ip、请求时间，这边具体看下
**客户**：[URL已脱敏]
**客户**：还有这一条链接也是 烦死人
**客户**：用户是用手机观看的
**客户**：不能解决 就吧账户里面的钱退给我 然后我换一家
**客服**：您好，用户这边是什么设备 安卓还是ios
**客户**：大部分安卓 都是60-80岁的客户，客户无法配合，反映的就是打不开
**客服**：您好，发生这种情况的用户这边有什么相同点吗，比如区域相同、设备相同等
**客户**：1[图片]
**客户**：这是今天突然反馈到我这边的 而且这客户是每天观看的  就刚刚不久 突然有部分客户反馈黑屏 [图片][图片]
**客户**：人家一共才百来号个会员  点开看的就只有五十人左右  就有七八个不能看
**客户**：用户60-80岁的爷爷奶奶 问他们 他们都不懂 之说不能观看
**客户**：这绝对是你们的问题了 我有三个后台 三个部门 不同服务器 不同域名 同一时间 反馈有很多用户看不了 打开就是黑屏
**客户**：唯一相同的是 全部 cnd 用的是你们的
**客服**：能不能让客户访问下iP地址查询--手机号码查询归属地 | 邮政编码查询 | iP地址归属地查询 | 身份证号码验证在线查询网 (ip138.com)这个地址截图获取下IP地址，我们这边查下日志信息，才能进行排查
**客户**：139.226.122.37223.68.117.12636.161.74.24442.238.158.168
**客户**：我用后台获取过 用户 IP 这只是看不了课的用户 我随便抽的 发给你的
**客服**：好的
**客户**：如果是我们后台搭建的有问题 不会在同一时间突然大批量出现这个问题 因为我们三个后台都是分开的服务器 域名
**客服**：正在排查
**客户**：朋友能快点不 我已经在挨吊了
**客户**：三个部门嘴巴像机关枪一样在扫射我
**客服**：[URL已脱敏]
**客户**：不可以 转圈
**客户**：有的客户 又可以看 有的又不能看
**客服**：稍等
**客服**：从您提供的ip上来查询日志，没有查询到有请求记录，看让客户切个网络环境再去访问看下呢？
**客户**：回复了 有一个人说 在微信直接点链接 就能看 但是通过别的方式不行
**客服**：[URL已脱敏]
**客户**：什么意思  现在怎么解决 技术又下班了
**客服**：能否联系上技术，问下资源什么时候上传到
**客户**：你看下[图片]
**客户**：你指的资源是什么 是什么时候把视频传到七牛云上面的吗
**客服**：是的
**客服**：可以让客户换个浏览器，用资源链接访问看下，看看返回的信息是不是 document not found
**客户**：不好意思[图片]
**客户**：技术回我了
**客服**：是的，这个链接下的资源不存在了，能访问的客户其实是访问到了缓存
**客户**：我的
**客服**：您那边处理看下，后续有问题再反馈
**客户**：不好意思，刚刚是我太大声了
**客服**：没关系的，您那边先处理看下能否恢复，后续还有问题反馈工单即可
**客户**：没问题了
**客服**：您好，嗯嗯好的

### 根本原因分析

域名配置或解析问题

---

## 19. 图片上传失败

**问题分类**: 对象存储｜上传下载

### 问题描述

使用鸿蒙sdk上传图片的时候，把选的图片保存到沙箱里面，然后把图片路径拼到成 internal://files/文件名 这样，再使用UploadFile.fromUri创建上传数据，然后上传失败，报错Unsupported uri schema type，我应该怎么解决这个错误，怎么对上传的图片进行格式转换

### 客服解答

**客户**：[图片][图片][图片]使用鸿蒙sdk上传图片的时候，把选的图片保存到沙箱里面，然后把图片路径拼到成 internal://files/文件名 这样，再使用UploadFile.fromUri创建上传数据，然后上传失败，报错Unsupported uri schema type，我应该怎么解决这个错误，怎么对上传的图片进行格式转换
**客服**：您好，您稍等这边确认一下
**客服**：您好， internal://协议的uri不支持，sdk目前支持file://和datashare://协议的url
**客服**：您好， internal://协议的uri不支持，sdk目前支持file://和datashare://协议的uri
**客户**：我把 internal://files/ 文件名改成了 file://files/文件名  报错{"name":"FileSystemError","message":"No such file or directory"}改成 datashare://files/文件名 报错{"name":"FileSystemError","message":"Invalid argument"}。请问有没有什么解决方案
**客服**：您是用什么方式获取的uri呢，这个一般不是都是用系统api获取吗或者您可以尝试用path上传试试
**客户**：[图片]是的，我是用相机拍的图片，但是获取到的uri是number类型Picke
**客户**：我用相机拍到的图片是这样的：file:[密钥已脱敏]_1727432085_170/IMG_20240927_181305.jpg，我用UploadFile.fromUri()传入这个uri,上传的时候报错{"name":"HttpRequestError","message":"key doesn't match with scope"}
**客服**：您好key doesn't match scope 表示上传文件指定的 key 和上传 token 中，putPolicy 的 scope 字段不符。上传指定的 key 必须跟 scope 里的 key 完全匹配或者前缀匹配。比如这里 token 里面 "scope":"lookbook-server-img:img/21c6da89"  key是 img/21c6da89
**客户**：[图片][图片]不知道这种用法对不对，还是要怎么用
**客服**：您把上传token发一下
**客户**："token":{"bucket":"image","asses[密钥已脱敏]ey":"[REDACTED_LONG_KEY]","signature":"[密钥已脱敏]:[密钥已脱敏]:[密钥已脱敏]","deadline":1727436700},
**客服**：{"scope":"image:[密钥已脱敏].jpg","deadline":1727436700}上传token里的 scope 参数跟了个 [密钥已脱敏].jpg的key。所以您上传的key也要传[密钥已脱敏].jpg才行如 const fileData: UploadFile = UploadFile.fromUri(uri2)  fileData.key = "[密钥已脱敏].jpg";如果上传代码不处理就要把token里的[密钥已脱敏].jpg去掉如{"scope":"image","deadline":1727436700}具体详情参考文档[URL已脱敏]
**客户**：现在fileDatd:设置成了这样了{"type":"uri","data":"file:[密钥已脱敏]_1727436948_178/IMG_20240927_193408.jpg","key":"[密钥已脱敏].jpg","mimeType":"image/jpg"}结果还是报：key doesn't match with scope报错里面的token是这样的："token":{"bucket":"image","asses[密钥已脱敏]ey":"[REDACTED_LONG_KEY]","signature":"[密钥已脱敏]:[密钥已脱敏]:[密钥已脱敏]","deadline":1727440448}
**客服**：您好，{"scope":"image:[密钥已脱敏].jpg","deadline":1727440448}您可以将token内的key去掉看下，像这样{"scope":"image","deadline":1727440448}
**客户**：[图片]我这里只看到了上传的数据和上传的配置，上传的数据里面只有{"type":"uri","data":"file:[密钥已脱敏]_1727436948_178/IMG_20240927_193408.jpg","key":"[密钥已脱敏].jpg","mimeType":"image/jpg"} 这些，没看到有scope、imgage、token这些属性，请问这是在哪里改的
**客服**：您好，您这边测试一下将key先指定为空看下
**客户**：上传的数据：{"type":"uri","data":"file:[密钥已脱敏]_1727438864_181/IMG_20240927_200604.jpg","key":"","mimeType":"image/jpg"}图片上传失败：{"name":"HttpRequestError","message":"key doesn't match with scope","reqId":"rDwAAAAnhaJnGPkX","token":{"bucket":"image","asses[密钥已脱敏]ey":"[REDACTED_LONG_KEY]","signature":"[密钥已脱敏]:[密钥已脱敏]:[密钥已脱敏]","deadline":1727442365}
**客服**：您好，这边看您的token还是这个的，说明您这边还是指定了key的，目前工程师不在需要明天白天帮您确认一下的，还请耐心等待一下{"scope":"image:[密钥已脱敏].jpg","deadline":1727442365}
**客户**：好的，这边的参数就两个，上传的数据和配置，您说的的这个{"scope":"image:[密钥已脱敏].jpg","deadline":1727442365} 我这里看不到，可能是在服务器上的，在服务器上我是改不了，除了鸿蒙端，其他端的是在正常使用的，所以麻烦您这边的工程师在的时候帮我确认一下，看看我这里的配置哪里有问题
**客服**：您好，嗯嗯好的还请耐心等待一下
**客户**：我今天按照您说的把token里面scope的key去掉了，把上传的的数据里面的key也去掉了，结果报错{"name":"HttpRequestError","message":"bad auth","reqId":"P_0AAACrtU3OWfkX"}上传的数据：{"type":"uri","data":"file:[密钥已脱敏]_1727510774_220/IMG_20240928_160434.jpg","mimeType":"image/jpg"}报错里面的token："token":{"bucket":"image","asses[密钥已脱敏]ey":"[REDACTED_LONG_KEY]","signature":"[密钥已脱敏]:[密钥已脱敏]:[密钥已脱敏]","deadline":1727514274}[图片]
**客服**：您好，请稍等
**客服**：您好，你们这几个token生成的不对哈，你们这个token 是使用的什么服务端域名SDK生成的呢
**客户**：用Java的SDK生成的，但是我们这边安卓和ios的都能用
**客服**：那您重新生成token测试看下，如果还是不行把报错信息和token再发给我一下，然后您这边方便让我这边用您的上传token上传试试吗
**客户**：好的，稍等
**客户**：可以了，我在tokenProvider这个参数里面调用接口去获取token后返回不行，先在外面调用接口去获取token和key,然后在tokenProvider里面直接返回事先获取到的token就可以了，不知道是哪里的代码写得有问题，或者说应该就是这样的[图片]
**客服**：嗯嗯好的
**客服**：这样的话您事先获取到token和key就可以了，建议是实现获取到token和key
**客户**：嗯嗯，我现在就是这样子做的，已经实现了。谢谢解答

### 根本原因分析

网络波动导致上传不稳定，建议使用断点续传功能

---

## 20. 我们证书要到期了，能不能延期一周

**问题分类**: CDN｜证书问题

### 问题描述

我们SSL证书要到期了，能不能延期一周，老板不在公司

### 客服解答

**客户**：我们SSL证书要到期了，能不能延期一周，老板不在公司
**客服**：您好，很抱歉，证书无法延期的手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免[URL已脱敏]
**客户**：[图片]你好，我已经上传ssl证书，下一步应该做什么呢？
**客户**：这里还是显示不足30天[图片]
**客服**：您好，点下这个部署[图片]

### 根本原因分析

SSL证书配置或过期问题

---

## 21. 七牛云API问题

**问题分类**: 对象存储｜其他类咨询

### 问题描述

自定义源站域名更新SSL的API接口未找到

### 客服解答

**客户**：自定义源站域名更新SSL的API接口未找到
**客服**：您好，十分抱歉目前这边没有自定义源站域名更新SSL的API接口
**客户**：那有无API可以绑定新的证书，比如我上传了两个证书到证书管理里面，有无API接口可以让我切换，从一个变成另一个
**客服**：您好，自定义源站域名只能手动操作的，目前没有这个接口的
**客户**：也就是说自定义源站域名的SSL无任何API接口，可以上传新证书，或者更改到其他的证书
**客服**：您好，账号上传证书接口可以参考下这个，其他证书相关的接口只有这些[URL已脱敏]
**客户**：SDK内有无这个接口
**客服**：您用的是哪个语言的sdk
**客户**：哪个语言有我就用哪个语言
**客服**：上传证书可以参考# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http
import json
# 需要填写七牛账号的 Access Key 和 Secret Key
access_key = "<access_key>"
secret_key = "<secret_key>"
auth = QiniuMacAuth(access_key, secret_key)
# 请求URL
url = "[URL已脱敏]
# 请求体
body = {
    "name": "xxxxxx",
    "common_name": "xxxxx",
    "pri": "xxxxxx",
    "ca": "xxxxxx"
}
ret, res = http._post_with_qiniu_mac(url, body, auth)
headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log, "text_body": res.text_body}
print(json.dumps(headers, indent=4, ensure_ascii=False))
print(json.dumps(ret, indent=4, ensure_ascii=False))
**客户**：这是OSS自定义源站域名那个ssl吧
**客服**：上传证书目前只有这个demo 您参考下

### 根本原因分析

SSL证书配置或过期问题

---

## 22. 1

**问题分类**: 对象存储｜上传下载

### 问题描述

老帐号找不到了

### 客服解答

**客户**：老帐号找不到了
**客服**：您好，有之前账号的邮箱，手机号，等信息吗

### 根本原因分析

具体问题需要根据实际场景分析

---

## 23. 一直卡在处理中

**问题分类**: CDN｜证书问题

### 问题描述

证书过期后   我重新申请了   然后配置进去了    一直卡在处理中

### 客服解答

**客户**：证书过期后   我重新申请了   然后配置进去了    一直卡在处理中
**客服**：您好，您稍等这边在确认中了
**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。
**客户**：好吧，谢谢
**客服**：您好，嗯嗯不客气的

### 根本原因分析

SSL证书配置或过期问题

---

## 24. 域名失误注销备案了,重新备案期间是否可以继续使用

**问题分类**: CDN｜其他类咨询

### 问题描述

域名失误注销备案了,重新备案期间是否可以继续使用

### 客服解答

**客户**：域名失误注销备案了,重新备案期间是否可以继续使用
**客服**：您好，根据国家政策规定，这边无法提供服务给未备案域名，需要您重新备案成功之后恢复
**客服**：您域名如果必须要使用的话，可以将域名覆盖调整到海外，海外可以未备案但是国内访问会产生跨境，访问不稳定
**客户**：域名已经恢复备案了,请解除冻结
**客户**：请解除已经冻结的域名[图片]
**客户**：有人没有

### 根本原因分析

域名配置或解析问题

---

## 25. 流量盗刷如何彻底限制？

**问题分类**: CDN｜其他类咨询

### 问题描述

已经设置了各种访问控制了，为什么还是会有盗刷的，怎么样才能绝对根除呢？已经被盗刷了几万G的流量了

### 客服解答

**客户**：已经设置了各种访问控制了，为什么还是会有盗刷的，怎么样才能绝对根除呢？已经被盗刷了几万G的流量了[图片]
**客服**：您好，麻烦将域名文本发工单，这边看下
**客户**：cdn.jifenyouhuidui.com这个域名哈还有就是刚刚改了点配置，然后现在还在队列中，也帮忙处理下嘞
**客服**：稍等
**客服**：ipv6 是必须的吗，也可以采用 v4，v4可以封禁网段，好屏蔽多ip变动访问这种另外，被访问的资源是否删除或者禁用，或是改名另外，处理后的资源，cdn 缓存是要清理的，打开这个页面，文件刷新，将被大量访问的 url 输入进行刷新缓存[URL已脱敏]

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 26. 短信收不到

**问题分类**: 云短信｜短信发送问题

### 问题描述

短信收不到 手机号码 [REDACTED_PHONE]

### 客服解答

**客户**：短信收不到 手机号码 [REDACTED_PHONE]
**客户**：啥情况 之前都可以
**客服**：您好，您稍等这边确认一下
**客服**：您好，这边看您的签名的问题导致的，需要您这边提供一下您的营业执照和法人的身份证照片才行的
**客户**：我这个签名是你们平台审核过了的哟
**客户**：难道要重新申请签名？
**客服**：您好，嗯嗯是的，运营商这边反馈需要重新报备一下的
**客户**：证件传过来了[图片][图片][图片]
**客服**：您好，您稍等这边帮您报备一下
**客户**：好的 可以了 给我 回复一下哈
**客服**：您好，嗯嗯这边运营商反馈明天周末得后天给报备了的，还请耐心等待一下的
**客服**：您好，这边已经为您报备了，您这边后续可以看下是否恢复了的
**客户**：我们这边已经报备了之前 怎么短信模板还是审核不过呀？
**客服**：您最新一个模版是今天创建的根据工信部和运营商要求，需要做企业实名认证，请在签名处提交签名对应的营业执照，法人身份证号，及营业执照盖章 请提供签名和公司关联，如小程序，app,软著等
**客户**：需要新建签名重新弄吗？
**客服**：是的 注意提交签名对应的营业执照，法人身份证号，及营业执照盖章 请提供签名和公司关联，如小程序，app,软著等

### 根本原因分析

企业认证需要提供社会信用代码或营业执照号

---

## 27. CDN 缓存了 404 的结果

**问题分类**: CDN｜其他类咨询

### 问题描述

用户场景：用户上传视频之后，会触发 OSS 对象存储的自动截帧任务生成视频封面。问题：如果在视频上传之后，但在视频封面生成之前，这个时候用户访问这个视频封面会发得到 404 返回值，并且 CDN 会缓存该 404 结果。导致用户在较长时间内都无法访问到该封面，尽管视频封面已经生成。请问是否有什么解决方案可以解决上述 CDN 缓存的问题？

### 客服解答

**客户**：用户场景：用户上传视频之后，会触发 OSS 对象存储的自动截帧任务生成视频封面。问题：如果在视频上传之后，但在视频封面生成之前，这个时候用户访问这个视频封面会发得到 404 返回值，并且 CDN 会缓存该 404 结果。导致用户在较长时间内都无法访问到该封面，尽管视频封面已经生成。请问是否有什么解决方案可以解决上述 CDN 缓存的问题？
**客服**：您好，您这边可以看下将这个文件的类型的缓存设置为0秒缓存看下
**客户**：如果设置成 0 秒是不是这个类型的CDN缓存就失效了？我只想将这个类型的 404 结果不缓存
**客服**：您好，嗯嗯是的，那这个目前是没有办法的

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 28. 内容审核反馈API

**问题分类**: 人工智能｜内容安全

### 问题描述

现在开启了内容识别，误报很多，知道图片无法显示，是否有API能够反馈结果？

### 客服解答

**客户**：现在开启了内容识别，误报很多，知道图片无法显示，是否有API能够反馈结果？
**客服**：您好，您这边可以在控制台确认一下的，目前的话只有使用API审核处理的资源才能返回结果的[URL已脱敏]

### 根本原因分析

具体问题需要根据实际场景分析

---

## 29. 为何归档生命周期设置后不生效

**问题分类**: 对象存储｜镜像存储

### 问题描述

空间生命周期设置自动归档不生效

### 客服解答

**客户**：空间生命周期设置自动归档不生效
**客服**：您好，生命周期规则设置成功后，仅对新上传的文件有效果，空间内旧有文件不会通过生命周期规则执行变更。生命周期规则设置成功后，新上传的文件，会在设置在xx天后的当天内删除文件。当portal中设置对整个空间生效的生命周期规则，接口或SDK中设置了单个文件生命周期规则，其接口或SDK中单个文件的生命周期设置优先级最高详情参考：[URL已脱敏]
**客户**：归档后的文件还可以访问吗？然后价格是怎么算的
**客服**：您好，归档文件必须是解冻之后才能访问，不能直接访问归档计费单价您参考这里[URL已脱敏]
**客户**：有办法自动触发解冻吗？比如归档后用户又突然访问了这个文件
**客服**：您好，这个没有的，这个需要您主动调用接口
**客户**：好的
**客服**：好的

### 根本原因分析

对象存储配置或使用问题

---

## 30. 域名防盗链配置处理时间长

**问题分类**: CDN｜配置问题

### 问题描述

您好，有几件事想麻烦您。一、我提交了开启防盗链设置，已经过去几小时了还没好，能否帮忙通过防盗链修改，谢谢！二、想咨询下黑名单的问题。我之前设置了单 IP 访问阈值，如果某个 IP 短时间内访问频率过高，就封禁几小时的。请问： 我自己能看到封禁了什么 IP 吗？我能取消封禁吗？三、能否帮我先取消所有封禁（因为我自己好像被封了）， 并帮我调整QPS 阈值为：30s 内访问 100次 ，封禁 8 小时

### 客服解答

**客户**：您好，有几件事想麻烦您。一、我提交了开启防盗链设置，已经过去几小时了还没好，能否帮忙通过防盗链修改，谢谢！二、想咨询下黑名单的问题。我之前设置了单 IP 访问阈值，如果某个 IP 短时间内访问频率过高，就封禁几小时的。请问： 我自己能看到封禁了什么 IP 吗？我能取消封禁吗？三、能否帮我先取消所有封禁（因为我自己好像被封了）， 并帮我调整QPS 阈值为：30s 内访问 100次 ，封禁 8 小时
**客服**：您好，这边帮您确认一下您这边看不到的暂无取消封禁的配置的这个暂无法取消的，十分抱歉的30s 内访问 100次 ，封禁 8 小时这边这边帮您反馈一下
**客户**：好的，多谢了，明晚我再测试 QPS 的设置后效果吧
**客服**：您好，嗯嗯好的

### 根本原因分析

具体问题需要根据实际场景分析

---

## 31. 一直在处理中卡住不动

**问题分类**: CDN｜配置问题

### 问题描述

能不能停止处理，我的删除啊

### 客服解答

**客户**：能不能停止处理，我的删除啊 [图片]
**客服**：您好，麻烦辛苦您这边重新申请一下新证书，这边未找到您的订单，您这边是否有删除过您的证书订单呢

### 根本原因分析

SSL证书配置或过期问题

---

## 32. 我的云存储的数据，必须要备案才可以用吗

**问题分类**: 对象存储｜上传下载

### 问题描述

我的云存储的数据，必须要备案才可以用吗如果不备案，可以使用系统自带的域名进行访问吗或者使用非大陆服务器访问？

### 客服解答

**客户**：我的云存储的数据，必须要备案才可以用吗如果不备案，可以使用系统自带的域名进行访问吗或者使用非大陆服务器访问？
**客服**：您好，国内存储的话需要绑定备案域名的，您可以创建一个海外存储空间的，让绑定一个未备案的域名走海外的，海外不需要备案的测试域名30天后会回收的
**客户**：必须要新创建空间吗  已经创建的空间可以改成 你说的海外存储吗
**客服**：您好，不支持的
**客户**：海外上传这么慢的吗[图片]
**客户**：[URL已脱敏]   我测试了一下 ，为啥打不开呢
**客服**：您好，这边测试看可以打开[图片]
**客户**：[URL已脱敏]  一个图片打开 要  10秒钟 左右？ 这个不太正常吧
**客户**：我选择的是新加坡 是不是这个位置比较慢？选择国外哪个位置会比较快呢
**客服**：您好，国内访问海外的话慢是符合预期的，您这边多访问几次拉取到缓存后会快些，您这边需要是业务需要的话，需要保证速度的话建议还是先给域名进行备案走国内的
**客户**：使用cdn域名和源站域名哪一个更好呢？这个我不太懂区别，是不是cdn域名要额外收费，然后国内访问速度会更快？
**客户**：另外再问下 不同地区的价格 有啥区别么 ，价目表在哪里可以看北美和新加坡  比如。
**客服**：您好，CDN域名和源站域名都会计费，CDN比原则域名便宜一些定价[URL已脱敏]
**客户**：如果我用国内的，但是我的域名没有备案，我只是用来存数据，比如我在宝塔用来备份网站数据到 七牛，不对外开启访问，就是自己下载，这样可以不备案使用国内位置的存储吗
**客服**：您好，如果不访问不下载可以存储的，上传到国内存储即可的，但是不绑定域名的话无法访问无法下载的，访问和下载是需要走域名的，所以有下载需求还是需要绑定备案域名的
**客户**：有没有办法可以下载整个空间里面的所有文件的 方法？比如压缩包一下  在下载？[图片]
**客服**：您好，七牛后台界面操作不支持批量下载的，批量下载，可以通过以下几种方式实现：方法1.调用list接口，遍历空间，获得空间内的文件信息，然后下载。代码逻辑是先调用 list 接口获得文件名的集合，再与空间域名拼接成url([URL已脱敏] 是空间域名，key是文件名)，循环调用 download 方法下载文件。[URL已脱敏] qshell 工具进行批量下载操作；qshell 工具下载地址：[URL已脱敏] 工具批量下载命令：[URL已脱敏] 的 qdownload 命令时，如果指定使用CDN域名下载时，建议将 public 参数置为true，下载时击中CDN缓存时产生CDN流量费用，未击中CDN缓存回源下载资源时产生的是CDN回源流量费用；如不指定，下载资源产生的全部是CDN回源流量费用。方法3:使用图形化工具kodo browser工具批量下载，勾选想要下载的文件/目录后点击【下载】即可。参考：[URL已脱敏]
**客户**：有压缩的功能吗 我这里的小文件比较多。
**客服**：没有打包压缩的功能

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 33. 请问咱们这个CDN流量1T或者是5T，半年或1年，指的是总共的还是每月会复位？

**问题分类**: CDN｜流量计费问题

### 问题描述

请问咱们这个CDN流量1T或者是5T，半年或1年，指的是总共的还是每月会复位？我不是技术，先咨询一下

### 客服解答

**客户**：请问咱们这个CDN流量1T或者是5T，半年或1年，指的是总共的还是每月会复位？我不是技术，先咨询一下
**客服**：您好，CDN流量包的话是总量的，用完就没了的

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 34. 证书部署 HTTPS 配置一直显示处理中

**问题分类**: CDN｜配置问题

### 问题描述

新证书（ID：[密钥已脱敏]）在部署过程中配置域名 static.ymlinks.com，img.ymlinks.com 一直显示处理中，按系统提示，正常时间只需要8-15分钟，目前没有相关操作反馈，且涉及到APP中图片无法正常正式，望给予相关支持。谢谢

### 客服解答

**客户**：新证书（ID：[密钥已脱敏]）在部署过程中配置域名 static.ymlinks.com，img.ymlinks.com 一直显示处理中，按系统提示，正常时间只需要8-15分钟，目前没有相关操作反馈，且涉及到APP中图片无法正常正式，望给予相关支持。谢谢[图片][图片]
**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

SSL证书配置或过期问题

---

## 35. 流量咨询

**问题分类**: 对象存储｜其他类咨询

### 问题描述

标准存储CDN回源流出流量-华东-浙江跟CDN-HTTP-中国大陆具体有啥区别，为啥两个都要计费

### 客服解答

**客户**：标准存储CDN回源流出流量-华东-浙江跟CDN-HTTP-中国大陆具体有啥区别，为啥两个都要计费
**客服**：您好，CDN是用户的访问流量您这边CDN回源流量的话可以参考下这个文档的[URL已脱敏]

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 36. 对象迁移失败

**问题分类**: 对象存储｜数据迁移

### 问题描述

[密钥已脱敏] 为什么我这个对象迁移任务失败了

### 客服解答

**客户**：[密钥已脱敏] 为什么我这个对象迁移任务失败了
**客服**：您好，您这边看下任务迁移的失败原因是什么呢？

### 根本原因分析

具体问题需要根据实际场景分析

---

## 37. 无法删除CDN

**问题分类**: CDN｜其他类咨询

### 问题描述

无法删除CDN的域名 ai-www-cdn.mq1234.com 一直在配置中

### 客服解答

**客户**：无法删除CDN的域名 ai-www-cdn.mq1234.com 一直在配置中[图片]
**客服**：您好这边帮您手动介入处理下 请稍等
**客服**：目前已经处理完成 需要删除的话 可以点击停用删除

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 38. CDN一直在配置

**问题分类**: CDN｜其他类咨询

### 问题描述

域名cdn-www.gdy1234.com的CDN一直在配置

### 客服解答

**客户**：域名cdn-www.gdy1234.com的CDN一直在配置
**客服**：您好这边帮您手动介入处理下 请稍等
**客服**：已经处理完成

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 39. 阿里云二级域名如和申请证书

**问题分类**: CDN｜证书问题

### 问题描述

您好，我不知道阿里云二级域名如何申请SSL证书，我按照文档七牛云文档申请的不知道对不对，现在卡在了域名所有权验证未通过 ，订单状态为【待确认】环节，麻烦您帮我看一下，谢谢！

### 客服解答

**客户**：您好，我不知道阿里云二级域名如何申请SSL证书，我按照文档七牛云文档申请的不知道对不对，现在卡在了域名所有权验证未通过 ，订单状态为【待确认】环节，麻烦您帮我看一下，谢谢！
**客服**：您好麻烦粘贴一下您的dns配置截图 这边看下
**客户**：[图片]我是域名备案主体是个体工商户，七牛云是我个人我需要将七牛云认证为企业吗？
**客服**：您好，您能提供下在域名服务商处的cname解析信息吗
**客服**：您好，您目前绑定的域名已经有A记录解析到您的网站IP了，再做七牛的CNAME会有解析冲突。[URL已脱敏] A 记录和 CNAME 解析。1. 重新添加，一个未使用过未解析过的二级域名，直接做CNAME解析，例如您原本在七牛绑定的是 xxx.com ，这个时候您重新绑定一个 cdn.xxx.com 到七牛，然后配置这个域名对应的解析即可。2. 删除您直接的A记录就可做CNAME解析(注意：A记录删除会导致您域名中的内容无法访问，需要谨慎操作)
**客户**：[图片][图片]一个是阿里云的，一个七牛云，我不确定这么配置对不
**客服**：您好，主机记录应该为：_[密钥已脱敏].ng.uyiben.cn
**客户**：大概多久提示域名所有权验证通过
**客服**：您这边配置好后，点击验证就可以显示结果

### 根本原因分析

企业认证需要提供社会信用代码或营业执照号

---

## 40. 多媒体样式最大只能500M么

**问题分类**: 对象存储｜其他类咨询

### 问题描述

多媒体样式最大视频文件只能是500M么

### 客服解答

**客户**：多媒体样式最大视频文件只能是500M么[图片]
**客服**：您好，是的

### 根本原因分析

具体问题需要根据实际场景分析

---

## 41. 验证码

**问题分类**: 云短信｜短信发送问题

### 问题描述

刚刚注册，你们送了300条短信，但还是收不到验证码

### 客服解答

**客户**：刚刚注册，你们送了300条短信，但还是收不到验证码[图片]
**客服**：您好短信发送前要提交签名审核报备和模版审核 这些审核通过才能发短信步骤参考 [URL已脱敏]

### 根本原因分析

具体问题需要根据实际场景分析

---

## 42. 文件无法访问

**问题分类**: CDN｜访问下载

### 问题描述

[URL已脱敏]

### 客服解答

**客户**：[URL已脱敏]
**客服**：您好，1.该文件是否有进行过删除操作？您检查一下上传时候是否指定了 deleteAfterDays，或者是存储空间设置了生命周期( [URL已脱敏] )2.是否有对文件做过 move 操作 ( [URL已脱敏] )3.是否有大致的文件上传时间和删除时间

### 根本原因分析

对象存储配置或使用问题

---

## 43. 域名证书不能用

**问题分类**: 对象存储｜其他类咨询

### 问题描述

images.yinwy.com，让我补全证书，提交让我公司信息，公司信息校验又不能提交

### 客服解答

**客户**：images.yinwy.com，让我补全证书，提交让我公司信息，公司信息校验又不能提交
**客服**：您好是要上传自有证书吗
**客服**：把报错截图提供一下
**客户**：我在阿里云申请了一个免费证书，上传了，先用到，不然网上图片都看不了
**客服**：您好1、建议您在证书厂商下载证书时，选择 Nginx 服务器类型的证书文件2、进入七牛云管理控制台：[URL已脱敏] 【上传自有证书】3、使用编辑器打开后续文件，并复制 .crt 或者 .pem 后缀的文件内容到证书内容 （公钥），复制 .key 后缀结尾的内容到 证书私钥 。[图片]如果需要把域名升级为 HTTPS 或者修改证书 的话，需要按照以下步骤绑定证书即可：[URL已脱敏]
**客户**：你们这个自动续期，没有用吗
**客户**：你们的免费https证书，不能自动续费吗
**客服**：免费证书不是自动续费的 到期前可以再次申请
**客服**：您好，手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免[URL已脱敏]

### 根本原因分析

SSL证书配置或过期问题

---

## 44. 怎么备案

**问题分类**: CDN｜其他类咨询

### 问题描述

zhishifufei888.com  再咱么你平台也可以备案吗？怎么备案 请指导   谢谢

### 客服解答

**客户**：zhishifufei888.com  再咱么你平台也可以备案吗？怎么备案 请指导   谢谢
**客服**：您好，请到您的主机托管商办理备案，流程参考 工信部公共查询系统：[URL已脱敏]

### 根本原因分析

具体问题需要根据实际场景分析

---

## 45. 更新了证书显示403这个是什么原因呢

**问题分类**: 对象存储｜其他类咨询

### 问题描述

更新了证书显示403这个是什么原因呢[URL已脱敏]

### 客服解答

**客户**：更新了证书显示403这个是什么原因呢[URL已脱敏]
**客服**：您好您配置的有referer白名单 把这个关闭一下
**客户**：这个是关着的哦没有开启
**客户**：找到了我试试
**客户**：可以了谢谢
**客服**：好的

### 根本原因分析

SSL证书配置或过期问题

---

## 46. 当前地区空间超过限制

**问题分类**: 对象存储｜其他类咨询

### 问题描述

当前地区空间超过限制

### 客服解答

**客户**：[图片]当前地区空间超过限制
**客服**：您好目前您这边需要的空间数量是多少 这边需要反馈处理

### 根本原因分析

对象存储配置或使用问题

---

## 47. 上传同名文件失败

**问题分类**: 对象存储｜其他类咨询

### 问题描述

上传同名文件会上传失败，同名不可以直接替换掉吗

### 客服解答

**客户**：上传同名文件会上传失败，同名不可以直接替换掉吗
**客服**：您好，您可以在上传策略中设置覆盖上传[URL已脱敏] 可以设置这里的scope字段 :，表示只允许用户上传指定key的文件。在这种模型下文件默认允许“修改”，已存在同名资源则会本次覆盖。如果希望只能上传指定key的文件，并且不允许修改，那么可以将下面的 insertOnly 属性值设为 1。这里通常报错最多的就是 614 错误，目标资源已存在。

### 根本原因分析

网络波动导致上传不稳定，建议使用断点续传功能

---

## 48. 一直卡住配置中

**问题分类**: CDN｜配置问题

### 问题描述

一晚上了 还在配置中

### 客服解答

**客户**：一晚上了 还在配置中
**客服**：您好这边帮您手动介入处理下 请稍等
**客服**：您的证书已经过期了 需要重新申请手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免[URL已脱敏]
**客户**：我是说一直在处理中
**客户**：都一晚上过去了[图片]
**客服**：状态已经处理好了 您刷新页面再看下

### 根本原因分析

SSL证书配置或过期问题

---

## 49. 新区域西北-陕西的源站上传地址是什么，谢谢

**问题分类**: 对象存储｜上传下载

### 问题描述

新区域西北-陕西的源站上传地址是什么，谢谢

### 客服解答

**客户**：新区域西北-陕西的源站上传地址是什么，谢谢
**客服**：您好这个区域目前需要申请审批后同步地址
**客户**：已解决，谢谢

### 根本原因分析

具体问题需要根据实际场景分析

---

## 50. 申请账户注销

**问题分类**: 账户与财务｜账户问题

### 问题描述

已不再使用七牛云，申请账号注销

### 客服解答

**客户**：已不再使用七牛云，申请账号注销
**客服**：您好，目前注销可以在控制台操作[URL已脱敏]

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 51. 通配域名证书无法部署在三级域名

**问题分类**: CDN｜证书问题

### 问题描述

通配域名证书不是适用所有子域名吗？gtimg.qq.com.v2club.top*.qq.v2club.top以上域名的全站加速都无法使用通配域名证书

### 客服解答

**客户**：通配域名证书不是适用所有子域名吗？gtimg.qq.com.v2club.top*.qq.v2club.top以上域名的全站加速都无法使用通配域名证书
**客服**：您好域名证书有严格的等级划分，要严格适配的，不能多占位*.v2club.top可以部署给 abc.v2club.top 和 123.v2club.top不适用于gtimg.qq.com.v2club.top ，您可以给gtimg.qq.com.v2club.top申请一个免费证书部署

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 52. 说我这边ssl证书到期！但是我已经更新了还是不行呢

**问题分类**: 对象存储｜其他类咨询

### 问题描述

说我这边ssl证书到期！但是我已经更新了还是不行呢我的全程截图了帮我尽快核实问题

### 客服解答

**客户**：说我这边ssl证书到期！但是我已经更新了还是不行呢我的全程截图了帮我尽快核实问题[图片][图片][图片][图片][图片]
**客户**：上次也是发这个问题
**客服**：您好weiqin.yike-tech.cn 这个域名的证书没有做文件验证 新证书还没有签发[URL已脱敏]
**客户**：需要怎么做呢
**客服**：需要您点击详情，然后根据提示进行文件 验证，系统会自动轮询，轮询通过才会颁发证书参考文档：[URL已脱敏]
**客户**：更新了呢
**客户**：你看看已经颁发了[图片]
**客服**：您截图的不是我们平台的证书
**客服**：如果要在我们这边使用 需要上传过来1、建议您在证书厂商下载证书时，选择 Nginx 服务器类型的证书文件2、进入七牛云管理控制台：[URL已脱敏] 【上传自有证书】3、使用编辑器打开后续文件，并复制 .crt 或者 .pem 后缀的文件内容到证书内容 （公钥），复制 .key 后缀结尾的内容到 证书私钥 。[图片]如果需要把域名升级为 HTTPS 或者修改证书 的话，需要按照以下步骤绑定证书即可：[URL已脱敏]
**客户**：我已经添加了，您帮我重新核查下，谢谢
**客服**：好的 请稍等
**客服**：这个域名下发配置有异常 可以删除后重新创建一下吗
**客服**：已经配置好了

### 根本原因分析

SSL证书配置或过期问题

---

## 53. 登入账号的消息通时间点与本地时间有差异

**问题分类**: 智能日志管理平台｜其他类咨询

### 问题描述

如图，消息通知的时间比北京时间快

### 客服解答

**客户**：如图，消息通知的时间比北京时间快[图片]
**客服**：您好这个不是昨天27号操作的绑定邮箱吗

### 根本原因分析

具体问题需要根据实际场景分析

---

## 54. 下载提示404错误

**问题分类**: 对象存储｜上传下载

### 问题描述

code...fms.chuanqiukeji.com/wpsOMS/SM_104420240404_222550_608IMG_1712240749_zgi.png?e=1727494155&token=[密钥已脱敏]:z3us--[密钥已脱敏]提示404错误

### 客服解答

**客户**：code...fms.chuanqiukeji.com/wpsOMS/SM_104420240404_222550_608IMG_1712240749_zgi.png?e=1727494155&token=[密钥已脱敏]:z3us--[密钥已脱敏]提示404错误
**客户**：说错了，是403错误
**客服**：您好您的域名开启了回源鉴权 把这个关闭后再访问看下
**客户**：{"error":"download token auth failed"}
**客户**：关了后提示这个 ，是我域名没有解析成功吗？昨天换了个域名。
**客服**：私有空间需要授权签算访问私有资源下载是通过HTTP GET的方式访问特定的 URL。私有资源URL与公开资源URL相比只是增加了两个参数e和token，分别表示过期时间和下载凭证。一个完整的私有资源 URL 如下所示：[URL已脱敏]
参数e表示 URL 的过期时间，采用Unix时间戳，单位为秒。超时的访问将返回 401 错误。参数token表示下载凭证。下载凭证是对资源访问的授权，不带下载凭证或下载凭证不合法都会导致 401 错误，表示验证失败。注意：如果请求方的时钟未校准，可能会造成有效期验证不正常，例如直接认为已过期。因此需要进行时钟校准。由于开发者无法保证客户端的时间都校准，所以应该在业务服务器上创建时间戳，并周期性校准业务服务器时钟。文档链接：[URL已脱敏]
**客户**：现在报403
**客户**：fms.chuanqiukeji.com/wpsOMS/SM_104420240928_111807_562IMG_1727493486_2lm.png?e=1727502004&token=[密钥已脱敏]:hP8Oev3XTp0xY8nOzS9-7TIfT6w=
**客服**：fms.chuanqiukeji.com 把回源鉴权策略关闭掉
再访问[URL已脱敏]
**客户**：私有空间需要授权签算访问私有资源下载是通过HTTP GET的方式访问特定的 URL。私有资源URL与公开资源URL相比只是增加了两个参数e和token，分别表示过期时间和下载凭证。一个完整的私有资源 URL 如下所示：[URL已脱敏]
参数e表示 URL 的过期时间，采用Unix时间戳，单位为秒。超时的访问将返回 401 错误。参数token表示下载凭证。下载凭证是对资源访问的授权，不带下载凭证或下载凭证不合法都会导致 401 错误，表示验证失败。注意：如果请求方的时钟未校准，可能会造成有效期验证不正常，例如直接认为已过期。因此需要进行时钟校准。由于开发者无法保证客户端的时间都校准，所以应该在业务服务器上创建时间戳，并周期性校准业务服务器时钟。文档链接：[URL已脱敏]
**客户**：监测到域名源站在七牛私有 BUCKET，建议打开回源鉴权功能。
**客户**：public static string [密钥已脱敏](string cloudfn)        {            try            {                Mac mac = new Mac([密钥已脱敏], [密钥已脱敏]);                               int expireInSeconds = 3600;                string accUrl = DownloadManager.CreatePrivateUrl(mac, 'www', cloudfn, expireInSeconds);                return accUrl;            }            catch (Exception err)            {                Msg.Error(err.Message, "下载异常QN");            }            return "";        }
**客服**：前边签算后的链接访问403 是您那边的回源鉴权一直无法通过

### 根本原因分析

对象存储配置或使用问题

---

## 55. 特定格式的文件只允许下载，不允许直接预览

**问题分类**: 对象存储｜其他类咨询

### 问题描述

例如我上传了一个html文件，在浏览器访问相关地址时，我不希望直接访问内容，而是提示我下载该html

### 客服解答

**客户**：例如我上传了一个html文件，在浏览器访问相关地址时，我不希望直接访问内容，而是提示我下载该html
**客服**：您好文件在浏览器端是默认直接打开的 这个是浏览器的处理策略 这边无法干预

### 根本原因分析

具体问题需要根据实际场景分析

---

## 56. 这里的私有云，公有云，指是什么？

**问题分类**: 对象存储｜上传下载

### 问题描述

这里的私有云，公有云，指是什么？私有是图片改成私有空间，就是私有云了吗？

### 客服解答

**客户**：这里的私有云，公有云，指是什么？私有是图片改成私有空间，就是私有云了吗？[图片][图片]
**客服**：您好查询您不是私有云客户 选择公有云即可

### 根本原因分析

对象存储配置或使用问题

---

## 57. 忘记密码了需要修改密码

**问题分类**: 账户与财务｜账户问题

### 问题描述

忘记密码了需要修改密码需要修改密码，但是忘记了原来的密码

### 客服解答

**客户**：忘记密码了需要修改密码需要修改密码，但是忘记了原来的密码
**客服**：您好可以到[URL已脱敏] 这个页面找回重置

### 根本原因分析

具体问题需要根据实际场景分析

---

## 58. 使用，Kodo Browse下载那个方法更便宜，有没有其它免费下载方案？

**问题分类**: CDN｜访问下载

### 问题描述

使用Kodo Browse的两种下载方法，外网流量出流量便宜一点，还是cdn流量下载？（如果没有缓存，是不是用回源流量下载的）下载那个方法更便宜，有没有其它免费下载方案？

### 客服解答

**客户**：使用Kodo Browse的两种下载方法，外网流量出流量便宜一点，还是cdn流量下载？（如果没有缓存，是不是用回源流量下载的）下载那个方法更便宜，有没有其它免费下载方案？[图片]
**客服**：您好cdn域名下载[图片]源站域名下载产生外网流出流量 [URL已脱敏] 对应的域名
**客户**：使用Kodo Browse  cdn域名下载   产生的是CDN下行流量，还是回源流量，按图片描述应该是回源流量 ，价格差近一倍呢静态 HTTPS 下载流量/动态加速 HTTPS 流量0.28 元/GB        CDN 回源流量0.15 元/GB[图片]
**客服**：cdn访问会从源站拉取资源 这个过程产生的就是cdn回源流量存储CDN回源流出流量的说明您可以参考下面的文档。[URL已脱敏]
**客户**：你说那个是正常访问 ，，，我现在咨询是使用Kodo Browse下载，  难道是这个文档描述不正确？[图片]
**客服**：cdn域名访问和下载是一个意思 您用Kodo Browse下载 只需要确认好 用cdn域名还是源站域名即可

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 59. 价格问题

**问题分类**: 对象存储｜其他类咨询

### 问题描述

抵扣系数 （数值）越大是越大，代表越贵吗？

### 客服解答

**客户**：抵扣系数 （数值）越大是越大，代表越贵吗？
**客服**：您好是咨询存储的计费吗
**客户**：OSS储存，外面流出流量，cdn流量，回源流量，应该都是一样的吧，抵扣系数 （数值）越大是越大，代表越贵吗？[图片][图片]
**客服**：抵扣系数越大 需要抵扣资源包的量越多 这个是资源包的抵扣逻辑[图片]
**客户**：那就是相当于，数值越大越贵的意思吧，越小消耗的越便宜
**客服**：可以这么理解

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 60. 后端服务访问CDN资源有时识别到另外一个无效证书导致报错

**问题分类**: CDN｜证书问题

### 问题描述

后端服务访问CDN资源有时识别到另外一个无效证书导致报错，如下图在myssl查询[URL已脱敏]

### 客服解答

**客户**：后端服务访问CDN资源有时识别到另外一个无效证书导致报错，如下图[图片]在myssl查询[URL已脱敏]
**客服**：您好访问查看部署的证书有效期与您截图的不符 多余的证书可以删掉[图片]
**客户**：a.bdydns.com 这个域名证书不是我配的 我只配了第一个*.hisugar.com的这个 对应CDN域名test-cdn-cm.hisugar.com
**客服**：如果证书选择的不对 到控制台更换一下
**客户**：我发现我所有配置的CDN域名都有这个情况
**客户**：名人配了 *.hisugar.com 这个域名证书 没配任何其它域名证书 我的证书管理中只有这一个域名证书 也选不了其它的 能不能针对我现在的问题场景沟通！！！
**客户**：我只配了 *.hisugar.com 这个域名证书 没配任何其它域名证书 我的证书管理中只有这一个域名证书 也选不了其它的 能不能针对我现在的问题场景沟通！！！
**客服**：*.hisugar.com  这个是您上传的自有证书  不是在我们这边申请的证书 具体您可以反馈您的证书服务厂商来确认证书有没有异常[图片]
**客户**：你没理解我的问题 这个证书没问题 有问题的是你们cdb服务不知道为什么加了一个不是我的证书 请理解我的问题再说 别老是往外推 有需要可以电话沟通 先充分理解问题好不好
**客服**：下载链接以及节点信息 麻烦粘贴一下
**客户**：[URL已脱敏]
**客户**：请问节点信息是什么? 我不知道怎么提供
**客服**：[URL已脱敏] 
——这个签算的链接不对
私有空间的处理上对 [URL已脱敏] 签算
生成的链接是 [URL已脱敏]
**客服**：节点获取方式：使用 chrome 浏览器，按照下述文档获取下 remote adress(对端节点ip)，request header(客户端请求头) 以及 response header(服务端响应头)信息，方便我们查询分析问题。[URL已脱敏]
**客户**：链接是过期了
**客户**：我现在在外面了 下午才回 这些你开chrome也可以获取的 如果必须我来提供 那晚点再提供
**客户**：请问你用myssl.com查询和分析过CDN域名对应的证书了吗?
**客服**：cdn上部署的证书是没有问题  您的文件访问签算方式不对[图片]curl -va -o /dev/null   "[URL已脱敏]
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 2408:8719:64:9a::275b:b629:443...
* Connected to test-cdn-cm.hisugar.com (2408:8719:64:9a::275b:b629) port 443 (#0)
* ALPN: offers h2
* ALPN: offers http/1.1
*  CAfile: /etc/ssl/cert.pem
*  CApath: none
* (304) (OUT), TLS handsh[密钥已脱敏]e, Client hello (1):
} [328 bytes data]
* (304) (IN), TLS handsh[密钥已脱敏]e, Server hello (2):
{ [122 bytes data]
* (304) (IN), TLS handsh[密钥已脱敏]e, Unknown (8):
{ [19 bytes data]
* (304) (IN), TLS handsh[密钥已脱敏]e, Certificate (11):
{ [2754 bytes data]
* (304) (IN), TLS handsh[密钥已脱敏]e, CERT verify (15):
{ [264 bytes data]
* (304) (IN), TLS handsh[密钥已脱敏]e, Finished (20):
{ [52 bytes data]
* (304) (OUT), TLS handsh[密钥已脱敏]e, Finished (20):
} [52 bytes data]
* SSL connection using TLSv1.3 / AEAD-AES256-GCM-SHA384
* ALPN: server accepted h2
* Server certificate:
*  subject: C=CN; ST=\U5E7F\U897F; L=\U5357\U5B81; O=\U5E7F\U897F\U6CDB\U7CD6\U79D1\U6280\U6709\U9650\U516C\U53F8; CN=*.hisugar.com
*  start date: Jan 24 03:22:05 2024 GMT
*  expire date: Feb 24 03:22:04 2025 GMT
*  subjectAltName: host "test-cdn-cm.hisugar.com" matched cert's "*.hisugar.com"
*  issuer: C=BE; O=GlobalSign nv-sa; CN=GlobalSign RSA OV SSL CA 2018
*  SSL certificate verify ok.
* Using HTTP2, server supports multiplexing
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* h2h3 [:method: GET]
* h2h3 [:path: /]
* h2h3 [:scheme: https]
* h2h3 [:authority: test-cdn-cm.hisugar.com]
* h2h3 [user-agent: curl/7.84.0]
* h2h3 [accept: */*]
* Using Stream ID: 1 (easy handle 0x7f8db4011a00)
> GET / HTTP/2
> Host: test-cdn-cm.hisugar.com
> user-agent: curl/7.84.0
> accept: */*
>
**客户**：不用管签算这类其它问题 看我发的第一张截图 dns的报错 我现在要解决的是这个问题 出现概率10%不到 偶发
**客户**：90%多的请求都是正常处理的
**客服**：把复现异常的cdn节点粘贴过来 这边代理测试下
**客户**：[图片]这个
**客户**：test-cdn-cm.hisugar.com
**客服**：cdn节点信息获取方式有两种1、ping域名得到2、使用 chrome 浏览器，按照下述文档获取下 remote adress(对端节点ip)，request header(客户端请求头) 以及 response header(服务端响应头)信息，方便我们查询分析问题。[URL已脱敏]

### 根本原因分析

企业认证需要提供社会信用代码或营业执照号

---

## 61. 如下图

**问题分类**: 对象存储｜其他类咨询

### 问题描述

【七牛云服务】尊敬的七牛云用户，您好！您的账号 [REDACTED_EMAIL] 下有存储源站域名已冻结，域名冻结后无法正常访问资源。详情参见邮件内容。您可登录「Portal/消息中心」关闭短信通知。

### 客服解答

**客户**：【七牛云服务】尊敬的七牛云用户，您好！您的账号 [REDACTED_EMAIL] 下有存储源站域名已冻结，域名冻结后无法正常访问资源。详情参见邮件内容。您可登录「Portal/消息中心」关闭短信通知。
**客服**：您好 errandz.xingzl.top 这个域名的ICP 备案过期了 请及时备案
**客户**：我对这个不是很懂，可以再问下去哪备案吗！因为程序员这边较忙没帮我及时这边处理
**客服**：您好，请到您的主机托管商办理备案，流程参考 工信部公共查询系统：[URL已脱敏]

### 根本原因分析

对象存储配置或使用问题

---

## 62. 使用kodoimport工具迁移失败

**问题分类**: 对象存储｜工具使用

### 问题描述

使用kodoimport时候，提示错误[root@[密钥已脱敏] kodoimport]# ./kodoimport2024-09-28T12:14:57.742049593+08:00     warn    job/job_cache.go:42     recover round error:job recover round, get roundCache error:resource temporarily unavailable      {"tag": "job_flows", "job_id": "[密钥已脱敏]"}2024-09-28T12:14:57.742471199+08:00     error   local/scheduler.go:221  job load:[密钥已脱敏] error:job already exist:[密钥已脱敏]        {"tag": "scheduler_flows", "name": null, "pid": 3727211, "web_address": "[IP已脱敏]:7900", "scheduler_address": "[IP已脱敏]:8001"}2024-09-28T12:14:57.742471199+08:00     error   local/scheduler.go:221  job load:[密钥已脱敏] error:job already exist:[密钥已脱敏]        {"tag": "scheduler_flows", "name": null, "pid": 3727211, "web_address": "[IP已脱敏]:7900", "scheduler_address": "[IP已脱敏]:8001"}2024-09-28T12:14:57.74249423+08:00      fatal   kodoimport/main.go:215  create job error:job already exist:[密钥已脱敏]       {"tag": "main_flows"}2024-09-28T12:14:57.74249423+08:00      fatal   kodoimport/main.go:215  create job error:job already exist:[密钥已脱敏]       {"tag": "main_flows"}

### 客服解答

**客户**：使用kodoimport时候，提示错误[root@[密钥已脱敏] kodoimport]# ./kodoimport2024-09-28T12:14:57.742049593+08:00     warn    job/job_cache.go:42     recover round error:job recover round, get roundCache error:resource temporarily unavailable      {"tag": "job_flows", "job_id": "[密钥已脱敏]"}2024-09-28T12:14:57.742471199+08:00     error   local/scheduler.go:221  job load:[密钥已脱敏] error:job already exist:[密钥已脱敏]        {"tag": "scheduler_flows", "name": null, "pid": 3727211, "web_address": "[IP已脱敏]:7900", "scheduler_address": "[IP已脱敏]:8001"}2024-09-28T12:14:57.742471199+08:00     error   local/scheduler.go:221  job load:[密钥已脱敏] error:job already exist:[密钥已脱敏]        {"tag": "scheduler_flows", "name": null, "pid": 3727211, "web_address": "[IP已脱敏]:7900", "scheduler_address": "[IP已脱敏]:8001"}2024-09-28T12:14:57.74249423+08:00      fatal   kodoimport/main.go:215  create job error:job already exist:[密钥已脱敏]       {"tag": "main_flows"}2024-09-28T12:14:57.74249423+08:00      fatal   kodoimport/main.go:215  create job error:job already exist:[密钥已脱敏]       {"tag": "main_flows"}[图片]
**客户**：能否使用什么命令清除这个job
**客服**：您好预期您这边的数据是从哪里迁移到哪里 麻烦说明下
**客户**：从一台服务器迁移到七牛配置文件如下{  "debug_level": 0, # 日志级别  "bind_host": "[IP已脱敏]:8001", #【调度器】运行地址  "use_https": false, # 请求是否使用 https，如果配置的 host 中包含了 http:// 或 [URL已脱敏] host 中的  #########不同任务需要修改内容#########  "dst_bucket": "zhongkangyang", # 【调度器】目标存储桶  "dst_access_key": "[REDACTED_ACCESS_KEY]", # 【调度器】目标存储桶用户[密钥已脱敏]  "dst_secret_key": "[REDACTED_SECRET_KEY]", # 【调度器】目标存储桶用户[密钥已脱敏]  "dst_prefix": "common/", #【调度器】目标前缀，默认为空，直接放在目标bucket下。一个本地文件路径为srcPrefix+[文件名]的文件，迁移到qiniu的object名称为dstPrefix+[文件名]  "dst_file_type": 0, #目标存储类型，取值: 0 表示标准存储；1 表示低频存储；2 表示归档存储, 默认标准存储  "insert_only": true, # 【调度器】如果目标文件存在，是否覆盖。 true: 不覆盖；false: 覆盖  "src_type": "local", # 【调度器】支持不同同步源类型,注意大小写，当前仅支持http,qiniu,oss,S3,local  "work_dirs": ["./works1","./works2"], # 【调度器】工作目录，目录下将包含任务持久化信息,任务运行前需要创建好；任务开始后结束前不要手动修改  "src_objects_count": 27, #【调度器】目录下文件个数，如果与实际有偏差，进度比例信息会不准确，不影响迁移功能,不可为0  "src_prefix":"/www/wwwroot/tj.xqq.zhongkangyang.cn/public/uploads/", #【调度器】如果srcType设置为local，则填写本地目录，需要完整路径，以单个正斜线（/）结尾，不支持本地路径下的软连接  "ignore_dir": false, # 保存文件在七牛空间时，使用的文件名是否忽略本地路径，默认为false, 默认上传到七牛空间的文件名都会带上从 src_prefix 开始的文件的相对路径最为前缀  "key_file": "",#在有记录本地失败任务需要重跑时，填写需要重跑任务列表文件即可  "is_incremental": true, #【调度器】是否打开增量迁移模式，布尔类型  "incremental_mode_interval": 3600, #【调度器】每间隔指定时间重新扫描一次增量数据,并迁移增量数据，单位s,默认7200s,配置不低于900s  #########不同任务需要修改内容done#########  "scheduler_addr": "[URL已脱敏]  # 请求调度器地址  "web_bind_host": "[IP已脱敏]:7900", # 绑定的服务地址，此服务可获取一些状态信息等，eg: 当前仅支持获取 worker 状态: curl [URL已脱敏]  "input_chan_size": 1000, # 【调度器】内存中缓存任务个数,默认1000  "dump_progress_intervals": 6, # 【调度器】持久化总体进度时间间隔，单位为s,默认60s  "worker_report_timeout": 1800, # 超过此时间任务状态未更新，调度器会重新分配任务，单位是s,默认1h  "worker_goroutine_num": 2 , # 执行者并发执行迁移任务个，默认20  "worker_rate_limit_mb": 1024, # 执行者速度限制，防止拖垮用户源站，单位是MB/s，默认1GB/s  "max_fail_count": 10000 , # 执行者任务最大连续失败次数，超过此个数程序将退出, 默认 10000  "upload_part_size_mb": 8,  # 执行者上传分片大小，，单位 MB, 默认 8 MB  "worker_resumable_up_size": 1073741824, # 执行者使用分片上传的阈值， 单位 B, 默认 1GB  "local_file_dir": "/tmp", # 执行者大文件本地缓存位置,默认是系统TempDir  "use_windows_separator": false  #windows上传时,保存文件名是否使用windows文件路径分隔符(\)，默认为false，使用unix文件路径分隔符(/),否则使用windows文件路径分隔符(\)  #"rs_host": "[URL已脱敏] #【调度器】 查询 目标文件是否已经存在的rs 地址，默认是公有云 rs 域名  #"uc_host": "[URL已脱敏] # 【调度器】查询dst bucket信息地址,默认是公有云地址中心机房bucket地址，当您使用非公有云时可以手动配置  #"region_up_host_map": {  #  "z0":"[URL已脱敏]  #  "z1":"[URL已脱敏]  #  "z2":"[URL已脱敏]  #  "na0":"[URL已脱敏]  #} # 不同区域上传地址，默认七牛云公有云外网地址，当您使用非公有云时可以手动配置}
**客服**：是我们的云主机吗
**客户**：不是，是阿里云
**客服**：您好，参考下方这个配置以及步骤重试下文档参考：[URL已脱敏] conf 文件夹中的 qiniu 移到工具的根目录，然后创建 works1 和 works2 文件夹[图片]2、修改 qiniu/single-mode/kodoimport.conf 配置文件。主要是修改 ，其他参数您可以自行修改迁移后的bucket名称（dst_bucket）迁移后的账户 [密钥已脱敏]、[密钥已脱敏]（dst_access_key、dst_secret_key）迁移后 bucket 绑定的加速域名（src_endpoint）源bucket待同步object的前缀（src_prefix），迁移全部文件的话留空即可迁移前的账户 [密钥已脱敏]、[密钥已脱敏]（src_access_key、src_secret_key）迁移前的 bucket 名称（src_bucket）工作目录（work_dirs）uc_host：[URL已脱敏] 到 kodoimport 目录，然后执行 ./kodoimport -f qiniu/single-mode/kodoimport.conf，就可以看到命令行在执行了，然后去对应空间查看文件是否迁移成功，如果有问题，您可以提供下您运行程序的报错截图[图片]
**客户**：执行结果如下./kodoimport -f ./kodoimport.conf Flag --old-config has been deprecated, Deprecated: use kodoimport-cli create job2024-09-28T13:47:38.545581846+08:00     warn    job/job_cache.go:42     recover round error:job recover round, get roundCache error:resource temporarily unavailable    {"tag": "job_flows", "job_id": "[密钥已脱敏]"}2024-09-28T13:47:38.545627883+08:00     error   local/scheduler.go:221  job load:[密钥已脱敏] error:job already exist:[密钥已脱敏]      {"tag": "scheduler_flows", "name": null, "pid": 3729428, "web_address": "[IP已脱敏]:7900", "scheduler_address": "[IP已脱敏]:8001"}2024-09-28T13:47:38.545627883+08:00     error   local/scheduler.go:221  job load:[密钥已脱敏] error:job already exist:[密钥已脱敏]      {"tag": "scheduler_flows", "name": null, "pid": 3729428, "web_address": "[IP已脱敏]:7900", "scheduler_address": "[IP已脱敏]:8001"}2024-09-28T13:47:38.545645989+08:00     fatal   kodoimport/main.go:215  create job error:job already exist:[密钥已脱敏]     {"tag": "main_flows"}2024-09-28T13:47:38.545645989+08:00     fatal   kodoimport/main.go:215  create job error:job already exist:[密钥已脱敏]     {"tag": "main_flows"}
**客服**：看报错是已经存在了
**客户**：对，是，问题是他没上传呢
**客户**：这个任务如何能删掉呢
**客服**：这边反馈下 请稍等
**客户**：解决了 kodoimport-cli job ls

### 根本原因分析

网络波动导致上传不稳定，建议使用断点续传功能

---

## 63. 账号注销

**问题分类**: 账户与财务｜账户问题

### 问题描述

不需要了

### 客服解答

**客户**：不需要了
**客服**：您好，目前注销可以在控制台操作[URL已脱敏]

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 64. 域名证书更新慢

**问题分类**: 对象存储｜其他类咨询

### 问题描述

我昨天设置更新一个域名的免费证书，提示15分钟，但是已经1天了，还是没完成

### 客服解答

**客户**：我昨天设置更新一个域名的免费证书，提示15分钟，但是已经1天了，还是没完成[图片]
**客服**：您好您申请的证书没有验证通过 等证书签发后才能部署到cdn域名
**客服**：可以申请一个新的证书 选择dns验证
**客户**：我上传了我们自己生成的证书，但是状态一直没变
**客服**：上传后要手动部署到cdn域名
**客户**：一直显示免费证书申请中，改不了
**客户**：就是在cdn域名里配置的
**客服**：您好，稍等这边看下
**客服**：您好，我这边给您把订单关闭下，您可以重新再申请一下
**客户**：什么时候能关闭，还一直是申请免费证书的状态
**客服**：您好，已经关闭
**客户**：没有啊，一直显示的是修改 HTTPS 配置处理中，免费证书申请耗时相对较长，平均 15 分钟完成，期间域名访问不受影响，部分配置不可修改，若长时间未配置完成，请提交工单反馈 常见证书问题
**客户**：small.ygcha.com.cn
**客服**：您好，您这边再重新申请一下免费证书把
**客户**：免费证书申请一直卡在那里啊，一直动不了，我想改成用本地的也关闭不了修改 HTTPS 配置处理中，免费证书申请耗时相对较长，平均 15 分钟完成，期间域名访问不受影响，部分配置不可修改，若长时间未配置完成，请提交工单反馈 常见证书问题
**客服**：您好，您看下是否可以到SSL证书中重新购买申请一个免费证书
**客户**：买了也没用啊，域名显示处理中，不能部署
**客户**：什么操作也做不了
**客服**：您好，您现在再看下可以绑定新证书吗
**客户**：修改 HTTPS 配置处理中，通常情况下 8-15 分钟完成，期间域名访问不受影响，部分配置不可修改，若较长时间未配置完成，请提交工单反馈 常见证书问题
**客户**：可以了
**客服**：好的

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 65. CDN回源流量包哪里可以买

**问题分类**: CDN｜流量计费问题

### 问题描述

我的回源资源包已用完，请问新资源包的购买链接是什么？

### 客服解答

**客户**：我的回源资源包已用完，请问新资源包的购买链接是什么？[图片]
**客服**：您好可以到 [URL已脱敏] 购买

### 根本原因分析

具体问题需要根据实际场景分析

---

## 66. 关闭CDN加速会影响到对象储存中的图片打开吗

**问题分类**: CDN｜其他类咨询

### 问题描述

问题1、就是说关闭CDN加速后，对象储存中的图片还能不能打开。问题2、其次就是如何在使用对象储存中，不超出流量范围，比如流量一个月10G，就是在10G内。

### 客服解答

**客户**：问题1、就是说关闭CDN加速后，对象储存中的图片还能不能打开。问题2、其次就是如何在使用对象储存中，不超出流量范围，比如流量一个月10G，就是在10G内。
**客服**：您好1、如果存储使用的是cdn域名 会有影响2、cdn http协议免费额度10G 超出部分按量扣费 具体使用由您那边来控制
**客户**：1、怎么查看是不是CDN域名？2、免费额度10G这个是在哪里控制
**客服**：1、在 [URL已脱敏] 创建的是cdn域名2、免费额度是产生计费时的抵扣制度 您那边不需要控制  具体访问使用是您那边来处理
**客户**：我查了下大概流量使用数据，9月26日一天就用了92.2G了，请提供下这个92.2G流量用到那里去了。
**客户**：还有一个，关于这个CDN加速，有没有教程说明这个流量如何使用会更节省
**客服**：您好，这个一般情况下，减少CDN流量1：控制客户端访问，减少客户端请求2：控制文件大小，减小文件体积，降低流量，比如图片压缩，文本压缩等
**客户**：麻烦回答下上面这后续的2个问题
**客户**：那你能提供下，我这9月26号1天永了92.2G的CDN流量，用到那里去了
**客服**：您好，这个您可以直接查看9-26的CDN日志接口分析具体的访问量和访问行为，建议在控制台 [URL已脱敏] 下载CDN日志后进行分析CDN日志的下载方式，以及日志中字段的含义参考文档：[URL已脱敏] referer 和 ip 黑白名单等方式来进行访问限制。
**客户**：谢谢

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 67. 账号注销

**问题分类**: 账户与财务｜账户问题

### 问题描述

已有账号

### 客服解答

**客户**：已有账号
**客服**：您好，目前注销可以在控制台操作[URL已脱敏]

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 68. 证书到期替换

**问题分类**: CDN｜证书问题

### 问题描述

如何在ssl证书到期前替换证书，申请了一个免费证书，在到期前无法部署，是要等到到期后才好部署吗

### 客服解答

**客户**：如何在ssl证书到期前替换证书，申请了一个免费证书，在到期前无法部署，是要等到到期后才好部署吗
**客服**：您好到期前的证书 如果已经申请了新的证书 可以到控制台直接更换新的证书处理[图片]

### 根本原因分析

SSL证书配置或过期问题

---

## 69. 主机退订

**问题分类**: 云主机｜主机

### 问题描述

你好，该主机，请给退一下。

### 客服解答

**客户**：你好，该主机，请给退一下。
**客服**：您好，麻烦针对如下问题做一下填写确认：1.退款原因（以便我方改进产品不足）：2.申请退款的产品实例ID：3.已使用时长所对应的费用不退回，请您确认已知晓；4.代金券支付部分无法退回，请您确认已知晓：5.主机或实例是否已备份？若已备份，请回复“数据已备份”；若无需备份，请回复“数据无需备份” 。（退款后服务器实例立即被清除，数据不再保留，请提前备份数据）6.主机退款是将整个实例全部退订，不是单独退订主机升级的部分，请您确认知晓？注意：a.如需退款多个实例，需要注明多个实例ID，退款资源会按照填写上述表单为准b.云主机和弹性公网ip属于两个实例，需要分别填写两个实例IDc.云主机退款时间预期1-3个工作日
**客户**：1.退款原因（以便我方改进产品不足）：项目已经停止2.申请退款的产品实例ID：i-[密钥已脱敏].已使用时长所对应的费用不退回，请您确认已知晓；知晓4.代金券支付部分无法退回，请您确认已知晓：知晓5.主机或实例是否已备份？若已备份，请回复“数据已备份”；若无需备份，请回复“数据无需备份” 。（退款后服务器实例立即被清除，数据不再保留，请提前备份数据）数据无需备份6.主机退款是将整个实例全部退订，不是单独退订主机升级的部分，请您确认知晓？知晓
**客服**：云主机和弹性公网ip属于两个实例，如果弹性公网ip也要退订 麻烦同样粘贴一下实例ID
**客户**：IDeip-[密钥已脱敏]名称I-hPrXg_E-XxAIj IP47.242.123.91请一并退订
**客服**：好的 这边提交审批处理 一般需要1-2个工组日 请耐心等待
**客服**：好的 这边提交审批处理 一般需要1-2个工作日 请耐心等待
**客服**：[URL已脱敏]
**客服**：您好主机已经退款完成，您的弹性公网IP是按量付费的，这个可以在控制台停用删除

### 根本原因分析

具体问题需要根据实际场景分析

---

## 70. 一直显示配置中

**问题分类**: CDN｜配置问题

### 问题描述

选的海外全站加速，一直显示配置中，无法使用，cname没生效

### 客服解答

**客户**：选的海外全站加速，一直显示配置中，无法使用，cname没生效
**客服**：您好这边帮您手动介入处理下 请稍等
**客服**：已经配置好了
**客户**：好的，谢谢

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 71. 过了一天域名还是没有配置好

**问题分类**: 对象存储｜其他类咨询

### 问题描述

过了一天域名还是没有配置好

### 客服解答

**客户**：过了一天域名还是没有配置好[图片]
**客服**：您好这边帮您手动介入处理下 请稍等
**客服**：您好，已处理完成

### 根本原因分析

域名配置或解析问题

---

## 72. 域名创建达到上限 麻烦帮我升级一下

**问题分类**: 对象存储｜其他类咨询

### 问题描述

域名创建达到上限 麻烦帮我升级一下

### 客服解答

**客户**：域名创建达到上限 麻烦帮我升级一下[图片]
**客服**：您好这个不是创建达到上限 是您的域名所有权验证没有通过创建之后到您的域名服务商后台配置下验证解析 才可以创建成功
**客户**：提示的就是说上限了啊
**客户**：[400550] 域名创建数量已达每日上限，请创建工单获取帮助点击查看
**客服**：您这个是当前账号下提示的吗
**客户**：是的
**客户**：要怎么处理呢
**客服**：退出登陆重试下
**客户**：不行 还是一样的提示
**客户**：[图片]你看看
**客服**：预期您要创建的域名数量是多少 这边反馈下
**客户**：50个
**客服**：这个我们反馈评估下 目前相关人员不在线 预计明天工作时间处理完成
**客户**：好的
**客服**：好的
**客户**：有人上班吗? 还是跟昨天一样啊
**客户**：人呢
**客服**：您好，您的联系方式提供下，这边同步商务和您联系下
**客户**：[REDACTED_PHONE]
**客服**：您好，稍等下，这边同步下
**客服**：你好，已经完成添加，您测试看下

### 根本原因分析

域名配置或解析问题

---

## 73. 昨天买的5T就用完了啊

**问题分类**: CDN｜流量计费问题

### 问题描述

昨天买的5T就用完了啊   能帮我看下啵

### 客服解答

**客户**：昨天买的5T就用完了啊   能帮我看下啵
**客服**：您好查看购买的相关产品资源包抵扣情况，您可以从「实时消费明细中」中点击「资源包抵扣明细」下载当月所有有效资源包的数据（资源包名称，对应订单号，本月可用总量，本月已用量，本月剩余）[URL已脱敏]
**客户**：2天用几个T有点托不住啊 有什么好的办法吗
**客户**：流量的抵扣明细可以查看的吗 我想优化下
**客服**：您好，资源包当月生效的话，是购买后抵扣当月产生的全部流量的，前面流量产生的扣费会后续重新退回的
**客户**：用了全站加速 的缓存 是不是可以节省的流量 但是全站加速本身也会产生费用 到底哪个会更省钱
**客服**：您好，业务场景不同的，全站加速更适用于网站等的，全站加速会比CDN更贵一些
**客户**：但是用了全站加速 的缓存  流量的消耗会少点 感觉这个流量用的好快
**客服**：您好，CDN和全站加速的缓存机制是一样的，全站加速比CDN多的是智能调度动静态资源分离的，您可以修改一下CDN的缓存配置，进行根据您的业务具体化的资源缓存配置进行修改调整看下的您也可以在 控制台 - cdn - 统计分析 - 日志分析 中看到您的top访问情况，比如高频访问的URL和客户端IP。[URL已脱敏] - 访问控制 中，开启IP黑白名单，对这部分IP进行封禁。[图片]
**客户**：我这有的一张图片就几百G 都不知道怎么弄的 是不是没有开启缓存  截图有上传不了
**客服**：您好，和缓存没有关系，您需要查看一下是否有部分IP请求数/请求流量异常，不符合您的业务预期，您可以在域名管理 - 访问控制 中，开启IP黑白名单，对这部分IP进行封禁。有缓存的请求：会产生CDN流量没有缓存的请求：会产生CDN流量和CDN回源流量
**客户**：这种的是不是不正常啊 一万多次[图片]
**客服**：您好，您这边自行分辨一下是否有异常的，因为我们不清楚您的业务情况，无法分辨是否为用户请求的，您可以看下具体产生的流量是否异常的，是否为您的业务用户等的，不正常您这边进行拉黑就行了的
**客户**：一天800多G 会不会不正常啊
**客服**：您好，我这边不清楚您的业务情况的，这个需要您这边自行分析下的
**客服**：您可以和以前的量进行比对一下，再看下近期的业务情况是否正常

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 74. 七牛云KODO登不上

**问题分类**: 对象存储｜上传下载

### 问题描述

七牛云KODO登不上收到，请5分钟内回复，急。

### 客服解答

**客户**：七牛云KODO登不上收到，请5分钟内回复，急。[图片]
**客服**：您好 选择公有云[图片]
**客户**：蠢货，公有云也登不上，我是问这个[密钥已脱敏]，[密钥已脱敏]是多少？给我打个电话，或量录视频详细说。电话：[REDACTED_PHONE]
**客服**：您好，1： 你们要选公有云2：[密钥已脱敏] [密钥已脱敏] 是你们自己的个人账号秘钥 ，在秘钥管理里面，这个只有你们自己看的到     [URL已脱敏]
**客户**：铁蛋，我就是输的这个[密钥已脱敏]和[密钥已脱敏]登不上。铁蛋，打我电话说：[REDACTED_PHONE]
**客服**：您好，是[密钥已脱敏] 和[密钥已脱敏]停用了吗？

### 根本原因分析

具体问题需要根据实际场景分析

---

## 75. 免费（仅限静态 HTTP 下载流量）

**问题分类**: 对象存储｜上传下载

### 问题描述

第 0 GB 至 10 GB    免费（仅限静态 HTTP 下载流量）Kodo Browser这个10GB怎么用，

### 客服解答

**客户**：第 0 GB 至 10 GB    免费（仅限静态 HTTP 下载流量）Kodo Browser这个10GB怎么用，
**客服**：您好访问下载使用http协议的cdn域名 在10g以内是免费的 出账的时候系统会自动抵扣
**客户**：你没理解我的意思，我的意思 用这个工具，Kodo Browser下载  是不是没法用这个免费流量 了？
**客服**：您的理解有误 Kodo Browser下载会用到cdn域名 如果域名是http协议 就在免费额度内
**客户**：是我没有描述完整，那我这样问，我目前用的https协议, Kodo Browser没有修改协议的地方，   通信协议是域名管理时进添加的，现在问题是不能删除重新配置，然后在图片里面改成http,也没有用（如图3），，想在想零时用一下http，有没有什么可行的办法？[图片][图片][图片]
**客服**：这个没有临时可行的方式1、cdn域名降级为http协议2、创建http协议的域名下载

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 76. 免费 from 自动催单

**问题分类**: CDN｜证书问题

### 问题描述

长时间处于域名发布环节，状态不刷新

### 客服解答

**客户**：长时间处于域名发布环节，状态不刷新
**客服**：您好这边帮您手动介入处理下 请稍等
**客户**：已经可以了

### 根本原因分析

域名配置或解析问题

---

## 77. 短信验证

**问题分类**: 云短信｜签名模板审核

### 问题描述

短信验证类模板内容怎么写，中间验证码的数字填什么

### 客服解答

**客户**：短信验证类模板内容怎么写，中间验证码的数字填什么[图片][图片]
**客服**：您好可以参考 [URL已脱敏] 这个示例
**客户**：这是因为什么要怎么操作[图片]
**客服**：短信签名目前需要报备审批 预计3个工作日左右 等签名审核通过后 再创建模版

### 根本原因分析

具体问题需要根据实际场景分析

---

## 78. 修改配置一直在配置中

**问题分类**: CDN｜配置问题

### 问题描述

修改配置一直在配置中

### 客服解答

**客户**：修改配置一直在配置中
**客服**：您好这边帮您手动介入处理下 请稍等
**客服**：已经处理完成

### 根本原因分析

具体问题需要根据实际场景分析

---

## 79. 域名过期

**问题分类**: 对象存储｜上传下载

### 问题描述

域名过期是否可以申请临时域名

### 客服解答

**客户**：域名过期是否可以申请临时域名
**客服**：您好
测试域名仅在创建空间时生成，有效期30天，目前暂不支持其他方式获取，由于工信部要求，无法将测试域名长期提供使用，建议您及时进行备案和域名替换呢。

### 根本原因分析

对象存储配置或使用问题

---

## 80. 创建域名处理中，3-4个小时了

**问题分类**: CDN｜配置问题

### 问题描述

创建域名一直处理中，3-4个小时了

### 客服解答

**客户**：创建域名一直处理中，3-4个小时了
**客服**：您好已经处理完成

### 根本原因分析

域名配置或解析问题

---

## 81. 申请退款

**问题分类**: 账户与财务｜其他类咨询

### 问题描述

新购CDN申请

### 客服解答

**客户**：新购CDN申请
**客服**：您好是要退款cdn的资源包吗 给下订单号
**客户**：[密钥已脱敏]
**客服**：您好退款需要提交内部审批 大约1-2个工作日 请耐心等待

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 82. 域名绑定问题，域名cname配置问题

**问题分类**: CDN｜配置问题

### 问题描述

这是个zyyp-shop的image-zyyp-net-idvodqn.qiniudns.com 配置，我想再dxza-shop也配置，那这个image-zyyp-net-idvodqn.qiniudns.com不知道从哪里来的。我要在阿里云配置cname,从哪里查看

### 客服解答

**客户**：这是个zyyp-shop的image-zyyp-net-idvodqn.qiniudns.com 配置，我想再dxza-shop也配置，那这个image-zyyp-net-idvodqn.qiniudns.com不知道从哪里来的。我要在阿里云配置cname,从哪里查看
**客服**：您好您在我们这边创建的有cdn域名 image.zyyp.net这个域名分配的cname值是 image-zyyp-net-idvodqn.qiniudns.com
**客户**：我还想再配一个images.zyyp.net
**客服**：您好可以再创建images.zyyp.net 为cdn域名
**客户**：image.zyyp.net能配两个空间吗
**客户**：我想把dxza-shop 也配到image.zyyp.net下这样我就不用再搞个域名了
**客服**：您好，一个域名只能创建一次，你们image.zyyp.net如果在其他空间绑定过，就必须先删除，然后重新在  dxza-shop  空间绑定
**客户**：一个域名只能绑定一个空间
**客户**：我的新空间  dxza-shop还需要完善什么
**客户**：我准备使用images.zyyp.net  给dxza-shop
**客服**：您好，不需要完善什么，你们重新绑定即可，已经和你们说了，一个域名只能绑定一次，但是一个空间可以绑定如果干个域名dxza-shop 可以绑定 image.zyyp.net
image1.zyyp.net
image2.zyyp.net
...
zyyp-shop 可以绑定1image.zyyp.net
2image1.zyyp.net
3image2.zyyp.net
...
就是你们不要想着一个域名可以在两个空间使用 ，同一个域名不能在两个地方同时床架，你们两个空间必然要用两个不同的域名主域名可以衍生若干个子域名，前缀不同就行
**客服**：您好，不需要完善什么，你们重新绑定即可，已经和你们说了，一个域名只能绑定一次，但是一个空间可以绑定若干个域名dxza-shop 可以绑定image.zyyp.net
image1.zyyp.net
image2.zyyp.net
...
zyyp-shop 可以绑定1image.zyyp.net
2image1.zyyp.net
3image2.zyyp.net
...
就是你们不要想着一个域名可以在两个空间使用 ，同一个域名不能在两个地方同时床架，你们两个空间必然要用两个不同的域名主域名可以衍生若干个子域名，前缀不同就行
**客户**：我原来 zyyp-shop绑定 image.zyyp.net,我可不可以dxza-shop也绑定image.zyyp.net?
**客户**：你能帮我操作一下不
**客服**：您好，这个这边无法帮你操作的，你们需要自己去修改的，一个域名不可能同时绑定在两个空间！
你们自己去删除域名重新绑定，或者去域名配置里面，修改源站，修改存储空间，指向新空间
**客服**：不可能 image.zyyp.net 既绑定A 空间，又绑定B 空间，上面的回复已经说得非常清楚了
**客户**：这个是从哪里来的 ，image-zyyp-net-idvodqn.qiniudns.com
**客服**：您好，这个是域名绑定后，给特定域名分配的cname ，要去你们的域名控制台配置对应的cname解析后，域名才可以正式使用
**客户**：我先绑定域名，这个image-zyyp-net-idvodqn.qiniudns.com  才出来的？
**客服**：是的

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 83. 申请https证书的步骤

**问题分类**: CDN｜证书问题

### 问题描述

申请https证书的步骤

### 客服解答

**客户**：申请https证书的步骤
**客服**：您好，手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免[URL已脱敏]

### 根本原因分析

SSL证书配置或过期问题

---

## 84. 配置一个小时了卡住不动

**问题分类**: CDN｜配置问题

### 问题描述

配置一个小时了卡住不动

### 客服解答

**客户**：配置一个小时了卡住不动
**客服**：您好这边帮您手动介入处理下 请稍等
**客服**：已经处理好了
**客户**：还有一个域名 [URL已脱敏]
**客服**：处理完成

### 根本原因分析

域名配置或解析问题

---

## 85. 上传Https签名报错

**问题分类**: 对象存储｜其他类咨询

### 问题描述

[    [        {            "title": "请求 ID",            "content": "gNSEBUpbbrPrWPkX"        },        {            "title": "日志栈",            "content": "fusionicp:9;fusionsslcert:23/400"        }    ]]

### 客服解答

**客户**：[    [        {            "title": "请求 ID",            "content": "gNSEBUpbbrPrWPkX"        },        {            "title": "日志栈",            "content": "fusionicp:9;fusionsslcert:23/400"        }    ]][图片]
**客户**：点击保存签名，会报错
**客服**：您好给一下复现的录屏 这边看下

### 根本原因分析

SSL证书配置或过期问题

---

## 86. 怎么查询是否是七牛的回源访问IP以避免被拦截

**问题分类**: CDN｜其他类咨询

### 问题描述

怎么判断回源源服务器的来源IP是否是七牛云的IP，有API和在线查询的吗

### 客服解答

**客户**：怎么判断回源源服务器的来源IP是否是七牛云的IP，有API和在线查询的吗
**客服**：您好很抱歉这个暂时没有查询接口
**客户**：好的
**客服**：好的

### 根本原因分析

具体问题需要根据实际场景分析

---

## 87. 免费 from 自动催单

**问题分类**: CDN｜证书问题

### 问题描述

长时间处于免费证书申请环节

### 客服解答

**客户**：长时间处于免费证书申请环节
**客服**：您好，您使用的是一键升级 https，该操作需要七牛帮您申请一个免费的 ssl 证书， 当前证书正在等待CA机构颁发，期间您不要操作 ssl 证书服务，一般会在 2 小时左右处理升级完成，请耐心等待。
**客服**：您好，已处理完成

### 根本原因分析

SSL证书配置或过期问题

---

## 88. 对象存储如何设置使用预警信息

**问题分类**: 对象存储｜其他类咨询

### 问题描述

对象存储如何设置使用预警信息

### 客服解答

**客户**：对象存储如何设置使用预警信息
**客服**：您好，这个一般你们用账号余额告警 和 CDN流量带宽告警即可

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 89. 是否支持上传和审核同时进行

**问题分类**: 人工智能｜内容安全

### 问题描述

目前使用七牛云的对象存储上传图片，请问能否在上传后同时进行图片审核，审核结果跟随上传返回的信息一起返回总的来说，是否有图片上传对象存储和审核用一个接口实现的方式？

### 客服解答

**客户**：目前使用七牛云的对象存储上传图片，请问能否在上传后同时进行图片审核，审核结果跟随上传返回的信息一起返回总的来说，是否有图片上传对象存储和审核用一个接口实现的方式？

### 根本原因分析

对象存储配置或使用问题

---

## 90. CDN 只设置主域名 没有设置www.主域名，能识别www.主域名吗

**问题分类**: CDN｜配置问题

### 问题描述

CDN 只设置主域名 没有设置www.主域名，能识别www.主域名吗

### 客服解答

**客户**：CDN 只设置主域名 没有设置www.主域名，能识别www.主域名吗
**客服**：您好，这个不能的，你们如果需要对 www 域名加速，那么就需要绑定 www 域名到CDN的
**客户**：如果访问07430743.com  那我是不是要设置两个 一个是07430743.com的加速，另外一个是www.07430743.com
**客服**：您好，如果 07430743.com  需要加速，只要 绑定 07430743.com 到CDN即可，不需要绑定 www ，看你们自己的需求就是哪个域名要加速，就绑定哪个域名
**客户**：您好，你帮我看看为什么[URL已脱敏]
**客服**：您好，您的域名不支持https访问，您可以升级为https您可以在 [域名管理] 中，点击您想要配置https的域名右侧的 [配置] 按钮，在新的页面中，在 [https配置] 下点击 [修改配置] ,点击开启->免费证书→勾选 [同意七牛云代申请免费证书] →确认，之后输入您账号的密码即可。一键https使用的是免费证书，配置一键 https 需要注意：配置生效时间主要是用于等待 CA 机构签发证书，证书一旦签发会在 10 分钟内部署完成，整体一键 https 预计可在 2 小时内完成。期间您不要操作 ssl 证书服务，否则可能造成证书签发失败。免费证书只支持绑定单个普通域名，若您需要使用一级域名的免费证书，请到购买证书页购买免费证书开启了以下功能会导致代理验证失败，无法代理申请证书： 回源鉴权、时间戳防盗链、IP 黑白名单、referer 防盗链当前加速域名需要 CNAME 到七牛给您分配的 CNAME 域名 当前加速域名的 DNS 记录中不能有 CAA 记录，或者 CAA 记录包含 Digicert.com 和 digicert.com免费证书有效期为一年，过期请重新申请需要授权七牛云代申请免费证书注意事项升级https后，流量计费说明：[URL已脱敏]
**客户**：我不想用SSL证书，用80端口可以加速吗
**客服**：您好，您的源站好像并不支持https访问，您源站会有307重定向，或者您的这边源站修改下呢
**客户**：好的，我检 查一下
**客服**：您好，是不支持http访问，很抱歉，这边输入错误
**客户**：我已经改了加速模式是HTTPS了，访问显示403
**客服**：您好，这边查看下日志，稍等
**客户**：我换了遵循原协议又可以了，但是百度抓取我的网站又不能访问了。
**客户**：[URL已脱敏]
**客户**：[图片]The plain HTTp request was sent to HTTPs port.
**客服**：您好，这个是说您的源站不支持http访问，需要使用https访问的
**客户**：好的。
**客服**：您好，您再观察下，如果不知道http，可以开启下强制https
**客户**：为什么[URL已脱敏] 无法访问，而[URL已脱敏] 可以 ，我源站这两个域名都设置了一样的配置
**客户**：提示 HTTP ERROR 508
**客户**：找到原因了 是我配置七牛回源协议出问题了
**客服**：您好，好的，您目前已经正常了对吗？
**客户**：正常了
**客服**：您好，好的，您再观察下，有什么问题您再反馈

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 91. 接入了两个域名，不同的协议有没有什么影响？

**问题分类**: CDN｜配置问题

### 问题描述

接入了两个域名，不同的协议有没有什么影响？一个http偶尔用一下，一个https长期使用，偶尔需要切换，有没有什么影响？

### 客服解答

**客户**：接入了两个域名，不同的协议有没有什么影响？一个http偶尔用一下，一个https长期使用，偶尔需要切换，有没有什么影响？[图片][图片]
**客服**：您好，两个域名互相独立，没有什么影响的，只是 HTTPS的网站 ，必须用 HTTPS 加载，这个你们留意下即可
**客户**：接入了两个域名，不同的协议，少说了一点，两个指向同一个储存桶？意思是CDN加速同一个东西，一个http偶尔用一下，一个https长期使用，偶尔需要切换有什么影响吗？
**客服**：您好，没有影响的
**客户**：好的，同时开启两个也没什么影响吧
**客服**：没有的

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 92. 怎么查询手机号绑定了多少账号？

**问题分类**: 账户与财务｜账户问题

### 问题描述

怎么查询自己的手机号绑定了多少账号？

### 客服解答

**客户**：怎么查询自己的手机号绑定了多少账号？
**客服**：您好，这个您无法查询，您可以提供一个具体手机号，这边帮您核实
**客户**：[REDACTED_PHONE]
**客服**：好的
**客服**：您好，手机号已绑定4个邮箱d**@yunjihd.comq***[REDACTED_EMAIL]fu*********[REDACTED_EMAIL]312****[REDACTED_EMAIL]你们确认下
**客户**：有一个账号是之前公司的，公司已经倒闭了，我需要怎么样才能解绑？
**客服**：您好，您可以考虑申请注销的，登录到那个账号后申请注销

### 根本原因分析

具体问题需要根据实际场景分析

---

## 93. 存在对象存储的图片怎么开启gzip压缩

**问题分类**: 对象存储｜其他类咨询

### 问题描述

存在对象存储的图片怎么开启gzip压缩

### 客服解答

**客户**：存在对象存储的图片怎么开启gzip压缩
**客服**：您好，gzip 压缩只是对 js txt 等文本文件生效，图片是不生效的，图片在域名配置中，开启图片瘦身即可

### 根本原因分析

对象存储配置或使用问题

---

## 94. 免费 from 自动催单

**问题分类**: CDN｜证书问题

### 问题描述

长时间处于免费证书申请环节

### 客服解答

**客户**：长时间处于免费证书申请环节
**客服**：您好，您使用的是一键升级 https，该操作需要七牛帮您申请一个免费的 ssl 证书， 当前证书正在等待CA机构颁发，期间您不要操作 ssl 证书服务，一般会在 2 小时左右处理升级完成，请耐心等待。

### 根本原因分析

SSL证书配置或过期问题

---

## 95. 这样配置下载什么影响吗？

**问题分类**: 对象存储｜上传下载

### 问题描述

接入了两个域名，不同的协议，两个指向同一个储存桶？意思是CDN加速同一个东西OSS储存空间，一个http用于Kodo Browse下载，一个https长期使用，偶尔需要切换，有什么影响吗？

### 客服解答

**客户**：接入了两个域名，不同的协议，两个指向同一个储存桶？意思是CDN加速同一个东西OSS储存空间，一个http用于Kodo Browse下载，一个https长期使用，偶尔需要切换，有什么影响吗？[图片][图片]
**客服**：你好，你们不要提交重复工单，域名互相隔离独立，没有影响
**客户**：不是提交重复的问题，而是之前问你们内部下载问题的时候说没有解决方案，这个方案是自己研究出来的，所以对你们七牛的工程师不放心，你们七牛工程工师很少吗？问来问去是同一个人在回答？重要的问题，问两个不同的人不可以吗？
**客服**：您好，域名互相隔离独立的，没有影响的

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 96. 增量审核设置后，图片还可以公网访问

**问题分类**: 人工智能｜内容安全

### 问题描述

添加指定bucket任务后，增量审核记录中能看到违规条数，但是七牛云上传返回的地址还可以打开该违规图片，自动禁用已选择

### 客服解答

**客户**：添加指定bucket任务后，增量审核记录中能看到违规条数，但是七牛云上传返回的地址还可以打开该违规图片，自动禁用已选择
**客服**：您好，麻烦 您提供一个封禁后还可以访问的链接，这边帮您确认核实下
**客户**：[URL已脱敏]
**客户**：[图片]这是我的增量设置
**客服**：您好，请稍等
**客服**：您好，已帮您做特殊配置，预计10分钟生效，生效后只要封禁就无法访问
**客户**：好的，一会我再测试下。后续如果有其他bucket需要审核，我该如何配置
**客服**：您好，您到时将域名提供下，工单申请AI及时通讯，这边帮您处理即可

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 97. 云存储，中国有一些省份无法访问

**问题分类**: 对象存储｜其他类咨询

### 问题描述

云存储，中国有一些省份无法访问，比如安徽，广东，江苏cigarhome.org

### 客服解答

**客户**：云存储，中国有一些省份无法访问，比如安徽，广东，江苏cigarhome.org
**客户**：北京，福建，甘肃，海南，河南，湖南，吉林；江西，内蒙古，宁夏，山东，陕西，上海，四川，浙江中国32省份地区，以上这些地区正常，其余的打不开，请问是不是服务器节点问题，可以处理吗
**客服**：你好，请稍等
**客服**：您好，麻烦您提供下具体CDN域名，这边帮您核实
**客户**：yan.jazxzw.com
**客服**：您好，已帮您做了节点优化，您稍后再观察下看看呢

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 98. 缓存时间怎么定，是不是越长越好？

**问题分类**: CDN｜配置问题

### 问题描述

缓存时间怎么定，是不是越长越好吗，需要考虑什么？设置时间越长，是不是意味着CDN回源流量用得越少？

### 客服解答

**客户**：缓存时间怎么定，是不是越长越好吗，需要考虑什么？设置时间越长，是不是意味着CDN回源流量用得越少？[图片]
**客服**：您好，理论是的，这个看你们自己的需求，一些经常需要发生变更的资源，可以设置缓存时间0 ，默认全局缓存30天
**客户**：设置时间越长，是不是意味着CDN回源流量用得越少？
**客服**：是的
**客户**：主要用于OSS图片加速，假设缓存设置了10天，个人网站图片更新了，10天内拉取数据不是变更后的数据，而是之前缓存的？
**客服**：是的，这个时候要主动刷新缓存的
**客户**：有没有针对某个更新过的链接，单独主动刷新缓存的操作，是怎么操作？
**客服**：您好，刷新缓存方法请参考：[URL已脱敏] portal.qiniu.com 控制台刷新缓存，点击左侧 cdn => 刷新预取方法2: api 接口地址：[URL已脱敏] : url 刷新，全网生效 10min 左右，目录刷新需要 30min 左右
**客户**：1.可以设置缓存时间0 ，是相当于不缓存不消耗回源流量吗    2.但是CDN下行又要去调取，缓存资源？
**客服**：您好，缓存时间0 ，相当于100%回源，CDN 节点没有缓存，一定会产生回源流量的
**客服**：所以设置0 是对动态业务的部分设置，不能设置全局缓存时间0

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 99. 登录邮箱密码 找不到

**问题分类**: 账户与财务｜其他类咨询

### 问题描述

你好 我这边注册当时是用的微信 直接绑定的  我刚才绑定完邮箱 用邮箱登录 没有密码 请问怎么设置 邮箱登录密码 ，没有找到 手机号登录页面

### 客服解答

**客户**：你好 我这边注册当时是用的微信 直接绑定的  我刚才绑定完邮箱 用邮箱登录 没有密码 请问怎么设置 邮箱登录密码 ，没有找到 手机号登录页面
**客服**：您好，这个你可以在登录页面重置密码，或者在这里修改密码即可[URL已脱敏]

### 根本原因分析

具体问题需要根据实际场景分析

---

## 100. 有没有接口可以查询到账户余额是否欠费

**问题分类**: 账户与财务｜计费问题

### 问题描述

我们是软件系统厂商，需要在系统上显示七牛是否欠费，否则等冻结了才发现就晚了，系统就用不了了

### 客服解答

**客户**：我们是软件系统厂商，需要在系统上显示七牛是否欠费，否则等冻结了才发现就晚了，系统就用不了了
**客户**：因为我们系统用的是七牛云cdn
**客户**：客户等cdn域名无法访问了才发现，平时也不怎么看手机和邮箱
**客服**：您好，请稍等
**客服**：您好，已电话联系，您看下这里的api接口[URL已脱敏]

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 101. 发票

**问题分类**: 账户与财务｜发票问题

### 问题描述

1月支出的发票申请不到

### 客服解答

**客户**：1月支出的发票申请不到
**客服**：您好，超出6个月充值金额，或低于1000元金额的发票，您无法自行申请，不清楚金额的话可以在开票金额栏填写全部金额还请您在控制台提前申请准备好对应的发票抬头信息，添加对应的专票抬头信息审核通过后，如果您已经有了专票的抬头信息，可以不用再次添加，另外，给您开的发票默认是数电发票，需要纸质发票可以说明需求，提供收件地址。根据《增值税专用发票使用规定》申请专票必须要和实名认证公司名保持一致。-------------开票信息-----------开票金额:发票抬头: 发票类型: 纳税人识别号: 开户银行名称: 开户账号: 公司名称: 公司地址: 联系电话:
**客户**：-------------开票信息-----------开票金额:206发票抬头: 发票类型: 纳税人识别号: 开户银行名称: 开户账号: 公司名称: 公司地址: 联系电话:
**客服**：您好，您提供一个电话联系方式，这边商务会在明日与您联系，您看下是否可以
**客户**：[REDACTED_PHONE]
**客服**：好的
**客服**：你好，请问商务是否已与您联系并协助开票了呢

### 根本原因分析

企业认证需要提供社会信用代码或营业执照号

---

## 102. 证书验证通过后无法使用，还是显示待确认

**问题分类**: CDN｜证书问题

### 问题描述

证书验证通过后无法使用，还是显示待确认

### 客服解答

**客户**：证书验证通过后无法使用，还是显示待确认
**客服**：您好，麻烦您将您的验证记录截图这边看下，这边帮您确认核实下
**客户**：如图[图片]
**客服**：好的
**客户**：这个也是[图片]
**客服**：您好，8-28订单失效了，你们得重新申请了，9-28的还在核实
**客户**：好的
**客服**：您好，已签发证书

### 根本原因分析

SSL证书配置或过期问题

---

## 103. js 的 fetch读取的图片为跨域，导致fetch的ok状态为false怎么解决？

**问题分类**: 对象存储｜上传下载

### 问题描述

js 的 fetch读取的图片为跨域，导致fetch的ok状态为false怎么解决？code...fetch(imgUrl, { mode: 'no-cors' })        .then((response: Response) => {            console.log('response', response)            return response.blob()        })        .then((blob: any) => {            console.log('blob:', blob)            option.img = URL.createObjectURL(blob)            console.log(33333, option.img)        })

### 客服解答

**客户**：js 的 fetch读取的图片为跨域，导致fetch的ok状态为false怎么解决？code...fetch(imgUrl, { mode: 'no-cors' })        .then((response: Response) => {            console.log('response', response)            return response.blob()        })        .then((blob: any) => {            console.log('blob:', blob)            option.img = URL.createObjectURL(blob)            console.log(33333, option.img)        })
**客服**：您好，fetch 接口不支持前端跨域的，这个fetch ，你们要在服务端执行，客户端向服务端发起fetch请求，服务端调用 fetch接口即可
**客户**：但是同行 没有做服务器转发 直接就可以跨域访问你们的地址是怎么做到的：[图片]
**客服**：您好，您说的是 CDN 域名么，你将有跨域的链接提供下，这边帮您检查下
**客户**：[URL已脱敏]
**客服**：您好，这个域名默认支持跨域的 ，你们这个貌似是有本地缓存吧，你们禁用本地缓存试试[图片]
**客户**：可是为什么获取的图片 blob 是空？[图片]
**客服**：您好，这个要你们自己确认下了，看下是不是有什么报错，存储不支持返回blob的，你们看下是不是转换的有问题还是其他什么原因

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 104. 出现报错问题

**问题分类**: 对象存储｜其他类咨询

### 问题描述

如下。修改SSL和催单报错请求 IDDAFDChMCGJe5ZvkX, DAFDChMCGJe5ZvkX, DAFDChMCGJe5ZvkX, DAFDChMCGJe5ZvkX日志栈FUSIONLINE:3;FUSIONLINE:3;BUCKET:10;BUCKET:14;fusionsslcert:4;fusiondomain_cud:90/400;APIS:104/400;PORTAL-PROXY:149/400[    [        {            "title": "请求 ID",            "content": "D8JIKgMIFf6mZvkX, D8JIKgMIFf6mZvkX, D8JIKgMIFf6mZvkX, D8JIKgMIFf6mZvkX"        },        {            "title": "日志栈",            "content": "fusiondomain_cud:2/400;APIS:96/400;PORTAL-PROXY:148/400"        }    ],    [        {            "title": "请求 ID",            "content": "0IL5qwp4LT6nZvkX, 0IL5qwp4LT6nZvkX, 0IL5qwp4LT6nZvkX, 0IL5qwp4LT6nZvkX"        },        {            "title": "日志栈",            "content": "fusiondomain_cud:1/400;APIS:70/400;PORTAL-PROXY:135/400"        }    ]]

### 客服解答

**客户**：如下。修改SSL和催单报错请求 IDDAFDChMCGJe5ZvkX, DAFDChMCGJe5ZvkX, DAFDChMCGJe5ZvkX, DAFDChMCGJe5ZvkX日志栈FUSIONLINE:3;FUSIONLINE:3;BUCKET:10;BUCKET:14;fusionsslcert:4;fusiondomain_cud:90/400;APIS:104/400;PORTAL-PROXY:149/400[    [        {            "title": "请求 ID",            "content": "D8JIKgMIFf6mZvkX, D8JIKgMIFf6mZvkX, D8JIKgMIFf6mZvkX, D8JIKgMIFf6mZvkX"        },        {            "title": "日志栈",            "content": "fusiondomain_cud:2/400;APIS:96/400;PORTAL-PROXY:148/400"        }    ],    [        {            "title": "请求 ID",            "content": "0IL5qwp4LT6nZvkX, 0IL5qwp4LT6nZvkX, 0IL5qwp4LT6nZvkX, 0IL5qwp4LT6nZvkX"        },        {            "title": "日志栈",            "content": "fusiondomain_cud:1/400;APIS:70/400;PORTAL-PROXY:135/400"        }    ]]
**客服**：您好，请问您具体是哪个域名需要调整呢
**客户**：file.yzycoc.com
**客服**：好的
**客服**：您好，当前域名状态有些问题，这边还在处理中，会尽快协助您处理完成
**客服**：您好，您现在重新修改配置试试呢
**客服**：你好，当前还在持续处理中，预计最迟会在明日处理完成，您看下是否可以呢
**客服**：你好，域名已经可以处理，您现在再试试呢
**客户**：好的，我尝试下

### 根本原因分析

SSL证书配置或过期问题

---

## 105. 提现资金

**问题分类**: 账户与财务｜计费问题

### 问题描述

余额拿出来

### 客服解答

**客户**：余额拿出来
**客服**：您好，根据我司的退款的流程，请提供以下信息，后续商务会走退款审批流程。另外，因退款周期需要看审批进度，还请您耐心等待，感谢您对我们工作的支持与配合！以下是退款需要提供的信息：第一步：核实注册人信息注册时间：注册人名字：注册人电话：注册人邮箱：第二步：财务信息是否开具过发票：退款金额：收款方名称：收款方开户行：（详细到支行信息）收款方银行账号：退款原因：注意：企业认证需要退款到企业账户，个人认证可以直接退到个人银行卡账户，退款仅支持退回到实名认证人的银行卡号中2.退款需要结清本月账单，如果本月有产生计费，需要等待次月扣款完成之后才能安排打款。3.是否有开具发票，如果开具发票需要寄回。将发票邮寄至以下地址：收件人：王俊瑛电话：[REDACTED_PHONE]地址：上海市浦东新区张江高科技园区亮秀路81号浦东软件园Q座 (南门)
**客户**：注册时间：2015年4月29日注册人名字：彭政富注册人电话：[REDACTED_PHONE]注册人邮箱：[REDACTED_EMAIL]第二步：财务信息是否开具过发票：否退款金额：8.77收款方名称：彭政富收款方开户行：中国建设银行股份有限公司罗定支行收款方银行账号：6217003270001360569退款原因：用不上了
**客服**：好的，这边商务会尽快协助您完成注销的
**客服**：好的，这边商务会尽快协助您完成的
**客户**：几个月过去了，为什么还不给提现
**客服**：您好，请稍等，这边帮您催促下
**客服**：您好，当前只支持原路返回，将返回到至支付宝账号814***[REDACTED_EMAIL]，您看下是否可以，或者麻烦您提供一个联系方式，这边商务与您联系
**客户**：返回到至支付宝账号814***[REDACTED_EMAIL]可以
**客服**：您好，收到，这边同步下商务为您跟进
**客服**：好的，已帮您申请，预计会尽快帮你完成提现
**客户**：好的
**客服**：好的

### 根本原因分析

企业认证需要提供社会信用代码或营业执照号

---

## 106. 之前备案的域名过期了，导致本平台的所有图片无法访问

**问题分类**: 对象存储｜上传下载

### 问题描述

之前备案的域名过期了，导致本平台的所有图片无法访问 该怎么拿到之前上传的所有图片

### 客服解答

**客户**：之前备案的域名过期了，导致本平台的所有图片无法访问 该怎么拿到之前上传的所有图片
**客户**：之前备案的域名过期了，导致本平台的所有图片无法访问 该怎么拿到之前上传的所有图片
**客服**：您好您可以使用最新的图形化工具kodo-browser上传/下载试下，支持批量管理。[URL已脱敏]

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 107. 充值了,但是账单里没有

**问题分类**: 账户与财务｜计费问题

### 问题描述

充值了,但是账单里没有

### 客服解答

**客户**：充值了,但是账单里没有
**客服**：您好，请您提供充值回单，这边同步商务为您跟进处理。

### 根本原因分析

具体问题需要根据实际场景分析

---

## 108. {"error":"invalid range: failed to overlap"}

**问题分类**: 对象存储｜上传下载

### 问题描述

{"error":"invalid range: failed to overlap"}

### 客服解答

**客户**：{"error":"invalid range: failed to overlap"}
**客户**：[URL已脱敏]
**客服**：您好，请稍等
**客服**：您好，这个是你们源文件异常，这个是个0字节的文件，你们确认下呢
**客户**：我已经搞定，根本原因是，接口这里，域名，我没有加[URL已脱敏]
**客服**：好的

### 根本原因分析

域名配置或解析问题

---

## 109. 域名证书买错了，可否退款

**问题分类**: 对象存储｜其他类咨询

### 问题描述

域名证书买错了，可否退款，写错二级域名了，因为填的时候提示的让人误解了

### 客服解答

**客户**：域名证书买错了，可否退款，写错二级域名了，因为填的时候提示的让人误解了
**客服**：您好，您将订单号提供下，这边明日帮您申请吊销证书申请退款
**客户**：[密钥已脱敏]
**客服**：好的

### 根本原因分析

SSL证书配置或过期问题

---

## 110. ssl证书显示“域名所有权验证未通过”

**问题分类**: 账户与财务｜账户问题

### 问题描述

这种情况我该怎么办，该如何操作，麻烦教一下

### 客服解答

**客户**：这种情况我该怎么办，该如何操作，麻烦教一下
**客户**：怎么才能验证通过域名所有权
**客服**：您好，你们去添加一个 cname解析即可
验证类型	cname
主机记录 _[密钥已脱敏].jinz
记录值	[密钥已脱敏].[密钥已脱敏].cmcdt3iloxipxn.trust-provider.com

### 根本原因分析

域名配置或解析问题

---

## 111. 时间戳防盗链和回源鉴权如何设置

**问题分类**: CDN｜配置问题

### 问题描述

由于看不懂，所以问下，这个时间戳防盗链和回源鉴权怎么操作呢

### 客服解答

**客户**：由于看不懂，所以问下，这个时间戳防盗链和回源鉴权怎么操作呢
**客服**：你好，时间戳防盗链，需要基于 key 去签算访问链接，你们要去砍时间戳防盗链的签算算法回源鉴权是CDN将请求参数转发到你们的鉴权服务器上，然后你们的鉴权地址接受请求，对参数校验，返回200 ，对CDN请求放行，返回403 ，对CDN请求拦截这两个都需要您参考文档，然后去服务器用代码实现的
**客户**：不懂，有没有简易的图文教程
**客户**：最好是视频操作教程
**客服**：您好，这个视频教程没有的，或者您也可以百度下，各家配置基本都是大差不差，通用的
**客户**：好吧，那图文教程你这有嘛
**客服**：您好，这个只有文档的[URL已脱敏]

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 112. 配置https一直在处理中

**问题分类**: CDN｜配置问题

### 问题描述

1、修改 HTTPS 配置处理中，通常情况下 8-15 分钟完成，期间域名访问不受影响，部分配置不可修改，若较长时间未配置完成，请提交工单反馈 。2、MX和CNAME解析冲突，如何解决？

### 客服解答

**客户**：1、修改 HTTPS 配置处理中，通常情况下 8-15 分钟完成，期间域名访问不受影响，部分配置不可修改，若较长时间未配置完成，请提交工单反馈 。2、MX和CNAME解析冲突，如何解决？
**客服**：您好，请稍等
**客服**：您好，冲突的话，你们只能换个域名，暂时没有其他更好的方式的
**客服**：您好，域名当前存在海外配置，预计还需要40min ，请您先耐心等待
**客户**：[URL已脱敏]
**客服**：您好，你们域名是纯海外加速，国内访问效果较差的，如果想要国内访问，域名需要设置全球加速或者国内加速才可以，国内加速域名必须有备案
**客户**：有一部分js文件访问的时候会返回错误[图片]
**客户**：域名tengzhou.ren 空间mjhblog
**客户**：域名mjh.im 空间mjhwww域名tengzhou.ren 空间mjhblog都是这个情况
**客服**：把存储空间的referer关闭一下再访问

### 根本原因分析

CDN配置或缓存问题，需要检查域名配置和缓存策略

---

## 113. 又卡壳了

**问题分类**: CDN｜配置问题

### 问题描述

网站卡壳了一直在配置域名mzf.heiyu.cc；域名添加不上见图

### 客服解答

**客户**：网站卡壳了一直在配置域名mzf.heiyu.cc；域名添加不上见图[图片]
**客服**：您好，您的原则有pay.heiyu.cc这个测试资源吗？
**客户**：没看懂
**客服**：就是您的源站可以访问到这个资源吗？需要可以正常访问到的资源才行的[URL已脱敏]
**客户**：[    [        {            "title": "请求 ID",            "content": "3IDeWGwKF2X4A_oX"        },        {            "title": "日志栈",            "content": "PORTAL-PROXY:35/500"        }    ]]
**客户**：[    [        {            "title": "请求 ID",            "content": "D0BBDmMCh7EKBPoX"        },        {            "title": "日志栈",            "content": "PORTAL-PROXY:32/500"        }    ],    [        {            "title": "请求 ID",            "content": "0PVhd4UAYs[密钥已脱敏]BPoX"        },        {            "title": "日志栈",            "content": "PORTAL-PROXY:31/500"        }    ],    [        {            "title": "请求 ID",            "content": "qIBQfwBsPc[密钥已脱敏]BPoX"        },        {            "title": "日志栈",            "content": "PORTAL-PROXY:34/500"        }    ],    [        {            "title": "请求 ID",            "content": "CkFhvAgAD8EKBPoX"        },        {            "title": "日志栈",            "content": "PORTAL-PROXY:33/500"        }    ],    [        {            "title": "请求 ID",            "content": "DhAHD0Ln9sEKBPoX"        },        {            "title": "日志栈",            "content": "PORTAL-PROXY:31/500"        }    ],    [        {            "title": "请求 ID",            "content": "D9AbJyAw4c[密钥已脱敏]BPoX"        },        {            "title": "日志栈",            "content": "PORTAL-PROXY:35/500"        }    ],    [        {            "title": "请求 ID",            "content": "Ch5D3IQagMEKBPoX"        },        {            "title": "日志栈",            "content": "PORTAL-PROXY:36/500"        }    ]]
**客户**：[    [        {            "title": "请求 ID",            "content": "DduQH7jAuEoQBPoX"        },        {            "title": "日志栈",            "content": "PORTAL-PROXY:32/500"        }    ]]
**客户**：[图片]1
**客服**：您好，页面异常，正常处理中，请稍等
**客服**：已修复

### 根本原因分析

域名配置或解析问题

---

## 114. 我上传到存储空间的文件无法显示

**问题分类**: 对象存储｜上传下载

### 问题描述

我原本上传到存储空间的图片是可以正常显示的,然后有一天我发现无法在我的网站上加载出存储在云空间的图片了,我打开控制台发现上传到云空间在本网站上也无法显示.之前是没问题的,是怎么回事呢?

### 客服解答

**客户**：我原本上传到存储空间的图片是可以正常显示的,然后有一天我发现无法在我的网站上加载出存储在云空间的图片了,我打开控制台发现上传到云空间在本网站上也无法显示.之前是没问题的,是怎么回事呢?
**客服**：您好，您这边能提供下具体的资源链接吗
**客户**：啊...我知道原因了....域名我忘了这茬......
**客服**：好的

### 根本原因分析

对象存储配置或使用问题

---

