# BuildingController

BuildingController

---

## 楼宇分页查询

> BASIC

**Path:** /building/queryPage

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
|name|string|楼宇名称|
|subDistrictCode|string|所属街道编码|
|subDistrictAdminName|string|街道管理人员|
|mainPurposeList|array|主要用途列表|
|\|─|integer||
|listingOrAwardIdList|array|挂牌或获奖情况ID列表|
|\|─|integer||
|buildingFeatureIdList|array|楼宇特色ID列表|
|\|─|integer||
|industrialPositioningIdList|array|产业定位ID列表|
|\|─|integer||
|floorCountRange|array|楼层数区间|
|\|─|integer||
|totalSpaceCountRange|array|总空间区间|
|\|─|integer||
|rentPriceRange|array|租金范围价格区间（元/m²/月）|
|\|─|number||
|createType|integer|创建方式（1用户创建 2后台创建）|
|releaseStatus|integer|发布状态（1未发布 2已发布）|

**Request Demo:**

{  
  "pageNum": "1",  
  "pageSize": "10",  
  "name": "",  
  "subDistrictCode": "",  
  "subDistrictAdminName": "",  
  "mainPurposeList": [  
    0  
  ],  
  "listingOrAwardIdList": [  
    0  
  ],  
  "buildingFeatureIdList": [  
    0  
  ],  
  "industrialPositioningIdList": [  
    0  
  ],  
  "floorCountRange": [  
    0  
  ],  
  "totalSpaceCountRange": [  
    0  
  ],  
  "rentPriceRange": [  
    0.0  
  ],  
  "createType": 0,  
  "releaseStatus": 0  
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

## 获取楼宇详情

> BASIC

**Path:** /building/getBuildingById

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
|\|─buildingId|integer|楼宇id|
|\|─name|string|楼宇名称|
|\|─floorCount|integer|楼层数|
|\|─developer|string|开发商|
|\|─logisticsCompany|string|物流公司|
|\|─address|string|地址|
|\|─subDistrictCode|string|所属街道编码|
|\|─subDistrictAdminId|integer|街道管理人员Id|
|\|─subDistrictAdminName|string|街道管理人员名称|
|\|─belongEntUnifiedSocialCreditCode|string|楼宇归属统一社会信用代码|
|\|─belongEntName|string|楼宇归属企业名称|
|\|─intro|string|楼宇简介|
|\|─styleImageList|array|楼宇风采id列表|
|\|─|object||
|\|─imageId|integer|图片id|
|\|─imageDesc|string|图片描述|
|\|─rentSaleWay|integer|租售方式|
|\|─rentPriceRange|array|租金范围价格区间（元/m²/月）|
|\|─|number||
|\|─manageFee|number|管理费（元/月）|
|\|─contactList|array|联系人列表|
|\|─|object||
|\|─contactName|string|联系人名称|
|\|─contactPhoneNumber|string|联系人手机|
|\|─contactQcCodeImageId|integer|联系人二维码id|
|\|─wechatOfficialImageId|integer|微信公众号id|
|\|─mainPurpose|integer|主要用途|
|\|─industrialIdList|array|产业定位|
|\|─|integer||
|\|─listingOrAwardIdList|array|挂牌或获奖情况|
|\|─|integer||
|\|─listingOrAwardOther|string|挂牌或获奖情况-其他|
|\|─buildingFeatureIdList|array|楼宇特色|
|\|─|integer||
|\|─buildingFeatureOther|string|楼宇特色-其他|
|\|─listedEntCount|integer|上市企业数量|
|\|─highTechEntCount|integer|高新企业数量|
|\|─starEntList|array|明星企业列表|
|\|─|object||
|\|─entName|string|企业名称|
|\|─entIndustrialIdList|array|企业产业定位|
|\|─|integer||
|\|─expDate|string|到期时间|
|\|─completionDateFormat|string|竣工时间|
|\|─totalFloorArea|number|总建筑面积（m²）|
|\|─totalOfficeArea|number|总办公面积（m²）|
|\|─totalCommercialArea|number|总商业面积（m²）|
|\|─storeyHeight|number|层高/净高（m)|
|\|─standardFloorArea|number|标准层面积（m²）|
|\|─elevatorCount|integer|电梯数量|
|\|─parkCount|integer|停车位数量|
|\|─parkFee|number|停车费（元/月）|
|\|─canteenFlag|integer|食堂标志（1有 0无）|
|\|─centAirFlag|integer|中央空调标志（1有 0无）|
|\|─releaseStatus|integer|发布状态（1未发布 2已发布）|
|\|─inAuditing|integer|审核中标志(1是 0否)|
|\|─tagSaveFlag|integer|Tag保存标志|
|msg|string||

**Response Demo:**

