# InvestController

InvestController

---

## 分页查询投资列表

> BASIC

**Path:** /invest/page

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|application/json|YES||

**Request Body:**

| name                        | type    | desc         |
| --------------------------- | ------- | ------------ |
| pageNum                     | integer | 当前页          |
| pageSize                    | integer | 页大小 默认10     |
| projectName                 | string  | 投资（项目）名称     |
| investSubject               | integer | 投资主体         |
| projectContact              | string  | 项目联系人        |
| projectContactPhone         | string  | 项目联系方式       |
| entName                     | string  | 企业名称         |
| entUnifiedSocialCreditCode  | string  | 企业统一社会信用代码   |
| plannedInvestAmountRange    | array   | 计划投资金额区间（万元） |
| \|─                         | number  |              |
| estimatedRevenueAmountRange | array   | 预计营收规模区间（万元） |
| \|─                         | number  |              |
| submitTimeRange             | array   | 提交时间区间       |
| \|─                         | string  |              |
| submitterType               | integer | 用户类型         |
| submitter                   | string  | 提交人姓名        |
| handleTimeRange             | array   | 办理时间区间       |
| \|─                         | string  |              |
| handleStatus                | integer | 办理状态         |

**Request Demo:**

{  
  "pageNum": "1",  
  "pageSize": "10",  
  "projectName": "",  
  "investSubject": 0,  
  "projectContact": "",  
  "projectContactPhone": "",  
  "entName": "",  
  "entUnifiedSocialCreditCode": "",  
  "plannedInvestAmountRange": [  
    0.0  
  ],  
  "estimatedRevenueAmountRange": [  
    0.0  
  ],  
  "submitTimeRange": [  
    ""  
  ],  
  "submitterType": 0,  
  "submitter": "",  
  "handleTimeRange": [  
    ""  
  ],  
  "handleStatus": 0  
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

## 提交投资信息

> BASIC

**Path:** /mobileTerm/invest/submitInvest

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|application/json|YES||

**Request Body:**

| name                       | type    | desc       |
| -------------------------- | ------- | ---------- |
| investorBackground         | integer | 投资背景       |
| projectContact             | string  | 项目联系人      |
| projectContactPhone        | string  | 项目联系方式     |
| entName                    | string  | 企业名称       |
| entUnifiedSocialCreditCode | string  | 企业统一社会信用代码 |
| projectName                | string  | 投资（项目）名称   |
| investSubject              | integer | 投资主体       |
| plannedInvestAmount        | number  | 计划投资金额（万元） |
| estimatedRevenueAmount     | number  | 预计营收规模（万元） |
| projectContent             | string  | 项目内容       |
| investDemand               | string  | 投资需求       |
| submitter                  | string  | 提交人姓名      |
| submitterCertificateNumber | string  | 提交人证件号码    |
| submitterType              | integer | 用户类型       |

**Request Demo:**

{  
  "investorBackground": 0,  
  "projectContact": "",  
  "projectContactPhone": "",  
  "entName": "",  
  "entUnifiedSocialCreditCode": "",  
  "projectName": "",  
  "investSubject": 0,  
  "plannedInvestAmount": 0.0,  
  "estimatedRevenueAmount": 0.0,  
  "projectContent": "",  
  "investDemand": "",  
  "submitter": "",  
  "submitterCertificateNumber": "",  
  "submitterType": 0  
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

## 办理投资信息

> BASIC

**Path:** /invest/handle

**Method:** POST

> REQUEST

**Headers:**

|name|value|required|desc|
|---|---|---|---|
|Content-Type|application/json|YES||

**Request Body:**

| name          | type    | desc |
| ------------- | ------- | ---- |
| investId      | integer | 投资ID |
| handleStatus  | integer | 办理状态 |
| handleOpinion | string  | 办理意见 |

**Request Demo:**

{  
  "investId": 0,  
  "handleStatus": 0,  
  "handleOpinion": ""  
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