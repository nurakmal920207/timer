# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 09:58:14 2022

@author: NurAkmal.MohdNordi
"""

import streamlit as st
import time

st.set_page_config()

ph = st.empty()
N = 5*60
start = st.button('Start')
stop = st.button('Stop')
if stop:
    start = False
secs = 0
while start:
    secs = secs + 1
    mm, ss = secs//60, secs%60
    ph.metric("Timer", f"{mm:02d}:{ss:02d}")
    time.sleep(1)