{  
  "code": 0,  
  "data": {  
    "idType": 0,  
    "id": 0,  
    "buildingId": 0,  
    "name": "",  
    "floorCount": 0,  
    "developer": "",  
    "logisticsCompany": "",  
    "address": "",  
    "subDistrictCode": "",  
    "subDistrictAdminId": 0,  
    "subDistrictAdminName": "",  
    "belongEntUnifiedSocialCreditCode": "",  
    "belongEntName": "",  
    "intro": "",  
    "styleImageList": [  
      {  
        "imageId": 0,  
        "imageDesc": ""  
      }  
    ],  
    "rentSaleWay": 0,  
    "rentPriceRange": [  
      0.0  
    ],  
    "manageFee": 0.0,  
    "contactList": [  
      {  
        "contactName": "",  
        "contactPhoneNumber": ""  
      }  
    ],  
    "contactQcCodeImageId": 0,  
    "wechatOfficialImageId": 0,  
    "mainPurpose": 0,  
    "industrialIdList": [  
      0  
    ],  
    "listingOrAwardIdList": [  
      0  
    ],  
    "listingOrAwardOther": "",  
    "buildingFeatureIdList": [  
      0  
    ],  
    "buildingFeatureOther": "",  
    "listedEntCount": 0,  
    "highTechEntCount": 0,  
    "starEntList": [  
      {  
        "entName": "",  
        "entIndustrialIdList": [  
          0  
        ],  
        "expDate": ""  
      }  
    ],  
    "completionDateFormat": "",  
    "totalFloorArea": 0.0,  
    "totalOfficeArea": 0.0,  
    "totalCommercialArea": 0.0,  
    "storeyHeight": 0.0,  
    "standardFloorArea": 0.0,  
    "elevatorCount": 0,  
    "parkCount": 0,  
    "parkFee": 0.0,  
    "canteenFlag": 0,  
    "centAirFlag": 0,  
    "releaseStatus": 0,  
    "inAuditing": 0,  
    "tagSaveFlag": 0  
  },  
  "msg": ""  
}

---

## 获取已修改的楼宇字段

> BASIC

**Path:** /building/updatedBuildingFields/{snapshotId}

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

## 获取楼宇列表--前端格式

> BASIC

**Path:** /building/getBuildingList

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

## 获取租售方式列表-前端格式

> BASIC

**Path:** /building/getRentSaleWayList

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

## 获取主要用途列表-前端格式

> BASIC

**Path:** /building/getMainPurposeList

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

## 获取多选信息列表

> BASIC

**Path:** /building/getMultipleList/{type}

**Method:** GET

> REQUEST

**Path Params:**

|name|value|desc|
|---|---|---|
|type||类型|

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
|\|─isOther|boolean|是否其他(1是 0否)|
|\|─children|array||
|\|─|object||
|\|─label|string|前端label|
|\|─value|object|前端value|
|\|─isOther|boolean|是否其他(1是 0否)|
|\|─children|array||
|\|─|object||
|msg|string||

**Response Demo:**

{  
  "code": 0,  
  "data": [  
    {  
      "label": "",  
      "value": {},  
      "isOther": false,  
      "children": [  
        {  
          "label": "",  
          "value": {},  
          "isOther": false,  
          "children": []  
        }  
      ]  
    }  
  ],  
  "msg": ""  
}

---

## 楼宇推荐

> BASIC

**Path:** /building/recommendBuilding

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|application/json|YES||

**Request Body:**

|name|type|desc|
|---|---|---|
|idType|integer|id类型|
|id|integer|id|
|isRecommend|boolean|是否推荐|

**Request Demo:**

