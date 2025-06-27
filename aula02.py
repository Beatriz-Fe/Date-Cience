import matplotlib.pyplot as plt

aluno = ['Amanda', 'Caio', 'Carla', 'Diego', 'Fernanda']
nota = [8.5, 6.0, 9.0, 7.5, 5.5]

plt.bar(aluno, nota, color=['#520120', '#08403E', '#706513', '#B57114', '#962B09'])

plt.title('Notas em Ciência de Dados')
plt.xlabel('Aluno')
plt.ylabel('Nota')

plt.show()
plt.savefig('exercicios/ex02.png')