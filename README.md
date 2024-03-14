# Backend_case

### 1. 查看所有餐厅列表

```
curl -H "Authorization: 2dd09e4342550f67986b5d789002a13c" http://127.0.0.1:5000/restaurants

```

这个命令会发送一个 GET 请求到 `/restaurants` 端点，服务器应该返回所有餐厅的列表。

### 2. 添加一家新餐厅

```
curl -X POST -H "Content-Type: application/json" -H "Authorization: 2dd09e4342550f67986b5d789002a13c" -d "{ \"name\": \"Pizza Palace\", \"location\": \"New York\", \"contact\": {\"phone\": \"456-789-0123\", \"email\": \"info@pizzapalace.com\"}, \"cuisine\": \"Italian\", \"rating\": 4.8}" http://127.0.0.1:5000/restaurants

```

这个命令通过 `-X POST` 发送一个 POST 请求，并通过 `-H "Content-Type: application/json"` 指定请求体为 JSON 格式。`-d` 参数后面跟着的是要添加的新餐厅的详细信息。

### 3. 查看特定餐厅的详细信息

将 `<id>` 替换为你想查看的餐厅的实际 ID。

```
curl -H "Authorization: 2dd09e4342550f67986b5d789002a13c" http://127.0.0.1:5000/restaurants/1
```

这个命令发送一个 GET 请求到 `/restaurants/1` 端点，用于获取 ID 为 1 的餐厅的详细信息。

### 4. 更新现有餐厅的详细信息

同样，将 `<id>` 替换为你想更新的餐厅的实际 ID。

```
curl -X PUT -H "Content-Type: application/json" -H "Authorization: 2dd09e4342550f67986b5d789002a13c" -d "{ \"name\": \"Updated Pasta Place\", \"location\": \"Rome\", \"cuisine\": \"Italian\", \"rating\": 4.6, \"contact\": {\"phone\": \"123-456-7890\", \"email\": \"update@pastaplace.com\"}}" http://127.0.0.1:5000/restaurants/1
```

这个命令通过 `-X PUT` 发送一个 PUT 请求来更新指定餐厅的信息。

### 5. 从列表中删除一家餐厅

将 `<id>` 替换为你想删除的餐厅的实际 ID。

```
curl -X DELETE -H "Authorization: 2dd09e4342550f67986b5d789002a13c" http://127.0.0.1:5000/restaurants/1
```

这个命令通过 `-X DELETE` 发送一个 DELETE 请求来删除指定的餐厅。

以上是使用 `curl` 来测试你的 Flask REST API 的基本示例。你可以根据实际的 API 端点和功能调整这些命令。此外，为了更方便地测试和调试 API，你也可以考虑使用像 Postman 这样的图形界面工具，它提供了一个更友好的用户界面来管理请求和响应。

### 6.作为一名用户，我想根据地点或菜看来筛选餐厅。←

```
curl -X GET "http://127.0.0.1:5000/restaurants?page=1&per_page=5location=New%20York&cuisine=Italian" -H "Authorization: 2dd09e4342550f67986b5d789002a13c"

```

### 7.使用`curl`请求分页结果

下面是一个示例`curl`命令，请求第1页数据，假设每页显示5条记录：

```
curl -X GET "http://127.0.0.1:5000/restaurants?page=1&per_page=5" -H "Authorization: 2dd09e4342550f67986b5d789002a13c"
```

- `page=1`表示请求的是第一页。
- `per_page=5`表示每页希望展示5条记录。

'''
 
