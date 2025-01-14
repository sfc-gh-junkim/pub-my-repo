import streamlit as st
import openai



# Streamlit 앱 UI
st.title("ChatGPT with Streamlit :balloon:")
st.subheader("OpenAI API를 활용한 대화형 앱")

# 사용자 입력
selected_model = st.selectbox("Select a model", ["gpt", "gpt-3.5", "gpt-3.5-turbo", "gpt-4-turbo"])
#user_input = st.text_input("Enter your message:")
user_input = st.text_area("Enter your message:", height=150)

if st.button("Send"):
    if user_input.strip():
        try:
            # ChatGPT API 호출
            response = openai.ChatCompletion.create(
                model=selected_model,  # 선택한 ChatGPT 모델
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            # 응답 출력
            chat_response = response['choices'][0]['message']['content']
            st.text_area("Response:", chat_response, height=200)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a message!")
