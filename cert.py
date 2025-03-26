import requests

def obtener_subdominios(domain):
    # URL base de crt.sh
    url = f"https://crt.sh/?q={domain}&output=json"
    
    # Hacer la solicitud GET para obtener los resultados en formato JSON
    response = requests.get(url)
    
    # Si la solicitud es exitosa, procesar los datos
    if response.status_code == 200:
        certificados = response.json()
        
        subdominios = set()  # Usamos un conjunto para evitar duplicados
        
        # Extraemos los subdominios de los certificados
        for certificado in certificados:
            nombre = certificado.get("name_value", "")
            # Si el nombre contiene más de un subdominio, lo agregamos
            if nombre:
                subdominios.update(nombre.split(","))
        
        return subdominios
    else:
        print(f"Error al obtener datos: {response.status_code}")
        return []

# Función principal
if __name__ == "__main__":
    dominio = input("Introduce el dominio (ejemplo.com): ").strip()
    
    subdominios = obtener_subdominios(dominio)
    
    if subdominios:
        print(f"Subdominios encontrados para {dominio}:")
        for subdominio in subdominios:
            print(subdominio)
    else:
        print("No se encontraron subdominios.")
