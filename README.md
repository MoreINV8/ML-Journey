# ML-Journey
working with machine learning, let's **start learning from beginers**.

- [ML-Journey](#ml-journey)
  - [Week 1](#week-1)
    - [Day 1 ("Data Type")](#day-1-data-type)
    - [Day 2, 3 ("Data Type 2")](#day-2-3-data-type-2)
    - [Day 3 ("Internet")](#day-3-internet)

> inspiration and guide line from this [YouTube](https://www.youtube.com/watch?v=MhCHrvfAXlc&list=PLBmyjHMDRyymkx738MhfZMBeE99DAA_R5&index=7 "YouTube").

## Week 1
### Day 1 ("Data Type")

* ***Binary Number***
    * A computer is electronic so the data that it can be work with are ether 0,1 tell this wire is on or off ```1 == on/0 == off```.
    * ***8 bits == 1 byte***
    * nowadays byte is smallest addressable unit in computer
    * how to detect odd number in binary ? => **Ans** look at last bit at once's position ```(value == 0) ? False : True```

* ***Integer Number***
    * overflow

* ***Floating Number***
    * roundoff

> [!NOTE]
> Learned Vocabulary :book:
> - aspirants => ผู้พูด
> - exorbitant => สูงเกินไป
> - sufficient => เพียงพอ

[08/04/2024]: #

---

### Day 2, 3 ("Data Type 2")

* ***Text***
  * __ASCII__
    * use 7 bits size
    * the first 32 charactors of ASCII is control charactors
  * __Unicode__
  * __UTF-8__
    * start with bit 0 represent ASCII charactors. **look for _single bytes_ to get charactor**
      * A --> 01000001
    * start with bits 110 represent Latin, Arabic, Greek, etc. **look for _two bytes_ to get charactor**
      * α --> 11001110 10110001
    * start with bits 1110 represent Asian charactors. **look for _three bytes_ to get charactor**
      * ก --> 11100000 10111000 10000001
    * start with bits 11110 represent other charactors. else **look for _four bytes_ to get charactor**
      * 🐳 --> 11110000 10011111 10010000 10110011

* ***Analog Data*** --> data wich have contiuously sequence of data ( eg. sound )
  * __Sampling__ --> reduce precision and continuously of data in X-axis
    * sample rate / sampling interval
  
  * __Quantization__ --> reduce precision and continuously of data in Y-axis
    * quantization interval
  * __Binary Encoding__
    * bit depth --> how many bit use encrypt each sample
  * __Reconstruction__ --> convert digital data back to wave

| Original                                           |                      Sampling                      |                        Quantization                        |                            Binary                             | Reconstruction                                              |
| :------------------------------------------------- | :------------------------------------------------: | :--------------------------------------------------------: | :-----------------------------------------------------------: | :---------------------------------------------------------- |
| ![original wave](/assets/images/original-wave.png) | ![sampling wave](/assets/images/sampling-wave.png) | ![quantization wave](/assets/images/quantization-wave.png) | ![binary encoded wave](/assets/images/binary-encode-wave.png) | ![reconstruction wave](/assets/images/reconstruct-wave.png) |

* ***Compression Data***
  * __Lossless__ --> reduce size file with out losing any information ( work with ``text document, simple image, binary data`` )
    * _Text document_ **eg.** "to be or not to be, that is the question" -->> "⊜ ⬗ or not ⊜ ⬗, ⟡at is ⟡e question" which replace ``"to" -->> ⊜``, ``"be" -->> ⬗``, ``"th" -->> ⟡``
    * _Simple image_ using **run-length encoding (RLE)** to reduce same pattern of color pixel **eg.** ``--====---====---`` - binary -> ``0011110001111000`` - RLE -> ``2, 4, 3, 4, 3``
      * > [!TIP] RLE can't be use in image which have different colors
    * _Binary data_ using **Huffman coding**
  * __Lossy__ --> reduce size file by discard less important information ( work with ``photos, audio, videos`` )
    * _Images_ kept only data of brightness and color wich reduce value of color
      * <div><img src="assets/images/lossy-brightness.png" height=100 alt="brightness"\><img src="assets/images/lossy-chroma.png" height=100 alt="chroma"\><img src="assets/images/lossy-result.jpg" height=100 alt="result"\></div>
    *  _Audio_ analyze and discard data wich human can't hear that data
*  ***Ethic***
   * Copyright
   * Fair use
   * Creative Commons
   * Open source
   * Public domain
   * Online publish
     * [Google Scholar](https://scholar.google.com/)
   * Open databases

> [!NOTE]
> Learned Vocabulary :book:
> - telegraphy => โทรเลข
> - telepriters => เครื่องพิมพ์ดีด
> - alternative => ทางเลือก
> - precise => แม่นยำ
> - irreversible => กลับไม่ได้
> - intellectual => ทางปัญญา
> - doctrine => หลักคำสอน

[09/04/2024]: #
[10/04/2024]: #

---

### Day 3 ("Internet")

* ***Words***
  * __Internet__ --> network able devices communicate with other.
  * __Protocal__ --> rule how can device communicated.
  * __Wires & Wireless__ --> connection between devices/protocal for converted eletromagnetic to binary data.
  * __IP__ --> unquely identify address be destination to send data to.
  * __TCP/UDP__ --> protocal that can transfer data and detect error along the way.
  * __TLS__ --> secure protocal sending encrypted data.
  * __HTTP & DNS__ --> protocal for World Wide Web.
  * __Computer Network__ --> grop of computering devices that interconnected with other
  * __Computering Device__ --> any device that can run a program
  * __Network Topology__ --> way computering device connected ![topology](/assets/images/network-topology.svg)
* ***Type of network***
  * __Local area Network "LAN"__ --> cover limited area eg. house, school
  * __Wild Area Network "WAN"__ --> cover large area extended many, many LANs
  * __Data Center Network "DCN"__ --> used in data center where data must exchanged with very little delay
* ***Physical connection***
  * __Copper cables__ --> transmit pulse of **electricity** that represent binary data <div class="box">![copper cable](/assets/images/copper-cable.svg)</div>
  * __Fiber-optic cables__ --> sending pulse of **light** that represent binary data ( can transfer data more than copper) <div class="box">![copper cable](/assets/images/fiber_optic-cable.svg)</div>
  * __Wireless__ --> converted binary data to **radio wave** and transmit through the air <div class="box">![copper cable](/assets/images/wireless.svg)</div>
* ***Transferation***
  * binary data transfer by <div class="box">![copper cable](/assets/images/binary-transfer.svg)</div>
  * __Bit rate__ --> number of bits data send for a second
  * __Bandwidth__ --> maximum bit rate of system
  * __Latency__ --> period of time sending data from computering device to other ( have milliseconds as unit ) also know as ping rate
  * __Internet speed__ --> combination of bandwidth and latency

> [!NOTE]
> Learned Vocabulary :book:
> - acronym => ตัวย่อ
> - knit => ถัก/ผสาน
> - opt => เลือก
> - congestion => ความแออัด

[10/04/2024]: #

---

<style>
  .box {
    background-color:#ffffff;padding:10px;border-radius:8px;
  }
</style>