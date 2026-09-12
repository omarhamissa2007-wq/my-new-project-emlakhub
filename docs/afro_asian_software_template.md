
# Software Project Documentation | توثيق مشروع البرمجيات

<div class="arabic">
قالب توثيق مشاريع البرمجيات — للمسابقة الأفريقية الآسيوية للتكنولوجيا
</div>

---

## 1. Project Overview | نظرة عامة على المشروع

| Field | Value |
|-------|-------|
| **Project Title** | [emlakhub] |
| **Project Type** | [Web App] |
| **Description** | [مشروع عقارات يتضمن شقق وفلل للايجار او البيع
ليسهل للعميل ان يقدر ينشر العقار بتاعه علي الموقع بتاعنا 
عرض تفاصيل كل عقار
تمكين المستخدمين من نشر عقاراتهم بعد تسجيل الدخول
إرسال تأكيدات عبر البريد الإلكتروني وواتساب
إدارة العقارات والعقود بشكل آمن
معرض عقارات
صفحة تفاصيل عقار
صفحة نشر عقار جديد
تسجيل دخول / إنشاء حساب
تحميل عقود وتنزيلها
إشعارات للرفع والتعاقد
] |
| **Target Users** |مستخدمين يبحثون عن عقارات للبيع أو الإيجار
شخاص يريدون تصفح عقارات مع تفاصيل كاملة (سعر، عنوان، غرف، مساحة)
بائعين أو مؤجرين يريدون نشر عقارهم على المنصة
عملاء يحتاجون تأكيدات أو إشعارات عبر البريد الإلكتروني وواتساب
 مستخدمين مهتمين بإدارة العقود وتنزيلها إلكترونياً
 |
| **Date** | [2025] |

### Tech Stack | Technology Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Language** | [Python] | [لغه اساسيه] |
| **Framework** | [Streamlit] | [ بيُستخدم لبناء واجهات ويب] |
| **Database** | [sqlite] | [datebase.db] |
| **Libraries** | [streamlit
smtplib
email.mime.text.MIMEText
email.mime.multipart.MIMEMultipart
pywhatkit
PIL (Pillow)
os
datetime
sqlite3] | [streamlit: يبني واجهة الموقع ويدير الصفحات والتفاعل مع المستخدم.
smtplib: يرسل بريد إلكتروني للتأكيد أو إشعارات العقود.
email.mime.text.MIMEText و email.mime.multipart.MIMEMultipart: يساعدان في صياغة محتوى البريد الإلكتروني بشكل منسق.
pywhatkit: يرسل رسائل واتساب تلقائياً للمستخدمين أو العملاء.
PIL (Pillow): يعالج الصور ويعرضها في صفحات العقارات.
os: يتعامل مع الملفات والمجلدات، مثل حفظ الصور أو قراءة المسارات.
datetime: ينشئ أرقام تعريف للعقارات بناءً على الوقت أو يحسب تاريخ/وقت الإرسال.
sqlite3فهي مكتبة بايثون للتعامل مع قواعد بيانات  يعني حفظ واسترجاع البيان] |
| [fill in] | [fill in] | [fill in] |

### Dependencies | المكتبات المستخدمة

| Package | Version | Purpose |
|---------|---------|---------|
| [fill in] | [fill in] | [fill in] |
| [fill in] | [fill in] | [fill in] |

<!-- Screenshot: Main screen of your project -->

<details>
<summary>Example: Student Health App</summary>

| Field | Value |
|-------|-------|
| **Project Title** | Student Health track er |
| **Project Type** | Web App |
| **Description** | A web application that helps students track  their daily water intake, sleep hours, and exercise. It provides personalized health tips based on the data entered. |
| **Target Users** | Students ages 12-18 |
| **Resolution / Platform** | Desktop + Mobile (responsive) |

### Tech Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Language** | Python | Backend logic |
| **Framework** | Streamlit | Web interface |
| **Database** | SQLite | Store user data |
| **Libraries** | pandas, matplotlib | Data analysis and charts |

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.28.0 | Web framework |
| pandas | 2.1.0 | Data manipulation |
| matplotlib | 3.8.0 | Charts and graphs |
| sqlite3 | built-in | Database |

