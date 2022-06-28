## 安博通 www.abtnetworks.com
## 概述

Nmap是用来探测计算机网络上的主机和服务的一种安全扫描器，Nmap通过发送特制的数据包到目标主机，然后对返回数据包进行分析，可用于主机探测、端口扫描、版本检测以及系统检测。

## 使用说明

Nmap工具在平台上能正常执行的前置条件如下：  

1、配置Nmap实例，用于连接部署了Nmap扫描功能的服务器地址；

2、配置动作参数，用于设置应用动作的输入；  


## 配置实例

| **参数** |  **参数别名** | **描述** | **必填** | **示例** |
| --- | --- | --- | --- |  --- |
| url | 服务器网址 | 部署了Nmap扫描功能的服务器地址 | 是 | https://192.168.215.170:8068 |

## 配置动作

### 1.端口扫描

该动作主要用于扫描主机资产的各个端口的状态信息，目的是获取主机资产开放了哪些端口号，支持扫描一个主机的多个端口，也支持扫描多个主机的多个端口。

#### 参数

| **参数** | **参数别名** | **描述** | **必填** | **示例** |
| --- | --- | --- | --- |  --- |
| assets | 资产IP |待扫描资产,资产可输入单ip和ip段，多个用逗号隔开| 是 |127.0.0.1 <br/> 127.0.0.1-127.0.0.2 <br/> 127.0.0.1/24 |
| ports |  端口号 |待扫描的端口，支持输入单个端口、多个端口、端口范围，填写多个值用逗号分开 | 否 |80-90,100 |
| excludeAssets | 排除资产IP | 排除掉不想被扫描的主机资产，多用于从范围中排除某个或某些IP | 否 | 127.1.1.4 |
| rate | 速度 | 扫描速度，扫描速度越高，扫描结果准确率越低，可输入范围在100-1000000之间，默认值为5000 | 否 | 5000 |

#### 返回

| **资产** | **端口** |
| --- | --- |
| 127.0.0.1 | 22,33,44,55 | 
| 192.168.215.22 | 8623,7651 | 


#### 返回json字段说明
```json
{
  "schema": {
    "type": "JSON_ARRAY"
  },
  "status": "Success",
  "data": [{
    "ipAddress": "IP地址",
    "ports": "端口集合"
  }]
}
```

#### 返回示例
```json
{
    "message":"success",
    "data":[
        {
            "ipAddress":"192.168.215.158",
            "ports":[
                "33060",
                "8181",
                "22",
                "54001",
                "54002",
                "80",
                "5601",
                "54003"
            ]
        },
        {
            "ipAddress":"192.168.215.159",
            "ports":[
                "8030",
                "8901",
                "9300",
                "8096",
                "41775"
            ]
        }
    ],
    "schema":{
        "type":"JSON_ARRAY"
    },
    "debugOutput":"",
    "status":"Success"
}

```


### 2.端口服务扫描

该动作主要用于扫描主机资产的各个端口的应用服务信息，目的是获取主机资产的各个端口对应的协议和服务数据，支持扫描一个主机的多个端口，也支持扫描多个主机的多个端口。

#### 参数

| **参数** | **参数别名** | **描述** | **必填** | **示例** |
| --- | --- | --- | --- |  --- |
| assets | 资产IP |待扫描资产,资产可输入单ip和ip段，多个用逗号隔开| 是 |192.168.215.158,192.168.215.159 <br/> 127.0.0.1-127.0.0.2 <br/> 127.0.0.1/24 |
| ports |  端口号 |待扫描的端口，支持输入单个端口、多个端口、端口范围，填写多个值用逗号分开 | 否 |80-90,100 |


#### 返回

