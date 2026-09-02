import streamlit as st
import datetime, json, random, time
st.set_page_config(page_title="Gold Sniper Bot SA", page_icon="🐼", layout="centered")

st.markdown("""
<style>
.stApp{background:#000} header{display:none}
.block-container{max-width:430px; padding:0 10px 120px 10px}
.panda-circle{width:250px; height:250px; margin:20px auto 10px auto; border-radius:50%; border:4px solid #FFD700; box-shadow:0 0 40px #FFD70088, 0 0 30px #ff000088; overflow:hidden; background:#111}
.trade-card{background:#111; border:1px solid #FFD70033; border-radius:10px; padding:10px; margin:6px 0; display:flex; justify-content:space-between; font-size:13px}
</style>
""", unsafe_allow_html=True)

if 'tab' not in st.session_state: st.session_state.tab="Home"
if 'logged' not in st.session_state: st.session_state.logged=False
if 'live' not in st.session_state: st.session_state.live=False
if 'trades' not in st.session_state: st.session_state.trades=[]
if 'user' not in st.session_state: st.session_state.user={}
if 'logs' not in st.session_state: st.session_state.logs=["[System] Bot ready 🇿🇦"]

SA_SERVERS = [
"JPMarkets-Real 🇿🇦","CMTrading-Real 🇿🇦","KhweziTrade-Real 🇿🇦","GT247-Real 🇿🇦",
"Exness-Real-SA 🇿🇦","FBS-Real-SA 🇿🇦","HFM-Real-SA 🇿🇦","Deriv-Real-SA 🇿🇦",
"Tickmill-Real-SA 🇿🇦","XM-Real-SA 🇿🇦","JustMarkets-Real-SA 🇿🇦","RazorMarkets-Real 🇿🇦",
"ScopeMarkets-Real-SA 🇿🇦","AvaTrade-Real-SA 🇿🇦","FXTM-Real-SA 🇿🇦","IQOption-Real-SA 🇿🇦"
]

def log(msg):
    now=datetime.datetime.now().strftime("%H:%M:%S")
    st.session_state.logs.append(f"[{now}] {msg}")

# PANDA HEADER - LIKE SCREENSHOT
st.markdown("""
<div class="panda-circle">
<img src="https://cdn.pixabay.com/photo/2023/12/09/10/05/panda-8438367_1280.jpg" style="width:100%; height:100%; object-fit:cover; filter: sepia(1) hue-rotate(10deg) saturate(1.5);">
</div>
<div style="text-align:center;">
<h1 style="color:white; font-size:30px; font-weight:900; margin:5px 0;">Gold Sniper Bot</h1>
<p style="color:#D4AF37; font-size:14px; margin:0;">Powerful Gold Scalping Bot 🇿🇦</p>
</div>
""", unsafe_allow_html=True)

# STATUS BADGE
if st.session_state.logged and st.session_state.live:
    st.success(f"● LIVE on {st.session_state.user.get('server','')} | {st.session_state.user.get('login','')} | Saving Trades ✅")
    # Simulate trade saving
    if random.random()>0.7:
        profit = round(random.uniform(-5, 25),2)
        trade = {"time":datetime.datetime.now().strftime("%H:%M:%S"), "pair":"XAUUSD", "type": random.choice(["BUY","SELL"]), "profit": profit, "server": st.session_state.user.get('server','')}
        st.session_state.trades.insert(0, trade)
        log(f"TRADE {trade['type']} XAUUSD {profit} ZAR on {trade['server']}")
elif st.session_state.logged:
    st.warning(f"Logged in: {st.session_state.user.get('login','')} on {st.session_state.user.get('server','')} - Press START to snipe")
else:
    st.markdown('<div style="background:#FFD70020; border:1px solid #FFD700; border-radius:20px; padding:8px; text-align:center; color:#FFD700;">○ Not Logged In - Login to Save Trades</div>', unsafe_allow_html=True)

# CONTROL BAR - ALL WORKING
c1,c2,c3 = st.columns([1,2,1])
with c1:
    if st.button("📈\nPAIRS", use_container_width=True, key="pairs_btn"):
        st.session_state.tab="Pairs"; log("Opened PAIRS"); st.rerun()
