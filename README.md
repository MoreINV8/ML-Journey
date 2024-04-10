# ML-Journey
working with machine learning, let's **start learning from beginers**.

- [ML-Journey](#ml-journey)
  - [Week 1](#week-1)
    - [Day 1 ("Data Type")](#day-1-data-type)
    - [Day 2, 3 ("Data Type 2")](#day-2-3-data-type-2)
    - [Day 3 ("Copy Right")](#day-3-copy-right)

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
      * <div><img src="assets/images/lossy-brightness.png"  style="margin-right:10px;height:100" alt="brightness"\><img src="assets/images/lossy-chroma.png" style="margin-right:10px;height:100" alt="chroma"\><img src="assets/images/lossy-result.jpg" height=100 alt="result"\></div>
    *  _Audio_ analyze and discard data wich human can't hear that data

> [!NOTE]
> Learned Vocabulary :book:
> - telegraphy => โทรเลข
> - telepriters => เครื่องพิมพ์ดีด
> - alternative => ทางเลือก
> - precise => แม่นยำ
> - irreversible => กลับไม่ได้

[09/04/2024]: #
[10/04/2024]: #

---

### Day 3 ("Copy Right")
