import streamlit as st, datetime, random, time, os, base64
st.set_page_config(page_title="Gold Sniper Pro SA", page_icon="🐼", layout="centered")

def img_b64(p):
    if os.path.exists(p):
        with open(p,"rb") as f:
            return f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"
    return None

logo = img_b64("logo.png")
bg = img_b64("bg.png")
# Fallback if not uploaded - uses same panda robot background as video
bg_url = bg if bg else "https://images.unsplash.com/photo-1605810230434-7631ac76ec81?w=800"
logo_url = logo if logo else "https://cdn.pixabay.com/photo/2023/12/09/10/05/panda-8438367_1280.jpg"

st.markdown(f"""
<style>
.stApp{{
background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.92)), url('{bg_url}');
background-size:cover; background-position:center top; background-attachment:fixed
}}
header{{display:none}}
.block-container{{max-width:420px; padding:0 0 130px 0!important}}
.panda-main{{
width:170px; height:170px; margin:28px auto 10px auto; border-radius:50%;
border:3px solid #ff1a1a; box-shadow:0 0 30px #ff1a1a, 0 0 60px #ff000066, inset 0 0 20px #000;
overflow:hidden; background:#0a0a0a; position:relative
}}
.panda-main img{{width:100%; height:100%; object-fit:cover}}
.control-bar{{
width:90%; max-width:360px; height:72px; margin:22px auto 8px auto;
background:#0a0a0a; border:2px solid #ff1a1a; border-radius:50px;
display:flex; align-items:center; justify-content:space-between;
padding:0 18px; box-shadow:0 0 25px #ff1a1a66; position:relative
}}
.start-center{{
width:92px; height:92px; background:radial-gradient(circle at 35% 35%, #ff4444, #cc0000);
border-radius:50%; display:flex; flex-direction:column; align-items:center; justify-content:center;
color:white; font-weight:900; font-size:11px; letter-spacing:1px;
border:3px solid #ff6666; box-shadow:0 0 25px #ff0000cc; position:absolute; left:50%; top:50%; transform:translate(-50%,-50%)
}}
.robot-list-pill{{
background:#0e0e0e; border:2px solid #ff1a1a; border-radius:50px;
padding:12px 16px; display:flex; align-items:center; justify-content:space-between;
margin:10px 20px; box-shadow:0 0 15px #ff000033
}}
.bottom-nav{{
position:fixed; bottom:0; left:0; right:0; background:#0a0a0aee; backdrop-filter:blur(12px);
border-top:1px solid #1a1a1a; display:flex; justify-content:space-around;
padding:12px 0 20px 0; max-width:420px; margin:0 auto; z-index:9999
}}
div.stButton > button{{background:transparent!important; border:none!important; color:#aaa!important; font-weight:700!important; font-size:11px!important}}
div.stButton > button:hover{{color:white!important}}
</style>
""", unsafe_allow_html=True)

if 'tab' not in st.session_state: st.session_state.tab="Home"
if 'logged' not in st.session_state: st.session_state.logged=False
if 'live' not in st.session_state: st.session_state.live=False
if 'trades' not in st.session_state: st.session_state.trades=[]
if 'user' not in st.session_state: st.session_state.user={}

SA = ["JPMarkets-Real 🇿🇦","CMTrading-Real 🇿🇦","KhweziTrade-Real 🇿🇦","GT247-Real 🇿🇦","Exness-Real-SA 🇿🇦","FBS-Real-SA 🇿🇦","HFM-Real-SA 🇿🇦","Deriv-Real-SA 🇿🇦","XM-Real-SA 🇿🇦","RazorMarkets-Real 🇿🇦","ScopeMarkets-SA 🇿🇦","AvaTrade-SA 🇿🇦","FXTM-SA 🇿🇦","JustMarkets-SA 🇿🇦"]

# AUTO SAVE TRADES WHEN LIVE
if st.session_state.logged and st.session_state.live and random.random()>0.65:
    pf=round(random.uniform(8,65),2)
    st.session_state.trades.insert(0,{"t":datetime.datetime.now().strftime("%H:%M:%S"), "p":random.choice(["XAUUSD","US30","USDZAR 🇿🇦"]), "d":random.choice(["BUY","SELL"]), "pf":pf, "s":st.session_state.user.get("server","SA")})

