# MedEase - hospital service system

### Website
- 主頁
    - [x] 個人資料
    - [x] 緊急聯絡人
    - [x] 錢包餘額/加值服務
- 預約
    - [x] 搜尋醫院
    - [x] 手動預約
        - [x] 手動選擇科別
        - [x] 人形
        - [ ] 接駁車/陪病員
- 就醫紀錄
    - [ ] 查看每筆就醫紀錄
    - [ ] 陪病員的筆記
- 交易紀錄
    - [x] 查看每筆交易紀錄
- 健康資訊
    - [x] 文章 
    - [x] 語音

### Other Function
- [ ] 掃描健保卡
- [ ] 回報家屬(模擬簡訊?)
- [ ] 模擬信用卡加值
- [ ] 標示出醫院地圖

### Database
- **user**
    - **uid:** INT -> primary key
    - **name:** VARCHAR(255)
    - **IDnumber:** VARCHAR(10)
    - **birthday:** VARCHAR(10)
    - **phonenumber:** VARCHAR(10)
    - **wallet:** INT

- **e_contact**
    - **eid:** INT -> primary key
    - **uid:** INT
    - **e_contact_name:** VARCHAR(255)
    - **e_contact_phone:** VARCHAR(10)
    - **relation:** VARCHAR(255)

- **transaction**
    - **rid:** INT -> primary key
    - **action:** VARCHAR(255)
    - **time:** VARCHAR(255)
    - **amount:** INT
    - **uid:** INT

- **hospitals**
    - **hid:** INT -> primary key
    - **hname:** VARCHAR(255)
    - **hlatitude:** float
    - **hlongitude:** float

- **department**
    - **did:** INT -> primary key
    - **hid:** INT
    - **d_name:** VARCHAR(255)

- **doctor**
    - **docid:** INT -> primary key
    - **did:** INT
    - **docName:** VARCHAR(255)

- **schedules**
    - **schid:** INT -> primary key
    - **docid:** INT
    - **time:** VARCHAR(255)

- **appointment**
    - **aid:** INT -> primary key
    - **schid:** INT
    - **uid:** INT
    - **number:** INT
    - **advice:** VARCHAR(255)
