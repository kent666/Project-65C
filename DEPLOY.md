# 构建适配国产 CPU 的轻量化镜像
docker build -t hot-water-server:latest .

# 启动容器并设置为开机自启
docker run -d \
  --name hot-water-commander \
  --restart always \
  -e PUSHDEER_KEY="你的KEY" \
  hot-water-server:latest