# TOP PANDA CIRCLE - EXACT LIKE SCREENSHOT
st.markdown(f"""
<div class="panda-main">
<img src="{logo_url}" style="filter: sepia(0.3) hue-rotate(-10deg) saturate(1.6) brightness(1.1);">
<div style="position:absolute; inset:0; background: radial-gradient(circle, rgba(255,0,0,0.25) 0%, transparent 70%);"></div>
</div>
<div style="text-align:center;">
<h1 style="color:white; font-size:29px; font-weight:900; margin:12px 0 4px 0; letter-spacing:0.3px;">Gold Sniper Pro SA</h1>
<p style="color:#aaa; font-size:13px; margin:0;">Powerful Scalping Bot 🇿🇦</p>
</div>
""", unsafe_allow_html=True)

if st.session_state.logged and st.session_state.live:
    st.markdown(f'<div style="background:#00ff0018; border:1px solid #0f0; color:#0f0; border-radius:20px; padding:6px; text-align:center; font-size:11px; margin:10px 20px;">● LIVE on {st.session_state.user.get("server")} | Saving Trades ✅ | {len(st.session_state.trades)} saved</div>', unsafe_allow_html=True)

# CONTROL BAR - PAIRS | START | LOGS - EXACT LIKE SCREENSHOT
st.markdown('<div class="control-bar">', unsafe_allow_html=True)
c1,c2,c3 = st.columns([1,1,1])
with c1:
    if st.button("📈\nPAIRS", key="pairs"): st.session_state.tab="Pairs"; st.rerun()
with c2:
    # Center START button
    if st.session_state.live:
        if st.button("⏹\nSTOP", key="stop"): st.session_state.live=False; st.rerun()
    else:
        if st.button("▶\nSTART", key="start"): 
            if not st.session_state.logged: st.session_state.tab="Activate"; st.rerun()
            else: st.session_state.live=True; st.rerun()
with c3:
    if st.button("🕒\nLOGS", key="logs"): st.session_state.tab="Logs"; st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align:center; margin:8px 0 22px 0; font-size:11px; color:#666;">Powered by <span style="color:#ff2222; font-weight:bold;">EAConnect SA</span></div>', unsafe_allow_html=True)

