from services.rag_service import ask_question

if __name__ == "__main__":
    while True:
        q = input("Ask: ")
        if q.lower() == "exit":
            break
        answer = ask_question(q)
        print("\nAnswer:\n", answer)