{  
  "idType": 0,  
  "id": 0,  
  "isRecommend": false  
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

## 楼宇排序

> BASIC

**Path:** /building/sortBuilding

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|application/json|YES||

**Request Body:**

|name|type|desc|
|---|---|---|
|idType|integer|id类型|
|id|integer|id|
|sort|integer|排序|

**Request Demo:**

{  
  "idType": 0,  
  "id": 0,  
  "sort": 0  
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

## 添加楼宇基础信息至快照

> BASIC

**Path:** /building/saveBuildingBaseInfo

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
|name|string|楼宇名称|
|floorCount|integer|楼层数|
|developer|string|开发商|
|logisticsCompany|string|物流公司|
|address|string|地址|
|subDistrictCode|string|所属街道编码|
|subDistrictAdminId|integer|街道管理人员Id|
|belongEntUnifiedSocialCreditCode|string|楼宇归属统一社会信用代码|
|belongEntName|string|楼宇归属企业名称|
|intro|string|楼宇简介|
|styleImageList|array|楼宇风采id列表|
|\|─|object||
|\|─imageId|integer|图片id|
|\|─imageDesc|string|图片描述|

**Request Demo:**

{  
  "id": 0,  
  "name": "",  
  "floorCount": 0,  
  "developer": "",  
  "logisticsCompany": "",  
  "address": "",  
  "subDistrictCode": "",  
  "subDistrictAdminId": 0,  
  "belongEntUnifiedSocialCreditCode": "",  
  "belongEntName": "",  
  "intro": "",  
  "styleImageList": [  
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

## 添加楼宇招商信息至快照

> BASIC

**Path:** /building/saveBuildingInvestmentInfo

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
|rentSaleWay|integer|租售方式|
|rentPriceRange|array|租金范围价格区间（元/m²/月）|
|\|─|number||
|manageFee|number|管理费（元/月）|
|contactList|array|联系人列表|
|\|─|object||
|\|─contactName|string|联系人名称|
|\|─contactPhoneNumber|string|联系人手机|
|contactQcCodeImageId|integer|联系人二维码id|
|wechatOfficialImageId|integer|微信公众号id|

**Request Demo:**

{  
  "id": 0,  
  "rentSaleWay": 0,  
  "rentPriceRange": [  
    0.0  
  ],  
  "manageFee": 0.0,  
  "contactList": [  
    {  
      "contactName": "",  
      "contactPhoneNumber": ""  
    }  
  ],  
  "contactQcCodeImageId": 0,  
  "wechatOfficialImageId": 0  
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

## 添加楼宇竞争力速览至快照

> BASIC

**Path:** /building/saveBuildingCompEdge

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|application/json|YES||

**Request Body:**

| name                   | type    | desc       |
| ---------------------- | ------- | ---------- |
| id                     | integer | id         |
| mainPurpose            | integer | 主要用途       |
| industrialIdList       | array   | 产业定位       |
| \|─                    | integer |            |
| listingOrAwardIdList   | array   | 挂牌或获奖情况    |
| \|─                    | integer |            |
| listingOrAwardOther    | string  | 挂牌或获奖情况-其他 |
| buildingFeatureIdList  | array   | 楼宇特色       |
| \|─                    | integer |            |
| buildingFeatureOther   | string  | 楼宇特色-其他    |
| listedEntCount         | integer | 上市企业数量     |
| highTechEntCount       | integer | 高新企业数量     |
| starEntList            | array   | 明星企业       |
| \|─                    | object  |            |
| \|─entName             | string  | 企业名称       |
| \|─entIndustrialIdList | array   | 企业产业定位     |
| \|─                    | integer |            |
| \|─expDate             | string  | 到期时间       |

**Request Demo:**

{  
  "id": 0,  
  "mainPurpose": 0,  
  "industrialIdList": [  
    0  
  ],  
  "listingOrAwardIdList": [  
    0  
  ],  
  "listingOrAwardOther": "",  
  "buildingFeatureIdList": [  
    0  
  ],  
  "buildingFeatureOther": "",  
  "listedEntCount": 0,  
  "highTechEntCount": 0,  
  "starEntList": [  
    {  
      "entName": "",  
      "entIndustrialIdList": [  
        0  
      ],  
      "expDate": ""  
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

## 添加楼宇详细信息至快照

> BASIC

**Path:** /building/saveBuildingDetailedInfo

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
|completionDateFormat|string|竣工时间|
|totalFloorArea|number|总建筑面积（m²）|
|totalOfficeArea|number|总办公面积（m²）|
|totalCommercialArea|number|总商业面积（m²）|
|storeyHeight|number|层高/净高（m)|
|standardFloorArea|number|标准层面积（m²）|
|elevatorCount|integer|电梯数量|
|parkCount|integer|停车位数量|
|parkFee|number|停车费（元/月）|
|canteenFlag|integer|食堂标志（1有 0无）|
|centAirFlag|integer|中央空调标志（1有 0无）|

**Request Demo:**

{  
  "id": 0,  
  "completionDateFormat": "",  
  "totalFloorArea": 0.0,  
  "totalOfficeArea": 0.0,  
  "totalCommercialArea": 0.0,  
  "storeyHeight": 0.0,  
  "standardFloorArea": 0.0,  
  "elevatorCount": 0,  
  "parkCount": 0,  
  "parkFee": 0.0,  
  "canteenFlag": 0,  
  "centAirFlag": 0  
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

## 提交楼宇信息

> BASIC

**Path:** /building/submitBuilding

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

## 申请编辑已提交楼宇->楼宇转存快照

> BASIC

**Path:** /building/applyEditSubmittedBuilding/{buildingId}

**Method:** GET

> REQUEST

**Path Params:**

|name|value|desc|
|---|---|---|
|buildingId||楼宇id|

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

## 删除楼宇

> BASIC

**Path:** /building/deleteBuilding

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