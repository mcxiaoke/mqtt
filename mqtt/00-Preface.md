# MQTT协议3.1.1中文版

* [OASIS标准](https://www.oasis-open.org/committees/mqtt/) 2014年10月29日

## 规范链接 （Specification URIs）

### 当前版本（This version）：

<http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.doc> (Authoritative)

<http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html>

<http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.pdf>

### 以前的版本（Previous version）：

<http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/cos01/mqtt-v3.1.1-cos01.doc> (Authoritative)

<http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/cos01/mqtt-v3.1.1-cos01.html>

<http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/cos01/mqtt-v3.1.1-cos01.pdf>

### 最新版本（Latest version）：

<http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.doc> (Authoritative)

<http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.html>

<http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.pdf>

### 技术委员会（Technical Committee）：

[结构化信息标准促进组织MQTT技术委员会](https://www.oasis-open.org/committees/mqtt/)

#### 主席（Chairs）：

拉斐尔·J·科恩 (<raphael.cohn@stormmq.com>), 个人

理查德·J·科彭 (<coppen@uk.ibm.com>), [IBM](http://www.ibm.com/)

#### 编辑（Editors）：

安德鲁·班克斯 (<Andrew_Banks@uk.ibm.com>), [IBM](http://www.ibm.com/)

拉胡尔·吉普塔 (<rahul.gupta@us.ibm.com>), [IBM](http://www.ibm.com/)

### 相关文档（Related work）：

#### 本规范与此有关：

-   MQTT和NIST网络安全框架1.0版。 编辑是杰夫·布朗和路易·菲利普·拉穆勒。最新版本： <http://docs.oasis-open.org/mqtt/mqtt-nist-cybersecurity/v1.0/mqtt-nist-cybersecurity-v1.0.html>.

### 摘要 （Abstract）

MQTT是一个客户端服务端架构的发布/订阅模式的消息传输协议。它的设计思想是轻巧、开放、简单、规范，因此易于实现。这些特点使得它对很多场景来说都是很好的选择，包括受限的环境如机器与机器的通信（M2M）以及物联网环境（IoT），这些场景要求很小的代码封装或者网络带宽非常昂贵。

本协议运行在TCP/IP，或其它提供了有序、可靠、双向连接的网络连接上。它有以下特点：

- 使用发布/订阅消息模式，提供了一对多的消息分发和应用之间的解耦。
- 消息传输不需要知道负载内容。
- 提供三种等级的服务质量：.

	- “最多一次”，尽操作环境所能提供的最大努力分发消息。消息可能会丢失。例如，这个等级可用于环境传感器数据，单次的数据丢失没关系，因为不久之后会再次发送。
	- “至少一次”，保证消息可以到达，但是可能会重复。
	- “仅一次”，保证消息只到达一次。例如，这个等级可用在一个计费系统中，这里如果消息重复或丢失会导致不正确的收费。
- 很小的传输消耗和协议数据交换，最大限度减少网络流量
- 异常连接断开发生时，能通知到相关各方。

### 状态 （Status）

本文档最后由OASIS成员在上面标示的日期最终修订或批准。批准的级别也在上面列出了。如果要查看本文档最新的修订版请检查上面的 *最新版本* 位置。技术委员会产生的其它修订版和其它技术文档都列在这里：<https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=mqtt#technical> 。

技术委员会成员对本规范的评论应该发送到技术委员会的邮件列表。其他人应该发送评论到技术委员会的公共评论列表，方法是点击技术委员会网站的 [发送评论](https://www.oasis-open.org/committees/comments/index.php?wg_abbrev=mqtt) 按钮，网页地址是 <https://www.oasis-open.org/committees/mqtt/> 。

关于实现本规范必不可少的任何专利是否已公开，以及其它的专利许可条款相关的信息，请参考技术委员会网站的知识产权部分（(<https://www.oasis-open.org/committees/mqtt/ipr.php>）。

### 引用格式（Citation format）：

引用此规范时应该使用下面的引文格式：

**\[mqtt-v3.1.1\]**

*MQTT Version 3.1.1*. Edited by Andrew Banks and Rahul Gupta*.* 29 October 2014. OASIS Standard. <http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html>. Latest version: <http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.html>.

### 文档链接

- [MQTT协议3.1.1中文翻译项目](https://github.com/mcxiaoke/mqtt)
- [MQTT协议3.1.1中文版PDF](https://github.com/mcxiaoke/mqtt/blob/master/protocol/MQTT-3.1.1-CN.pdf)

## 修订记录

| **版 本** | **日 期**  | **发布说明**                               |
|-----------|------------|------------------------------------------|
| 1.0.0     | 2015-07-30 | 翻译全部文本，完成初步审校，公开发布第一版 |
| 1.0.1     | 2015-10-22 | 修订几处笔误，增补几处未翻译的文本         |
| 1.0.2     | 2016-02-04 | 转换为Markdown格式，发布更有好的在线阅读版本 |
| 1.0.3     | 2016-02-06 | 补充中英文对照，修正部分链接和格式 |

## 译者

- [GitHub](https://github.com/mcxiaoke)
- [Blog](http://blog.mcxiaoke.com/)
- [Email](mailto:mail@mcxiaoke.com)

## 目录

- [第一章 - 介绍](01-Introduction.md)
- [第二章 – MQTT控制报文格式](02-ControlPacketFormat.md)
- [第三章 – MQTT控制报文](03-ControlPackets.md)
- [第四章 – 操作行为](04-OperationalBehavior.md)
- [第五章 – 安全](05-Security.md)
- [第六章 – 使用WebSocket](06-WebSocket.md)
- [第七章 – 一致性目标](07-Conformance.md)
- [附录B - 强制性规范声明](08-AppendixB.md)


