import streamlit as st

st.set_page_config(
    page_title="BMI & BMR Calculator",
    page_icon="💪",
    layout="wide"
)

st.markdown("""
<style>
html, body, .stApp {
    direction: rtl;
    text-align: right;
    background: #0b0f19;
    color: white;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
}

h1, h2, h3, p, label, span, div {
    direction: rtl !important;
    text-align: right !important;
}

.main-title {
    text-align: center !important;
    font-size: 48px;
    font-weight: 900;
}

.subtitle {
    text-align: center !important;
    font-size: 22px;
    color: #cbd5e1;
    margin-bottom: 30px;
}

.stButton > button {
    width: 100%;
    height: 38px;
    border-radius: 18px;
    background: linear-gradient(135deg, #22c55e, #16a34a);
    color: white;
    font-size: 24px;
    font-weight: 900;
    border: none;
}

.card {
    background: #f8fafc;
    color: #0f172a;
    border-radius: 24px;
    padding: 30px;
    min-height: 185px;
    border-bottom: 9px solid #22c55e;
    box-shadow: 0 18px 38px rgba(0,0,0,0.25);
}

.card.warning {
    border-bottom-color: #f97316;
}

.card.danger {
    border-bottom-color: #ef4444;
}

.card-title {
    font-size: 26px;
    font-weight: 900;
    color: #0f172a;
}

.card-value {
    font-size: 58px;
    font-weight: 900;
    color: #0f172a;
    margin-top: 10px;
}

.badge {
    display: inline-block;
    margin-top: 12px;
    padding: 8px 18px;
    border-radius: 999px;
    background: #bbf7d0;
    color: #008236;
    font-size: 22px;
    font-weight: 900;
}

.badge.warning {
    background: #fed7aa;
    color: #c2410c;
}

.badge.danger {
    background: #fecaca;
    color: #b91c1c;
}

.section {
    background: #111827;
    border: 1px solid #26344f;
    border-radius: 26px;
    padding: 30px;
    margin-top: 28px;
}

.recommend {
    background: #ecfdf5;
    color: #064e3b;
    border-right: 9px solid #10b981;
    border-radius: 24px;
    padding: 28px;
    font-size: 24px;
    font-weight: 800;
    line-height: 2;
}

.goal {
    background: #123524;
    color: #dcfce7;
    border: 1px solid #1f7a4d;
    border-radius: 14px;
    padding: 4px 14px;
    font-size: 20px;
    font-weight: 900;
    margin-top: 18px;
}

.timeline {
    background: #0f2f46;
    color: #dbeafe;
    border: 1px solid #2563eb;
    border-radius: 14px;
    padding: 10px 16px;
    font-size: 19px;
    font-weight: 800;
    margin-top: 12px;
    line-height: 1.8;
}

.scale-box {
    background: #111827;
    border: 1px solid #26344f;
    border-radius: 26px;
    padding: 30px;
    margin-top: 28px;
}

.bmi-track {
    position: relative;
    height: 24px;
    border-radius: 999px;
    background: linear-gradient(
        270deg,
        #facc15 0%,
        #facc15 17.3%,
        #22c55e 17.3%,
        #22c55e 42%,
        #f97316 42%,
        #f97316 61.5%,
        #ef4444 61.5%,
        #ef4444 100%
    );
    margin-top: 22px;
}

.bmi-marker {
    position: absolute;
    top: -9px;
    width: 9px;
    height: 42px;
    border-radius: 999px;
    background: white;
    box-shadow: 0 0 0 5px rgba(255,255,255,0.25);
}

.scale-labels {
    display: flex;
    flex-direction: row-reverse;
    margin-top: 16px;
    font-size: 18px;
    font-weight: 900;
    color: white;
}

.scale-labels span {
    text-align: center !important;
}

.scale-under {
    width: 17.3%;
    color: #facc15;
}

.scale-normal {
    width: 24.7%;
    color: #22c55e;
}

.scale-over {
    width: 19.5%;
    color: #f97316;
}

.scale-obese {
    width: 38.5%;
    color: #ef4444;
}

.plan-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 18px;
}

.plan-item {
    background: #0b1220;
    border: 1px solid #334155;
    border-radius: 20px;
    padding: 24px;
    font-size: 22px;
    font-weight: 700;
    color: #e5e7eb;
}

.plan-item strong {
    color: white;
    font-size: 24px;
}

.warning-box {
    background: #fff7ed;
    color: #9a3412;
    border-right: 9px solid #f97316;
    padding: 6px 14px;
    border-radius: 22px;
    font-size: 21px;
    font-weight: 800;
    margin-top: 28px;
}

hr {
    border: none;
    height: 1px;
    background: #26344f;
    margin: 42px 0;
}

@media (max-width: 900px) {
    .plan-grid {
        grid-template-columns: 1fr;
    }
}
</style>
""", unsafe_allow_html=True)


