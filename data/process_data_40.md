# 技术支持工单数据 - Part 40

本文档包含 114 个结构化技术支持问答记录

---

## 一直返回同一个uploadId，并且提示{"error":"no such uploadId"}

**问题分类**: 对象存储｜上传下载

### 问题描述

请求获取uploadId 但是每次返回的都是同一个，uploadId 是 671f6a43***

### 客服解答

1. 您好，您这边使用的是什么语言的SDK上传？您的这个ID是什么值，我们上传是没有uploadId这个参数的

2. 您好，您这边是上传多大的文件呢？

3. 您好，默认是4mb为一片的，所以一直都是一片的，您这边使用一下这个demo上传吧https://github.com/qiniu/java-sdk/blob/master/examples/upload.java

4. 您好，分片上传也是上传单文件的，只是上传方式是分片了，后面还是会合成的

5. 您好，分片上传v2java sdk提供了demo，您可以测试下呢：https://github.com/qiniu/java-sdk/blob/master/examples/upload_v2_api.java

### 根本原因分析

认证凭证或权限配置问题

### 完整对话记录

**客户**：请求获取uploadId 但是每次返回的都是同一个，uploadId 是 671f6a43***

**客户**：异常堆栈uploadToken=o5wkhBmO***:yh648J6a***=:eyJzY29w*** 18:42:22.088 [http-nio***] ERROR c.a.f.a.s.upload.controller.FileUploadController - PostChunk failedcom.qiniu.common.QiniuException: PUT http://up-na0.qiniup.com/***  {ResponseInfo:com.qiniu.http.Response@40fc196c,status:612, reqId:s7EAAAA3yBDQlwIY, xlog:X-Log, xvia:, adress:up-na0.qiniup.com/148.153.*.*:80, duration:6.989000 s, error:no such uploadId}  {"error":"no such uploadId"}	at com.qiniu.http.Client.send(Client.java:429)	at com.qiniu.storage.Api.innerRequest(Api.java:123)	at com.qiniu.storage.Api.requestW***(Api.java:144)	at com.qiniu.storage.ApiUploa***.request(ApiUploa***.java:66)

**客服**：您好，您这边使用的是什么语言的SDK上传？您的这个ID是什么值，我们上传是没有uploadId这个参数的

**客户**：您好，我是使用的JAVA-SDK，V2 分片上传有一个uploadId的参数的

**客服**：您好，您这边是上传多大的文件呢？

