# ML-Journey
working with machine learning, let's **start learning from beginers**.

- [ML-Journey](#ml-journey)
  - [Week 1](#week-1)
    - [Day 1 ("Data Type")](#day-1-data-type)
    - [Day 2 ("Data Type 2")](#day-2-data-type-2)

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

### Day 2 ("Data Type 2")

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
    * working by replace duplicated data
      * eg. "to be or not to be, that is the question" -->> "⊜ ⬗ or not ⊜ ⬗, ⟡at is ⟡e question" which replace ``"to" -->> ⊜``, ``"be" -->> ⬗``, ``"th" -->> ⟡``
  * __Lossy__ --> reduce size file by discard less important information ( work with ``photos, audio`` )

> [!NOTE]
> Learned Vocabulary :book:
> - telegraphy => โทรเลข
> - telepriters => เครื่องพิมพ์ดีด
> - alternative => ทางเลือก
> - precise => แม่นยำ

[09/04/2024]: #

---