def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return weight / (height_m ** 2)


def calculate_bmr(weight, height_cm, age, gender):
    if gender == "זכר":
        return 10 * weight + 6.25 * height_cm - 5 * age + 5
    return 10 * weight + 6.25 * height_cm - 5 * age - 161


def bmi_category(bmi):
    if bmi < 18.5:
        return "תת משקל"
    elif bmi < 25:
        return "משקל תקין"
    elif bmi < 30:
        return "עודף משקל"
    return "השמנה"


def healthy_weight_range(height_cm):
    height_m = height_cm / 100
    return 18.5 * height_m ** 2, 24.9 * height_m ** 2


def activity_factor(level):
    return {
        "ללא פעילות": 1.2,
        "פעילות קלה": 1.375,
        "פעילות בינונית": 1.55,
        "פעילות גבוהה": 1.725,
        "פעילות גבוהה מאוד": 1.9
    }[level]


def bmi_style(category):
    if category == "משקל תקין":
        return "", "תקין"
    if category in ["תת משקל", "עודף משקל"]:
        return "warning", category
    return "danger", category


def bmi_marker_position(bmi):
    min_bmi = 14
    max_bmi = 40
    pos = ((bmi - min_bmi) / (max_bmi - min_bmi)) * 100
    return max(0, min(100, pos))


st.markdown('<div class="main-title">CaloriQ - Track Smart. Live Better.</div>', unsafe_allow_html=True)

st.markdown(
    '<div style="text-align:center;font-size:18px;color:#22c55e;font-weight:700;margin-top:-10px;margin-bottom:10px;">Created by BNamatix</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">הכנס נתונים וקבל המלצה לפי BMI, BMR ורמת פעילות</div>',
    unsafe_allow_html=True
)

with st.container(border=True):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("מין", ["זכר", "נקבה"])
        age = st.number_input("גיל", min_value=10, max_value=100, value=25)
        height = st.number_input("גובה בס״מ", min_value=120, max_value=230, value=175)

    with col2:
        weight = st.number_input("משקל בק״ג", min_value=30.0, max_value=250.0, value=70.0, step=0.5)
        activity = st.selectbox(
            "רמת פעילות",
            ["ללא פעילות", "פעילות קלה", "פעילות בינונית", "פעילות גבוהה", "פעילות גבוהה מאוד"]
        )
        daily_change = st.number_input(
            "כמה קלוריות ביום לדעתך תוכל לשמור כפער?",
            min_value=100,
            max_value=1500,
            value=300,
            step=50
        )

    calculate = st.button("חשב המלצה")