**客户**：我贴一下我 这边的代码import com.qiniu.common.QiniuException;import com.qiniu.common.Zone;import com.qiniu.http.Client;import com.qiniu.http.Response;import com.qiniu.storage.*;import com.qiniu.storage.model.DefaultPutRet;import com.qiniu.util.Auth;import lombok.extern.slf4j.Slf4j;import org.springframework.web.multipart.MultipartFile;import java.io.IOException;import java.util.HashMap;import java.util.List;import java.util.Map;import java.util.Objects;import java.util.stream.Collectors;@Slf4jpublic class FileStor*** {    private FileStor*** properties;    private Auth auth;    private String uploadToken;    private Long uploadTokenExpires;    private ApiUploa*** apiUploa***;    private ApiUploa*** apiUploa***;    private ApiUploa*** apiUploa***;    private BucketManager bucketManager;    private Client client;    private Configuration configuration;    public FileStor***(FileStor*** properties) {        this.properties = properties;        this.auth = Auth.create(properties.getAccessKey(), properties.getSecretKey());    }    /**     * 获取上传token，避免反复创建     *     * @return uploadToken     */    public String getUploadToken() {        if (Objects.isNull(uploadToken) || uploadTokenExpires < System.currentTimeMillis()) {            refreshToken(properties.getBucket());        }        return uploadToken;    }    private String uploadToken(String bucket) {        return auth.uploadToken(bucket);    }    private void refreshToken(String bucket) {        uploadToken = uploadToken(bucket);        System.out.println("uploadToken="+uploadToken);        uploadTokenExpires = System.currentTimeMillis() + 1000 * 7000;    }    public ApiUploa*** getApiUp***() {        if (Objects.isNull(apiUploa***)) {            client = getClient();            apiUploa*** = new ApiUploa***(client);        }        return apiUploa***;    }    public ApiUploa*** getApiUp***() {        if (Objects.isNull(apiUploa***)) {            client = getClient();            apiUploa*** = new ApiUploa***(client);        }        return apiUploa***;    }    public ApiUploa*** getApiUp***() {        if (Objects.isNull(apiUploa***)) {            client = getClient();            apiUploa*** = new ApiUploa***(client);        }        return apiUploa***;    }    private BucketManager getBucketManager() {        if (Objects.isNull(bucketManager)) {            Configuration configuration = new Configuration(Zone.zone0());            bucketManager = new BucketManager(auth, configuration);        }        return bucketManager;    }    public Client getClient() {        if (client == null) {            client = new Client(getConfiguration());        }        return client;    }    public Configuration getConfiguration() {        if (configuration == null) {            configuration = new Configuration(Zone.autoZone());            configuration.resumabl*** = Configuration.Resumabl***.V2;        }        return configuration;    }    public boolean delete(String key) {        try {            getBucketManager().delete(properties.getBucket(), key);            log.warn("delete file ok||bucket={}||key={}", properties.getBucket(), key);            return true;        } catch (Exception e) {            log.error("delete file failed||key={}||error:", key, e);        }        return false;    }    /******分片上传 开始********/    /**     * 获取上传id     *     * @param path     文件路径 test-media     * @param fileName 文件名 a-1.jpeg     * @return     */    public String getUploadId(String path, String fileName) throws QiniuException {        ApiUploa***.Request initUploadRequest = new ApiUploa***.Request(this.properties.getUrlPrefix(), getUploadToken()).setKey(path + "/" + fileName);        ApiUploa***.Response initUploadResponse = getApiUp***().request(initUploadRequest);        return initUploadResponse.getUploadId();    }    /**     * 上传文件切片     *     * @param file         文件     * @param path         存储路径     * @param saveFileName 保存文件名     * @param partNumber   第几块切片     * @return 是否上传成功     */    public PartInfo uploadMultiPartFile(String uploadId, MultipartFile file, String path, String saveFileName, int partNumber) throws IOException {        String urlPrefix = this.properties.getUrlPrefix();        String token = getUploadToken();        // 上传文件数据        byte[] partData = file.getBytes();        PartInfo partInfo = new PartInfo();        ApiUploa***.Request uploadPartRequest = new ApiUploa***.Request(urlPrefix, token, uploadId, partNumber).setKey(path + "/" + saveFileName).setUploadData(partData, 0, partData.length, null);        ApiUploa***.Response uploadPartResponse = this.getApiUp***().request(uploadPartRequest);        partInfo.setMd5(uploadPartResponse.getMd5());        partInfo.setPartNumber(partNumber);        partInfo.setEtag(uploadPartResponse.getEtag());        return partInfo;    }    /**     * 组织上传的文件     *     * @param partInfoList 已上传文件信息     * @param path         保存路径 dev-test     * @param saveFileName 保存文件名     */    public String assembleUploadFile(String uploadId, List<PartInfo> partInfoList, String path, String saveFileName) throws IOException {        String urlPrefix = this.properties.getUrlPrefix();        String token = this.getUploadToken();        // 将pageInfo转化为map        List<Map<String, Object>> partInfoMapList = partInfoList.stream().map(partInfo -> {            Map<String, Object> map = new HashMap<>();            map.put("partNumber", partInfo.getPartNumber());            map.put("etag", partInfo.getEtag());            return map;        }).collect(Collectors.toList());        //参数,x:foo为必带        Map<String, Object> customParam = new HashMap<>();        customParam.put("x:foo", "foo-Value");        ApiUploa***.Request complete*** = new ApiUploa***.Request(urlPrefix, token, uploadId, partInfoMapList).setKey(path + "/" + saveFileName).setFileName(saveFileName).setCustomParam(customParam);        ApiUploa***.Response complete*** = getApiUp***().request(complete***);        log.info("complete upload:{}", complete***.getResponse());        DefaultPutRet ret = JsonUtils.parseObject(complete***.getResponse().bodyString(), DefaultPutRet.class);        return this.getUrl(ret.key);    }    /******分片上传 结束********/    public String getUrl(String key) {        return properties.getHost() + "/" + key;    }}

**客户**：第一步调用  public String getUploadId(String path, String fileName) 是成功的，就是每次都返回相同的内容第二步调用 public PartInfo uploadMultiPartFile(String uploadId, MultipartFile file, String path, String saveFileName, int partNumber) throws IOException { 的时候 就提示 {"error":"no such uploadId"}

**客户**：这边上传的文件是1MB

**客服**：您好，默认是4mb为一片的，所以一直都是一片的，您这边使用一下这个demo上传吧https://github.com/***

**客户**：单文件的我之前已经试过了，是可以的，我现在就是要试一下这种分片的。我找一个大文件试一下吧

**客服**：您好，分片上传也是上传单文件的，只是上传方式是分片了，后面还是会合成的

**客服**：您好，分片上传v2java sdk提供了demo，您可以测试下呢：https://github.com/***

**客户**：谢谢，我再看看

---

## 上传文件失败

**问题分类**: 对象存储｜上传下载

### 问题描述

从阿里云香港上传文件失败，{"level":"error","event_time":"2024-10-28 19:22:08.583","msg":"fileId=f611b004***,upload to qiniu err=Post \"https://upload.qiniup.com/***": EOF","stacktrace":"github.com/roodeag/ai-healthcare/router/handler.fileUpload.func1\n\t/Users/roodeag/roodea20241009/github.com/ai-healthcare/router/handler/upload.go:182"}

### 客服解答

1. 您好，辛苦您提供以下信息，我们排查下：完整的上传报错信息上传设备的 IP 和 DNS；https://ping.huatuo.qq.com/上传token：上传速度检测   https://www.bandwidthplace.com/ping 上传域名 测试截图

2. 您好，这个报错是网络异常导致的，你们试试将dns指向8.8.8.8 试试，看看是否可以呢

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：从阿里云香港上传文件失败，{"level":"error","event_time":"2024-10-28 19:22:08.583","msg":"fileId=f611b004***,upload to qiniu err=Post \"https://upload.qiniup.com/***": EOF","stacktrace":"github.com/roodeag/ai-healthcare/router/handler.fileUpload.func1\n\t/Users/roodeag/roodea20241009/github.com/ai-healthcare/router/handler/upload.go:182"}

**客服**：您好，辛苦您提供以下信息，我们排查下：完整的上传报错信息上传设备的 IP 和 DNS；https://ping.huatuo.qq.com/***   https://www.bandwidthplace.com/*** 上传域名 测试截图

**客户**：[图片]1.上传报错信息是：Post \"https://upload.qiniup.com/***": EOF"2.设备ip：47.242.*.*.上传token：我是通过服务端go代码上传的，不知道是不是报错里的这个：ZjYxMWIw***.5.root@iZj6c2kx***:~/app/build# ping upload.qiniup.comPING globalcdndynamic.qiniu.com.w.kunlungr.com (163.181.*.*) 56(84) bytes of data.64 bytes from 163.181.*.*: icmp_seq=1 ttl=57 time=1.68 ms64 bytes from 163.181.*.*: icmp_seq=2 ttl=57 time=1.71 ms64 bytes from 163.181.*.*: icmp_seq=3 ttl=57 time=1.71 ms64 bytes from 163.181.*.*: icmp_seq=4 ttl=57 time=1.65 ms^C--- globalcdndynamic.qiniu.com.w.kunlungr.com ping statistics ---4 packets transmitted, 4 received, 0% packet loss, time 3004msrtt min/avg/max/mdev = 1.652/1.687/1.711/0.023 ms

**客户**：使用咱们的qshell工具测试了下，查询区域错误？：2024/10/28 20:09:39.788 [D]  form upload:testdir/a.txt => [roodea001:a.txt]2024/10/28 20:09:39.789 [D]  upload token:E-TKGw5t***:3fx1gWaF***=:eyJzY29w***/10/28 20:09:39.951 [D]  upload:   end upload:testdir/a.txt => [roodea001:a.txt] error:form upload => query region error, errorMsg: address forbidden,address=uc.qbox.me:802024/10/28 20:09:39.951 [E]  Upload  failed:testdir/a.txt => [roodea001:a.txt] error:upload source => form upload => query region error, errorMsg: address forbidden,address=uc.qbox.me:802024/10/28 20:09:39.951 [E]  Upload Failed, a.txt       4       17301167608636478 error:upload source => form upload => query region error, errorMsg: address forbidden,address=uc.qbox.me:802024/10/28 20:09:39.951 [D]  work consumer 0   end2024/10/28 20:09:39.951 [D]  work flow did end2024/10/28 20:09:39.951 [I]  job dir:/root/.qshell/users/roodea/qupload2/33940377***, there is a cache related to this command in this folder, which will also be used next time the same command is executed. If you are sure that you don’t need it, you can delete this folder.2024/10/28 20:09:39.951 [D]  save download result to path:/root/.qshell/users/roodea/qupload2/33940377***/.result2024/10/28 20:09:39.951 [I]  --------------- Upload Result ---------------2024/10/28 20:09:39.951 [I]                Total:         12024/10/28 20:09:39.951 [I]              Success:         02024/10/28 20:09:39.951 [I]              Failure:         12024/10/28 20:09:39.951 [I]            Overwrite:         02024/10/28 20:09:39.951 [I]         NotOverwrite:         02024/10/28 20:09:39.951 [I]              Skipped:         02024/10/28 20:09:39.951 [I]             Duration:         0s2024/10/28 20:09:39.951 [I]  ---------------------------------------------

**客服**：您好，这个报错是网络异常导致的，你们试试将dns指向8.8.8.8 试试，看看是否可以呢

---

## 配置超时

**问题分类**: CDN｜配置问题

### 问题描述

修改 HTTPS 配置处理中，通常情况下 8-15 分钟完成，期间域名访问不受影响，部分配置不可修改，若较长时间未配置完成，请提交工单反馈 常见证书问题实际超过3个小时，配置仍然未生效。

### 客服解答

1. 您好，请稍等，这边帮您确认下

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：修改 HTTPS 配置处理中，通常情况下 8-15 分钟完成，期间域名访问不受影响，部分配置不可修改，若较长时间未配置完成，请提交工单反馈 常见证书问题实际超过3个小时，配置仍然未生效。

**客服**：您好，请稍等，这边帮您确认下

**客户**：感谢

---

## 图片无法打开，时间有7分钟左右

**问题分类**: CDN｜访问下载

### 问题描述

北京时间2024-10-28 15:51 左右，图片无法打开，你们官网的 CDN 模块也无法打开，时间有7分钟左右。这是什么原因？

### 客服解答

1. 您好非常抱歉给您造成不便，经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您清理下客户端dns缓存，稍后再观察看看

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：北京时间2024-10-28 15:51 左右，图片无法打开，你们官网的 CDN 模块也无法打开，时间有7分钟左右。这是什么原因？

**客服**：您好非常抱歉给您造成不便，经确认是由于个别节点网络抖动导致的，异常节点已剔除下线，辛苦您清理下客户端dns缓存，稍后再观察看看

---

## 云主机远程登录密码忘记怎么办

**问题分类**: 云主机｜网络安全

### 问题描述

如题IP 101.132.101.86我们一直用Windows 远程桌面连接登录 因为更换新电脑 但是忘记了 远程登录密码 我该怎么处理

### 客服解答

1. 您好，这个您在 控制台的主机列表 - 操作中，选择重置密码，然后重启主机即可

2. 可以的

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：如题IP 101.132.101.86我们一直用Windows 远程桌面连接登录 因为更换新电脑 但是忘记了 远程登录密码 我该怎么处理

**客服**：您好，这个您在 控制台的主机列表 - 操作中，选择重置密码，然后重启主机即可

**客户**：因为我没有找到控制台在哪里， 在实例里找到 图片所示这里是不是改 我远程桌面连接登录密码？[图片]

**客服**：可以的

---

## 长时间在配置

**问题分类**: CDN｜配置问题

### 问题描述

cdn-www.gdy1234.com长时间在配置

### 客服解答

1. 您好，请稍等

2. 您好，久等了，已处理完成，您确认下

### 根本原因分析

配置参数错误或不当

### 完整对话记录

**客户**：cdn-www.gdy1234.com长时间在配置

**客服**：您好，请稍等

**客服**：您好，久等了，已处理完成，您确认下

---

## 图片基本处理能否支持更大原图尺寸？

**问题分类**: 智能多媒体｜图片处理

### 问题描述

其实这是一个典型的售前问题，但售前客服居然让我开技术工单询问，我也很意外（见附件），问题如下：我们想从阿里oss迁移到七牛，其中会用到图片处理，看到说明文档里有明确原图限制20M。而由于之前阿里给我们的是50M原图限制，所以已经用在生产环境中了。想了解一下，我们需要对象存储的图片在线处理满足50M原图的能力。这个部分能满足吗？如果能满足，那么是在什么条件下可以被满足？还是不可能满足？另，因运营需要，我们无法先通过图片持久化，再使用在线图片处理的方式。

### 客服解答

1. 您好，请稍等，这边帮您确认下

2. 您好，当前图片在线处理，超出20M ，会返回报错image too large ，当前50M的图片只能用异步持久化处理，在线处理的话当前还是不能支持的，已经将您的需求反馈给产研同事们评估的，后期有优化更新排期的话，这边再给您反馈您看下是否可以

3. 好的

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：其实这是一个典型的售前问题，但售前客服居然让我开技术工单询问，我也很意外（见附件），问题如下：我们想从阿里oss迁移到七牛，其中会用到图片处理，看到说明文档里有明确原图限制20M。而由于之前阿里给我们的是50M原图限制，所以已经用在生产环境中了。想了解一下，我们需要对象存储的图片在线处理满足50M原图的能力。这个部分能满足吗？如果能满足，那么是在什么条件下可以被满足？还是不可能满足？另，因运营需要，我们无法先通过图片持久化，再使用在线图片处理的方式。[图片]

**客服**：您好，请稍等，这边帮您确认下

**客服**：您好，当前图片在线处理，超出20M ，会返回报错image too large ，当前50M的图片只能用异步持久化处理，在线处理的话当前还是不能支持的，已经将您的需求反馈给产研同事们评估的，后期有优化更新排期的话，这边再给您反馈您看下是否可以

**客户**：好的，感谢

**客服**：好的

---

## 怎么才能访问这个文件，空间名zhxiaofang

**问题分类**: 对象存储｜其他类咨询

### 问题描述

http://zhxiaofang.cn/***

### 客服解答

1. 您好，您的这个域名没有做cname解析，您确认下呢主机记录是 @

2. 您好，这个你们去配置cname解析，域名在哪里买的，就去哪里配置主机记录 @ , 记录类型 cname ，记录值 zhxiaofang-cn-idvoina.qiniudns.com 可以咨询下您的域名供应商

3. 稍等

4. 您好，麻烦您再访问试下

5. 您好，不客气的

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：http://zhxiaofang.cn/***

**客服**：您好，您的这个域名没有做cname解析，您确认下呢主机记录是 @

**客户**：具体怎么操作，我不太懂

**客服**：您好，这个你们去配置cname解析，域名在哪里买的，就去哪里配置主机记录 @ , 记录类型 cname ，记录值 zhxiaofa***.qiniudns.com 可以咨询下您的域名供应商

**客户**：域名已经配置好了，但是这个地址还是访问不了

**客服**：稍等

**客服**：您好，麻烦您再访问试下

**客户**：可以了，谢谢

**客服**：您好，不客气的

---

## 请帮我删除sbgg空间

**问题分类**: 对象存储｜数据迁移

### 问题描述

因我公司业务调整，需要删除sbgg空间，目前此空间2.7T，总文件数:22818571,如果通过调用删除文件api接口，会非常慢，希望得到帮助。

### 客服解答

1. 您好，删除文件属于高危操作，空间删除后，文件将无法恢复，请您慎重操作。如果您确认需要由我们操作本次空间删除，您可以留下联系方式，这边安排商务经理和您确认下，确认无误后，将由商务经理帮您发起删除申请。

2. 好的，这边商务会尽快与您联系的

3. 好的

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：因我公司业务调整，需要删除sbgg空间，目前此空间2.7T，总文件数:22818571,如果通过调用删除文件api接口，会非常慢，希望得到帮助。

**客服**：您好，删除文件属于高危操作，空间删除后，文件将无法恢复，请您慎重操作。如果您确认需要由我们操作本次空间删除，您可以留下联系方式，这边安排商务经理和您确认下，确认无误后，将由商务经理帮您发起删除申请。

**客户**：确认，无需恢复。我的电话 [REDACTED_PHONE]

**客服**：好的，这边商务会尽快与您联系的

**客户**：商务说已经提交工单，请尽快安排，谢谢

**客服**：好的

**客户**：我这边已经可以删除了，谢谢

---

## 一直处理中

**问题分类**: CDN｜证书问题

### 问题描述

一直在处理中

### 客服解答

1. 您好，请稍等

2. 你好，域名存在海外配置，预计还需要40min处理完成

3. 您好，已中断回滚

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：一直在处理中[图片]

**客服**：您好，请稍等

**客服**：你好，域名存在海外配置，预计还需要40min处理完成

**客户**：还是不行，给中断掉吧 不用https了

**客户**：都4个多小时了，

**客服**：您好，已中断回滚

---

## 主机包月到期没有自动释放

**问题分类**: 云主机｜主机

### 问题描述

实例机器当时只买了一个月，没有开启自动续费，为什么没有自动释放，每个月都扣费。

### 客服解答

1. 您好，这边帮您确认下，请稍等

2. 您好，您在哪里看到这个实例有自动续费的呢2023-12-16 00:00:00这个实例在 23年12月，1个月就已经过期了 ，您当前的费用主要要源自于存储 和  按量计算的公网iphttps://portal.qiniu.com/financial/bills/estimated-consume你们确认下，你们需要将ip 释放 并且 将存储空间文件全部删除后，才不会继续产生计费注意，删除的任何资源都无法恢复

3. 您好，是的，按量的ip，不设置自动释放时间的话，是不会随主机释放的，只有包年包月的ip才会追随主机释放

4. 生命周期只对设置后的增量文件生效，对存量文件不会起效，存量文件需要调用接口或者qshell 工具处理才可以

5. 您好，对存量文件做转换，你们提供一个电话联系方式，这边安排商务与您联系即可

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：实例机器当时只买了一个月，没有开启自动续费，为什么没有自动释放，每个月都扣费。

**客服**：您好，这边帮您确认下，请稍等

**客服**：您好，您在哪里看到这个实例有自动续费的呢2023-12-16 00:00:00这个实例在 23年12月，1个月就已经过期了 ，您当前的费用主要要源自于存储 和  按量计算的公网iphttps://portal.qiniu.com/*** 释放 并且 将存储空间文件全部删除后，才不会继续产生计费注意，删除的任何资源都无法恢复

**客户**：我刚才看到主机还在，不过刷新页面后没有了。ip还计费，ip是不会自动随主机释放的是吗？

**客服**：您好，是的，按量的ip，不设置自动释放时间的话，是不会随主机释放的，只有包年包月的ip才会追随主机释放

**客户**：另外，我对m77-staging设置了生命周期，为什么一直没有转为低频存储。

**客户**：另外一个 m77-prod 也是的，我都设置了生命周期[图片]

**客服**：生命周期只对设置后的增量文件生效，对存量文件不会起效，存量文件需要调用接口或者qshell 工具处理才可以

**客户**：有什么办法对现有文件最快转为深度归档

**客服**：您好，对存量文件做转换，你们提供一个电话联系方式，这边安排商务与您联系即可

---

## 调用发短信接口返回找不到模板id

**问题分类**: 云短信｜短信发送问题

### 问题描述

{"error":"NotFoundError","message":"template(1840665307232874496) not found","request_id":"RP51r1MuprG-oQIY"}

### 客服解答

1. 您好，你们这个是不是设置错了ak sk ，您如果方便的话，方便生成一组测试ak sk 提供给这边么，这边帮您测试核实下

2. 您好，或者您将完整的请求提供下，这边帮您确认下只有 jCciD48kMK0Ba3dxvdU8Aw9JCXjia4Qts7jbA2tG:lsBJ-cr-sxjsb5fyDZMpXaAHUms=这边不支持你们的请求body 的string 是什么的

3. 好的

### 根本原因分析

认证凭证或权限配置问题

### 完整对话记录

**客户**：{"error":"NotFoundError","message":"template(1840665307232874496) not found","request_id":"RP51r1MuprG-oQIY"}

**客户**：调用的是这个接口：https://sms.qiniuapi.com/***

**客服**：您好，你们这个是不是设置错了ak sk ，您如果方便的话，方便生成一组测试ak sk 提供给这边么，这边帮您测试核实下

**客户**：jCciD48k***:lsBJ-cr-***=

**客户**：outData["template_id"] = "1840665307232874496"outData["mobile"] = "[REDACTED_PHONE]"outData["parameters"] = map[string]int{    "code": 123,}

**客服**：您好，或者您将完整的请求提供下，这边帮您确认下只有 jCciD48k***:lsBJ-cr-***=这边不支持你们的请求body 的string 是什么的

**客户**：import "github.com/qiniu/api.v7/v7/auth"url := "https://sms.qiniuapi.com/***"outData := utils.NewMap()outData["template_id"] = "1840665307232874496"outData["mobile"] = "[REDACTED_PHONE]"outData["parameters"] = map[string]int{    "code": 123,}body := outDatareqData, _ := jsoniter.Marshal(body)req, reqErr := http.NewRequest("POST", url, bytes.NewReader(reqData))if reqErr != nil {    log.Errorf("内容检测失败:%v", reqErr)}req.Header.Add("Content-Type", "sms.qiniuapi.com")req.Header.Add("Host", "application/json")mac := auth.New(config.Conf.QiNiuYun.AccessKey, config.Conf.QiNiuYun.SecretKey)qiniuToken, signErr := mac.SignRequestV2(req)if signErr != nil {    panic(signErr)}req.Header.Add("Authorization", "Qiniu "+qiniuToken)resp, respErr := http.DefaultClient.Do(req)if respErr != nil {    panic(respErr)}defer resp.Body.Close()resData, ioErr := io.ReadAll(resp.Body)if ioErr != nil {    panic(ioErr)}fmt.Println(string(resData))

**客户**：log.Errorf的这段代码不用在意，复制过来没删除的

**客户**：上面那有两段代码复制错了req.Header.Add("Content-Type", "application/json")req.Header.Add("Host", "sms.qiniuapi.com")这个才是对的具体为什么提示下面的信息就不知道了{"error":"NotFoundError","message":"template(1840665307232874496) not found","request_id":"RP51rwBTbpWzowIY"}

**客户**：可以了，id写错了，因为填写了使用签名那一行括号里的id，实际上要填写的是下面不显眼的那一行id

**客服**：好的

---

## 我域名绑定服务器正常为什么解析到你这边就提示反诈了

**问题分类**: CDN｜访问下载

### 问题描述

1

### 客服解答

1. 请稍等

2. 您好，你们绑定在七牛的是 qn.0454.wang ，你们要用这个域名去访问

3. qn 域名测试是没有问题的，访问正常，你们如果有问题，看下你们qn 这个主机记录是不是设置了多个解析，将 qn 无关记录的解析删除qiniu.0454.wang 这个域名与七牛无关，没在七牛绑定[图片]

4. 您好，你们看下回复https://qiniu.8687.wang/  这个域名不在七牛，与七牛无关的

5. 您好，访问正常[图片]

6. 您好，具体是哪个区域无法打开呢，清理下客户端DNS缓存试试呢

7. 这边代理江苏测试下，有结论再给您反馈

8. 您好，这边当前没有复现，如果您这边还有提示，麻烦您将访问到的节点提供下，浏览器F12给下对应响应节点和 报错截图

9. 您好，这个有可能是运营商检查备案信息导致的，当前可以访问即可

10. 好的，您不用谢的

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：1

**客户**：只要CNAME记录就提示反诈

**客户**：所有应用都无法安装了 是不是域名问题呢

**客户**：帮我看看啊

**客服**：请稍等

**客服**：您好，你们绑定在七牛的是 qn.0454.wang ，你们要用这个域名去访问

**客户**：我反诈拦截了哦，还有我现在用的qiniu.8687.wang在平台所有应用都无法安装

**客户**：帮我看看什么情况吧

**客户**：还有qn.0454.wang这个域名 我PING还是我服务器IP

**客户**：CNAME 还没生效吗

**客户**：https://qiniu.8687.wang/ 绑定的这个现在打开是无法访问网站

**客服**：qn 域名测试是没有问题的，访问正常，你们如果有问题，看下你们qn 这个主机记录是不是设置了多个解析，将 qn 无关记录的解析删除qiniu.0454.wang 这个域名与七牛无关，没在七牛绑定[图片]

**客户**：https://qiniu.8687.wang/ 这个呢 现在用这个是无法访问

**客服**：您好，你们看下回复https://qiniu.8687.wang/  这个域名不在七牛，与七牛无关的

**客服**：您好，访问正常[图片]

**客户**：很多人反映是无法打开 是不是地区屏蔽了呢

**客服**：您好，具体是哪个区域无法打开呢，清理下客户端DNS缓存试试呢

**客户**：江苏地区

**客户**：刚刚用户反映大多数都不行

**客服**：这边代理江苏测试下，有结论再给您反馈

**客户**：现在是啥情况 主要是我在服务器没提示反诈 解析到你这边后就提示

**客服**：您好，这边当前没有复现，如果您这边还有提示，麻烦您将访问到的节点提供下，浏览器F12给下对应响应节点和 报错截图

**客户**：好奇怪啊 我现在加的所有域名都不拦截了 刚刚全部都在拦截

**客户**：真的太奇怪了 之前的全部都在拦截 现在全好了

**客服**：您好，这个有可能是运营商检查备案信息导致的，当前可以访问即可

**客户**：好的谢啦 辛苦了

**客服**：好的，您不用谢的

---

## 域名更新不成功

**问题分类**: CDN｜证书问题

### 问题描述

few-update.ubnt.com 证书即将到期，证书更新显示一直在处理中

### 客服解答

1. 您好，久等，已处理完成

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：few-update.ubnt.com 证书即将到期，证书更新显示一直在处理中

**客服**：您好，久等，已处理完成

---

## 网段怎么设置格式 [REDACTED_PRIVATE_IP]-[REDACTED_PRIVATE_IP] 这样吗

**问题分类**: CDN｜访问下载

### 问题描述

网段怎么设置格式 [REDACTED_PRIVATE_IP]-[REDACTED_PRIVATE_IP] 这样吗 网段怎么设置格式 [REDACTED_PRIVATE_IP],[REDACTED_PRIVATE_IP] 这样吗 也不对

### 客服解答

1. 网段限制最后两段，是 设置 /16[REDACTED_PRIVATE_IP]/16 表示 192.168.xxx.xxx 全网段

2. 1：是的2：[REDACTED_PRIVATE_IP]/24 网段设置，你们可以百度下子网掩码规则即可

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：网段怎么设置格式 [REDACTED_PRIVATE_IP]-[REDACTED_PRIVATE_IP] 这样吗 网段怎么设置格式 [REDACTED_PRIVATE_IP],[REDACTED_PRIVATE_IP] 这样吗 也不对

**客服**：网段限制最后两段，是 设置 /16[REDACTED_PRIVATE_IP]/16 表示 192.168.xxx.xxx 全网段

**客户**：要限制[REDACTED_PRIVATE_IP]到[REDACTED_PRIVATE_IP] 这整个一段就是设置为  [REDACTED_PRIVATE_IP]/16 即可对吧如果限制[REDACTED_PRIVATE_IP]到[REDACTED_PRIVATE_IP] 这段呢

**客服**：1：是的2：[REDACTED_PRIVATE_IP]/24 网段设置，你们可以百度下子网掩码规则即可

---

## 账号注销

**问题分类**: 账户与财务｜账户问题

### 问题描述

不想用了

### 客服解答

1. 您好，目前注销可以在控制台操作https://portal.qiniu.com/developer/user/security目前用户自助注销需满足以下所有条件：1、账号为普通账号（非财务父子账号、OEM账号）2、账号下实时消费无产品用量、无消费金额（数据需要您自己删除）对象存储：https://portal.qiniu.com/kodo/bucketCDN：https://portal.qiniu.com/cdn/domain3、账号下无各种欠费实时消费明细（查看您当月消费）https://portal.qiniu.com/financial/bills/estimated-consume如有欠费，将在下月5号出账、8号扣款，结算后，您再提交账号注销。4、账号下没有正在处理的提现审批https://portal.qiniu.com/financial/withdraw5、账号当前没有被冻结注意：账号注销后，账号无法找回

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：不想用了

**客服**：您好，目前注销可以在控制台操作https://portal.qiniu.com/***

---

## 命中率极低是什么情况？

**问题分类**: CDN｜刷新缓存问题

### 问题描述

ereakvipok9ba.playwoool.com发现这个域名的CDN命中率极低，才12%。见截图，帮我看下是怎么回事？

### 客服解答

1. 您好，请稍等，这边帮您确认下

2. 您好，你们这个域名加载的资源是不是主要是加载的冷资源或者新文件呢，是不是每个视频文件一般只播放1-2次呢，这种冷 新文件第一次访问一定没有缓存的，会导致流量命中率极低的

3. 您好，这边再帮您检查下，请稍等

4. 您好，这边还在帮您确认中，有结论再给您反馈

5. 您好，这边帮您优化了下，您明天再观察下，看下是否可以，如果还是比较低的话，可以建议使用源站域名，源站域名不使用加速，没有缓存

### 根本原因分析

配置参数错误或不当

### 完整对话记录

**客户**：ereakvipok9ba.playwoool.com发现这个域名的CDN命中率极低，才12%。见截图，帮我看下是怎么回事？[图片]

**客服**：您好，请稍等，这边帮您确认下

**客服**：您好，你们这个域名加载的资源是不是主要是加载的冷资源或者新文件呢，是不是每个视频文件一般只播放1-2次呢，这种冷 新文件第一次访问一定没有缓存的，会导致流量命中率极低的

**客户**：不是的，目前资源都是老资源为主。而且每个视频也是很多次很多客户访问。就是我也是忽略了参数的，资源每次访问会有鉴权参数。主要命中率12%实在太低了。

**客服**：您好，这边再帮您检查下，请稍等

**客服**：您好，这边还在帮您确认中，有结论再给您反馈

**客服**：您好，这边帮您优化了下，您明天再观察下，看下是否可以，如果还是比较低的话，可以建议使用源站域名，源站域名不使用加速，没有缓存

---

## https降级

**问题分类**: CDN｜配置问题

### 问题描述

记得你们家有10G免费流量来着

### 客服解答

1. 您好，请稍等

2. 您好，已帮您完成降级，您确认下

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：记得你们家有10G免费流量来着

**客服**：您好，请稍等

**客服**：您好，已帮您完成降级，您确认下

---

## 为什么我不能申请胡志明地区的对象存储

**问题分类**: 对象存储｜其他类咨询

### 问题描述

我想新建一个胡志明的存储，提示要申请

### 客服解答

1. 您好，您这边具体是有什么需求需要开通这个区域呢，直接使用东南亚空间可以吗

2. 您好，麻烦留一下您的联系方式，由商务同事跟进对接，协助您开通。

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：我想新建一个胡志明的存储，提示要申请

**客服**：您好，您这边具体是有什么需求需要开通这个区域呢，直接使用东南亚空间可以吗

**客户**：因为我现在就在胡志明，用胡志明的更快

**客服**：您好，麻烦留一下您的联系方式，由商务同事跟进对接，协助您开通。

---

## 申请存量数据批量修改智能存储服务

**问题分类**: 对象存储｜上传下载

### 问题描述

已设置生命周期，希望可以申请文档中所说的 “使用生命周期将已存在的数据批量从标准存储或低频存储转换到智能分层存储”相关文档：https://developer.qiniu.com/***

### 客服解答

1. 您好，您这边可以使用qhsell工具进行批量转存储类型的qshell工具：https://developer.qiniu.com/kodo/1302/qshell#9batchexpire命令：https://github.com/qiniu/qshell/blob/master/docs/batchchtype.md

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：已设置生命周期，希望可以申请文档中所说的 “使用生命周期将已存在的数据批量从标准存储或低频存储转换到智能分层存储”相关文档：https://developer.qiniu.com/***

**客服**：您好，您这边可以使用qhsell工具进行批量转存储类型的qshell工具：https://developer.qiniu.com/***

---

## 使用 vue3 上传文件为什么浏览器控制台提示qiniu.upload is not a function

**问题分类**: 对象存储｜SDK使用

### 问题描述

import * as qiniu from 'qiniu-js'···const observable = qiniu.upload(file, file.name, token, putExtra, config);TypeError: qiniu.upload is not a function
    at handleUpload (index.vue:184:28)

### 客服解答

1. 您好

2. 抱歉这个目前没有

3. 您用的js sdk 是哪个版本的

### 根本原因分析

认证凭证或权限配置问题

### 完整对话记录

**客户**：import * as qiniu from 'qiniu-js'···const observable = qiniu.upload(file, file.name, token, putExtra, config);TypeError: qiniu.upload is not a function
    at handleUpload (index.vue:184:28)

**客户**：// 自定义上传方法const handleUpload = async (options) => {  const { file } = options;  const token = await getUpTokenApi();  if (!token) return;  const config = {    useCdnDomain: true,    region: 'z2', // 华南地区  };  const putExtra = {    fname: file.name,    params: {},    mimeType: null,  };  const observable = qiniu.upload(file, file.name, token, putExtra, config);  observable.subscribe({    next(res) {      // 上传进度      console.log('progress:', res.total.percent);    },    error(err) {      // 上传失败      ElMessage.error('上传失败');    },    complete(res) {      // 上传成功      ElMessage.success('上传成功');      console.log('response:', res);    },  });};

**客服**：您好
可以参考这个demo重试下
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>进度条属性上传</title>
</head>
<body>
    <form method="post" enctype="multipart/form-data">
      <input name="key"  type="hidden" value=""/>
      <input name="token"  type="hidden" value=""/>
      <input name="accept" type="hidden" />
      <input id="input-file" class="upload" type="file" value="" onchange="getPhoto(this)">
         <br/>
         <span class="img"> </span>
<div id="totalBar" style="float:left;width:20%;height:30px;border:1px solid;border-radius:3px">
            <div id="totalBarColor" style="width:0%;border:0;background:#FFFE33; color: #FFF;height:28px;"></div>
            <span class="speed"></span>
         </div>
<br/>
         <BR/>
      <input type="button" value="上传" onclick="upload()"/>
      <input type="button" value="暂停" onclick="filepause()"/>
    </form>
     <script src="https://code.jquery.com/***"></script>
     <script src="https://unpkg.com/***"></script>
<script>
                    var subObject;
                    var file;
                    //定义上传配置，注意上传域名的设置，华东空间z0,华南z2，华北z1
                    var config = {
                      region: qiniu.region.z2
                    };
var putExtra = {
};
var compareChunks = [];
                    var observable;
                    var subscription;
function getPhoto(node) {
                        var imgURL = "";
                        try{
                            file = null;
                            if(node.files && node.files[0] ){
                                file = node.files[0];
                            }else if(node.files && node.files.item(0)) {
                                file = node.files.item(0);
                            }
                        }catch(e){
}
                        creatImg(imgURL,file.name);
                        return imgURL;
                    }
function creatImg(imgRUL,fileName){
                        $("input[name=key]").val(fileName);
                        //var textHtml = "<img src='"+imgRUL+"'width='40px' height='40px'/>";
                        //$(".img").html(textHtml);
                        $("#totalBarColor").css("width","0%");
                    }
function upload() {
                            // 设置next,error,complete对应的操作，分别处理相应的进度信息，错误信息，以及完成后的操作
                        subObject = {
                              next: next,
                              error: error,
                              complete: complete
                        };
                        token = "设置你们的上传token"
                        //上传
                        observable = qiniu.upload(file, file.name, token, putExtra, config);
                        // 调用sdk上传接口获得相应的observable，控制上传和暂停
                        subscription = observable.subscribe(subObject);
                    }
function filepause(){
                       subscription.unsubscribe();
                    }
//分片上传返回response，标记上传进度
                    var next = function(response) {
                       var chunks = response.chunks||[];
                       var total = response.total;
                       $(".speed").text("进度：" + total.percent + "% ");
                       $("#totalBarColor")
                           .css(
                                "width",
                                 total.percent + "%"
                       );
                       compareChunks = chunks;
                     };
var error = function(err) {
                           alert(err.message);
                     };
var complete = function(res) {
                         console.log(res);
                         console.log(res.key);
};
            </script>
</body>
</html>

**客户**：有没有vue3的demo

**客服**：抱歉这个目前没有

**客户**：那你们那个sdk的demo有吗

**客户**：照着你的文档来还提示错误

**客户**：import * as qiniu from 'qiniu-js'···const observable = qiniu.upload(file, file.name, token, putExtra, config);主要是确认一下这里哪里有问题

**客服**：您用的js sdk 是哪个版本的

---

## 免费 from 自动催单

**问题分类**: CDN｜证书问题

### 问题描述

长时间处于域名发布环节

### 客服解答

1. 您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：长时间处于域名发布环节

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

---

## 摄像头全不在线？

**问题分类**: 视频监控｜业务咨询

### 问题描述

空间ID    PeanetProd摄像头全不在线

### 客服解答

1. 您好，请稍等，这边帮您确认下

2. 您好目前已经反馈产研侧确认中 有结论这边答复您 辛苦耐心等待

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：空间ID    PeanetProd摄像头全不在线

**客服**：您好，请稍等，这边帮您确认下

**客户**：你好，有确认到问题吗？这边应急监控用，挺着急的

**客服**：您好目前已经反馈产研侧确认中 有结论这边答复您 辛苦耐心等待

**客户**：我这边看已经恢复正常了。。。

---

## QVS摄像头全显示离线，包括无线网卡链接以及网线连接

**问题分类**: 视频监控｜控制台使用

### 问题描述

QVS摄像头全显示离线，包括无线网卡链接以及网线连接，加急！！！！

### 客服解答

1. 您好，请稍等，这边帮您核实确认中

2. 您好，您目前现在是否正常

3. 您好，很抱歉具体原因目前正在核实，您稍等下

4. 您好，这边核实原因，是因为迁移过程中，缓存和mongo数据不一致，触发了设备状态校验，校验数据失败时，状态就变成离线了

5. 您好，很抱歉，核实目前给到的结果是明天迁移完成您的问题这边在反馈下

6. 您好，您查看下目前是否已经恢复

7. 您好，重启下设备看下

8. 您好，如果没法重启的话，需要等待下等设备重新注册，变成非jjh就可以

9. 您好，请稍等

10. 您好，当前已经可以，您重启设备重新上线看看呢

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：QVS摄像头全显示离线，包括无线网卡链接以及网线连接，加急！！！！

**客服**：您好，请稍等，这边帮您核实确认中

**客服**：您好，您目前现在是否正常

**客户**：确认完了吗

**客户**：什么原因造成的  现在基本都在线了

**客户**：明天 省领导来开现场会 不会再出现这种问题了吧

**客服**：您好，很抱歉具体原因目前正在核实，您稍等下

**客服**：您好，这边核实原因，是因为迁移过程中，缓存和mongo数据不一致，触发了设备状态校验，校验数据失败时，状态就变成离线了

**客户**：什么时候能迁移完事，什么时候能解决或者怎么才能解决。现在七牛特别不稳定，我们之前一点问题都没有的摄像头拉流都拉不下来，或者是显示在线，但是拉不下来视频流，我们排查了网络及电源都没有问题。而且注册摄像头非常慢，好几个小时才能对接上。明天我这有省领导来检查，这个严重影响了我们的业务，先给解决一下！！！

**客服**：您好，很抱歉，核实目前给到的结果是明天迁移完成您的问题这边在反馈下

**客服**：您好，您查看下目前是否已经恢复

**客户**：现在页面特别慢，而且拉流拉不下来，设备显示在线拉流时却提示离线，先给我这个问题解决一下呗，尤其明天上午，有省领导要看的现场会，务必别让明天上午的使用出现问题

**客服**：您好，重启下设备看下

**客户**：我的摄像头都分布在不同地方 没办法都重启一遍

**客服**：您好，如果没法重启的话，需要等待下等设备重新注册，变成非jjh就可以

**客户**：31011500991320060350  重启设备还是不再线

**客户**：中午还好用

**客服**：您好，请稍等

**客服**：您好，当前已经可以，您重启设备重新上线看看呢

---

## 免费 from 自动催单

**问题分类**: CDN｜证书问题

### 问题描述

长时间处于域名检测环节

### 客服解答

1. [图片]

2. 您好，这边手动介入下处理，麻烦稍等。

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：长时间处于域名检测环节

**客服**：[图片]

**客服**：您好，这边手动介入下处理，麻烦稍等。

---

## 免费 from 自动催单

**问题分类**: CDN｜证书问题

### 问题描述

长时间处于免费证书申请环节

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：长时间处于免费证书申请环节

**客户**：怎么进度条一直没动 能加速处理一下吗 项目在运行当中

---

## https一直在审核中

**问题分类**: CDN｜配置问题

### 问题描述

media.yuanchuangtj.cn 已经配置了ssl证书但在cname配置时一直处于审核状态

### 客服解答

1. 您好，这边手动介入下处理，麻烦稍等。

2. 您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：media.yuanchuangtj.cn 已经配置了ssl证书但在cname配置时一直处于审核状态

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

**客户**：谢谢， 已经确认OK

---

## 域名所有权验证

**问题分类**: CDN｜访问下载

### 问题描述

验证不了，加不了域名

### 客服解答

1. 您好，您目前解析配置是如何配置的

2. 您好，主机记录修改成这个[图片]

3. 您好，好像没有看见[图片]

4. 您好，主机记录不对，记录值也不对了，之前的配置，只需要修改红框内的主机记录为verification[图片]

### 根本原因分析

配置参数错误或不当

### 完整对话记录

**客户**：验证不了，加不了域名

**客服**：您好，您目前解析配置是如何配置的

**客户**：[图片]您看看是哪里不对吗[图片]

**客户**：是以前的域名不行了，我换一个域名，我解析了一个qiniuyun.yilongyl.com

**客服**：您好，主机记录修改成这个[图片]

**客户**：好，改了要等一会才行吗

**客服**：您好，好像没有看见[图片]

**客户**：我改了，图片传不了

**客户**：你看看哪里不对，我在改[图片]

**客户**：我看到了哪里问题了

**客服**：您好，主机记录不对，记录值也不对了，之前的配置，只需要修改红框内的主机记录为verification[图片]

---

## 视频无法播放

**问题分类**: 对象存储｜其他类咨询

### 问题描述

http://sljkkiilc.hd-bkt.clouddn.com/***

### 客服解答

1. 您好测试域名会忽略参数缓存 修改为私有空间访问试下

### 根本原因分析

认证凭证或权限配置问题

### 完整对话记录

**客户**：http://sljkkiilc.hd-bkt.clouddn.com/***

**客服**：您好测试域名会忽略参数缓存 修改为私有空间访问试下

---

## 抖音小程序中无法播放视频

**问题分类**: 对象存储｜其他类咨询

### 问题描述

已按抖音的要求配置了refer的白名单：tmaservice.developer.toutiao.com，抖音那边还无法播放我的resource.baixing.com下面的视频，返回403，请问为什么，昨天设置的。早已经超过1个小时。

### 客服解答

1. 您好播放的视频链接是什么 这边测试下

2. referer防盗链要到cdn侧配置 您配置的是存储空间的referer 把这个关闭一下

3. [图片]

4. 访问在cdn侧配置referer 存储的referer关闭掉

### 根本原因分析

配置参数错误或不当

### 完整对话记录

**客户**：已按抖音的要求配置了refer的白名单：tmaservice.developer.toutiao.com，抖音那边还无法播放我的resource.baixing.com下面的视频，返回403，请问为什么，昨天设置的。早已经超过1个小时。

**客服**：您好播放的视频链接是什么 这边测试下

**客户**：http://resource.baixing.net/***

**客户**：请问我是不是只在这里设置就用可以呢？[图片]

**客户**：还有其他设置的地方吗？

**客服**：referer防盗链要到cdn侧配置 您配置的是存储空间的referer 把这个关闭一下

**客户**：请问cdn侧的配置在哪里？

**客服**：[图片]

**客户**：存储段的是其他人设置的我不敢关，请问如何在cdn上加上refer   存储上也加 可以吗？

**客服**：访问在cdn侧配置referer 存储的referer关闭掉

---

## 充值没有到账

**问题分类**: 账户与财务｜账户问题

### 问题描述

充值没有到账

### 客服解答

1. 您好，您稍等这边帮您反馈一下

2. 您好，核实充值已到账，您确认下呢，谢谢

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：充值没有到账[图片]

**客服**：您好，您稍等这边帮您反馈一下

**客服**：您好，核实充值已到账，您确认下呢，谢谢

---

## 配置错误了

**问题分类**: CDN｜配置问题

### 问题描述

麻烦帮我拒绝一下审核

### 客服解答

1. 您好，已经回滚处理

2. 已经处理完成

### 根本原因分析

配置参数错误或不当

### 完整对话记录

**客户**：麻烦帮我拒绝一下审核

**客服**：您好，已经回滚处理

**客户**：你好部署不了

**客户**：这个提示不能部署[图片]

**客户**：能帮我配置部署下吗

**客服**：已经处理完成

**客户**：好的谢谢

---

## 我的域名homepage.91mp.com一直处于处理中，无法进行任何操作是怎么回事？

**问题分类**: CDN｜证书问题

### 问题描述

我的域名homepage.91mp.com一直处于处理中，无法进行任何操作是怎么回事？已经很多天了

### 客服解答

1. 您好，这边手动介入下处理，麻烦稍等。

2. 您好，抱歉让您久等了，已经处理完成，您确认下。

3. 您好，免费证书无法续费的，只能重新申请免费证书进行使用的，您这边重新申请一下新的免费证书使用即可的

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：我的域名homepage.91mp.com一直处于处理中，无法进行任何操作是怎么回事？已经很多天了

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

**客户**：homepage.91mp.com显示证书已过期，却无法续费操作，是怎么回事

**客服**：您好，免费证书无法续费的，只能重新申请免费证书进行使用的，您这边重新申请一下新的免费证书使用即可的

---

## 申请陕西oss

**问题分类**: 对象存储｜其他类咨询

### 问题描述

尚有申请正在审核中，无需重复申请。一直在审核，没反应，请协助处理一下。

### 客服解答

1. 您好，十分抱歉给您带来的不便。目前该区域还暂未正式上线，目前是在收集需求的，后续上线后您这边再申请看下的

2. 您好，存储区域创建后不支持修改地区的，这个没有什么影响的，都可以使用的

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：尚有申请正在审核中，无需重复申请。一直在审核，没反应，请协助处理一下。

**客服**：您好，十分抱歉给您带来的不便。目前该区域还暂未正式上线，目前是在收集需求的，后续上线后您这边再申请看下的

**客户**：那我现在在别的地区，创建的oss，后续可以转区吗

**客服**：您好，存储区域创建后不支持修改地区的，这个没有什么影响的，都可以使用的

---

## 验证码短信一直显示待发送状态

**问题分类**: 云短信｜短信发送问题

### 问题描述

您好，请问一下这几个任务ID的短信发送状态一直显示待发送是什么原因？

### 客服解答

1. 您好，稍等下，这边核实看下

2. 您好，目前看是不是都已经发送成功了？

3. 您好，任务id是前面这部分，可以复制几个过来吗[图片]

4. 您好，稍等下，这边核实下

5. 您好核实是下发时手机终端信号问题导致的

6. 没事的的，有什么问题您再反馈

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：您好，请问一下这几个任务ID的短信发送状态一直显示待发送是什么原因？[图片]

**客服**：您好，稍等下，这边核实看下

**客服**：您好，目前看是不是都已经发送成功了？

**客户**：是的，现在已经发送成功了，请问刚刚一直未发送是什么原因导致的呢？

**客服**：您好，任务id是前面这部分，可以复制几个过来吗[图片]

**客户**：好的，1851081544546922496、1851077417930604544、1851076606580240384、1851076105901977601这四个

**客服**：您好，稍等下，这边核实下

**客服**：您好核实是下发时手机终端信号问题导致的

**客户**：好的，谢谢~

**客服**：没事的的，有什么问题您再反馈

---

## 降级https协议为http

**问题分类**: CDN｜配置问题

### 问题描述

不再用证书,降级https协议为http

### 客服解答

1. 您好，很抱歉，月底无法操作降级，您可以等到5号再来操作

2. 您好，好的

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：不再用证书,降级https协议为http

**客服**：您好，很抱歉，月底无法操作降级，您可以等到5号再来操作

**客户**：好的。

**客服**：您好，好的

---

## qiniuyun.qingzhouba nxue.com域名绑定的 SSL证书即将过期

**问题分类**: 对象存储｜其他类咨询

### 问题描述

qiniuyun.qingzhouba nxue.com域名绑定的 SSL证书即将过期  想续费TrustAsia DV免费域名型可以使用吗

### 客服解答

1. 您好，是11月22号过期，您可以到11月20号再来进行操作

2. 您好，您可以在 [域名管理] 中，点击您想要配置https的域名右侧的 [配置] 按钮，在新的页面中，在 [https配置] 下点击 [修改配置] ,点击开启->免费证书→勾选 [同意七牛云代申请免费证书] →确认，之后输入您账号的密码即可。一键https使用的是免费证书，配置一键 https 需要注意：配置生效时间主要是用于等待 CA 机构签发证书，证书一旦签发会在 10 分钟内部署完成，整体一键 https 预计可在 2 小时内完成。期间您不要操作 ssl 证书服务，否则可能造成证书签发失败。免费证书只支持绑定单个普通域名，若您需要使用一级域名的免费证书，请到购买证书页购买免费证书开启了以下功能会导致代理验证失败，无法代理申请证书： 回源鉴权、时间戳防盗链、IP 黑白名单、referer 防盗链当前加速域名需要 CNAME 到七牛给您分配的 CNAME 域名 当前加速域名的 DNS 记录中不能有 CAA 记录，或者 CAA 记录包含 Digicert.com 和 digicert.com免费证书有效期为一年，过期请重新申请需要授权七牛云代申请免费证书注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：qiniuyun.qingzhouba nxue.com域名绑定的 SSL证书即将过期  想续费TrustAsia DV免费域名型可以使用吗

**客服**：您好，是11月22号过期，您可以到11月20号再来进行操作

**客服**：您好，您可以在 [域名管理] 中，点击您想要配置https的域名右侧的 [配置] 按钮，在新的页面中，在 [https配置] 下点击 [修改配置] ,点击开启->免费证书→勾选 [同意七牛云代申请免费证书] →确认，之后输入您账号的密码即可。一键https使用的是免费证书，配置一键 https 需要注意：配置生效时间主要是用于等待 CA 机构签发证书，证书一旦签发会在 10 分钟内部署完成，整体一键 https 预计可在 2 小时内完成。期间您不要操作 ssl 证书服务，否则可能造成证书签发失败。免费证书只支持绑定单个普通域名，若您需要使用一级域名的免费证书，请到购买证书页购买免费证书开启了以下功能会导致代理验证失败，无法代理申请证书： 回源鉴权、时间戳防盗链、IP 黑白名单、referer 防盗链当前加速域名需要 CNAME 到七牛给您分配的 CNAME 域名 当前加速域名的 DNS 记录中不能有 CAA 记录，或者 CAA 记录包含 Digicert.com 和 digicert.com免费证书有效期为一年，过期请重新申请需要授权七牛云代申请免费证书注意事项升级https后，流量计费说明：https://developer.qiniu.com/***]

---

## SSL证书提前更新

**问题分类**: CDN｜访问下载

### 问题描述

SSL证书提前更新，如何更新？

### 客服解答

1. 您好手动选择一下您要选择的新证书 然后提交配置就可以

2. 申请新证书时在签发后手动部署到cdn 更新证书

3. 证书没选择对 在图示的地方更换证书[图片]

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：SSL证书提前更新，如何更新？[图片]

**客户**：新的已上传，为什么不能部署

**客服**：您好手动选择一下您要选择的新证书 然后提交配置就可以

**客户**：是不是每次不用重新上传，直接学费就行如何提交配置

**客服**：申请新证书时在签发后手动部署到cdn 更新证书

**客户**：为什么新的点击部署，部署日期还是不对呢？

**客服**：证书没选择对 在图示的地方更换证书[图片]

---

## 免费 from 自动催单

**问题分类**: CDN｜证书问题

### 问题描述

长时间处于免费证书申请环节

### 客服解答

1. 您好您的证书没有做验证配置，验证通过才能签发证书『待确认』是需要您点击详情，然后根据提示进行文件或者 DNS TXT 验证，系统会自动轮询，轮询通过才会颁发证书参考文档：https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

2. 需要验证才可以签发证书

3. 申请证书的域名

4. 都可以

5. 不是 申请证书时 系统会分配主机记录 记录值 根据我们分配的内容去配置

6. 手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide4.升级HTTPS配置https://developer.qiniu.com/fusion/manual/4952/https-configuration

7. 您截图的处理步骤 跟上述发的手动申请步骤是一样的  按照2024-10-29 10:52:45回复的步骤申请

8. 不要用系统那个代申请的方式 手动去申请 选择dns验证方式

9. 已经回滚

10. 好的

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：长时间处于免费证书申请环节

**客服**：您好您的证书没有做验证配置，验证通过才能签发证书『待确认』是需要您点击详情，然后根据提示进行文件或者 DNS TXT 验证，系统会自动轮询，轮询通过才会颁发证书参考文档：https://developer.qiniu.com/***]

**客户**：我记得之前的免费证书不是点击申请就可以了吗？现在需要怎么验证？[图片]

**客服**：需要验证才可以签发证书

**客户**：还有你说的验证是哪个域名需要验证？

**客服**：申请证书的域名

**客户**：你们的免费证书是哪个机构的？我应该用txt还是cname

**客服**：都可以

**客户**：[图片]这个值是固定的是吧？我只需要换下域名

**客服**：不是 申请证书时 系统会分配主机记录 记录值 根据我们分配的内容去配置

**客户**：那主机记录和记录值在哪获取啊

**客服**：手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/***

**客户**：[图片]我现在走的这个 还需要手动申请证书再验证？然后上传证书？

**客服**：您截图的处理步骤 跟上述发的手动申请步骤是一样的  按照2024-10-29 10:52:45回复的步骤申请

**客户**：[图片]你们代申请的是文件验证  这个怎么关了 我还是自己去申请吧

**客服**：不要用系统那个代申请的方式 手动去申请 选择dns验证方式

**客户**：[图片]这个怎么让它停下来

**客户**：这个卡着我干不了别的

**客服**：已经回滚

**客户**：ok

**客服**：好的

---

## 图片在国外打不开

**问题分类**: 对象存储｜其他类咨询

### 问题描述

https://static-hyq.haoyunqi.com.cn/*** 。这个链接地址在国内可以打开，在境外之前是可以打开的，从上周开始打不开了。

### 客服解答

1. 您好，您这边需要海外访问的话需要将CDN域名的覆盖范围切换到海外或者全球的，目前覆盖范围是国内，海外访问国内节点的话会超时和访问慢的，您这边可以到CDN-域名管理-域名详情下修改一下域名覆盖范围

2. 您好，会增加海外访问的流量计费的，海外访问的会计费海外区域，原来是海外访问国内节点计费国内区域的，费用您这边可以使用后后续观察一下的

3. 您好，不会影响业务访问，只是海外用户访问走海外节点，资源包不能通用，需要购买海外资源包使用的，您可以留一下您的联系方式，这边让商务经理与您联系确认一下的

4. 嗯嗯是的，不购买的话是按量计费的

5. 您好，全球是包含海外线路的，海外线路是配置轮询是比较慢的

6. 嗯嗯好的

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：https://static-hyq.haoyunqi.com.cn/*** 。这个链接地址在国内可以打开，在境外之前是可以打开的，从上周开始打不开了。[图片]

**客服**：您好，您这边需要海外访问的话需要将CDN域名的覆盖范围切换到海外或者全球的，目前覆盖范围是国内，海外访问国内节点的话会超时和访问慢的，您这边可以到CDN-域名管理-域名详情下修改一下域名覆盖范围

**客户**：调整到全球之后和之前大陆对比访问速度有区别吗？  还有费用方面有增加吗？[图片]

**客服**：您好，会增加海外访问的流量计费的，海外访问的会计费海外区域，原来是海外访问国内节点计费国内区域的，费用您这边可以使用后后续观察一下的

**客户**：我cdn 只买了国内的套餐，还需要买国外的cdn套餐吗？还是可以直接使用扣费。

**客户**：现在调整cdn到全球之后会影响现有业务的访问吗？

**客服**：您好，不会影响业务访问，只是海外用户访问走海外节点，资源包不能通用，需要购买海外资源包使用的，您可以留一下您的联系方式，这边让商务经理与您联系确认一下的

**客户**：不购买国外cdn也可以使用吧，就按量来计费》？

**客服**：嗯嗯是的，不购买的话是按量计费的

**客户**：为什么设置了全球配置了这么久还没好，都半小时过去了。[图片]

**客户**：现在配置好了

**客服**：您好，全球是包含海外线路的，海外线路是配置轮询是比较慢的

**客户**：好的，了解。

**客服**：嗯嗯好的

---

## 打开速度慢

**问题分类**: 对象存储｜其他类咨询

### 问题描述

http://shipin.nb-ck.com/***   打开速度很慢  放在www.chinamold.com这个网址上

### 客服解答

1. 您好，1、麻烦提供下您的 ip、dns 信息，和cdn节点信息，这边代理测试下可以通过访问这个链接 http://ping.huatuo.qq.com/ 获取本地的 ip 和 dns 信息，在检测域名这边输入下cdn域名，点击提交检测，然后截图通过工单提交给我们[图片]2、建议使用 chrome 浏览器，按照下述文档获取下 remote adress(对端节点ip)，request header(客户端请求头) 以及 response header(服务端响应头)信息，方便我们查询分析问题。https://developer.qiniu.com/fusion/kb/1478/how-to-access-network-in-the-browser-request-information

2. 用谷歌浏览器打开 f12 看下cdn节点是什么 这边看下

3. 这边帮您优化了一下线路 20分钟后您再访问看下

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：http://shipin.nb-ck.com/***   打开速度很慢  放在www.chinamold.com这个网址上

**客服**：您好，1、麻烦提供下您的 ip、dns 信息，和cdn节点信息，这边代理测试下可以通过访问这个链接 http://ping.huatuo.qq.com/ 获取本地的 ip 和 dns 信息，在检测域名这边输入下cdn域名，点击提交检测，然后截图通过工单提交给我们[图片]2、建议使用 chrome 浏览器，按照下述文档获取下 remote adress(对端节点ip)，request header(客户端请求头) 以及 response header(服务端响应头)信息，方便我们查询分析问题。https://developer.qiniu.com/***

**客户**：1[图片]

**客服**：用谷歌浏览器打开 f12 看下cdn节点是什么 这边看下

**客户**：是不是用海外CDN加速的原因

**客户**：http://shipin.nb-ck.com/***  你可以直接看加载速度就跟不上，是不是因为我这个视频上传太久你们对老视频限流了

**客服**：这边帮您优化了一下线路 20分钟后您再访问看下

---

## 新接入设备显示未注册

**问题分类**: 视频监控｜业务咨询

### 问题描述

如题3101150099132000003931011500991320000033

### 客服解答

1. 您好，这边看这个设备是已经正常的：31011500991320000033这个是有延迟的可以稍后再看下的，如果还是不行的建议您这边重新注册一下的看下

2. 您好，您这边耐心等待一下，这边还在确认中

3. 您好，目前已经反馈产品处理中了，还请耐心等待一下

4. 您好，摄像头设备都是正常开启在线的是吧

5. 您好，嗯嗯您耐心等待一下

6. 您好，这边已经让产品加急了，十分抱歉给您带来的不便，还请耐心等待一下

7. 嗯嗯这边在加急了

8. 十分抱歉，这个目前还没有具体的时间的，这边问下产品看下是否有具体时间

9. 您好，您这边目前再重启一下设备后再看下呢？

10. 嗯嗯好的您稍等

11. 您好，目前已经恢复了，您再看下呢

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：如题3101150099132000003931011500991320000033

**客服**：您好，这边看这个设备是已经正常的：31011500991320000033这个是有延迟的可以稍后再看下的，如果还是不行的建议您这边重新注册一下的看下

**客户**：31011500991320000039，31011500991320000040，31011500991320000041

**客户**：重新注册过了，还是不行。

**客户**：31011500991320000042

**客服**：您好，您这边耐心等待一下，这边还在确认中

**客户**：31011500991320000055、31011500991320000054、31011500991320000053 还是存在问题

**客服**：您好，目前已经反馈产品处理中了，还请耐心等待一下

**客户**：部份设备在线，拉不了流参考ID：31011500***

**客服**：您好，摄像头设备都是正常开启在线的是吧

**客户**：是的

**客户**：正常的

**客服**：您好，嗯嗯您耐心等待一下

**客户**：我都等了2个小时了！！！！

**客服**：您好，这边已经让产品加急了，十分抱歉给您带来的不便，还请耐心等待一下

**客户**：好的 辛苦你们尽快。

**客服**：嗯嗯这边在加急了

**客户**：有大致的修复时间吗？现场师傅还在等！

**客服**：十分抱歉，这个目前还没有具体的时间的，这边问下产品看下是否有具体时间

**客户**：设备在线，拉不了流的问题还没有解决吗？？？

**客服**：您好，您这边目前再重启一下设备后再看下呢？

**客户**：还是不行，现在变成设备也不在线了，但是摄像头设备都是正常开启在线的

**客服**：嗯嗯好的您稍等

**客户**：这个问题今天解决不了吗？？

**客服**：您好，目前已经恢复了，您再看下呢

---

## 部分304部分200

**问题分类**: CDN｜刷新缓存问题

### 问题描述

https://image.vipc.cn/*** 响应304https://image.vipc.cn/*** 200 ，为什么部分的状态是304，304部分可以改为301或者200？

### 客服解答

1. 您好，304状态码不影响的，这个是您的url资源和之前请求的没有变动，未修改的状态码的这个状态码无法修改的，您可以将缓存设置为0这样就请求不到缓存的，但是这样会导致每次请求都会回源，会失去加速效果，而且会导致回源流量增加的

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：https://image.vipc.cn/*** 响应304https://image.vipc.cn/*** 200 ，为什么部分的状态是304，304部分可以改为301或者200？

**客服**：您好，304状态码不影响的，这个是您的url资源和之前请求的没有变动，未修改的状态码的这个状态码无法修改的，您可以将缓存设置为0这样就请求不到缓存的，但是这样会导致每次请求都会回源，会失去加速效果，而且会导致回源流量增加的

**客户**：好的

---

## 视频监控部分设备不正常

**问题分类**: 视频监控｜其他类咨询

### 问题描述

近期在更换SIP服务器，今天上午发现有部分平台设备，显示在线，但对应的摄像头离线，且最后心跳时间及注册时间异常。是否在进行服务器维护操作，需要多久时间才能恢复正常。

### 客服解答

1. 您好，稍等下，这边核实下

2. 您好，目前哪些设备有问题，可以提供下设备id吗，这边查看下

3. 您好，好的，这边同步产品查看下

4. 您好，您查看下目前是否已经恢复

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：近期在更换SIP服务器，今天上午发现有部分平台设备，显示在线，但对应的摄像头离线，且最后心跳时间及注册时间异常。是否在进行服务器维护操作，需要多久时间才能恢复正常。

**客服**：您好，稍等下，这边核实下

**客服**：您好，目前哪些设备有问题，可以提供下设备id吗，这边查看下

**客户**：现在在大部分恢复了

**客户**：31011500991180060866_34020000001320000003这个方便的话看下，有几个摄像头现在正常了，有几个显示在线，但拉流还是不正常。

**客户**：这个设备，之前显示平台设备离线，后来设备显示在线了，但摄像头还是离线，现在是摄像头也都显示在线了，但有部分无法成功拉流。

**客户**：31011500991180057344这台设备上午不正常，目前可以成功拉流，上午更换了SIP服务器，但注册时间并没有更新。之前其它设备更换SIP服务器，都会更新最新注册时间

**客服**：您好，好的，这边同步产品查看下

**客服**：您好，您查看下目前是否已经恢复

---

## 域名所有权验证未通过

**问题分类**: 对象存储｜上传下载

### 问题描述

域名所有权验证未通过

### 客服解答

1. 您好，您的解析配置如何配置的，截图看下呢

### 根本原因分析

配置参数错误或不当

### 完整对话记录

**客户**：域名所有权验证未通过

**客服**：您好，您的解析配置如何配置的，截图看下呢

---

## 密码重置无法设置

**问题分类**: 账户与财务｜账户问题

### 问题描述

密码重置无法设置

### 客服解答

1. 您好，您这个无法设置具体有什么报错呢

### 根本原因分析

账户密码或登录凭证问题

### 完整对话记录

**客户**：密码重置无法设置

**客户**：麻烦尽快处理

**客户**：速度

**客服**：您好，您这个无法设置具体有什么报错呢

---

## 证书配置失败

**问题分类**: CDN｜证书问题

### 问题描述

"title": "日志栈",            "content": "fusionicp:6;fusionsslcert:25/400"

### 客服解答

1. 您好1、建议您在证书厂商下载证书时，选择 Nginx 服务器类型的证书文件2、进入七牛云管理控制台：https://portal.qiniu.com/certificate/ssl，点击 【上传自有证书】3、使用编辑器打开后续文件，并复制 .crt 或者 .pem 后缀的文件内容到证书内容 （公钥），复制 .key 后缀结尾的内容到 证书私钥 。[图片]如果需要把域名升级为 HTTPS 或者修改证书 的话，需要按照以下步骤绑定证书即可：https://developer.qiniu.com/fusion/manual/4952/https-configuration

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**："title": "日志栈",            "content": "fusionicp:6;fusionsslcert:25/400"

**客户**：上传证书失败

**客服**：您好1、建议您在证书厂商下载证书时，选择 Nginx 服务器类型的证书文件2、进入七牛云管理控制台：https://portal.qiniu.com/*** 【上传自有证书】3、使用编辑器打开后续文件，并复制 .crt 或者 .pem 后缀的文件内容到证书内容 （公钥），复制 .key 后缀结尾的内容到 证书私钥 。[图片]如果需要把域名升级为 HTTPS 或者修改证书 的话，需要按照以下步骤绑定证书即可：https://developer.qiniu.com/***

---

## 状态一直在处理中

**问题分类**: CDN｜配置问题

### 问题描述

saas-img.sh-yq.cn状态一直在处理中

### 客服解答

1. 您好已经帮您手动介入处理完成

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：saas-img.sh-yq.cn状态一直在处理中

**客服**：您好已经帮您手动介入处理完成

---

## 有时看到30分钟，又回去了。我们看请求次数比较多。

**问题分类**: CDN｜刷新缓存问题

### 问题描述

有时看到30分钟，又回去了。我们看请求次数比较多。卡顿

### 客服解答

1. 您好，请稍等，这边帮您确认下

2. 您好，这边帮您测试了下，看起来是没有问题的[图片]

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：有时看到30分钟，又回去了。我们看请求次数比较多。卡顿

**客服**：您好，请稍等，这边帮您确认下

**客服**：您好，这边帮您测试了下，看起来是没有问题的[图片]

---

## 烦请开具发票

**问题分类**: 账户与财务｜发票问题

### 问题描述

本次充值，请协助开具发票。发票请发邮箱：[REDACTED_EMAIL]谢谢

### 客服解答

1. 您好，发票开具体麻烦您提供一个联系方式，这边安排商务与你联系

2. 好的

3. 您好，您当前在发票列表中查看下，看下是否已经开具了呢

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：[图片]本次充值，请协助开具发票。发票请发邮箱：[REDACTED_EMAIL]谢谢

**客服**：您好，发票开具体麻烦您提供一个联系方式，这边安排商务与你联系

**客户**：开票信息如下：-------------开票信息-----------开票金额: 150元发票抬头: 北京国信云服科技有限公司发票类型: 增值税专用发票纳税人识别号: 91110108MA003UN95A开户银行名称: 招商银行股份有限公司北京中关村支行开户账号: [REDACTED_ID_CARD_15]公司名称: 北京国信云服科技有限公司公司地址: 北京市海淀区西小口路66号中关村东升科技园B-2楼一层D101A-66室联系电话: [REDACTED_LANDLINE]------------邮寄地址--------------收件人：吕春亭联系电话：[REDACTED_PHONE]邮寄地址：山东省 烟台市 福山区 古现街道长江路300号业达智慧谷C栋410邮箱：[REDACTED_EMAIL]

**客服**：好的

**客服**：您好，您当前在发票列表中查看下，看下是否已经开具了呢

---

## 关闭强制https访问失败

**问题分类**: CDN｜证书问题

### 问题描述

关闭强制https访问操作失败，点击确定按钮无反应

### 客服解答

1. 您好目前这个域名的证书已经过期了 无法使用https协议 因此无法操作关闭强制https

2. 到图示这个地方更换[图片]

3. chatoss.zhyell.com 这个域名目前没有可替换的证书先申请证书 在证书签发后 再替换

4. 您好，手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide4.升级HTTPS配置https://developer.qiniu.com/fusion/manual/4952/https-configuration注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

5. 先把证书申请下来 等证书签发后 再更换证书

6. [图片]

7. 到您的域名服务商后台 根据我们分配的信息 去配置完成验证[图片]

8. 已经处理好了 您再看下

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：关闭强制https访问操作失败，点击确定按钮无反应

**客服**：您好目前这个域名的证书已经过期了 无法使用https协议 因此无法操作关闭强制https

**客户**：您好，那我想更换证书，怎么更换

**客服**：到图示这个地方更换[图片]

**客户**：[图片]您好，没法儿点击确认按钮，点击没反应

**客户**：点击没反应[图片]

**客服**：chatoss.zhyell.com 这个域名目前没有可替换的证书先申请证书 在证书签发后 再替换

**客户**：在哪儿申请免费证书

**客户**：以前都是按照要求，关闭强制https访问，就可以申请证书了。现在点了关闭按钮，再点确认按钮，什么提示都没有，一点儿反应都没有

**客户**：现在业务上正在用，麻烦加急处理下

**客服**：您好，手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/***]

**客户**：怎么给chatoss.zhyell.com更换上

**客服**：先把证书申请下来 等证书签发后 再更换证书

**客服**：[图片]

**客户**：buxing[图片]

**客户**：之前都是先强制关闭https强制访问，然后再申请证书，现在点确认按钮没反应

**客服**：到您的域名服务商后台 根据我们分配的信息 去配置完成验证[图片]

**客户**：确认按钮刚刚可以了

**客服**：已经处理好了 您再看下

---

## 上传文件，文件消失

**问题分类**: 对象存储｜上传下载

### 问题描述

我手动上传文件，文件过了几天消失了

### 客服解答

1. 您好，1.麻烦提供一下具体的资源链接，您需要确认下文件名是否完整正确2.该文件是否有进行过删除操作？您检查一下上传时候是否指定了 deleteAfterDays，或者是存储空间设置了生命周期( https://developer.qiniu.com/kodo/manual/3699/life-cycle-management )3.是否有对文件做过 move 操作 ( https://developer.qiniu.com/kodo/api/1288/move )4.是否有大致的文件上传时间和删除时间

2. 丢失的时间是什么时候呢？

3. 您好，您这边将您的上传文件的上传token给一下，这边看下您的上传token，这边看您上传这个topic目录下的文件都有自动删除的生命周期的，您检查一下上传时候是否指定了 deleteAfterDays

### 根本原因分析

认证凭证或权限配置问题

### 完整对话记录

**客户**：我手动上传文件，文件过了几天消失了

**客服**：您好，1.麻烦提供一下具体的资源链接，您需要确认下文件名是否完整正确2.该文件是否有进行过删除操作？您检查一下上传时候是否指定了 deleteAfterDays，或者是存储空间设置了生命周期( https://developer.qiniu.com/*** )3.是否有对文件做过 move 操作 ( https://developer.qiniu.com/*** )4.是否有大致的文件上传时间和删除时间

**客户**：没有进行删除过，http://image.jianlifangshyz.site/***  上传时间2024-07-16 17:53:14

**客服**：丢失的时间是什么时候呢？

**客户**：没有细查，不知

**客服**：您好，您这边将您的上传文件的上传token给一下，这边看下您的上传token，这边看您上传这个topic目录下的文件都有自动删除的生命周期的，您检查一下上传时候是否指定了 deleteAfterDays

---

## 鸿蒙sdk的使用

**问题分类**: 对象存储｜SDK使用

### 问题描述

Android跟harmonyos的文档差的太多，需要技术支持

### 客服解答

1. 您好具体是哪里有疑问 可以说明下

2. 您这边上传的代码发一下呢

3. 用这个分片上传的方式试下呢// 创建分片上传任务const uploadTask = createMultipartUploadV2Task(file, config);

4. const fileData: UploadFile = UploadFile.fromUri(uri2)

5. 图片路径需要通过域名+文件名拼接来得到

### 根本原因分析

认证凭证或权限配置问题

### 完整对话记录

**客户**：Android跟harmonyos的文档差的太多，需要技术支持

**客服**：您好具体是哪里有疑问 可以说明下

**客户**：at UploadError (oh_modules/.ohpm/@qiniu+upload@1.0.2/oh_modules/@qiniu/upload/src/main/ets/components/@internal/types/error.ts:13:18)    at anonymous (oh_modules/.ohpm/@qiniu+upload@1.0.2/oh_modules/@qiniu/upload/src/main/ets/components/http/index.ts:138:22)[图片]

**客服**：您这边上传的代码发一下呢

**客户**：fileUri = "file://media/Photo/383/IMG_1730167887_377/IMG_20241029_100947.jpg"const file = UploadFile.fromUri(fileUri)let config: UploadConfig = {  // apiServerUrl:"https://upload.qiniup.com",  logLevel: "INFO",  tokenProvider: () => this.getQiniuToken()}// 创建直传任务const uploadTask = createDi***(getContext(this), file, config);uploadTask.onComplete((uploadContext) => {  Logger.debug(TAG + " onComplete " + uploadContext)})uploadTask.onError((uploadContext) => {  Logger.debug(TAG + " onError " + uploadContext?.message)  Logger.debug(TAG + " onError " + uploadContext?.stack)  Logger.debug(TAG + " onError " + uploadContext?.reqId)  Logger.debug(TAG + " onError " + uploadContext?.name)})uploadTask.start()

**客服**：用这个分片上传的方式试下呢// 创建分片上传任务const uploadTask = createMu***(file, config);

**客户**：可以了，现在有个问题，我怎么设置保存的文件名以及获取上传成功的图片路径

**客服**：const fileData: UploadFile = UploadFile.fromUri(uri2)
  fileData.key = "testtest.jpg";
这样设置key

**客服**：图片路径需要通过域名+文件名拼接来得到

---

## 存储空间中的文件批量转为低频存储

**问题分类**: 对象存储｜其他类咨询

### 问题描述

存储空间中的文件（所有BT400开头的文件和LG400开头的文件）批量从标准存储转为低频存储

### 客服解答

1. 您好，您这边可以使用qhsell工具进行批量转存储类型的qshell工具：https://developer.qiniu.com/kodo/1302/qshell#9listbucket2列举文件命令：https://github.com/qiniu/qshell/blob/master/docs/listbucket2.mdbatchexpire批量转换命令：https://github.com/qiniu/qshell/blob/master/docs/batchchtype.md

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：存储空间中的文件（所有BT400开头的文件和LG400开头的文件）批量从标准存储转为低频存储

**客服**：您好，您这边可以使用qhsell工具进行批量转存储类型的qshell工具：https://developer.qiniu.com/***

---

## money.congx.cn 证书配置

**问题分类**: CDN｜证书问题

### 问题描述

长时间未配置完成

### 客服解答

1. 您好，这边手动介入下处理，麻烦稍等。

2. 您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：长时间未配置完成

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

---

## 以图搜图

**问题分类**: 智能多媒体｜其他类咨询

### 问题描述

请问你们平台有以图搜图相关的功能接口可用吗

### 客服解答

1. 您好，十分抱歉目前以图搜图功能已经下线了的，已经不在维护了的

2. 您好，有什么问题您再反馈

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：请问你们平台有以图搜图相关的功能接口可用吗

**客服**：您好，十分抱歉目前以图搜图功能已经下线了的，已经不在维护了的

**客户**：好吧

**客服**：您好，有什么问题您再反馈

---

## 播放器sdk licence

**问题分类**: 视频监控｜SDK使用

### 问题描述

获取QPlayer2的licence

### 客服解答

1. 您好，麻烦提供下已经信息，这边为您申请授权1，客户账号： 必填 账号绑定邮箱or手机号2，业务场景：必填   比如rtmp 直播 mp4点播； 如果 场景比较特殊 需要详细点描述下 比如同个页面有2个播放画面等3，应用名称：选填4，应用分类：社交/游戏/购物/教育/其他 选填5，系统平台：Android/iOS/iOS & Android 必填6，应用包名： 必填

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：获取QPlayer2的licence

**客服**：您好，麻烦提供下已经信息，这边为您申请授权1，客户账号： 必填 账号绑定邮箱or手机号2，业务场景：必填   比如rtmp 直播 mp4点播； 如果 场景比较特殊 需要详细点描述下 比如同个页面有2个播放画面等3，应用名称：选填4，应用分类：社交/游戏/购物/教育/其他 选填5，系统平台：Android/iOS/iOS & Android 必填6，应用包名： 必填

---

## 怎么设置文件访问权限

**问题分类**: 对象存储｜其他类咨询

### 问题描述

你好，我想设置我空间中的文件仅能在特定的域名下访问，比如只能在www.ju1.cn网站上访问，不能在浏览器中单独访问。请问怎么设置？

### 客服解答

1. 您好，这个您设置下 referer 白名单，加入您的域名，然后设置禁止空referer 即可

### 根本原因分析

认证凭证或权限配置问题

### 完整对话记录

**客户**：你好，我想设置我空间中的文件仅能在特定的域名下访问，比如只能在www.ju1.cn网站上访问，不能在浏览器中单独访问。请问怎么设置？

**客服**：您好，这个您设置下 referer 白名单，加入您的域名，然后设置禁止空referer 即可

---

## 域名配置长时间为处理中

**问题分类**: CDN｜配置问题

### 问题描述

beifen.1fh.top 长时间为处理中，已经十几个小时了

### 客服解答

1. 您好，这边手动介入下处理，麻烦稍等。

2. 您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

配置参数错误或不当

### 完整对话记录

**客户**：beifen.1fh.top 长时间为处理中，已经十几个小时了

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

---

## 域名所有权验证

**问题分类**: CDN｜配置问题

### 问题描述

域名解析已经配置txt，域名所有权验证要多久才会刷新,域名解析配置txt 可以放在子域名吗

### 根本原因分析

配置参数错误或不当

### 完整对话记录

**客户**：域名解析已经配置txt，域名所有权验证要多久才会刷新,域名解析配置txt 可以放在子域名吗

---

## 接口限制

**问题分类**: 对象存储｜镜像存储

### 问题描述

/sisyphus/fetch这个抓取的接口是否有并发限制,我们正在迁移文件到七牛,发现这个接口的每秒在6-7个请求,是否可以调大

### 客服解答

1. 你好，异步fetch，任务进入队列异步执行，这个处理的小号时间是不固定的，这个无法调整的

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：/sisyphus/fetch这个抓取的接口是否有并发限制,我们正在迁移文件到七牛,发现这个接口的每秒在6-7个请求,是否可以调大

**客服**：你好，异步fetch，任务进入队列异步执行，这个处理的小号时间是不固定的，这个无法调整的

---

## 需要补充两份文件

**问题分类**: 账户与财务｜其他类咨询

### 问题描述

因商务审核需要贵公司提供以下文件：供方调查表、供应商准入申请单，模版见附件，需加盖公章

### 客服解答

1. 您好，您可以提供一个电话联系方式，这边安排商务与您联系

2. 好的

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：因商务审核需要贵公司提供以下文件：供方调查表、供应商准入申请单，模版见附件，需加盖公章

**客服**：您好，您可以提供一个电话联系方式，这边安排商务与您联系

**客户**：[REDACTED_PHONE]

**客户**：蒉颖峰

**客户**：邮寄地址是：上海市浦东云台路145号806 陈铭炜收 [REDACTED_PHONE]

**客服**：好的

---

## 同个 OSS 空间多个加速域名缓存问题

**问题分类**: CDN｜其他类咨询

### 问题描述

如果 OSS 有一个 images 空间，此空间映射了两个加速域名：1、a.images.com2、b.images.com现在我上传了一个新图片到 images 空间，path 为 /example.png。之后我访问了 https://a.images.com/*** https://b.images.com/*** b.images.com 可以共享 a.images.com 上次回源的结果？

### 客服解答

1. 您好这个是不会共享回源的  初次访问都会从源站拉取资源访问

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：如果 OSS 有一个 images 空间，此空间映射了两个加速域名：1、a.images.com2、b.images.com现在我上传了一个新图片到 images 空间，path 为 /example.png。之后我访问了 https://a.images.com/*** https://b.images.com/*** b.images.com 可以共享 a.images.com 上次回源的结果？

**客户**：补充：上树两个加速域名的 CDN 配置是一样的

**客服**：您好这个是不会共享回源的  初次访问都会从源站拉取资源访问

---

## 解冻域名处理中一个多小时了，而且不能访问

**问题分类**: CDN｜配置问题

### 问题描述

解冻域名处理中一个多小时了，而且不能访问

### 客服解答

1. 您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：解冻域名处理中一个多小时了，而且不能访问[图片]

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

---

## 如何快速删除有文件的空间？

**问题分类**: 对象存储｜其他类咨询

### 问题描述

删除空间前要先清空空间里的文件。但空间里有过万个文件，不清楚应该如何快速删除整个空间？

### 客服解答

1. 您好，您可以通过qshell批量删除，三条命令就可以了。1.先下载qshell工具并使用qshell account 命令登陆账户。下载及安装文档 https://developer.qiniu.com/kodo/tools/1302/qshellwindows环境下安装qshell教程 https://developer.qiniu.com/kodo/kb/5545/windows-environment-installation-qshell-tutorial2.使用listbucket2命令列举出空间内所有资源例如 qshell listbucket2 空间名 -o result.txt命令文档 https://github.com/qiniu/qshell/blob/master/docs/listbucket2.md3.使用batchdelete命令批量删除第2步列举出的列表文件。例如 qshell batchdelete --force 空间名 -i result.txt命令文档 https://github.com/qiniu/qshell/blob/master/docs/batchdelete.md注意：主动删除资源不可以恢复，请慎重

2. 1、可以列举到 result.txt里﻿2、如果您需要我们操作本次空间删除，您可以留下联系方式，这边安排商务经理和您确认下，确认无误后，将由商务经理帮您发起删除申请。注意：删除文件属于高危操作，空间删除后，文件将无法恢复，请您慎重操作。

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：删除空间前要先清空空间里的文件。但空间里有过万个文件，不清楚应该如何快速删除整个空间？

**客服**：您好，您可以通过qshell批量删除，三条命令就可以了。1.先下载qshell工具并使用qshell account 命令登陆账户。下载及安装文档 https://developer.qiniu.com/*** https://developer.qiniu.com/*** qshell listbucket2 空间名 -o result.txt命令文档 https://github.com/*** qshell batchdelete --force 空间名 -i result.txt命令文档 https://github.com/***

**客户**：刚刚再仔细看了一下，是有几十万的文件，可以导出到 result.txt 里吗？

**客服**：1、可以列举到 result.txt里﻿2、如果您需要我们操作本次空间删除，您可以留下联系方式，这边安排商务经理和您确认下，确认无误后，将由商务经理帮您发起删除申请。注意：删除文件属于高危操作，空间删除后，文件将无法恢复，请您慎重操作。

---

## 一直显示处理中

**问题分类**: CDN｜配置问题

### 问题描述

一直显示处理中

### 客服解答

1. 您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：一直显示处理中

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

**客户**：已经可以了

---

## 上游状态回调问题，

**问题分类**: 云短信｜短信发送问题

### 问题描述

你好，  我想咨询下  ，我这边搭的 代码  发送回调 是  这个 ，     可以正常收到状态

### 客服解答

1. 您好，上面的代码是可以正常接收的是吗？

2. 您好，这个我们确认不到的，我们这边能否看下回调是否正常的，回调正常的我们这边回调访问就没有问题的，这个应该是代码的问题的，这个代码需要您这边自行确认一下的，之前是否有正常接收到呢？

### 根本原因分析

配置参数错误或不当

### 完整对话记录

**客户**：你好，  我想咨询下  ，我这边搭的 代码  发送回调 是<?php// 短信发送状态回调的端点if ($_SERVER['REQUEST_METHOD'] == 'POST') {    // 从输入中获取 JSON 字符串    $json = file_get_contents('php://input');    // 将 JSON 解码作为关联阵列    $data = json_decode($json, true);    // 定义要保存短信状态的文件路径    $filePath = 'sms_deli***.txt';  // 请确保此路径是可写的    if (!empty($data['items'])) {        foreach ($data['items'] as $item) {            // 构建要记录的字符串            $logMessage = "已收到移动设备的提交状态：{$item['mobile']}，message_id：{$item['message_id']}，status：{$item['status']}";                        // 如果消息失败，添加错误信息            if ($item['status'] == 'FAILED') {                $logMessage .= "，错误：{$item['error']}";            }                        // 将信息写入日志文件            file_put_contents($filePath, $logMessage . "\n", FILE_APPEND);            // 同时记录到 PHP 的错误日志中            error_log($logMessage);        }    }    // 响应 HTTP 200 OK    http_response_code(200);} else {    // 不是 POST 请求    http_response_code(405);}?>  这个 ，     可以正常收到状态

**客户**：上行状态回调 <?php// 上行短信回调的端点if ($_SERVER['REQUEST_METHOD'] == 'POST') {    // 从输入中获取 JSON 字符串    $json = file_get_contents('php://input');    // 将 JSON 解码作为关联数组    $data = json_decode($json, true);    // 定义要保存上行短信的文件路径    $filePath = 'inbound_sms.txt';  // 请确保此路径是可写的    if (!empty($data['items'])) {        foreach ($data['items'] as $item) {            // 构建要记录的字符串            $logMessage = "收到上行短信：手机号码：{$item['mobile']}，内容：{$item['content']}，时间：{$item['time']}";            // 将上行短信信息写入日志文件            file_put_contents($filePath, $logMessage . "\n", FILE_APPEND);            // 同时记录到 PHP 的错误日志中            error_log($logMessage);        }    }    // 响应 HTTP 200 OK    http_response_code(200);} else {    // 不是 POST 请求    http_response_code(405);}?>是这个

**客户**：上行状态回调 用户回复 任何信息都无法收到  配置管理也都配置上了 方便帮我看下 是否哪里有问题吗

**客服**：您好，上面的代码是可以正常接收的是吗？

**客户**：您好 是的发送回调是有正常接收，  用户回复短信内容的时候 是接收不到

**客户**：看不到 用户的回复内容 ，比如我发查询回复1 ，用户回复了 1  我这边接收不到 ，麻烦贵公司技术帮我看下以上代码 是否正确

**客服**：您好，这个我们确认不到的，我们这边能否看下回调是否正常的，回调正常的我们这边回调访问就没有问题的，这个应该是代码的问题的，这个代码需要您这边自行确认一下的，之前是否有正常接收到呢？

---

## 短信发送失败

**问题分类**: 云短信｜短信发送问题

### 问题描述

短信发送失败。信息一直显示待发送

### 客服解答

1. 您好，稍等下，这边看下

2. 您好，已经重新调整，您再测试发送看下

3. 您好，有什么问题您再反馈

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：短信发送失败。信息一直显示待发送

**客户**：上一个工单，说需要提交法人身份证。欧阳伟贤[REDACTED_ID_CARD_18]

**客户**：[REDACTED_PHONE]，[REDACTED_PHONE],[REDACTED_PHONE]。[REDACTED_PHONE]都是收不到短信

**客户**：请尽快处理

**客服**：您好，稍等下，这边看下

**客服**：您好，已经重新调整，您再测试发送看下

**客户**：好的

**客服**：您好，有什么问题您再反馈

---

## 对公汇款未到账

**问题分类**: 账户与财务｜其他类咨询

### 问题描述

对公汇款未到账

### 客服解答

1. 您好，稍等下，这边催下进度

2. 您好，稍等

3. 您好，已经到账了的

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：对公汇款未到账[图片]

**客服**：您好，稍等下，这边催下进度

**客户**：好的

**客服**：您好，稍等

**客户**：还没好么

**客服**：您好，已经到账了的

**客户**：收到

---

## 公司主体要注销，余额怎么提现

**问题分类**: 账户与财务｜其他类咨询

### 问题描述

公司主体要注销，余额怎么提现

### 客服解答

1. 您好，这个只能原路返回，如果主体一旦注销，使用原企业银行充值，将无法提现，建议您先完成提现，再注销

2. 您好，目前已支持，自助申请原路提现(支付宝，微信，网上银行)，线下提现(银行卡)功能。提现入口链接：https://portal.qiniu.com/financial/withdraw提现注意事项：1、申请提现前，需将该笔提现充值对应的增值税发票退回至七牛云。发票退票流程2、原路提现预计需3～5个工作日，线下提现预计需要5~15个工作日，七牛打款后具体到账时间以银行为准。3、可提现金额需要扣除实时消费金额、欠票金额、赠送金额和未支付金额。提现说明4、支持未认证用户申请原路提现，不支持申请线下提现5、原路提现充值：微信充值（充值时间小于 330 天）、支付宝充值（充值时间小于 330 天）、网上银行充值（充值时间小于 80 天）

### 根本原因分析

认证凭证或权限配置问题

### 完整对话记录

**客户**：公司主体要注销，余额怎么提现

**客服**：您好，这个只能原路返回，如果主体一旦注销，使用原企业银行充值，将无法提现，建议您先完成提现，再注销

**客户**：怎么提现？

**客服**：您好，目前已支持，自助申请原路提现(支付宝，微信，网上银行)，线下提现(银行卡)功能。提现入口链接：https://portal.qiniu.com/*** 330 天）、支付宝充值（充值时间小于 330 天）、网上银行充值（充值时间小于 80 天）

---

## 文件管理全选 点击批量操作，下载 报错

**问题分类**: 对象存储｜上传下载

### 问题描述

文件管理全选 点击批量操作，下载 报错

### 客服解答

1. 您好，您使用下这个图形化工具kodo browser工具批量下载，勾选想要下载的文件/目录后点击【下载】即可。参考：https://developer.qiniu.com/kodo/tools/5972/kodo-browser

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：文件管理全选 点击批量操作，下载 报错

**客服**：您好，您使用下这个图形化工具kodo browser工具批量下载，勾选想要下载的文件/目录后点击【下载】即可。参考：https://developer.qiniu.com/***

---

## 我已经提交

**问题分类**: CDN｜证书问题

### 问题描述

这样就等着，不用再操作了吗？

### 客服解答

1. 您好不是的 证书申请后要做所有权验证配置，步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide4.升级HTTPS配置https://developer.qiniu.com/fusion/manual/4952/https-configuration注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：这样就等着，不用再操作了吗？

**客服**：您好不是的 证书申请后要做所有权验证配置，步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/***]

**客户**：我的证书到期了，重新申请了证书，小程序图片还是不显示？是什么情况？

---

## 流量消耗不对

**问题分类**: CDN｜流量计费问题

### 问题描述

订单：dd0be7f1***。昨天刚买了500G，怎么现在显示全用完了？用哪里了？

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：订单：dd0be7f1***。昨天刚买了500G，怎么现在显示全用完了？用哪里了？

---

## referer防盗链

**问题分类**: 对象存储｜上传下载

### 问题描述

我通过接口将文件上传到私有空间里，并且将签名的文件链接通过接口传送到第三方平台的接口调用，但是第三方接口报错了：原因是我在七牛云中设置了referer防盗链。第三方平台技术是这样说的，我也把IP列表设置到referer防盗链的白名单里了，但还是不能访问。请问怎么处理？

### 客服解答

1. 您好，你们这个设置错了，要去CDN域名里面设置，不是在 空间设置里面设置

2. 您好，之前的回复有误，您直接忽略，您是当前第三方回源源站域名出现403 ，这边先帮您过滤下日志，看下第三方回源携带的真实referer是什么

3. 您好，这个你们现在在空间设置里面，只要开启了允许空referer即可，当前看下来，403的请求都是没有携带 referer的第三方给您的是 回源IP ，这个一般是用于IP黑白名单设置的，存储这边没有设置ip黑白名单，ip无需额外配置

4. 您好，这个情况下，建议你们两个域名分开，给百度OCR和网易易盾 调用的域名 ，使用源站域名1，不对外暴露在网站加载的视频，使用域名2 ，设置referer白名单，并且禁止空您的这个场景，只使用1个域名不太好处理

5. 是的。没有具体操作，不对外暴露是指不在公开的网页中使用，外界无法知晓这个域名。

### 根本原因分析

配置参数错误或不当

### 完整对话记录

**客户**：[图片]我通过接口将文件上传到私有空间里，并且将签名的文件链接通过接口传送到第三方平台的接口调用，但是第三方接口报错了：[图片]原因是我在七牛云中设置了referer防盗链。[图片]第三方平台技术是这样说的，我也把IP列表设置到referer防盗链的白名单里了，但还是不能访问。请问怎么处理？

**客服**：您好，你们这个设置错了，要去CDN域名里面设置，不是在 空间设置里面设置

**客户**：我没找到，具体是在哪里呢？有相应的文档吗？

**客服**：您好，之前的回复有误，您直接忽略，您是当前第三方回源源站域名出现403 ，这边先帮您过滤下日志，看下第三方回源携带的真实referer是什么

**客服**：您好，这个你们现在在空间设置里面，只要开启了允许空referer即可，当前看下来，403的请求都是没有携带 referer的第三方给您的是 回源IP ，这个一般是用于IP黑白名单设置的，存储这边没有设置ip黑白名单，ip无需额外配置

**客户**：是在 CDN-》域名管理-》访问控制-》referer防盗链 里设置吗？我有多个空间，我希望我ju1video空间里的资源只能在www.ju1.cn网站上引用，并且不允许通过浏览器地址栏直接访问空间里的资源 URL，于是我设置“是否允许空 Referer”为“否”。但是有个问题，我的资源URL需要作为参数在 百度OCR和网易易盾 接口中调用，如果设置了不允许空 Referer，那么第三方平台无法下载。 怎么让资源既不能直接在浏览器中输入访问，又能让第三方平台接口调用下载呢？

**客服**：您好，这个情况下，建议你们两个域名分开，给百度OCR和网易易盾 调用的域名 ，使用源站域名1，不对外暴露在网站加载的视频，使用域名2 ，设置referer白名单，并且禁止空您的这个场景，只使用1个域名不太好处理

**客户**：一个资源使用2个域名，一个域名用于第三方接口调用，一个用于网站中加载显示。是这个意思吗？“给百度OCR和网易易盾 调用的域名 ，使用源站域名1，不对外暴露”  这个具体怎么操作呢？需要准备什么资料呢？

**客服**：是的。没有具体操作，不对外暴露是指不在公开的网页中使用，外界无法知晓这个域名。

**客户**：好的，我明白了。谢谢~

---

## 资源包退款

**问题分类**: CDN｜其他类咨询

### 问题描述

您好，请将我账号下没有使用的资源包退款：关联订单号为：438b8b51***

### 客服解答

1. 您好这边同步商务处理 请稍等

2. 已经退款完成

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：您好，请将我账号下没有使用的资源包退款：关联订单号为：438b8b51***

**客服**：您好这边同步商务处理 请稍等

**客服**：已经退款完成

---

## ssl证书nginx配置

**问题分类**: CDN｜证书问题

### 问题描述

服务器nginx那边证书是crt的，目前下载的是pem的，如何吧pem转crt的或者如何通过一键部署把ssl证书部署到服务器端

### 客服解答

1. 您好，您可以使用openssl命令操作转换的，可以百度一下pem类型证书转换crt类型的

2. 您好，您的这个域名已部署这个证书了，使用勾选不上的

3. 目前只支持这些的[图片]

4. 一个ssl证书如何绑定多个域名？这个你们要使用泛域名*.doufangsls.com证书才可以，一个证书匹配若干三级域名，但是泛域名证书是需要收费的，你们确认下

5. 您好，自有证书就是你们 在第三方平台的证书，然后上传到七牛，你问的应该是免费证书，这边有 3个月的免费证书提供

6. 您好，自有这个是第三方的，从第三方上传的，比如你们在腾讯买的亚信的证书，然后将腾讯的亚信证书上传到七牛，才叫做自有证书不需要纠结自有这个概念，直接忽略他，免费证书手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide4.升级HTTPS配置https://developer.qiniu.com/fusion/manual/4952/https-configuration

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：服务器nginx那边证书是crt的，目前下载的是pem的，如何吧pem转crt的或者如何通过一键部署把ssl证书部署到服务器端

**客服**：您好，您可以使用openssl命令操作转换的，可以百度一下pem类型证书转换crt类型的

**客户**：[图片][图片]他这个部署怎么用能不放ssl证书文件就能生效骂

**客户**：ssl证书有没有crt的生成方式

**客服**：您好，您的这个域名已部署这个证书了，使用勾选不上的

**客服**：目前只支持这些的[图片]

**客户**：一个ssl证书如何绑定多个域名？[图片]

**客服**：一个ssl证书如何绑定多个域名？这个你们要使用泛域名*.doufangsls.com证书才可以，一个证书匹配若干三级域名，但是泛域名证书是需要收费的，你们确认下

**客户**：[图片]你们有短期的自有证书吗

**客服**：您好，自有证书就是你们 在第三方平台的证书，然后上传到七牛，你问的应该是免费证书，这边有 3个月的免费证书提供

**客户**：有3个月的免费自有证书吗？

**客服**：您好，自有这个是第三方的，从第三方上传的，比如你们在腾讯买的亚信的证书，然后将腾讯的亚信证书上传到七牛，才叫做自有证书不需要纠结自有这个概念，直接忽略他，免费证书手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/***

---

## zazhiba.com.cn 这个站首页的ccs js这些样式加载不了 http和htpps的问题

**问题分类**: CDN｜刷新缓存问题

### 问题描述

zazhiba.com.cn 这个站首页的ccs js这些样式加载不了 http和htpps的问题

### 客服解答

1. 您好麻烦给下截图标注说明 这边看下

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：zazhiba.com.cn 这个站首页的ccs js这些样式加载不了 http和htpps的问题

**客服**：您好麻烦给下截图标注说明 这边看下

---

## 访问对象存储失败

**问题分类**: 对象存储｜上传下载

### 问题描述

网络ping延迟很低（10ms以内），但上传数据时报失败:2024/10/29 06:15:16.158316 juicefs[47] : Upload chunks/0/248/248816_0_4194304: timeout after 10m0s: function timeout (try 1) [cached_store.go:410]                              ││ 2024/10/29 06:15:19.207225 juicefs[47] : found new configuration: storage=s3 bucket=http://hornwood-juicefs1.s3.cn-north-1.qiniucs.com ak=IAM-DAv5*** ││ 2024/10/29 06:15:48.691704 juicefs[47] : Upload chunks/0/248/248885_5_4194304: timeout after 10m0s: function timeout (try 3) [cached_store.go:410]                              ││ 2024/10/29 06:16:28.343629 juicefs[47] : slow request: PUT chunks/0/249/249706_5_4194304 (req_id: "", err: RequestError: send request failed                                    ││ caused by: Put "http://s3.cn-north-1.qiniucs.com/***": readfrom tcp [REDACTED_PRIVATE_IP].15:56662->222.222.*.*:80: write tcp [REDACTED_PRIVATE_IP].15:566 ││ 2024/10/29 06:16:41.007755 juicefs[47] : Upload chunks/0/249/249404_8_4194304: timeout after 10m0s: function timeout (try 1) [cached_store.go:410]                              ││ 2024/10/29 06:16:50.943377 juicefs[47] : Upload chunks/0/249/249789_15_4194304: timeout after 10m0s: function timeout (try 2) [cached_store.go:410]                             ││ 2024/10/29 06:17:32.361433 juicefs[47] : Upload chunks/0/249/249788_0_4194304: timeout after 10m0s: function timeout (try 1) [cached_store.go:410]                              ││ 2024/10/29 06:18:18.694178 juicefs[47] : Upload chunks/0/249/249770_9_4194304: timeout after 10m0s: function timeout (try 1) [cached_store.go:410]                              ││ 2024/10/29 06:18:25.087054 juicefs[47] : slow request: PUT chunks/0/249/249404_8_4194304 (req_id: "", err: RequestError: send request failed                                    ││ caused by: Put "http://s3.cn-north-1.qiniucs.com/***": readfrom tcp [REDACTED_PRIVATE_IP].15:42538->111.225.*.*:80: write tcp [REDACTED_PRIVATE_IP].15:425 ││ 2024/10/29 06:18:25.321110 juicefs[47] : slow request: PUT chunks/0/249/249021_11_4194304 (req_id: "", err: RequestError: send request failed                                   ││ caused by: Put "http://s3.cn-north-1.qiniucs.com/***": readfrom tcp [REDACTED_PRIVATE_IP].15:56498->222.222.*.*:80: write tcp [REDACTED_PRIVATE_IP].15:56 ││ 2024/10/29 06:19:01.941913 juicefs[47] : slow request: PUT chunks/0/248/248885_5_4194304 (req_id: "", err: RequestError: send request failed                                    ││ caused by: Put "http://s3.cn-north-1.qiniucs.com/***": readfrom tcp [REDACTED_PRIVATE_IP].15:57408->111.225.*.*:80: write tcp [REDACTED_PRIVATE_IP].15:574 ││ 2024/10/29 06:19:01.955651 juicefs[47] : slow request: PUT chunks/0/249/249792_1_4194304 (req_id: "", err: RequestError: send request failed                                    ││ caused by: Put "http://s3.cn-north-1.qiniucs.com/***": readfrom tcp [REDACTED_PRIVATE_IP].15:34850->111.225.*.*:80: write tcp [REDACTED_PRIVATE_IP].15:3485 ││ 2024/10/29 06:19:14.919533 juicefs[47] : Upload chunks/0/249/249772_11_4194304: timeout after 10m0s: function timeout (try 1) [cached_store.go:410]                             ││ 2024/10/29 06:19:26.789656 juicefs[47] : slow request: PUT chunks/0/249/249788_0_4194304 (req_id: "", err: RequestError: send request failed                                    ││ caused by: Put "http://s3.cn-north-1.qiniucs.com/***": readfrom tcp [REDACTED_PRIVATE_IP].15:36434->111.225.*.*:80: write tcp [REDACTED_PRIVATE_IP].15:3643 ││ 2024/10/29 06:20:13.649247 juicefs[47] : slow request: PUT chunks/0/249/249736_7_4194304 (req_id: "", err: RequestError: send request failed

### 客服解答

1. 您好，您这边使用SDK接口或者其他方式上传看下是否正常呢？

2. 您好，这个是没有限制的，根据您本地客户端的上行带宽进行合理配置并发数的

3. 嗯嗯

4. 您好，测试域名不支持生产环境使用，而且有效期为30天，会自动过期的，然后S3的话建议可以使用S3域名的

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：网络ping延迟很低（10ms以内），但上传数据时报失败:2024/10/29 06:15:16.158316 juicefs[47] <WARNING>: Upload chunks/0/248/248816_0_4194304: timeout after 10m0s: function timeout (try 1) [cached_store.go:410]                              ││ 2024/10/29 06:15:19.207225 juicefs[47] <INFO>: found new configuration: storage=s3 bucket=http://hornwood-juicefs1.s3.cn-north-1.qiniucs.com ak=IAM-DAv5*** ││ 2024/10/29 06:15:48.691704 juicefs[47] <WARNING>: Upload chunks/0/248/248885_5_4194304: timeout after 10m0s: function timeout (try 3) [cached_store.go:410]                              ││ 2024/10/29 06:16:28.343629 juicefs[47] <WARNING>: slow request: PUT chunks/0/249/249706_5_4194304 (req_id: "", err: RequestError: send request failed                                    ││ caused by: Put "http://s3.cn-north-1.qiniucs.com/***": readfrom tcp [REDACTED_PRIVATE_IP].15:56662->222.222.*.*:80: write tcp [REDACTED_PRIVATE_IP].15:566 ││ 2024/10/29 06:16:41.007755 juicefs[47] <WARNING>: Upload chunks/0/249/249404_8_4194304: timeout after 10m0s: function timeout (try 1) [cached_store.go:410]                              ││ 2024/10/29 06:16:50.943377 juicefs[47] <WARNING>: Upload chunks/0/249/249789_15_4194304: timeout after 10m0s: function timeout (try 2) [cached_store.go:410]                             ││ 2024/10/29 06:17:32.361433 juicefs[47] <WARNING>: Upload chunks/0/249/249788_0_4194304: timeout after 10m0s: function timeout (try 1) [cached_store.go:410]                              ││ 2024/10/29 06:18:18.694178 juicefs[47] <WARNING>: Upload chunks/0/249/249770_9_4194304: timeout after 10m0s: function timeout (try 1) [cached_store.go:410]                              ││ 2024/10/29 06:18:25.087054 juicefs[47] <WARNING>: slow request: PUT chunks/0/249/249404_8_4194304 (req_id: "", err: RequestError: send request failed                                    ││ caused by: Put "http://s3.cn-north-1.qiniucs.com/***": readfrom tcp [REDACTED_PRIVATE_IP].15:42538->111.225.*.*:80: write tcp [REDACTED_PRIVATE_IP].15:425 ││ 2024/10/29 06:18:25.321110 juicefs[47] <WARNING>: slow request: PUT chunks/0/249/249021_11_4194304 (req_id: "", err: RequestError: send request failed                                   ││ caused by: Put "http://s3.cn-north-1.qiniucs.com/***": readfrom tcp [REDACTED_PRIVATE_IP].15:56498->222.222.*.*:80: write tcp [REDACTED_PRIVATE_IP].15:56 ││ 2024/10/29 06:19:01.941913 juicefs[47] <WARNING>: slow request: PUT chunks/0/248/248885_5_4194304 (req_id: "", err: RequestError: send request failed                                    ││ caused by: Put "http://s3.cn-north-1.qiniucs.com/***": readfrom tcp [REDACTED_PRIVATE_IP].15:57408->111.225.*.*:80: write tcp [REDACTED_PRIVATE_IP].15:574 ││ 2024/10/29 06:19:01.955651 juicefs[47] <WARNING>: slow request: PUT chunks/0/249/249792_1_4194304 (req_id: "", err: RequestError: send request failed                                    ││ caused by: Put "http://s3.cn-north-1.qiniucs.com/***": readfrom tcp [REDACTED_PRIVATE_IP].15:34850->111.225.*.*:80: write tcp [REDACTED_PRIVATE_IP].15:3485 ││ 2024/10/29 06:19:14.919533 juicefs[47] <WARNING>: Upload chunks/0/249/249772_11_4194304: timeout after 10m0s: function timeout (try 1) [cached_store.go:410]                             ││ 2024/10/29 06:19:26.789656 juicefs[47] <WARNING>: slow request: PUT chunks/0/249/249788_0_4194304 (req_id: "", err: RequestError: send request failed                                    ││ caused by: Put "http://s3.cn-north-1.qiniucs.com/***": readfrom tcp [REDACTED_PRIVATE_IP].15:36434->111.225.*.*:80: write tcp [REDACTED_PRIVATE_IP].15:3643 ││ 2024/10/29 06:20:13.649247 juicefs[47] <WARNING>: slow request: PUT chunks/0/249/249736_7_4194304 (req_id: "", err: RequestError: send request failed

**客服**：您好，您这边使用SDK接口或者其他方式上传看下是否正常呢？

**客户**：请教下，咱们七牛云对bucket的并发读写数是有限制的吧？可以帮忙看看hornwood-juicefs1这个bucket的iops之类的限制值是多少吗？

**客服**：您好，这个是没有限制的，根据您本地客户端的上行带宽进行合理配置并发数的

**客户**：好的

**客服**：嗯嗯

**客户**：我们要使用s3协议在生产环境用的话，要使用哪个域名呢？是用系统域名还是自定义源站域名？这个测试域名的限制是针对哪个域名的？https://developer.qiniu.com/***

**客服**：您好，测试域名不支持生产环境使用，而且有效期为30天，会自动过期的，然后S3的话建议可以使用S3域名的

---

## 百度抓取异常

**问题分类**: CDN｜配置问题

### 问题描述

2024.10.29  14：16分 提交百度的抓取情况现示403 ，麻烦看一下日志，是不是我的黑名单把百度的IP封杀了?

### 客服解答

1. 您好，分析具体的访问量和访问行为，建议在控制台 https://portal.qiniu.com/cdn/log 下载CDN日志后进行分析CDN日志的下载方式，以及日志中字段的含义参考文档：https://developer.qiniu.com/fusion/manual/3847/cdn-log-fusion这边不清楚您这边具体需要确认的IP的，您这边可以下载自行分析看下的

2. 您好，您这边源站是不是将我们这边的IP拦截了，您看下是否是源站将我们给拦截了，那您源站应该将我们的IP加白的183.60.220.0/24120.83.145.0/24120.232.101.0/242409:8c54:2030:209::0/642408:8756:4cff:d205::0/64240e:97d:2014:203::0/64125.94.43.0/24163.142.153.0/24183.240.180.0/242409:8c54:b010:3d::0/662408:8756:4cff:f014::0/66240e:97c:20:701::0/66

3. 您的源站应该是有限制的，这边请求您的源站都会返回403的curl -I 'http://47.112.246.194/1.html' -H 'host:www.xxzrjzx.com'

4. 您好，源站限制还是有问题的，报错是找不到域名，这边测试的话也有问题[图片]

5. 您这边目前得需要让源站我们可以通过这个正常访问到的才行的目前绑host请求您的源站还是请求不到的：curl -I 'http://47.112.246.194/1.html' -H 'host:www.xxzrjzx.com'

6. 您好，您nginx上是否有这个www.xxzrjzx.com站点呢？

7. 您好，您这边源站是不是有UA限制啊，这边测试curl是不通的，切换浏览器的UA后才能访问到的

8. 嗯嗯好的，您这边后续可以排查下源站相关配置的

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：2024.10.29  14：16分 提交百度的抓取情况现示403 ，麻烦看一下日志，是不是我的黑名单把百度的IP封杀了?[图片]

**客服**：您好，分析具体的访问量和访问行为，建议在控制台 https://portal.qiniu.com/*** 下载CDN日志后进行分析CDN日志的下载方式，以及日志中字段的含义参考文档：https://developer.qiniu.com/***

**客户**：220.181.*.* UNKNOWN 48 [29/Oct/2024:14:20:57 +0800] "GET http://www.xxzrjzx.com/ HTTP/1.1" 403 297 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/***)"116.162.*.* UNKNOWN 101 [29/Oct/2024:14:50:47 +0800] "GET http://www.xxzrjzx.com/ HTTP/1.1" 403 704 "https://m.baidu.com/" "Mozilla/5.0 (Linux; Android 10; ELE-AL00 Build/HUAWEIELE-AL00; wv) 这两个IP是百度的，而且这个两个IP并没有在黑名单中，为什么还返回403.我的源站没有拦百度的IP

**客服**：您好，您这边源站是不是将我们这边的IP拦截了，您看下是否是源站将我们给拦截了，那您源站应该将我们的IP加白的183.60.220.0/24120.83.145.0/24120.232.101.0/242409:8c54:2030:209::0/642408:8756:4cff:d205::0/64240e:97d:2014:203::0/64125.94.43.0/24163.142.153.0/24183.240.180.0/242409:8c54:b010:3d::0/662408:8756:4cff:f014::0/66240e:97c:20:701::0/66

**客户**：源站没有拦截啊

**客户**：我曾经[图片]把网站切换源站 百度是正常的

**客服**：您的源站应该是有限制的，这边请求您的源站都会返回403的curl -I 'http://47.112.*.*/*** -H 'host:www.xxzrjzx.com'
HTTP/1.1 403 Forbidden
Server: nginx
Date: Wed, 30 Oct 2024 08:20:49 GMT
Content-Type: text/html
Content-Length: 146
Connection: keep-alive

**客户**：#if ($request_method !~* GET|POST) {  #   return 403;#	 break; #  }我取消这个，你在看看

**客户**：[图片]现在 百度又出现404了

**客服**：您好，源站限制还是有问题的，报错是找不到域名，这边测试的话也有问题[图片]

**客户**：难道 是域名被劫持了吗，我现在DNS指向源站看看

**客服**：您这边目前得需要让源站我们可以通过这个正常访问到的才行的目前绑host请求您的源站还是请求不到的：curl -I 'http://47.112.*.*/*** -H 'host:www.xxzrjzx.com'

**客户**：是什么问题 ？我DNS解析源站 百度抓取就正常了[图片]

**客服**：您好，您nginx上是否有这个www.xxzrjzx.com站点呢？

**客服**：您好，您这边源站是不是有UA限制啊，这边测试curl是不通的，切换浏览器的UA后才能访问到的

**客户**：应该没有UA限制，算了吧，我直接用源站，暂时不用CDN。

**客服**：嗯嗯好的，您这边后续可以排查下源站相关配置的

---

## 已经充值费用，有10分钟了什么时候恢复

**问题分类**: 账户与财务｜账户问题

### 问题描述

费用充值已经超过10分钟了，什么时候能够正常使用

### 客服解答

1. 您好，您的账号已经完成解冻

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：费用充值已经超过10分钟了，什么时候能够正常使用

**客服**：您好，您的账号已经完成解冻

**客户**：为什么图片还是无法加载出来呢

**客户**：可以了，恢复了

---

## 流量计费不对

**问题分类**: CDN｜流量计费问题

### 问题描述

订单：dd0be7f1***。昨天刚买了500G，怎么现在显示全用完了？用哪里了？

### 客服解答

1. 您好，资源包选择当月生效的话，这个月产生的流量会全部使用资源包抵扣的您可以查看下您的实时消费，这边会显示使用资源包抵扣

2. 您好，之前使用余额抵扣的流量会使用资源包抵扣，余额会进行返回

3. 您好，很抱歉，这边无法查看到您的订单信息，您的联系方式提供下，这边同步商务和您联系，帮您看下

4. 您好，稍等下，这边同步下

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：订单：dd0be7f1***。昨天刚买了500G，怎么现在显示全用完了？用哪里了？

**客服**：您好，资源包选择当月生效的话，这个月产生的流量会全部使用资源包抵扣的您可以查看下您的实时消费，这边会显示使用资源包抵扣

**客户**：我又没欠费，为啥要抵扣？抵扣什么？

**客服**：您好，之前使用余额抵扣的流量会使用资源包抵扣，余额会进行返回

**客户**：我余额没改变过，你是在这儿猜谜谜呢？我都把订单号发给你了，你不会查下？这么敷衍？还有你们这破工单，连个图都传不了。

**客服**：您好，很抱歉，这边无法查看到您的订单信息，您的联系方式提供下，这边同步商务和您联系，帮您看下

**客户**：[REDACTED_PHONE]

**客服**：您好，稍等下，这边同步下

---

## 上传证书报错

**问题分类**: CDN｜证书问题

### 问题描述

[    [        {            "title": "请求 ID",            "content": "HLwROhELefUj2QIY"        },        {            "title": "日志栈",            "content": "fusionicp:9;fusionsslcert:13/400"        }    ]]

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：[    [        {            "title": "请求 ID",            "content": "HLwROhELefUj2QIY"        },        {            "title": "日志栈",            "content": "fusionicp:9;fusionsslcert:13/400"        }    ]]

---

## 671f2ce1a0f9bb37c2625b5f订单号SSL一直在审核

**问题分类**: 云主机｜其他类咨询

### 问题描述

证书备注名sealandlogis.com产品名称TrustAsia 免费域名型 (DV) 单域名证书创建时间2024-10-28 14:19:13订单状态待审核

### 客服解答

1. 您好，您需要提示进行文件验证，系统会自动轮询，轮询通过才会颁发证书参考文档：https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

2. 您好，稍等下，这边帮您加急下

3. 您好，很抱歉，目前订单已经超时，您重新申请下呢之前ca无法检测到验证值，您是否有做海外访问限制，如果有的话，需要加白ca海外服务器IP，如果还是无法使用文件验证方式通过域名验证，可以尝试使用其他验证方式完成验证。验证IP白名单:91.199.212.13291.199.212.13391.199.212.14891.199.212.15191.199.212.17691.212.12.13254.189.196.217

4. 您好，要不你这边手动申请下证书，进行下dns验证？

5. 不使用文件验证了？

6. 您好，手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/certificate/apply2.补全信息3.免费证书验证https://developer.qiniu.com/ssl/manual/3667/ssl-certificate-of-free-dns-validation-guide4.升级HTTPS配置https://developer.qiniu.com/fusion/manual/4952/https-configuration注意事项升级https后，流量计费说明：https://developer.qiniu.com/fusion/kb/3887/https-issues-related-to-the-faq[图片]

7. 您好，这个只是我们验证通过了，ca那边没有验证通过，您尝试使用dns验证看下吧

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：证书备注名sealandlogis.com产品名称TrustAsia 免费域名型 (DV) 单域名证书创建时间2024-10-28 14:19:13订单状态待审核

**客服**：您好，您需要提示进行文件验证，系统会自动轮询，轮询通过才会颁发证书参考文档：https://developer.qiniu.com/***]

**客户**：提交了文件验证，还是提示一直待审核

**客服**：您好，稍等下，这边帮您加急下

**客服**：您好，很抱歉，目前订单已经超时，您重新申请下呢之前ca无法检测到验证值，您是否有做海外访问限制，如果有的话，需要加白ca海外服务器IP，如果还是无法使用文件验证方式通过域名验证，可以尝试使用其他验证方式完成验证。验证IP白名单:91.199.212.13291.199.212.13391.199.212.14891.199.212.15191.199.212.17691.212.12.13254.189.196.217

**客户**：验证IP白名单是什么意思？怎么验证

**客服**：您好，要不你这边手动申请下证书，进行下dns验证？

**客服**：不使用文件验证了？

**客服**：您好，手动申请并使用免费SSL证书步骤如下1.免费证书申请证书品牌：TrustAsia限免证书种类：DV限免https://portal.qiniu.com/***]

**客户**：为什么域名所有权验证验证通过了，CA不颁发证书？

**客服**：您好，这个只是我们验证通过了，ca那边没有验证通过，您尝试使用dns验证看下吧

---

## 我新添加了一个域名为什么在域名管理那里看不到

**问题分类**: 对象存储｜其他类咨询

### 问题描述

我新添加了一个域名为什么在域名管理那里看不到ssl.juhao.com

### 客服解答

1. 您好是刚创建的新域名吗 创建后要做域名所有权验证 验证通过才可以显示域名

2. 创建时页面点击所有权验证 根据系统分配的信息 到您的域名服务商后台解析

3. 创建之后提示 您还没有输入域名[图片]

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：我新添加了一个域名为什么在域名管理那里看不到ssl.juhao.com

**客服**：您好是刚创建的新域名吗 创建后要做域名所有权验证 验证通过才可以显示域名

**客户**：解析到哪里？

**客服**：创建时页面点击所有权验证 根据系统分配的信息 到您的域名服务商后台解析

**客户**：麻烦截图看一下在哪里点击所有权验证

**客户**：没有看到所有权验证[图片]

**客服**：创建之后提示 您还没有输入域名[图片]

---

## sdk

**问题分类**: 云短信｜其他类咨询

### 问题描述

请问方便提供c#语言的sdk吗？谢谢-framework

### 客服解答

1. 您好可以参考 https://developer.qiniu.com/kodo/1237/csharp 下载安装使用

2. 目前暂时没有C# 相关示例demo，您可以参考API接口文档：https://developer.qiniu.com/sms/5897/sms-api-send-message 自行实现

3. 是的

4. sdk里关于云短信demo的问题 我们会向产品侧反馈评估优化

5. 参考这个demo 修改下部分参数使用试试

6. 好的

### 根本原因分析

认证凭证或权限配置问题

### 完整对话记录

**客户**：请问方便提供c#语言的sdk吗？谢谢-framework

**客户**：请问sms短信服务方便提供c#语言的sdk吗？谢谢-framework

**客服**：您好可以参考 https://developer.qiniu.com/*** 下载安装使用

**客户**：....这个是存储服务，不是短信服务

**客服**：目前暂时没有C# 相关示例demo，您可以参考API接口文档：https://developer.qiniu.com/*** 自行实现

**客户**：......

**客户**：// 计算 HMAC-SHA1 签名，并对签名结果做 URL 安全的 Base64 编码sign = hmac_sha1(data, "Your_Secret_Key")encodedSign = urlsafe_***(sign)这里的 hmac_sha1(data, "Your_Secret_Key")，是拼接data和sk再做sha1吗？文档地址：服务鉴权_API 文档_云短信 - 七牛开发者中心

**客服**：是的

**客户**：没救了..您可以看下华为提供的文档C#_消息&短信 MSGSMS_华为云...没c#可以理解，cpp也没有...what can isay。我再试下拼接吧，不行就用其他服务商

**客服**：sdk里关于云短信demo的问题 我们会向产品侧反馈评估优化

**客户**：太夸张了真的，老哥。0.0.阿里和华为的sms都尝试过，这个的确太夸张了。

**客服**：参考这个demo 修改下部分参数使用试试
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Security.Cryptography;
using System.IO;
using Qiniu.Util;
using System.Web;
namespace Qiniu.Token
{
    public class Qiniutoken
    {
        public static string qiniutoken(Mac mac,Uri url,String body,String contentType,String method)
        {
            // input path and host and rawquery
            string path = url.AbsolutePath;
            string host = url.Host;
            string rawquery = url.Query;
            var data = new System.Text.StringBuilder();
            data.AppendFormat("{0} {1}", method, path);
            if (rawquery != String.Empty)
                data.AppendFormat("{0}", rawquery);
            data.AppendFormat("\nHost: {0}", host);
            if (contentType != String.Empty)
                data.AppendFormat("\nContent-Type: {0}", contentType);
            data.Append("\n\n");
            if (contentType != String.Empty && contentType != "application/octet-stream")
                data.Append(body);
            String sdata = data.ToString();
            Console.WriteLine(sdata);
            HMACSHA1 hmac = new HMACSHA1(Encoding.UTF8.GetBytes(mac.SecretKey));
            byte[] digest = hmac.ComputeHash(Encoding.UTF8.GetBytes(sdata));
            string qiniuToken = String.Format("Qiniu {0}:{1}", mac.AccessKey, System.Convert.ToBase64String(digest).Replace("/", "_").Replace("+", "-"));
            Console.WriteLine(qiniuToken);
            return qiniuToken;
        }
    }
}

**客户**：放弃了，转其他云了

**客服**：好的

---

## 关于上行异常

**问题分类**: 视频监控｜业务咨询

### 问题描述

上行异常

### 客服解答

1. 您好，请稍等

2. 您好，您现在重启下设备和网路，看下是否可以呢

### 根本原因分析

文件传输或分片处理问题

### 完整对话记录

**客户**：上行异常

**客服**：您好，请稍等

**客户**：好的 你查一下，图片附件上传不了

**客服**：您好，您现在重启下设备和网路，看下是否可以呢

---

## 开发票

**问题分类**: 账户与财务｜发票问题

### 问题描述

开取未开的发票

### 客服解答

1. 您好，在发票管理中 申请发票哈https://portal.qiniu.com/financial/invoice-contract/invoice

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：开取未开的发票

**客服**：您好，在发票管理中 申请发票哈https://portal.qiniu.com/***

---

## SSL 一直显示处理中 https显示已过期

**问题分类**: 对象存储｜其他类咨询

### 问题描述

已经更新ssl， 但是一直显示https处理中无法使用 已经更新了两个星期了

### 客服解答

1. 您好，请稍等

2. 您好，久等了，已处理完成，您确认下

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：已经更新ssl， 但是一直显示https处理中无法使用 已经更新了两个星期了

**客服**：您好，请稍等

**客服**：您好，久等了，已处理完成，您确认下

---

## 充值错误，需要转移。

**问题分类**: 账户与财务｜账户问题

### 问题描述

转出账户[REDACTED_PHONE]转入账户[REDACTED_PHONE]原因：充值错误。

### 客服解答

1. 您好，麻烦留一下您的联系方式，这边商务跟进处理

### 根本原因分析

需要进一步排查具体原因

### 完整对话记录

**客户**：转出账户[REDACTED_PHONE]转入账户[REDACTED_PHONE]原因：充值错误。

**客服**：您好，麻烦留一下您的联系方式，这边商务跟进处理

---

## 下载文件下不下来

**问题分类**: CDN｜其他类咨询

### 问题描述

下载文件下不下来

### 客服解答

1. 您好哪个文件无法下载 给下对应链接

2. 给下复现超时的文件链接 这边看下

3. 您好您这边没有提供任何有效信息 无法定位问题1、提供下超时的访问链接2、麻烦提供下您的 ip、dns 信息，和cdn节点信息，这边代理测试下可以通过访问这个链接 http://ping.huatuo.qq.com/ 获取本地的 ip 和 dns 信息，在检测域名这边输入下cdn域名，点击提交检测，然后截图通过工单提交给我们[图片]3、建议使用 chrome 浏览器，按照下述文档获取下 remote adress(对端节点ip)，request header(客户端请求头) 以及 response header(服务端响应头)信息，方便我们查询分析问题。https://developer.qiniu.com/fusion/kb/1478/how-to-access-network-in-the-browser-request-information

4. cdn侧没有异常 检查一下您的下行网络带宽是否有多业务占用

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：下载文件下不下来

**客服**：您好哪个文件无法下载 给下对应链接

**客户**：3点半 到4点多 这头文件读取超时

**客户**：能看一下我们这头有啥冲突吗

**客服**：给下复现超时的文件链接 这边看下

**客户**：或者什么原因导致的

**客服**：您好您这边没有提供任何有效信息 无法定位问题1、提供下超时的访问链接2、麻烦提供下您的 ip、dns 信息，和cdn节点信息，这边代理测试下可以通过访问这个链接 http://ping.huatuo.qq.com/ 获取本地的 ip 和 dns 信息，在检测域名这边输入下cdn域名，点击提交检测，然后截图通过工单提交给我们[图片]3、建议使用 chrome 浏览器，按照下述文档获取下 remote adress(对端节点ip)，request header(客户端请求头) 以及 response header(服务端响应头)信息，方便我们查询分析问题。https://developer.qiniu.com/***

**客户**：2024-10-29 13:34:54,288 - INFO - https://audiovideo.axa2.com/*** 下载中2024-10-29 13:34:54,313 - INFO - https://audiovideo.axa2.com/*** 下载中2024-10-29 13:35:41,320 - INFO - https://audiovideo.axa2.com/*** 下载中2024-10-29 13:35:41,331 - INFO - https://audiovideo.axa2.com/*** 下载中

**客户**：现在访问可以

**客户**：能不能看看3点多 有没有什么波动

**客服**：cdn侧没有异常 检查一下您的下行网络带宽是否有多业务占用

---

## games.resource.hcdcdn.cn

**问题分类**: CDN｜访问下载

### 问题描述

这个域名访问不了 https 已经配置了

### 客服解答

1. 您好，这边测试看是正常的证书的，您这边清理一下本地dns缓存后再看下呢[图片]

2. 您好，这个应该就是本地缓存导致的，可以看下使用无痕浏览看下是否可以正常访问的

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：这个域名访问不了 https 已经配置了

**客服**：您好，这边测试看是正常的证书的，您这边清理一下本地dns缓存后再看下呢[图片]

**客户**：部分地区访问不了 不知道为什么 不是全部的

**客服**：您好，这个应该就是本地缓存导致的，可以看下使用无痕浏览看下是否可以正常访问的

---

## 两个存储资源包没有叠加起作用

**问题分类**: 对象存储｜其他类咨询

### 问题描述

如图，资源包是50T+10T，总共60T。但是资源包的抵扣数量只有50T的生效了，10T的没生效，

### 客服解答

1. 你好，这边截图提供看下呢https://portal.qiniu.com/financial/respack-mgr/current

2. 您好，您的资源60t已经抵扣完了的，资源包不同区域抵扣系数不同，华北存储您使用1g，需要抵扣1.2g资源包[图片]

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：[图片]如图，资源包是50T+10T，总共60T。但是资源包的抵扣数量只有50T的生效了，10T的没生效，[图片]

**客服**：你好，这边截图提供看下呢https://portal.qiniu.com/***

**客户**：图[图片]

**客服**：您好，您的资源60t已经抵扣完了的，资源包不同区域抵扣系数不同，华北存储您使用1g，需要抵扣1.2g资源包[图片]

**客户**：好的

---

## 加了gzip参数就无法下载

**问题分类**: CDN｜访问下载

### 问题描述

如果是使用 curl https://art.cdn.pagor.cn/*** Accept-Encoding 的头就没返回了请问是不是 gzip 引擎出问题了？

### 客服解答

1. 您好，刷新下文件cdn缓存看下刷新缓存方法请参考：https://developer.qiniu.com/fusion/kb/1325/refresh-the-cache-and-the-effect-of-time方法1: portal.qiniu.com 控制台刷新缓存，点击左侧 cdn => 刷新预取方法2: api 接口地址：https://developer.qiniu.com/fusion/api/1229/cache-refreshTip : url 刷新，全网生效 10min 左右，目录刷新需要 30min 左右

2. 您好，带随机参数跳过缓存是可以正常访问的，刷新下cdn缓存，还有本地缓存看下[图片]

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：如果是使用 curl https://art.cdn.pagor.cn/*** Accept-Encoding 的头就没返回了请问是不是 gzip 引擎出问题了？

**客服**：您好，刷新下文件cdn缓存看下刷新缓存方法请参考：https://developer.qiniu.com/*** portal.qiniu.com 控制台刷新缓存，点击左侧 cdn => 刷新预取方法2: api 接口地址：https://developer.qiniu.com/*** : url 刷新，全网生效 10min 左右，目录刷新需要 30min 左右

**客户**：刷新预取没用，你可以用浏览器试试看我上面说的操作

**客服**：您好，带随机参数跳过缓存是可以正常访问的，刷新下cdn缓存，还有本地缓存看下[图片]

---

## 费用咨询

**问题分类**: CDN｜流量计费问题

### 问题描述

总用量0.0763 GB你好，看到费用明细里产生了-0.02元，总流量是0.0763，还没超过10G免费流量，开始计费了？是什么原因，望支持，多谢。

### 客服解答

1. 您好，计费项的完整名称麻烦提供下

2. 您好，cdn-https没有免费额度的。cdn-http有10G免费额度免费额度须知：https://developer.qiniu.com/af/kb/1574/free-credit-information

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：总用量0.0763 GB你好，看到费用明细里产生了-0.02元，总流量是0.0763，还没超过10G免费流量，开始计费了？是什么原因，望支持，多谢。

**客服**：您好，计费项的完整名称麻烦提供下

**客户**：请看附件[图片]

**客服**：您好，cdn-https没有免费额度的。cdn-http有10G免费额度免费额度须知：https://developer.qiniu.com/***

**客户**：哦哦，多谢啦

---

## 防盗链加白名单一直在配置中

**问题分类**: CDN｜配置问题

### 问题描述

添加白名单的配置时间特别长，早上9点多就开始加了，一直到现在还是显示的在配置中，刷新也没有任何的反应

### 客服解答

1. 您好，这边手动介入下处理，麻烦稍等。

2. 您好，抱歉让您久等了，已经处理完成，您确认下。

3. 没事的

### 根本原因分析

配置参数错误或不当

### 完整对话记录

**客户**：添加白名单的配置时间特别长，早上9点多就开始加了，一直到现在还是显示的在配置中，刷新也没有任何的反应[图片]

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

**客户**：好的，已经完成了，谢谢麻烦了

**客服**：没事的

---

## 新建域名CDN 域名  premium.wscn.net 卡住

**问题分类**: CDN｜其他类咨询

### 问题描述

新建域名CDN 域名  premium.wscn.net 一直卡主。

### 客服解答

1. 您好已经帮您手动介入处理完成

### 根本原因分析

CDN节点或缓存问题

### 完整对话记录

**客户**：新建域名CDN 域名  premium.wscn.net 一直卡主。

**客服**：您好已经帮您手动介入处理完成

**客户**：收到，谢谢

---

## 大小屏联动直播业务直播流接口打通技术需求

**问题分类**: 直播云｜其他类咨询

### 问题描述

在大屏上做直播带货，然后主播通过手机端直播，用户通过大屏看直播，大屏的直播技术我们公司会开发，现在需要一个可以提供手机端的直播技术，且能把大小屏的直播流接口打通的技术公司。

### 客服解答

1. 您好，请稍等

2. 您好，还在帮您核实中

3. 老师，这边直播能实现推流，手机端也有推流sdk和rtc的sdk，以及播放器，能实现直播的全套流程，和sdk，您可以看下直播的相关文档了解下https://developer.qiniu.com/pili

4. 可以腾讯会议

5. 您可以约个时间，把会议信息发出来，这边到时候按时进来

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：在大屏上做直播带货，然后主播通过手机端直播，用户通过大屏看直播，大屏的直播技术我们公司会开发，现在需要一个可以提供手机端的直播技术，且能把大小屏的直播流接口打通的技术公司。

**客服**：您好，请稍等

**客户**：有什么进展了吗

**客服**：您好，还在帮您核实中

**客服**：老师，这边直播能实现推流，手机端也有推流sdk和rtc的sdk，以及播放器，能实现直播的全套流程，和sdk，您可以看下直播的相关文档了解下https://developer.qiniu.com/***

**客户**：那我们能通过会议或者是别的方式双方沟通，出一套具体的方案嘛。

**客服**：可以腾讯会议

**客服**：您可以约个时间，把会议信息发出来，这边到时候按时进来

---

## CDN 加载文件异常

**问题分类**: CDN｜访问下载

### 问题描述

页面加载 CSS，多刷新几次页面就会偶发出现加载失败的情况，文件大小由 412kb 变成 800b。

### 客服解答

1. 您好，请求到历史的cdn缓存了。刷新cdn缓存后再观察下刷新缓存方法请参考：https://developer.qiniu.com/fusion/kb/1325/refresh-the-cache-and-the-effect-of-time方法1: portal.qiniu.com 控制台刷新缓存，点击左侧 cdn => 刷新预取方法2: api 接口地址：https://developer.qiniu.com/fusion/api/1229/cache-refreshTip : url 刷新，全网生效 10min 左右，目录刷新需要 30min 左右

2. 您好，同文件名的历史版本，源站已经更新过看不到哪一次的，上一个个这个文件名的文件内容，删除后上传同文件名的文件或覆盖上传会出现。最近更新是最近一次此文件名的上传时间

3. cdn缓存默认是一个月的。有覆盖更新需要手动刷新下。800b就是上个版本的文件缓存，您刷新一下cdn缓存预计就可以了。

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：[图片]页面加载 CSS，多刷新几次页面就会偶发出现加载失败的情况，文件大小由 412kb 变成 800b。

**客服**：您好，请求到历史的cdn缓存了。刷新cdn缓存后再观察下刷新缓存方法请参考：https://developer.qiniu.com/*** portal.qiniu.com 控制台刷新缓存，点击左侧 cdn => 刷新预取方法2: api 接口地址：https://developer.qiniu.com/*** : url 刷新，全网生效 10min 左右，目录刷新需要 30min 左右

**客户**：请求到了哪一次的缓存？这个文件显示最近更新时间 14:18，正是上次提交的时间。[图片]

**客服**：您好，同文件名的历史版本，源站已经更新过看不到哪一次的，上一个个这个文件名的文件内容，删除后上传同文件名的文件或覆盖上传会出现。最近更新是最近一次此文件名的上传时间

**客户**：意思是源文件有覆盖更新就会这样吗？我理解 CDN 缓存刷新不及时，可能会加载到旧的文件，但是这个 800b 是咋回事呢？

**客服**：cdn缓存默认是一个月的。有覆盖更新需要手动刷新下。800b就是上个版本的文件缓存，您刷新一下cdn缓存预计就可以了。

**客户**：行，我这边处理一下吧。

---

## 是否可以设置cdn流量限制，超过就停止服务？

**问题分类**: CDN｜访问下载

### 问题描述

是否可以设置cdn流量限制，超过就停止服务？

### 客服解答

1. 您好，很抱歉，没有这个配置的建议配置『流量带宽告警』，为预防CDN流量超过某一阈值，可以针对CDN域名设置告警配置，当使用量超过您设置的告警值会进行通知。参考文档：https://developer.qiniu.com/fusion/kb/4059/the-alarm-configuration

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：是否可以设置cdn流量限制，超过就停止服务？

**客服**：您好，很抱歉，没有这个配置的建议配置『流量带宽告警』，为预防CDN流量超过某一阈值，可以针对CDN域名设置告警配置，当使用量超过您设置的告警值会进行通知。参考文档：https://developer.qiniu.com/***

---

## 批量转化出存储类型

**问题分类**: 对象存储｜其他类咨询

### 问题描述

筛选出所有低频存储，批量转化为归档只读应该怎么做

### 客服解答

1. 您好，您这边可以使用qhsell工具进行批量转存储类型的qshell工具：https://developer.qiniu.com/kodo/1302/qshell#9batchexpire命令：https://github.com/qiniu/qshell/blob/master/docs/batchchtype.md

2. 按照这个示例来转换[图片]

3. 2015/03/22/——是文件名前缀 给下您的联系方式 这边同步商务处理

4. 好的 请保持电话通畅

5. qshell listbucket2 <Bucket> --file-types 1 -o <ListBucketResultFile>

6. 测试正常的，您用的哪个版本qshellqshell -v

7. 是的

8. awk '{print $1}' result.txt > result1.t 保留文件名

9. 看下上条回复 用awk命令处理

10. awk需要安装 可以在网上找一下教程 这边目前没有这个文档操作步骤

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：筛选出所有低频存储，批量转化为归档只读应该怎么做

**客服**：您好，您这边可以使用qhsell工具进行批量转存储类型的qshell工具：https://developer.qiniu.com/***

**客户**：请帮我看看这个命令有什么错误qshell chtype wenyin-dev       __（7）+黄德辉1224__（代金券）_160x70mm_500张_{300g}___________电话，[REDACTED_PHONE]红红 地址，大足区龙岗街道办事处北环路白鹤林1号楼20230829183553.cdr  4

**客户**：请帮我看看这个命令有什么错误[图片]

**客服**：按照这个示例来转换[图片]

**客户**：这个是文件路径吗？[图片]

**客户**：能不能帮我远程操作一下？确实搞不懂

**客服**：2015/03/22/——是文件名前缀 给下您的联系方式 这边同步商务处理

**客户**：[REDACTED_PHONE]

**客服**：好的 请保持电话通畅

**客户**：listbucket2命令中的--file-types 的实际使用案例 和使用格式我想把所有低频存储的列举出来并输出成文本

**客服**：qshell listbucket2 <Bucket> --file-types 1 -o <ListBucketResultFile>

**客户**：我用的是这个命令，但是一直在屏幕输出，没有输出在文档上来

**客户**：qshell listbucket2 wenyin-dev --file-types 1 -o liebiao.txt我是用这样的命令

**客服**：测试正常的，您用的哪个版本qshellqshell -v

**客户**：如果我想把文件批量转为归档直读的话，使用qshell batchchtype if-pbl -i tochangetype.txt 这个命令的时候，必须把tochangetype.txt这个文档里面的 后缀都改为4吗？

**客户**：如果我想把文件批量转为归档直读的话，使用qshell batchchtype if-pbl -i tochangetype.txt 这个命令的时候，必须把tochangetype.txt这个文档里面的 后缀都改为4吗？[图片]

**客服**：是的

**客户**：listbucket2的命令使用中，我如何只获取，文件名与存储类型。过滤其他不需要的信息

**客户**：如图中，这些是我不需要的信息[图片]

**客服**：awk '{print $1}' result.txt > result1.t 保留文件名

**客户**：qshell listbucket2 wenyin-dev --file-types 1 -o liebiao.txt我使用命令是这样的，但是导出来的文档里面 会包含很多信息，但是我只需要文件名 和存储类型应该怎么做

**客服**：看下上条回复 用awk命令处理

**客户**：win10系统里面有awk吗？还是qshell集成了这个工具？

**客服**：awk需要安装 可以在网上找一下教程 这边目前没有这个文档操作步骤

---

## 数据迁移报错

**问题分类**: 对象存储｜数据迁移

### 问题描述

shqy空间的图片迁移到 moko-2024时报错了，是什么原因？是区域 Endpoint 填写的不对吗?

### 客服解答

1. 您好，你们这个是怎么配置的迁移任务，麻烦将你们的配置截图这边看下

2. 稍等

3. 您好，区域endpoint 修改成这个域名：s3.cn-north-1.qiniucs.coms3服务域名：https://developer.qiniu.com/kodo/4088/s3-access-domainname

4. 输入https://s3.cn-north-1.qiniucs.comdevelop那个是文档。

5. 稍等

6. 您好，源端区域修改成 cn-north-1修改后再试下

7. 嗯嗯不客气的

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：shqy空间的图片迁移到 moko-2024时报错了，是什么原因？是区域 Endpoint 填写的不对吗?[图片]

**客服**：您好，你们这个是怎么配置的迁移任务，麻烦将你们的配置截图这边看下

**客户**：下面是配置的截图[图片][图片]

**客服**：稍等

**客服**：您好，区域endpoint 修改成这个域名：s3.cn-north-1.qiniucs.coms3服务域名：https://developer.qiniu.com/***

**客户**：是这样吗？ 区域 Endpoint 输入https://s3.cn-north-1.qiniucs.com 还是 https://developer.qiniu.com/***]

**客户**：s3服务域名：https://developer.qiniu.com/*** 这个在哪里输入？

**客服**：输入https://s3.cn-north-1.qiniucs.comdevelop那个是文档。

**客户**：[图片]这是配置信息，还是不行[图片]

**客服**：稍等

**客服**：您好，源端区域修改成 cn-north-1修改后再试下

**客户**：我又试了一次，现在可以了 端区域还是用的 华北-河北

**客户**：谢谢了

**客服**：嗯嗯不客气的

---

## 10月25日已备案的域名在七牛云空间新增域名时显示“未备案域名”

**问题分类**: CDN｜配置问题

### 问题描述

aimoermall.cn域名于2024年10月25日在工信部备案成功，但是在七牛云存储空间绑定域名-新增域名时显示该域名为“未备案域名”

### 客服解答

1. 稍等

2. 您好，域名是否弄错了，这个域名这边查询没备案的[图片]工信部官网查询方式：1.登录 https://beian.miit.gov.cn/#/Integrated/recordQuery2.选择「ICP备案查询」3.输入网站域名，点击搜索

3. 您好，我们这边需要域名的网站备案。

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：aimoermall.cn域名于2024年10月25日在工信部备案成功，但是在七牛云存储空间绑定域名-新增域名时显示该域名为“未备案域名”

**客服**：稍等

**客服**：您好，域名是否弄错了，这个域名这边查询没备案的[图片]工信部官网查询方式：1.登录 https://beian.miit.gov.cn/***

**客户**：我去确认下

**客户**：域名是经过 APP 备案的，不是网站备案[图片]

**客服**：您好，我们这边需要域名的网站备案。

---

## 配置ssl证书

**问题分类**: CDN｜配置问题

### 问题描述

帮我配置最新的ssl证书

### 客服解答

1. 您好，请稍等

2. 您好，久等了，已处理完成，您确认下

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：帮我配置最新的ssl证书

**客服**：您好，请稍等

**客服**：您好，久等了，已处理完成，您确认下

---

## 账号注销

**问题分类**: 账户与财务｜账户问题

### 问题描述

有阿里云

### 客服解答

1. 您好，目前注销可以在控制台操作https://portal.qiniu.com/developer/user/security目前用户自助注销需满足以下所有条件：1、账号为普通账号（非财务父子账号、OEM账号）2、账号下实时消费无产品用量、无消费金额（数据需要您自己删除）对象存储：https://portal.qiniu.com/kodo/bucketCDN：https://portal.qiniu.com/cdn/domain3、账号下无各种欠费实时消费明细（查看您当月消费）https://portal.qiniu.com/financial/bills/estimated-consume如有欠费，将在下月5号出账、8号扣款，结算后，您再提交账号注销。4、账号下没有正在处理的提现审批https://portal.qiniu.com/financial/withdraw5、账号当前没有被冻结注意：账号注销后，账号无法找回

2. 您好，如果控制台提示提交工单，请检查下注销需满足的条件。本月如有用量，下月出账后控制台再提交注销。

3. 您好，这边反馈专员为您申请。

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：有阿里云

**客户**：注销账号

**客服**：您好，目前注销可以在控制台操作https://portal.qiniu.com/***

**客户**：好的，请帮我注销。注销需要工单系统的支持。

**客服**：您好，如果控制台提示提交工单，请检查下注销需满足的条件。本月如有用量，下月出账后控制台再提交注销。

**客户**：满足条件。

**客户**：请速度处理，你们的效率太慢。

**客户**：不给注销请直说，没必要绕弯子。

**客服**：您好，这边反馈专员为您申请。

---

## 配置证书一直没配置好

**问题分类**: CDN｜配置问题

### 问题描述

看图

### 客服解答

1. 您好证书在审核中 请耐心等待

2. 已经部署完成

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：看图[图片]

**客服**：您好证书在审核中 请耐心等待

**客服**：已经部署完成

---

## 咨询下pili-sdk-java最新版本

**问题分类**: 直播云｜其他类咨询

### 问题描述

目前公司不支持低版本的sdk，需要升级，需要咨询下pili-sdk-java最新版本

### 客服解答

1. 您好，您稍等这边帮您确认一下

2. 您好，您目前 使用的 是哪个sdk，以及需要哪些功能。pili-sdk-java 这个不再维护了。如果需要使用 直播相关的功能，可参考：https://github.com/qiniu/java-sdk/blob/master/src/main/java/com/qiniu/streaming/StreamingManager.java或者直接按照七牛官网文档，调 HTTP 接口 。

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：目前公司不支持低版本的sdk，需要升级，需要咨询下pili-sdk-java最新版本

**客服**：您好，您稍等这边帮您确认一下

**客服**：您好，您目前 使用的 是哪个sdk，以及需要哪些功能。pili-sdk-java 这个不再维护了。如果需要使用 直播相关的功能，可参考：https://github.com/*** HTTP 接口 。

---

## qvs播放不出来 不正常

**问题分类**: 视频监控｜业务咨询

### 问题描述

31011500991180056686

### 客服解答

1. 您好工单401902已经回复您 目前已经恢复正常 您再看下呢

2. 测试来看播放是正常的  您再试下[图片]

3. 这边后台看下 请稍等

4. 31011500991180061727重启设备看下

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：31011500991180056686

**客户**：都离线31011500991180061727瓯态园菜尚门平台离线6查看通道列表删除31011500991180061728菜袋子平台

**客服**：您好工单401902已经回复您 目前已经恢复正常 您再看下呢

**客户**：https://qvs-live.qzb.ax168.com:447/3nm4x1h77l89s/31011500***.m3u8 还是不行啊 ，感觉平台也很卡

**客服**：测试来看播放是正常的  您再试下[图片]

**客户**：今天就不太正常 31011500991180061727瓯态园菜尚门平台离线6查看通道列表删除31011500991180061728菜袋子平台离线6查看通道列表 这2个平台也是离线

**客服**：这边后台看下 请稍等

**客户**：就有的正常，有的不正常

**客服**：31011500991180061727重启设备看下
31011500991180061728是在线状态的
[图片]

---

## 七牛有没有官方的cdn域名地址

**问题分类**: CDN｜其他类咨询

### 问题描述

七牛有没有官方的cdn域名地址

### 客服解答

1. 您好，我们这边只有测试域名的，都是需要创建自定义CDN域名才行的，也就是创建自己的域名的，我们的测试域名只有创建新空间的时候才会分配有效期30天的测试域名的

2. 您好，这个是s3域名的，您这边是需要用来干什么用的

3. 那您这边获取下您的空间的s3域名看下的，在您的空间管理的空间概览下查看[图片]

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：[图片]七牛有没有官方的cdn域名地址

**客服**：您好，我们这边只有测试域名的，都是需要创建自定义CDN域名才行的，也就是创建自己的域名的，我们的测试域名只有创建新空间的时候才会分配有效期30天的测试域名的

**客户**：https://tudongli.s3.cn-south-1.qiniucs.com/***

**客服**：您好，这个是s3域名的，您这边是需要用来干什么用的

**客户**：是需要在拼多多的服务器内下载该图片，然后拼多多云内是不允许访问外网的

**客服**：那您这边获取下您的空间的s3域名看下的，在您的空间管理的空间概览下查看[图片]

**客户**：s3域名不支持直接访问的吗[图片]

**客户**：好吧，我知道了

---

## 证书无法验证所有权

**问题分类**: CDN｜证书问题

### 问题描述

1

### 客服解答

1. 您好，这个不上我们平台购买的吧，解析记录验证是需要到您的域名购买厂商完成的

2. 嗯嗯好的，您这边关闭工单即可的

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：1[图片]

**客服**：您好，这个不上我们平台购买的吧，解析记录验证是需要到您的域名购买厂商完成的

**客户**：已解决了

**客服**：嗯嗯好的，您这边关闭工单即可的

---

## 更换覆盖节点卡住

**问题分类**: CDN｜配置问题

### 问题描述

zjjcts.com和www.zjjcts.com更换覆盖节点卡住

### 客服解答

1. 您好，这边手动介入下处理，麻烦稍等。

2. 您好，抱歉让您久等了，已经处理完成，您确认下。

### 根本原因分析

CDN节点或缓存问题

### 完整对话记录

**客户**：zjjcts.com和www.zjjcts.com更换覆盖节点卡住

**客服**：您好，这边手动介入下处理，麻烦稍等。

**客服**：您好，抱歉让您久等了，已经处理完成，您确认下。

---

## 小程序图片加载不出来

**问题分类**: CDN｜访问下载

### 问题描述

做的小程序图片加载不出来

### 客服解答

1. 您好，您账户在 2024-07-24 09:41 已被冻结，2024-09-11 12:28 解冻自冻结之日起的第 31 个自然日，如现金账户仍然欠费，视作您默认放弃数据，七牛云存储将删除账户中的数据，并且不可恢复。欠费冻结须知：https://developer.qiniu.com/af/kb/1543/lack-of-information

2. 您好，创建新的空间直接上传就好域名的话，可以删除重新绑定下

3. 您好，可以参考下https://developer.qiniu.com/kodo/1233/console-quickstart

4. 您好，具体需要什么信息，您是哪里不理解，可以拨打 400-808-9176 转 2 号线和我们联系

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：做的小程序图片加载不出来

**客服**：您好，您账户在 2024-07-24 09:41 已被冻结，2024-09-11 12:28 解冻自冻结之日起的第 31 个自然日，如现金账户仍然欠费，视作您默认放弃数据，七牛云存储将删除账户中的数据，并且不可恢复。欠费冻结须知：https://developer.qiniu.com/***

**客户**：那怎么恢复呢

**客户**：我现在解冻了不欠费了，我怎么再把图片重新上传呢

**客服**：您好，创建新的空间直接上传就好域名的话，可以删除重新绑定下

**客户**：有教程吗

**客服**：您好，可以参考下https://developer.qiniu.com/***

**客户**：很多步骤教程没有，方便电话沟通吗

**客服**：您好，具体需要什么信息，您是哪里不理解，可以拨打 400-808-9176 转 2 号线和我们联系

---

## 未消费完金额发票退票

**问题分类**: 账户与财务｜发票问题

### 问题描述

2024年1月份打款金额25000元，开数电普通发票价税合计25000元，截止到现在存在未消费完的金额，公司要注销，需要申请把剩余金额提现，部分金额发票要作废。

### 客服解答

1. 您好，麻烦您提供一个联系方式，这边安排商务与您联系，协助提现退款

2. 好的

3. 您好，是开票金额没有退回是吗，您需要开多少金额的发票，开票信息提供下，这边同步商务给您开票

4. 你好，好的，这个就是开票信息内的对吧

5. 您好，稍等下

6. 您好，您的发票已经申请，您可以在发票管理查看您的开票进度https://portal.qiniu.com/financial/invoice-contract/invoice

7. 您好，您的开票信息不是专票吧，不是的没法开专票的

8. 您好，您后台有对应的开票信息吗？有的话，您控制台取消申请看下，这边同步商务重新给您开票

9. 这边内部同步看下

10. 您好，很抱歉，已经开出来 ，没法取消了如果需要需求需要在走一次退票流程

11. 您好，这样可以吗？如果后续您需要开专票，您需要后台有专票的开票信息，可以添加下

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：2024年1月份打款金额25000元，开数电普通发票价税合计25000元，截止到现在存在未消费完的金额，公司要注销，需要申请把剩余金额提现，部分金额发票要作废。[图片]

**客服**：您好，麻烦您提供一个联系方式，这边安排商务与您联系，协助提现退款

**客户**：[REDACTED_PHONE]

**客服**：好的

**客户**：您好！发票已退票，需要重新开已消费金额的发票要怎么申请？

**客服**：您好，是开票金额没有退回是吗，您需要开多少金额的发票，开票信息提供下，这边同步商务给您开票

**客户**：需要开票金额：21540.22元，如能开专票麻烦开专票，谢谢！开票信息如下：公司名称：深圳市聚立网络科技有限公司税号：91440300MA5HM7HT6F地址：深圳市宝安区西乡街道臣田社区宝民二路190号臣田工业区商业楼8530手机号码：[REDACTED_PHONE]开户行及账号：中国农业银行深圳翠竹支行  41011300040042765

**客服**：你好，好的，这个就是开票信息内的对吧

**客户**：对的

**客服**：您好，稍等下

**客服**：您好，您的发票已经申请，您可以在发票管理查看您的开票进度https://portal.qiniu.com/***

**客户**：不能开专票吗？

**客服**：您好，您的开票信息不是专票吧，不是的没法开专票的

**客户**：开专票和普票为啥和我给您的开票信息有关呢？专普票的开票信息不都一样的咩

**客服**：您好，您后台有对应的开票信息吗？有的话，您控制台取消申请看下，这边同步商务重新给您开票

**客户**：[图片]重新添加开票信息了

**客户**：[图片]这个如何取消？

**客服**：这边内部同步看下

**客户**：好的，麻烦了

**客服**：您好，很抱歉，已经开出来 ，没法取消了如果需要需求需要在走一次退票流程

**客户**：好的吧

**客服**：您好，这样可以吗？如果后续您需要开专票，您需要后台有专票的开票信息，可以添加下

---

## 如何下载下来空间的文件

**问题分类**: 对象存储｜上传下载

### 问题描述

我想知道能否下载下来，做个测试

### 客服解答

1. 您好，在空间-文件管理，选择您需要下载的文件右侧「更多」中下载

2. 您好您可以使用最新的图形化工具kodo-browser下载试下，支持批量管理。https://developer.qiniu.com/kodo/tools/5972/kodo-browser注意：使用该工具目前进行上传/下载，如果不指定cdn域名的话，下载产生的流量费用为「外网流量」

3. 用源站域名下载产生外网流出流量 价格 参考 https://www.qiniu.com/prices/kodo

### 根本原因分析

SSL/TLS证书配置问题

### 完整对话记录

**客户**：我想知道能否下载下来，做个测试

**客户**：能人工吗

**客服**：您好，在空间-文件管理，选择您需要下载的文件右侧「更多」中下载

**客户**：但是只能一个一个的下载 对吗？这就导致没有办法更换对象云存储了 对不。我有几万个文件，没法下载下来吧

**客服**：您好您可以使用最新的图形化工具kodo-browser下载试下，支持批量管理。https://developer.qiniu.com/***

**客户**：那在七牛上 启用 CDN 怎么收费的呢？我目前就只配置了两个原站域名。没有配置加速CDN

**客服**：用源站域名下载产生外网流出流量 价格 参考 https://www.qiniu.com/***

---

## 订单66f6c6fab32fad84195b7488

**问题分类**: CDN｜证书问题

### 问题描述

订单66f6c6fab32fad84195b7488尽快审核，都尼玛1个月了

### 客服解答

1. 您好，免费证书24h没有办法就超时了，您重新申请下证书订单呢

2. 您好，很抱歉，这个订单已经超时，无法继续申请，您需要重新申请下订单才行

### 根本原因分析

网络连接问题或DNS解析异常

### 完整对话记录

**客户**：订单66f6c6fab32fad84195b7488尽快审核，都尼玛1个月了

**客服**：您好，免费证书24h没有办法就超时了，您重新申请下证书订单呢

**客户**：申请你麻痹，日你妈

**客服**：您好，很抱歉，这个订单已经超时，无法继续申请，您需要重新申请下订单才行

---

