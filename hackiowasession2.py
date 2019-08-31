span = 2

if span == 1:
    print('Hello')
elif span == 2:
    print('Howdy')
else:
    print('Greetings')


def func_with_no_args():
    return f'Hello world! {span}'

class someclass:

    def __init__(self, a):
        self.a = a

    def s(self):
        print(self.a)

    def convert_list_to_sent(self, sen):
        list = ''

        if len(sen) == 1:
            return sen[0]

        for i in range(len(sen)):
            if i == len(sen) - 1:
                list += 'and ' + sen[i]
            else:
                list += sen[i] + ', '
        return list


if __name__ == '__main__':
    print(func_with_no_args())

    foo = someclass(3)
    foo.s()

    print([1, 2] * 4)

    s = ['asd', 'ds', 'jgf', 'rgr']
    print('ds' not in s)
    a, *args = s
    print(a, args)

    tuple2 = (1, 2, 3)  # const list
    single_el_tuple = (1,)

    print(foo.convert_list_to_sent(s))

    assert foo.convert_list_to_sent(['ads', 'ad']) == 'ads, and ad'
