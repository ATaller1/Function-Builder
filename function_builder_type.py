num_of_inputs = input('How many inputs are there?')

def input_builder(num_of_inputs):
    '''(int -> list)
    Ask the user how many inputs they want to use and take in that many of inputs
    to build contract type
    '''

    num_of_inputs = int(num_of_inputs)
    global new_input
    new_input=[]
    for i in range(num_of_inputs):
        n=str(i+1)
        string_bldr=input('What is input number ' + str(n) + '? ')
        new_input.append(string_bldr)
    return new_input
    
input_builder(num_of_inputs)

num_of_outputs = input('How many outputs are there?')
def output_builder(num_of_outputs):
    '''(int -> list)
    Ask the user how many outputs they want to use and take in that many of inputs
    to build contract type
    '''
    num_of_outputs = int(num_of_outputs)
    global new_output
    new_output=[]
    for i in range(num_of_outputs):
        n=str(i+1)
        string_bldr=input('What is output number ' + str(n) + '? ')
        new_output.append(string_bldr)
    return new_output

output_builder(num_of_outputs)

num_of_examples = input("How many examples do you want to create?")

def example_builder(num_of_examples):
    '''create the examples to add to the contract'''
    num_of_examples = int(num_of_examples)
    global new_example
    global new_example_ans
    new_example = []
    new_example_ans = []
    for i in range(num_of_examples):
        n=str(i+1)
        string_bldr=input('What is example number ' + str(n) + '? ')
        new_example.append(string_bldr)
        string_bldr2=input('What is the answer to example number ' + str(n) + '?')
        new_example_ans.append(string_bldr2)
        i = i + 1
    return new_example, new_example_ans

example_builder(num_of_examples)

new_input=['str','str']
new_output=['str']
new_example = ['example_builder(1)','example_builder(2)']
new_example_ans = ['3','4']

def create_contract(new_input, new_output, new_example):
    '''create the contract for the new function'''
    sentence_beg = '""" (' 
    typecntrct_begin = ''
    typecntrct_end = ")"
    sentence_example = ">>> "
    sentence_answer = ''
    sentence_end ='"""'
    i = 0
    j = 0
    for i, item in enumerate(new_input):
        if i == 0:
            sentence_beg = sentence_beg + item
        else:
            sentence_beg = sentence_beg + ', ' + item 
    for i, item in enumerate(new_output):
        if i == 0:
            typecntrct_begin =  item 
        else:
            typecntrct_begin = typecntrct_begin +  ', ' + item
    for i, item in enumerate(new_example):
        items = new_example_ans[i]
        if i == 0:
            print (sentence_beg + ' -> ' + typecntrct_begin  + typecntrct_end)
            print (sentence_example + ("{}".format(new_example[i])) + '\n' + ("{}".format(new_example_ans[i])))
        else:
            print (sentence_example + ("{}".format(new_example[i])) + '\n' + ("{}".format(new_example_ans[i])))
        if i + 1 == len(new_example):
            print (sentence_end)

create_contract(new_input, new_output, new_example)