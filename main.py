import streamlit as st
import random

# List of greeting messages
greetings = [
    "Hello, World!",
    "Welcome to our app!",
    "Greetings, user!",
    "Nice to see you!",
    "How's your day going?",
    "Hello there!",
    "Hi, thanks for visiting!",
    "Welcome aboard!",
    "Glad you're here!",
    "Hey, what's up!"
]


def main():
    st.title("Random Greeting Generator")

    st.write("Click the button below to get a random greeting!")

    if st.button("Generate Greeting"):
        greeting = random.choice(greetings)
        st.header(greeting)


if __name__ == "__main__":
    main()