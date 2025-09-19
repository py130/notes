# MobileTermController

MobileTermController

---

## 移动端登录

> BASIC

**Path:** /mobileTerm/mobileLogin

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|application/json|YES||

**Request Body:**

|name|type|desc|
|---|---|---|
|phoneNumber|string|手机号码|

**Request Demo:**

{  
  "phoneNumber": ""  
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
|\|─token|string|token|
|\|─type|string|用户类型 SYS_USER :后台登录 ZW_USER :政务登录 MOBILE_ENT_USER :手机企业用户登录 MOBILE_VISITOR_USER :手机游客用户登录|
|msg|string||

**Response Demo:**

{  
  "code": 0,  
  "data": {  
    "token": "",  
    "type": ""  
  },  
  "msg": ""  
}

---

## 上传文件

> BASIC

**Path:** /mobileTerm/file/upload

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|multipart/form-data|YES||

**Form:**

|name|value|required|type|desc|
|---|---|---|---|---|
|file||NO|file|文件|

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

## 读取文件

> BASIC

**Path:** /mobileTerm/file/readFile/{id}

**Method:** GET

> REQUEST

**Path Params:**

|name|value|desc|
|---|---|---|
|id||文件id|

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

## 楼宇分页查询

> BASIC

**Path:** /mobileTerm/building/queryBuildingPage

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|application/json|YES||

**Request Body:**

| name                    | type    | desc             |
| ----------------------- | ------- | ---------------- |
| pageNum                 | integer | 当前页              |
| pageSize                | integer | 页大小 默认10         |
| fuzzyQuery              | string  | 模糊查询             |
| subDistrictCode         | string  | 所属街道编码           |
| industrialPositioningId | integer | 产业定位id           |
| listingOrAwardId        | integer | 挂牌或获奖情况ID        |
| parkId                  | integer | 园区               |
| rentPriceRange          | array   | 租金范围价格区间（元/m²/月） |
| \|─                     | number  |                  |
| floorCountRange         | array   | 楼层数区间            |
| \|─                     | integer |                  |
| totalFloorAreaRange     | array   | 总建筑面积区间          |
| \|─                     | number  |                  |
| onlyFollow              | boolean | 只看关注             |

**Request Demo:**

{  
  "pageNum": "1",  
  "pageSize": "10",  
  "fuzzyQuery": "",  
  "subDistrictCode": "",  
  "industrialPositioningId": 0,  
  "listingOrAwardId": 0,  
  "parkId": 0,  
  "rentPriceRange": [  
    0.0  
  ],  
  "floorCountRange": [  
    0  
  ],  
  "totalFloorAreaRange": [  
    0.0  
  ],  
  "onlyFollow": false  
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

## 楼宇查询统计

> BASIC

**Path:** /mobileTerm/building/statBuildingSearchResult

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
|fuzzyQuery|string|模糊查询|
|subDistrictCode|string|所属街道编码|
|industrialPositioningId|integer|产业定位id|
|listingOrAwardId|integer|挂牌或获奖情况ID|
|parkId|integer|园区|
|rentPriceRange|array|租金范围价格区间（元/m²/月）|
|\|─|number||
|floorCountRange|array|楼层数区间|
|\|─|integer||
|totalFloorAreaRange|array|总建筑面积区间|
|\|─|number||
|onlyFollow|boolean|只看关注|

**Request Demo:**

{  
  "pageNum": "1",  
  "pageSize": "10",  
  "fuzzyQuery": "",  
  "subDistrictCode": "",  
  "industrialPositioningId": 0,  
  "listingOrAwardId": 0,  
  "parkId": 0,  
  "rentPriceRange": [  
    0.0  
  ],  
  "floorCountRange": [  
    0  
  ],  
  "totalFloorAreaRange": [  
    0.0  
  ],  
  "onlyFollow": false  
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
|\|─buildingCount|integer|楼宇数|
|\|─freeSpaceCount|integer|闲置空间数|
|msg|string||

**Response Demo:**

{  
  "code": 0,  
  "data": {  
    "buildingCount": 0,  
    "freeSpaceCount": 0  
  },  
  "msg": ""  
}

---

## 楼宇详情-展示页

> BASIC

**Path:** /mobileTerm/building/getBuildingDetail/{buildingId}

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
|data|object||
|\|─buildingId|integer|楼宇id|
|\|─buildingImageList|array|楼宇图片列表|
|\|─|object||
|\|─imageId|integer|图片id|
|\|─imageDesc|string|图片描述|
|\|─name|string|楼宇名称|
|\|─rentPriceRange|array|租金范围价格区间（元/m²/月）|
|\|─|number||
|\|─subDistrict|string|所属街道|
|\|─floorCount|integer|楼层数|
|\|─address|string|地址|
|\|─parkNameList|array|特色园区名称|
|\|─|string||
|\|─industrialList|array|产业定位列表|
|\|─|string||
|\|─listingOrAwardList|array|挂牌或获奖情况列表|
|\|─|string||
|\|─buildingFeatureList|array|楼宇特色列表|
|\|─|string||
|\|─listedEntCount|integer|上市企业数量|
|\|─highTechEntCount|integer|高新企业数量|
|\|─intro|string|楼宇简介|
|\|─logisticsCompany|string|物流公司|
|\|─parkCount|integer|停车位数量|
|\|─elevatorCount|integer|电梯数量|
|\|─centAirFlag|integer|中央空调标志（1有 0无）|
|\|─canteenFlag|integer|食堂标志（1有 0无）|
|\|─manageFee|number|管理费（元/月）|
|\|─parkFee|number|停车费（元/月）|
|\|─contactList|array|联系人列表|
|\|─|object||
|\|─contactName|string|联系人名称|
|\|─contactPhoneNumber|string|联系人手机|
|\|─contactQcCodeImageId|integer|联系人二维码id|
|\|─wechatOfficialImageId|integer|微信公众号id|
|\|─followFlag|integer|关注标识（1关注 0未关注）|
|msg|string||

**Response Demo:**

{  
  "code": 0,  
  "data": {  
    "buildingId": 0,  
    "buildingImageList": [  
      {  
        "imageId": 0,  
        "imageDesc": ""  
      }  
    ],  
    "name": "",  
    "rentPriceRange": [  
      0.0  
    ],  
    "subDistrict": "",  
    "floorCount": 0,  
    "address": "",  
    "parkNameList": [  
      ""  
    ],  
    "industrialList": [  
      ""  
    ],  
    "listingOrAwardList": [  
      ""  
    ],  
    "buildingFeatureList": [  
      ""  
    ],  
    "listedEntCount": 0,  
    "highTechEntCount": 0,  
    "intro": "",  
    "logisticsCompany": "",  
    "parkCount": 0,  
    "elevatorCount": 0,  
    "centAirFlag": 0,  
    "canteenFlag": 0,  
    "manageFee": 0.0,  
    "parkFee": 0.0,  
    "contactList": [  
      {  
        "contactName": "",  
        "contactPhoneNumber": ""  
      }  
    ],  
    "contactQcCodeImageId": 0,  
    "wechatOfficialImageId": 0,  
    "followFlag": 0  
  },  
  "msg": ""  
}

---

## 获取楼宇最终状态的id和id类型

> BASIC

**Path:** /mobileTerm/building/getFinalBuildingIdTypeAndId/{buildingId}

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
|data|object||
|\|─idType|integer|id类型|
|\|─id|integer|id|
|msg|string||

**Response Demo:**

{  
  "code": 0,  
  "data": {  
    "idType": 0,  
    "id": 0  
  },  
  "msg": ""  
}

---

## 空间分页查询

> BASIC

**Path:** /mobileTerm/space/querySpacePage

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
|buildingId|integer|楼宇id|
|rentSaleStatusList|array|租售状态列表|
|\|─|integer||
|areaRange|array|面积区间|
|\|─|number||
|excludeSpaceIdList|array|不包含的空间id|
|\|─|integer||
|onlyFollow|boolean|只看关注|

**Request Demo:**

{  
  "pageNum": "1",  
  "pageSize": "10",  
  "buildingId": 0,  
  "rentSaleStatusList": [  
    0  
  ],  
  "areaRange": [  
    0.0  
  ],  
  "excludeSpaceIdList": [  
    0  
  ],  
  "onlyFollow": false  
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

## 空间详情-展示页

> BASIC

**Path:** /mobileTerm/space/getSpaceDetail/{spaceId}

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
|data|object||
|\|─spaceId|integer|空间id|
|\|─spaceImageList|array|空间图片列表|
|\|─|object||
|\|─imageId|integer|图片id|
|\|─imageDesc|string|图片描述|
|\|─rentPrice|number|租金价格（元/月）|
|\|─area|number|面积（m²）|
|\|─floor|integer|楼层|
|\|─unitNo|string|单元号|
|\|─manageFee|number|管理费（元/月）|
|\|─rentSaleWayStr|string|租售方式|
|\|─orientStr|string|朝向|
|\|─decorStr|string|装修|
|\|─rentSaleStatusStr|string|租售状态|
|\|─buildingId|integer|楼宇id|
|\|─buildingName|string|楼宇名称|
|\|─address|string|地址|
|\|─floorCount|integer|楼层数|
|\|─parkNameList|array|特色园区名称列表|
|\|─|string||
|\|─industrialList|array|产业定位列表|
|\|─|string||
|\|─listingOrAwardList|array|挂牌或获奖情况列表|
|\|─|string||
|\|─buildingFeatureList|array|楼宇特色列表|
|\|─|string||
|\|─listedEntCount|integer|上市企业数量|
|\|─highTechEntCount|integer|高新企业数量|
|\|─contactList|array|联系人列表|
|\|─|object||
|\|─contactName|string|联系人名称|
|\|─contactPhoneNumber|string|联系人手机|
|\|─followFlag|integer|关注标识（1关注 0未关注）|
|msg|string||

**Response Demo:**

{  
  "code": 0,  
  "data": {  
    "spaceId": 0,  
    "spaceImageList": [  
      {  
        "imageId": 0,  
        "imageDesc": ""  
      }  
    ],  
    "rentPrice": 0.0,  
    "area": 0.0,  
    "floor": 0,  
    "unitNo": "",  
    "manageFee": 0.0,  
    "rentSaleWayStr": "",  
    "orientStr": "",  
    "decorStr": "",  
    "rentSaleStatusStr": "",  
    "buildingId": 0,  
    "buildingName": "",  
    "address": "",  
    "floorCount": 0,  
    "parkNameList": [  
      ""  
    ],  
    "industrialList": [  
      ""  
    ],  
    "listingOrAwardList": [  
      ""  
    ],  
    "buildingFeatureList": [  
      ""  
    ],  
    "listedEntCount": 0,  
    "highTechEntCount": 0,  
    "contactList": [  
      {  
        "contactName": "",  
        "contactPhoneNumber": ""  
      }  
    ],  
    "followFlag": 0  
  },  
  "msg": ""  
}

---

## 获取空间最终状态的id和id类型

> BASIC

**Path:** /mobileTerm/space/getFinalSpaceIdTypeAndId/{spaceId}

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
|data|object||
|\|─idType|integer|id类型|
|\|─id|integer|id|
|msg|string||

**Response Demo:**

{  
  "code": 0,  
  "data": {  
    "idType": 0,  
    "id": 0  
  },  
  "msg": ""  
}

---

## 园区分页查询

> BASIC

**Path:** /mobileTerm/park/queryParkPage

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

**Request Demo:**

{  
  "pageNum": "1",  
  "pageSize": "10"  
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

## 获取园区详情

> BASIC

**Path:** /mobileTerm/park/getParkDetail/{parkId}

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

| name                  | type    | desc        |
| --------------------- | ------- | ----------- |
| code                  | integer |             |
| data                  | object  |             |
| \|─id                 | integer | 园区id        |
| \|─parkImageList      | array   | 园区图片列表      |
| \|─                   | object  |             |
| \|─imageId            | integer | 图片id        |
| \|─imageDesc          | string  | 图片描述        |
| \|─name               | string  | 园区名称        |
| \|─address            | string  | 园区地址        |
| \|─level              | integer | 园区等级        |
| \|─levelStr           | string  | 园区等级        |
| \|─availLand          | number  | 可用土地（亩）     |
| \|─buildingJoinCount  | integer | 楼宇数量        |
| \|─freeSpaceCount     | integer | 可租售空间       |
| \|─totalFreeArea      | number  | 可租售空间面积（m²） |
| \|─industrialList     | array   | 产业定位列表      |
| \|─                   | string  |             |
| \|─intro              | string  | 园区简介        |
| \|─contactList        | array   | 联系人列表       |
| \|─                   | object  |             |
| \|─contactName        | string  | 联系人名称       |
| \|─contactPhoneNumber | string  | 联系人手机       |
| msg                   | string  |             |

**Response Demo:**

{  
  "code": 0,  
  "data": {  
    "id": 0,  
    "parkImageList": [  
      {  
        "imageId": 0,  
        "imageDesc": ""  
      }  
    ],  
    "name": "",  
    "address": "",  
    "level": 0,  
    "levelStr": "",  
    "availLand": 0.0,  
    "buildingJoinCount": 0,  
    "freeSpaceCount": 0,  
    "totalFreeArea": 0.0,  
    "industrialList": [  
      ""  
    ],  
    "intro": "",  
    "contactList": [  
      {  
        "contactName": "",  
        "contactPhoneNumber": ""  
      }  
    ]  
  },  
  "msg": ""  
}

---

## 设置用户关注

> BASIC

**Path:** /mobileTerm/my/setUserFollow

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|application/json|YES||

**Request Body:**

|name|type|desc|
|---|---|---|
|idType|integer|id类型（1楼宇 3空间）|
|relId|integer|关联id|
|isFollow|boolean|是否关注|

**Request Demo:**

{  
  "idType": 0,  
  "relId": 0,  
  "isFollow": false  
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

## 获取用户搜索楼宇记录

> BASIC

**Path:** /mobileTerm/my/getBuildingSearchRecordList

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

## 清空用户搜索楼宇记录

> BASIC

**Path:** /mobileTerm/my/clearBuildingSearchRecord

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
|data|boolean||
|msg|string||

**Response Demo:**

{  
  "code": 0,  
  "data": false,  
  "msg": ""  
}

---

## 我的楼宇-根据统一社会信用代码列表获取楼宇列表

> BASIC

**Path:** /mobileTerm/my/getBuildingList

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|application/json|YES||

**Request Body:**

|name|type|desc|
|---|---|---|
|entUnifiedSocialCreditCodeList|array|企业统一社会信用代码列表|
|\|─|string||

**Request Demo:**

{  
  "entUnifiedSocialCreditCodeList": [  
    ""  
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
|data|array||
|\|─|object||
|\|─buildingId|integer|楼宇id|
|\|─buildingName|string|楼宇名称|
|\|─address|string|地址|
|\|─inAuditing|integer|审核中标志（1是 0否）|
|msg|string||

**Response Demo:**

{  
  "code": 0,  
  "data": [  
    {  
      "buildingId": 0,  
      "buildingName": "",  
      "address": "",  
      "inAuditing": 0  
    }  
  ],  
  "msg": ""  
}

---

## 我的楼宇-根据楼宇id获取空间分页列表

> BASIC

**Path:** /mobileTerm/my/querySpacePageByBuildingId

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
|buildingId|integer|楼宇id|

**Request Demo:**

{  
  "pageNum": "1",  
  "pageSize": "10",  
  "buildingId": 0  
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

**Path:** /mobileTerm/building/getBuildingById

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
|\|─inAuditing|integer|审核中标志（1是 0否）|
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

## 添加楼宇基础信息至快照

> BASIC

**Path:** /mobileTerm/building/saveBuildingBaseInfo

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

**Path:** /mobileTerm/building/saveBuildingInvestmentInfo

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

**Path:** /mobileTerm/building/saveBuildingCompEdge

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
|mainPurpose|integer|主要用途|
|industrialIdList|array|产业定位|
|\|─|integer||
|listingOrAwardIdList|array|挂牌或获奖情况|
|\|─|integer||
|listingOrAwardOther|string|挂牌或获奖情况-其他|
|buildingFeatureIdList|array|楼宇特色|
|\|─|integer||
|buildingFeatureOther|string|楼宇特色-其他|
|listedEntCount|integer|上市企业数量|
|highTechEntCount|integer|高新企业数量|
|starEntList|array|明星企业|
|\|─|object||
|\|─entName|string|企业名称|
|\|─entIndustrialIdList|array|企业产业定位|
|\|─|integer||
|\|─expDate|string|到期时间|

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

**Path:** /mobileTerm/building/saveBuildingDetailedInfo

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

**Path:** /mobileTerm/building/submitBuilding

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

**Path:** /mobileTerm/building/applyEditSubmittedBuilding/{buildingId}

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

## 获取已修改的楼宇字段

> BASIC

**Path:** /mobileTerm/building/updatedBuildingFields/{snapshotId}

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

## 获取空间详情

> BASIC

**Path:** /mobileTerm/space/getSpaceById

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
|\|─id|integer|id|
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
|\|─otherSubDistrict|string|本市其他区区名|
|\|─createDate|string|创建时间|
|\|─rentSaleStatusHistoryList|array|历史租售状态|
|\|─|object||
|\|─id|integer|id|
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
|\|─otherSubDistrict|string|本市其他区区名|
|\|─createDate|string|创建时间|
|\|─showImageList|array|环境展示id列表|
|\|─|object||
|\|─imageId|integer|图片id|
|\|─imageDesc|string|图片描述|
|\|─inAuditing|integer|审核中标志（1是 0否）|
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
      "id": 0,  
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
      "otherSubDistrict": "",  
      "createDate": ""  
    },  
    "rentSaleStatusHistoryList": [  
      {  
        "id": 0,  
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
        "otherSubDistrict": "",  
        "createDate": ""  
      }  
    ],  
    "showImageList": [  
      {  
        "imageId": 0,  
        "imageDesc": ""  
      }  
    ],  
    "inAuditing": 0  
  },  
  "msg": ""  
}

---

## 添加闲置空间至快照

> BASIC

**Path:** /mobileTerm/space/saveSpace

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

**Path:** /mobileTerm/space/submitSpace

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

**Path:** /mobileTerm/space/applyEditSubmittedSpace/{spaceId}

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

## 空间删除

> BASIC

**Path:** /mobileTerm/space/deleteSpace

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

---

## 获取楼宇审核流程

> BASIC

**Path:** /mobileTerm/audit/getBuildingAuditProcess

**Method:** GET

> REQUEST

**Query:**

|name|value|required|desc|
|---|---|---|---|
|idType||YES|id类型|
|relId||YES|关联id|

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
|\|─process|string|流程名|
|\|─operator|string|操作人|
|\|─operationTime|string|操作时间|
|\|─otherContent|string|其他说明|
|msg|string||

**Response Demo:**

{  
  "code": 0,  
  "data": [  
    {  
      "process": "",  
      "operator": "",  
      "operationTime": "",  
      "otherContent": ""  
    }  
  ],  
  "msg": ""  
}

---

## 获取多选信息列表

> BASIC

**Path:** /mobileTerm/dict/getMultipleList/{type}

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
|\|─isOther|boolean|是否其他（1是 0否）|
|\|─children|array||
|\|─|object||
|\|─label|string|前端label|
|\|─value|object|前端value|
|\|─isOther|boolean|是否其他（1是 0否）|
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

## 获取空间朝向列表-前端格式

> BASIC

**Path:** /mobileTerm/dict/getOrientList

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

**Path:** /mobileTerm/dict/getDecorList

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

**Path:** /mobileTerm/dict/getSpaceStatus

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

**Path:** /mobileTerm/dict/getRentSaleWayList

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

## 获取广州市下区县列表-前端格式

> BASIC

**Path:** /mobileTerm/dict/getGZDistricts

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