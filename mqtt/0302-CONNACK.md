## 3.2 CONNACK – 确认连接请求


服务端发送CONNACK报文响应从客户端收到的CONNECT报文。服务端发送给客户端的第一个报文**必须**是CONNACK \[MQTT-3.2.0-1\]。

如果客户端在合理的时间内没有收到服务端的CONNACK报文，客户端**应该**关闭网络连接。*合理* 的时间取决于应用的类型和通信基础设施。

### 3.2.1 固定报头

固定报头的格式见 [图例 3.8 – CONNACK 报文固定报头](#_Figure_3.8_–) 的描述。

##### 图例 3.8 – CONNACK 报文固定报头

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
       <td colspan="4" align="center">MQTT报文类型 (2)</td>
       <td colspan="4" align="center">Reserved 保留位</td>
     </tr>
     <tr>
       <td></td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">1</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
     </tr>
     <tr>
       <td>byte 2...</td>
       <td colspan="8" align="center">剩余长度 (2)</td>
     </tr>
     <tr>
       <td></td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">1</td>
       <td align="center">0</td>
     </tr>
   </table>

**剩余长度字段**

表示可变报头的长度。对于CONNACK报文这个值等于2。

### 3.2.2 可变报头

可变报头的格式见 [图例 3.9 –CONNACK报文可变报头](#_图例_3.9_–CONNACK报文可变报头) 的描述。

##### 图例 3.9 –CONNACK报文可变报头

|              | **描述**        | **7**          | **6** | **5** | **4** | **3** | **2** | **1** | **0** |
|--------------|-----------------|----------------|-------|-------|-------|-------|-------|-------|-------|
| 连接确认标志 | Reserved 保留位 | SP<sup>1</sup> |
| byte 1       |                 | 0              | 0     | 0     | 0     | 0     | 0     | 0     | X     |
| 连接返回码   |
| byte 2       |                 | X              | X     | X     | X     | X     | X     | X     | X     |

  <table style="text-align:center">
     <tr>
      <td></td>
      <td align="center"><strong>描述</strong></td>
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
       <td colspan="2">连接确认标志</td>
       <td colspan="7" align="center">Reserved 保留位</td>
       <td align="center">SP<sup>1</sup></td>
     </tr>
     <tr>
       <td align="center">byte 1</td>
       <td></td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">0</td>
       <td align="center">X</td>
     </tr>
     <tr>
       <td colspan="10">连接返回码</td>
     </tr>
     <tr>
       <td align="center">byte 2</td>
       <td></td>
       <td align="center">X</td>
       <td align="center">X</td>
       <td align="center">X</td>
       <td align="center">X</td>
       <td align="center">X</td>
       <td align="center">X</td>
       <td align="center">X</td>
       <td align="center">X</td>
     </tr>
   </table>

#### 连接确认标志 Connect Acknowledge Flags

第1个字节是 *连接确认标志*，位7-1是保留位且**必须**设置为0。 
第0 (SP)位 是当前会话（Session Present）标志。

#### 当前会话 Session Present

**位置：**连接确认标志的第0位。

如果服务端收到清理会话（CleanSession）标志为1的连接，除了将CONNACK报文中的返回码设置为0之外，还**必须**将CONNACK报文中的当前会话设置（Session Present）标志为0 \[MQTT-3.2.2-1\]。

如果服务端收到一个CleanSession为0的连接，当前会话标志的值取决于服务端是否已经保存了ClientId对应客户端的会话状态。如果服务端已经保存了会话状态，它**必须**将CONNACK报文中的当前会话标志设置为1 \[MQTT-3.2.2-2\]。如果服务端没有已保存的会话状态，它**必须**将CONNACK报文中的当前会话设置为0。还需要将CONNACK报文中的返回码设置为0 \[MQTT-3.2.2-3\]。

当前会话标志使服务端和客户端在是否有已存储的会话状态上保持一致。

一旦完成了会话的初始化设置，已经保存会话状态的客户端将期望服务端维持它存储的会话状态。如果客户端从服务端收到的当前的值与预期的不同，客户端可以选择继续这个会话或者断开连接。客户端可以丢弃客户端和服务端之间的会话状态，方法是，断开连接，将清理会话标志设置为1，再次连接，然后再次断开连接。

如果服务端发送了一个包含非零返回码的CONNACK报文，它**必须**将当前会话标志设置为0 \[MQTT-3.2.2-4\]。

#### 连接返回码 Connect Return code

**位置：**可变报头的第2个字节。

连接返回码字段使用一个字节的无符号值，在 [表格 3.1 –连接返回码的值](#_表格_3.1_–连接返回码的值) 中列出。如果服务端收到一个合法的CONNECT报文，但出于某些原因无法处理它，服务端应该尝试发送一个包含非零返回码（表格中的某一个）的CONNACK报文。如果服务端发送了一个包含非零返回码的CONNACK报文，那么它**必须**关闭网络连接 \[MQTT-3.2.2-5\].。

##### 表格 3.1 –连接返回码的值

| **值** | **返回码响应**                       | **描述**                                          |
|--------|--------------------------------------|---------------------------------------------------|
| 0      | 0x00连接已接受                       | 连接已被服务端接受                                |
| 1      | 0x01连接已拒绝，不支持的协议版本     | 服务端不支持客户端请求的MQTT协议级别              |
| 2      | 0x02连接已拒绝，不合格的客户端标识符 | 客户端标识符是正确的UTF-8编码，但服务端不允许使用 |
| 3      | 0x03连接已拒绝，服务端不可用         | 网络连接已建立，但MQTT服务不可用                  |
| 4      | 0x04连接已拒绝，无效的用户名或密码   | 用户名或密码的数据格式无效                        |
| 5      | 0x05连接已拒绝，未授权               | 客户端未被授权连接到此服务器                      |
| 6-255  |                                      | 保留                                              |

如果认为上表中的所有连接返回码都不太合适，那么服务端**必须**关闭网络连接，不需要发送CONNACK报文 \[MQTT-3.2.2-6\]。

### 3.2.3 有效载荷

CONNACK报文没有有效载荷。


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


