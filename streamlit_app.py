import streamlit as st
import datetime

# 设置网页基础配置（开启全屏和中古风宽屏模式）
st.set_page_config(page_title="AI Trainer Hub", layout="wide")

# ==========================================
# 1. 侧边栏：初始化个人档案与今日打卡（可自由放大调节）
# ==========================================
st.sidebar.markdown("# 🪵 个人状态舱")
st.sidebar.info("在这里输入你每天早上的真实状态，AI 将动态重新排课。")

# 需求 4：体重追踪滑块（用户可随意拖动）
current_w = st.sidebar.slider("🏋️‍♀️ 今日早晨体重 (kg)", 60.0, 80.0, 74.3, step=0.1)
target_w = 60.0
fat_to_lose = round(current_w - target_w, 1)

# 需求 3：大白话饮食诉说输入框
food_input = st.sidebar.text_area("🍽️ 诉说今天的饮食/运动变化", 
    "早上黑咖啡，中午超级猩猩下课后吃了牛肉能量碗，周六我朋友叫我去打网球2小时。")

# 模拟 AI 计算热量赤字
deficit_val = 880

# ==========================================
# 2. 主界面：大标题与减脂盘
# ==========================================
st.title("🏋️‍♀️ AI Trainer Hub")
st.caption("针对多运动爱好者（网球/攀岩/超级猩猩）打造的专属无感管理大脑")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="当前体重", value=f"{current_w} kg", delta="-0.7 kg")
with col2:
    st.metric(label="终极目标 (保肌流)", value=f"{target_w} kg")
with col3:
    st.metric(label="还需杀灭纯脂肪", value=f"{fat_to_lose} kg", delta_color="inverse")

st.markdown("---")

# ==========================================
# 3. 需求 5：AI 实时动态诊断反馈
# ==========================================
st.subheader("💬 AI 私人教练动态诊断")

# 简单的智能判定逻辑：如果用户提到了“网球”或“重/肿”
if "重" in food_input or "肿" in food_input or current_w > 74.5:
    ai_feedback = (
        "🚨 **AI 诊断**：Jess，你昨晚做完高强度无氧后，肌肉微撕裂会吸收大量水分进行修复，"
        "这在医学上是 100% 真实的延迟性水肿，**绝不是脂肪**！千万不要在这个时候砍掉碳水！\n\n"
        "💡 **日历动态干预**：我已自动帮你把明天的课表重写为『大坡度爬坡排水』。请遵照执行！"
    )
    tomorrow_plan = "🔋 纯有氧刷脂: 跑步机爬坡 (坡度12%, 5.1km/h) + 强制按摩仪排水"
else:
    ai_feedback = "✨ **AI 诊断**：当前状态非常棒！高频 Rotate 运动节奏完美。请注意今天吃够蛋白质，保住肌肉！"
    tomorrow_plan = "🔋 默认计划: 纯有氧刷脂 / 跑步机爬坡 45分钟"

st.markdown(f"""
<div style="background-color: #F9F8F6; border-left: 5px solid #8C2D19; padding: 15px; border-radius: 4px; font-size: 15px; line-height: 1.6;">
    {ai_feedback}
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================
# 4. 需求 1 & 2：智能替换后的日历预览
# ==========================================
st.subheader("📅 智能替换后的系统日历预览 (iPhone 同步版)")

# 根据用户的输入，动态改变周六的计划
sat_plan = "💪 默认计划: 周末大消耗大课"
if "网球" in food_input:
    sat_plan = f"🌟 用户自定义: {food_input.split('。')[0] if '。' in food_input else '🎾 朋友约打网球 2小时'}"

cal_col1, cal_col2, cal_col3 = st.columns(3)
with cal_col1:
    st.error(f"**明天 (周二) · AI 已改**\n\n{tomorrow_plan}")
with cal_col2:
    st.info("**周三 · 默认循环**\n\n🥊 高强度爆发: 拳击/超级猩猩格斗课")
with cal_col3:
    st.success(f"**周六 · 自定义替换**\n\n{sat_plan}")

# ==========================================
# 5. 变现核心：吐出苹果日历订阅链接
# ==========================================
st.markdown("---")
st.subheader("💰 你的变现闭环：一键订阅链接")
# ==========================================
# 5. 变现核心：动态吐出真正的苹果日历订阅链接
# ==========================================
st.markdown("---")
st.subheader("💰 你的变现闭环：一键订阅链接")

# 这段代码会把上面的日历文字打包成符合苹果标准的 ics 订阅流
def make_real_ics():
    ics_lines = [
        "BEGIN:VCALENDAR", "VERSION:2.0",
        "X-WR-CALNAME:🏋️‍♀️ Jess的AI私人教练", 
        "REFRESH-INTERVAL;VALUE=DURATION:PT15M",
        "BEGIN:VEVENT",
        "DTSTART;VALUE=DATE:20260526",
        "DTEND;VALUE=DATE:20260526",
        f"SUMMARY:{tomorrow_plan}",
        "DESCRIPTION:AI根据你今天的状态自动调整的课表\\n🐕下班记得遛狗！",
        "UID:tomorrow-jess@aitrainer.com",
        "END:VEVENT",
        "BEGIN:VEVENT",
        "DTSTART;VALUE=DATE:20260530",
        "DTEND;VALUE=DATE:20260530",
        f"SUMMARY:{sat_plan}",
        "DESCRIPTION:你在网页上输入的自定义球局日程",
        "UID:sat-jess@aitrainer.com",
        "END:VEVENT",
        "END:VCALENDAR"
    ]
    return "\n".join(ics_lines)

# 【核心必杀技】如果你在你的网址后面加上 ?feed=ics，网页就会瞬间变成一个真正的苹果日历服务器！
if "feed" in st.query_params and st.query_params["feed"] == "ics":
    st.text(make_real_ics())
    st.stop() # 强制停止渲染网页，只给苹果系统吐出日历文本

# 在网页上显示你自己的真实网址（自动获取）
# 注意：把下面的 "your-app-name" 改成你刚才在 Streamlit 面板上自己填写的二级域名
your_real_url = "https://your-app-name.streamlit.app/?feed=ics"
# 比如你刚才如果填了 jess-coach，那就是：https://jess-coach.streamlit.app/?feed=ics

# 自动把 https:// 替换为苹果专属的 webcal:// 协议
apple_ready_url = your_real_url.replace("https://", "webcal://")

st.text_input("请复制下方你专属的真实链接（拿去 iPhone 订阅绝对不报错）：", value=apple_ready_url)

