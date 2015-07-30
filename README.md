# MQTT协议3.1.1版

## 中文翻译

文档|连接
----|----
英文版 HTML：| [MQTT Version 3.1.1](http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.html)
英文版 PDF：| [MQTT Version 3.1.1](http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.pdf)
中文版 HTML：| [MQTT协议3.1.1中文版](http://mcxiaoke.github.io/mqtt/protocol/MQTT-3.1.1-CN.html)
中文版 PDF：| [MQTT协议3.1.1中文版](protocol/MQTT-3.1.1-CN.pdf)

## MQTT概述

```
MQTT是一个客户端服务端架构的发布/订阅模式的消息传输协议。它的设计思想是轻巧、开放、
简单、规范，因此易于实现。这些特点使得它对很多场景来说都是很好的选择，包括受限的环境如
机器与机器的通信（M2M）以及物联网环境（IoT），这些场景要求很小的代码封装或者网络带宽
非常昂贵。
```

本协议运行在TCP/IP或其它提供了有序、可靠、双向连接的网络连接上，特点：

* 使用发布/订阅消息模式，提供了一对多的消息分发和应用之间的解耦。
* 消息传输不需要知道负载内容。
* 提供三种等级的服务质量：.
	- "最多一次"，尽操作环境所能提供的最大努力分发消息。消息可能会丢失。例如，这个
等级可用于环境传感器数据，单次的数据丢失没关系，因为不久之后会再次发送。
	- "至少一次"，保证消息可以到达，但是可能会重复。
	- "仅一次"，保证消息只到达一次。例如，这个等级可用在一个计费系统中，这里如果消息重复或丢失会导致不正确的收费。
* 很小的传输消耗和协议数据交换，最大限度减少网络流量
* 异常连接断开发生时，能通知到相关各方。

------
## 关于作者

### 联系方式
* Blog: <http://blog.mcxiaoke.com>
* Github: <https://github.com/mcxiaoke>
* Email: [mail@mcxiaoke.com](mailto:mail@mcxiaoke.com)

### 开源项目

* Rx文档中文翻译: <https://github.com/mcxiaoke/RxDocs>
* Next公共组件库: <https://github.com/mcxiaoke/Android-Next>
* Gradle多渠道打包工具: <https://github.com/mcxiaoke/gradle-packer-plugin>
* 蘑菇饭App: <https://github.com/mcxiaoke/minicat>
* 饭否客户端: <https://github.com/mcxiaoke/fanfouapp-opensource>
* Volley镜像: <https://github.com/mcxiaoke/android-volley>