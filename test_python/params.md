"""

所有的返回参数中 code == 0 就是成功 否则失败  

查询url: /api/getList?current_page=1&page_size=5
method: GET     
request params 
current_page 和 page_size 为int 且必须存在

response params
{
    "code": 0,
    "data": {
        "employees": [
            {
                "firstName": "Lewis",
                "lastName": "Burson",
                "salary": 40700,
                "userid": 1
            },
            {
                "firstName": "b",
                "lastName": "bb",
                "salary": 22,
                "userid": 3
            },
            {
                "firstName": "c",
                "lastName": "cc",
                "salary": 33,
                "userid": 4
            },
            {
                "firstName": "d",
                "lastName": "dd",
                "salary": 44,
                "userid": 5
            },
            {
                "firstName": "e",
                "lastName": "ee",
                "salary": 55,
                "userid": 6
            }
        ],
        "total": 8
    },
    "msg": "request_success"
}


add url: /api/add
method: POST
request params 
遗下参数必须全部存在
{
    "firstName": "9999",
    "lastName": "9991",
    "salary": "99"
}
response params 
{
    "code": 0, 
    "data": null,
    "msg": "request_success"
}


edit url: /api/edit
method: POST
{
    "userid": 2,  # 必须存在 
    "firstName": "9999", # 不存在为空字符串 "" 
    "lastName": "999", # 不存在为空字符串 "" 
    "salary": "99" # 不存在为空字符串 "" 
}
response params 
{
    "code": 0, 
    "data": null,
    "msg": "request_success"
}


del url: /api/del
method: POST
{
    "userid": 2,  # 必须存在 
}
response params 
{
    "code": 0, 
    "data": null,
    "msg": "request_success"
}

"""