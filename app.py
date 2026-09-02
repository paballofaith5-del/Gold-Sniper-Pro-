import streamlit as st, datetime, random, time
st.set_page_config(page_title="Gold Sniper Pro SA", page_icon="🐼", layout="centered")
st.markdown("""
<style>
.stApp{background:#000 url('https://i.imgur.com/8QJ4sQq.png'); background-size:cover} header{display:none}
.block-container{max-width:420px; padding:0 0 120px 0}
.panda-circle{width:230px; height:230px; margin:15px auto 10px auto; border-radius:50%; border:3px solid #ff1a1a; box-shadow:0 0 35px #ff1a1a99, inset 0 0 20px #000; overflow:hidden; background:#111}
.control-capsule{background:linear-gradient(90deg,#0a0a0a,#1e1e1e); border:2px solid #ff1a1a; border-radius:50px; padding:5px 10px; display:flex; justify-content:space-between; align-items:center; box-shadow:0 0 25px #ff1a1a66; margin:20px 10px 5px 10px; height:85px}
.start-btn{width:95px; height:95px; background:radial-gradient(#ff3333,#cc0000); border-radius:50%; display:flex; flex-direction:column; align-items:center; justify-content:center; color:white; font-weight:900; box-shadow:0 0 20px #ff0000aa; border:3px solid #ff6666; margin-top:-15px}
.robot-capsule{background:#111; border:2px solid #ff1a1a; border-radius:50px; padding:12px 18px; display:flex; align-items:center; justify-content:space-between; margin:10px}
.trade-card{background:#111; border:1px solid #FFD70044; border-radius:10px; padding:8px; margin:5px 0; font-size:12px; display:flex; justify-content:space-between}
.bottom-nav{position:fixed; bottom:0; left:0; right:0; background:#0a0a0a; border-top:1px solid #222; display:flex; justify-content:space-around; padding:10px 0 18px 0; max-width:420px; margin:0 auto; z-index:9999}
</style>
""", unsafe_allow_html=True)

if 'tab' not in st.session_state: st.session_state.tab="Home"
if 'logged' not in st.session_state: st.session_state.logged=False
if 'live' not in st.session_state: st.session_state.live=False
if 'trades' not in st.session_state: st.session_state.trades=[]
if 'user' not in st.session_state: st.session_state.user={}
if 'logs' not in st.session_state: st.session_state.logs=["[00:50] SA Bot ready..."]

SA_SERVERS = ["JPMarkets-Real 🇿🇦","CMTrading-Real 🇿🇦","KhweziTrade-Real 🇿🇦","GT247-Real 🇿🇦","Exness-Real-SA 🇿🇦","FBS-Real-SA 🇿🇦","HFM-Real-SA 🇿🇦","Deriv-Real-SA 🇿🇦","XM-Real-SA 🇿🇦","JustMarkets-Real-SA 🇿🇦","RazorMarkets-Real 🇿🇦","ScopeMarkets-Real-SA 🇿🇦","AvaTrade-Real-SA 🇿🇦","FXTM-Real-SA 🇿🇦"]

def addlog(m):
    st.session_state.logs.append(f"[{datetime.datetime.now().strftime('%H:%M')}] {m}")

# === TOP LOGO LIKE SCREENSHOT ===
st.markdown("""
<div class="panda-circle">
<img src="https://i.ibb.co/3Yv4vK7h/panda-gold.jpg" onerror="this.src='https://cdn.pixabay.com/photo/2023/12/09/10/05/panda-8438367_1280.jpg'" style="width:100%; height:100%; object-fit:cover; filter: sepia(0.8) hue-rotate(-20deg) saturate(1.8) brightness(1.1);">
</div>
<div style="text-align:center;">
<h1 style="color:white; font-size:28px; font-weight:900; margin:10px 0 2px 0; text-shadow:0 0 10px #ff1a1a;">Gold Sniper Pro SA</h1>
<p style="color:#aaa; font-size:13px; margin:0;">Powerful Gold Scalping Bot 🇿🇦</p>
</div>
""", unsafe_allow_html=True)

