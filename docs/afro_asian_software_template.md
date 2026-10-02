# Software Project Documentation | توثيق مشروع البرمجيات

<div class="arabic">
قالب توثيق مشاريع البرمجيات — للمسابقة الأفريقية الآسيوية للتكنولوجيا
</div>

---

## 1. Project Overview | نظرة عامة على المشروع

| Field | Value |
|-------|-------|
| **Project Title** | EmlakHub |
| **Project Type** | Web App |
| **Description** | مشروع عقارات مصمم لتسهيل البحث عن العقارات وبيعها أو تأجيرها عبر واجهة ويب سهلة الاستخدام. يتيح للمستخدم تصفح العقارات الموجودة في المعرض عرض تفاصيل كل عقار إضافة عقار جديد بعد تسجيل الدخول وتحضير العقود والتحميل لها. كما يدعم إدارة بيانات المستخدمين وملفات العقود المرسلة من العميل. |
| **Target Users** | مستخدمين يبحثون عن عقارات للبيع أو الإيجار مالكون يريدون نشر عقاراتهم ومستخدمين يريدون عرض تفاصيل كاملة عن العقار من حيث السعر والعنوان والعدد والمساحة. |
| **Date** | 2026 |

### Tech Stack | Technology Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Language** | Python | تطوير المنطق الأساسي للتطبيق |
| **Framework** | Streamlit | بناء واجهة المستخدم وقواعد الصفحات |
| **Database** | SQLite | حفظ بيانات العقارات والمستخدمين والعقود |
| **Libraries** | Streamlit, sqlite3, Pillow, pathlib, uuid4 | عرض العقارات تخزين البيانات تحميل الصور إدارة الملفات |
| **File Storage** | Local uploads folder | حفظ الصور والعقود المرفوعة من المستخدم |

---

## 2. Problem Statement | بيان المشكلة

<div class="arabic">
المشكلة الرئيسية هي صعوبة الوصول إلى معلومات العقارات بشكل منظم وسريع خاصة عندما يحتاج العميل إلى البحث عن عقار مناسب قراءة التفاصيل ثم متابعة الإجراءات مثل التعاقد أو الإقرار. كما أن المالك يحتاج إلى منصة تمكنه من عرض عقاره بسهولة وبدون تعقيد.
</div>

### What problem does this project solve? | ما المشكلة التي يحلها هذا المشروع
This project solves the problem of fragmented property searching and manual property management. Users can browse available houses and apartments, see details quickly, and contact the seller or landlord through a centralized online platform.

### Why does it matter? | لماذا هذا مهم
It matters because property buying, selling, and renting often require a clear presentation of information, trust, and organized documentation. EmlakHub simplifies the process and reduces time spent in searching and managing property records.

### How is it currently solved? | كيف تحل المشكلة حاليا
The app currently provides a web-based property gallery, user registration and login, property upload form, property details page, and contract management workflow. This makes the process easier than dealing with traditional scattered methods.

---

## 3. Technical Architecture | البنية التقنية

<div class="arabic">
المشروع مبني باستخدام Streamlit وهو إطار عمل Python لإنشاء تطبيق ويب سريع وبسيط. يتم تخزين البيانات في قاعدة SQLite محلية بينما يتم حفظ الصور والعقود داخل مجلدات المشروع لتسهيل الإدارة.
</div>

### Project Structure | هيكل المشروع

```text
my-new-project-emlakhub/
├── app.py                          # نقطة الدخول الرئيسية للتطبيق
├── database/
│   ├── datebase.db                # قاعدة البيانات الرئيسية
│   └── datebase.sql               # ملف تعريف جداول قاعدة البيانات
├── assets/
│   └── documents/
│       ├── ownership_contract.pdf
│       └── tenant_contract.pdf
├── data/
│   └── uploads/                   # الصور والعقود المرفوعة من المستخدم
├── pages/
│   ├── add-property.py            # صفحة إضافة عقار جديد
│   ├── contract.py                # صفحة العقود والموافقة
│   ├── delete-property.py         # حذف العقار
│   ├── gallery.py                 # معرض العقارات الرئيسي
│   ├── login.py                   # تسجيل الدخول
│   ├── property_details.py        # تفاصيل العقار
│   ├── restiger.py               # تسجيل مستخدم جديد
│   ├── view-contracts.py         # عرض العقود المسجلة
│   └── view_users.py             # عرض المستخدمين
├── docs/
│   └── afro_asian_software_template.md
├── images/
│   └── ...
└── ...
```

