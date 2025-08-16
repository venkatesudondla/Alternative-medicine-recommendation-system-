def get_response(user_input):
    user_input = user_input.lower()

    if "migraine" in user_input:
        return "Avoid bright lights, stay hydrated, eat healthy, and inhale turmeric steam."
    elif "headache" in user_input:
        return "Try ginger tea, peppermint oil, or acupressure for relief."
    elif "cold and cough" in user_input:
        return "Stay hydrated with warm fluids, rest well, and inhale steam."
    elif "cold" in user_input:
        return "Use tulsi tea, steam inhalation, or honey with lemon."
    elif "cough" in user_input:
        return "Drink warm fluids, rest, and use a humidifier if needed."
    elif "stomach pain" in user_input:
        return "Try bananas, stay hydrated, and use a hot water bag."
    elif "itching" in user_input:
        return "Use oatmeal baths, cool compresses, or aloe vera."
    elif "throat pain" in user_input:
        return "Gargle salt water, drink chamomile tea, and stay hydrated."
    elif "lower back pain" in user_input:
        return "Try gentle yoga, apply heat, and reduce stress."
    elif "diabetes" in user_input:
        return "Try fenugreek seeds, cinnamon tea, and bitter gourd juice."
    elif "pimples" in user_input:
        return "Use aloe vera, tea tree oil, and wash your face regularly."
    elif "dandruff" in user_input:
        return "Apply neem paste or use coconut oil with lemon."
    elif "hairfall" in user_input:
        return "Use onion juice, amla, or coconut oil."
    elif "open pores" in user_input:
        return "Apply ice cubes, tomato juice, or multani mitti mask."
    elif "black pores" in user_input:
        return "Steam your face weekly and use a clay mask."
    elif "knee pain" in user_input:
        return "Apply turmeric, hot compress, or do light stretching."
    elif "joint pain" in user_input:
        return "Use Epsom salt baths, essential oils, or turmeric tea."
    elif "heart pain" in user_input:
        return "Try deep breathing and hawthorn tea, but consult a doctor."
    elif "neck pain" in user_input:
        return "Use cold/heat therapy and do light neck exercises."
    elif "back pain" in user_input:
        return "Try child’s pose, turmeric milk, and warm compress."
    elif "toe pain" in user_input:
        return "Soak in Epsom salt water and rest your feet."
    elif "dizziness" in user_input:
        return "Stay hydrated, use ginger, and avoid sudden movements."
    elif "vomit" in user_input:
        return "Try ginger tea, lemon water, or mint leaves."
    elif "dark circles" in user_input:
        return "Apply cucumber slices or cold tea bags and sleep well."
    elif "black lips" in user_input:
        return "Use lemon-honey scrub or beetroot balm."
    elif "hormone" in user_input:
        return "Take flaxseeds, try ashwagandha, and reduce sugar."
    elif "pcod" in user_input:
        return "Try cinnamon, fenugreek, and spearmint tea."
    elif "cancer" in user_input:
        return "Include turmeric, green tea, leafy greens, and consult a doctor."
    elif "blindness" in user_input:
        return "Eat carrots, amla, omega-3s, and reduce screen time."
    elif "teeth pain" in user_input:
        return "Apply clove oil, rinse with saltwater, or use garlic paste."
    elif "kidney stones" in user_input:
        return "Try barley water, basil juice, and drink plenty of water."
    elif "gastric" in user_input:
        return "Use fennel seeds, ajwain, or buttermilk with hing."
    elif "elbow pain" in user_input:
        return "Apply ice, stretch, and massage with turmeric oil."
    elif "elbow" in user_input and "darkness" in user_input:
        return "Try lemon scrub or yogurt-turmeric paste."
    elif "obesity" in user_input:
        return "Start your day with lemon water, cinnamon tea, and regular exercise."

    return "I'm still learning. Please consult a doctor for serious symptoms."