<table>
    <thead>
        <tr>
            <th>资产</th>
            <th>Mac</th>
            <th>名称</th>
            <th>操作系统</th>
            <th>状态</th>
        </tr>
    </thead>
    <tbody>
         <tr>
            <td>192.168.215.158</td>
            <td>52-54-00-1f-ac-a4</td>
            <td>主机A</td>
            <td>Linux 3.2 - 4.9</td>
            <td>up</td>
        </tr>
        <tr>
            <td colspan="5">
                <table>
                    <thead>
                        <tr>
                            <th>端口</th>
                            <th>服务</th>
                            <th>应用</th>
                            <th>版本</th>
                        </tr>
                    </thead>
                    <tbody>
                         <tr>
                            <td>22</td>
                            <td>ssh</td>
                            <td>OpenSSH</td>
                            <td>7.4</td>
                        </tr>
                         <tr>
                            <td>80</td>
                            <td>http</td>
                            <td>nginx</td>
                            <td>1.20.1</td>
                        </tr>
                        <tr>
                            <td>33060</td>
                            <td>mysql</td>
                            <td>MySQL</td>
                            <td>5.7.36</td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table>

#### 返回json字段说明
```json
{
  "schema": {
    "type": "JSON_ARRAY"
  },
  "status": "Success",
  "data": [{
    "ipAddress": "ip地址",
    "macAddress": "MAC地址",
    "macVendor": "供应商",
    "status": "状态",
    "name": "资产名称",
    "os": "操作系统",
    "cpe": "通用平台枚举项",
    "portServiceList": [{
      "ipAddress": "ip地址",
      "protocol": "协议",
      "port": "端口",
      "status": "状态",
      "reason": "reason",
      "reasonTTL": "reasonTTL",
      "name": "服务名称",
      "product": "服务应用",
      "extraInfo": "附属信息",
      "cpe": "通用平台枚举项",
      "version": "版本",
      "frigen": "服务指纹",
      "memo": "备注"
    }],
    "vulnInfoList": "漏洞集合"
  }]
}
```


#### 返回示例
```json
{
    "message":"success",
    "data":[
        {
            "ipAddress":"192.168.215.159",
            "macAddress":"00:50:56:B8:8E:09",
            "macVendor":null,
            "status":"up",
            "name":"\n",
            "os":"ASUS RT-N56U WAP (Linux 3.4)",
            "cpe":null,
            "portServiceList":[
                {
                    "ipAddress":"192.168.215.159",
                    "protocol":"tcp",
                    "port":"80",
                    "status":"open",
                    "reason":"syn-ack",
                    "reasonTTL":"63",
                    "name":"http",
                    "product":"nginx",
                    "extraInfo":null,
                    "cpe":"cpe:/a:igor_sysoev:nginx:1.20.1",
                    "version":"1.20.1",
                    "frigen":null,
                    "memo":null
                },
                {
                    "ipAddress":"192.168.215.159",
                    "protocol":"tcp",
                    "port":"33060",
                    "status":"open",
                    "reason":"syn-ack",
                    "reasonTTL":"63",
                    "name":"mysql",
                    "product":"MySQL",
                    "extraInfo":null,
                    "cpe":"cpe:/a:mysql:mysql:5.7.36",
                    "version":"5.7.36",
                    "frigen":null,
                    "memo":null
                }
            ]
        }
    ],
    "schema":{
        "type":"JSON_ARRAY"
    },
    "status":"Success"
}

```

### 3.资产扫描

该动作主要用于扫描主机资产的详情信息，包括主机资产的基本信息如操作系统类型、版本号、供应商、MAC地址等，端口信息、协议、应用服务等。支持扫描一个主机的多个端口，也支持扫描多个主机的多个端口。

资产扫描是端口扫描+端口服务扫描的组合; 第一步就是利用端口扫描工具先把主机上的端口过滤一遍，得到一个存活的端口集合，第二步是利用端口服务扫描工具对这些存活的端口进行服务探测。

#### 参数

