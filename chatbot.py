import sys
import time
import random
from datetime import datetime
import win32com.client  # Windows Vocal Engine
import ollama          # Local AI Brain Engine

class HarshilPremiumVoiceEngine:
    def __init__(self):
        self.bot_name = "AlphaCore Prime"
        self.user_name = "User"
        self.interaction_count = 0
        self.ollama_model = "harshil-ai:latest" 

        # Initialize the Voice Engine with Async capabilities
        try:
            self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
            self.async_flag = 1 
            
            # 🔥 VOICE UPGRADE UPGRADE PROTOCOL 🔥
            # Let's see what voices are installed on Harshil's laptop
            voices = self.speaker.GetVoices()
            
            # Let's search for a better voice (Zira is much clearer and nicer than the default)
            for index, voice in enumerate(voices):
                voice_name = voice.GetDescription()
                if "Zira" in voice_name or "Hazel" in voice_name:
                    self.speaker.Voice = voices.Item(index)
                    break
            
            # Let's adjust the speaking rate (0 is normal, 1 is slightly faster and less robotic)
            self.speaker.Rate = 1
            
        except Exception:
            self.speaker = None
            self.async_flag = 0

        print(f"📡 [SYSTEM]: High-Speed Streaming Active. Voice Profile Optimized.")
        print(f"🧠 [SYSTEM]: Connected to local model matrix: '{self.ollama_model}'")

        # --- FAST IF-ELSE KNOWLEDGE DATABASES ---
        self.programming_jokes = [
            "Why do programmers wear glasses? Because they can't C#!",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
            "There are 10 types of people: those who understand binary, and those who don't."
        ]
        
        self.tech_quotes = [
            "“Talk is cheap. Show me the code.” – Linus Torvalds",
            "“Simplicity is the soul of efficiency.” – Austin Freeman"
        ]

    def instant_talk_and_type(self, text: str):
        """Used for ultra-fast instant responses from the if-else matrix."""
        sys.stdout.write(f"[{self.bot_name}]: {text}\n")
        sys.stdout.flush()
        if self.speaker:
            self.speaker.Speak(text, self.async_flag)

    def process_message(self, user_stream: str):
        normalized = user_stream.lower().strip()
        self.interaction_count += 1

        # ============================================================
        # TRACK 1: INSTANT IF-ELSE CONDITIONAL LOGIC
        # ============================================================
        if normalized in ['terminate', 'exit', 'quit', 'bye', 'goodbye']:
            print(f"[{self.bot_name}]: Deconstructing active threads. Goodbye!")
            sys.exit(0)

        elif any(phrase in normalized for phrase in ["my name is harshil", "i'm harshil", "i am harshil", "boss", "creator"]):
            self.user_name = "Harshil Palande (Executive Creator)"
            self.instant_talk_and_type("Access token matched! Welcome back, Boss. Executive developer clearance granted.")

        elif "my name is" in normalized or "call me" in normalized:
            parts = user_stream.split()
            self.user_name = parts[-1].strip("!.,")
            self.instant_talk_and_type(f"System memory updated. Hello, {self.user_name}!")

        elif normalized in ['hello', 'hi', 'hey', 'greetings', 'yo']:
            self.instant_talk_and_type(f"Hello {self.user_name}! Systems nominal. What process shall we initiate?")

        elif "joke" in normalized or "laugh" in normalized:
            self.instant_talk_and_type(random.choice(self.programming_jokes))

        elif "quote" in normalized or "motivation" in normalized:
            self.instant_talk_and_type(random.choice(self.tech_quotes))

        elif any(phrase in normalized for phrase in ["time", "date", "day"]):
            formatted_time = datetime.now().strftime('%A, %B %d, %Y at %I:%M %p')
            self.instant_talk_and_type(f"The current local system time is: {formatted_time}")

        # ============================================================
        # TRACK 2: HIGH-SPEED STREAMING AI BRAIN
        # ============================================================
        else:
            try:
                sys.stdout.write(f"[{self.bot_name}]: ")
                sys.stdout.flush()
                
                stream = ollama.chat(
                    model=self.ollama_model,
                    messages=[
                        {
                            'role': 'system',
                            'content': f'You are AlphaCore Prime, a helpful desktop assistant. The user is named {self.user_name}. Keep your response to 1 short sentence.'
                        },
                        {'role': 'user', 'content': user_stream}
                    ],
                    stream=True  
                )
                
                full_response_text = ""
                
                for chunk in stream:
                    token = chunk['message']['content']
                    sys.stdout.write(token)
                    sys.stdout.flush()
                    full_response_text += token
                print() 
                
                if self.speaker and full_response_text.strip():
                    self.speaker.Speak(full_response_text, self.async_flag)
                    
            except Exception:
                self.instant_talk_and_type("Local neural stream pipeline failed. Please check Ollama background status.")

def main():
    engine = HarshilPremiumVoiceEngine()
    print("═" * 65)
    print("   ALPHALABS HIGH-SPEED HYBRID NEURAL INTERFACE PIPELINE v6.5 ")
    print("═" * 65)
    
    while True:
        try:
            print("-" * 65)
            user_input = input("User Console Interface > ")
            if not user_input.strip():
                continue
            engine.process_message(user_input)
        except (KeyboardInterrupt, SystemExit):
            print("\n\n⚠️ Shutting down active stream threads cleanly.")
            break

if __name__ == "__main__":
    main()