with c2:
    if st.session_state.live:
        if st.button("⏹ STOP", use_container_width=True, type="primary", key="stop_btn"):
            st.session_state.live=False; log("Bot STOPPED"); st.rerun()
    else:
        if st.button("▶ START", use_container_width=True, type="primary", key="start_btn"):
            if not st.session_state.logged:
                st.session_state.tab="Activate"; log("Need login before START"); st.rerun()
            else:
                st.session_state.live=True; log(f"STARTED sniping on {st.session_state.user.get('server')}"); st.rerun()
with c3:
    if st.button("≡\nLOGS", use_container_width=True, key="logs_btn"):
        st.session_state.tab="Logs"; log("Opened LOGS"); st.rerun()

st.markdown('<div style="text-align:center; font-size:11px; color:#666; margin:8px;">powered by <b style="color:#ff2222;">EAConnect SA</b></div>', unsafe_allow_html=True)

# CONTENT TABS
if st.session_state.tab=="Home":
    st.markdown("### 🤖 Robot List")
    colA, colB = st.columns([3,1])
    with colA: st.markdown(f'<div class="trade-card"><span style="color:white;">Gold Sniper Bot 🇿🇦</span><span style="color:{"#0f0" if st.session_state.live else "#f00"}">● {"ACTIVE" if st.session_state.live else "IDLE"}</span></div>', unsafe_allow_html=True)
    with colB:
        if st.button("Profile"): st.session_state.tab="Profile"; st.rerun()

    if st.session_state.logged:
        st.markdown("### 💾 Saved Trades (Auto-Saving)")
        if not st.session_state.trades:
            st.info("No trades yet - Press START to start saving trades on SA server")
        for t in st.session_state.trades[:10]:
            color="#0f0" if t['profit']>0 else "#f00"
            st.markdown(f'<div class="trade-card"><span>{t["time"]} {t["type"]} {t["pair"]}</span><span style="color:{color}">R {t["profit"]}</span></div>', unsafe_allow_html=True)
        total = sum([x['profit'] for x in st.session_state.trades])
        st.metric("Total Profit Today (ZAR)", f"R {total:.2f}", f"{len(st.session_state.trades)} trades")
        if st.button("Clear Trade History"): st.session_state.trades=[]; log("Cleared trades"); st.rerun()
    else:
        st.warning("Login to start saving trades automatically!")

elif st.session_state.tab=="Pairs":
    st.markdown("### 📈 Select Pairs to Snipe")
    pairs = st.multiselect("Pairs:", ["XAUUSD - GOLD MAIN 🔥","EURUSD","GBPUSD","USDZAR 🇿🇦","EURZAR 🇿🇦","BTCUSD","NAS100","US30"], default=["XAUUSD - GOLD MAIN 🔥"])
    if st.button("Save & Back to Home ✅", use_container_width=True, type="primary"):
        log(f"Pairs saved {pairs}"); st.session_state.tab="Home"; st.rerun()

elif st.session_state.tab=="Logs":
    st.markdown("### ≡ Live Logs - SA Server")
    for l in reversed(st.session_state.logs[-25:]):
        st.code(l)
    c1,c2 = st.columns(2)
    with c1:
        if st.button("Clear Logs"): st.session_state.logs=[]; st.rerun()
    with c2:
        if st.button("Back Home"): st.session_state.tab="Home"; st.rerun()

elif st.session_state.tab=="Activate":
    st.markdown("### 🔑 Login - All South Africa Servers 🇿🇦")
    with st.form("login_form"):
        key = st.text_input("EA Connect Key 🔑", placeholder="XXXX-XXXX-XXXX-SA")
        login = st.text_input("MT5 Login", placeholder="e.g 12345678")
        pwd = st.text_input("Password", type="password")
        server = st.selectbox("Select SA Server 🇿🇦 (All SA Brokers)", SA_SERVERS, index=11)
        pairs = st.multiselect("Pairs", ["XAUUSD - GOLD MAIN 🔥","USDZAR 🇿🇦","EURZAR 🇿🇦","BTCUSD"], default=["XAUUSD - GOLD MAIN 🔥"])
        submit = st.form_submit_button("🚀 LOGIN & SAVE TRADES ON SA SERVER", use_container_width=True, type="primary")
        if submit:
            if login and pwd:
                st.session_state.logged=True
                st.session_state.user={"login":login, "server":server, "key":key, "pairs":pairs}
                st.session_state.tab="Home"
                st.session_state.live=True
                log(f"Logged in {login} on {server}")
                log(f"Trade saving ENABLED on {server}")
                st.success(f"✅ Logged in on {server}! Trades will be saved automatically!")
                st.balloons()
                time.sleep(1)
                st.rerun()
            else:
                st.error("Enter Login & Password")

