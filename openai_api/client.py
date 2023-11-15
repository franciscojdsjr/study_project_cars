import openai


def get_car_ai_bio(model, brand, year):
    prompt = f'''
    Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 250 caracteres. Fale coisas especificas desse modelo de carro
    '''
    openai.api_key = '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'
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        max_tokens=1000,
    )
    return response['choices'][0]['text']