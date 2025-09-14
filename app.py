import streamlit as st
from langchain.llms import OpenAI
from dotenv import load_dotenv

# 環境変数を読み込む
load_dotenv()

def get_advice(user_input, advisor_type):
    """
    LLMからのアドバイスを取得する関数。

    Args:
        user_input (str): ユーザーが入力した悩み。
        advisor_type (str): 選択された専門家の種類。

    Returns:
        str: LLMからのアドバイス。
    """
    # LangChainのLLMを初期化
    llm = OpenAI(temperature=0.7)

    # システムメッセージを選択値に応じて変更
    if advisor_type == "食事の専門家":
        system_message = "あなたは食事の専門家です。ユーザーの悩みに対して適切な食事のアドバイスを提供してください。"
    elif advisor_type == "運動の専門家":
        system_message = "あなたは運動の専門家です。ユーザーの悩みに対して適切な運動のアドバイスを提供してください。"
    else:
        system_message = "あなたは一般的なアドバイザーです。"

    # プロンプトを作成
    prompt = f"{system_message}\nユーザーの悩み: {user_input}"

    # LLMにプロンプトを渡して応答を取得
    response = llm(prompt)

    return response

def main():
    st.title("健康アドバイザーアプリ")

    # アプリの説明
    st.write("""
        ### アプリの概要
        このアプリは、以下の手順で使用できます：
        1. 専門家の種類を選択してください（食事の専門家または運動の専門家）。
        2. お悩みを入力フォームに記入してください。
        3. 送信ボタンを押すと、選択した専門家からのアドバイスが表示されます。

        **注意**: このアプリはAIを活用しており、提供されるアドバイスは参考情報としてご利用ください。
    """)

    # ラジオボタンで専門家の種類を選択
    advisor_type = st.radio("専門家の種類を選択してください:", ("食事の専門家", "運動の専門家"))

    # 入力フォーム
    user_input = st.text_input("お悩みを入力してください:")

    # 送信ボタン
    if st.button("送信"):
        if user_input:
            st.write(f"選択された専門家: {advisor_type}")
            st.write(f"入力された内容: {user_input}")
            advice = get_advice(user_input, advisor_type)
            st.write(f"アドバイス: {advice}")
        else:
            st.warning("お悩みを入力してください！")

if __name__ == "__main__":
    main()

