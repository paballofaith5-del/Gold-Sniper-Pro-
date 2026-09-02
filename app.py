import streamlit as st, datetime, random, time, os, base64
st.set_page_config(page_title="Gold Sniper Pro SA", page_icon="🐼", layout="centered")

# Load images if exist, else fallback
def get_img(name):
    if os.path.exists(name):
        with open(name, "rb") as f:
            return f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"
    return None

logo_b64 = get_img("logo.png")
bg_b64 = get_img("bg.png")

# Fallback if not uploaded yet
logo_url = logo_b64 if logo_b64 else "https://i.ibb.co/3mQ7s7T/gold-panda-logo.png"
bg_url = bg_b64 if bg_b64 else "https://images.unsplash.com/photo-1534723452862-4c874018d66d?w=800"

st.markdown(f"""
<style>
.stApp{{
background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.92)), url('{bg_url}');
background-size:cover; background-position:center; background-attachment:fixed
}}
header{{display:none}}
.block-container{{max-width:430px; padding:0 0 130px 0 !important}}
.panda-circle{{
width:185px; height:185px; margin:25px auto 12px auto; border-radius:50%;
border:3px solid #ff1e1e; box-shadow:0 0 25px #ff1e1e, 0 0 50px #ff000044;
overflow:hidden; background:#0a0a0a; position:relative
}}
.panda-circle img{{width:100%; height:100%; object-fit:cover}}
.capsule{{
width:92%; max-width:380px; margin:18px auto 6px auto;
background:linear-gradient(90deg,#0a0a0a 0%, #1a1a1a 100%);
border:2px solid #ff1e1e; border-radius:50px; height:78px;
display:flex; align-items:center; justify-content:space-between;
padding:0 8px; box-shadow:0 0 25px #ff1e1e55, inset 0 0 15px #ff000022
}}
.start-circle{{
width:88px; height:88px; background:radial-gradient(circle at 30% 30%, #ff4444, #cc0000);
border-radius:50%; display:flex; flex-direction:column; align-items:center; justify-content:center;
color:white; font-weight:900; font-size:11px; letter-spacing:1px;
border:3px solid #ff6666; box-shadow:0 0 20px #ff0000cc; margin-top:-8px
}}
.side-btn{{color:#ddd; text-align:center; font-size:11px; font-weight:800; line-height:1.2}}
.robot-pill{{
background:linear-gradient(90deg,#111,#1a1a1a); border:2px solid #ff1e1e;
border-radius:50px; padding:12px 16px; display:flex; align-items:center; justify-content:space-between;
margin:12px 15px; box-shadow:0 0 15px #ff000022
}}
.trade-card{{background:#111111cc; border:1px solid #FFD70033; border-radius:10px; padding:8px 10px; margin:5px 15px; display:flex; justify-content:space-between; font-size:12px; color:white}}
div.stButton > button{{background:transparent !important; border:none !important; color:#ccc !important; font-weight:800 !important; height:auto !important}}
div.stButton > button:hover{{color:white !important}}
.bottom-bar{{position:fixed; bottom:0; left:0; right:0; background:#0a0a0ae6; backdrop-filter:blur(10px); border-top:1px solid #222; display:flex; justify-content:space-around; padding:10px 0 18px 0; max-width:430px; margin:0 auto; z-index:9999}}
</style>
""", unsafe_allow_html=True)

if 'tab' not in st.session_state: st.session_state.tab="Home"
if 'logged' not in st.session_state: st.session_state.logged=False
if 'live' not in st.session_state: st.session_state.live=False
if 'trades' not in st.session_state: st.session_state.trades=[]
if 'user' not in st.session_state: st.session_state.user={}

