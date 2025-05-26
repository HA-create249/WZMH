

pip install openai nltk




import re
import openai
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import os

# config.py
OPENAI_API_KEY = "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"

# mental_health_knowledge.py

knowledge_base = {
    "depression": {
        "keywords": [
            "sad", "hopeless", "worthless", "tired", "empty", "guilt",  # English
            "حزين", "يائس", "تعب", "فارغ", "ذنب", "لا قيمة لي"  # Arabic
        ],
        "advice": {
            "en": "It sounds like you may be feeling symptoms of depression. Try to rest, talk to someone you trust, and if possible, connect with a mental health professional.",
            "ar": "يبدو أنك تعاني من أعراض الاكتئاب. حاول أن تستريح، وتحدث إلى شخص تثق به، وإذا أمكن تواصل مع مختص في الصحة النفسية."
        }
    },
    "anxiety": {
        "keywords": [
            "anxious", "worried", "panic", "afraid", "tense", "heart racing",
            "قلق", "خائف", "توتر", "ذعر", "تسارع القلب", "خوف"
        ],
        "advice": {
            "en": "You may be experiencing anxiety.\nYou're not alone.\nYou are not weak.\nHelp exists, even if far — don’t stop searching for it.\n Try grounding techniques like deep breathing or counting five things you see around you.",
            "ar": "قد تكون تعاني من القلق.\n لستَ وحدك\nنت لست ضعيفًا\nالمساعدة موجودة، وإن كانت بعيدة\n جرب تقنيات التنفس العميق أو ركز على خمسة أشياء تراها من حولك."
        }
    },
    "ptsd": {
        "keywords": [
            "flashbacks", "nightmares", "numb", "avoid", "trauma",
            "ذكريات مؤلمة", "كوابيس", "خدر", "تجنب", "صدمة"
        ],
        "advice": {
            "en": "These symptoms may relate to PTSD.\nYou are not weak — your brain is responding to extreme stress.\n Flashbacks, nightmares, numbness, or fear are common responses to trauma, not personal failures.\n Talking to someone about what you’ve been through can be healing.\nIf you're not ready to speak yet, that's okay. Even listening to others who went through something similar can help. Music, Quran recitations, or trauma-informed guided meditations can reduce panic and help the nervous system settle.",
            "ar": "قد تكون هذه الأعراض مرتبطة باضطراب ما بعد الصدمة.\nلست ضعيفًا — دماغك يتفاعل مع ضغط نفسي شديد.\n الكوابيس، الذكريات المؤلمة، الخدر، والخوف — كلها ردود فعل شائعة على الصدمة.\n الحديث مع شخص تثق به يمكن أن يساعدك في الشفاء.\nوإن لم تكن مستعدًا للكلام، يكفي أن تسمع تجارب من مروا بما مررت به. استمع للقرآن، للموسيقى الهادئة، أو لتأملات مصممة لضحايا الصدمة."
        }
    }
}



# OpenAI setup
openai.api_key = OPENAI_API_KEY

# Basic Arabic/English tokenizer
def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())  # Simple Arabic/English split

def detect_language(text):
    arabic_chars = re.findall(r'[\u0600-\u06FF]', text)
    return "ar" if len(arabic_chars) > 0 else "en"

def rule_based_response(user_input):
    tokens = tokenize(user_input)
    lang = detect_language(user_input)

    for disorder, data in knowledge_base.items():
        if any(word in tokens for word in data["keywords"]):
            return f"[{disorder.upper()}]\n{data['advice'][lang]}"
    return {
        "en": "I'm here to listen. Can you describe how you're feeling?",
        "ar": "أنا هنا لأستمع إليك. هل يمكنك أن تخبرني أكثر عن شعورك؟"
    }[lang]

def gpt_response(user_input):
    lang = detect_language(user_input)
    system_prompt = {
        "en": "You are a compassionate mental health assistant helping people in war zones. Respond with kindness.",
        "ar": "أنت مساعد في الصحة النفسية تقدم الدعم للأشخاص في مناطق الحرب. كن لطيفاً ومتفهماً."
    }[lang]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        max_tokens=200
    )
    return response["choices"][0]["message"]["content"].strip()

def main():

    print("🤖  دردشة الصحة النفسية لمساعدتك في التعامل مع آثار ما بعد الحرب(Mental Health Chatbot to help you treat with the aftermath of war)\nType 'exit' to quit.\n")
    print("أخبرني بما تشعر و أنا سأعطيك بعض النصائح للتعامل مع الموقف\nTell me what you feel, and Iwill give you some advice to manage your situation\n")
    mode = input("Choose mode: [1] Rule-based or [2] GPT-powered: ")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Bot: Take care. حافظ على نفسك ❤️")
            break

        if mode == "1":
            reply = rule_based_response(user_input)
        elif mode == "2":
            reply = gpt_response(user_input)
        else:
            reply = "Invalid mode. Please restart and choose 1 or 2."

        print("Bot:", reply)

if __name__ == "__main__":
    main()