| **参数** | **参数别名** | **描述** | **必填** | **示例** |
| --- | --- | --- | --- |  --- |
| assets | 资产IP |待扫描资产,资产可输入单ip和ip段，多个用逗号隔开| 是 |127.0.0.1 <br/> 127.0.0.1-127.0.0.2 <br/> 127.0.0.1/24 |
| ports |  端口号 |待扫描的端口，支持输入单个端口、多个端口、端口范围，填写多个值用逗号分开 | 否 |80-90,100 |
| excludeAssets | 排除资产IP | 排除掉不想被扫描的主机资产，多用于从范围中排除某个或某些IP | 否 | 127.1.1.4 |
| rate | 速度 | 扫描速度，扫描速度越高，扫描结果准确率越低，可输入范围在100-1000000之间，默认值为5000 | 否 | 5000 |


#### 返回

<table>
    <thead>
        <tr>
            <th>资产</th>
            <th>Mac</th>
            <th>名称</th>
            <th>操作系统</th>
            <th>状态</th>
        </tr>
    </thead>
    <tbody>
         <tr>
            <td>192.168.215.158</td>
            <td>52-54-00-1f-ac-a4</td>
            <td>主机A</td>
            <td>Linux 3.2 - 4.9</td>
            <td>up</td>
        </tr>
        <tr>
            <td colspan="5">
                <table>
                    <thead>
                        <tr>
                            <th>端口</th>
                            <th>服务</th>
                            <th>应用</th>
                            <th>版本</th>
                        </tr>
                    </thead>
                    <tbody>
                         <tr>
                            <td>22</td>
                            <td>ssh</td>
                            <td>OpenSSH</td>
                            <td>7.4</td>
                        </tr>
                         <tr>
                            <td>80</td>
                            <td>http</td>
                            <td>nginx</td>
                            <td>1.20.1</td>
                        </tr>
                        <tr>
                            <td>33060</td>
                            <td>mysql</td>
                            <td>MySQL</td>
                            <td>5.7.36</td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table>

#### 返回json字段说明
```json
{
  "schema": {
    "type": "JSON_ARRAY"
  },
  "status": "Success",
  "data": [{
    "ipAddress": "ip地址",
    "macAddress": "MAC地址",
    "macVendor": "供应商",
    "status": "状态",
    "name": "资产名称",
    "os": "操作系统",
    "cpe": "通用平台枚举项",
    "portServiceList": [{
      "ipAddress": "ip地址",
      "protocol": "协议",
      "port": "端口",
      "status": "状态",
      "reason": "reason",
      "reasonTTL": "reasonTTL",
      "name": "服务名称",
      "product": "服务应用",
      "extraInfo": "附属信息",
      "cpe": "通用平台枚举项",
      "version": "版本",
      "frigen": "服务指纹",
      "memo": "备注"
    }],
    "vulnInfoList": "漏洞集合"
  }]
}
```


#### 返回示例
```json
{
    "message":"success",
    "data":[
        {
            "ipAddress":"192.168.215.159",
            "macAddress":"00:50:56:B8:8E:09",
            "macVendor":null,
            "status":"up",
            "name":"\n",
            "os":"ASUS RT-N56U WAP (Linux 3.4)",
            "cpe":null,
            "portServiceList":[
                {
                    "ipAddress":"192.168.215.159",
                    "protocol":"tcp",
                    "port":"80",
                    "status":"open",
                    "reason":"syn-ack",
                    "reasonTTL":"63",
                    "name":"http",
                    "product":"nginx",
                    "extraInfo":null,
                    "cpe":"cpe:/a:igor_sysoev:nginx:1.20.1",
                    "version":"1.20.1",
                    "frigen":null,
                    "memo":null
                },
                {
                    "ipAddress":"192.168.215.159",
                    "protocol":"tcp",
                    "port":"33060",
                    "status":"open",
                    "reason":"syn-ack",
                    "reasonTTL":"63",
                    "name":"mysql",
                    "product":"MySQL",
                    "extraInfo":null,
                    "cpe":"cpe:/a:mysql:mysql:5.7.36",
                    "version":"5.7.36",
                    "frigen":null,
                    "memo":null
                }
            ]
        }
    ],
    "schema":{
        "type":"JSON_ARRAY"
    },
    "status":"Success"
}

```
