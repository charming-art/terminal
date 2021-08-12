# IO

Methods for IO.

<a name="load_json" href="#load_json">#</a> cm.**load_json**(*filename*)

Loads data from JSON file to dict object.

```JSON
// test_object.json
{
  "name": "Jack",
  "age": 10,
  "friends": ["Petter", "Tom"]
}
```

```JSON
// test_array.json
[
  { "name": "Peter", "age": 10 },
  { "name": "Tom", "age": 15 }
]

```

```py
import charming as cm

o = cm.load_json('../assets/files/test_object.json')
a = cm.load_json('../assets/files/test_array.json')

print(o, a)

# {'name': 'Jack', 'age': 10, 'friends': ['Petter', 'Tom']}
# [{'name': 'Peter', 'age': 10}, {'name': 'Tom', 'age': 15}]
```

<a name="load_csv" href="#load_csv">#</a> cm.**load_csv**(*filename*)

Loads data from CSV file to dict object.

```CSV
name, age, sex
Peter, 10, '男'
Yuki, 10, '女'
```

```py
import charming as cm

o = cm.load_csv('../assets/files/test.csv')

print(o)

# [{'name': 'Peter', ' age': ' 10', ' sex': " '男'"}, {'name': 'Yuki', ' age': ' 10', ' sex': " '女'"}]
```
