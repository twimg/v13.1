import streamlit as st
import pandas as pd
import random
import datetime

st.set_page_config(page_title="Club Strive - v13", layout="wide")

# 背景画像設定（モバイル対応）
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1605733160314-4ed6c1dc4f83");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>⚽ Club Strive - Mobile</h1>", unsafe_allow_html=True)

# クラブと選手データ
teams = ['ストライバーFC', 'レグルスSC', 'アルマーレFC', 'ブラッドフォールズ', 'シルフィード東京', 'バルデナールFC']
players_df = pd.read_csv("players.csv")

# UI
menu = st.selectbox("メニューを選択", ["ホーム", "選手一覧", "試合", "スカウト", "移籍交渉"])

if menu == "ホーム":
    st.subheader("🏠 ホーム画面")
    st.write("ようこそ、クラブストライブへ！")
elif menu == "選手一覧":
    st.subheader("📋 選手一覧")
    st.dataframe(players_df)
elif menu == "試合":
    st.subheader("⚔️ 試合シミュレーター")
    home = st.selectbox("ホームチーム", teams)
    away = st.selectbox("アウェイチーム", [t for t in teams if t != home])
    if st.button("試合開始！"):
        result = {
            '日付': datetime.date.today(),
            'ホーム': home,
            'アウェイ': away,
            'スコア': f"{random.randint(0,3)} - {random.randint(0,3)}",
            'ポゼッション': f"{random.randint(45,55)}% vs {random.randint(45,55)}%",
        }
        st.write(result)
elif menu == "スカウト":
    st.subheader("🔍 スカウト画面（準備中）")
    st.info("今後実装予定のスカウト検索機能です。")
elif menu == "移籍交渉":
    st.subheader("💼 移籍交渉画面（準備中）")
    st.warning("移籍交渉インターフェースは開発中です。")
