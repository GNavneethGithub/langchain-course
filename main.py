from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama


def main() -> None:
    prompt = PromptTemplate.from_template(
        """
        Answer the following question clearly and concisely:

        {information}

        Include:
        1. Practical key points.
        2. One inspirational quote.
        """.strip()
    )

    model = ChatOllama(
        model="gemma4:12b",
        temperature=0.7,
    )

    chain = prompt | model

    response = chain.invoke(
        {
            "information": (
                "How can someone reduce weight effectively "
                "while still satisfying hunger, using only vegan options?"
            )
        }
    )

    print(response.content)


if __name__ == "__main__":
    main()
