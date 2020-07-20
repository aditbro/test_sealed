from solution import load, store

test_cases = {
    'a=ab;d=c8\nln=21\n222=ool': [
        {
            'a': 'ab',
            'd': 'c8'
        },
        {
            'ln': '21'
        },
        {
            '222': 'ool'
        }
    ],
    '': {},
    'lns=123\nsad-ew=213;nm=20312': [
        {
            'lns': '123'
        },
        {
            'sad-ew': '213',
            'nm': '20312'
        }
    ],
    '\n\nsds=12321\n\nsadsa=2132;b=c': [
        {}, {},
        {'sds': '12321'},
        {}, {'sadsa': '2132', 'b': 'c'}
    ]
}

for case, ans in test_cases.items():
    load_result = load(case)
    store_result = store(ans)

    assert load_result == ans, print(load_result, ans)
    assert load(store_result) == ans, print(store_result, case)