### Key Files | الملفات الرئيسية

| File | Purpose |
|------|---------|
| app.py | نقطة الدخول في التطبيق |
| pages/gallery.py | عرض جميع العقارات في معرض مرئي |
| pages/login.py | تسجيل الدخول إلى الحساب |
| pages/restiger.py | تسجيل مستخدم جديد |
| pages/add-property.py | إدخال بيانات عقار جديد وصورة العقار |
| pages/property_details.py | رؤية تفاصيل العقار وحذفه |
| pages/contract.py | ملء بيانات العقد وتحميله وإرساله |
| database/datebase.sql | تعريف الجداول الأساسية |

---

## 4. Features & User Flow | الميزات وتدفق المستخدم

<div class="arabic">
المشروع يقدم تجربة مستخدم مبسطة: يبدأ المستخدم بالمعرض ثم يمكنه الدخول عرض تفاصيل العقار أو إضافة عقار جديد. بعد ذلك يمكنه إنجاز العقد ورفع نسخة الموقعة.
</div>

### Feature List | قائمة الميزات

| # | Feature | Description | Status |
|---|---------|-------------|:------:|
| 1 | Property gallery | عرض العقارات في شكل بطاقات مع السعر والعنوان وعدد الغرف والمساحة | ✅ |
| 2 | Search function | البحث عن العقار حسب الاسم أو العنوان | ✅ |
| 3 | User login | تسجيل الدخول إلى الحسابات الموجودة | ✅ |
| 4 | User registration | إنشاء حساب جديد للمستخدم | ✅ |
| 5 | Add property | إضافة عقار جديد مع صورة ووصف أساسي | ✅ |
| 6 | Property details | عرض تفاصيل العقار بالكامل | ✅ |
| 7 | Contract generation | عرض العقد ومتطلبات التعاقد | ✅ |
| 8 | Contract upload | رفع العقد الموقع بصيغة PDF | ✅ |
| 9 | View contracts | عرض العقود المسجلة داخل النظام | ✅ |

> Status: ✅ Complete | ⏳ In Progress | ❌ Not Started

### User Flow | تدفق المستخدم

```text
                    ┌────────────────────┐
                    │   Home / Gallery   │
                    └─────────┬──────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
      ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
      │ Login        │ │ Register     │ │ Add Property │
      └──────┬───────┘ └──────┬───────┘ └──────┬───────┘
             │                 │                 │
             └────────────┬────┴────────────┬────┘
                          ▼                 ▼
                 ┌──────────────────┐
                 │ Property Details │
                 └────────┬─────────┘
                          │
                          ▼
                  ┌──────────────┐
                  │ Contract     │
                  │ Page         │
                  └──────┬───────┘
                         │
                         ▼
                  ┌──────────────┐
                  │ Save / Upload│
                  │ Contract     │
                  └──────────────┘
```

### Screen Reference | دليل الشاشات

| Screen | File / Route | Description | Transitions To |
|--------|-------------|-------------|----------------|
| Home Gallery | pages/gallery.py | Display of all properties with images and prices | Login, Register, Details |
| Login | pages/login.py | Login for existing users | Gallery |
| Register | pages/restiger.py | New user registration | Login |
| Add Property | pages/add-property.py | Upload image and save a new listing | Gallery |
| Property Details | pages/property_details.py | Shows property info, image, delete option | Contract, Gallery |
| Contract | pages/contract.py | Select contract type, download PDF, upload signed file | Gallery |
| View Contracts | pages/view-contracts.py | List all contract records | Details |

---

## 5. UI/UX Design | تصميم واجهة المستخدم

<div class="arabic">
الواجهة تعتمد على تصميم بسيط وواضح مع بطاقات للعقارات أزرار واضحة وعرض متسلسل للبيانات المهمة مثل السعر العنوان عدد الغرف والمساحة.
</div>

### Screenshots | لقطات الشاشة

