def func(**kwargs):
    for k,v in kwargs.items():
        print(f'{k}',{v})


d = {'name' : 'shivam' , 'age' :'27' , 'cl' :'8'}

func(**d)

