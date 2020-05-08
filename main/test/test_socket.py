from websocket import create_connection
# 通过socket路由访问
ws = create_connection("ws://localhost:5000/socket/hosts/info_query")
ws.send("{'host_id':'1'}")
result = ws.recv()
print(result)
ws.close()