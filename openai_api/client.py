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