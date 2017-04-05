## 3.14 DISCONNECT –断开连接

DISCONNECT报文是客户端发给服务端的最后一个控制报文。表示客户端正常断开连接。

### 3.14.1 固定报头

##### 图例 3.35 – DISCONNECT报文固定报头

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
     <td colspan="4" align="center">MQTT控制报文类型 (14)</td>
     <td colspan="4" align="center">保留位</td>
   </tr>
   <tr>
       <td></td>
       <td align="center">1</td>
       <td align="center">1</td>
       <td align="center">1</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
     </tr>
   <tr>
     <td>byte 2</td>
     <td colspan="8" align="center">剩余长度 (0)</td>
   </tr>
   <tr>
       <td></td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
     </tr>
 </table>

服务端**必须**验证所有的保留位都被设置为0，如果它们不为0**必须**断开连接 \[MQTT-3.14.1-1\]。

### 3.14.2 可变报头

DISCONNECT报文没有可变报头。

### 3.14.3 有效载荷

DISCONNECT报文没有有效载荷。

### 3.14.4 响应

客户端发送DISCONNECT报文之后：

-   **必须**关闭网络连接 \[MQTT-3.14.4-1\]。
-   **不能**通过那个网络连接再发送任何控制报文 \[MQTT-3.14.4-2\]。

服务端在收到DISCONNECT报文时：

-   **必须**丢弃任何与当前连接关联的未发布的遗嘱消息，具体描述见 3.1.2.5节 \[MQTT-3.14.4-3\]。
-   **应该**关闭网络连接，如果客户端 还没有这么做。


## 第三章目录 MQTT控制报文

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


