import streamlit as st
st.set_page_config(page_title="Gold Sniper Bot", page_icon="🐼", layout="centered")
st.markdown("""
<style>
.stApp{background:#000} div[data-testid="stHeader"]{display:none}
.block-container{max-width:430px; padding-top:0px; padding-bottom:120px}
.panda-circle{width:250px; height:250px; margin:25px auto 15px auto; border-radius:50%; border:4px solid #FFD700; box-shadow:0 0 40px #FFD70088, 0 0 30px #ff000088; overflow:hidden; background:#111}
.control-bar{background:linear-gradient(90deg,#0a0a0a,#1a1a1a); border:2px solid #ff2222; border-radius:60px; padding:8px 15px; display:flex; justify-content:space-between; align-items:center; box-shadow:0 0 25px #ff000066; margin:35px 5px 10px 5px; height:80px}
.start-rect{width:130px; height:55px; background:#ff1a1a; border-radius:15px; display:flex; align-items:center; justify-content:center; color:white; font-weight:900; box-shadow:0 0 20px #ff0000aa}
.robot-pill{background:#111; border:1px solid #FFD70044; border-radius:12px; padding:14px; display:flex; justify-content:space-between; margin:10px 0}
.bottom-nav{position:fixed; bottom:0; left:0; right:0; background:#0a0a0a; border-top:1px solid #222; display:flex; justify-content:space-around; padding:12px 0 20px 0; max-width:430px; margin:0 auto; z-index:999}
</style>
""", unsafe_allow_html=True)

if 'show' not in st.session_state: st.session_state.show=False
if 'live' not in st.session_state: st.session_state.live=False

st.markdown("""
<div class="panda-circle">
<img src="https://cdn.pixabay.com/photo/2023/12/09/10/05/panda-8438367_1280.jpg" style="width:100%; height:100%; object-fit:cover; filter: sepia(1) hue-rotate(10deg) saturate(1.5);">
</div>
<div style="text-align:center;">
<h1 style="color:white; font-size:32px; font-weight:900; margin:15px 0 5px 0;">Gold Sniper Bot</h1>
<p style="color:#D4AF37; font-size:15px;">Powerful Gold Scalping Bot</p>
</div>
<div class="control-bar">
<div style="text-align:center; color:#D4AF37;"><div>📈</div><div style="font-size:11px;">PAIRS</div></div>
<div class="start-rect">▶ START</div>
<div style="text-align:center; color:#D4AF37;"><div>≡</div><div style="font-size:11px;">LOGS</div></div>
</div>
<div style="text-align:center; margin-top:12px; font-size:12px; color:#666;">powered by <b style="color:#ff2222;">EAConnect</b></div>
<div style="display:flex; gap:15px; margin-top:30px;">
<div style="border:1px solid #D4AF37; border-radius:20px; padding:6px 12px; color:#D4AF37; font-size:12px;">🤖 Robot List</div>
<div class="robot-pill" style="flex:1;"><div style="color:white;">Gold Sniper Bot</div><div style="color:#0f0; font-size:11px;">● ACTIVE</div></div>
</div>
<div class="bottom-nav">
<div style="text-align:center; color:#D4AF37;">🏠<br><small>Home</small></div>
<div style="text-align:center; color:#666;">📊<br><small>Metatrader</small></div>
<div style="text-align:center; color:#666;">🎯<br><small>Scanner</small></div>
<div style="text-align:center; color:#666;">⚙️<br><small>Settings</small></div>
</div>
""", unsafe_allow_html=True)

if st.button("▶ START BOT - TAP HERE", use_container_width=True, type="primary"):
    st.session_state.show=True

if st.session_state.show:
    st.markdown("---")
    st.markdown("<h3 style='color:#FFD700; text-align:center;'>🔑 EA Connect Activation</h3>", unsafe_allow_html=True)
    with st.form("f"):
        st.text_input("EA Connect Key 🔑", placeholder="XXXX-XXXX-XXXX")
        st.text_input("MT5 Login", placeholder="12345678")
        st.text_input("Password", type="password")
        st.text_input("Server", value="RazorMarkets-Real")
        st.multiselect("Pairs", ["XAUUSD - GOLD MAIN 🔥","EURUSD","GBPUSD","BTCUSD","NAS100"], default=["XAUUSD - GOLD MAIN 🔥"])
        if st.form_submit_button("🚀 ACTIVATE GOLD SNIPER", use_container_width=True, type="primary"):
            st.success("✅ Gold Sniper Bot ACTIVATED! Auto trading XAUUSD!")
            st.balloons()
            st.session_state.live=True

if st.session_state.live:
    st.markdown('<div style="background:#FFD70020; border:1px solid #FFD700; border-radius:10px; padding:10px; text-align:center; color:#FFD700;">● LIVE - Sniping GOLD XAUUSD...</div>', unsafe_allow_html=True)
