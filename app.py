import streamlit as st
st.set_page_config(page_title="Gold Sniper Bot", page_icon="🐼", layout="centered")
st.markdown("""
<style>
.stApp{background:#000}
header{display:none}
.block-container{max-width:430px; padding-top:0px; padding-bottom:120px}
.panda-circle{width:250px; height:250px; margin:25px auto 15px auto; border-radius:50%; border:4px solid #FFD700; box-shadow:0 0 40px #FFD70088, 0 0 30px #ff000088; overflow:hidden; background:#111}
.control-bar{background:linear-gradient(90deg,#0a0a0a,#1a1a1a); border:2px solid #ff2222; border-radius:60px; padding:8px 15px; display:flex; justify-content:space-between; align-items:center; box-shadow:0 0 25px #ff000066; margin:25px 5px 10px 5px; height:80px}
.pair-card{background:#111; border:1px solid #FFD70033; border-radius:10px; padding:10px; margin:5px 0}
</style>
""", unsafe_allow_html=True)

if 'tab' not in st.session_state: st.session_state.tab="Home"
if 'live' not in st.session_state: st.session_state.live=False
if 'pairs' not in st.session_state: st.session_state.pairs=["XAUUSD - GOLD MAIN 🔥"]
if 'logs' not in st.session_state: st.session_state.logs=["[12:37] Bot ready... Waiting for START"]

sa_servers = [
"JPMarkets-Real", "CMTrading-Real", "KhweziTrade-Real", "GT247-Real", 
"Exness-Real-SA", "FBS-Real-SA", "HFM-Real-SA", "Deriv-Real-SA",
"Tickmill-Real-SA", "XM-Real-SA", "JustMarkets-Real-SA", "RazorMarkets-Real",
"ScopeMarkets-Real-SA", "AvaTrade-Real-SA"
]

def add_log(msg):
    st.session_state.logs.append(msg)
    if len(st.session_state.logs)>50: st.session_state.logs.pop(0)

# TOP PANDA
st.markdown("""
<div class="panda-circle">
<img src="https://cdn.pixabay.com/photo/2023/12/09/10/05/panda-8438367_1280.jpg" style="width:100%; height:100%; object-fit:cover; filter: sepia(1) hue-rotate(10deg) saturate(1.5);">
</div>
<div style="text-align:center;">
<h1 style="color:white; font-size:32px; font-weight:900; margin:10px 0 2px 0;">Gold Sniper Bot</h1>
<p style="color:#D4AF37; font-size:14px;">Powerful Gold Scalping Bot 🇿🇦</p>
</div>
""", unsafe_allow_html=True)

# STATUS
if st.session_state.live:
    st.markdown('<div style="background:#00ff0022; border:1px solid #00ff00; color:#00ff00; border-radius:20px; padding:8px; text-align:center; font-weight:bold;">● LIVE - Sniping GOLD XAUUSD on SA Server</div>', unsafe_allow_html=True)
else:
    st.markdown('<div style="background:#FFD70022; border:1px solid #FFD70066; color:#FFD700; border-radius:20px; padding:8px; text-align:center;">○ STOPPED - Press START</div>', unsafe_allow_html=True)

# CONTROL BAR - ALL BUTTONS WORKING NOW
c1,c2,c3 = st.columns([1,2,1])
with c1:
    if st.button("📈\nPAIRS", use_container_width=True):
        st.session_state.tab="Pairs"
        add_log("[12:38] Opened PAIRS selector")
with c2:
    if st.button("▶ START", use_container_width=True, type="primary"):
        if not st.session_state.live:
            st.session_state.tab="Activate"
            add_log("[12:38] START pressed - Need activation")
        else:
            st.session_state.live=False
            add_log("[12:38] Bot STOPPED by user")
            st.warning("Bot STOPPED")
with c3:
    if st.button("≡\nLOGS", use_container_width=True):
        st.session_state.tab="Logs"
        add_log("[12:38] Opened LOGS")

st.markdown('<div style="text-align:center; margin-top:8px; font-size:11px; color:#666;">powered by <b style="color:#ff2222;">EAConnect SA</b></div>', unsafe_allow_html=True)

# TABS LOGIC
if st.session_state.tab=="Home":
    st.markdown("### 🤖 Robot List")
    st.markdown(f'<div class="pair-card" style="display:flex; justify-content:space-between;"><span style="color:white;">Gold Sniper Bot 🇿🇦</span><span style="color:{"#0f0" if st.session_state.live else "#f00"}">● {"ACTIVE" if st.session_state.live else "STOPPED"}</span></div>', unsafe_allow_html=True)
    st.info(f"Selected Pairs: {', '.join(st.session_state.pairs)}")
    st.metric("Today Profit", "R 1,247.50" if st.session_state.live else "R 0.00", "+12.5%" if st.session_state.live else "0%")

elif st.session_state.tab=="Pairs":
    st.markdown("### 📈 Select Trading Pairs")
    pairs = st.multiselect("Choose pairs to snipe:", ["XAUUSD - GOLD MAIN 🔥","EURUSD","GBPUSD","USDZAR 🇿🇦","EURZAR 🇿🇦","BTCUSD","NAS100","US30"], default=st.session_state.pairs)
    if st.button("Save Pairs ✅", use_container_width=True, type="primary"):
        st.session_state.pairs=pairs
        add_log(f"[12:38] Pairs saved: {pairs}")
        st.session_state.tab="Home"
        st.success("Pairs Saved!")
        st.rerun()

elif st.session_state.tab=="Logs":
    st.markdown("### ≡ Live Logs")
    for log in reversed(st.session_state.logs[-20:]):
        st.code(log)
    if st.button("Clear Logs", use_container_width=True):
        st.session_state.logs=["[12:38] Logs cleared"]
        st.rerun()
    if st.button("Back to Home", use_container_width=True):
        st.session_state.tab="Home"
        st.rerun()

elif st.session_state.tab=="Activate":
    st.markdown("### 🔑 EA Connect Activation - SA Servers 🇿🇦")
    with st.form("activate"):
        st
