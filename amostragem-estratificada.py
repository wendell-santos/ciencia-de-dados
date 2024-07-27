{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "24a0dddd-080e-4d98-adc2-ce6335557b80",
   "metadata": {},
   "outputs": [],
   "source": [
    "#importação das bibliotecas: pandas para carregar arquivos .csv e train_test_split para divisão da base de dados (separar amostras)\n",
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "dbe8bcee-28f5-40c3-ae5c-30f01fef080b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "class\n",
       "Iris-setosa        50\n",
       "Iris-versicolor    50\n",
       "Iris-virginica     50\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#carregamento da base de dados e contagem de quantos registros existem por classe\n",
    "iris = pd.read_csv('iris.csv')\n",
    "iris['class'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "32741d4c-6357-4545-851f-cc2b79e8843c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#iris.iloc[:, 0:4]: buscamos somente os atributos previsores, ou seja, os dados sobre pétala e sétala de planta\n",
    "#iris.iloc[:, 4]: buscamos somente a classe, que é a espécie da planta (setosa, virginica ou versicolor)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9bc80f27-b614-4487-8db7-6ccdb849d38b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "deec8468-6963-4e3c-9445-847881ee22fa",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d77f064a-1c20-493b-b772-2c49a6c76a8f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
