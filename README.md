# PwnProjects
CTF Pwn 刷题记录，不断更新中...

## PWN环境
* [Ancypwn](https://github.com/Escapingbug/ancypwn)

## 工具指南
* [pwntools](https://pwntoolsdocinzh-cn.readthedocs.io/en/master/index.html)

## 刷题记录
### Platform 1 - [JarvisOJ](https://www.jarvisoj.com)
Jarvis OJ is a CTF training platform developed by Jarvis from USSLab in ZJU. This platform will collect or make a series of problems having a good quality for CTFers to solve. Hope you can improve your security skills in this platform and enjoy it.

* [[61dctf]calc.exe](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/61DCTF/calcexe) : [WriteUp](https://coldwave96.github.io/2021/02/04/Calcexe/)
* [[61dctf]fm](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/61DCTF/fm) : [WriteUp](https://coldwave96.github.io/2020/09/08/61DCTF-fm/)
* [Add](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/Add) : [WriteUp](https://coldwave96.github.io/2021/01/28/Add/)
* [Backdoor](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/Backdoor) : [WriteUp](https://coldwave96.github.io/2020/08/18/Backdoor/)
* [Guess](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/Guess) : [WriteUp](https://coldwave96.github.io/2020/08/31/Guess/)
* [Guestbook2](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/Guestbook2)
* [HTTP](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/HTTP) : [WriteUp](https://coldwave96.github.io/2020/09/03/HTTP/)
* [Item Board](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/ItemBoard) : [WriteUp](https://coldwave96.github.io/2020/10/20/ItemBoard/)
* [Smashes](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/Smashes) : [WriteUp](https://coldwave96.github.io/2020/08/06/Smashes/)
* [Tell Me Something](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/TellMeSomething)
* [Test Your Memory](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/TestYourMemory)
* [Typo](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/Typo) : [WriteUp](https://coldwave96.github.io/2021/01/20/Typo/)
* [[XMAN]level0](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/XMAN/level0) : [WriteUp](https://coldwave96.github.io/2020/05/01/XMAN-level0/)
* [[XMAN]level1](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/XMAN/level1) : [WriteUp](https://coldwave96.github.io/2020/05/07/XMAN-level1/)
* [[XMAN]level2](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/XMAN/level2/level2) : [WriteUp](https://coldwave96.github.io/2020/05/01/XMAN-level2/)
* [[XMAN]level2(x64)](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/XMAN/level2/level2_x64) : [WriteUp](https://coldwave96.github.io/2020/05/11/XMAN-level2-x64/)
* [[XMAN]level3](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/XMAN/level3/level3) : [WriteUp](https://coldwave96.github.io/2020/05/20/XMAN-level3/)
* [[XMAN]level3(x64)](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/XMAN/level3/level3_x64)
* [[XMAN]level4](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/XMAN/level4) : [WriteUp](https://coldwave96.github.io/2020/06/22/XMAN-level4/)
* [[XMAN]level5](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/XMAN/level5) : [WriteUp](https://coldwave96.github.io/2020/06/23/XMAN-level5/)
* [[XMAN]level6](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/XMAN/level6/level6) : [WriteUp](https://coldwave96.github.io/2020/07/29/XMAN-level6/)
* [[XMAN]level6_x64](https://github.com/Coldwave96/PwnProjects/tree/main/JarvisOJ/XMAN/level6/level6_x64)

### Platform 2 - [ROP Emporium](https://ropemporium.com)
Learn return-oriented programming through a series of challenges.

#### [Challenge 1 - ret2win](https://ropemporium.com/challenge/ret2win.html) : [WriteUp](https://coldwave96.github.io/2020/05/19/ret2win/)
ret2win means "return here to win" and it's recommended you start with this challenge. Visit the challenge page by clicking this card to learn more.

#### [Challenge 2 - split](https://ropemporium.com/challenge/split.html) : [WriteUp](https://coldwave96.github.io/2020/05/27/split/)
ret2win means "return here to win" and it's recommended you start with this challenge. Visit the challenge page by clicking this card to learn more.

#### [Challenge 3 - callme](https://ropemporium.com/challenge/callme.html) : [WriteUp](https://coldwave96.github.io/2020/05/29/callme/)
Chain calls to multiple imported methods with specific arguments and see how the differences between 64 & 32 bit calling conventions affect your ROP chain.

#### [Challenge 4 - write4](https://ropemporium.com/challenge/write4.html) : [WriteUp](https://coldwave96.github.io/2020/06/02/write4/)
Find and manipulate gadgets to construct an arbitrary write primitive, then use it to learn where and how to get your data into process memory.

#### [Challenge 5 - badchars](https://ropemporium.com/challenge/badchars.html) : [WriteUp](https://coldwave96.github.io/2020/06/05/badchars/)
Learn to deal with "badchars": characters that will not make it into process memory intact or cause other issues such as premature chain termination.

#### [Challenge 6 - fluff](https://ropemporium.com/challenge/fluff.html) : [WriteUp](https://coldwave96.github.io/2020/06/10/fluff/)
Sort the useful gadgets from the fluff to construct another write primitive in this challenge. You'll have to get creative though, the gadgets aren't straightforward.

#### [Challenge 7 - pivot](https://ropemporium.com/challenge/pivot.html) : [WriteUp](https://coldwave96.github.io/2020/06/11/pivot/)
Stack space is at a premium in this challenge and you'll have to pivot the stack onto a second ROP chain elsewhere in memory to ensure your success.

#### [Challenge 8 - ret2csu](https://ropemporium.com/challenge/ret2csu.html) : [WriteUp](https://coldwave96.github.io/2020/06/15/ret2csu/)
Learn a ROP technique that lets you populate useful calling convention registers like rdi, rsi and rdx even in an environment where gadgets are sparse.

### Platform 3 - [pwnable](https://pwnable.tw)
Pwnable.tw is a wargame site for hackers to test and expand their binary exploiting skills.

* [hacknote](https://github.com/Coldwave96/PwnProjects/tree/main/pwnable/hacknote) : [WriteUp](https://coldwave96.github.io/2020/07/09/Hacknote/)

### [easy_csu](https://github.com/Coldwave96/PwnProjects/tree/main/easy_csu)
