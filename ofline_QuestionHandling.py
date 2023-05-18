
#error handling offline if chatGPT is not working
# these are the answers for the most popular 20 questions asked to bots
def process_question(question):
    question = question.lower()

    if "hello" in question or "hey" in question:
        return "hey there!"

    if "bye" in question:
        return "goodbye have a nice day!"

    if "name" in question:
        return "My name is ChatGPT."

    if "old" in question or "age" in question:
        return "As an AI, I don't have an age."

    if "from" in question or "origin" in question:
        return "I exist in the digital realm, so I don't have a physical location."

    if "purpose" in question or "goal" in question:
        return "My purpose is to assist and provide information."

    if "help" in question:
        return "I'll do my best to help you. What do you need assistance with?"

    if "weather" in question:
        return "I'm sorry, but as an AI, I don't have real-time access to weather information."

    if "joke" in question:
        return "Sure, here's a joke: Why don't scientists trust atoms? Because they make up everything!"

    if "eiffel tower" in question:
        return "The Eiffel Tower is approximately 330 meters tall."

    if "square root" in question:
        return "The square root of 144 is 12."

    if "convert" in question or ("miles" in question and "kilometers" in question):
        return "10 miles is approximately equal to 16.09 kilometers."

    if "pancakes" in question or "make" in question:
        return "To make pancakes, you'll need flour, eggs, milk, and a few other ingredients. Would you like a detailed recipe?"

    if "news" in question or "latest news" in question:
        return "I'm sorry, but as an AI, I don't have real-time access to news updates."

    if "play" in question or "song" in question:
        return "I'm sorry, but I can't play songs as I'm a text-based AI."

    if "translate" in question:
        return "The translation of 'hello' to French is 'bonjour'."

    if "meaning of life" in question:
        return "The meaning of life is subjective and can vary for each individual."

    if "reset" in question and "password" in question:
        return "To reset your password, you should visit the website or application where your account is registered and follow the password reset process."

    if "scientists" in question or "inventors" in question or "artists" in question:
        return "There have been many famous scientists, inventors, and artists throughout history. Some notable examples include Albert Einstein, Leonardo da Vinci, and Vincent van Gogh."

    if "symptoms" in question and "covid-19" in question:
        return "Common symptoms of COVID-19 include fever, cough, fatigue, loss of taste or smell, and difficulty breathing. However, it's important to consult official health sources for accurate and up-to-date information."
    if "language settings" in question or "change language" in question:
        return "To change the language settings, go to the settings menu of the application or device you're using and look for the language settings option."

    if "improve" in question and "credit score" in question:
        return "To improve your credit score, you can pay your bills on time, keep your credit card balances low, and maintain a healthy credit utilization ratio."

    if "recommend" in question and ("book" in question or "movie" in question or "tv show" in question):
        return "Sure! Could you please provide some preferences or genres that you're interested in?"

    if "start a small business" in question:
        return "The steps to start a small business may vary depending on your location and the type of business you want to establish. Generally, it involves conducting market research, creating a business plan, registering your business, and securing financing."

    if "clean" in question and ("coffee stain" in question or "carpet" in question):
        return "To clean a coffee stain from a carpet, you can blot the stain with a clean cloth or paper towel, then apply a mixture of mild detergent and water, followed by blotting with water to rinse."

    if "side effects" in question and "medication" in question:
        return "The specific side effects of a medication can vary. It's best to consult the medication's packaging, informational leaflet, or your healthcare provider for detailed information."

    if "delete" in question and ("social media account" in question or "account" in question):
        return "To delete your social media account, you typically need to go to the account settings or privacy settings section of the respective social media platform and look for the option to delete or deactivate your account."

    if "recipe" in question:
        return "Sure! Please provide the name of the dish you're looking for a recipe for."

    if "population of usa" in question:
        return "As of my knowledge cutoff in 2021, the population of the United States of America is approximately 331 million people."

    if "file" in question and "taxes" in question:
        return "To file your taxes, you generally need to gather your income and expense information, complete the necessary tax forms or use tax software, and submit your tax return to the appropriate tax authority."

    if "best way" in question and ("invest" in question or "stock market" in question):
        return "Investing in the stock market can be complex. It's generally recommended to educate yourself about investing, diversify your investments, and consider long-term strategies. Consulting with a financial advisor can also be beneficial."

    if "suggest" in question and ("workout routines" in question or "beginners" in question):
        return "For beginners, it's recommended to start with a combination of cardiovascular exercises, strength training, and flexibility exercises. It's important to start slowly, listen to your body, and gradually increase intensity."

    if "troubleshoot" in question and ("internet connection" in question or "internet" in question):
        return "To troubleshoot your internet connection, you can try restarting your modem and router, checking cable connections, ensuring your Wi-Fi signal is strong, or contacting your internet service provider for assistance."

    if "requirements" in question and ("driver's license" in question or "license" in question):
        return "The requirements for obtaining a driver's license vary depending on your location. Typically, it involves meeting the minimum"

    return "I'm sorry, I don't have information on that topic. Maybe you can ask my brother Google"