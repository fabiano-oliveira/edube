import pickle
from dataclasses import dataclass

@dataclass
class Sample:
    name: str
    num: int

    def get_name(self):
        return 'Hello ' + self.name 


s = Sample("Fabiano", 10)

a_dict = dict()
a_dict['EUR'] = {'code':'Euro', 'symbol': '€'}
a_dict['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
a_dict['USD'] = {'code':'US dollar', 'symbol': '$'}
a_dict['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}

a_list = ['a', 123, [10, 100, 1000]]


with open('data.pckl', 'wb') as file_out:
    pickle.dump(a_dict, file_out)
    pickle.dump(a_list, file_out)
    pickle.dump(s, file_out)


with open('data.pckl', 'rb') as file_in:
    b_dict = pickle.load(file_in)
    b_list = pickle.load(file_in)
    b_sample = pickle.load(file_in)

print(type(b_dict))
print(b_dict)
print(type(b_list))
print(b_list)
print(type(b_sample))
print(b_sample)
print(b_sample.get_name())