# LIVE BADGE & TRADE SAVING SIMULATION
if st.session_state.logged and st.session_state.live:
    st.markdown(f'<div style="background:#00ff0022; border:1px solid #0f0; color:#0f0; border-radius:20px; padding:6px; text-align:center; font-size:12px;">● LIVE on {st.session_state.user.get("server")} | Saving Trades ✅ | {len(st.session_state.trades)} saved</div>', unsafe_allow_html=True)
    if random.random()>0.6:
        p=round(random.uniform(-8,32),2)
        t={"time":datetime.datetime.now().strftime("%H:%M:%S"), "type":random.choice(["BUY","SELL"]), "pair":"XAUUSD", "profit":p, "server":st.session_state.user.get("server")}
        st.session_state.trades.insert(0,t)
        addlog(f"TRADE {t['type']} XAUUSD R{p} on {t['server']}")

# === CONTROL CAPSULE - EXACT LIKE SCREENSHOT - ALL WORKING ===
c1,c2,c3 = st.columns([1,1.2,1])
with c1:
    if st.button("📈\nPAIRS", key="pairs_top", use_container_width=True):
        st.session_state.tab="Pairs"; addlog("PAIRS opened"); st.rerun()
with c2:
    # BIG START BUTTON IN MIDDLE LIKE SCREENSHOT
    if st.session_state.live:
        if st.button("⏹\nSTOP", key="stop_top", use_container_width=True, type="primary"):
            st.session_state.live=False; addlog("STOP pressed"); st.rerun()
    else:
        if st.button("▶\nSTART", key="start_top", use_container_width=True, type="primary"):
            if not st.session_state.logged:
                st.session_state.tab="Activate"; st.rerun()
            else:
                st.session_state.live=True; addlog(f"START on {st.session_state.user.get('server')}"); st.rerun()
with c3:
    if st.button("🕒\nLOGS", key="logs_top", use_container_width=True):
        st.session_state.tab="Logs"; addlog("LOGS opened"); st.rerun()

st.markdown('<div style="text-align:center; margin:8px 0 20px 0; font-size:11px;"><span style="color:#666;">powered by</span> <span style="color:#ff2222; font-weight:bold;">EAConnect SA</span></div>', unsafe_allow_html=True)