<!-- Screenshot: Landing page -->
**Landing Page**: صفحة معرض العقارات تعرض بطاقات بالعقارات المتاحة مع صورة اسم العقار السعر العنوان وغرف العقار.

<!-- Screenshot: Main dashboard -->
**Dashboard**: صفحة تفاصيل العقار تعرض بيانات العقار بشكل منظم مع صورة كبيرة ووصف مختصر وسهولة الوصول إلى زر العقود.

<!-- Screenshot: Key feature screen -->
**Key Feature**: صفحة إضافة العقار تسمح بإدخال اسم العقار المساحة نوع العقار العنوان السعر عدد الغرف ثم رفع صورة العقار.

### Design System | نظام التصميم

| Element | Style |
|---------|-------|
| **Primary Color** | #0F172A (dark slate blue) |
| **Secondary Color** | #16A34A (green) |
| **Font** | Segoe UI, Arial, Cairo |
| **Button Style** | Rounded buttons with strong contrast |
| **Layout** | Card-based layout using Streamlit panels |

### Responsive Design | التصميم المتجاوب

| Breakpoint | Layout | Tested? |
|------------|--------|:-------:|
| Desktop (1024px+) | Multi-column cards and wide property details | ✅ |
| Tablet (768-1024px) | Adjusted cards with stacked sections | ☐ |
| Mobile (< 768px) | Single-column layout and full-width buttons | ☐ |

---

## 6. Data Sources | مصادر البيانات

<div class="arabic">
المشروع يعتمد على قاعدة بيانات SQLite داخل المشروع بالإضافة إلى إدخالات المستخدم من النماذج وتحميل الصور من جهاز المستخدم.
</div>

### Data Sources | مصادر البيانات

| Source | Type | Description |
|--------|------|-------------|
| database/datebase.db | SQLite Database | Stores property listings, users, and contract details |
| User Input | Form Submission | Values entered for login, registration, and property creation |
| Uploaded Files | Local Storage | Property images and signed PDF contracts |
| Streamlit Session State | In-memory state | Selected property and current navigation state |

### Database Schema | مخطط قاعدة البيانات

| Table | Columns | Description |
|-------|---------|-------------|
| property | id, name, area, type, address, price, number_of_rooms, img_url, created_at | Stores the property listing information |
| users | id, name, email, password, dob, phone, ssn, created_at | Stores registered users |
| contracts / tenant_contract | id, name, phone, email, card_number, contract_type, property_id, property_type, property_price, property_address, created_at | Saves the generated contract information |

### External APIs (if any) | واجهات برمجة التطبيقات

| API | Purpose | Rate Limit |
|-----|---------|------------|
| None | All data is stored locally in the app | N/A |

---

## 7. Educational Content | المحتوى التعليمي

<div class="arabic">
هذا المشروع يعلم الطالب كيفية بناء تطبيق ويب عملي باستخدام Python ويفهم كيفية تنظيم البيانات إنشاء واجهات مستخدم وربط الصفحات مع قاعدة البيانات.
</div>

### Learning Objectives | أهداف التعلم

By the end of this project, the student will be able to:

1. Build a full web application using Python and Streamlit.
2. Design and work with a SQLite database for storing real-world data.
3. Create interactive forms for login, registration, and property listing.
4. Manage uploaded files such as property images and PDF contracts.
5. Build a complete user flow from browsing to property details and contract management.

### Cultural / Historical Context | السياق الثقافي / التاريخي

| Topic | Description |
|-------|-------------|
| Real estate access | The project connects to the real-life need for easier property discovery and digital contract handling |
| Digital transformation | It teaches how local services can be improved through simple online systems |

### Curriculum Alignment | التوافق مع المنهج

| Skill Area | What the Student Practices |
|------------|---------------------------|
| Problem Solving | Identifying a real property-management problem and building a digital solution |
| Computational Thinking | Data modeling, database logic, and workflow design |
| Creativity | Interface design, layout design, and user-friendly visual structure |
| Collaboration | Working on separate app sections like login, gallery, and contracts |
| Technical Writing | Documenting app structure, features, and data flow |

---

## 8. Marketing Plan | خطة تسويقية

> **Short version** — for full marketing plans, use the main Afro-Asian template.

