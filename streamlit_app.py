import streamlit as st
import datetime

# 1. 接收来自 iPad 快捷指令传过来的“用户大白话”和“今日体重”
# 如果快捷指令没有传，就使用默认值
query_params = st.query_params
user_status = query_params.get("status", "今天早上黑咖啡，周六我朋友叫我去打网球2小时。")
current_weight = float(query_params.get("weight", 74.3))

# 2. 核心 AI 动态判定逻辑（处理突发事件和状态）
target_weight = 60.0
fat_to_lose = round(current_weight - target_weight, 1)

# 动态改变周二课表（应对水肿突发事件）
if "重" in user_status or "肿" in user_status or current_weight > 74.5:
    tomorrow_plan = "🔋 AI干预: 大坡度跑步机爬坡 (坡度12%, 5.1km/h) + 按摩仪排水"
    ai_desc = "AI根据你昨晚无氧后的延迟性水肿，自动为你重写的排水日程。🐕下班别忘了遛狗打卡！"
else:
    tomorrow_plan = "🔋 默认有氧: 慢跑 45 分钟"
    ai_desc = "状态良好，继续保持！"

# 动态改变周六课表（应对朋友约球突发事件）
if "网球" in user_status:
    sat_plan = "🌟 专属计划: 🎾 朋友约打网球 2小时 + 小腿气囊按摩"
elif "攀岩" in user_status:
    sat_plan = "🌟 专属计划: 🧗‍♀️ 室内岩馆攀岩 2.5小时"
else:
    sat_plan = "💪 默认计划: 周末大消耗超级猩猩大课"

# 3. 把这些动态算好的结果，打包成苹果标准日历文本
real_ics_text = f"""BEGIN:VCALENDAR
VERSION:2.0
X-WR-CALNAME:🏋️‍♀️ Jess的AI私人教练
BEGIN:VEVENT
DTSTART;VALUE=DATE:20260526
DTEND;VALUE=DATE:20260527
SUMMARY:{tomorrow_plan}
DESCRIPTION:{ai_desc}
END:VEVENT
BEGIN:VEVENT
DTSTART;VALUE=DATE:20260530
DTEND;VALUE=DATE:20260531
SUMMARY:{sat_plan}
DESCRIPTION:根据你的突发事件动态更新的球局。
END:VEVENT
END:VCALENDAR"""

# 【核心黑科技】如果快捷指令来抓数据，网页什么都不显示，只吐出这串绝对纯净的 ICS 文本
st.text(real_ics_text)
