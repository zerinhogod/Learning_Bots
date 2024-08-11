from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="pause",
            description=f"Pausar música/vídeo atual.",
            thumb_url="https://graph.org/file/aabd3ff1f3a2806bbb98e.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="resume",
            description=f"Retornar música/vídeo atual.",
            thumb_url="https://graph.org/file/aabd3ff1f3a2806bbb98e.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="skip",
            description=f"Pular para próxima música/vídeo atual.",
            thumb_url="https://graph.org/file/aabd3ff1f3a2806bbb98e.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="end",
            description="Encerrar música/vídeo atual.",
            thumb_url="https://graph.org/file/aabd3ff1f3a2806bbb98e.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="shuffle",
            description="Modo ordem aleatória da playlist atual.",
            thumb_url="https://graph.org/file/aabd3ff1f3a2806bbb98e.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="loop",
            description="Repetir faixa atual.",
            thumb_url="https://graph.org/file/aabd3ff1f3a2806bbb98e.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
