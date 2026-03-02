from find_similar import TokenText, find_similar


def chunks_to_text_list(chunks: list[dict])->list[str]:
    return [chunk['text'] for chunk in chunks]


def chunks_to_token_text(chunks: list[dict])->list[TokenText]:
    return [
        TokenText(
            chunk['text'],
            chunk_id=chunk['chunk_id']
        )
        for chunk in chunks
    ]


def token_texts_to_dict(token_texts: list[TokenText])->list[dict]:
    return [
        {
            'text': token_text.text,
            'score': token_text.cos,
            'chunk_id': token_text.chunk_id,
        }
        for token_text in token_texts
    ]


def search_chunks(
    chunks: list[dict],
    query: str,
    top_n: int = 5,
) -> list[dict]:
    texts = chunks_to_token_text(chunks)
    token_texts = find_similar(query, texts, count=top_n)

    print('START')

    print(query)

    print(len(texts))

    for token in token_texts:
        print(token.text)
        print(token.cos)
        print(token.chunk_id)

    result = token_texts_to_dict(token_texts)
    return result
