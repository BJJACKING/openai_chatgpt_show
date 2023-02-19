# -*-coding:utf-8-*-


from config import *


def get_openai_txt(prompt):
    ans = openai.Completion.create(
        prompt=prompt,
        temperature=0,
        max_tokens=600,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        model=COMPLETIONS_MODEL
    )["choices"][0]["text"].strip(" \n")
    print("type(ans): ", type(ans))
    print(ans)
    return ans


if __name__ == "__main__":
    prompt = "你好"
    get_openai_txt(prompt)
