# 第二章 MQTT控制报文格式 MQTT Control Packet format

## 目录

- [第一章 - 介绍](01-Introduction.md)
- [第二章 – MQTT控制报文格式](02-ControlPacketFormat.md)
- [第三章 – MQTT控制报文](03-ControlPackets.md)
- [第四章 – 操作行为](04-OperationalBehavior.md)
- [第五章 – 安全](05-Security.md)
- [第六章 – 使用WebSocket](06-WebSocket.md)
- [第七章 – 一致性目标](07-Conformance.md)
- [附录B - 强制性规范声明](08-AppendixB.md)

## 2.1 MQTT控制报文的结构 Structure of an MQTT Control Packet

MQTT协议通过交换预定义的MQTT控制报文来通信。这一节描述这些报文的格式。

MQTT控制报文由三部分组成，按照 [图例 2.1 –MQTT控制报文的结构](#_Figure_2.1_-) 描述的顺序：

##### 图例 2.1 –MQTT控制报文的结构

| Fixed header | 固定报头，所有控制报文都包含  |
|-----------------|---------------------------|
| Variable header | 可变报头，部分控制报文包含 |
| Payload | 有效载荷，部分控制报文包含         |

## 2.2 固定报头 Fixed header

每个MQTT控制报文都包含一个固定报头。[图例 2.2 -固定报头的格式](#_Figure_2.2_-) 描述了固定报头的格式。

##### 图例 2.2 -固定报头的格式

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
    <td colspan="4" align="center">MQTT控制报文的类型</td>
    <td colspan="4" align="center">用于指定控制报文类型的标志位</td>
  </tr>
  <tr>
    <td>byte 2...</td>
    <td colspan="8" align="center">剩余长度</td>
  </tr>
</table>

### 2.2.1 MQTT控制报文的类型 MQTT Control Packet type

**位置：**第1个字节，二进制位7-4。

表示为4位无符号值，这些值的定义见 [表格 2.1 -控制报文的类型](#_Table_2.1_-)

##### 表格 2.1 -控制报文的类型 

| **名字**    | **值** | **报文流动方向** | **描述**                            |
|-------------|--------|------------------|-------------------------------------|
| Reserved    | 0      | 禁止             | 保留                                
| CONNECT     | 1      | 客户端到服务端   | 客户端请求连接服务端                
| CONNACK     | 2      | 服务端到客户端   | 连接报文确认                        
| PUBLISH     | 3      | 两个方向都允许   | 发布消息                            
| PUBACK      | 4      | 两个方向都允许   | QoS 1消息发布收到确认               
| PUBREC      | 5      | 两个方向都允许   | 发布收到（保证交付第一步）          |
| PUBREL      | 6      | 两个方向都允许   | 发布释放（保证交付第二步）          |
| PUBCOMP     | 7      | 两个方向都允许   | QoS 2消息发布完成（保证交互第三步） |
| SUBSCRIBE   | 8      | 客户端到服务端   | 客户端订阅请求                      
| SUBACK      | 9      | 服务端到客户端   | 订阅请求报文确认                    
| UNSUBSCRIBE | 10     | 客户端到服务端   | 客户端取消订阅请求                  
| UNSUBACK    | 11     | 服务端到客户端   | 取消订阅报文确认                    
| PINGREQ     | 12     | 客户端到服务端   | 心跳请求                            
| PINGRESP    | 13     | 服务端到客户端   | 心跳响应                            
| DISCONNECT  | 14     | 客户端到服务端   | 客户端断开连接                      
| Reserved    | 15     | 禁止             | 保留                                

### 2.2.2 标志 Flags

固定报头第1个字节的剩余的4位 \[3-0\]包含每个MQTT控制报文类型特定的标志，见 [表格 2.2 -标志位](#表格-2.2--标志位)。表格 2.2中任何标记为“保留”的标志位，都是保留给以后使用的，**必须**设置为表格中列出的值 \[MQTT-2.2.2-1\]。如果收到非法的标志，接收者**必须**关闭网络连接。有关错误处理的详细信息见 4.8节 \[MQTT-2.2.2-2\]。

#####  表格 2.2 - 标志位 Flag Bits

| **控制报文** | **固定报头标志**   | **Bit 3**       | **Bit 2**       | **Bit 1**       | **Bit 0**          |
|--------------|--------------------|-----------------|-----------------|-----------------|--------------------|
| CONNECT      | Reserved           | 0               | 0               | 0               | 0                  |
| CONNACK      | Reserved           | 0               | 0               | 0               | 0                  |
| PUBLISH      | Used in MQTT 3.1.1 | DUP<sup>1</sup> | QoS<sup>2</sup> | QoS<sup>2</sup> | RETAIN<sup>3</sup> |
| PUBACK       | Reserved           | 0               | 0               | 0               | 0                  |
| PUBREC       | Reserved           | 0               | 0               | 0               | 0                  |
| PUBREL       | Reserved           | 0               | 0               | 1               | 0                  |
| PUBCOMP      | Reserved           | 0               | 0               | 0               | 0                  |
| SUBSCRIBE    | Reserved           | 0               | 0               | 1               | 0                  |
| SUBACK       | Reserved           | 0               | 0               | 0               | 0                  |
| UNSUBSCRIBE  | Reserved           | 0               | 0               | 1               | 0                  |
| UNSUBACK     | Reserved           | 0               | 0               | 0               | 0                  |
| PINGREQ      | Reserved           | 0               | 0               | 0               | 0                  |
| PINGRESP     | Reserved           | 0               | 0               | 0               | 0                  |
| DISCONNECT   | Reserved           | 0               | 0               | 0               | 0                  |

- DUP<sup>1</sup> =控制报文的重复分发标志
- QoS<sup>2</sup> = PUBLISH报文的服务质量等级
- RETAIN<sup>3</sup> = PUBLISH报文的保留标志

PUBLISH控制报文中的DUP, QoS和RETAIN标志的描述见 3.3.1节。

### 2.2.3 剩余长度 Remaining Length

**位置：**从第2个字节开始。

剩余长度（Remaining Length）表示当前报文剩余部分的字节数，包括可变报头和负载的数据。剩余长度不包括用于编码剩余长度字段本身的字节数。

剩余长度字段使用一个变长度编码方案，对小于128的值它使用单字节编码。更大的值按下面的方式处理。低7位有效位用于编码数据，最高有效位用于指示是否有更多的字节。因此每个字节可以编码128个数值和一个*延续位（continuation bit）*。剩余长度字段最大4个字节。

> **非规范评注**
>
> 例如，十进制数64会被编码为一个字节，数值是64，十六进制表示为0x40,。十进制数字321(=65+2\*128)被编码为两个字节，最低有效位在前。第一个字节是 65+128=193。注意最高位为1表示后面至少还有一个字节。第二个字节是1。
>
> **非规范评注**
>
> 这允许应用发送最大256MB(268,435,455)大小的控制报文。这个数值在报文中的表示是：0xFF,0xFF,0xFF,0x7F。
>
> [表格 2.4剩余长度字段的大小](#_Table_2.4_Size)展示了剩余长度字段所表示的值随字节增长。

##### 表格 2.4剩余长度字段的大小 Size of Remaining Length field

| **字节数** | **最小值**                         | **最大值**                           |
|------------|------------------|----------------------|
| 1          | 0 (0x00)                           | 127 (0x7F)                           |
| 2          | 128 (0x80, 0x01)                   | 16 383 (0xFF, 0x7F)                  |
| 3          | 16 384 (0x80, 0x80, 0x01)          | 2 097 151 (0xFF, 0xFF, 0x7F)         |
| 4          | 2 097 152 (0x80, 0x80, 0x80, 0x01) | 268 435 455 (0xFF, 0xFF, 0xFF, 0x7F) |

分别表示（每个字节的低7位用于编码数据，最高位是标志位）：

- 1个字节时，从0(0x00)到127(0x7f)
- 2个字节时，从128(0x80,0x01)到16383(0Xff,0x7f)
- 3个字节时，从16384(0x80,0x80,0x01)到2097151(0xFF,0xFF,0x7F)
- 4个字节时，从2097152(0x80,0x80,0x80,0x01)到268435455(0xFF,0xFF,0xFF,0x7F)

>**非规范评注**
>
>非负整数X使用变长编码方案的算法如下：
>
```
   do
  encodedByte = X MOD 128
  X = X DIV 128
 // if there are more data to encode, set the top bit of this byte
 if ( X > 0 )
     encodedByte = encodedByte OR 128
 endif
     'output' encodedByte
while ( X > 0 )

```

>MOD是模运算，DIV是整数除法，OR是位操作或（C语言中分别是%，/，|）


>**非规范评注**
>
>剩余长度字段的解码算法如下：
>
```
multiplier = 1
value = 0
do
      encodedByte = 'next byte from stream'
      value += (encodedByte AND 127) * multiplier
      if (multiplier > 128*128*128)
        throw Error(Malformed Remaining Length)
      multiplier *= 128
while ((encodedByte AND 128) != 0)
```

>AND是位操作与（C语言中的&）

>这个算法终止时，value包含的就是剩余长度的值。

## 2.3 可变报头 Variable header

某些MQTT控制报文包含一个可变报头部分。它在固定报头和负载之间。可变报头的内容根据报文类型的不同而不同。可变报头的报文标识符（Packet Identifier）字段存在于在多个类型的报文里。

### 2.3.1 报文标识符 Packet Identifier

##### 图例 2.3 -报文标识符字节 Packet Identifier bytes

| **Bit** | **7**  - **0** |
|---------|----------------|
| byte 1  | 报文标识符 MSB |
| byte 2  | 报文标识符 LSB |

很多控制报文的可变报头部分包含一个两字节的报文标识符字段。这些报文是PUBLISH（QoS > 0时）， PUBACK，PUBREC，PUBREL，PUBCOMP，SUBSCRIBE, SUBACK，UNSUBSCRIBE，UNSUBACK。

SUBSCRIBE，UNSUBSCRIBE和PUBLISH（QoS大于0）控制报文**必须**包含一个非零的16位报文标识符（Packet Identifier）\[MQTT-2.3.1-1\]。客户端每次发送一个新的这些类型的报文时都**必须**分配一个当前未使用的报文标识符 \[MQTT-2.3.1-2\]。如果一个客户端要重发这个特殊的控制报文，在随后重发那个报文时，它**必须**使用相同的标识符。当客户端处理完这个报文对应的确认后，这个报文标识符就释放可重用。QoS 1的PUBLISH对应的是PUBACK，QoS 2的PUBLISH对应的是PUBCOMP，与SUBSCRIBE或UNSUBSCRIBE对应的分别是SUBACK或UNSUBACK \[MQTT-2.3.1-3\]。发送一个QoS 0的PUBLISH报文时，相同的条件也适用于服务端 \[MQTT-2.3.1-4\]。

QoS等于0的PUBLISH报文**不能**包含报文标识符 \[MQTT-2.3.1-5\]。

PUBACK, PUBREC, PUBREL报文**必须**包含与最初发送的PUBLISH报文相同的报文标识符 \[MQTT-2.3.1-6\]。类似地，SUBACK和UNSUBACK**必须**包含在对应的SUBSCRIBE和UNSUBSCRIBE报文中使用的报文标识符 \[MQTT-2.3.1-7\]。

需要报文标识符的控制报文在 [表格 2.5 -包含报文标识符的控制报文](#_Table_2.5_-) 中列出。

##### 表格 2.5 -包含报文标识符的控制报文 Control Packets that contain a Packet Identifier

| **控制报文** | **报文标识符字段**     |
|--------------|------------------------|
| CONNECT      | 不需要                 |
| CONNACK      | 不需要                 |
| PUBLISH      | 需要（如果QoS > 0） |
| PUBACK       | 需要                   |
| PUBREC       | 需要                   |
| PUBREL       | 需要                   |
| PUBCOMP      | 需要                   |
| SUBSCRIBE    | 需要                   |
| SUBACK       | 需要                   |
| UNSUBSCRIBE  | 需要                   |
| UNSUBACK     | 需要                   |
| PINGREQ      | 不需要                 |
| PINGRESP     | 不需要                 |
| DISCONNECT   | 不需要                 |

客户端和服务端彼此独立地分配报文标识符。因此，客户端服务端组合使用相同的报文标识符可以实现并发的消息交换。

**非规范评注**

客户端发送标识符为0x1234的PUBLISH报文，它有可能会在收到那个报文的PUBACK之前，先收到服务端发送的另一个不同的但是报文标识符也为0x1234的PUBLISH报文。

Client | Server
---|---
PUBLISH | Packet Identifier=0x1234---
--PUBLISH | Packet Identifier=0x1234
PUBACK | Packet Identifier=0x1234---
--PUBACK | Packet Identifier=0x1234

## 2.4 有效载荷 Payload

某些MQTT控制报文在报文的最后部分包含一个有效载荷，这将在第三章论述。对于PUBLISH来说有效载荷就是应用消息。[表格 2.6 – 包含有效载荷的控制报文](#_Table_2.6_-) 列出了需要有效载荷的控制报文。

##### 表格 2.6 – 包含有效载荷的控制报文 Control Packets that contain a Payload

| **控制报文** | **有效载荷** |
|--------------|--------------|
| CONNECT      | 需要         |
| CONNACK      | 不需要       |
| PUBLISH      | 可选         |
| PUBACK       | 不需要       |
| PUBREC       | 不需要       |
| PUBREL       | 不需要       |
| PUBCOMP      | 不需要       |
| SUBSCRIBE    | 需要         |
| SUBACK       | 需要         |
| UNSUBSCRIBE  | 需要         |
| UNSUBACK     | 不需要       |
| PINGREQ      | 不需要       |
| PINGRESP     | 不需要       |
| DISCONNECT   | 不需要       |


### 项目主页

- [MQTT协议中文版](https://github.com/mcxiaoke/mqtt)


