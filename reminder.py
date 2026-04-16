import schedule
import time
import requests
from datetime import datetime

# --- 配置区 ---
PUSHDEER_KEY = "你的PUSHDEER_KEY"  # 在 PushDeer App 免费获取
HOT_WATER_API = "https://api2.pushdeer.com/message/push"

def fetch_hot_water_intel():
    """模拟抓取今日热水全球情报"""
    # 实际应用中，这里可以接入更复杂的爬虫逻辑
    today = datetime.now().strftime('%Y-%m-%d')
    intel = [
        "· [科学] 研究显示 40°C 温水对食道粘膜最为友好。",
        "· [趋势] 社交媒体上关于 'Hot Water Therapy' 的讨论热度上升 15%。",
        "· [警示] 提醒：饮水超过 65°C 会增加 2A 类致癌风险，请务必晾凉！"
    ]
    return f"📅 **日期：{today}**\n\n" + "\n".join(intel)

def send_push():
    content = fetch_hot_water_intel()
    title = "🍵 您的今日“多喝热水”情报已送达"
    
    payload = {
        "pushkey": PUSHDEER_KEY,
        "text": title,
        "desp": content,
        "type": "markdown"
    }
    
    try:
        response = requests.get(HOT_WATER_API, params=payload)
        if response.status_code == 200:
            print(f"[{datetime.now()}] 推送成功！记得喝水。")
        else:
            print(f"[{datetime.now()}] 推送失败，状态码：{response.status_code}")
    except Exception as e:
        print(f"❌ 网络异常: {e}")

# --- 调度区 ---
# 每天早上 9:30 给自己一个硬核的关心
schedule.every().day.at("09:30").do(send_push)

if __name__ == "__main__":
    print("🛰️ 多喝热水·全球指挥中心（本地部署版）已启动...")
    print(f"📍 目标设备：龙芯/Hermes Server | 推送通道：PushDeer")
    # 启动时先推个测试，确认通路正常
    # send_push() 
    while True:
        schedule.run_pending()
        time.sleep(60)
