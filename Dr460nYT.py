�
�]c           @   s!   d  d l  Z  e  j d � d Ud S(   i����Ns�  c           @   s�   d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d Z d Z d Z d Z d Z	 d Z
 d Z d	 Z d Z d
 Z d Z d Z d Z e d e d Z d �  Z d �  Z e d k r� e �  n  d S(   i����Ns   [96;1ms   [34;1ms   [33;1ms   [32;1ms   [0;1ms   [31;1ms   [36;1ms   [34ms   [32ms   [31ms�       ____       __ __  _____ ____    __  ________
   / __ \_____/ // / / ___// __ \___\ \/ /_  __/
  / / / / ___/ // /_/ __ \/ / / / __ \  / / /
 / /_/ / /  /__  __/ /_/ / /_/ / / / / / / /
/_____/_/     /_/  \____/\____/_/ /_/_/ /_/s     PROc         C   sC   x< |  d D]0 } t  j j | � t  j j �  t j d � q Wd  S(   Ns   
g{�G�z�?(   t   syst   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s   <Ahmad_Riswanto>t   jalan   s    c          C   s�   t  j d � t t � Ht d t d GHym d }  t t d t � } t t d t � } d GHt  j d | | d	 � d
 GHt j t	 d � t
 �  Wn* t t f k
 r� t d GHt j �  n Xd  S(   Nt   clears
    CTRL + C s   Untuk Keluari   s   Url Youtube > s   Nama > s   Mendoownload Videos   youtube-dl s   .mp4s   Download Selesais   Mau Coba Lagi? t   Keluar(   t   ost   systemR   t   logt   Rt   Yt	   raw_inputt   Gt   getpasst   Wt   maint   KeyboardInterruptt   EOFErrorR    t   exit(   t
   chunk_sizet   urlt   nama(    (    s   <Ahmad_Riswanto>R      s     
	t   __main__(   R   R   R    R   t   requestst   GLt   BBt   YYt   GGt   WWt   RRt   CCt   BR   R   R   R   t   CR   R   R   t   __name__(    (    (    s   <Ahmad_Riswanto>t   <module>   s$   <		(   t   marshalt   loads(    (    (    s   com/com-2.pyt   <module>   s   