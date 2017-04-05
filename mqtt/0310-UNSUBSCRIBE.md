## 3.10 UNSUBSCRIBE –取消订阅

客户端发送UNSUBSCRIBE报文给服务端，用于取消订阅主题。

### 3.10.1 固定报头

##### 图例 3.28 – UNSUBSCRIBE报文固定报头

<table style="text-align:center">
   <tr>
     <td align="center"><strong>Bit</strong></td>
     <td align="center"><strong>7</strong></td>
     <td align="center"><strong>6</strong></td>
     <td align="center"><strong>5</strong></td>
     <td align="center"><strong>4</strong></td>
     <td align="center"><strong>3</strong></td>
     <td align="center"><strong>2</strong></td>
     <td align="center"><strong>1</strong></td>
     <td align="center"><strong>0</strong></td>
   </tr>
   <tr>
     <td>byte 1</td>
     <td colspan="4" align="center">MQTT控制报文类型 (10)</td>
     <td colspan="4" align="center">保留位</td>
   </tr>
   <tr>
       <td></td>
       <td align="center">1</td>
       <td align="center">0</td>
       <td align="center">1</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">1</td>
       <td align="center">0</td>
     </tr>
   <tr>
     <td>byte 2</td>
     <td colspan="8" align="center">剩余长度</td>
   </tr>
 </table>

UNSUBSCRIBE报文固定报头的第3,2,1,0位是保留位且**必须**分别设置为0,0,1,0。服务端**必须**认为任何其它的值都是不合法的并关闭网络连接 \[MQTT-3.10.1-1\]。

**剩余长度字段**

等于可变报头的长度加上有效载荷的长度。

### 3.10.2 可变报头

可变报头包含一个报文标识符。2.3.1节提供了有关报文标识符的更多信息。

##### 图例 3.29 – UNSUBSCRIBE报文可变报头

<table style="text-align:center">
   <tr>
     <td align="center"><strong>Bit</strong></td>
     <td align="center"><strong>7</strong></td>
     <td align="center"><strong>6</strong></td>
     <td align="center"><strong>5</strong></td>
     <td align="center"><strong>4</strong></td>
     <td align="center"><strong>3</strong></td>
     <td align="center"><strong>2</strong></td>
     <td align="center"><strong>1</strong></td>
     <td align="center"><strong>0</strong></td>
   </tr>
   <tr>
     <td>byte 1</td>
     <td colspan="8" align="center">报文标识符 MSB</td>
   </tr>
   <tr>
     <td>byte 2</td>
     <td colspan="8" align="center">报文标识符 LSB</td>
   </tr>
 </table>

### 3.10.3 有效载荷

UNSUBSCRIBE报文的有效载荷包含客户端想要取消订阅的主题过滤器列表。UNSUBSCRIBE报文中的主题过滤器**必须**是连续打包的、按照1.5.3节定义的UTF-8编码字符串 \[MQTT-3.10.3-1\]。

UNSUBSCRIBE报文的有效载荷**必须**至少包含一个消息过滤器。没有有效载荷的UNSUBSCRIBE报文是违反协议的 \[MQTT-3.10.3-2\]。有关错误处理的更多信息请查看4.8节。

#### 有效载荷非规范示例