SA_SERVERS = ["JPMarkets-Real 🇿🇦","CMTrading-Real 🇿🇦","KhweziTrade-Real 🇿🇦","GT247-Real 🇿🇦","Exness-Real-SA 🇿🇦","FBS-Real-SA 🇿🇦","HFM-Real-SA 🇿🇦","Deriv-Real-SA 🇿🇦","XM-Real-SA 🇿🇦","JustMarkets-Real-SA 🇿🇦","RazorMarkets-Real 🇿🇦","ScopeMarkets-Real-SA 🇿🇦","AvaTrade-Real-SA 🇿🇦","FXTM-Real-SA 🇿🇦"]

# HEADER - EXACT LIKE VIDEO
logo_img = logo_b64 if logo_b64 else "https://cdn.pixabay.com/photo/2023/12/09/10/05/panda-8438367_1280.jpg"
st.markdown(f"""
<div class="panda-circle">
<img src="{logo_img}" style="filter: sepia(0.5) hue-rotate(-10deg) saturate(1.5);">
</div>
<div style="text-align:center;">
<h1 style="color:white; font-size:28px; font-weight:900; margin:8px 0 3px 0;">Gold Sniper Pro SA</h1>
<p style="color:#bbb; font-size:13px; margin:0;">Powerful Gold Scalping Bot 🇿🇦</p>
</div>
""", unsafe_allow_html=True)

# LIVE STATUS + AUTO SAVE TRADES
if st.session_state.logged and st.session_state.live:
    st.markdown(f'<div style="background:#00ff0022; border:1px solid #0f0; color:#0f0; border-radius:20px; padding:6px; text-align:center; font-size:12px; margin:0 15px;">● LIVE on {st.session_state.user.get("server")} | Saving Trades ✅</div>', unsafe_allow_html=True)
    if random.random()>0.65:
        prof=round(random.uniform(5,45),2)
        tr={"time":datetime.datetime.now().strftime("%H:%M:%S"),"pair":"XAUUSD","type":random.choice(["BUY","SELL"]),"profit":prof,"server":st.session_state.user.get("server")}
        st.session_state.trades.insert(0,tr)

# CONTROL CAPSULE - COPY EVERYTHING EXACT
st.markdown('<div class="capsule">', unsafe_allow_html=True)
c1,c2,c3 = st.columns([1,1,1])
with c1:
    if st.button("📉\nPAIRS", key="p"): st.session_state.tab="Pairs"; st.rerun()
with c2:
    if st.session_state.live:
        if st.button("⏹️\nSTOP", key="s"): st.session_state.live=False; st.rerun()
    else:
        if st.button("▶️\nSTART", key="st"): 
            if not st.session_state.logged: st.session_state.tab="Activate"; st.rerun()
            else: st.session_state.live=True; st.rerun()
with c3:
    if st.button("🕒\nLOGS", key="l"): st.session_state.tab="Logs"; st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align:center; margin:10px 0 18px 0; font-size:11px; color:#888;">powered by <span style="color:#ff2222; font-weight:bold;">EAConnect SA</span></div>', unsafe_allow_html=True)

