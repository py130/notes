# BuildingSpaceController

BuildingSpaceController

---

## 空间分页查询

> BASIC

**Path:** /building/space/queryPage

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|application/json|YES||

**Request Body:**

| name                 | type    | desc               |
| -------------------- | ------- | ------------------ |
| pageNum              | integer | 当前页                |
| pageSize             | integer | 页大小 默认10           |
| buildingId           | integer | 楼宇ID               |
| buildingName         | string  | 楼宇名称               |
| subDistrictCode      | string  | 所属街道编码             |
| subDistrictAdminName | string  | 街道管理人员             |
| floorRange           | array   | 楼层区间               |
| \|─                  | integer |                    |
| areaRange            | array   | 面积区间               |
| \|─                  | number  |                    |
| rentPriceRange       | array   | 租金价格区间             |
| \|─                  | number  |                    |
| orientList           | array   | 朝向列表               |
| \|─                  | integer |                    |
| decorList            | array   | 装修列表               |
| \|─                  | integer |                    |
| rentSaleWayList      | array   | 租售方式列表             |
| \|─                  | integer |                    |
| rentSaleStatusList   | array   | 租售状态列表             |
| \|─                  | integer |                    |
| spaceStatus          | integer | 空间状态（2公开 1隐藏 0未发布） |
| createType           | integer | 创建方式（1用户创建 2后台创建）  |

**Request Demo:**