if calculate:
    bmi = calculate_bmi(weight, height)
    bmr = calculate_bmr(weight, height, age, gender)
    tdee = bmr * activity_factor(activity)

    category = bmi_category(bmi)
    min_weight, max_weight = healthy_weight_range(height)
    style, badge = bmi_style(category)
    marker = bmi_marker_position(bmi)

    if bmi >= 25:
        goal = "ירידה במשקל"
        target_weight = max_weight
        calories = tdee - 500
        plan_type = "גירעון קלורי מתון"
        weekly_change = "ירידה משוערת של 0.4–0.6 ק״ג בשבוע"
    elif bmi < 18.5:
        goal = "עלייה במשקל"
        target_weight = min_weight
        calories = tdee + 300
        plan_type = "עודף קלורי מתון"
        weekly_change = "עלייה הדרגתית ובריאה"
    else:
        goal = "שמירה על המשקל"
        target_weight = weight
        calories = tdee
        plan_type = "מאזן קלורי ניטרלי"
        weekly_change = "שמירה על המשקל הקיים"

    calories = max(calories, 1200)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h2>תוצאות</h2>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    c1.markdown(
        f'<div class="card {style}"><div class="card-title">BMI</div><div class="card-value">{bmi:.1f}</div><div class="badge {style}">{badge}</div></div>',
        unsafe_allow_html=True
    )

    c2.markdown(
        f'<div class="card"><div class="card-title">BMR</div><div class="card-value">{bmr:.0f}</div><div class="badge">קלוריות במנוחה</div></div>',
        unsafe_allow_html=True
    )

    c3.markdown(
        f'<div class="card"><div class="card-title">TDEE</div><div class="card-value">{tdee:.0f}</div><div class="badge">הוצאה יומית</div></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="scale-box">'
        f'<h2>סקאלת BMI</h2>'
        f'<div class="bmi-track"><div class="bmi-marker" style="right:{marker}%;"></div></div>'
        f'<div class="scale-labels">'
        f'<span class="scale-obese">השמנה</span>'
        f'<span class="scale-over">עודף משקל</span>'
        f'<span class="scale-normal">תקין</span>'
        f'<span class="scale-under">תת משקל</span>'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h2>המלצה אישית</h2>", unsafe_allow_html=True)

    st.markdown(
        f'<div class="recommend">'
        f'<b>מטרה מומלצת:</b> {goal}<br>'
        f'<b>טווח משקל תקין בין :</b> {min_weight:.1f} - {max_weight:.1f} ק״ג<br>'
        f'<b>משקל יעד מומלץ:</b> {target_weight:.1f} ק״ג<br>'
        f'<b>צריכת קלוריות יומית מומלצת:</b> {calories:.0f} קלוריות<br>'
        f'<b>סוג התוכנית:</b> {plan_type}'
        f'</div>',
        unsafe_allow_html=True
    )

    difference = target_weight - weight

    if difference < 0:
        goal_message = f"עליך לרדת בערך {abs(difference):.1f} ק״ג כדי להגיע ליעד המחושב."
    elif difference > 0:
        goal_message = f"עליך לעלות בערך {difference:.1f} ק״ג כדי להגיע ליעד המחושב."
    else:
        goal_message = "אתה כבר נמצא בטווח היעד המחושב."

    st.markdown(f'<div class="goal">{goal_message}</div>', unsafe_allow_html=True)

    kg_gap = abs(difference)
    calories_per_kg = 7500
    total_calorie_gap = kg_gap * calories_per_kg

    days_to_goal = 0
    months_to_goal = 0

    if kg_gap == 0:
        timeline_text = "אתה כבר נמצא בטווח היעד ולכן אין צורך בחישוב זמן הגעה."
    else:
        days_to_goal = total_calorie_gap / daily_change
        months_to_goal = days_to_goal / 30

        if goal == "ירידה במשקל":
            timeline_text = (
                f"פער של {kg_gap:.1f} ק״ג מהיעד שווה בערך "
                f"{total_calorie_gap:,.0f} קלוריות. "
                f"בגירעון יומי של כ־{daily_change} קלוריות, "
                f"הגעה ליעד צפויה בתוך כ־{days_to_goal:.0f} ימים "
                f"(בערך {months_to_goal:.1f} חודשים)."
            )
        elif goal == "עלייה במשקל":
            timeline_text = (
                f"פער של {kg_gap:.1f} ק״ג מהיעד שווה בערך "
                f"{total_calorie_gap:,.0f} קלוריות. "
                f"בעודף יומי של כ־{daily_change} קלוריות, "
                f"הגעה ליעד צפויה בתוך כ־{days_to_goal:.0f} ימים "
                f"(בערך {months_to_goal:.1f} חודשים)."
            )
        else:
            timeline_text = "אתה כבר נמצא בטווח היעד ולכן אין צורך בחישוב זמן הגעה."

    st.markdown(f'<div class="timeline">{timeline_text}</div>', unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h2>פירוט התוכנית</h2>", unsafe_allow_html=True)

    st.markdown(
        f'<div class="section">'
        f'<div class="plan-grid">'
        f'<div class="plan-item"><strong>צריכה יומית</strong><br>{calories:.0f} קלוריות ביום</div>'
        f'<div class="plan-item"><strong>כיוון התוכנית</strong><br>{plan_type}</div>'
        f'<div class="plan-item"><strong>קצב התקדמות</strong><br>{weekly_change}</div>'
        f'<div class="plan-item"><strong>מעקב מומלץ</strong><br>שקילה ומדידת היקפים פעם בשבוע</div>'
        f'<div class="plan-item"><strong>פער קלורי ליעד</strong><br>{total_calorie_gap:,.0f} קלוריות</div>'
        f'<div class="plan-item"><strong>זמן משוער ליעד</strong><br>{days_to_goal:.0f} ימים | {months_to_goal:.1f} חודשים</div>'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="warning-box">⚠️ המערכת מספקת הערכה כללית בלבד ואינה מחליפה ייעוץ רפואי או תזונאי מוסמך.</div>',
        unsafe_allow_html=True
    )
