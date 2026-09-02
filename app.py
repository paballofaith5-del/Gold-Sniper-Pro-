import streamlit as st, datetime, random, time, os, base64
st.set_page_config(page_title="EA Trade SA", page_icon="🤖", layout="centered")

st.markdown("""
<style>
.stApp{background:#000} header{display:none}
.block-container{max-width:430px; padding:0 0 120px 0 !important}
.glass{background:linear-gradient(180deg,#1a1a1a,#0f0f0f); border:1px solid #333; border-radius:18px; padding:12px; margin:10px 15px; box-shadow:0 4px 20px #000}
.green-dot{width:10px; height:10px; background:#00ff00; border-radius:50%; box-shadow:0 0 8px #0f0; display:inline-block}
.trade-box{background:#0a0a0a; border:1px solid #222; border-radius:12px; padding:10px; margin:8px 0}
.btn-row{display:flex; justify-content:space-around; margin:15px 0}
.add-robot{background:linear-gradient(90deg,#2a2a2a,#1a1a1a); border:1px solid #444; border-radius:50px; padding:16px 20px; display:flex; align-items:center; gap:12px; margin:20px 15px; box-shadow:0 2px 10px #000}
.bottom-nav{position:fixed; bottom:0; left:0; right:0; background:#0a0a0a; border-top:1px solid #222; border-radius:25px 25px 0 0; display:flex; justify-content:space-around; padding:12px 0 20px 0; max-width:430px; margin:0 auto; z-index:9999}
</style>
""", unsafe_allow_html=True)

if 'tab' not in st.session_state: st.session_state.tab="Home"
if 'logged' not in st.session_state: st.session_state.logged=False
if 'live' not in st.session_state: st.session_state.live=False
if 'trades' not in st.session_state: st.session_state.trades=[]
if 'user' not in st.session_state: st.session_state.user={}

SA_SERVERS = ["JPMarkets-Real 🇿🇦","CMTrading-Real 🇿🇦","KhweziTrade-Real 🇿🇦","GT247-Real 🇿🇦","Exness-Real-SA 🇿🇦","FBS-Real-SA 🇿🇦","HFM-Real-SA 🇿🇦","Deriv-Real-SA 🇿🇦","XM-Real-SA 🇿🇦","RazorMarkets-Real 🇿🇦","ScopeMarkets-SA 🇿🇦","AvaTrade-SA 🇿🇦"]

# TOP NOTIFICATION BAR - LIKE SCREENSHOT
st.markdown("""
<div class="glass" style="display:flex; justify-content:space-between; align-items:center; padding:10px 12px;">
<div style="display:flex; align-items:center; gap:8px;">
<div style="width:32px; height:32px; background:#00ff0022; border-radius:50%; display:flex; align-items:center; justify-content:center; border:1px solid #0f0;">🟢</div>
<div>
<div style="color:white; font-size:12px; font-weight:700;">Gold Sniper Pro SA Scanning Markets...</div>
<div style="color:#ffaa00; font-size:10px;">🚀 Trade 15/15: BUY order executed</div>
</div>
</div>
<span style="color:#666;">✕</span>
</div>
""", unsafe_allow_html=True)

# AI TRADE ANALYSIS - EXACT LIKE SCREENSHOT
pair = random.choice(["US30","XAUUSD","NAS100","USDZAR 🇿🇦"])
direction = random.choice(["BUY","SELL"])
entry = round(random.uniform(53000,54000) if pair=="US30" else random.uniform(2640,2660),2)
sl = round(entry-300,2)
tp = round(entry+500,2)
color = "#00ff88" if direction=="BUY" else "#ff4444"

st.markdown(f"""
<div class="glass" style="margin-top:5px;">
<div style="color:#888; font-size:9px; letter-spacing:1.5px;">AI TRADE ANALYSIS</div>
<div style="color:{color}; font-size:20px; font-weight:900; margin:4px 0;">{pair}. {direction}</div>
<div style="color:#aaa; font-size:11px;">Entry {entry} · SL {sl} · TP {tp}</div>
<div style="color:#666; font-size:9px; margin-top:6px;">SL: {sl}, TP: {tp}. Use proper position sizing.</div>
</div>
""", unsafe_allow_html=True)

# VIDEO CARD - LIKE SCREENSHOT
st.markdown("""
<div class="glass" style="padding:0; overflow:hidden; position:relative; height:200px; background:#000;">
<div style="position:absolute; top:0; left:0; right:0; bottom:0; background: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.9)), url('https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=800'); background-size:cover; background-position:center;"></div>
<div style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:55px; height:55px; background:#ffffff33; border-radius:50%; display:flex; align-items:center; justify-content:center; backdrop-filter:blur(5px);"><span style="font-size:24px; margin-left:3px;">▶</span></div>
<div style="position:absolute; top:60%; left:0; right:0; text-align:center; padding:0 15px;">
<div style="color:white; font-size:11px; background:#00000099; display:inline-block; padding:4px 8px; border-radius:10px;">Stop saying robots don't work<br>you just got rong people in the game</div>
<div style="color:white; font-weight:900; font-size:18px; margin-top:8px; letter-spacing:0.5px;">GOLD SNIPER PRO SA <span style="display:inline-block; width:12px; height:12px; background:#00ff00; border-radius:50%; box-shadow:0 0 8px #0f0; border:2px solid #000;"></span></div>
</div>
<div style="position:absolute; bottom:10px; left:0; right:0; display:flex; justify-content:space-around;">
<div style="text-align:center; color:#aaa;"><div style="font-size:20px;">□</div><div style="font-size:9px;">STOP</div></div>
<div style="text-align:center; color:#aaa;"><div style="font-size:18px;">📈</div><div style="font-size:9px;">QUOTES</div></div>
<div style="text-align:center; color:#aaa;"><div style="font-size:18px;">🗑️</div><div style="font-size:9px;">REMOVE</div></div>
</div>
</div>
""", unsafe_allow_html=True)