{  
  "pageNum": "1",  
  "pageSize": "10",  
  "buildingId": 0,  
  "buildingName": "",  
  "subDistrictCode": "",  
  "subDistrictAdminName": "",  
  "floorRange": [  
    0  
  ],  
  "areaRange": [  
    0.0  
  ],  
  "rentPriceRange": [  
    0.0  
  ],  
  "orientList": [  
    0  
  ],  
  "decorList": [  
    0  
  ],  
  "rentSaleWayList": [  
    0  
  ],  
  "rentSaleStatusList": [  
    0  
  ],  
  "spaceStatus": 0,  
  "createType": 0  
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

## 统计闲置空间

> BASIC

**Path:** /building/space/statSpace

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|application/json|YES||

**Request Body:**

|name|type|desc|
|---|---|---|
|pageNum|integer|当前页|
|pageSize|integer|页大小 默认10|
|buildingId|integer|楼宇ID|
|buildingName|string|楼宇名称|
|subDistrictCode|string|所属街道编码|
|subDistrictAdminName|string|街道管理人员|
|floorRange|array|楼层区间|
|\|─|integer||
|areaRange|array|面积区间|
|\|─|number||
|rentPriceRange|array|租金价格区间|
|\|─|number||
|orientList|array|朝向列表|
|\|─|integer||
|decorList|array|装修列表|
|\|─|integer||
|rentSaleWayList|array|租售方式列表|
|\|─|integer||
|rentSaleStatusList|array|租售状态列表|
|\|─|integer||
|spaceStatus|integer|空间状态（2公开 1隐藏 0未发布）|
|createType|integer|创建方式（1用户创建 2后台创建）|

**Request Demo:**

{  
  "pageNum": "1",  
  "pageSize": "10",  
  "buildingId": 0,  
  "buildingName": "",  
  "subDistrictCode": "",  
  "subDistrictAdminName": "",  
  "floorRange": [  
    0  
  ],  
  "areaRange": [  
    0.0  
  ],  
  "rentPriceRange": [  
    0.0  
  ],  
  "orientList": [  
    0  
  ],  
  "decorList": [  
    0  
  ],  
  "rentSaleWayList": [  
    0  
  ],  
  "rentSaleStatusList": [  
    0  
  ],  
  "spaceStatus": 0,  
  "createType": 0  
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
|\|─totalCount|integer|总数|
|\|─totalFreeCount|integer|总闲置空间数|
|\|─totalFreeArea|number|总闲置面积m²|
|msg|string||

**Response Demo:**

{  
  "code": 0,  
  "data": {  
    "totalCount": 0,  
    "totalFreeCount": 0,  
    "totalFreeArea": 0.0  
  },  
  "msg": ""  
}

---

## 获取空间详情

> BASIC

**Path:** /building/space/getSpaceById

**Method:** GET

> REQUEST

**Query:**

|name|value|required|desc|
|---|---|---|---|
|idType||YES|id类型|
|id||YES|id|

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
|\|─idType|integer|id类型|
|\|─id|integer|id|
|\|─spaceId|integer|空间id|
|\|─buildingId|integer|楼宇id|
|\|─buildingName|string|楼宇名称|
|\|─floor|integer|楼层|
|\|─unitNo|string|单元号|
|\|─area|number|面积（m²）|
|\|─orient|integer|朝向|
|\|─decor|integer|装修|
|\|─rentPrice|number|租金价格（元/月）|
|\|─manageFee|number|管理费（元/月）|
|\|─rentSaleWay|integer|租售方式|
|\|─rentSaleStatusVo|object|租售状态|
|\|─rentSaleStatus|integer|租售状态|
|\|─rentSaleStatusStr|string|租售状态|
|\|─rentSaleEnt|string|租售企业|
|\|─entIndustrialIdList|array|企业产业定位|
|\|─|integer||
|\|─entIndustrialList|array|企业产业定位|
|\|─|string||
|\|─flowDirection|integer|流动方向|
|\|─flowDirectionStr|string|流动方向|
|\|─otherSubDistrictCode|string|本市其他区区划|
|\|─createDate|string|创建时间|
|\|─rentSaleStatusHistoryList|array|历史租售状态|
|\|─|object||
|\|─rentSaleStatus|integer|租售状态|
|\|─rentSaleStatusStr|string|租售状态|
|\|─rentSaleEnt|string|租售企业|
|\|─entIndustrialIdList|array|企业产业定位|
|\|─|integer||
|\|─entIndustrialList|array|企业产业定位|
|\|─|string||
|\|─flowDirection|integer|流动方向|
|\|─flowDirectionStr|string|流动方向|
|\|─otherSubDistrictCode|string|本市其他区区划|
|\|─createDate|string|创建时间|
|\|─showImageList|array|环境展示id列表|
|\|─|object||
|\|─imageId|integer|图片id|
|\|─imageDesc|string|图片描述|
|msg|string||

**Response Demo:**

{  
  "code": 0,  
  "data": {  
    "idType": 0,  
    "id": 0,  
    "spaceId": 0,  
    "buildingId": 0,  
    "buildingName": "",  
    "floor": 0,  
    "unitNo": "",  
    "area": 0.0,  
    "orient": 0,  
    "decor": 0,  
    "rentPrice": 0.0,  
    "manageFee": 0.0,  
    "rentSaleWay": 0,  
    "rentSaleStatusVo": {  
      "rentSaleStatus": 0,  
      "rentSaleStatusStr": "",  
      "rentSaleEnt": "",  
      "entIndustrialIdList": [  
        0  
      ],  
      "entIndustrialList": [  
        ""  
      ],  
      "flowDirection": 0,  
      "flowDirectionStr": "",  
      "otherSubDistrictCode": "",  
      "createDate": ""  
    },  
    "rentSaleStatusHistoryList": [  
      {  
        "rentSaleStatus": 0,  
        "rentSaleStatusStr": "",  
        "rentSaleEnt": "",  
        "entIndustrialIdList": [  
          0  
        ],  
        "entIndustrialList": [  
          ""  
        ],  
        "flowDirection": 0,  
        "flowDirectionStr": "",  
        "otherSubDistrictCode": "",  
        "createDate": ""  
      }  
    ],  
    "showImageList": [  
      {  
        "imageId": 0,  
        "imageDesc": ""  
      }  
    ]  
  },  
  "msg": ""  
}

---

## 获取已修改的空间字段

> BASIC

**Path:** /building/space/updatedSpaceFields/{snapshotId}

**Method:** GET

> REQUEST

**Path Params:**

|name|value|desc|
|---|---|---|
|snapshotId||快照id|

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
|\|─|string||
|msg|string||

**Response Demo:**

{  
  "code": 0,  
  "data": [  
    ""  
  ],  
  "msg": ""  
}

---

## 获取空间最后租售状态

> BASIC

**Path:** /building/space/getLastRentSaleStatus

**Method:** GET

> REQUEST

**Query:**

|name|value|required|desc|
|---|---|---|---|
|idType||YES|id类型|
|id||YES|id|

> RESPONSE

**Headers:**

| name         | value                          | required | desc |
| ------------ | ------------------------------ | -------- | ---- |
| content-type | application/json;charset=UTF-8 | NO       |      |

**Body:**

| name                    | type    | desc    |
| ----------------------- | ------- | ------- |
| code                    | integer |         |
| data                    | object  |         |
| \|─rentSaleStatus       | integer | 租售状态    |
| \|─rentSaleStatusStr    | string  | 租售状态    |
| \|─rentSaleEnt          | string  | 租售企业    |
| \|─entIndustrialIdList  | array   | 企业产业定位  |
| \|─                     | integer |         |
| \|─entIndustrialList    | array   | 企业产业定位  |
| \|─                     | string  |         |
| \|─flowDirection        | integer | 流动方向    |
| \|─flowDirectionStr     | string  | 流动方向    |
| \|─otherSubDistrictCode | string  | 本市其他区区划 |
| \|─createDate           | string  | 创建时间    |
| msg                     | string  |         |

**Response Demo:**

{  
  "code": 0,  
  "data": {  
    "rentSaleStatus": 0,  
    "rentSaleStatusStr": "",  
    "rentSaleEnt": "",  
    "entIndustrialIdList": [  
      0  
    ],  
    "entIndustrialList": [  
      ""  
    ],  
    "flowDirection": 0,  
    "flowDirectionStr": "",  
    "otherSubDistrictCode": "",  
    "createDate": ""  
  },  
  "msg": ""  
}

---

## 获取空间朝向列表-前端格式

> BASIC

**Path:** /building/space/getOrientList

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

## 获取空间装修列表-前端格式

> BASIC

**Path:** /building/space/getDecorList

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

## 获取空间状态列表-前端格式

> BASIC

**Path:** /building/space/getSpaceStatus

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

## 获取空间租售方式列表-前端格式

> BASIC

**Path:** /building/space/getRentSaleWayList

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

## 获取空间租售状态列表-前端格式

> BASIC

**Path:** /building/space/getRentSaleStatusList

**Method:** GET

> REQUEST

**Query:**

|name|value|required|desc|
|---|---|---|---|
|code||NO||

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

## 添加闲置空间至快照

> BASIC

**Path:** /building/space/saveSpace

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|application/json|YES||

**Request Body:**

|name|type|desc|
|---|---|---|
|id|integer|id|
|buildingId|integer|楼宇id|
|floor|integer|空间位置-楼层|
|unitNo|string|空间位置-单元号|
|area|number|面积（m²）|
|orient|integer|朝向|
|decor|integer|装修|
|rentPrice|number|租金价格（元/月）|
|manageFee|number|管理费（元/月）|
|rentSaleWay|integer|租售方式|
|rentSaleStatusDto|object|租售状态|
|\|─rentSaleStatus|integer|租售状态|
|\|─rentSaleEnt|string|租售企业|
|\|─entIndustrialIdList|array|企业产业定位|
|\|─|integer||
|\|─flowDirection|integer|流动方向|
|\|─otherSubDistrictCode|string|本市其他区区划|
|showImageList|array|环境展示id列表|
|\|─|object||
|\|─imageId|integer|图片id|
|\|─imageDesc|string|图片描述|

**Request Demo:**

{  
  "id": 0,  
  "buildingId": 0,  
  "floor": 0,  
  "unitNo": "",  
  "area": 0.0,  
  "orient": 0,  
  "decor": 0,  
  "rentPrice": 0.0,  
  "manageFee": 0.0,  
  "rentSaleWay": 0,  
  "rentSaleStatusDto": {  
    "rentSaleStatus": 0,  
    "rentSaleEnt": "",  
    "entIndustrialIdList": [  
      0  
    ],  
    "flowDirection": 0,  
    "otherSubDistrictCode": ""  
  },  
  "showImageList": [  
    {  
      "imageId": 0,  
      "imageDesc": ""  
    }  
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

## 提交空间信息

> BASIC

**Path:** /building/space/submitSpace

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|application/json|YES||

**Request Body:**

|name|type|desc|
|---|---|---|
|snapshotId|integer|快照id|
|isRelease|boolean|是否发布|

**Request Demo:**

{  
  "snapshotId": 0,  
  "isRelease": false  
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

## 申请修改已提交的空间->空间转存快照

> BASIC

**Path:** /building/space/applyEditSubmittedSpace/{spaceId}

**Method:** GET

> REQUEST

**Path Params:**

|name|value|desc|
|---|---|---|
|spaceId||空间id|

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

## 修改空间租售状态

> BASIC

**Path:** /building/space/editSpaceRentSaleStatus

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|application/json|YES||

**Request Body:**

| name                 | type    | desc    |
| -------------------- | ------- | ------- |
| rentSaleStatus       | integer | 租售状态    |
| rentSaleEnt          | string  | 租售企业    |
| entIndustrialIdList  | array   | 企业产业定位  |
| \|─                  | integer |         |
| flowDirection        | integer | 流动方向    |
| otherSubDistrictCode | string  | 本市其他区区划 |
| idType               | integer | id类型    |
| id                   | integer | id      |

**Request Demo:**

{  
  "rentSaleStatus": 0,  
  "rentSaleEnt": "",  
  "entIndustrialIdList": [  
    0  
  ],  
  "flowDirection": 0,  
  "otherSubDistrictCode": "",  
  "idType": 0,  
  "id": 0  
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

## 空间公开

> BASIC

**Path:** /building/space/publicSpace

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|application/json|YES||

**Request Body:**

|name|type|desc|
|---|---|---|
|spaceId|integer|空间id|
|isPublic|boolean|是否公开|

**Request Demo:**

{  
  "spaceId": 0,  
  "isPublic": false  
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

## 空间删除

> BASIC

**Path:** /building/space/deleteSpace

**Method:** GET

> REQUEST

**Query:**

|name|value|required|desc|
|---|---|---|---|
|idType||YES|id类型|
|id||YES|id|

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