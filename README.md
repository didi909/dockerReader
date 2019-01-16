# dockerReader
通过docker inspect信息生成docker run脚本，手残党的福音

作为系统管理员，有时候会临时性的创建一些容器，过后当需要找到该容器的启动脚本时，由于有复杂的volumn挂载和port的映射信息，需要一条一条的去读docker inspect信息，现在通过该工具简化这个步骤。

用法：
基于python3编写
python3 readInspect.py 容器名

输入示例：
python3 readInspect.py ltfox-setting

输出示例：
docker run -d --name=ltfox-setting --network==ltfoxdockercompose_default  -v /opt/ltfox-docker-compose-volumes/ltfox-setting:/app/ltfox-setting:rw ltfox-setting:latest  java -Dspring.profiles.active=dev -jar /app/ltfox-setting/ltfox-setting.jar

注意：
目前只支持输出容器名、网络、挂载、端口映射、镜像名、启动命令等内容，更多功能开发中，如果没有你需要的，可以提issue给我