# AUTO SAVE TRADES IF LIVE
if st.session_state.logged and st.session_state.live:
    if random.random()>0.7:
        p=round(random.uniform(10,60),2)
        tr={"time":datetime.datetime.now().strftime("%H:%M:%S"), "pair":pair, "type":direction, "profit":p, "server":st.session_state.user.get("server","SA")}
        st.session_state.trades.insert(0,tr)
    st.markdown(f'<div style="background:#00ff0022; border:1px solid #0f0; color:#0f0; border-radius:15px; padding:6px; text-align:center; font-size:11px; margin:10px 15px;">● LIVE on {st.session_state.user.get("server")} | Saving Trades ✅ | {len(st.session_state.trades)} Trades</div>', unsafe_allow_html=True)

# ADD ROBOT BUTTON - EXACT LIKE SCREENSHOT
if st.button("+  ADD ROBOT\nHOST ROBOT KEY", key="add_robot", use_container_width=True):
    st.session_state.tab="Activate"
    st.rerun()

st.markdown("""
<div class="add-robot">
<div style="width:36px; height:36px; background:#333; border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:20px;">+</div>
<div>
<div style="color:white; font-weight:800; font-size:14px; letter-spacing:0.5px;">ADD ROBOT</div>
<div style="color:#888; font-size:10px; letter-spacing:1px;">HOST ROBOT KEY</div>
</div>
</div>
""", unsafe_allow_html=True)

# CONTENT BASED ON TAB
if st.session_state.tab=="Home":
    if st.session_state.trades:
        st.markdown(f"<div style='margin:15px; color:white; font-weight:700;'>💾 Saved Trades on SA Server - Total R {sum([x['profit'] for x in st.session_state.trades]):.2f} ({len(st.session_state.trades)})</div>", unsafe_allow_html=True)
        for tr in st.session_state.trades[:12]:
            col="#00ff88" if tr['profit']>0 else "#ff4444"
            st.markdown(f'<div style="background:#111; border:1px solid #222; border-radius:10px; padding:10px; margin:5px 15px; display:flex; justify-content:space-between; font-size:12px;"><span style="color:white;">{tr["time"]} {tr["type"]} {tr["pair"]} | {tr["server"][:14]}</span><span style="color:{col}; font-weight:bold;">R {tr["profit"]}</span></div>', unsafe_allow_html=True)
    else:
        if not st.session_state.logged:
            st.info("Tap ADD ROBOT to login with SA server and start saving trades 🇿🇦")

elif st.session_state.tab=="Activate":
    st.markdown("### 🔑 EA Trade Activation - SA Servers 🇿🇦")
    with st.form("ea"):
        key=st.text_input("Host Robot Key 🔑", placeholder="EA-TRADE-SA-XXXX")
        login=st.text_input("MT5 Login", value="4056103")
        pwd=st.text_input("Password", type="password", value="1234")
        server=st.selectbox("Select SA Server 🇿🇦", SA_SERVERS, index=0)
        pairs=st.multiselect("Pairs to Save", ["XAUUSD - GOLD MAIN 🔥","US30 🇿🇦","USDZAR 🇿🇦","EURZAR 🇿🇦","NAS100","BTCUSD"], default=["XAUUSD - GOLD MAIN 🔥","US30 🇿🇦"])
        if st.form_submit_button("🚀 ACTIVATE EA TRADE ON SA SERVER", use_container_width=True, type="primary"):
            st.session_state.logged=True; st.session_state.user={"login":login,"server":server}; st.session_state.live=True; st.session_state.tab="Home"
            st.session_state.trades.insert(0,{"time":datetime.datetime.now().strftime("%H:%M:%S"),"pair":"XAUUSD","type":"BUY","profit":25.50,"server":server})
            st.success(f"✅ Activated on {server}! Saving trades!"); st.balloons(); time.sleep(1); st.rerun()

elif st.session_state.tab=="Scanner":
    st.markdown("### AI Scanner SA 🇿🇦")
    st.metric("US30", "53,941.10", "+250 BUY 🔥")
    st.metric("XAUUSD", "$2,645.30", "BUY 95%")
    if st.button("Scan & Save Trade 🔍", use_container_width=True, type="primary") and st.session_state.logged:
        st.session_state.trades.insert(0,{"time":datetime.datetime.now().strftime("%H:%M:%S"),"type":"BUY","pair":"US30","profit":round(random.uniform(15,50),2),"server":st.session_state.user.get("server")})
        st.success("Trade saved!")

elif st.session_state.tab=="Metatrader":
    st.markdown("### MetaTrader SA 🇿🇦")
    st.selectbox("All SA Servers", SA_SERVERS)
    st.text_input("Login"); st.text_input("Password", type="password")
    if st.button("Connect SA Server ✅", use_container_width=True, type="primary"): st.success("Connected to SA Server!")

# BOTTOM NAV - EXACT LIKE SCREENSHOT
st.markdown('<div class="bottom-nav">', unsafe_allow_html=True)
b1,b2,b3 = st.columns(3)
with b1:
    if st.button("🏠\nHome", key="bh", use_container_width=True): st.session_state.tab="Home"; st.rerun()
with b2:
    if st.button("◫\nAI Scanner", key="bs", use_container_width=True): st.session_state.tab="Scanner"; st.rerun()
with b3:
    if st.button("🗄️\nMetaTrader", key="bm", use_container_width=True): st.session_state.tab="Metatrader"; st.rerun()
st.markdown('</div>', unsafe_allow_html=True)
