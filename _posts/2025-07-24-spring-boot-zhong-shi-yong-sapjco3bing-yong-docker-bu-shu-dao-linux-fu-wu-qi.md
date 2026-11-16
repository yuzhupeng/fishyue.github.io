---
layout: post
title: spring boot中使用sapjco3，并用docker部署到Linux服务器
date: 2025-07-24 09:00:00
summary: 一、在windows中的配置
categories: Backend
---

# [在spring boot中使用sapjco3，并用docker部署到Linux服务器] "发布于 2025-07-24 15:26")

一、在windows中的配置

二、linux的配置

三、spring boot项目构建

sapjco3包含很多个操作系统版本，不同的操作系统需要使用不同的配置文件和配置方式，不过sapjco3.jar是可以通用的。

![](https://img2020.cnblogs.com/blog/1543878/202008/1543878-20200819105934366-640195848.png)

# 一、在windows中的配置

windows中需要的文件主要包括：

sapjco3.dll

sapjco3.pdb

sapjco3.jar

## 1、sapjco3.dll文件

32位系统

将 sapjco3.dll 加入到c:/windows/system32/目录 或者 将 sapjco3.dll 加入到 JDK/bin 目录下；

64位系统

将 sapjco3.dll 加入到c:/windows/SysWOW64/目录 或者 将 sapjco3.dll 加入到 JDK/bin 目录下；

64位机可以直接将sapjco3.dll放在"C:\Windows\System32"目录下，这样以后不必针对具体的应用来配置它；

![](https://img2020.cnblogs.com/blog/1543878/202008/1543878-20200819110146552-1363688094.png)

上面的配置是为了将它放在系统环境变量path可以找到的地方，所以也可以直接把sapjco3.dll文件所在的位置，配置到系统环境变量path下面；

## 2、sapjco3.pdb文件

在springboot中使用sapjco3可以不用配置sapjco3.pdb，如果在kettle中需要调用sap的接口，则需要把sapjco3.pdb放在kettle的根目录"${KETTLE_HOME}/"下面；

## 3、sapjco3.jar文件

这个文件就是java调用sap的主要api，包含许多方法，如连接sap、获取接口参数、设置接口参数和获取返回参数等；

这里**推荐将sapjco3.jar放在项目的lib目录下面，然后在项目打包的时候，将本地依赖的jar包打包到项目jar中**；

也可以将sapjco3.jar放在${JAVA_HOME}/lib目录下或者放在其他目录并将该目录下的sapjco3.jar添加到系统环境变量CLASSPATH下面；

也可以在pom.xml中引入sapjco3.jar依赖，这样项目打包的时候会将sapjco3.0.14.jar打包到项目jar里面，但是这样sapjco3.jar文件是带有版本后缀的，在项目部署的时候，会启动失败，报错：It is not allowed to rename or repackage the original archive “sapjco3.jar”。需要手动进入jar包，将sapjco3.0.14.jar名称修改为sapjco3.jar；

[![复制代码](//assets.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

```
<!-- https://mvnrepository.com/artifact/com.sap.conn.jco/sapjco3 -->
<dependency>
        <groupId>com.sap.conn.jco</groupId>
        <artifactId>sapjco3</artifactId>
        <version>3.0.14</version>
        <scope>test</scope>
</dependency>
```

[![复制代码](//assets.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

还有一种方式是使用maven的install命令将sapjco3.jar安装到本地仓库，然后在项目中引入依赖，但是切记jar包不能后缀版本号；

---

# 二、linux的配置

linux需要的文件包括：

libsapjco3.so

sapjco3.jar

其中jar包sapjco3.jar与windows版的可以通用；重点是将libsapjco3.so文件配置到linux的jre/lib运行时环境中或者项目可以加载到libsapjco3.so的其他位置；

## 1、Linux系统：

1)将压缩文件解压到某个目录下面，比如/home/appuser/sapjco3/ 下面：

> tar -zxvf sapjco3-linuxx86_64-3.0.17.tgz -C /home/appuser/sapjco3

2)配置环境变量

> vim /etc/profile

在配置文件内加上下面的内容：

> export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/home/appuser/sapjco3
>
> export CLASSPATH=.:JAVA_HOME/lib:{JAVA_HOME}/lib:JAVA_HOME/lib:{LD_LIBRARY_PATH}/sapjco3.jar

或者

先将文件libsapjco3.so复制到${JAVA_HOME}/jre/lib/amd64/server文件夹下

> export LD_LIBRARY_PATH=LD_LIBRARY_PATH:{LD_LIBRARY_PATH}:LD_LIBRARY_PATH:{JAVA_HOME}/jre/lib/amd63/server
>
> export CLASSPATH=.:JAVA_HOME/lib:{JAVA_HOME}/lib:JAVA_HOME/lib:{LD_LIBRARY_PATH}/sapjco3.jar

上面配置的重点是libsapjco3.so的位置，对于sapjco3.jar，可以配置到环境变量${CLASSPATH}中，也可以打包在项目中；

官方的推荐如下：

## 2、docker：

在docker中可以使用 **-v 宿主机目录:容器目录** 的方式将libsapjco3.so和sapjco3.jar进行映射：

> docker run -d \
>
> --restart=always \
>
> --name springboot-sapjco3 \
>
> -v "$PWD/sapringboot-sapjco3":/usr/app \
>
> **-v /home/appuser/sapjco3/libsapjco3.so:/usr/lib/libsapjco3.so** \
>
> --workdir="/usr/app" \
>
> -p 8080:8080 \
>
> java:8u111 \
>
> java -jar sprringboot-sapjco3.jar

这样就将宿主机的libsapjco3.so映射到了容器的/usr/lib下面；

如果项目中没有打包sapjco3.jar文件，也可以在docker run 的 -v 命令中将该文件映射到jdk的lib目录下：

> -v /hemo/appuser/sapjco3/sapjco3.jar:/usr/lib/jvm/java-8-openjdk-amd64/lib/sapjco3.jar

# 三、spring boot项目构建

## 1、项目结构与配置文件

将sapjco3.jar放在项目resource/lib下面；

CONNECT_SAP_CONFIG.jcoDestination文件是连接SAP的配置文件，必需放在项目的根目录下面，其内容如下：

> 
```
#for tests only !
jco.client.lang=en
jco.client.client=710
jco.client.user=admin
jco.client.passwd=admin
jco.client.sysnr=00
jco.client.ashost=192.168.1.11
```

配置pom.xml，引入自定义jar包，并在项目打包时将自定义jar包打包进项目的jar：

[![复制代码](//assets.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

```
<dependencies>
        <!--maven打包时，将resources/lib/sapjco3.jar一并打包-->
        <dependency>
            <groupId>com.sap</groupId>
            <artifactId>sapjco3</artifactId>
            <version>1.0</version>
            <scope>system</scope>
          <systemPath>${project.basedir}/src/main/resources/lib/sapjco3.jar</systemPath>
        </dependency>
        <!--其他依赖-->
        <dependency>
              ......
        </dependency>
<dependencies>
<build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <executable>true</executable>
                    <includeSystemScope>true</includeSystemScope>
                </configuration>
                <dependencies>
                    <dependency>
                        <groupId>org.springframework</groupId>
                        <artifactId>springloaded</artifactId>
                        <version>1.2.5.RELEASE</version>
                    </dependency>
                </dependencies>
            </plugin>
        </plugins>
</build>
```

[![复制代码](//assets.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

## 2.获取sap连接对象

[![复制代码](//assets.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

```
public class JCoDestinationBuilder {
    public static JCoDestination destination = null;
    private static final Logger logger = LogUtils.getPlatformLogger();
    public static JCoDestination build() throws JCoException {
        if (null==destination) {
            synchronized (JCoDestinationBuilder.class) {
                try {
                    if (null == destination)
                        destination = JCoDestinationManager.getDestination("CONNECT_SAP_CONFIG");
                    destination.ping();
                    logger.info("Connect to SAP successfully......");
                } catch (JCoException e) {
                    e.printStackTrace();
                    logger.error("Connect to SAP failed, error msg: " + e.toString());
                }
            }
        }
        //logger.info(String.valueOf(destination.getAttributes()));
        return destination;
    }
}
```

[![复制代码](//assets.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

## 3.调用sap接口函数

[![复制代码](//assets.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

```
@Service
public class SappiMonitorServiceImpl implements SappiMonitorService {
    @Autowired
    Sm58EntityRepository sm58EntityRepository;
    @Autowired
    MessageService messageService;
    @Autowired
    private Environment environment;
    private static final Logger logger = LogUtils.getPlatformLogger();

    @Override
    public JSONObject monitorSm58(SappiSm58 sappiSm58) throws JCoException {
        if (sappiSm58==null) sappiSm58 = new SappiSm58();
        JCoDestination destination = JCoDestinationBuilder.build();
        JCoFunction function = destination.getRepository().getFunction("ZMONITOR_SM58");
        JCoParameterList importlist = function.getImportParameterList();
        JCoParameterList exportList = function.getExportParameterList();
        JCoParameterList tables = function.getTableParameterList();

        importlist.setValue("I_BEGIN_DATE",sappiSm58.getI_begin_date());
        importlist.setValue("I_END_DATE",sappiSm58.getI_end_date());
        try {
            function.execute(destination);
            //logger.warn(function.toXML());
        } catch (JCoException e) {
            e.printStackTrace();
            logger.error("execute()failed......");
        }
        JCoTable t_arfcistate = tables.getTable("T_ARFCISTATE");
        for (int i=0;i<t_arfcistate.getNumRows();i++) {
            t_arfcistate.setRow(i);
            Sm58Entity sm58Entity = new Sm58Entity();
            sm58Entity.setArfcipid(t_arfcistate.getString("ARFCIPID"));
            sm58Entity.setArfcpid(t_arfcistate.getString("ARFCPID"));
            sm58Entity.setArfctime(t_arfcistate.getString("ARFCTIME"));
            sm58Entity.setArfctidcnt(t_arfcistate.getString("ARFCTIDCNT"));
            sm58Entity.setArfcdest(t_arfcistate.getString("ARFCDEST"));
            sm58Entity.setArfcluwcnt(t_arfcistate.getString("ARFCLUWCNT"));
            sm58Entity.setArfcstate(t_arfcistate.getString("ARFCSTATE"));
            sm58Entity.setArfcfnam(t_arfcistate.getString("ARFCFNAM"));
            sm58Entity.setArfcreturn(t_arfcistate.getString("ARFCRETURN"));
            sm58Entity.setArfcuzeit(t_arfcistate.getString("ARFCUZEIT"));
            sm58Entity.setArfcdatum(t_arfcistate.getString("ARFCDATUM"));
            sm58Entity.setArfcuser(t_arfcistate.getString("ARFCUSER"));
            sm58Entity.setArfcretrys(t_arfcistate.getLong("ARFCRETRYS"));
            sm58Entity.setArfctcode(t_arfcistate.getString("ARFCTCODE"));
            sm58Entity.setArfcrhost(t_arfcistate.getString("ARFCRHOST"));
            sm58Entity.setArfcmsg(t_arfcistate.getString("ARFCMSG"));
            sm58Entity.setArfcreserv(t_arfcistate.getString("ARFCRESERV"));
            sm58Entity.setHash(t_arfcistate.getString("HASH"));
            sm58EntityRepository.save(sm58Entity);
        }
        String markdown = SappiMonitorServiceImpl.generateMarkdown("monitorSm58",
                exportList.getString("E_ERR_NUM").replaceAll(" ",""));
        //调用MessageService接口
        MarkdownMessage markdownMessage = new MarkdownMessage();
        markdownMessage.setUserid(environment.getProperty("sap.pi.monitor.sm58.touser"));
        markdownMessage.setMarkdown(markdown);
        JSONObject jsonObject = new JSONObject();
        if ("E".equals(exportList.getString("E_STATUS"))) {
            jsonObject = messageService.sendMarkdown(markdownMessage);
            jsonObject.put("errCode","-1");
            jsonObject.put("errMsg","系统运行出现" + exportList.getString("E_ERR_NUM") +"条错误");
        } else {
            jsonObject.put("errCode","0");
            jsonObject.put("errMsg","系统运行正常");
        }
        return jsonObject;
    }
}
```

[![复制代码](//assets.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

上面代码中，**粗体**部分是获取sap连接对象、接口参数赋值、接口调用和获取返回结果的主要代码；

## 4.编写相应的Controller代码

[![复制代码](//assets.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

```
@Api(tags = "SAPPI运行状态监控", description = "监控SAPPI运行状态")
@Controller
@RequestMapping("/monitor/sappi")
public class SappiMonitorController {
    @Autowired
    SappiMonitorService sappiMonitorService;

    @ApiOperation(value = "事务代码:SXI_MONITOR", notes = "请求方式:POST")
    @PostMapping("/sxi_monitor")
    @ResponseBody
    public JSONObject monitorSxi_monitor(@RequestBody(required = false) SappiSxi_monitor sappiSxi_monitor) throws Exception {
        return sappiMonitorService.monitorSxi_monitor(sappiSxi_monitor);
    }

    @ApiOperation(value = "事务代码:SM58", notes = "请求方式:POST")
    @PostMapping("/sm58")
    @ResponseBody
    public JSONObject monitorSm58(@RequestBody(required = false) SappiSm58 sappiSm58) throws Exception {
        return sappiMonitorService.monitorSm58(sappiSm58);
    }
}
```

[![复制代码](//assets.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

## 5.运行与测试

上面的代码中，只贴出了sapjco使用的主要部分，其中数据库的持久化部分和将sap接口调用结果发送到微信通知的部分都可以删减掉；

测试时，请求方式改为GET方式即可：

即\*\*@PostMapping("/sm58")\*\* 改为 **@GetMapping("/sm58")**

然后在浏览器或者用postman直接调用接口：**localhost:8080/monitor/sappi/sm58**

将会看到如下返回结果：

> {  
> 　　"invalidUser": "",  
> 　　"invalidTagList": [],  
> 　　"errCode": "-1",  
> 　　"errMsg": "系统运行出现1 条错误",  
> 　　"invalidPartyList": [],  
> 　　"invalidUserList": []  
> }

## 6、打包与部署

使用maven的package命令将项目打包成jar包，并上传到linux服务器/home/appuser/springboot-sapjco目录下面；

使用上面的docker命令部署并运行项目；

# 四、各操作系统sapjco文件下载：

链接: [https://pan.baidu.com/s/1-1Cxam_9Q6o0z_NqqOGvoA](https://pan.baidu.com/s/1-1Cxam_9Q6o0z_NqqOGvoA "下载sapjco3.jar") 提取码: v7c8
