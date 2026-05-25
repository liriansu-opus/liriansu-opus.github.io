---
title:     "0x5f3759df: A Magical Number"
date:      "2014-03-07 14:11:31"
zhUrl: /magic-number
aliases:
  - /magic-number-en
---

Today while reading various algorithm introductions I came across this line: "The magical number 0x5f3759df was not invented by John Carmack. The reason it was initially misunderstood is mainly that many game programmers who had long worshiped Carmack's halo were scared shitless when reading the Quake3 source code......" This piqued my curiosity, and after looking up some material I've put the whole story together as follows.

<!--more-->

## Quake3

Quake3 is a classic FPS game from the 90s, with not only beautiful graphics but also a well-optimized program, capable of running smoothly even on average-spec computers. This is mainly thanks to its 3D engine id Tech3, which was developed under the leadership of John Carmack.

Carmack is an American code monkey, one of the founders of id Software. He became famous for his outstanding achievements in 3D technology. Carmack is also a proponent of open source software. In 1996 he released the source code of Quake, and a programmer rewrote it into a Linux version and sent it to Carmack. Carmack didn't consider this an infringement, but instead asked his employees to develop the Linux version of Quake based on this patch. In the following days id Software also released the source code of Quake2, and in 2005, the source code of Quake3 was also released.

(This is the official download address ftp://ftp.idsoftware.com/idstuff/source/quake3-1.32b-source.zip)

We know that the lower-level a function is, the more frequently it's called. If you optimize the lower-level functions well, efficiency naturally goes up. A 3D engine, when you get down to it, is still math operations. In the lowest-level operation functions (in game/code/q_math.c), there are many interesting functions, some of which are even astonishing in how they were written.


## The Magical 0x5f3759df

In the operations function file you can find a function whose purpose is to take the inverse square root of a number, functionally the same as the system function (float)(1.0/sqrt(x)), but four times more efficient:

```
float Q_rsqrt( float number )
{
    long i;
    float x2, y;
    const float threehalfs = 1.5F;

    x2 = number * 0.5F;
    y = number;
    i = * ( long * ) &y;         // evil floating point bit level hacking
    i = 0x5f3759df - ( i >> 1 ); // WHAT THE FUCK?
    y = * ( float * ) &i;
    y = y * ( threehalfs - ( x2 * y * y ) );       // 1st iteration
    // y = y * ( threehalfs - ( x2 * y * y ) );    // 2nd iteration, this can be removed

#ifndef Q3_VM
#ifdef __linux__
    assert( !isnan(y) ); // bk010122 - FPE?
#endif
#endif
    return y;
}
```

The core of this function, the most baffling line, is the one labeled "WHAT THE FUCK"

`i = 0x5f3759df - ( i >> 1 );`

Adding one more line `y = y * ( threehalfs - ( x2 * y * y ) );` completes the square root operation.

Normal square root calculations use Newton's iterative method. For example, to compute sqrt(5), first let A = 2, then B = 5 / A; A = (A + B) / 2; loop like this, and A and B will get closer and closer, the final result being root five. The badass thing about Carmack's algorithm is that it directly uses the number 0x5f3759df to guess a value, and after one calculation gets very close to root N. This saves many iterative approximation steps, and the function's efficiency is greatly optimized.

After Purdue mathematician Chris Lomont learned about this number he became very interested and decided to research its mystery. This Lomont is also a beast — after careful research he theoretically derived an optimal guess value: 0x5f37642f, very close to the 0x5f3759df in the code. After getting this result Lomont was very pleased, and he raced his number against Carmack's magic number, and Carmack won...... Nobody knows how Carmack came up with his number......

Lomont was unwilling to accept that his carefully derived theoretical optimum lost to Carmack, so he used an exhaustive-search-like method to try one by one, and finally found a number slightly better than Carmack's 0x5f3759df: 0x5f375a86. So Lomont happily wrote a paper about this result and published it...... (Paper link: https://www.matrix67.com/data/InvSqrt.pdf)

This algorithm also got its own name: Fast Inverse Square Root


## The Inventor of the Algorithm

Because John Carmack was the developer of the entire Quake project, at first many people simply assumed that the magic number 0x5f3759df was Carmack's masterpiece. But later Carmack himself denied this in a reply to an inquiry email. Carmack recalled that it was probably a veteran code monkey on the Quake project named Terje Mathisen who wrote this piece of code. Mathisen replied that he had indeed written similar code, but he wasn't the original. The earliest known implementation was by Gary Tarilli in the SGI Indigo, but he also said he had just made some improvements to the constant — he wasn't actually the author either.

Although there's no definitive conclusion about who invented the entire algorithm, people still enjoy talking about Carmack and his magic number 0x5f3759df.


> References:
> https://www.guokr.com/post/90718/
> https://www.matrix67.com/data/InvSqrt.pdf
> https://www.matrix67.com/blog/archives/362
> https://en.wikipedia.org/wiki/Fast_inverse_square_root
> https://en.wikipedia.org/wiki/John_Carmack
> https://zh.wikipedia.org/wiki/%E5%B9%B3%E6%96%B9%E6%A0%B9%E5%80%92%E6%95%B0%E9%80%9F%E7%AE%97%E6%B3%95