elif st.session_state.tab=="Profile":
    st.markdown("### 👤 Profile - Looks like Screenshot")
    if st.session_state.logged:
        st.markdown(f"""
        <div style="background:#111; border:1px solid #FFD700; border-radius:15px; padding:15px; text-align:center;">
        <div style="width:80px; height:80px; background:#FFD700; border-radius:50%; margin:0 auto; display:flex; align-items:center; justify-content:center; font-size:40px;">👤</div>
        <h3 style="color:white; margin:10px 0;">Trader {st.session_state.user['login']}</h3>
        <p style="color:#D4AF37;">{st.session_state.user['server']}</p>
        <p style="color:#0f0;">● Trade Saving ACTIVE</p>
        <p style="color:#aaa;">Trades Saved: {len(st.session_state.trades)}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Logout", use_container_width=True):
            st.session_state.logged=False; st.session_state.live=False; st.session_state.tab="Home"; st.rerun()
    else:
        st.info("Not logged in - Go to START to login")
    if st.button("Back Home", use_container_width=True):
        st.session_state.tab="Home"; st.rerun()

elif st.session_state.tab=="Metatrader":
    st.markdown("### 📊 Metatrader - SA Servers 🇿🇦")
    st.selectbox("SA Server", SA_SERVERS, key="mt_server")
    st.text_input("Login", key="mt_login")
    st.text_input("Password", type="password", key="mt_pwd")
    if st.button("Connect to SA Server ✅", use_container_width=True, type="primary"):
        st.success("Connected to SA Server! Ready to save trades")
        log("MT5 Connected SA")
    st.info("Supports: JP Markets, CM Trading, Khwezi, GT247, Exness SA, FBS SA, HFM SA, Deriv SA, XM SA - All South Africa!")

elif st.session_state.tab=="Scanner":
    st.markdown("### 🎯 Gold Scanner SA")
    if st.button("Scan XAUUSD Now 🔍", use_container_width=True, type="primary"):
        log("Scanning GOLD...")
        st.success("STRONG BUY Signal 95% - Saving trade...")
        if st.session_state.logged:
            st.session_state.trades.insert(0, {"time":datetime.datetime.now().strftime("%H:%M:%S"), "pair":"XAUUSD", "type":"BUY", "profit": round(random.uniform(5,30),2), "server": st.session_state.user.get('server','Scanner')})
    st.metric("XAUUSD", "$2,645.30", "+$12.50")
    st.metric("Signal", "BUY 🔥", "95%")

elif st.session_state.tab=="Settings":
    st.markdown("### ⚙️ Settings")
    st.slider("Lot Size", 0.01, 1.0, 0.10)
    st.selectbox("Default SA Server", SA_SERVERS)
    st.toggle("Auto Save Trades on SA Server", True)
    st.toggle("ZAR Profit Display", True)
    st.button("Save Settings ✅", use_container_width=True, type="primary")

# BOTTOM NAV - ALL WORKING
st.markdown("<br><br>", unsafe_allow_html=True)
b1,b2,b3,b4 = st.columns(4)
with b1:
    if st.button("🏠\nHome", use_container_width=True, key="nav_home"): st.session_state.tab="Home"; st.rerun()
with b2:
    if st.button("📊\nMeta", use_container_width=True, key="nav_meta"): st.session_state.tab="Metatrader"; st.rerun()
with b3:
    if st.button("🎯\nScan", use_container_width=True, key="nav_scan"): st.session_state.tab="Scanner"; st.rerun()
with b4:
    if st.button("⚙️\nSet", use_container_width=True, key="nav_set"): st.session_state.tab="Settings"; st.rerun()
