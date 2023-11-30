import google.generativeai as palm

API_KEY = 'AIzaSyAc92AyCAM1fKno2fBtkVRwnWPrmF6kNMA'
palm.configure(api_key = API_KEY)

model_list = [_ for _ in palm.list_models()]
for model in model_list:
    print(model.name)

#Example 1 - Text Generation
model_id = 'models/text-bison-001'
prompt = '''
Write a marketing proposal to sell an ice cream product, limits the proposal to 50 words
'''

completion = palm.generate_text(
    model = model_id,
    prompt = prompt,
    temperature = 0.99, #the randomness of the output
    #the maximum length of the response
    max_output_tokens = 800,
    candidate_count = 2
 )

# completion.result
completion.candidates[0]['output']