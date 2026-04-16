import webbrowser
import time
import schedule # 需要 pip install schedule
from datetime import datetime

def job():
    keyword = "drinking hot water health benefits news"
    # 也可以增加中文搜索
    print(f"[{datetime.now()}] 🔔 提醒时间到！该喝热水了。")
    print("[*] 正在为你获取全球今日热水资讯...")
    
    urls = [
        f"https://www.google.com/search?q={keyword}&tbs=qdr:d", # 搜索过去24小时
        f"https://www.baidu.com/s?wd=多喝热水+新闻&gpc=stf",
        "https://news.google.com/search?q=hot%20water%20health"
    ]
    
    for url in urls:
        webbrowser.open(url)
    
    print("✅ 任务完成。记得水温保持在 40°C 左右哦！")

# 设置每天上午 10:30 执行
schedule.every().day.at("10:30").do(job)

if __name__ == "__main__":
    print("🚀 自动化提醒脚本已启动，保持后台运行中...")
    print("💡 提示：按 Ctrl+C 可以停止。")
    while True:
        schedule.run_pending()
        time.sleep(60) # 每分钟检查一次
