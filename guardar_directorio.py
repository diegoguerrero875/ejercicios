import pickle

def guardar_dicc(dicc_a_guardar, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dicc_a_guardar, file)

def cargar_dicc(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)