## 3.9 SUBACK – 订阅确认

服务端发送SUBACK报文给客户端，用于确认它已收到并且正在处理SUBSCRIBE报文。

SUBACK报文包含一个返回码清单，它们指定了SUBSCRIBE请求的每个订阅被授予的最大QoS等级。

### 3.9.1 固定报头

##### 图例 3.24 – SUBACK报文固定报头

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
     <td colspan="4" align="center">MQTT控制报文类型 (9)</td>
     <td colspan="4" align="center">保留位</td>
   </tr>
   <tr>
       <td></td>
       <td align="center">1</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">1</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
     </tr>
   <tr>
     <td>byte 2</td>
     <td colspan="8" align="center">剩余长度</td>
   </tr>
 </table>
 
**剩余长度字段**

等于可变报头的长度加上有效载荷的长度。

### 3.9.2 可变报头

可变报头包含等待确认的SUBSCRIBE报文的报文标识符。[图例 3.25 – SUBACK报文可变报头](#_图例_3.25_–) 描述了可变报头的格式。

##### 图例 3.25 – SUBACK报文可变报头

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
 
### 3.9.3 有效载荷

有效载荷包含一个返回码清单。每个返回码对应等待确认的SUBSCRIBE报文中的一个主题过滤器。返回码的顺序**必须**和SUBSCRIBE报文中主题过滤器的顺序相同 \[MQTT-3.9.3-1\]。

[图例 3.26 – SUBACK报文有效载荷格式](#_Figure_3.26_-) 描述了有效载荷中单字节编码的返回码字段。

##### 图例 3.26 – SUBACK报文有效载荷格式

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
     <td></td>
     <td colspan="8" align="center">返回码</td>
   </tr>
    <tr>
       <td>byte 1</td>
       <td align="center">X</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">X</td>
       <td align="center">X</td>
     </tr>
 </table>
 
允许的返回码值：

- 0x00 - 最大QoS 0
- 0x01 - 成功 – 最大QoS 1
- 0x02 - 成功 – 最大 QoS 2
- 0x80 - Failure  失败

0x00, 0x01, 0x02, 0x80之外的SUBACK返回码是保留的，**不能**使用\[MQTT-3.9.3-2\]。

#### 有效载荷非规范示例

> [图例 3.27 -有效载荷字节格式非规范示例](#_Figure_3.27_-) 展示了在 [表格 3.6 -有效载荷非规范示例](#_Table_3.5_-) 简要描述的SUBACK报文的有效载荷。

##### 表格 3.6 -有效载荷非规范示例

| Success - Maximum QoS 0  | 0   |
|--------------------------|-----|
| Success - Maximum QoS 2  | 2   |
| Failure                  | 128 |

##### 图例 3.27 -有效载荷字节格式非规范示例

|        | **描述**                 | **7** | **6** | **5** | **4** | **3** | **2** | **1** | **0** |
|--------|--------------------------|-------|-------|-------|-------|-------|-------|-------|-------|
| byte 1 | Success - Maximum QoS 0  | 0     | 0     | 0     | 0     | 0     | 0     | 0     | 0     |
| byte 2 | Success - Maximum QoS 2  | 0     | 0     | 0     | 0     | 0     | 0     | 1     | 0     |
| byte 3 | Failure                  | 1     | 0     | 0     | 0     | 0     | 0     | 0     | 0     |


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


