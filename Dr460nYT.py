ó
]c           @   s6  d  d l  Z  d  d l Z d  d l Z d  d l Z y d  d l Z Wng e k
 r© e d e d GHe j d  e j e d e	 d e d  e  j
 d  e j   n Xd Z d	 Z d
 Z d Z d Z d Z d Z d Z d
 Z d Z d Z	 d Z d Z e d e d Z d   Z d   Z e d k r2e   n  d S(   iÿÿÿÿNs   [#]>> s*   Sepertinya Module Requests Belum Di Pasangi   s   [!] s   Tekan Enter Untuk Menginstall s   pip2 install requests requestss   [96;1ms   [34;1ms   [33;1ms   [32;1ms   [0;1ms   [31;1ms   [36;1ms   [34ms   [32ms   [31msè       ____       __ __  _____ ____    __  ________
   / __ \_____/ // / / ___// __ \___\ \/ /_  __/
  / / / / ___/ // /_/ __ \/ / / / __ \  / / /
 / /_/ / /  /__  __/ /_/ / /_/ / / / / / / /
/_____/_/     /_/  \____/\____/_/ /_/_/ /_/s     PROc         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g{®Gáz?(   t   syst   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s   /sdcard/MyProject/Dr460nYT.pyt   jalan"   s    c          C   s-  t  j d  t t  Ht d t d GHym d }  t t d t  } t t d t  } d GHt  j d | | d	  d
 GHt j t	 d  t
   Wn t t f k
 rÂ t d GHt j   ng t k
 r(t d t d GHt j d  t j t d t	 d t d  t  j d  t j   n Xd  S(   Nt   clears
    CTRL + C s   Untuk Keluari   s   Url Youtube > s   Nama > s   Mendoownload Videos   youtube-dl s   .mp4s   Download Selesais   Mau Coba Lagi? t   Keluars   [#]>> s!   Sepertinya Module Belum Di Pasangi   s   [!] s   Tekan Enter Untuk Menginstall s    pip2 install requests youtube-dl(   t   ost   systemR   t   logt   Rt   Yt	   raw_inputt   Gt   getpasst   Wt   maint   KeyboardInterruptt   EOFErrorR    t   exitt   KeyErrorR   R   (   t
   chunk_sizet   urlt   nama(    (    s   /sdcard/MyProject/Dr460nYT.pyR   (   s,    
	!t   __main__(   R   R   R    R   t   requestst   ImportErrorR   R   R   R   R   R   t   GLt   BBt   YYt   GGt   WWt   RRt   CCt   BR   t   CR   R   R   t   __name__(    (    (    s   /sdcard/MyProject/Dr460nYT.pyt   <module>   s4   0!		