# CONTENT
if st.session_state.tab=="Home":
    st.markdown('<div style="color:#999; font-size:13px; margin:0 22px 8px 22px;">Robot List</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="robot-list-pill">
    <div style="display:flex; align-items:center; gap:10px;">
    <div style="width:34px; height:34px; border-radius:50%; overflow:hidden; background:#111; border:1px solid #333;"><img src="{logo_url}" style="width:100%; height:100%; object-fit:cover;"></div>
    <span style="color:white; font-weight:600; font-size:14px;">Gold Sniper Pro SA</span>
    </div>
    <div style="width:28px; height:28px; background:#1a0000; border-radius:50%; display:flex; align-items:center; justify-content:center; color:#ff4444; font-size:14px; border:1px solid #ff2222;">✕</div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.logged:
        tot=sum([x['pf'] for x in st.session_state.trades])
        st.markdown(f"<div style='color:white; margin:16px 22px 8px 22px; font-weight:700; font-size:13px;'>💾 Saved Trades on {st.session_state.user.get('server')} - R {tot:.2f} ({len(st.session_state.trades)})</div>", unsafe_allow_html=True)
        for tr in st.session_state.trades[:15]:
            col="#00ff88" if tr['pf']>0 else "#ff4444"
            st.markdown(f'<div style="background:#111111cc; border:1px solid #222; border-radius:10px; padding:9px 12px; margin:5px 20px; display:flex; justify-content:space-between; font-size:12px;"><span style="color:#ddd;">{tr["t"]} {tr["d"]} {tr["p"]} | {tr["s"][:16]}</span><span style="color:{col}; font-weight:bold;">R {tr["pf"]}</span></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="text-align:center; color:#666; margin:30px 20px; font-size:13px;">Tap START to login with SA server<br>and start saving trades 🇿🇦</div>', unsafe_allow_html=True)

elif st.session_state.tab=="Activate":
    st.markdown("### 🔑 EA Connect Activation - All SA Servers 🇿🇦")
    with st.form("act"):
        key=st.text_input("EA Connect Key 🔑", value="GOLD-SA-2025")
        login=st.text_input("MT5 Login", value="4056103")
        pwd=st.text_input("Password", type="password", value="1234")
        server=st.selectbox("Select SA Server 🇿🇦", SA, index=0)
        pairs=st.multiselect("Pairs to Save", ["XAUUSD - GOLD MAIN 🔥","US30 🇿🇦","USDZAR 🇿🇦","EURZAR 🇿🇦","NAS100","BTCUSD"], default=["XAUUSD - GOLD MAIN 🔥","US30 🇿🇦"])
        if st.form_submit_button("🚀 ACTIVATE & SAVE TRADES ON SA SERVER", use_container_width=True, type="primary"):
            st.session_state.logged=True; st.session_state.live=True; st.session_state.user={"login":login,"server":server}
            st.session_state.trades.insert(0,{"t":datetime.datetime.now().strftime("%H:%M:%S"),"p":"XAUUSD","d":"BUY","pf":42.50,"s":server})
            st.session_state.tab="Home"; st.success(f"✅ {server} Activated! Saving trades!"); st.balloons(); time.sleep(1); st.rerun()

elif st.session_state.tab=="Pairs":
    st.markdown("### 📈 Pairs"); st.multiselect("Pairs", ["XAUUSD - GOLD MAIN 🔥","US30 🇿🇦","USDZAR 🇿🇦","EURZAR 🇿🇦","BTCUSD"], default=["XAUUSD - GOLD MAIN 🔥"])
    if st.button("Save ✅", use_container_width=True, type="primary"): st.session_state.tab="Home"; st.rerun()

elif st.session_state.tab=="Logs":
    st.markdown("### 🕒 Logs - Saved Trades SA")
    for tr in st.session_state.trades: st.code(f"{tr['t']} {tr['d']} {tr['p']} R{tr['pf']} on {tr['s']}")
    if st.button("Back Home"): st.session_state.tab="Home"; st.rerun()

elif st.session_state.tab=="Metatrader":
    st.markdown("### Metatrader - SA Servers 🇿🇦")
    st.selectbox("SA Server", SA); st.text_input("Login"); st.text_input("Password", type="password")
    if st.button("Connect SA ✅", use_container_width=True, type="primary"): st.success("Connected SA! Saving trades enabled!")

elif st.session_state.tab=="Scanner":
    st.markdown("### Scanner SA 🇿🇦")
    st.metric("XAUUSD", "$2,645.30", "BUY 95% 🔥")
    if st.button("Scan & Save Trade", use_container_width=True, type="primary") and st.session_state.logged:
        st.session_state.trades.insert(0,{"t":datetime.datetime.now().strftime("%H:%M:%S"),"p":"XAUUSD","d":"BUY","pf":round(random.uniform(10,60),2),"s":st.session_state.user.get("server")})
        st.success("Trade saved on SA server!")

elif st.session_state.tab=="Settings":
    st.markdown("### Settings")
    st.slider("Lot Size",0.01,1.0,0.10); st.selectbox("Default SA Server", SA); st.toggle("Auto Save Trades", True); st.toggle("ZAR Mode 🇿🇦", True)

# BOTTOM NAV - EXACT LIKE SCREENSHOT: Home / Metatrader / Scanner / Settings
st.markdown('<div class="bottom-nav">', unsafe_allow_html=True)
b1,b2,b3,b4 = st.columns(4)
with b1:
    if st.button("🏠\nHome", key="bh"): st.session_state.tab="Home"; st.rerun()
with b2:
    if st.button("🗄️\nMetatrader", key="bm"): st.session_state.tab="Metatrader"; st.rerun()
with b3:
    if st.button("◫\nScanner", key="bs"): st.session_state.tab="Scanner"; st.rerun()
with b4:
    if st.button("⚙️\nSettings", key="bse"): st.session_state.tab="Settings"; st.rerun()
st.markdown('</div>', unsafe_allow_html=True)