</details>

---

## 2. Problem Statement | بيان المشكلة

<div class="arabic">
هنا تكتب المشكلة التي يحلها مشروعك — لماذا هذا المشروع مهم؟
</div>

### What problem does this project solve? | ما المشكلة التي يحلها هذا المشروع؟

[fill in — 2-3 sentences describing the real-world problem]

### Why does it matter? | لماذا هذا مهم؟

[fill in — who is affected by this problem? what happens if it's not solved?]

### How is it currently solved? | كيف تُحل المشكلة حالياً؟

[fill in — what alternatives exist? why are they not good enough?]

<details>
<summary>Example: Student Health App</summary>

### What problem does this project solve?

Many students don't track  their health habits — water intake, sleep, and exercise. They don't realize how these habits affect their energy, focus, and academic performance. There's no simple, fun tool designed specifically for students to monitor these habits.

### Why does it matter?

Poor health habits lead to low energy, difficulty concentrating, and long-term health problems. Students who track  their habits are more likely to make positive changes.

### How is it currently solved?

Students can use general health apps like MyFitnessPal or Apple Health, but these are designed for adults, not students. They're complex, overwhelming, and not culturally relevant to students in our region.

</details>

---

## 3. Technical Architecture | البنية التقنية

<div class="arabic">
هنا تشرح كيف مشروعك مبني من الداخل — هيكل الملفات والتقنيات المستخدمة
</div>

### Project Structure | هيكل المشروع

```
project-name/
├── main.py              # Entry point
├── templates/           # HTML templates (if web app)
│   ├── index.html
│   └── about.html
├── static/              # CSS, JS, images
│   ├── style.css
│   └── script.js
├── database/            # Database files
│   └── app.db
├── requirements.txt     # Python dependencies
└── README.md            # (optional)
```

[Replace the above with your actual project structure]

### Architecture Diagram | مخطط البنية

```
[User] → [Frontend] → [Backend] → [Database]
```

[Draw or describe your architecture — how do the parts connect?]

### Key Files | الملفات الرئيسية

| File | Purpose | Lines of Code |
|------|---------|:-------------:|
| [fill in] | [what it does] | [approximate] |
| [fill in] | [what it does] | [approximate] |
| [fill in] | [what it does] | [approximate] |

<details>
<summary>Example: Student Health App</summary>

### Project Structure

```
health-track er/
├── app.py               # Main Streamlit app
├── pages/
│   ├── 1_dashboard.py   # Dashboard with charts
│   ├── 2_log.py         # Daily habit logging
│   └── 3_tips.py        # Health tips page
├── data/
│   └── habits.db        # SQLite database
├── utils/
│   ├── database.py      # Database functions
│   └── charts.py        # Chart generation
├── images/
│   └── logo.png
├── requirements.txt
└── .streamlit/
    └── config.toml      # Streamlit config
```

### Architecture Diagram

```
[Student] → [Streamlit Browser] → [Python Backend] → [SQLite Database]
                    ↓
              [Charts (matplotlib)]
```

### Key Files

| File | Purpose | Lines of Code |
|------|---------|:-------------:|
| app.py | Main app entry point | ~50 |
| pages/2_log.py | Daily habit logging form | ~120 |
| utils/database.py | Database CRUD operations | ~80 |
| utils/charts.py | Chart generation functions | ~60 |

</details>

---

## 4. Features & User Flow | الميزات وتدفق المستخدم

<div class="arabic">
هنا تكتب قائمة الميزات + مخطط تدفق المستخدم عبر الشاشات
</div>

### Feature List | قائمة الميزات

| # | Feature | Description | Status |
|---|---------|-------------|:------:|
| 1 | [fill in] | [what it does] | ✅ / ⏳ / ❌ |
| 2 | [fill in] | [what it does] | ✅ / ⏳ / ❌ |
| 3 | [fill in] | [what it does] | ✅ / ⏳ / ❌ |
| 4 | [fill in] | [what it does] | ✅ / ⏳ / ❌ |
| 5 | [fill in] | [what it does] | ✅ / ⏳ / ❌ |

> Status: ✅ Complete | ⏳ In Progress | ❌ Not Started

### User Flow | تدفق المستخدم

```
                    ┌──────────────┐
                    │   LANDING    │
                    │    PAGE      │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │   LOGIN /    │
                    │   REGISTER   │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │   DASHBOARD  │
                    │  (main hub)  │
                    └──┬───┬───┬───┘
                       │   │   │
              ┌────────┘   │   └────────┐
              ▼            ▼            ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │ Screen 1 │ │ Screen 2 │ │ Screen 3 │
        │ (name)   │ │ (name)   │ │ (name)   │
        └──────────┘ └──────────┘ └──────────┘
```

[Replace with your actual user flow]

### Screen Reference | دليل الشاشات

| Screen | File / Route | Description | Transitions To |
|--------|-------------|-------------|----------------|
| [fill in] | [fill in] | [what user sees/does] | [where they can go] |
| [fill in] | [fill in] | [what user sees/does] | [where they can go] |
| [fill in] | [fill in] | [what user sees/does] | [where they can go] |

<details>
<summary>Example: Student Health App</summary>

### Feature List

| # | Feature | Description | Status |
|---|---------|-------------|:------:|
| 1 | Daily Logging | Students log water, sleep, and exercise | ✅ |
| 2 | Dashboard | Visual charts showing weekly/monthly trends | ✅ |
| 3 | Health Tips | Personalized tips based on logged data | ✅ |
| 4 | User Registration | Students create accounts to save data | ✅ |
| 5 | Export Data | Download health data as CSV | ⏳ |

### User Flow

```
                    ┌──────────────┐
                    │   LANDING    │
                    │  (welcome)   │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │   REGISTER   │
                    │   / LOGIN    │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │  DASHBOARD   │
                    │ (charts)     │
                    └──┬───┬───┬───┘
                       │   │   │
              ┌────────┘   │   └────────┐
              ▼            ▼            ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │   LOG    │ │   TIPS   │ │  EXPORT  │
        │ (daily)  │ │ (health) │ │ (data)   │
        └──────────┘ └──────────┘ └──────────┘
```

### Screen Reference

| Screen | File / Route | Description | Transitions To |
|--------|-------------|-------------|----------------|
| Landing | app.py | Welcome page with login/register | Register, Login |
| Register | pages/register.py | Create new account | Dashboard |
| Dashboard | pages/1_dashboard.py | Charts and weekly summary | Log, Tips, Export |
| Log | pages/2_log.py | Daily habit entry form | Dashboard |
| Tips | pages/3_tips.py | Personalized health advice | Dashboard |
| Export | pages/export.py | Download data as CSV | Dashboard |

</details>

---

## 5. UI/UX Design | تصميم واجهة المستخدم

<div class="arabic">
هنا تحط لقطات الشاشة + وصف التصميم البصري لمشروعك
</div>

### Screenshots | لقطات الشاشة

<!-- Screenshot: Landing page -->
**Landing Page**: [describe what the user sees]

<!-- Screenshot: Main dashboard -->
**Dashboard**: [describe what the user sees]

<!-- Screenshot: Key feature screen -->
**Key Feature**: [describe what the user sees]

<!-- Add more screenshots as needed -->

### Design System | نظام التصميم

| Element | Style |
|---------|-------|
| **Primary Color** | [e.g., #1a73e8 (blue)] |
| **Secondary Color** | [e.g., #34a853 (green)] |
| **Font** | [e.g., Inter, Arial, Cairo] |
| **Button Style** | [e.g., rounded, flat, gradient] |
| **Layout** | [e.g., sidebar navigation, top navbar, cards] |

### Responsive Design | التصميم المتجاوب

| Breakpoint | Layout | Tested? |
|------------|--------|:-------:|
| Desktop (1024px+) | [describe layout] | ☐ |
| Tablet (768-1024px) | [describe layout] | ☐ |
| Mobile (< 768px) | [describe layout] | ☐ |

<details>
<summary>Example: Student Health App</summary>

### Screenshots

<!-- Screenshot: Landing page -->
**Landing Page**: Clean welcome screen with app logo, "Welcome to Health track er!" message, and two buttons: "Login" and "Register". Blue and green color scheme.

<!-- Screenshot: Dashboard -->
**Dashboard**: Shows 3 charts — weekly water intake bar chart, sleep hours line chart, and exercise pie chart. Summary cards at the top show daily averages.

<!-- Screenshot: Log page -->
**Log Page**: Simple form with 3 input fields: Water (glasses), Sleep (hours), Exercise (minutes). Submit button saves to database.

### Design System

| Element | Style |
|---------|-------|
| **Primary Color** | #1a73e8 (blue) |
| **Secondary Color** | #34a853 (green) |
| **Font** | Inter |
| **Button Style** | Rounded, flat |
| **Layout** | Streamlit sidebar navigation |

### Responsive Design

| Breakpoint | Layout | Tested? |
|------------|--------|:-------:|
| Desktop (1024px+) | Full sidebar + main content area | ☐ |
| Tablet (768-1024px) | Collapsible sidebar | ☐ |
| Mobile (< 768px) | Stacked layout, full-width charts | ☐ |

</details>

---

## 6. Data Sources | مصادر البيانات

<div class="arabic">
هنا تكتب منين جبت الداتا — قاعدة بيانات، API، ملفات، أو داتا مكتوبة في الكود
</div>

### Data Sources | مصادر البيانات

| Source | Type | Description |
|--------|------|-------------|
| [fill in] | [Database / API / JSON / Static / User Input] | [what data it provides] |
| [fill in] | [fill in] | [fill in] |
| [fill in] | [fill in] | [fill in] |

### Database Schema | مخطط قاعدة البيانات

| Table | Columns | Description |
|-------|---------|-------------|
| [fill in] | [fill in] | [what it stores] |
| [fill in] | [fill in] | [what it stores] |

### External APIs (if any) | واجهات برمجة التطبيقات

| API | Purpose | Rate Limit |
|-----|---------|------------|
| [fill in] | [what it's used for] | [requests per day/hour] |

<details>
<summary>Example: Student Health App</summary>

### Data Sources

| Source | Type | Description |
|--------|------|-------------|
| habits.db | SQLite Database | Stores user accounts, daily logs |
| User Input | Form Submissions | Water, sleep, exercise data |
| Streamlit Session | Session State | Current logged-in user |

### Database Schema

| Table | Columns | Description |
|-------|---------|-------------|
| users | id, username, password_hash, created_at | User accounts |
| daily_logs | id, user_id, date, water, sleep, exercise | Daily habit entries |

### External APIs

| API | Purpose | Rate Limit |
|-----|---------|------------|
| None | All data is local | N/A |

</details>

---

## 7. Educational Content | المحتوى التعليمي

<div class="arabic">
هنا تكتب المحتوى التعليمي — ماذا يتعلم الطالب من هذا المشروع؟ كيف يتعلق بالمنهج؟
</div>

### Learning Objectives | أهداف التعلم

By the end of this project, the student will be able to:

1. [fill in — e.g., Build a full-stack web application with Python]
2. [fill in — e.g., Design and query a SQLite database]
3. [fill in — e.g., Create responsive UI with HTML/CSS]
4. [fill in — e.g., Implement user authentication]
5. [fill in]

### Cultural / Historical Context | السياق الثقافي / التاريخي

| Topic | Description |
|-------|-------------|
| [Theme of your project] | [How does it connect to culture, science, or society?] |
| [fill in] | [fill in] |

### Curriculum Alignment | التوافق مع المنهج

| Skill Area | What the Student Practices |
|------------|---------------------------|
| Problem Solving | [e.g., Breaking a real problem into code solutions] |
| Computational Thinking | [e.g., Data modeling, algorithms, abstraction] |
| Creativity | [e.g., UI design, user experience, visual storytelling] |
| Collaboration | [e.g., Pair programming, code reviews] |
| Technical Writing | [e.g., Documenting architecture and features] |

<details>
<summary>Example: Student Health App</summary>

### Learning Objectives

1. Build a full-stack web application using Python and Streamlit
2. Design and implement a SQLite database with CRUD operations
3. Create data visualizations with matplotlib
4. Implement user registration and session management
5. Apply UI/UX design principles for responsive layouts

### Cultural / Historical Context

| Topic | Description |
|-------|-------------|
| Student Health | Health track ing tools exist but none are designed specifically for students in our region — this project bridges that gap |
| Data Privacy | Students learn about handling personal health data responsibly |

### Curriculum Alignment

| Skill Area | What the Student Practices |
|------------|---------------------------|
| Problem Solving | Identifying a real student need and building a solution |
| Computational Thinking | Database design, data modeling, chart generation |
| Creativity | UI/UX design, color schemes, user flow |
| Collaboration | Working with team members on different features |
| Technical Writing | Documenting architecture and writing this template |

</details>

---

## 8. Marketing Plan | خطة تسويقية

> **Short version** — for full marketing plans, use the main Afro-Asian template.

<div class="arabic">
نسخة مختصرة — للخطط التسويقية الكاملة، استخدم القالب الرئيسي
</div>

### Target Audience | الجمهور المستهدف

- **Primary**: [who will use this — e.g., students ages 12-18]
- **Secondary**: [who else — e.g., teachers, parents, schools]
- **Tertiary**: [anyone else — e.g., health organizations, coding communities]

### Platforms | المنصات

- [e.g., Web browser (Chrome, Firefox, Edge)]
- [e.g., Mobile phone]
- [e.g., School computers]

### Promotion Ideas | أفكار ترويجية

1. [e.g., Share demo video on YouTube/TikTok]
2. [e.g., Present at school science fair]
3. [e.g., Post screenshots on class group]
4. [e.g., Submit to Afro-Asian Tech Forum competition]

<details>
<summary>Example: Student Health App</summary>

### Target Audience

- **Primary**: Students ages 12-18 who want to track  health habits
- **Secondary**: Teachers looking for health education tools
- **Tertiary**: School administrators interested in student wellness programs

### Platforms

- Web browser (desktop + mobile)
- School computer labs

### Promotion Ideas

1. Demo video on school YouTube channel
2. Present at end-of-semester exhibition
3. Post screenshots on school WhatsApp group
4. Submit to Afro-Asian Tech Forum — Educational Tools category

</details>

---

## 9. Student Worksheet | ورقة عمل الطالب

> **Instructions**: Copy this section into your own document and fill it in for YOUR project.

---

### My Project Information | معلومات مشروعي

**Student Name**: ___________________________

**Project Title**: ___________________________

**Date**: ___________________________

---

#### What is your project about? | عن ماذا يتحدث مشروعي؟

_______________________________________________
_______________________________________________

#### What problem does it solve? | ما المشكلة التي يحلها؟

_______________________________________________
_______________________________________________

---

### My Tech Stack | التقنيات المستخدمة

**My project type** (circle one): Web App / Desktop App / Mobile App / Python Script / Other: _______

**Technologies I used**:

| Category | Technology |
|----------|-----------|
| Language | |
| Framework | |
| Database | |
| Libraries | |

---

### My Screens | شاشات مشروعي

Draw or describe all the screens in your project:

| Screen Name | What the user sees/does | How to get here |
|-------------|------------------------|-----------------|
| | | |
| | | |
| | | |

---

### My Features | ميزات مشروعي

| Feature | What it does | Status |
|---------|-------------|:------:|
| | | ✅ / ⏳ / ❌ |
| | | ✅ / ⏳ / ❌ |
| | | ✅ / ⏳ / ❌ |

---

### My Data | بيانات مشروعي

**Where does data come from?**

_______________________________________________

**What data is stored?**

_______________________________________________

---

### What I Learned | ما تعلمته

1. The hardest part of building my project was: _________________________________

2. The most fun part of building my project was: _________________________________

3. If I had more time, I would add: _________________________________

4. One thing I would do differently: _________________________________

---

### Screenshot of My Project | لقطة شاشة من مشروعي

<!-- Paste a screenshot of your project running here -->

---

**Instructor Notes** | ملاحظات المدرس:

_______________________________________________
_______________________________________________

---

<div class="session-footer">
  <p>Techno Kids, Techno Future — Software Documentation Template</p>
  <p>Afro-Asian Tech Forum · Software Category · 2026</p>
</div>
