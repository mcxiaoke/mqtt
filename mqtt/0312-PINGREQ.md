## 3.12 PINGREQ – 心跳请求

客户端发送PINGREQ报文给服务端的。用于：

1.  在没有任何其它控制报文从客户端发给服务的时，告知服务端客户端还活着。
2.  请求服务端发送 响应确认它还活着。
3.  使用网络以确认网络连接没有断开。

保持连接（Keep Alive）处理中用到这个报文，详细信息请查看 3.1.2.10节。

### 3.12.1 固定报头

##### 图例 3.33 – PINGREQ报文固定报头

| **Bit** | **7**                 | **6**  | **5** | **4** | **3** | **2** | **1** | **0** |
|---------|-----------------------|--------|-------|-------|-------|-------|-------|-------|
| byte 1  | MQTT控制报文类型 (12) | 保留位 |
|         | 1                     | 1      | 0     | 0     | 0     | 0     | 0     | 0     |
| byte 2  | 剩余长度 (0)          |
|         | 0                     | 0      | 0     | 0     | 0     | 0     | 0     | 0     |

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
     <td colspan="4" align="center">MQTT控制报文类型 (12)</td>
     <td colspan="4" align="center">保留位</td>
   </tr>
   <tr>
       <td></td>
       <td align="center">1</td>
       <td align="center">1</td>
       <td align="center">0</td>
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
 
### 3.12.2 可变报头

PINGREQ报文没有可变报头。

### 3.12.3 有效载荷

PINGREQ报文没有有效载荷。

### 3.12.4 响应

服务端**必须**发送 PINGRESP报文响应客户端的PINGREQ报文 \[MQTT-3.12.4-1\]。


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


