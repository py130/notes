# BuildingParkController

BuildingParkController

---

## 园区分页查询

> BASIC

**Path:** /building/park/queryPage

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|application/json|YES||

**Request Body:**

| name             | type    | desc     |
| ---------------- | ------- | -------- |
| pageNum          | integer | 当前页      |
| pageSize         | integer | 页大小 默认10 |
| name             | string  | 园区名称     |
| levelList        | array   | 园区等级列表   |
| \|─              | integer |          |
| industrialIdList | array   | 产业定位ID列表 |
| \|─              | integer |          |

**Request Demo:**

{  
  "pageNum": "1",  
  "pageSize": "10",  
  "name": "",  
  "levelList": [  
    0  
  ],  
  "industrialIdList": [  
    0  
  ]  
}

> RESPONSE

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|content-type|application/json;charset=UTF-8|NO||

**Body:**

|name|type|desc|
|---|---|---|
|code|integer||
|data|object||
|msg|string||

**Response Demo:**

{  
  "code": 0,  
  "data": {},  
  "msg": ""  
}

---

## 获取园区列表--前端格式

> BASIC

**Path:** /building/park/getParkList

**Method:** GET

> REQUEST

> RESPONSE

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|content-type|application/json;charset=UTF-8|NO||

**Body:**

|name|type|desc|
|---|---|---|
|code|integer||
|data|array||
|\|─|object||
|\|─label|string|前端label|
|\|─value|object|前端value|
|msg|string||

**Response Demo:**

{  
  "code": 0,  
  "data": [  
    {  
      "label": "",  
      "value": {}  
    }  
  ],  
  "msg": ""  
}

---

## 获取园区详情

> BASIC

**Path:** /building/park/getParkById/{parkId}

**Method:** GET

> REQUEST

**Path Params:**

|name|value|desc|
|---|---|---|
|parkId||园区id|

> RESPONSE

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|content-type|application/json;charset=UTF-8|NO||

**Body:**

| name                                | type    | desc         |
| ----------------------------------- | ------- | ------------ |
| code                                | integer |              |
| data                                | object  |              |
| \|─id                               | integer | id           |
| \|─name                             | string  | 园区名称         |
| \|─industrialIdList                 | array   | 产业定位         |
| \|─                                 | integer |              |
| \|─availLand                        | number  | 可用土地（亩）      |
| \|─level                            | integer | 园区等级         |
| \|─address                          | string  | 园区地址         |
| \|─belongEntUnifiedSocialCreditCode | string  | 园区归属统一社会信用代码 |
| \|─belongEntName                    | string  | 园区归属企业名称     |
| \|─intro                            | string  | 园区简介         |
| \|─contactList                      | array   | 联系人列表        |
| \|─                                 | object  |              |
| \|─contactName                      | string  | 联系人名称        |
| \|─contactPhoneNumber               | string  | 联系人手机        |
| \|─showImageList                    | array   | 环境展示列表       |
| \|─                                 | object  |              |
| \|─imageId                          | integer | 图片id         |
| \|─imageDesc                        | string  | 图片描述         |
| \|─buildingJoinList                 | array   | 关联楼宇         |
| \|─                                 | object  |              |
| \|─buildingId                       | integer | 楼宇id         |
| \|─buildingName                     | string  | 楼宇名称         |
| \|─subDistrictCode                  | string  | 所属街道编码       |
| \|─subDistrict                      | string  | 所属街道         |
| \|─buildingArea                     | number  | 楼宇面积m²       |
| \|─totalSpaceCount                  | integer | 总空间数         |
| \|─createTime                       | string  | 创建时间         |
| msg                                 | string  |              |

**Response Demo:**