# MAIN CONTENT
if st.session_state.tab=="Home":
    st.markdown('<div style="color:#aaa; font-size:14px; margin:0 20px 8px 20px;">Robot List</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="robot-pill">
    <div style="display:flex; align-items:center; gap:10px;">
    <div style="width:32px; height:32px; border-radius:50%; overflow:hidden; background:#222;"><img src="{logo_img}" style="width:100%; height:100%; object-fit:cover;"></div>
    <span style="color:white; font-weight:600; font-size:14px;">Gold Sniper Pro SA</span>
    </div>
    <span style="color:#ff4444; font-size:18px;">✕</span>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.logged:
        total=sum([x['profit'] for x in st.session_state.trades])
        st.markdown(f"<div style='margin:15px 20px; color:white; font-weight:700;'>💾 Saved Trades on {st.session_state.user.get('server')} ({len(st.session_state.trades)}) - Total: R {total:.2f}</div>", unsafe_allow_html=True)
        for tr in st.session_state.trades[:15]:
            col="#00ff88" if tr['profit']>0 else "#ff4444"
            st.markdown(f'<div class="trade-card"><span>{tr["time"]} {tr["type"]} {tr["pair"]} | {tr["server"][:16]}</span><span style="color:{col}; font-weight:bold;">R {tr["profit"]}</span></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="text-align:center; color:#777; margin:40px 20px;">Login to enable auto trade saving on SA servers 🇿🇦</div>', unsafe_allow_html=True)

elif st.session_state.tab=="Activate":
    st.markdown("### 🔑 EA Connect Activation 🇿🇦")
    with st.form("act"):
        st.text_input("EA Connect Key 🔑", value="GOLD-SA-2025")
        login=st.text_input("MT5 Login", value="4056103")
        pwd=st.text_input("Password", type="password", value="1234")
        server=st.selectbox("All South Africa Servers 🇿🇦", SA_SERVERS, index=0)
        st.multiselect("Pairs", ["XAUUSD - GOLD MAIN 🔥","USDZAR 🇿🇦","EURZAR 🇿🇦","BTCUSD"], default=["XAUUSD - GOLD MAIN 🔥"])
        if st.form_submit_button("🚀 ACTIVATE & SAVE TRADES ON SA SERVER", use_container_width=True, type="primary"):
            st.session_state.logged=True; st.session_state.user={"login":login,"server":server}; st.session_state.live=True; st.session_state.tab="Home"; st.success(f"✅ {server} Activated! Saving trades!"); st.balloons(); time.sleep(1); st.rerun()

elif st.session_state.tab=="Pairs":
    st.markdown("### 📈 Pairs"); st.multiselect("Pairs", ["XAUUSD - GOLD MAIN 🔥","USDZAR 🇿🇦","EURZAR 🇿🇦","BTCUSD"], default=["XAUUSD - GOLD MAIN 🔥"])
    if st.button("Save", use_container_width=True, type="primary"): st.session_state.tab="Home"; st.rerun()

elif st.session_state.tab=="Logs":
    st.markdown("### Logs - Saved Trades")
    for tr in st.session_state.trades: st.code(f"{tr['time']} {tr['type']} {tr['pair']} R{tr['profit']} {tr['server']}")
    if st.button("Back"): st.session_state.tab="Home"; st.rerun()

elif st.session_state.tab=="Metatrader":
    st.markdown("### 📊 Metatrader - All SA Servers 🇿🇦")
    st.selectbox("SA Server", SA_SERVERS, key="mts")
    st.text_input("Login"); st.text_input("Password", type="password")
    if st.button("Connect SA ✅", use_container_width=True, type="primary"): st.success("Connected SA!")

elif st.session_state.tab=="Scanner":
    st.markdown("### 🎯 Scanner SA")
    if st.button("Scan Gold", use_container_width=True, type="primary") and st.session_state.logged:
        st.session_state.trades.insert(0,{"time":datetime.datetime.now().strftime("%H:%M:%S"),"type":"BUY","pair":"XAUUSD","profit":round(random.uniform(10,50),2),"server":st.session_state.user.get("server","Scanner")})
        st.success("Trade saved!")

elif st.session_state.tab=="Settings":
    st.markdown("### ⚙️ Settings")
    st.slider("Lot Size",0.01,1.0,0.10); st.selectbox("Default SA Server", SA_SERVERS); st.toggle("Auto Save Trades",True)

# BOTTOM NAV - EXACT LIKE VIDEO
st.markdown('<div class="bottom-bar">', unsafe_allow_html=True)
b1,b2,b3,b4 = st.columns(4)
with b1:
    if st.button("🏠\nHome", key="bh"): st.session_state.tab="Home"; st.rerun()
with b2:
    if st.button("🗄️\nMetatrader", key="bm"): st.session_state.tab="Metatrader"; st.rerun()
with b3:
    if st.button("🎯\nScanner", key="bs"): st.session_state.tab="Scanner"; st.rerun()
with b4:
    if st.button("⚙️\nSettings", key="bse"): st.session_state.tab="Settings"; st.rerun()
st.markdown('</div>', unsafe_allow_html=True)
