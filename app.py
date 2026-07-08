from graph import graph

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    result = graph.invoke({
        "question": question
    })

    print("\nAI:", result["final_answer"])