> [图例 3.30 -有效载荷字节格式非规范示例](#_Figure_3.30_-) 展示了 [表格 3.7 -有效载荷非规范示例](#_Table3.6_-_Payload) 简要描述的UNSUBSCRIBE报文的有效载荷。

##### 表格 3.7 -有效载荷非规范示例

| 主题过滤器 | “a/b” |
|------------|-------|
| 主题过滤器 | “c/d” |

##### 图例 3.30 -有效载荷字节格式非规范示例

|            | **描述**       | **7** | **6** | **5** | **4** | **3** | **2** | **1** | **0** |
|------------|----------------|-------|-------|-------|-------|-------|-------|-------|-------|
| 主题过滤器 |
| byte 1     | Length MSB (0) | 0     | 0     | 0     | 0     | 0     | 0     | 0     | 0     |
| byte 2     | Length LSB (3) | 0     | 0     | 0     | 0     | 0     | 0     | 1     | 1     |
| byte 3     | ‘a’ (0x61)     | 0     | 1     | 1     | 0     | 0     | 0     | 0     | 1     |
| byte 4     | ‘/’ (0x2F)     | 0     | 0     | 1     | 0     | 1     | 1     | 1     | 1     |
| byte 5     | ‘b’ (0x62)     | 0     | 1     | 1     | 0     | 0     | 0     | 1     | 0     |
| 主题过滤器 |
| byte 6     | Length MSB (0) | 0     | 0     | 0     | 0     | 0     | 0     | 0     | 0     |
| byte 7     | Length LSB (3) | 0     | 0     | 0     | 0     | 0     | 0     | 1     | 1     |
| byte 8     | ‘c’ (0x63)     | 0     | 1     | 1     | 0     | 0     | 0     | 1     | 1     |
| byte 9     | ‘/’ (0x2F)     | 0     | 0     | 1     | 0     | 1     | 1     | 1     | 1     |
| byte 10    | ‘d’ (0x64)     | 0     | 1     | 1     | 0     | 0     | 1     | 0     | 0     |

### 3.10.4 响应

UNSUBSCRIBE报文提供的主题过滤器（无论是否包含通配符）**必须**与服务端持有的这个客户端的当前主题过滤器集合逐个字符比较。如果有任何过滤器完全匹配，那么它（服务端）自己的订阅将被删除，否则不会有进一步的处理 \[MQTT-3.10.4-1\]。

如果服务端删除了一个订阅：

-   它**必须**停止分发任何新消息给这个客户端 \[MQTT-3.10.4-2\]。
-   它**必须**完成分发任何已经开始往客户端发送的QoS 1和QoS 2的消息 \[MQTT-3.10.4-3\]。
-   它**可以**继续发送任何现存的准备分发给客户端的缓存消息。

服务端**必须**发送UNSUBACK报文响应客户端的UNSUBSCRIBE请求。UNSUBACK报文**必须**包含和UNSUBSCRIBE报文相同的报文标识符 \[MQTT-3.10.4-4\]。即使没有删除任何主题订阅，服务端也**必须**发送一个UNSUBACK响应 \[MQTT-3.10.4-5\]。

如果服务端收到包含多个主题过滤器的UNSUBSCRIBE报文，它**必须**如同收到了一系列的多个UNSUBSCRIBE报文一样处理那个报文，除了将它们的响应合并到一个单独的UNSUBACK报文外。 \[MQTT-3.10.4-6\]。


### 第三章目录 MQTT控制报文

- [3.0 Contents – MQTT控制报文](03-ControlPackets.md)
- [3.1 CONNECT – 连接服务端](0301-CONNECT.md)
- [3.2 CONNACK – 确认连接请求](0302-CONNACK.md)
- [3.3 PUBLISH – 发布消息](0303-PUBLISH.md)
- [3.4 PUBACK –发布确认](0304-PUBACK.md)
- [3.5 PUBREC – 发布收到（QoS 2，第一步）](0305-PUBREC.md)
- [3.6 PUBREL – 发布释放（QoS 2，第二步）](0306-PUBREL.md)
- [3.7 PUBCOMP – 发布完成（QoS 2，第三步）](0307-PUBCOMP.md)
- [3.8 SUBSCRIBE - 订阅主题](0308-SUBSCRIBE.md)
- [3.9 SUBACK – 订阅确认](0309-SUBACK.md)
- [3.10 UNSUBSCRIBE –取消订阅](0310-UNSUBSCRIBE.md)
- [3.11 UNSUBACK – 取消订阅确认](0311-UNSUBACK.md)
- [3.12 PINGREQ – 心跳请求](0312-PINGREQ.md)
- [3.13 PINGRESP – 心跳响应](0313-PINGRESP.md)
- [3.14 DISCONNECT –断开连接](0314-DISCONNECT.md)

### 项目主页

- [MQTT协议中文版](https://github.com/mcxiaoke/mqtt)