<div class="arabic">
نسخة مختصرة — الخطة التسويقية تركز على عرض التطبيق كحل عملي للحسابات العقارية والبحث عن العقارات بطريقة أسرع وأكثر تنظيما.
</div>

### Target Audience | الجمهور المستهدف

- **Primary**: Buyers, renters, and property seekers looking for housing options online
- **Secondary**: Property owners and landlords who want to list their properties
- **Tertiary**: Real-estate agents and students exploring digital property management tools

### Platforms | المنصات

- Web browser on desktop
- Web browser on mobile devices
- Local demo environment for presentation and testing

### Promotion Ideas | أفكار ترويجية

1. Present the app in a school or competition exhibition.
2. Share screenshots of the property gallery and contract form on social media.
3. Demonstrate the app live to potential users and property owners.
4. Use the project as a practical example of digital transformation in real estate.

---

## 9. Student Worksheet | ورقة عمل الطالب

> **Instructions**: Copy this section into your own document and fill it in for YOUR project.

---

### My Project Information | معلومات مشروعي

**Student Name**: omar hossam hamissa

**Project Title**: EmlakHub

**Date**: 2026

---

#### What is your project about? | عن ماذا يتحدث مشروعي

مشروعي هو موقع إلكتروني للعقارات يساعد المستخدمين على البحث عن العقارات عرض تفاصيلها وإدارة بيانات العقود.

#### What problem does it solve? | ما المشكلة التي يحلها

يساعد المشروع في تنظيم عملية البحث عن العقار وتسهيل نشر العقارات وإدارة العمليات المتعلقة بالعقود بطريقة أسرع وأكثر وضوحا.

---

### My Tech Stack | التقنيات المستخدمة

**My project type** (circle one): Web App / Desktop App / Mobile App / Python Script / Other: Web App

**Technologies I used**:

| Category | Technology |
|----------|-----------|
| Language | Python |
| Framework | Streamlit |
| Database | SQLite |
| Libraries | streamlit, sqlite3, Pillow, pathlib, uuid4 |

---

### My Screens | شاشات مشروعي

| Screen Name | What the user sees/does | How to get here |
|-------------|------------------------|-----------------|
| Gallery | Shows all available properties with prices and addresses | Main app page |
| Login | Signs in to an existing user account | From gallery |
| Register | Creates a new account | From gallery or login |
| Add Property | Adds a new real-estate listing with image upload | From gallery |
| Property Details | Views the full property description and options | By selecting a card |
| Contract | Downloads and uploads the property contract | From property details |

---

### My Features | ميزات مشروعي

| Feature | What it does | Status |
|---------|-------------|:------:|
| Property gallery | Displays property cards with price and location | ✅ |
| Search | Finds a property by name or address | ✅ |
| Login | Authenticates the user | ✅ |
| Registration | Creates a new user account | ✅ |
| Add property | Saves a new listing | ✅ |

---

### My Data | بيانات مشروعي

**Where does data come from?**

البيانات تأتي من نموذج المستخدم قاعدة البيانات المحلية وملفات الصور أو العقود المرفوعة داخل المشروع.

**What data is stored?**

يتم حفظ بيانات العقارات بيانات المستخدمين تفاصيل العقود وصور العقارات المرفوعة.

---

### What I Learned | ما تعلمته

1. The hardest part of building my project was: connecting the pages together and making the property flow work consistently.

2. The most fun part of building my project was: designing the property gallery and adding the property details experience.

3. If I had more time, I would add: email and WhatsApp notifications, better user sessions, and a stronger admin dashboard.

4. One thing I would do differently: I would organize the project into a cleaner modular structure with shared functions and better validation.

---

### Screenshot of My Project | لقطة شاشة من مشروعي

<!-- Paste a screenshot of your project running here -->

---

**Instructor Notes** | ملاحظات المدرس:

This project demonstrates an end-to-end real estate web app built with Python and Streamlit. It combines simple UI design, database storage, and file management in a practical and accessible solution.

---

<div class="session-footer">
  <p>Techno Kids, Techno Future — Software Documentation Template</p>
  <p>Afro-Asian Tech Forum · Software Category · 2026</p>
</div>