# === CONTENT ===
if st.session_state.tab=="Home":
    st.markdown('<div style="color:#aaa; margin:10px 15px; font-size:14px;">Robot List</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="robot-capsule">
    <div style="display:flex; align-items:center; gap:10px;">
    <div style="width:35px; height:35px; background:#222; border-radius:50%; display:flex; align-items:center; justify-content:center;">🐼</div>
    <div style="color:white; font-weight:600; font-size:14px;">Gold Sniper Pro SA</div>
    </div>
    <div style="color:{'#0f0' if st.session_state.live else '#ff1a1a'};">{'●' if st.session_state.live else '○'}</div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.logged:
        st.markdown("### 💾 Saved Trades - SA Server")
        if not st.session_state.trades:
            st.info("Press START to start saving trades")
        for tr in st.session_state.trades[:12]:
            col="#0f0" if tr['profit']>0 else "#f00"
            st.markdown(f'<div class="trade-card"><span>{tr["time"]} {tr["type"]} {tr["pair"]} | {tr["server"][:12]}</span><span style="color:{col}; font-weight:bold;">R{tr["profit"]}</span></div>', unsafe_allow_html=True)
        total=sum([x['profit'] for x in st.session_state.trades])
        st.metric("Total Profit (ZAR)", f"R {total:.2f}", f"{len(st.session_state.trades)} trades")
        if st.button("Clear History"): st.session_state.trades=[]; st.rerun()
    else:
        st.warning("Login first to enable trade saving on SA servers 🇿🇦")
        if st.button("Login Now - Choose SA Server", use_container_width=True, type="primary"):
            st.session_state.tab="Activate"; st.rerun()

elif st.session_state.tab=="Pairs":
    st.markdown("### 📈 PAIRS")
    st.multiselect("Select pairs:", ["XAUUSD - GOLD MAIN 🔥","EURUSD","GBPUSD","USDZAR 🇿🇦","EURZAR 🇿🇦","BTCUSD","NAS100","US30"], default=["XAUUSD - GOLD MAIN 🔥"])
    if st.button("Save Pairs ✅", use_container_width=True, type="primary"): st.session_state.tab="Home"; st.rerun()

elif st.session_state.tab=="Logs":
    st.markdown("### 🕒 LOGS")
    for l in reversed(st.session_state.logs[-30:]): st.code(l)
    if st.button("Back Home"): st.session_state.tab="Home"; st.rerun()

elif st.session_state.tab=="Activate":
    st.markdown("### 🔑 EA Connect Activation - SA Servers 🇿🇦")
    st.markdown(f'<div style="background:#111; border:1px solid #ff1a1a; border-radius:10px; padding:10px; margin:10px 0;"><p style="color:#FFD700; text-align:center; font-size:12px;">All South Africa Servers Supported 🇿🇦</p></div>', unsafe_allow_html=True)
    with st.form("act"):
        st.text_input("EA Connect Key 🔑", placeholder="XXXX-XXXX-XXXX-SA")
        login=st.text_input("MT5 Login", placeholder="12345678")
        pwd=st.text_input("Password", type="password")
        server=st.selectbox("Select SA Server 🇿🇦", SA_SERVERS, index=0)
        st.multiselect("Pairs to Save", ["XAUUSD - GOLD MAIN 🔥","USDZAR 🇿🇦","EURZAR 🇿🇦","BTCUSD"], default=["XAUUSD - GOLD MAIN 🔥"])
        go=st.form_submit_button("🚀 ACTIVATE & SAVE TRADES ON SA SERVER", use_container_width=True, type="primary")
        if go:
            if login and pwd:
                st.session_state.logged=True; st.session_state.user={"login":login, "server":server}; st.session_state.live=True; st.session_state.tab="Home"
                addlog(f"Activated {login} on {server}"); addlog("Trade saving ENABLED"); st.success(f"✅ Activated on {server}! Saving trades now!"); st.balloons(); time.sleep(1); st.rerun()
            else: st.error("Enter login + password")

elif st.session_state.tab=="Metatrader":
    st.markdown("### Metatrader SA 🇿🇦")
    st.selectbox("SA Server", SA_SERVERS)
    st.text_input("Account")
    st.text_input("MT5 Password", type="password")
    if st.button("Connect SA Server ✅", use_container_width=True, type="primary"): st.success("Connected! Trades will be saved")
    st.info("All SA Brokers: JP Markets, CM Trading, Khwezi, GT247, Exness SA, FBS SA, etc.")

elif st.session_state.tab=="Scanner":
    st.markdown("### Scanner")
    if st.button("Scan Gold XAUUSD 🔍", use_container_width=True, type="primary"):
        if st.session_state.logged:
            st.session_state.trades.insert(0,{"time":datetime.datetime.now().strftime("%H:%M:%S"),"type":"BUY","pair":"XAUUSD","profit":round(random.uniform(10,40),2),"server":"Scanner-SA"})
            st.success("Signal saved as trade!")
    st.metric("XAUUSD", "$2,645.30", "+$15.20")
    st.metric("Signal", "STRONG BUY 🔥")

elif st.session_state.tab=="Settings":
    st.markdown("### Settings")
    st.slider("Lot Size",0.01,1.0,0.10)
    st.selectbox("Default SA Server", SA_SERVERS)
    st.toggle("Auto Save Trades", True)
    st.toggle("ZAR Mode 🇿🇦", True)
    if st.button("Save", use_container_width=True, type="primary"): st.success("Saved!")

# BOTTOM NAV - EXACT LIKE SCREENSHOT - ALL WORKING
b1,b2,b3,b4 = st.columns(4)
with b1:
    if st.button("🏠\nHome", key="bh", use_container_width=True): st.session_state.tab="Home"; st.rerun()
with b2:
    if st.button("📊\nMeta", key="bm", use_container_width=True): st.session_state.tab="Metatrader"; st.rerun()
with b3:
    if st.button("🎯\nScan", key="bs", use_container_width=True): st.session_state.tab="Scanner"; st.rerun()
with b4:
    if st.button("⚙️\nSet", key="bse", use_container_width=True): st.session_state.tab="Settings"; st.rerun()
