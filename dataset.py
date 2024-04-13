import pandas as pd

# datos
data = {
    'Título': ['El código Da Vinci', '1984', 'Harry Potter y la piedra filosofal', 'Cien años de soledad', 'Orgullo y prejuicio'],
    'Autor': ['Dan Brown', 'George Orwell', 'J.K. Rowling', 'Gabriel García Márquez', 'Jane Austen'],
    'Género': ['Misterio', 'Ciencia ficción', 'Fantasía', 'Realismo mágico', 'Romance clásico'],
    'Fecha de lectura': ['2023-04-15', '2023-05-20', '2023-06-10', '2023-07-05', '2023-08-20'],
    'Número de páginas': [480, 328, 332, 432, 432],
    'Opinión': ['Me encantó la trama intrigante', 'Una visión distópica fascinante', 'Una historia mágica que cautiva desde el principio', 'Una obra maestra que te transporta a otro mundo', 'Una historia de amor atemporal con personajes inolvidables']
}

df = pd.DataFrame(data)


print("DataFrame original:")
print(df)


print("\nLibros de género Fantasía:")
print(df[df['Género'] == 'Fantasía'])

# por número de páginas
print("\nLibros ordenados por número de páginas:")
print(df.sort_values(by='Número de páginas'))
