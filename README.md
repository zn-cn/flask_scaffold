# project scaffold for python

## 项目组件

* 数据库：mysql, redis
* 框架：flask
* modules: flask, pymysql, logging, PyJWT, redis, config, uwsgi
* web服务器：uwsgi
* 反向代理服务器：nginx
* 测试: 使用postman对各个接口进行测试

## 项目说明

* 传输协议: https,具体可访问pytemplate.bingyan.net(由于0x13 congress导致华中大局域网,只有校园网能访问
* 传输形式: JSON
* 缓存: 使用redis,5分钟有效
* 功能: 简单的注册登录和查询功能,登录使用jwt,jwt七天有效,每次登录刷新jwt

## 接口APIs

## 用户注册
### POST /api/v1/users
#### Request
```
{
    "username": String, // 用户名
    "passowrd": String, // 密码
    "email": String, // 邮箱地址
}
``` 
#### Respones
```
{
    "successful": Boolean, // 请求成功或失败
    "data": {
        "token": String, //  web token
    }
}
```

## 用户登录
### POST /api/v1/login
#### Request
在header的Authorization字段中带入jwt
#### Response
```
{
    "successful": Boolean, // 请求成功或失败
    "data": {
        "token": String, //  web token 
    }    
}
```

## 邮箱查询
### GET /api/v1/emails/:username
#### Response
```
{
    "successful": Boolean, // 请求成功或失败
    "data": String // email address
}
```
