import chainlit  as cl
@cl.on_message
async def main(message: cl.Message):

 response = f" you said: {message.content}"

 await cl.Message(content=response).send()







# def main():
#     print("Hello from simple-chatbot!")


# if __name__ == "__main__":
#     main()
