import streamlit as st

# Title and intro
st.set_page_config(page_title="ISKCON Rajkot Chatbot", page_icon="🛕")
st.title("🛕 ISKCON Rajkot Guest House Chatbot")
st.markdown("Type a keyword like `room`, `breakfast`, `address`, `contact`, `lunch`, etc.\nHare Krishna! 🙏")

# Keyword-based response dictionary
responses = {
    "hello": "Hare Krishna! Welcome to ISKCON Rajkot Guest House assistant. How may I serve you today? You can ask about room, food, contact or address.",

    "room": (
        "🛏️ Here are the available room options at ISKCON Rajkot Guest House:\n"
        "- 2 Beds: Non-AC ₹1000 / AC ₹1500\n"
        "- 3 Beds: Non-AC ₹1500 / AC ₹2000\n"
        "- 4 Beds: Non-AC ₹2000 / AC ₹2500\n"
        "All rooms are clean, peaceful, and spiritually vibrant for your divine stay 🙏"
    ),

    "checkin": (
        "🕙 Check-in and Check-out time is from 10 AM to 10 AM the next day.\n"
        "Please arrive on time for a smooth and peaceful stay."
    ),

    "address": (
        "📍 ISKCON Rajkot is located just 3 km from Rajkot Railway Station,\n"
        "and only a 2-minute walking distance from the main Dwarkadhish Mandir.\n"
        "A divine place full of bhakti and peace awaits you."
    ),

    "breakfast": (
        "🍛 *Breakfast Prasadam*: ₹80/- per person (Unlimited)\n"
        "Includes: Upma, Poha, Sambhar — Menu changes daily.\n"
        "Start your day with a sattvic and fulfilling meal 🌞"
    ),

    "lunch": (
        "🍽️ *Lunch (Rajbhog) Prasadam*: ₹160/- per person (Unlimited)\n"
        "Includes: Rice, Dal, Roti, Sabji, Papad, Pickle, Salad, Buttermilk, Sweet.\n"
        "All items are offered to Lord Krishna before serving 🙏"
    ),

    "dinner": (
        "🌙 *Dinner Prasadam*: ₹60/- per person (Unlimited)\n"
        "Includes: Khichdi, Papad, Pickle — simple and digestible meal before rest."
    ),

    "menu": (
        "📝 Note: Menu and pricing may vary depending on the day or special events.\n"
        "Please confirm in advance for updated prasadam details."
    ),

    "contact": (
        "📞 For Room Booking, Prasadam Inquiry or Darshan arrangements, please contact:\n"
        "Krishna Das Prabhuji – +91 88491 25949\n"
        "It will be our honor to serve you."
    ),

    "thank you": "You're welcome! May Lord Krishna bless you. Hare Krishna 🙏",

    "bye": "Hare Krishna! Thank you for connecting. Have a blissful day 🌸"
}

# Input box
user_input = st.text_input("🙏 Ask your question (like 'room', 'lunch', 'contact'):")

# Logic to generate response
if user_input:
    key = user_input.lower()
    if key in responses:
        st.success(responses[key])
    else:
        st.warning("Sorry, I didn't understand that. Try keywords like `room`, `lunch`, `contact`, `address`.")