{  
  "code": 0,  
  "data": {  
    "id": 0,  
    "name": "",  
    "industrialIdList": [  
      0  
    ],  
    "availLand": 0.0,  
    "level": 0,  
    "address": "",  
    "belongEntUnifiedSocialCreditCode": "",  
    "belongEntName": "",  
    "intro": "",  
    "contactList": [  
      {  
        "contactName": "",  
        "contactPhoneNumber": ""  
      }  
    ],  
    "showImageList": [  
      {  
        "imageId": 0,  
        "imageDesc": ""  
      }  
    ],  
    "buildingJoinList": [  
      {  
        "buildingId": 0,  
        "buildingName": "",  
        "subDistrictCode": "",  
        "subDistrict": "",  
        "buildingArea": 0.0,  
        "totalSpaceCount": 0,  
        "createTime": ""  
      }  
    ]  
  },  
  "msg": ""  
}

---

## 保存园区信息

> BASIC

**Path:** /building/park/savePark

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|application/json|YES||

**Request Body:**

| name                             | type    | desc         |
| -------------------------------- | ------- | ------------ |
| id                               | integer | id           |
| name                             | string  | 园区名称         |
| industrialIdList                 | array   | 产业定位         |
| \|─                              | integer |              |
| availLand                        | number  | 可用土地（亩）      |
| level                            | integer | 园区等级         |
| address                          | string  | 园区地址         |
| belongEntUnifiedSocialCreditCode | string  | 园区归属统一社会信用代码 |
| belongEntName                    | string  | 园区归属企业名称     |
| intro                            | string  | 园区简介         |
| contactList                      | array   | 联系人列表        |
| \|─                              | object  |              |
| \|─contactName                   | string  | 联系人名称        |
| \|─contactPhoneNumber            | string  | 联系人手机        |
| showImageList                    | array   | 环境展示id列表     |
| \|─                              | object  |              |
| \|─imageId                       | integer | 图片id         |
| \|─imageDesc                     | string  | 图片描述         |
| buildingIdList                   | array   | 关联楼宇         |
| \|─                              | integer |              |

**Request Demo:**

{  
  "id": 0,  
  "name": "",  
  "industrialIdList": [  
    0  
  ],  
  "availLand": 0.0,  
  "level": 0,  
  "address": "",  
  "belongEntUnifiedSocialCreditCode": "",  
  "belongEntName": "",  
  "intro": "",  
  "contactList": [  
    {  
      "contactName": "",  
      "contactPhoneNumber": ""  
    }  
  ],  
  "showImageList": [  
    {  
      "imageId": 0,  
      "imageDesc": ""  
    }  
  ],  
  "buildingIdList": [  
    0  
  ]  
}

> RESPONSE

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|content-type|application/json;charset=UTF-8|NO||

**Body:**

|name|type|desc|
|---|---|---|
|code|integer||
|data|integer||
|msg|string||

**Response Demo:**

{  
  "code": 0,  
  "data": 0,  
  "msg": ""  
}

---

## 设置园区授权用户

> BASIC

**Path:** /building/park/setParkAuthUser

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|application/json|YES||

**Request Body:**

| name       | type    | desc   |
| ---------- | ------- | ------ |
| parkId     | integer | 园区ID   |
| userIdList | array   | 用户ID列表 |
| \|─        | integer |        |

**Request Demo:**

{  
  "parkId": 0,  
  "userIdList": [  
    0  
  ]  
}

> RESPONSE

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|content-type|application/json;charset=UTF-8|NO||

**Body:**

|name|type|desc|
|---|---|---|
|code|integer||
|data|boolean||
|msg|string||

**Response Demo:**

{  
  "code": 0,  
  "data": false,  
  "msg": ""  
}

---

## 删除园区

> BASIC

**Path:** /building/park/deletePark/{parkId}

**Method:** GET

> REQUEST

**Path Params:**

|name|value|desc|
|---|---|---|
|parkId||园区id|

> RESPONSE

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|content-type|application/json;charset=UTF-8|NO||

**Body:**

|name|type|desc|
|---|---|---|
|code|integer||
|data|boolean||
|msg|string||

**Response Demo:**

{  
  "code": 0,  
  "data": false,  
  "msg": ""  
}